"""
Prépare un échantillon de 200 replies pour validation Cohen's kappa.

Usage:
    python scripts/prepare_kappa_sample.py

Produit:
    outputs/analysis_v3/annotation/kappa_sample_200.csv
    - 25 replies par candidat (stratifié)
    - Colonnes: reply_id, text, candidate_id, sentiment_gpt (label GPT-5 Nano), sentiment_human (VIDE, à remplir)
    - L'annotateur remplit sentiment_human (CRITIQUE | SOUTIEN | HOSTILITE | IRONIE)
    - Puis: python scripts/compute_cohens_kappa.py
"""
import pandas as pd
from pathlib import Path

LABELS = ["CRITIQUE", "SOUTIEN", "HOSTILITE", "IRONIE"]
N_PER_CANDIDATE = 25
TOTAL = 200  # 8 candidats × 25

_ROOT = Path(__file__).resolve().parent.parent
REPLIES_PATH = _ROOT / "final" / "data" / "replies_classified.csv"
OUT_CSV = _ROOT / "outputs" / "analysis_v3" / "annotation" / "kappa_sample_200.csv"


def _norm_sentiment(s: str) -> str | None:
    if pd.isna(s) or str(s).strip() == "":
        return None
    s = str(s).upper().replace("HOSTILITÉ", "HOSTILITE").replace("É", "E")
    if s in LABELS:
        return s
    if s in ("INCONNU", "UNKNOWN"):
        return None
    return None


def run():
    if not REPLIES_PATH.exists():
        print(f"Erreur: {REPLIES_PATH} introuvable. Placer replies_classified.csv dans final/data/")
        return

    df = pd.read_csv(REPLIES_PATH, nrows=100_000)
    if "candidate_id" not in df.columns:
        for c in ["target_candidate", "candidate"]:
            if c in df.columns:
                df["candidate_id"] = df[c]
                break
        else:
            print("Erreur: colonne candidate_id / target_candidate / candidate manquante")
            return

    sent_col = "sentiment"
    if sent_col not in df.columns:
        for c in ["sentiment_4class", "label", "annotation_4class"]:
            if c in df.columns:
                sent_col = c
                break
        else:
            print("Erreur: colonne sentiment manquante")
            return

    df["sentiment_gpt"] = df[sent_col].apply(_norm_sentiment)
    df = df[df["sentiment_gpt"].notna()].copy()

    text_col = "text" if "text" in df.columns else "reply_text"
    if text_col not in df.columns:
        print("Erreur: colonne text manquante")
        return

    out_rows = []
    for cand, g in df.groupby("candidate_id", dropna=False):
        n_avail = len(g)
        n_take = min(N_PER_CANDIDATE, n_avail)
        if n_take < 10:
            continue
        sample = g.sample(n=n_take, random_state=42)
        for _, row in sample.iterrows():
            rid = str(row.get("reply_id", row.get("id", "")))
            out_rows.append({
                "reply_id": rid,
                "text": row[text_col][:500] if pd.notna(row[text_col]) else "",
                "candidate_id": cand,
                "sentiment_gpt": row["sentiment_gpt"],
                "sentiment_human": "",  # À remplir manuellement
            })

    out_df = pd.DataFrame(out_rows)
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    out_df.to_csv(OUT_CSV, index=False, encoding="utf-8")
    print(f"Échantillon sauvegardé : {OUT_CSV}")
    print(f"  {len(out_df)} lignes, {out_df['candidate_id'].nunique()} candidats")
    print("\nInstructions:")
    print("  1. Ouvrir kappa_sample_200.csv")
    print("  2. Remplir la colonne sentiment_human (CRITIQUE | SOUTIEN | HOSTILITE | IRONIE)")
    print("  3. Exécuter: python scripts/compute_cohens_kappa.py")
