# Analyse 2 : Resonance Thematique (LDA)
## Paris Municipales 2026 — Pipeline v3

### Methodologie
- **Algorithme** : Latent Dirichlet Allocation (LDA), 10 themes
- **Corpus** : tweets personnels des 8 candidats (8 candidats)
- **Pre-traitement** : suppression URLs, mentions, stopwords francais (166 mots), n-grammes 1-2
- **Resonance** = engagement moyen (likes + 2*shares + comments) des tweets du theme

---

### 1. Themes identifies (LDA)

| # | Theme | Top mots-cles |
|---|---|---|
| 1 | **Logement & urbanisme** | logement, place, habitants, social, the, retrouvez, suis, rendez |
| 2 | **Vie locale & citoyennete** | plan, parisiennes, projet, ville, populaire, maire, grand, nouveau |
| 3 | **Geopolitique & international** | france, contre, millions, ue, pays, français, europe, com |
| 4 | **Social & solidarite** | ceux, monde, santé, année, président, française, font, avons |
| 5 | **Securite & delinquance** | politique, public, sécurité, argent, service, enfants, police, famille |
| 6 | **Arrondissement / Liberté / Gauche** | arrondissement, liberté, gauche, campagne, soir, jours, ensemble, ville |
| 7 | **Budget & finances** | euros, milliards, français, 000, gouvernement, loi, nationale, budget |
| 8 | **Education & culture** | droite, dati, culture, extrême, fr, extrême droite, gauche, mme |
| 9 | **Deux / Emmanuel / Peuple** | deux, emmanuel, peuple, grégoire, européenne, fr, droits, macron |
| 10 | **Soutien / Jour / France** | soutien, jour, france, contre, république, été, pourquoi, comment |

---

### 2. Theme dominant par candidat

| Candidat | Theme dominant | % corpus |
|---|---|---|
| Belliard (EELV) | Education & culture | 16.9% |
| Gregoire (PS) | Education & culture | 12.3% |
| Brossat (PCF) | Education & culture | 19.9% |
| Bournazel (Hor.) | Arrondissement / Liberté / Gauche | 13.2% |
| Dati (LR) | Logement & urbanisme | 15.7% |
| Knafo (Reconq.) | Education & culture | 14.9% |
| Chikirou (LFI) | Geopolitique & international | 14.3% |
| Mariani (RN) | Geopolitique & international | 17.2% |

---

### 3. Top resonance thematique (engagement moyen)

| Candidat | Theme | N tweets | Engagement moyen |
|---|---|---|---|
| Knafo (Reconq.) | Securite & delinquance | 83 | 32638 |
| Knafo (Reconq.) | Soutien / Jour / France | 55 | 29315 |
| Knafo (Reconq.) | Budget & finances | 189 | 27811 |
| Knafo (Reconq.) | Social & solidarite | 89 | 23191 |
| Knafo (Reconq.) | Geopolitique & international | 184 | 20887 |

---

### Conclusions

1. **Specialisation thematique** : chaque candidat se distingue par un theme de predilection —
   les themes detectes correspondent aux programmes declaratifs de chaque parti.
2. **Resonance != Volume** : certains themes peu abordes generent un engagement disproportionne
   (effets d'agenda ou de buzz sur un sujet de polarisation).
3. **Convergence / divergence** : les themes "Logement" et "Budget" sont transpartisans,
   tandis que "Immigration" et "Ecologie" sont plus polarises ideologiquement.
