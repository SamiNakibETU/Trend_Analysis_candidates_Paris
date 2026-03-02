# Données sources — Municipales Paris 2026

Fichiers partagés entre toutes les analyses.

## Fichiers

### tweets_twitter.csv — 7 659 lignes
Tous les tweets des 8 candidats collectés via Nitter (Twitter).
Colonnes : tweet_id, candidate_id, candidate, parti, camp, timestamp,
text, hashtags, mentions, likes, shares, comments, views, engagement,
engagement_rate, year_week, week_start

- engagement = likes + shares×2 + comments
- engagement_rate = engagement/views×100 (NaN si views=0)
- Périmètre : Jan 2025 – Fév 2026

### posts_instagram.csv — 3 317 lignes
Posts Instagram. shares et views = 0 (non fournis par l'API).
Colonnes : post_id, candidate_id, candidate, parti, camp, timestamp,
text, likes, comments, shares, views, engagement

### replies_classified.csv — 44 599 lignes
Replies Twitter + commentaires Instagram classifiés par GPT-5 Nano
(prompt 4 classes, sans NEUTRE).
Colonnes : reply_id, candidate_id, candidate, parti, camp, platform,
text, author_username, timestamp, likes, sentiment

Distribution du sentiment :
- CRITIQUE  : 37.9%   (conteste les idées avec arguments)
- SOUTIEN   : 26.5%   (approuve, encourage, défend)
- HOSTILITE : 23.8%   (attaque la personne)
- IRONIE    :  10.6%  (sarcasme, second degré)
- INCONNU   :   1.1%  (réponse hors norme du modèle)

## Candidats
| candidate_id | Nom | Parti | Camp |
|---|---|---|---|
| sarah_knafo | Sarah Knafo | Reconquete | Droite |
| rachida_dati | Rachida Dati | LR | Droite |
| thierry_mariani | Thierry Mariani | RN | Extreme droite |
| sophia_chikirou | Sophia Chikirou | LFI | Gauche radicale |
| emmanuel_gregoire | Emmanuel Gregoire | PS | Gauche |
| ian_brossat | Ian Brossat | PCF | Gauche radicale |
| david_belliard | David Belliard | EELV | Gauche |
| pierre_yves_bournazel | Pierre-Yves Bournazel | Horizons | Centre-droit |
