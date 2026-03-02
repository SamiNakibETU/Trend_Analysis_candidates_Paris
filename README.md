# 🗳️ Paris 2026 — Qui domine la conversation numérique ?

> Analyse quantitative de 7 659 tweets, 44 599 réponses et 3 317 posts Instagram
> de 8 candidats aux municipales de Paris. 13 mois. NLP. Réseaux. OSINT.

![Classement ER par candidat — Twitter](figures/01_er_classement.png)

---

## 3 résultats clés

1. **Knafo domine l'engagement** — ER médian 11,5 ‰ (×5 la médiane des 7 autres). Distribution très asymétrique : quelques pics viraux expliquent l’écart.
2. **Grégoire = hub des mentions** — 80 des 139 mentions cross-candidats (57 %). Quand les candidats s’attaquent, ils parlent de lui.
3. **Echo chambers marqués** — Knafo 88 %, Chikirou 78 %, Dati 77 %. Homophilie idéologique : corrélation ρ ≈ −0,60 entre proximité idéologique et chevauchement d’audience.

---

## Liens

| Ressource | Contenu |
|-----------|---------|
| [Méthodologie](docs/methodologie.md) | ER, NSI, echo score, LDA, limites |
| [Résultats chiffrés](docs/RESULTATS_CHIFFRES.md) | Tableaux exhaustifs, p-values |
| [Notebooks](notebooks/) | 9 notebooks d’analyse (engagement → BERT) |
| [Note d'analyse](docs/note_analyse.md) | Synthèse narrative, findings |

---

## Reproduction

```bash
pip install -r requirements.txt
# Placer tweets_twitter.csv, posts_instagram.csv, replies_classified.csv dans final/data/
jupyter notebook notebooks/01_engagement_viralite.ipynb
```

---

## À propos

Projet personnel — analyse OSINT et data science des campagnes numériques municipales.  
**Sami Nakib** · [GitHub](https://github.com/SamiNakibETU) · *[LinkedIn à compléter] · Formation : [à compléter]*

---

## Setup développeur

```bash
# Config git (éviter "Your Name" sur les commits)
git config user.name "Sami Nakib"
git config user.email "votre@email.com"

# Cohen's kappa (validation sentiment)
make kappa-sample    # → outputs/.../kappa_sample_200.csv
# Remplir sentiment_human, puis :
make kappa-calc      # → docs/kappa_results.md

# Tests
make test
```

---

*Licence MIT*
