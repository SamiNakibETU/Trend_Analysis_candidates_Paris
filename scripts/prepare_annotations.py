"""
Préparation des annotations pour fine-tuning CamemBERT.
Charge les données depuis plusieurs sources possibles, normalise et produit
bert_annotations_4class.csv.

Usage:
    python scripts/prepare_annotations.py
    python -c "from scripts.prepare_annotations import run; run()"
"""
import pandas as pd
from pathlib import Path
import sys

# Chemins
_ROOT = Path(__file__).resolve().parent.parent
_BASE = _ROOT.parent
A6_DATA = _BASE / "final" / "A6_bert_finetuning" / "data"
A6_OUT = _BASE / "final" / "A6_bert_finetuning" / "outputs"
ANNOTATIONS_LEGACY = _BASE / "outputs" / "analysis_v3" / "annotation"
OUT_CSV = _ROOT / "data" / "bert_annotations_4class.csv"
OUT_MULTILABEL_CSV = _ROOT / "data" / "bert_annotations_multilabel.csv"

LABELS = ["CRITIQUE", "HOSTILITE", "IRONIE", "SOUTIEN"]
LABEL_COLS = ["lbl_critique", "lbl_hostilite", "lbl_ironie", "lbl_soutien"]  # ordre = LABELS
LABEL2ID = {l: i for i, l in enumerate(LABELS)}
PRIORITY_ORDER = ["HOSTILITE", "IRONIE", "CRITIQUE", "SOUTIEN"]


def _resolve_multi_label(raw: str) -> str:
    """Règle label_dominant si multi-label : HOSTILITE > IRONIE > CRITIQUE > SOUTIEN."""
    if pd.isna(raw) or str(raw).strip() == "":
        return None
    s = str(raw).upper().replace("HOSTILITÉ", "HOSTILITE").replace("HOSTILITE", "HOSTILITE")
    parts = [p.strip() for p in s.replace("|", ",").replace(";", ",").split(",")]
    valid = [p for p in parts if p in LABELS]
    if not valid:
        return None
    for lbl in PRIORITY_ORDER:
        if lbl in valid:
            return lbl
    return valid[0]


def _load_mono_label() -> pd.DataFrame | None:
    p = A6_DATA / "annotations_mono_label.csv"
    if p.exists():
        df = pd.read_csv(p)
        if "label_dominant" in df.columns and "text" in df.columns:
            return df
    return None


def _load_a6_train_test() -> pd.DataFrame | None:
    train_p = A6_OUT / "A6_train.csv"
    test_p = A6_OUT / "A6_test.csv"
    if train_p.exists() and test_p.exists():
        train = pd.read_csv(train_p)
        test = pd.read_csv(test_p)
        return pd.concat([train, test], ignore_index=True)
    return None


def _load_bert_stratified() -> pd.DataFrame | None:
    p = ANNOTATIONS_LEGACY / "bert_annotation_stratified.csv"
    if p.exists():
        df = pd.read_csv(p, sep=";")
        if "annotation_4class" in df.columns and "text" in df.columns:
            df = df[df["annotation_4class"].notna() & (df["annotation_4class"].str.strip() != "")]
            if len(df) > 0:
                return df
    return None


def _parse_labels_multi(raw: str) -> set:
    """Parse labels_multi ou annotation_4class -> set des labels parmi CRITIQUE, HOSTILITE, IRONIE, SOUTIEN."""
    if pd.isna(raw) or str(raw).strip() == "":
        return set()
    s = str(raw).upper().replace("HOSTILITÉ", "HOSTILITE").replace("É", "E")
    parts = [p.strip() for p in s.replace("|", ",").replace(";", ",").split(",")]
    return {p for p in parts if p in LABELS}


def _df_to_multilabel(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convertit un DF avec labels_multi ou annotation_4class en format multi-label (colonnes binaires).
    """
    raw_col = "labels_multi" if "labels_multi" in df.columns else "annotation_4class"
    if raw_col not in df.columns:
        return None
    text_col = "text" if "text" in df.columns else "tweet"
    if text_col not in df.columns:
        return None

    rows = []
    for _, r in df.iterrows():
        labels_set = _parse_labels_multi(r[raw_col])
        if not labels_set:
            continue
        txt = r.get(text_col, "") or ""
        row = {
            "text": str(txt).strip(),
            "candidate_id": r.get("candidate_id", ""),
            "stratum": r.get("stratum", ""),
        }
        for i, lbl in enumerate(LABELS):
            row[LABEL_COLS[i]] = 1 if lbl in labels_set else 0
        row["n_labels"] = len(labels_set)
        row["labels_str"] = "|".join(sorted(labels_set))
        if row["text"]:
            rows.append(row)
    out = pd.DataFrame(rows)
    if out.empty:
        return None
    out["text"] = out["text"].astype(str).str.strip()
    out = out[out["text"].str.len() > 0]
    return out.reset_index(drop=True)


def _normalize_df(df: pd.DataFrame, source: str) -> pd.DataFrame:
    """Normalise vers text, label_dominant, label_id, candidate_id, stratum."""
    text_col = "text" if "text" in df.columns else "tweet" if "tweet" in df.columns else None
    if text_col is None:
        raise ValueError(f"Pas de colonne text/tweet dans {source}")

    label_col = "label_dominant" if "label_dominant" in df.columns else "annotation_4class"
    if label_col not in df.columns:
        raise ValueError(f"Pas de colonne label_dominant/annotation_4class dans {source}")

    out = pd.DataFrame()
    out["text"] = df[text_col].fillna("").astype(str).str.strip()
    out["label_raw"] = df[label_col].astype(str)
    out["label_dominant"] = out["label_raw"].apply(_resolve_multi_label)
    out["candidate_id"] = df["candidate_id"] if "candidate_id" in df.columns else ""
    out["stratum"] = df["stratum"] if "stratum" in df.columns else ""

    out = out[out["text"].str.len() > 0]
    out = out[out["label_dominant"].notna()]
    out = out[out["label_dominant"].isin(LABELS)]
    out = out[~out["label_dominant"].isin(["DEMANDE", "INCONNU"])]

    out["label_id"] = out["label_dominant"].map(LABEL2ID)
    return out[["text", "label_dominant", "label_id", "candidate_id", "stratum"]].reset_index(drop=True)


def run():
    df = None
    source = ""

    if _load_mono_label() is not None:
        raw = _load_mono_label()
        raw = raw[raw["label_dominant"].isin(LABELS)]
        if len(raw) >= 50:
            df = _normalize_df(raw, "annotations_mono_label")
            source = "A6 annotations_mono_label"

    if df is None and _load_a6_train_test() is not None:
        raw = _load_a6_train_test()
        raw = raw[raw["label_dominant"].isin(LABELS)]
        if len(raw) >= 50:
            df = _normalize_df(raw, "A6_train+A6_test")
            source = "A6_train + A6_test"

    if df is None and _load_bert_stratified() is not None:
        raw = _load_bert_stratified()
        raw["label_dominant"] = raw["annotation_4class"].apply(_resolve_multi_label)
        raw = raw[raw["label_dominant"].notna() & raw["label_dominant"].isin(LABELS)]
        if len(raw) >= 50:
            df = _normalize_df(raw, "bert_annotation_stratified")
            source = "bert_annotation_stratified"

    if df is None or len(df) < 50:
        print("Erreur: pas assez de données annotées (minimum 50).")
        print("  Vérifier: A6_data/annotations_mono_label.csv, A6_outputs/A6_train.csv, ou annotation/bert_annotation_stratified.csv")
        return 1

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_CSV, index=False)
    print(f"Écrit: {OUT_CSV} ({len(df)} exemples, source: {source})")
    print("  Distribution:", df["label_dominant"].value_counts().to_dict())

    # Sortie multi-label si la source a labels_multi / annotation_4class multi
    raw_for_ml = _load_a6_train_test() if A6_OUT.joinpath("A6_train.csv").exists() else None
    if raw_for_ml is not None and "labels_multi" in raw_for_ml.columns:
        ml_df = _df_to_multilabel(raw_for_ml)
        if ml_df is not None and len(ml_df) >= 50:
            ml_df.to_csv(OUT_MULTILABEL_CSV, index=False)
            n_multi = (ml_df["n_labels"] > 1).sum()
            print(f"Écrit: {OUT_MULTILABEL_CSV} ({len(ml_df)} exemples, {n_multi} multi-label)")
    elif raw_for_ml is not None and "annotation_4class" in raw_for_ml.columns:
        ml_df = _df_to_multilabel(raw_for_ml)
        if ml_df is not None and len(ml_df) >= 50:
            ml_df.to_csv(OUT_MULTILABEL_CSV, index=False)
            n_multi = (ml_df["n_labels"] > 1).sum()
            print(f"Écrit: {OUT_MULTILABEL_CSV} ({len(ml_df)} exemples, {n_multi} multi-label)")

    return 0


if __name__ == "__main__":
    sys.exit(run())
