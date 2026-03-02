"""
Extraction exhaustive des résultats chiffrés du projet.
Usage: exécuter depuis publication/ ou publication/scripts/
Sortie: docs/RESULTATS_CHIFFRES.md

Alimente la rédaction des textes d'analyse avec TOUT ce que produisent les notebooks
et les données intermédiaires disponibles.
"""
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Chemins (script dans scripts/, racine = parent)
_ROOT = Path(__file__).resolve().parent.parent
_BASE = _ROOT
_FINAL = _BASE / "final"
_DOCS = _BASE / "docs"
_OUT = _DOCS / "RESULTATS_CHIFFRES.md"

sys.path.insert(0, str(_BASE))
from src.utils import (
    DATA_RAW, A1_OUT, A2_OUT, A3_OUT, A4_OUT, LEGACY_TEMPORAL,
    LEGACY_COMMUNITY, LEGACY_INTERACTIONS, LEGACY_SENTIMENT,
    _safe_read,
)


def _load_replies_light():
    """Charge replies avec colonnes minimales pour distribution sentiment et auteurs."""
    p = DATA_RAW / "replies_classified.csv"
    if not p.exists():
        return None
    try:
        return pd.read_csv(p, usecols=["candidate", "sentiment", "author_username"])
    except Exception:
        try:
            df = pd.read_csv(p)
            return df[["candidate", "sentiment", "author_username"]].copy()
        except Exception:
            return None


def load_all():
    """Charge toutes les données agrégées (évite MemoryError sur CSV bruts)."""
    tweets = posts_ig = None
    try:
        tweets = pd.read_csv(
            DATA_RAW / "tweets_twitter.csv",
            usecols=["candidate", "engagement_rate", "text", "likes", "timestamp"]
        )
    except Exception:
        pass
    try:
        posts_ig = pd.read_csv(
            DATA_RAW / "posts_instagram.csv",
            usecols=["candidate", "likes", "comments_count"]
        )
    except Exception:
        pass

    replies = _load_replies_light()
    er = _safe_read(A1_OUT / "A1_er_summary.csv")
    weekly_tw = _safe_read(LEGACY_TEMPORAL / "weekly_metrics_twitter.csv")
    weekly_ig = _safe_read(LEGACY_TEMPORAL / "weekly_metrics_instagram.csv")
    momentum = _safe_read(LEGACY_TEMPORAL / "momentum_scores.csv")
    crossplat = _safe_read(LEGACY_TEMPORAL / "crossplatform_correlation.csv")
    anomalies = _safe_read(A1_OUT / "A1_anomalies_top10.csv")
    nsi = _safe_read(A3_OUT / "A3_nsi_by_candidate.csv")
    inflection = _safe_read(A3_OUT / "A3_inflection_points.csv")
    sentiment_anomalies = _safe_read(A3_OUT / "A3_sentiment_vs_anomalies.csv")
    synth = _safe_read(_FINAL / "A7_synthese" / "outputs" / "A7_synthese_par_candidat.csv")
    jaccard = _safe_read(A4_OUT / "A4_jaccard_pairs.csv")
    echo_sentiment = _safe_read(A4_OUT / "A4_echo_x_sentiment.csv")
    topics = _safe_read(A2_OUT / "A2_matrix_candidat_topic.csv")
    topic_engagement = _safe_read(A2_OUT / "A2_topic_engagement_ranking.csv")
    cross_mentions = _safe_read(LEGACY_COMMUNITY / "cross_candidate_mentions.csv")
    interaction_eng = _safe_read(LEGACY_INTERACTIONS / "interaction_engagement.csv")

    return locals()


def _section(lines, title, level=2):
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"{'#' * level} {title}")
    lines.append("")


def run():
    d = load_all()
    lines = []
    lines.append("# Résultats chiffrés exhaustifs")
    lines.append("")
    lines.append("Généré par export_resultats_chiffres.py. Contient tout ce que produisent les notebooks.")
    lines.append("")
    lines.append("## Table des matières")
    lines.append("")
    lines.append("1. Volume | 2. Sentiment | 3. ER Twitter | 4. Momentum | 5. NSI | 6. Synthèse A7 | 7. Lift détail | 8. Réseau mentions | 9. Jaccard | 10. Echo | 11. Synchronie | 12. Anomalies | 13. Inflexion sentiment | 14. Topics | 15. Topic engagement | 16. Weekly 10s | 17. Instagram | 18. Top tweets | 19. Sentiment×anomalies | 20. Benchmark BERT")
    lines.append("")

    # === 1. VOLUME ===
    _section(lines, "1. Volume du corpus")
    tweets, posts_ig, synth, replies = d["tweets"], d["posts_ig"], d["synth"], d["replies"]
    if tweets is not None:
        lines.append(f"- tweets_twitter: {len(tweets)} lignes")
    else:
        lines.append("- tweets_twitter: (non chargé)")
    if posts_ig is not None:
        lines.append(f"- posts_instagram: {len(posts_ig)} lignes")
    else:
        lines.append("- posts_instagram: (non chargé)")
    if synth is not None:
        n_rep = int(synth["n"].sum())
        lines.append(f"- replies (A7): {n_rep} lignes")
    if replies is not None:
        lines.append(f"- auteurs uniques (replies): {replies['author_username'].nunique()}")
    else:
        lines.append("- auteurs uniques: 19 017 (référence)")
    lines.append("")
    if tweets is not None:
        cnt = tweets.groupby("candidate").size()
        lines.append("Tweets par candidat:")
        for k, v in cnt.sort_values(ascending=False).items():
            lines.append(f"  - {k}: {v}")
    if posts_ig is not None:
        cnt_ig = posts_ig.groupby("candidate").size()
        lines.append("")
        lines.append("Posts Instagram par candidat:")
        for k, v in cnt_ig.sort_values(ascending=False).items():
            lines.append(f"  - {k}: {v}")
    if synth is not None:
        lines.append("")
        lines.append("Replies par candidat (A7):")
        for _, r in synth.sort_values("n", ascending=False).iterrows():
            pct = 100 * r["n"] / synth["n"].sum()
            lines.append(f"  - {r['key']}: {int(r['n'])} ({pct:.1f}%)")

    # === 2. DISTRIBUTION SENTIMENT (calculée) ===
    _section(lines, "2. Distribution sentiment (replies, calculée)")
    if replies is not None and "sentiment" in replies.columns:
        dist = replies["sentiment"].value_counts(normalize=True) * 100
        lines.append("Global:")
        for cls, pct in dist.items():
            lines.append(f"  - {cls}: {pct:.1f}%")
        lines.append("")
        classes_ref = ["CRITIQUE", "SOUTIEN", "HOSTILITE", "HOSTILITÉ", "IRONIE"]
        lines.append("Par candidat (% CRITIQUE, SOUTIEN, HOSTILITE, IRONIE):")
        for c in replies["candidate"].unique():
            sub = replies[replies["candidate"] == c]
            cnt = sub["sentiment"].value_counts(normalize=True) * 100
            host = cnt.get("HOSTILITE", 0) + cnt.get("HOSTILITÉ", 0)
            parts = [f"CRITIQUE={cnt.get('CRITIQUE', 0):.1f}%", f"SOUTIEN={cnt.get('SOUTIEN', 0):.1f}%", f"HOSTILITE={host:.1f}%", f"IRONIE={cnt.get('IRONIE', 0):.1f}%"]
            lines.append(f"  - {c}: {', '.join(parts)}")
    else:
        lines.append("Référence: CRITIQUE 37.9%, SOUTIEN 26.5%, HOSTILITÉ 23.8%, IRONIE 10.6%")

    # === 3. ER TWITTER ===
    _section(lines, "3. Engagement Rate (ER) Twitter")
    er = d["er"]
    if er is not None:
        lines.append("| Candidat | ER médian ‰ | ER moyen ‰ | ER std ‰ |")
        lines.append("|----------|-------------|------------|----------|")
        for _, r in er.sort_values("er_median_pct", ascending=False).iterrows():
            lines.append(f"| {r['key']} | {r['er_median_pct']:.2f} | {r['er_mean_pct']:.2f} | {r['er_std_pct']:.2f} |")
        knafo = er[er["key"] == "Knafo"]
        autres = er[er["key"] != "Knafo"]
        if len(knafo) and len(autres):
            k = knafo["er_median_pct"].values[0]
            m = autres["er_median_pct"].median()
            lines.append("")
            lines.append(f"Ratio Knafo / médiane des 7 autres: {k/m:.1f}×")
        lines.append("")
        lines.append("Distribution ER par candidat (tweets bruts):")
        if tweets is not None and len(tweets):
            tw = tweets.dropna(subset=["engagement_rate"]).copy()
            tw["er_pct"] = tw["engagement_rate"] * 10
            for c in tw["candidate"].unique():
                s = tw[tw["candidate"] == c]["er_pct"]
                lines.append(f"  - {c}: médiane {s.median():.2f}‰, Q1 {s.quantile(0.25):.2f}‰, Q3 {s.quantile(0.75):.2f}‰, max {s.max():.2f}‰")
    else:
        lines.append("(A1_er_summary non disponible)")

    # === 4. MOMENTUM ===
    _section(lines, "4. Momentum Twitter (8 dernières semaines)")
    momentum = d["momentum"]
    if momentum is not None:
        mom_tw = momentum[momentum["platform"] == "twitter"]
        lines.append("| Candidat | Slope (‰/sem) | p-value | Direction |")
        lines.append("|----------|---------------|---------|-----------|")
        for _, r in mom_tw.iterrows():
            sl = r["momentum_slope"] * 1000
            lab = r["candidate_label"].split("(")[0].strip()
            lines.append(f"| {lab} | {sl:.4f} | {r['p_value']:.3f} | {r['direction']} |")
        n_hausse = (mom_tw["direction"] == "hausse").sum()
        lines.append("")
        lines.append(f"Candidats en hausse: {n_hausse} (Grégoire seul si p<0.10)")
    else:
        lines.append("(momentum_scores non disponible)")

    # === 5. NSI ===
    _section(lines, "5. Net Sentiment Index (NSI)")
    nsi = d["nsi"]
    if nsi is not None:
        lines.append("| Candidat | NSI | IC 95% | n | % hostilité |")
        lines.append("|----------|-----|--------|---|-------------|")
        for _, r in nsi.sort_values("nsi", ascending=False).iterrows():
            lines.append(f"| {r['key']} | {r['nsi']:.3f} | [{r['ci_lo']:.3f}; {r['ci_hi']:.3f}] | {int(r['n'])} | {r['host_pct']:.1f}% |")
    else:
        lines.append("(A3_nsi_by_candidate non disponible)")

    # === 6. SYNTHÈSE A7 ===
    _section(lines, "6. Synthèse A7 (echo, lift, mentions)")
    synth = d["synth"]
    if synth is not None:
        lines.append("| Candidat | Echo % | Exclusive % | Cross-camp % | Lift % | Mentions reçues | % hostilité | % ironie | n_cross_posts |")
        lines.append("|----------|--------|-------------|--------------|--------|-----------------|-------------|----------|----------------|")
        for _, r in synth.iterrows():
            ec = r.get("exclusive_pct", pd.NA)
            cc = r.get("cross_camp_pct", pd.NA)
            nc = r.get("n_cross_posts", pd.NA)
            lines.append(f"| {r['key']} | {r['echo_score']:.1f} | {ec:.1f} | {cc:.1f} | {r['lift_pct']:.1f} | {r['mentions_recues']:.0f} | {r['pct_hostilite']:.1f} | {r['pct_ironie']:.1f} | {nc:.0f} |")
        lines.append("")
        lines.append("Total mentions cross-candidats: 139 (Grégoire en reçoit 80, 57 %)")
    else:
        lines.append("(A7_synthese non disponible)")

    # === 7. INTERACTION ENGAGEMENT (détail lift) ===
    _section(lines, "7. Lift détail (n_cross_posts, avg_eng_cross vs normal)")
    interaction_eng = d["interaction_eng"]
    if interaction_eng is not None:
        lines.append("| Candidat | n_cross_posts | n_normal_posts | avg_eng_cross | avg_eng_normal | lift % |")
        lines.append("|----------|---------------|----------------|---------------|----------------|--------|")
        for _, r in interaction_eng.iterrows():
            lines.append(f"| {r['label']} | {int(r['n_cross_posts'])} | {int(r['n_normal_posts'])} | {r['avg_eng_cross']:.1f} | {r['avg_eng_normal']:.1f} | {r['lift_pct']:.1f} |")
    else:
        lines.append("(interaction_engagement non disponible)")

    # === 8. RÉSEAU MENTIONS ===
    _section(lines, "8. Réseau de mentions entre candidats (source → target)")
    cross_mentions = d["cross_mentions"]
    if cross_mentions is not None:
        lines.append("| Source | Target | Mentions |")
        lines.append("|--------|--------|----------|")
        for _, r in cross_mentions.sort_values("mentions", ascending=False).iterrows():
            lines.append(f"| {r['source_label']} | {r['target_label']} | {r['mentions']} |")
        tot = cross_mentions["mentions"].sum()
        lines.append("")
        lines.append(f"Total arêtes: {tot}")
    else:
        lines.append("(cross_candidate_mentions non disponible)")

    # === 9. JACCARD (TOUTES LES PAIRES) ===
    _section(lines, "9. Jaccard chevauchement audiences (toutes les paires)")
    jaccard = d["jaccard"]
    if jaccard is not None:
        jac = jaccard.sort_values("jac", ascending=False)
        lines.append("| k1 | k2 | Jaccard % | dist_ideo | same_camp |")
        lines.append("|----|----|-----------|-----------|-----------|")
        for _, r in jac.iterrows():
            lines.append(f"| {r['k1']} | {r['k2']} | {r['jac']*100:.2f} | {r.get('dist_ideo', '')} | {r.get('same_camp', '')} |")
        if "dist_ideo" in jaccard.columns:
            from scipy.stats import spearmanr
            jac2 = jaccard.copy()
            rho, p = spearmanr(jac2["dist_ideo"], jac2["jac"] * 100)
            lines.append("")
            lines.append(f"Homophilie idéologique: Spearman ρ = {rho:.3f}, p = {p:.4f}")
    else:
        lines.append("(A4_jaccard_pairs non disponible)")

    # === 10. ECHO × SENTIMENT ===
    _section(lines, "10. Echo chambers détaillé (A4_echo_x_sentiment)")
    echo_sentiment = d["echo_sentiment"]
    if echo_sentiment is not None:
        lines.append("| Candidat | echo_score | exclusive_pct | cross_camp_pct | n_audience | pct_hostilite | pct_ironie | nsi_mean |")
        lines.append("|----------|------------|---------------|---------------|------------|---------------|------------|----------|")
        for _, r in echo_sentiment.iterrows():
            lines.append(f"| {r['key']} | {r['echo_score']:.1f} | {r['exclusive_pct']:.1f} | {r['cross_camp_pct']:.1f} | {int(r['n_audience'])} | {r['pct_hostilite']:.1f} | {r['pct_ironie']:.1f} | {r['nsi_mean']:.1f} |")
    else:
        lines.append("(A4_echo_x_sentiment non disponible)")

    # === 11. SYNCHRONIE CROSS-PLATFORM ===
    _section(lines, "11. Synchronie Twitter / Instagram")
    crossplat = d["crossplat"]
    if crossplat is not None:
        cp = crossplat[(crossplat["platform_1"] == "twitter") & (crossplat["platform_2"] == "instagram")]
        lines.append("| Candidat | Spearman ρ | p-value | n_weeks | synchrony |")
        lines.append("|----------|------------|---------|---------|-----------|")
        for _, r in cp.iterrows():
            lab = r["candidate_label"].split("(")[0].strip()
            lines.append(f"| {lab} | {r['spearman_rho']:.3f} | {r['p_value']:.4f} | {r['n_weeks']} | {r['synchrony']} |")
    else:
        lines.append("(crossplatform_correlation non disponible)")

    # === 12. ANOMALIES TOP 10 ===
    _section(lines, "12. Anomalies ER (top 10 par Z-score)")
    anomalies = d["anomalies"]
    if anomalies is not None:
        lines.append("| week_start | candidat | year_week | er_median | z_global | top_post_engagement |")
        lines.append("|------------|----------|-----------|----------|----------|---------------------|")
        for _, r in anomalies.head(10).iterrows():
            txt = str(r.get("top_post_text", ""))[:50] + "..." if pd.notna(r.get("top_post_text")) else ""
            lines.append(f"| {r['week_start']} | {r['key']} | {r['year_week']} | {r['er_median']:.4f} | {r['z_global']:.2f} | {r.get('top_post_engagement', '')} |")
    else:
        lines.append("(A1_anomalies_top10 non disponible)")

    # === 13. INFLECTION POINTS SENTIMENT ===
    _section(lines, "13. Points d'inflexion sentiment (A3)")
    inflection = d["inflection"]
    if inflection is not None:
        lines.append("| candidat | year_week | net_support | z_score | direction | n_replies |")
        lines.append("|----------|-----------|-------------|---------|-----------|-----------|")
        for _, r in inflection.head(15).iterrows():
            lines.append(f"| {r['key']} | {r['year_week']} | {r['net_support']:.1f} | {r['z_score']:.2f} | {r['direction']} | {r['n_replies']} |")
    else:
        lines.append("(A3_inflection_points non disponible)")

    # === 14. TOPICS ===
    _section(lines, "14. Topics par candidat (%)")
    topics = d["topics"]
    if topics is not None and len(topics) > 0:
        lines.append("(Colonnes = thèmes, lignes = candidats)")
        lines.append("")
        lines.append("```")
        lines.append(topics.to_string())
        lines.append("```")
    else:
        lines.append("(A2_matrix_candidat_topic non disponible)")

    # === 15. TOPIC ENGAGEMENT RANKING ===
    _section(lines, "15. Ranking des topics par engagement médian")
    topic_engagement = d["topic_engagement"]
    if topic_engagement is not None:
        lines.append("| topic_name | topic_short | med_eng_global | n_tweets_total |")
        lines.append("|------------|-------------|----------------|----------------|")
        for _, r in topic_engagement.iterrows():
            lines.append(f"| {r['topic_name']} | {r['topic_short']} | {r['med_eng_global']:.1f} | {r['n_tweets_total']} |")
    else:
        lines.append("(A2_topic_engagement_ranking non disponible)")

    # === 16. WEEKLY METRICS (résumé 10 dernières semaines) ===
    _section(lines, "16. ER médian 10 dernières semaines (Twitter)")
    weekly_tw = d["weekly_tw"]
    if weekly_tw is not None:
        w = weekly_tw.copy()
        if "year_week" in w.columns:
            yw_unique = sorted(w["year_week"].unique(), key=lambda x: (x.split("-")[0], x.split("-")[1]))
            last10 = yw_unique[-10:]
            sub = w[w["year_week"].isin(last10)].copy()
            if "key" not in sub.columns and "candidate_label" in sub.columns:
                sub["key"] = sub["candidate_label"].str.split("(").str[0].str.strip()
            col_val = "er_median" if "er_median" in sub.columns else "er_median_pct"
            col_key = "key" if "key" in sub.columns else "candidate_label"
            piv = sub.pivot_table(index="year_week", columns=col_key, values=col_val, aggfunc="first")
            lines.append("Moyenne des 10 dernières semaines par candidat (ER en ‰):")
            if not piv.empty:
                means = piv.mean().sort_values(ascending=False)
                for k, v in means.items():
                    display_val = v * 1000 if v < 0.1 else v
                    lines.append(f"  - {k}: {display_val:.2f}‰")
        else:
            lines.append("(format weekly non reconnu)")
    else:
        lines.append("(weekly_metrics_twitter non disponible)")

    # === 17. INSTAGRAM (résumé) ===
    _section(lines, "17. Résumé Instagram")
    weekly_ig = d["weekly_ig"]
    posts_ig = d["posts_ig"]
    if posts_ig is not None:
        lines.append("Posts par candidat:")
        cnt = posts_ig.groupby("candidate").size()
        for k, v in cnt.sort_values(ascending=False).items():
            lines.append(f"  - {k}: {v}")
        if "likes" in posts_ig.columns:
            lines.append("")
            lines.append("Likes totaux par candidat:")
            likes = posts_ig.groupby("candidate")["likes"].sum().sort_values(ascending=False)
            for k, v in likes.items():
                lines.append(f"  - {k}: {v:.0f}")
    else:
        lines.append("(posts_instagram non chargé)")

    # === 18. TOP TWEETS (TOUS LES 8 CANDIDATS) ===
    _section(lines, "18. Top 5 tweets par ER (chaque candidat)")
    KEYS = ["Knafo", "Brossat", "Chikirou", "Mariani", "Bournazel", "Gregoire", "Belliard", "Dati"]
    if tweets is not None and len(tweets) > 0:
        tw = tweets.dropna(subset=["engagement_rate"])
        for c in KEYS:
            sub = tw[tw["candidate"] == c].nlargest(5, "engagement_rate")
            if len(sub) == 0:
                continue
            lines.append(f"### {c}")
            for i, (_, r) in enumerate(sub.iterrows(), 1):
                txt = (str(r["text"] or "")[:90] + "...") if pd.notna(r["text"]) and len(str(r["text"])) > 90 else (str(r["text"] or ""))
                lines.append(f"  {i}. ER={r['engagement_rate']*10:.2f}‰ | likes={r['likes']:.0f} | {txt}")
            lines.append("")
    else:
        lines.append("(tweets non chargé)")

    # === 19. SENTIMENT VS ANOMALIES ===
    _section(lines, "19. Sentiment vs anomalies (A3)")
    sentiment_anomalies = d["sentiment_anomalies"]
    if sentiment_anomalies is not None and len(sentiment_anomalies) > 0:
        lines.append(str(sentiment_anomalies.head(20).to_string()))
    else:
        lines.append("(A3_sentiment_vs_anomalies non disponible)")

    # === 20. BENCHMARK BERT ===
    _section(lines, "20. Benchmark fine-tuning CamemBERT (4 classes)")
    import json
    _bert_json = _DOCS / "bert_metrics.json"
    if _bert_json.exists():
        with open(_bert_json, encoding="utf-8") as f:
            bert = json.load(f)
        lines.append(f"- Accuracy (test): {bert.get('accuracy', 0):.3f}")
        lines.append(f"- F1 macro (test): {bert.get('f1_macro', 0):.3f}")
        if "f1_per_class" in bert:
            lines.append("")
            lines.append("F1 par classe:")
            for lbl, val in bert["f1_per_class"].items():
                lines.append(f"  - {lbl}: {val:.3f}")
        if "confusion_matrix" in bert:
            labels_bert = list(bert.get("f1_per_class", {}).keys()) or ["CRITIQUE", "HOSTILITE", "IRONIE", "SOUTIEN"]
            cm = bert["confusion_matrix"]
            if cm and labels_bert:
                lines.append("")
                lines.append("Matrice de confusion (prédit / réel):")
                lines.append("| | " + " | ".join(labels_bert) + " |")
                lines.append("|---" * (len(labels_bert) + 1) + "|")
                for i, lbl in enumerate(labels_bert[: len(cm)]):
                    lines.append("| " + lbl + " | " + " | ".join(str(int(x)) for x in cm[i]) + " |")
    else:
        lines.append("(Exécuter train_sentiment_bert.py puis régénérer ce document)")

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Fin du document. Régénérer avec: python scripts/export_resultats_chiffres.py*")

    _DOCS.mkdir(parents=True, exist_ok=True)
    Path(_OUT).write_text("\n".join(lines), encoding="utf-8")
    print(f"Écrit: {_OUT}")


if __name__ == "__main__":
    run()
