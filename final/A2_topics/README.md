# A2 — Résonance Thématique (LDA)

**Question** : Quels thèmes les candidats abordent-ils ? Lesquels génèrent le plus d'engagement ?

## Fichiers

### topic_distribution.csv — 80 lignes (8 candidats × 10 thèmes)
% du corpus de chaque candidat consacré à chaque thème LDA.
Colonnes : candidate_id, label, topic_id, topic_name, topic_pct

### topic_resonance.csv — 80 lignes
Engagement moyen par thème et candidat.
Colonnes : candidate_id, topic_id, topic_name, n_tweets, avg_engagement,
median_engagement, total_engagement, avg_views, label

### topic_timeline.csv — 591 lignes
Évolution hebdomadaire du nombre de tweets par thème (tous candidats).
Colonnes : week, topic_name, n_tweets, avg_eng

### topic_wordclouds_data.csv — 150 lignes (10 thèmes × 15 mots)
Top-15 mots par thème pour visualisation.
Colonnes : topic_id, topic_name, rank, word

## Notes
- LDA entraîné sur les 7 659 tweets des candidats (pas les replies)
- 10 thèmes identifiés, nommage semi-automatique
- Source tweets : final/data/tweets_twitter.csv
