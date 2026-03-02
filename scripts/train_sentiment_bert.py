"""
Fine-tuning BERT/RoBERTa pour classification sentiment politique.

Deux modes :
- Single-label (défaut) : une classe par exemple (CRITIQUE, HOSTILITE, IRONIE, SOUTIEN).
- Multi-label (--multi_label) : plusieurs classes possibles par exemple (BCE).
  Exploite les annotations complètes (ex. "CRITIQUE|HOSTILITE") au lieu du label dominant.

Usage:
    python scripts/train_sentiment_bert.py --preset best
    python scripts/train_sentiment_bert.py --multi_label --preset best
    python scripts/train_sentiment_bert.py --model camembertv2-base --preset best
"""
from __future__ import annotations

import argparse
import re
import json
import random
import sys
from pathlib import Path

# Chemins
_ROOT = Path(__file__).resolve().parent.parent
_BASE = _ROOT.parent
sys.path.insert(0, str(_ROOT))

try:
    from src.utils import BERT_ANNOTATIONS, BERT_ANNOTATIONS_MULTILABEL, MODEL_DIR
except ImportError:
    BERT_ANNOTATIONS = _ROOT / "data" / "bert_annotations_4class.csv"
    BERT_ANNOTATIONS_MULTILABEL = _ROOT / "data" / "bert_annotations_multilabel.csv"
    MODEL_DIR = _ROOT / "models" / "sentiment_camembert"

LABEL_COLS = ["lbl_critique", "lbl_hostilite", "lbl_ironie", "lbl_soutien"]

_DOCS = _ROOT / "docs"
_REPORT_MD = _DOCS / "BERT_FINETUNING_REPORT.md"
_METRICS_JSON = _DOCS / "bert_metrics.json"

LABELS = ["CRITIQUE", "HOSTILITE", "IRONIE", "SOUTIEN"]
LABEL2ID = {l: i for i, l in enumerate(LABELS)}
ID2LABEL = {i: l for l, i in LABEL2ID.items()}
N_LABELS = len(LABELS)

MODEL_ALIASES = {
    "camembert-base": "camembert-base",
    "camembert-base-ccnet": "almanach/camembert-base-ccnet",
    "camembertv2-base": "almanach/camembertv2-base",
    "camembertav2-base": "almanach/camembertav2-base",
    "xlm-roberta-base": "xlm-roberta-base",
}


_NLPAUG_AUG = None


def _augment_text(text: str, method: str = "swap") -> str:
    """Augmentation: synonym replacement (nlpaug) ou random swap (EDA light)."""
    global _NLPAUG_AUG
    if method == "nlpaug":
        try:
            if _NLPAUG_AUG is None:
                import nlpaug.augmenter.word as naw
                _NLPAUG_AUG = naw.ContextualWordEmbsAug(
                    model_path="camembert-base",
                    model_type="roberta",
                    action="substitute",
                    aug_p=0.1,
                    device="cpu",
                )
            augmented = _NLPAUG_AUG.augment(text)
            return augmented[0] if isinstance(augmented, list) else augmented
        except Exception:
            method = "swap"
    if method == "swap":
        words = text.split()
        if len(words) < 3:
            return text
        n_swaps = max(1, int(len(words) * 0.1))
        for _ in range(n_swaps):
            i, j = random.sample(range(len(words)), 2)
            words[i], words[j] = words[j], words[i]
        return " ".join(words)
    return text


def _get_augment_method():
    """Détecte si nlpaug est dispo et initialise le cache, sinon fallback swap."""
    global _NLPAUG_AUG
    try:
        import nlpaug.augmenter.word as naw
        _NLPAUG_AUG = naw.ContextualWordEmbsAug(
            model_path="camembert-base",
            model_type="roberta",
            action="substitute",
            aug_p=0.1,
            device="cpu",
        )
        return "nlpaug"
    except Exception:
        _NLPAUG_AUG = None
        return "swap"


def augment_train_data(df, text_col="text", label_col="label_id"):
    """Double le train set avec des exemples augmentés."""
    import pandas as pd

    method = _get_augment_method()
    augmented = []
    for _, row in df.iterrows():
        text = str(row[text_col])
        aug_text = _augment_text(text, method=method)
        augmented.append({text_col: aug_text, label_col: row[label_col]})
    aug_df = pd.DataFrame(augmented)
    return pd.concat([df, aug_df], ignore_index=True)


def get_llrd_param_groups(model, lr: float, decay: float = 0.95):
    """
    Layer-wise Learning Rate Decay.
    Classifier = lr, layer 11 = lr*decay, ..., layer 0 = lr*decay^12, embeddings = lr*decay^13.
    Supporte RoBERTa/CamemBERT et DeBERTa/CamemBERTav2.
    """
    base = getattr(model, "roberta", None) or getattr(model, "deberta", None) or getattr(model, "transformer", None)
    if base is None:
        return [{"params": [p for p in model.parameters() if p.requires_grad], "lr": lr}]

    encoder = getattr(getattr(base, "encoder", None), "layer", None)
    n_layers = len(encoder) if encoder is not None else 0

    # Grouper paramètres par couche
    by_layer = {}
    classifier_params = []
    emb_params = []

    for name, param in model.named_parameters():
        if not param.requires_grad:
            continue
        m = re.search(r"encoder\.layer\.(\d+)", name)
        if m:
            by_layer.setdefault(int(m.group(1)), []).append(param)
        elif "embeddings" in name:
            emb_params.append(param)
        else:
            classifier_params.append(param)

    param_groups = []
    if classifier_params:
        param_groups.append({"params": classifier_params, "lr": lr})
    for i in range(n_layers - 1, -1, -1):
        if i in by_layer:
            depth = n_layers - 1 - i
            param_groups.append({
                "params": by_layer[i],
                "lr": lr * (decay ** (depth + 1)),
            })
    if emb_params:
        param_groups.append({
            "params": emb_params,
            "lr": lr * (decay ** (n_layers + 1)),
        })
    return param_groups


def compute_kl_loss(logits1, logits2):
    """KL divergence bidirectionnelle entre 2 distributions (R-Drop)."""
    import torch.nn.functional as F
    p_loss = F.kl_div(
        F.log_softmax(logits1, dim=-1),
        F.softmax(logits2, dim=-1),
        reduction="batchmean",
    )
    q_loss = F.kl_div(
        F.log_softmax(logits2, dim=-1),
        F.softmax(logits1, dim=-1),
        reduction="batchmean",
    )
    return (p_loss + q_loss) / 2


def ce_loss_with_smoothing_and_weights(logits, labels, weight, smoothing=0.1):
    """CrossEntropy avec label_smoothing + class weights (reduction=none puis manual)."""
    import torch.nn.functional as F

    loss = F.cross_entropy(
        logits, labels, reduction="none", label_smoothing=smoothing
    )
    if weight is not None:
        loss = (loss * weight.to(logits.device)[labels]).mean()
    else:
        loss = loss.mean()
    return loss


def focal_loss(logits, labels, weight, gamma=2.0, alpha=None):
    """Focal loss pour classes déséquilibrées."""
    import torch.nn.functional as F

    probs = F.softmax(logits, dim=-1)
    pt = probs.gather(1, labels.unsqueeze(1)).squeeze(1)
    ce = F.cross_entropy(logits, labels, reduction="none")
    focal = (1 - pt) ** gamma * ce
    if alpha is not None:
        alpha = alpha.to(logits.device)
        focal = focal * alpha[labels]
    return focal.mean()


class RDropTrainer:
    """
    Trainer avec R-Drop, label smoothing, class weights, focal loss optionnel.
    Hérite du Trainer HuggingFace, override compute_loss.
    """

    def __init__(
        self,
        base_trainer_cls,
        rdrop_alpha: float = 0.2,
        label_smoothing: float = 0.1,
        class_weights=None,
        use_focal: bool = False,
        focal_gamma: float = 2.0,
        focal_alpha=None,
    ):
        self.rdrop_alpha = rdrop_alpha
        self.label_smoothing = label_smoothing
        self.class_weights = class_weights
        self.use_focal = use_focal
        self.focal_gamma = focal_gamma
        self.focal_alpha = focal_alpha or class_weights
        self._base_cls = base_trainer_cls

    def __call__(self, *args, **kwargs):
        base = self._base_cls
        rdrop_alpha = self.rdrop_alpha
        label_smoothing = self.label_smoothing
        class_weights = self.class_weights
        use_focal = self.use_focal
        focal_gamma = self.focal_gamma
        focal_alpha = self.focal_alpha

        class _RDropTrainer(base):
            def compute_loss(self, model, inputs, return_outputs=False, **kw):
                import torch
                import torch.nn.functional as F

                labels = inputs.pop("labels", None)
                weight = class_weights
                if weight is not None:
                    weight = weight.to(model.device)

                # Forward x2 (R-Drop)
                outputs1 = model(**inputs)
                outputs2 = model(**inputs)
                logits1, logits2 = outputs1.logits, outputs2.logits

                # CE loss (sur les 2 passes, moyenne)
                if use_focal:
                    if weight is None:
                        weight = torch.ones(N_LABELS, device=model.device)
                    loss1 = focal_loss(
                        logits1, labels, weight, gamma=focal_gamma, alpha=focal_alpha
                    )
                    loss2 = focal_loss(
                        logits2, labels, weight, gamma=focal_gamma, alpha=focal_alpha
                    )
                else:
                    if weight is None:
                        loss1 = F.cross_entropy(
                            logits1, labels,
                            reduction="mean",
                            label_smoothing=label_smoothing,
                        )
                        loss2 = F.cross_entropy(
                            logits2, labels,
                            reduction="mean",
                            label_smoothing=label_smoothing,
                        )
                    else:
                        loss1 = ce_loss_with_smoothing_and_weights(
                            logits1, labels, weight, smoothing=label_smoothing
                        )
                        loss2 = ce_loss_with_smoothing_and_weights(
                            logits2, labels, weight, smoothing=label_smoothing
                        )
                ce_loss = 0.5 * (loss1 + loss2)

                # KL divergence
                kl_loss = compute_kl_loss(logits1, logits2)
                loss = ce_loss + rdrop_alpha * kl_loss

                return (loss, outputs1) if return_outputs else loss

        return _RDropTrainer(*args, **kwargs)


def _run_multilabel(args, data_path: Path):
    """Pipeline d'entraînement multi-label (BCE)."""
    import pandas as pd
    import numpy as np
    import torch
    from sklearn.model_selection import train_test_split
    from transformers import (
        AutoTokenizer,
        AutoModelForSequenceClassification,
        TrainingArguments,
        Trainer,
        DataCollatorWithPadding,
        EarlyStoppingCallback,
    )
    from datasets import Dataset
    from sklearn.metrics import f1_score, accuracy_score

    df = pd.read_csv(data_path)
    for c in LABEL_COLS:
        if c not in df.columns:
            print(f"Colonne manquante: {c}. Exécuter prepare_annotations.py.")
            return 1
    df["labels"] = df[LABEL_COLS].values.tolist()
    df = df[["text", "labels"] + (["n_labels"] if "n_labels" in df.columns else [])]
    df["text"] = df["text"].fillna("").astype(str).str.strip()
    df = df[df["text"].str.len() > 0]
    if len(df) < 50:
        print("Pas assez d'exemples (min 50)")
        return 1

    strat_col = "n_labels" if "n_labels" in df.columns and df["n_labels"].nunique() > 1 else None
    try:
        train, rest = train_test_split(
            df, test_size=0.3, stratify=strat_col and df[strat_col], random_state=42
        )
        val, test = train_test_split(
            rest, test_size=0.5, stratify=strat_col and rest[strat_col], random_state=42
        )
    except Exception:
        train, rest = train_test_split(df, test_size=0.3, random_state=42)
        val, test = train_test_split(rest, test_size=0.5, random_state=42)

    if args.oversample:
        # Suréchantillonner les exemples avec IRONIE ou SOUTIEN (labels minoritaires)
        train = train.copy()
        for i, col in enumerate(LABEL_COLS):
            if col in ["lbl_ironie", "lbl_soutien"]:
                sub = train[train["labels"].apply(lambda r: (r[i] == 1) if isinstance(r, (list, np.ndarray)) else False)]
                if len(sub) > 0:
                    n_rep = min(4, max(2, int(len(train) / (len(sub) + 1))))
                    extra = pd.concat([sub] * (n_rep - 1), ignore_index=True)
                    train = pd.concat([train, extra], ignore_index=True)
        train = train.sample(frac=1, random_state=42).reset_index(drop=True)
        print(f"Après oversample: Train {len(train)} exemples")

    if args.augment:
        def _aug_row(r):
            txt = _augment_text(str(r["text"]), _get_augment_method())
            return {"text": txt, "labels": r["labels"]}
        aug_rows = [_aug_row(r) for _, r in train.iterrows()]
        aug_df = pd.DataFrame(aug_rows)
        train = pd.concat([train[["text", "labels"]], aug_df], ignore_index=True)
        print(f"Après augmentation: Train {len(train)} exemples")

    # Poids pos_weight BCE : pénaliser plus les faux négatifs sur labels rares (IRONIE, SOUTIEN)
    pos_counts = np.array([sum((r[i] if isinstance(r, (list, np.ndarray)) else 0) for r in train["labels"]) for i in range(N_LABELS)])
    neg_counts = len(train) - pos_counts
    pos_weight = (neg_counts / (pos_counts + 1e-6)).astype(np.float32)
    pos_weight_tensor = torch.tensor(pos_weight, dtype=torch.float)
    print(f"  pos_weight BCE (IRONIE/SOUTIEN renforcés): {dict(zip(LABELS, pos_weight.round(2)))}")

    print(f"Multi-label | Train: {len(train)} | Val: {len(val)} | Test: {len(test)}")
    n_multi = sum(1 for ls in train["labels"] if sum(ls) > 1)
    print(f"  Exemples multi-label (train): {n_multi}")

    model_name = MODEL_ALIASES.get(args.model, args.model)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    def tokenize(batch):
        return tokenizer(batch["text"], truncation=True, max_length=256, padding=False)

    def prepare_batch(batch):
        tok = tokenizer(
            batch["text"], truncation=True, max_length=256, padding=False
        )
        tok["labels"] = [[float(y) for y in r] for r in batch["labels"]]
        return tok

    def ds_from_df(d):
        ds = Dataset.from_pandas(d[["text", "labels"]])
        ds = ds.map(prepare_batch, batched=True, batch_size=32, remove_columns=["text"])
        ds.set_format("torch")
        return ds

    train_ds = ds_from_df(train)
    val_ds = ds_from_df(val)
    test_ds = ds_from_df(test)

    model = AutoModelForSequenceClassification.from_pretrained(
        model_name, num_labels=N_LABELS, id2label=ID2LABEL, label2id=LABEL2ID
    )
    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

    class MultilabelBCETrainer(Trainer):
        def __init__(self, pos_weight=None, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.pos_weight = pos_weight

        def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
            import torch.nn.functional as F
            labels = inputs.pop("labels")
            outputs = model(**inputs)
            pw = self.pos_weight.to(outputs.logits.device) if self.pos_weight is not None else None
            loss = F.binary_cross_entropy_with_logits(
                outputs.logits.float(),
                labels.float(),
                pos_weight=pw,
                reduction="mean",
            )
            return (loss, outputs) if return_outputs else loss

    def compute_metrics(eval_pred):
        logits, labels = eval_pred
        preds = (torch.sigmoid(torch.tensor(logits)) > 0.5).int().numpy()
        labels = np.array(labels)
        f1_per = []
        for i in range(N_LABELS):
            f1_per.append(f1_score(labels[:, i], preds[:, i], zero_division=0))
        subset_acc = (preds == labels).all(axis=1).mean()
        return {
            "f1_macro": float(np.mean(f1_per)),
            "subset_acc": float(subset_acc),
            **{f"f1_{LABELS[i].lower()}": float(f1_per[i]) for i in range(N_LABELS)},
        }

    out_dir = Path(args.output) if args.output else MODEL_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    train_out = out_dir / "camembert_finetuned"
    train_out.mkdir(parents=True, exist_ok=True)

    training_args = TrainingArguments(
        output_dir=str(train_out),
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch,
        per_device_eval_batch_size=16,
        learning_rate=args.lr,
        warmup_ratio=args.warmup_ratio,
        weight_decay=args.weight_decay,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="f1_macro",
        greater_is_better=True,
        logging_steps=25,
        report_to="none",
    )

    trainer = MultilabelBCETrainer(
        pos_weight=pos_weight_tensor,
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=4)],
    )

    print("Entraînement multi-label (BCE)...")
    trainer.train()

    preds = trainer.predict(test_ds)
    logits = preds.predictions
    y_pred = (torch.sigmoid(torch.tensor(logits)) > 0.5).int().numpy()
    y_true = np.array([[int(x) for x in r] for r in test["labels"].values])

    f1_per = [f1_score(y_true[:, i], y_pred[:, i], zero_division=0) for i in range(N_LABELS)]
    f1_macro = float(np.mean(f1_per))
    subset_acc = (y_pred == y_true).all(axis=1).mean()

    metrics = {
        "subset_accuracy": float(subset_acc),
        "f1_macro": float(f1_macro),
        "f1_per_class": {LABELS[i]: float(f1_per[i]) for i in range(N_LABELS)},
    }

    trainer.save_model(str(out_dir))
    tokenizer.save_pretrained(str(out_dir))

    _DOCS.mkdir(parents=True, exist_ok=True)
    with open(_METRICS_JSON, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    lines = [
        "# Rapport fine-tuning multi-label BERT",
        "",
        "## Métriques (test set)",
        "",
        f"- Subset accuracy: {subset_acc:.3f}",
        f"- F1 macro: {f1_macro:.3f}",
        "",
        "### F1 par classe (binaire)",
        "",
    ]
    for lbl, val in zip(LABELS, f1_per):
        lines.append(f"- {lbl}: {val:.3f}")
    lines.extend(["", "Source: train_sentiment_bert.py --multi_label", ""])

    Path(_REPORT_MD).write_text("\n".join(lines), encoding="utf-8")
    print(f"Modèle: {out_dir}")
    print(f"Rapport: {_REPORT_MD}")
    print(f"F1 macro: {f1_macro:.3f} | Subset acc: {subset_acc:.3f}")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Train BERT/RoBERTa sentiment classifier (SOTA pipeline)"
    )
    parser.add_argument(
        "--data",
        type=Path,
        default=None,
        help="Path to bert_annotations_4class.csv",
    )
    parser.add_argument(
        "--model",
        type=str,
        default="camembert-base",
        choices=list(MODEL_ALIASES.keys()),
        help="Model to use",
    )
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--lr", type=float, default=2e-5)
    parser.add_argument("--batch", type=int, default=16)
    parser.add_argument("--warmup_ratio", type=float, default=0.1)
    parser.add_argument("--weight_decay", type=float, default=0.01)
    parser.add_argument("--label_smoothing", type=float, default=0.1)
    parser.add_argument("--rdrop_alpha", type=float, default=0.2)
    parser.add_argument("--llrd_decay", type=float, default=0.95)
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--augment", action="store_true", help="Data augmentation")
    parser.add_argument("--focal", action="store_true", help="Focal loss")
    parser.add_argument("--oversample", action="store_true", help="Oversample minority classes (CRITIQUE, IRONIE)")
    parser.add_argument("--no_llrd", action="store_true", help="Disable LLRD")
    parser.add_argument(
        "--preset",
        choices=["default", "best"],
        default="default",
        help="Preset: best = augment + focal + oversample + 8 epochs",
    )
    parser.add_argument(
        "--multi_label",
        action="store_true",
        help="Mode multi-label : plusieurs classes par exemple (BCE). Utilise bert_annotations_multilabel.csv.",
    )
    args = parser.parse_args()

    if args.preset == "best":
        args.augment = True
        args.focal = True
        args.oversample = True
        args.epochs = 10
        args.rdrop_alpha = 0.1
        args.label_smoothing = 0.05
        print("Preset best: augment + focal + oversample, 10 epochs, rdrop=0.1")

    data_path = Path(args.data) if args.data else (BERT_ANNOTATIONS_MULTILABEL if args.multi_label else BERT_ANNOTATIONS)
    if not data_path.is_absolute():
        data_path = _ROOT / data_path
    if not data_path.exists():
        src = "prepare_annotations.py (produit bert_annotations_multilabel.csv)" if args.multi_label else "prepare_annotations.py"
        print(f"Données non trouvées. Exécuter d'abord: python scripts/{src}")
        return 1

    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split

    if args.multi_label:
        return _run_multilabel(args, data_path)

    df = pd.read_csv(data_path)
    df["label_id"] = df["label_id"].astype(int)
    df = df[df["label_id"].notna() & df["label_id"].isin(range(N_LABELS))]
    if len(df) < 50:
        print("Pas assez d'exemples (min 50)")
        return 1

    train, rest = train_test_split(
        df, test_size=0.3, stratify=df["label_id"], random_state=42
    )
    val, test = train_test_split(
        rest, test_size=0.5, stratify=rest["label_id"], random_state=42
    )

    if args.oversample:
        # Répliquer CRITIQUE et IRONIE pour équilibrer (minority oversampling)
        minor_classes = [0, 2]  # CRITIQUE, IRONIE
        parts = [train]
        for c in minor_classes:
            sub = train[train["label_id"] == c]
            if len(sub) > 0:
                n_repeat = max(2, int(train["label_id"].value_counts().max() / len(sub)))
                parts.append(pd.concat([sub] * (n_repeat - 1), ignore_index=True))
        train = pd.concat(parts, ignore_index=True).sample(frac=1, random_state=42).reset_index(drop=True)
        print(f"Après oversample: Train {len(train)} exemples")

    if args.augment:
        train = augment_train_data(train)
        print(f"Après augmentation: Train {len(train)} exemples")

    print(f"Train: {len(train)} | Val: {len(val)} | Test: {len(test)}")

    try:
        import torch
        from transformers import (
            AutoTokenizer,
            AutoModelForSequenceClassification,
            TrainingArguments,
            Trainer,
            DataCollatorWithPadding,
            EarlyStoppingCallback,
            get_linear_schedule_with_warmup,
        )
        from datasets import Dataset
        from sklearn.utils.class_weight import compute_class_weight
        from sklearn.metrics import (
            f1_score,
            accuracy_score,
            classification_report,
            confusion_matrix,
        )
    except ImportError as e:
        print("Erreur: pip install transformers torch datasets")
        print(e)
        return 1

    model_name = MODEL_ALIASES.get(args.model, args.model)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    def tokenize(batch):
        return tokenizer(
            batch["text"], truncation=True, max_length=256, padding=False
        )

    train_ds = Dataset.from_pandas(
        train[["text", "label_id"]].rename(columns={"label_id": "labels"})
    )
    val_ds = Dataset.from_pandas(
        val[["text", "label_id"]].rename(columns={"label_id": "labels"})
    )
    test_ds = Dataset.from_pandas(
        test[["text", "label_id"]].rename(columns={"label_id": "labels"})
    )

    train_ds = train_ds.map(tokenize, batched=True, batch_size=32).remove_columns(
        ["text"]
    )
    val_ds = val_ds.map(tokenize, batched=True, batch_size=32).remove_columns(
        ["text"]
    )
    test_ds = test_ds.map(tokenize, batched=True, batch_size=32).remove_columns(
        ["text"]
    )
    train_ds.set_format("torch")
    val_ds.set_format("torch")
    test_ds.set_format("torch")

    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

    model = AutoModelForSequenceClassification.from_pretrained(
        model_name,
        num_labels=N_LABELS,
        id2label=ID2LABEL,
        label2id=LABEL2ID,
    )

    cw = compute_class_weight(
        "balanced",
        classes=np.array(list(range(N_LABELS))),
        y=train["label_id"].astype(int).values,
    )
    # Renforcer les poids pour CRITIQUE (0) et IRONIE (2), classes difficiles
    cw = np.array(cw, dtype=np.float32)
    cw[0] *= 1.5  # CRITIQUE
    cw[2] *= 1.5  # IRONIE
    cw_tensor = torch.tensor(cw, dtype=torch.float)

    # Focal alpha = inverse des fréquences (comme class weight)
    focal_alpha = cw_tensor.clone() if args.focal else None

    def compute_metrics(eval_pred):
        logits, labels = eval_pred
        preds = np.argmax(logits, axis=-1)
        return {
            "accuracy": float(accuracy_score(labels, preds)),
            "f1_macro": float(
                f1_score(labels, preds, average="macro", zero_division=0)
            ),
        }

    out_dir = Path(args.output) if args.output else MODEL_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    train_out = out_dir / "camembert_finetuned"
    train_out.mkdir(parents=True, exist_ok=True)

    training_args = TrainingArguments(
        output_dir=str(train_out),
        num_train_epochs=args.epochs,
        per_device_train_batch_size=args.batch,
        per_device_eval_batch_size=16,
        learning_rate=args.lr,
        warmup_ratio=args.warmup_ratio,
        weight_decay=args.weight_decay,
        eval_strategy="epoch",
        save_strategy="epoch",
        load_best_model_at_end=True,
        metric_for_best_model="f1_macro",
        greater_is_better=True,
        logging_steps=25,
        report_to="none",
    )

    def create_llrd_optimizer_and_scheduler():
        if args.no_llrd:
            return None
        param_groups = get_llrd_param_groups(
            model, args.lr, decay=args.llrd_decay
        )
        optimizer = torch.optim.AdamW(
            param_groups,
            lr=args.lr,
            weight_decay=args.weight_decay,
        )
        try:
            n_gpus = max(1, torch.cuda.device_count())
        except Exception:
            n_gpus = 1
        steps_per_epoch = max(1, len(train_ds) // (args.batch * n_gpus))
        num_training_steps = steps_per_epoch * args.epochs
        num_warmup_steps = int(num_training_steps * args.warmup_ratio)
        scheduler = get_linear_schedule_with_warmup(
            optimizer,
            num_warmup_steps=num_warmup_steps,
            num_training_steps=num_training_steps,
        )
        return optimizer, scheduler

    optimizers_tuple = create_llrd_optimizer_and_scheduler()

    # RDropTrainer: 2 forwards, CE + label smoothing + weights, KL, focal optionnel
    rdrop_factory = RDropTrainer(
        Trainer,
        rdrop_alpha=args.rdrop_alpha,
        label_smoothing=args.label_smoothing,
        class_weights=cw_tensor,
        use_focal=args.focal,
        focal_gamma=2.0,
        focal_alpha=focal_alpha,
    )
    trainer = rdrop_factory(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=4 if args.epochs >= 8 else 3)],
        optimizers=optimizers_tuple if optimizers_tuple else None,
    )

    print("Entraînement...")
    trainer.train()

    preds = trainer.predict(test_ds)
    y_pred_ids = np.argmax(preds.predictions, axis=-1)
    y_pred = np.array([ID2LABEL[int(p)] for p in y_pred_ids])
    y_true = np.array([ID2LABEL[int(l)] for l in test["label_id"].values])

    acc = accuracy_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred, average="macro", labels=LABELS, zero_division=0)
    f1_per = f1_score(y_true, y_pred, average=None, labels=LABELS, zero_division=0)
    cm = confusion_matrix(y_true, y_pred, labels=LABELS)

    metrics = {
        "accuracy": float(acc),
        "f1_macro": float(f1),
        "f1_per_class": {LABELS[i]: float(f1_per[i]) for i in range(N_LABELS)},
        "confusion_matrix": cm.tolist(),
    }

    trainer.save_model(str(out_dir))
    tokenizer.save_pretrained(str(out_dir))

    _DOCS.mkdir(parents=True, exist_ok=True)
    with open(_METRICS_JSON, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    lines = [
        "# Rapport fine-tuning BERT/RoBERTa",
        "",
        "## Métriques (test set)",
        "",
        f"- Accuracy: {acc:.3f}",
        f"- F1 macro: {f1:.3f}",
        "",
        "### F1 par classe",
        "",
    ]
    for lbl, val in zip(LABELS, f1_per):
        lines.append(f"- {lbl}: {val:.3f}")
    lines.extend([
        "",
        "### Matrice de confusion",
        "",
        "| | " + " | ".join(LABELS) + " |",
        "|---" * (N_LABELS + 1) + "|",
    ])
    for i, lbl in enumerate(LABELS):
        lines.append(
            "| "
            + lbl
            + " | "
            + " | ".join(str(cm[i, j]) for j in range(N_LABELS))
            + " |"
        )
    lines.extend(["", "Source: train_sentiment_bert.py", ""])

    Path(_REPORT_MD).write_text("\n".join(lines), encoding="utf-8")
    print(f"Modèle: {out_dir}")
    print(f"Rapport: {_REPORT_MD}")
    print(f"F1 macro: {f1:.3f} | Accuracy: {acc:.3f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
