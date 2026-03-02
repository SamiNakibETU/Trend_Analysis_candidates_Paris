# A5 — Interactions Inter-Candidats

**Question** : Qui parle de qui ? Les posts de confrontation génèrent-ils plus d'engagement ?

## Fichiers

### interaction_matrix.csv — 8×8 matrice
N(candidat_i → candidat_j) = nombre de fois où i mentionne j dans ses tweets.
Index/colonnes avec SHORT_LABELS.

Résultats clés :
- Grégoire = cible principale (mentionné par Brossat 27x, Chikirou 21x, Belliard 13x)
- Knafo, Chikirou, Mariani = 0 mention sortante (stratégie d'évitement)

### interaction_timeline.csv — 84 lignes
Mentions croisées agrégées par semaine.
Colonnes : week, source, target, pair, n_mentions, total_engagement, avg_engagement

### interaction_engagement.csv — 8 lignes
Lift d'engagement : posts avec mention inter-candidat vs posts normaux.
Colonnes : candidate_id, label, n_cross_posts, n_normal_posts,
avg_eng_cross, avg_eng_normal, lift_pct

- Dati : +44.8% lift (les confrontations lui profitent)
- Mariani : -87.1% (les confrontations lui nuisent)

### interaction_cross_text.csv — 139 lignes
Contexte textuel des mentions croisées avec thèmes identifiés.
Colonnes : source, target, pair, themes, n_themes, text_snippet

### (tweets source : final/data/tweets_twitter.csv)
