# Progress -- Pipeline v3

## Analyse 1 : Temporel
- [x] Pre-traitement temporel
- [x] Metriques hebdomadaires (Twitter: 427 rows, IG: 427, TikTok: 39)
- [x] Detection anomalies (70 anomalies: 15 pics viraux, 53 pics significatifs, 2 creux)
- [x] Cross-platform correlation (14 paires: Bournazel/Gregoire synchronises, Chikirou independant)
- [x] Momentum (Gregoire seul momentum positif Twitter; Knafo en baisse)
- [x] Ecosysteme Gregoire (ecosysteme gauche = 9.5% du volume Knafo)
- [x] Visualisations (8 fichiers HTML)
- [x] Rapport

Resultats cles :
- Twitter ER median: Knafo (1.15%) >> Brossat (0.64%) >> Chikirou (0.41%) >> Dati (0.06%)
- 15 pics viraux detectes, Chikirou z=5.6 (W30/2025, Gaza) plus fort
- Seul Gregoire a un momentum positif sur Twitter en Q1 2026
- Ecosysteme gauche unie insuffisant face a Knafo (9.5% des interactions)

## Analyse 3 : Sentiment
- [x] Normalisation replies (44 599 apres dedup/filtre)
- [x] Batch GPT-5 Nano (4 chunks, 9 echecs sur 4463 requetes)
- [x] Agregation resultats (sentiment_by_candidate, polarization_scores)
- [x] Sentiment hebdo (154 semaines) + croisement temporel
- [x] Visualisations (5 HTML)
- [x] Rapport
Resultats cles : voir REPORT_sentiment.md

## Analyse 4 : Communautes
- [x] Graphe bipartite auteur-candidat (19012 auteurs)
- [x] Matrice Jaccard (8x8 candidats)
- [x] Scores chambre d'echo
- [x] Reseau mentions inter-candidats (21 paires)
- [x] Detection communautes Louvain (8 communautes)
- [x] Visualisations (5 HTML)
- [x] Rapport

## Analyse 5 : Interactions
- [x] Matrice mentions inter-candidats
- [x] Timeline interactions par semaine
- [x] Engagement lift (posts croises vs normaux)
- [x] Analyse thematique des mentions croisees
- [x] Visualisations (5 HTML : reseau, heatmap, lift, timeline, sankey)
- [x] Rapport
Resultats cles : voir REPORT_interactions.md

## Analyse 2 : Topics
- [x] LDA (10 themes sur 7549 tweets)
- [x] Identification des themes (nommage semi-automatique)
- [x] Distribution thematique par candidat
- [x] Resonance thematique (engagement moyen par theme)
- [x] Timeline hebdomadaire des themes
- [x] Visualisations (5 HTML)
- [x] Rapport
Resultats cles : voir REPORT_topics.md
