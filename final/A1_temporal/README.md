# A1 — Dynamiques Temporelles

**Question** : Comment évolue la présence numérique de chaque candidat sur 13 mois ?

## Fichiers

### tweets_source.csv — 7 659 lignes
Tweets avec engagement_rate et year_week. Source pour re-calculs.

### weekly_metrics_twitter.csv — 427 lignes (8 candidats × ~53 semaines)
Métriques Twitter agrégées par semaine.
Colonnes clés : candidate_id, year_week, er_median, er_mean, volume,
interactions_total, likes_total, comments_total, shares_total, week_start

### weekly_metrics_instagram.csv — 427 lignes
Même structure, pour Instagram.

### weekly_metrics_tiktok.csv — 39 lignes
⚠️ Données partielles : 4 candidats seulement, couverture limitée.

### anomalies_detected.csv — 70 anomalies
Pics viraux et creux d'engagement détectés (z-score global + rolling 8 semaines).
Colonnes clés : candidate_id, week_start, anomaly_type (viral_pic/significant_pic/creux),
z_score, top_post_text, top_post_engagement
- 15 pics viraux (z > 3)
- 53 pics significatifs (z > 2)
- 2 creux

### momentum_scores.csv — 19 lignes
Tendance des 8 dernières semaines par candidat × plateforme.
Colonnes : candidate_id, platform, momentum_slope, r_squared, p_value, direction

### crossplatform_correlation.csv — 14 paires
Corrélations Spearman Twitter↔Instagram par candidat.
Colonnes : candidate_id, spearman_rho, p_value, synchrony

### ecosystem_gregoire.csv — 60 semaines
Métriques de l'écosystème gauche unie autour de Grégoire (Grégoire + Brossat + Belliard).
Colonnes : year_week, interactions_total, er_ecosystem, er_gregoire_solo
