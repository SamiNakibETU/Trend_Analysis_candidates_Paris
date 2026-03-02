"""
Calcule le Cohen's kappa entre annotations humaines et labels GPT-5 Nano.

Usage:
    python scripts/compute_cohens_kappa.py

Lit:
    outputs/analysis_v3/annotation/kappa_sample_200.csv
    - Doit contenir sentiment_gpt et sentiment_human remplis

Écrit:
    docs/kappa_results.md (résumé)
    outputs/analysis_v3/annotation/kappa_confusion.csv (matrice)
"""
import pandas as pd
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
SAMPLE_CSV = _ROOT / "outputs" / "analysis_v3" / "annotation" / "kappa_sample_200.csv"
OUT_MD = _ROOT / "docs" / "kappa_results.md"
OUT_CSV = _ROOT / "outputs" / "analysis_v3" / "annotation" / "kappa_confusion.csv"

LABELS = ["CRITIQUE", "SOUTIEN", "HOSTILITE", "IRONIE"]


def _norm(s: str) -> str | None:
    if pd.isna(s) or str(s).strip() == "":
        return None
    s = str(s).upper().replace("HOSTILITÉ", "HOSTILITE").replace("É", "E")
    return s if s in LABELS else None


def run():
    if not SAMPLE_CSV.exists():
        print(f"Erreur: {SAMPLE_CSV} introuvable.")
        print("Exécuter d'abord: python scripts/prepare_kappa_sample.py")
        return

    df = pd.read_csv(SAMPLE_CSV)
    df["gpt"] = df["sentiment_gpt"].apply(_norm)
    df["human"] = df["sentiment_human"].apply(_norm)
    df = df[df["human"].notna() & df["gpt"].notna()]

    if len(df) < 50:
        print(f"Erreur: seulement {len(df)} réponses annotées. Minimum 50 requis.")
        return

    try:
        from sklearn.metrics import cohen_kappa_score, confusion_matrix, classification_report
    except ImportError:
        print("pip install scikit-learn")
        return

    kappa = cohen_kappa_score(df["human"], df["gpt"], labels=LABELS)
    cm = confusion_matrix(df["human"], df["gpt"], labels=LABELS)
    report = classification_report(df["human"], df["gpt"], labels=LABELS, output_dict=True)

    cm_df = pd.DataFrame(cm, index=LABELS, columns=LABELS)
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    cm_df.to_csv(OUT_CSV)
    print(f"Matrice de confusion : {OUT_CSV}")

    md = f"""# Cohen's kappa — Validation sentiment GPT vs humain

**Échantillon** : {len(df)} replies annotées manuellement (stratifié par candidat)

## Résultat

| Métrique | Valeur |
|----------|--------|
| **κ (Cohen's kappa)** | {kappa:.3f} |
| Interprétation | {"excellent" if kappa >= 0.75 else "substantial" if kappa >= 0.60 else "modéré" if kappa >= 0.40 else "fair" if kappa >= 0.20 else "poor"} |

## Matrice de confusion

Voir `outputs/analysis_v3/annotation/kappa_confusion.csv`

## F1 par classe (humain = référence)

| Classe | Precision | Recall | F1 |
|--------|-----------|--------|-----|
"""
    for lbl in LABELS:
        r = report.get(lbl, {})
        md += f"| {lbl} | {r.get('precision', 0):.2f} | {r.get('recall', 0):.2f} | {r.get('f1-score', 0):.2f} |\n"

    md += """
## Méthode

- Stratification : 25 replies par candidat (dans la mesure du possible)
- Classes : CRITIQUE, SOUTIEN, HOSTILITE, IRONIE
- Annotateur : humain unique
- Référence : labels GPT-5 Nano (classification initiale)
"""
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write(md)
    print(f"Résumé : {OUT_MD}")
    print(f"\nκ = {kappa:.3f} ({len(df)} paires)")
