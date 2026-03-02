# Paris Municipales 2026 — Analyse quantitative des réseaux sociaux

7 659 tweets · 3 317 posts Instagram · 44 599 réponses classifiées · 8 candidats · 13 mois

Analyse des campagnes numériques (Twitter, Instagram) des candidats aux municipales de Paris 2026 : engagement, sentiment, echo chambers, interactions, cross-platform.

---

## Structure

```
├── notebooks/      # 9 notebooks d'analyse (01→09)
├── figures/        # PNG 300 DPI
├── docs/           # Méthodologie, résultats, matériau articles
├── scripts/        # Export chiffres, fine-tuning CamemBERT
├── src/utils.py   # Palette, style, fonctions de visualisation
├── config/         # Candidats, requêtes
├── final/          # Données et outputs pipeline (data/, A1–A7)
└── outputs/        # Données intermédiaires (analysis_v3)
```

---

## Reproduction

1. Placer les données (`tweets_twitter.csv`, `posts_instagram.csv`, `replies_classified.csv`) dans `final/data/`
2. `pip install -r requirements.txt`
3. Exécuter les notebooks dans l'ordre : `jupyter notebook notebooks/01_engagement_viralite.ipynb`

Pour régénérer les résultats : `python scripts/export_resultats_chiffres.py`

**Fine-tuning CamemBERT** : `python scripts/prepare_annotations.py` puis `python scripts/train_sentiment_bert.py`

---

## Méthodologie

- **ER** : (likes + comments + shares) / followers × 100
- **NSI** : (SOUTIEN − HOSTILITÉ) / total
- **Echo score** : 100 − cross_camp_pct
- **Lift** : (ER_cross − ER_normal) / ER_normal

Références : Rathje et al. 2021, Barberá 2020, Cinelli et al. 2022.

---

## Licence

MIT
