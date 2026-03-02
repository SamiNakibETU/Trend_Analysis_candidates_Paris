# A3 — Sentiment des Audiences (4 Classes)

**Question** : Quelles attitudes les réseaux sociaux expriment-ils envers chaque candidat ?

## Fichiers

### sentiment_weekly_4class.csv — ~400 lignes
⭐ FICHIER PRINCIPAL POUR L'ANALYSE TEMPORELLE.
Sentiment hebdomadaire calculé sur les 44 599 replies (nouvelle classification 4 classes).
Colonnes : candidate_id, candidate, parti, camp, year_week, week_start, n_replies,
n_soutien, n_critique, n_hostilite, n_ironie, n_inconnu,
pct_soutien, pct_critique, pct_hostilite, pct_ironie,
net_support, polarization

- net_support = pct_soutien - pct_hostilite - pct_ironie
- polarization = pct_hostilite + pct_ironie

### (replies source : final/data/replies_classified.csv)
Les 44 599 replies classifiées sont dans final/data/ pour éviter la duplication.

## Distribution globale
- CRITIQUE  : 37.9% — le sentiment dominant
- SOUTIEN   : 26.5%
- HOSTILITE : 23.8%
- IRONIE    : 10.6%

## Candidats par volume de replies
- Sarah Knafo : 24 106 replies (54% du corpus)
- Rachida Dati : 8 419
- Pierre-Yves Bournazel : 4 824
