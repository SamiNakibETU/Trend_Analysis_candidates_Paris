# Résultats chiffrés exhaustifs

Généré par export_resultats_chiffres.py. Contient tout ce que produisent les notebooks.

## Table des matières

1. Volume | 2. Sentiment | 3. ER Twitter | 4. Momentum | 5. NSI | 6. Synthèse A7 | 7. Lift détail | 8. Réseau mentions | 9. Jaccard | 10. Echo | 11. Synchronie | 12. Anomalies | 13. Inflexion sentiment | 14. Topics | 15. Topic engagement | 16. Weekly 10s | 17. Instagram | 18. Top tweets | 19. Sentiment×anomalies | 20. Benchmark BERT


---

## 1. Volume du corpus

- tweets_twitter: 7659 lignes
- posts_instagram: (non chargé)
- replies (A7): 44091 lignes
- auteurs uniques (replies): 19017

Tweets par candidat:
  - Knafo: 1189
  - Gregoire: 1163
  - Brossat: 1142
  - Mariani: 931
  - Dati: 886
  - Chikirou: 881
  - Bournazel: 847
  - Belliard: 620

Replies par candidat (A7):
  - Knafo: 23811 (54.0%)
  - Dati: 8325 (18.9%)
  - Bournazel: 4783 (10.8%)
  - Mariani: 2128 (4.8%)
  - Belliard: 1892 (4.3%)
  - Brossat: 1706 (3.9%)
  - Chikirou: 797 (1.8%)
  - Gregoire: 649 (1.5%)

---

## 2. Distribution sentiment (replies, calculée)

Global:
  - CRITIQUE: 37.9%
  - SOUTIEN: 26.5%
  - HOSTILITE: 23.8%
  - IRONIE: 10.6%
  - INCONNU: 1.1%

Par candidat (% CRITIQUE, SOUTIEN, HOSTILITE, IRONIE):
  - Knafo: CRITIQUE=31.7%, SOUTIEN=36.1%, HOSTILITE=21.7%, IRONIE=9.3%
  - Dati: CRITIQUE=47.0%, SOUTIEN=14.8%, HOSTILITE=25.0%, IRONIE=12.1%
  - Mariani: CRITIQUE=42.4%, SOUTIEN=21.2%, HOSTILITE=24.9%, IRONIE=10.3%
  - Chikirou: CRITIQUE=30.8%, SOUTIEN=14.4%, HOSTILITE=39.3%, IRONIE=14.5%
  - Gregoire: CRITIQUE=47.8%, SOUTIEN=22.3%, HOSTILITE=18.6%, IRONIE=11.1%
  - Brossat: CRITIQUE=40.4%, SOUTIEN=11.9%, HOSTILITE=32.5%, IRONIE=14.0%
  - Belliard: CRITIQUE=45.2%, SOUTIEN=12.7%, HOSTILITE=25.9%, IRONIE=15.0%
  - Bournazel: CRITIQUE=46.9%, SOUTIEN=15.2%, HOSTILITE=25.8%, IRONIE=11.4%

---

## 3. Engagement Rate (ER) Twitter

| Candidat | ER médian ‰ | ER moyen ‰ | ER std ‰ |
|----------|-------------|------------|----------|
| Knafo | 11.53 | 32.66 | 54.39 |
| Brossat | 6.42 | 7.31 | 3.99 |
| Chikirou | 4.09 | 5.58 | 4.56 |
| Mariani | 3.12 | 4.89 | 5.89 |
| Bournazel | 2.28 | 2.77 | 1.42 |
| Gregoire | 1.16 | 1.45 | 0.90 |
| Belliard | 0.86 | 1.50 | 1.17 |
| Dati | 0.60 | 0.90 | 0.82 |

Ratio Knafo / médiane des 7 autres: 5.1×

Distribution ER par candidat (tweets bruts):
  - Belliard: médiane 14.99‰, Q1 9.20‰, Q3 21.63‰, max 85.89‰
  - Gregoire: médiane 16.85‰, Q1 10.80‰, Q3 23.82‰, max 74.20‰
  - Brossat: médiane 38.93‰, Q1 24.56‰, Q3 57.08‰, max 151.53‰
  - Bournazel: médiane 29.00‰, Q1 18.17‰, Q3 41.32‰, max 110.43‰
  - Dati: médiane 23.17‰, Q1 13.81‰, Q3 36.91‰, max 97.31‰
  - Knafo: médiane 76.78‰, Q1 49.34‰, Q3 103.66‰, max 228.39‰
  - Chikirou: médiane 66.89‰, Q1 38.40‰, Q3 101.53‰, max 200.55‰
  - Mariani: médiane 47.75‰, Q1 30.48‰, Q3 71.67‰, max 210.66‰

---

## 4. Momentum Twitter (8 dernières semaines)

| Candidat | Slope (‰/sem) | p-value | Direction |
|----------|---------------|---------|-----------|
| D. Belliard | -0.2719 | 0.035 | baisse |
| E. Grégoire | 0.0794 | 0.489 | hausse |
| I. Brossat | -0.5246 | 0.034 | baisse |
| P-Y. Bournazel | -0.2470 | 0.060 | baisse |
| R. Dati | -0.2474 | 0.041 | baisse |
| S. Knafo | -1.0848 | 0.061 | baisse |
| S. Chikirou | -0.8659 | 0.061 | baisse |
| T. Mariani | -0.6089 | 0.090 | baisse |

Candidats en hausse: 1 (Grégoire seul si p<0.10)

---

## 5. Net Sentiment Index (NSI)

| Candidat | NSI | IC 95% | n | % hostilité |
|----------|-----|--------|---|-------------|
| Knafo | 0.145 | [0.137; 0.155] | 23811 | 22.0% |
| Gregoire | 0.037 | [-0.014; 0.088] | 649 | 18.6% |
| Mariani | -0.038 | [-0.065; -0.010] | 2128 | 25.2% |
| Dati | -0.104 | [-0.117; -0.089] | 8325 | 25.3% |
| Bournazel | -0.107 | [-0.125; -0.089] | 4783 | 26.0% |
| Belliard | -0.133 | [-0.160; -0.108] | 1892 | 26.2% |
| Brossat | -0.209 | [-0.239; -0.179] | 1706 | 32.9% |
| Chikirou | -0.251 | [-0.299; -0.202] | 797 | 39.6% |

---

## 6. Synthèse A7 (echo, lift, mentions)

| Candidat | Echo % | Exclusive % | Cross-camp % | Lift % | Mentions reçues | % hostilité | % ironie | n_cross_posts |
|----------|--------|-------------|--------------|--------|-----------------|-------------|----------|----------------|
| Brossat | 62.2 | 60.6 | 37.8 | -33.7 | 14 | 36.8 | 9.7 | 31 |
| Chikirou | 77.7 | 74.6 | 22.3 | -11.7 | 0 | 35.8 | 16.3 | 23 |
| Belliard | 52.5 | 49.7 | 47.5 | -82.9 | 7 | 15.2 | 7.3 | 18 |
| Gregoire | 67.5 | 61.2 | 32.5 | 27.3 | 80 | 9.2 | 8.8 | 16 |
| Bournazel | 58.2 | 58.2 | 41.8 | -58.8 | 5 | 14.1 | 7.1 | 16 |
| Dati | 77.1 | 61.2 | 22.9 | 44.8 | 33 | 19.7 | 8.4 | 5 |
| Knafo | 88.1 | 81.8 | 11.9 | -15.6 | 0 | 20.1 | 8.8 | 2 |
| Mariani | 57.4 | 57.4 | 42.6 | -87.1 | 0 | 25.4 | 4.7 | 3 |

Total mentions cross-candidats: 139 (Grégoire en reçoit 80, 57 %)

---

## 7. Lift détail (n_cross_posts, avg_eng_cross vs normal)

| Candidat | n_cross_posts | n_normal_posts | avg_eng_cross | avg_eng_normal | lift % |
|----------|---------------|----------------|---------------|----------------|--------|
| Dati | 5 | 881 | 1167.2 | 806.0 | 44.8 |
| Gregoire | 16 | 1147 | 217.5 | 170.8 | 27.3 |
| Chikirou | 23 | 858 | 1317.8 | 1492.0 | -11.7 |
| Knafo | 2 | 1187 | 17180.5 | 20350.8 | -15.6 |
| Brossat | 31 | 1111 | 1107.6 | 1670.2 | -33.7 |
| Bournazel | 16 | 831 | 240.2 | 583.8 | -58.8 |
| Belliard | 18 | 602 | 139.2 | 815.5 | -82.9 |
| Mariani | 3 | 928 | 296.0 | 2303.4 | -87.1 |

---

## 8. Réseau de mentions entre candidats (source → target)

| Source | Target | Mentions |
|--------|--------|----------|
| Brossat | Gregoire | 27 |
| Chikirou | Gregoire | 21 |
| Chikirou | Dati | 14 |
| Belliard | Gregoire | 13 |
| Bournazel | Gregoire | 11 |
| Gregoire | Brossat | 9 |
| Gregoire | Dati | 6 |
| Bournazel | Dati | 5 |
| Dati | Gregoire | 5 |
| Gregoire | Belliard | 5 |
| Chikirou | Bournazel | 4 |
| Belliard | Brossat | 4 |
| Mariani | Dati | 3 |
| Brossat | Dati | 3 |
| Belliard | Dati | 2 |
| Knafo | Gregoire | 2 |
| Belliard | Bournazel | 1 |
| Bournazel | Belliard | 1 |
| Brossat | Belliard | 1 |
| Chikirou | Brossat | 1 |
| Mariani | Gregoire | 1 |

Total arêtes: 139

---

## 9. Jaccard chevauchement audiences (toutes les paires)

| k1 | k2 | Jaccard % | dist_ideo | same_camp |
|----|----|-----------|-----------|-----------|
| Bournazel | Dati | 9.26 | 1 | False |
| Brossat | Belliard | 9.26 | 2 | False |
| Bournazel | Belliard | 7.84 | 2 | False |
| Dati | Knafo | 7.60 | 1 | False |
| Gregoire | Belliard | 6.33 | 1 | True |
| Knafo | Mariani | 4.98 | 1 | True |
| Dati | Belliard | 4.48 | 3 | False |
| Dati | Mariani | 4.11 | 2 | False |
| Bournazel | Knafo | 3.94 | 2 | False |
| Bournazel | Brossat | 3.84 | 4 | False |
| Gregoire | Brossat | 3.84 | 3 | False |
| Bournazel | Mariani | 3.76 | 3 | False |
| Dati | Brossat | 3.23 | 5 | False |
| Bournazel | Gregoire | 2.73 | 1 | False |
| Chikirou | Brossat | 2.46 | 1 | True |
| Chikirou | Gregoire | 2.12 | 2 | False |
| Chikirou | Belliard | 2.06 | 1 | False |
| Mariani | Belliard | 1.90 | 5 | False |
| Knafo | Brossat | 1.77 | 6 | False |
| Knafo | Belliard | 1.76 | 4 | False |
| Mariani | Brossat | 1.53 | 7 | False |
| Dati | Gregoire | 1.22 | 2 | False |
| Bournazel | Chikirou | 1.16 | 3 | False |
| Dati | Chikirou | 1.08 | 4 | False |
| Knafo | Chikirou | 0.57 | 5 | False |
| Mariani | Gregoire | 0.53 | 4 | False |
| Mariani | Chikirou | 0.50 | 6 | False |
| Knafo | Gregoire | 0.41 | 3 | False |

Homophilie idéologique: Spearman ρ = -0.600, p = 0.0007

---

## 10. Echo chambers détaillé (A4_echo_x_sentiment)

| Candidat | echo_score | exclusive_pct | cross_camp_pct | n_audience | pct_hostilite | pct_ironie | nsi_mean |
|----------|------------|---------------|---------------|------------|---------------|------------|----------|
| Knafo | 88.1 | 81.8 | 11.9 | 10602 | 20.1 | 8.8 | 15.4 |
| Chikirou | 77.7 | 74.6 | 22.3 | 701 | 35.8 | 16.3 | -29.9 |
| Dati | 77.1 | 61.2 | 22.9 | 4184 | 19.7 | 8.4 | 2.0 |
| Gregoire | 67.5 | 61.2 | 32.5 | 551 | 9.2 | 8.8 | 19.6 |
| Brossat | 62.2 | 60.6 | 37.8 | 1340 | 36.8 | 9.7 | -24.8 |
| Bournazel | 58.2 | 58.2 | 41.8 | 2612 | 14.1 | 7.1 | 16.9 |
| Mariani | 57.4 | 57.4 | 42.6 | 1720 | 25.4 | 4.7 | -1.7 |
| Belliard | 52.5 | 49.7 | 47.5 | 1279 | 15.2 | 7.3 | 7.2 |

---

## 11. Synchronie Twitter / Instagram

| Candidat | Spearman ρ | p-value | n_weeks | synchrony |
|----------|------------|---------|---------|-----------|
| D. Belliard | 0.516 | 0.0004 | 43 | modéré |
| E. Grégoire | 0.699 | 0.0000 | 55 | synchronisé |
| I. Brossat | 0.205 | 0.1330 | 55 | indépendant |
| P-Y. Bournazel | 0.821 | 0.0000 | 53 | synchronisé |
| R. Dati | 0.235 | 0.1286 | 43 | indépendant |
| S. Knafo | 0.493 | 0.0001 | 56 | modéré |
| S. Chikirou | -0.004 | 0.9761 | 49 | indépendant |
| T. Mariani | 0.210 | 0.3041 | 26 | indépendant |

---

## 12. Anomalies ER (top 10 par Z-score)

| week_start | candidat | year_week | er_median | z_global | top_post_engagement |
|------------|----------|-----------|----------|----------|---------------------|
| 2025-07-21 | Chikirou | 2025-W30 | 0.0312 | 5.63 | 38560 |
| 2025-08-14 | Mariani | 2025-W33 | 0.0334 | 4.84 | 36441 |
| 2025-03-16 | Dati | 2025-W11 | 0.0045 | 4.37 | 2231 |
| 2025-10-21 | Gregoire | 2025-W43 | 0.0048 | 3.73 | 1404 |
| 2025-03-29 | Knafo | 2025-W13 | 0.2349 | 3.72 | 173831 |
| 2025-08-07 | Bournazel | 2025-W32 | 0.0077 | 3.46 | 277 |
| 2025-02-26 | Brossat | 2025-W09 | 0.0198 | 3.12 | 11064 |
| 2025-07-28 | Brossat | 2025-W31 | 0.0190 | 2.93 | 53029 |
| 2025-04-14 | Mariani | 2025-W16 | 0.0221 | 2.92 | 3930 |
| 2025-12-29 | Dati | 2026-W01 | 0.0033 | 2.88 | 6311 |

---

## 13. Points d'inflexion sentiment (A3)

| candidat | year_week | net_support | z_score | direction | n_replies |
|----------|-----------|-------------|---------|-----------|-----------|
| Brossat | 2025-W17 | -33.3 | -14.65 | Baisse | 3 |
| Mariani | 2025-W43 | 0.0 | 13.45 | Hausse | 1 |
| Brossat | 2026-W03 | -57.1 | -5.25 | Baisse | 14 |
| Knafo | 2026-W06 | 46.7 | 5.20 | Hausse | 45 |
| Dati | 2025-W17 | 100.0 | 4.85 | Hausse | 2 |
| Bournazel | 2026-W06 | -33.3 | -4.70 | Baisse | 3 |
| Knafo | 2025-W38 | -25.0 | -4.35 | Baisse | 8 |
| Dati | 2026-W03 | 100.0 | 3.83 | Hausse | 1 |
| Gregoire | 2025-W41 | 71.4 | 3.76 | Hausse | 7 |
| Brossat | 2026-W08 | -100.0 | -3.71 | Baisse | 1 |
| Chikirou | 2026-W02 | -56.4 | -3.36 | Baisse | 39 |
| Mariani | 2026-W05 | 50.0 | 3.32 | Hausse | 4 |
| Bournazel | 2025-W26 | 0.0 | -3.00 | Baisse | 11 |
| Gregoire | 2025-W24 | 40.0 | -2.97 | Baisse | 5 |
| Bournazel | 2026-W07 | -60.0 | -2.93 | Baisse | 5 |

---

## 14. Topics par candidat (%)

(Colonnes = thèmes, lignes = candidats)

```
             Unnamed: 0  Arrondissement / Liberté / Gauche  Budget  Générique†  Anti-droite/Dati*  Géopolitique  Logement  Sécurité  Social  Soutien/France  Local/Paris
0         Brossat (PCF)                               7.95   13.30        6.00              19.88         10.09      8.24      9.08    7.98            9.53         7.96
1        Chikirou (LFI)                               8.44   11.17        6.42              10.49         14.28     10.41      9.23    8.95           10.31        10.30
2       Belliard (EELV)                              10.83    6.54        5.47              16.89          9.57     10.60      8.95   11.56            8.53        11.06
3         Grégoire (PS)                              11.30    7.86        8.11              12.33          9.32     12.31      8.29    9.23           11.23        10.02
4  Bournazel (Horizons)                              13.18    6.44        6.32               9.61          8.41     13.08     10.53   12.25            7.57        12.61
5             Dati (LR)                               9.95    6.61        6.27              11.14          9.96     15.65     10.70   12.21            9.05         8.46
6    Knafo (Reconquête)                               9.04   11.97        7.68              14.88         13.40     10.24      9.33    8.77            7.19         7.52
7          Mariani (RN)                               8.18   11.44        7.06              15.08         17.18      7.99     10.19    8.17            7.51         7.20
```

---

## 15. Ranking des topics par engagement médian

| topic_name | topic_short | med_eng_global | n_tweets_total |
|------------|-------------|----------------|----------------|
| Logement & urbanisme | Logement | 248.0 | 916 |
| Arrondissement / Liberté / Gauche | nan | 271.8 | 696 |
| Vie locale & citoyennete | Local/Paris | 284.2 | 620 |
| Social & solidarite | Social | 422.0 | 680 |
| Geopolitique & international | Géopolitique | 429.2 | 968 |
| Education & culture | Anti-droite/Dati* | 455.0 | 1270 |
| Securite & delinquance | Sécurité | 468.8 | 648 |
| Budget & finances | Budget | 556.0 | 792 |
| Soutien / Jour / France | Soutien/France | 595.5 | 593 |
| Deux / Emmanuel / Peuple | Générique† | 705.5 | 366 |

---

## 16. ER médian 10 dernières semaines (Twitter)

Moyenne des 10 dernières semaines par candidat (ER en ‰):
  - S. Knafo: 8.25‰
  - S. Chikirou: 5.34‰
  - I. Brossat: 4.69‰
  - P-Y. Bournazel: 3.99‰
  - T. Mariani: 2.88‰
  - D. Belliard: 2.75‰
  - E. Grégoire: 1.93‰
  - R. Dati: 1.39‰

---

## 17. Résumé Instagram

(posts_instagram non chargé)

---

## 18. Top 5 tweets par ER (chaque candidat)

### Knafo
  1. ER=228.39‰ | likes=4128 | Surveiller nos frontières ce serait impossible ? Des centaines de pays le font. Nous l’avo...
  2. ER=217.51‰ | likes=6634 | Von der Leyen se comporte comme une lobbyiste allemande. Elle ne défend pas les intérêts d...
  3. ER=198.66‰ | likes=4481 | L'agriculture est une activité aussi stratégique que le nucléaire. Les agriculteurs ne son...
  4. ER=197.01‰ | likes=6163 | Vous êtes déjà 500 000 à mes côtés sur Instagram ! 500 000 fois merci ! ❤️ Vous êtes tous ...
  5. ER=192.40‰ | likes=2519 | On marche sur la tête : on taxe les importations d'engrais et on détaxe les importations d...

### Brossat
  1. ER=151.53‰ | likes=5232 | Dans quel monde les plus riches demandent aux plus pauvres de mettre la main à la poche ? ...
  2. ER=142.79‰ | likes=718 | Après avoir échoué à interdire l’UNRWA, en violation du droit international, Israël a tout...
  3. ER=142.73‰ | likes=2234 | Bayrou est arrivé par effraction. Il n’a aucune légitimité à gouverner. Encore moins à men...
  4. ER=131.69‰ | likes=802 | M. Bayrou est un menteur compulsif. Il lance un conclave sur les retraites, promet que l’â...
  5. ER=126.72‰ | likes=269 | Et maintenant le ministre du logement propose de compter les places de prison dans le taux...

### Chikirou
  1. ER=200.55‰ | likes=718 | Le sort de l'équipage de la #HandalaFlotilla dépend de notre mobilisation et de notre vigi...
  2. ER=187.34‰ | likes=40 | Nos 9 priorités :
- le logement,
- l'éducation communale,
- la bifurcation écologique,
- l...
  3. ER=184.22‰ | likes=976 | Il appelle à l'union de toutes les droites, y compris les fachos, dans la ville où le mair...
  4. ER=183.04‰ | likes=290 | Aujourd’hui nous sommes en état d’urgence vitale : sur l’écologie, le logement, il faut ag...
  5. ER=180.98‰ | likes=247 | Pour la propreté, nous souhaitons tout municipaliser pour tout coordonner. C'est moins che...

### Mariani
  1. ER=210.66‰ | likes=5706 | Lideranças da Europa convergem que o Brasil será mais estratégico do que nunca em áreas se...
  2. ER=202.20‰ | likes=1654 | En acceptant le 3 sept.2025 le changement de "statut" de l’accord du Mercosur,Macron accep...
  3. ER=201.01‰ | likes=2958 | Pour les femmes, le burkini est depuis le 10 juin obligatoire sur les plages en Syrie. Von...
  4. ER=189.94‰ | likes=1382 | 📺 Oui la démocratie est menacée dans l’UE ! L’annulation du 1er tour de l’élection préside...
  5. ER=186.15‰ | likes=1598 | A chaque semaine, son scandale dans cette Union Européenne 🤷‍♂️ Cette fois ont découvre qu...

### Bournazel
  1. ER=110.43‰ | likes=756 | 🔴 STOP À LA BARBARIE DES COMBATS DE COQS ! 9 000 combats par an dans le Nord-Pas-de-Calais...
  2. ER=90.23‰ | likes=9 | Pour l’abrogation avec des arguments lemonde.fr/idees/article/202…
Bien cordialement
  3. ER=85.17‰ | likes=7646 | Merci Loïs, tu nous as fait rêver ! 💙💪 #RolandGarros
  4. ER=79.62‰ | likes=56 | Je souhaite que la France puisse se doter d’un budget responsable et juste :
✅ Juste pour ...
  5. ER=73.35‰ | likes=45 | Ce matin sur le terrain avec @Benoitpernin au marché de l’avenue Ledru-Rollin #Paris12 pou...

### Gregoire
  1. ER=74.20‰ | likes=10 | La bataille pour Paris sera rude, nous le savons. Et nous avons l’immense responsabilité d...
  2. ER=72.52‰ | likes=10 | Stop à la galère du logement ! Je veux créer des solutions accessibles.
  3. ER=72.22‰ | likes=2480 | Afin de restaurer la confiance démocratique, Emmanuel Grégoire propose d’interdire aux per...
  4. ER=70.39‰ | likes=574 | Soutenir le livre et voter contre les subventions aux librairies indépendantes en Conseil ...
  5. ER=64.63‰ | likes=8 | Notre seule confrontation sera démocratique et motivée par une unique préoccupation : répo...

### Belliard
  1. ER=85.89‰ | likes=5 | La liste d'union de la gauche et des écologistes pour Paris 11 est déposée 👏🏼 C'est parti ...
  2. ER=76.46‰ | likes=84109 | BREAKING: This is in Trump's back yard. Washington DC No Kings Day Protest. This is just t...
  3. ER=75.00‰ | likes=2 | Ce sont les chiffres pour la France. C'est la réalité d'enfants sans famille qui ont trop ...
  4. ER=71.36‰ | likes=20042 | Téhéran, ce soir. Mesdames messieurs, nous vous présentons le peuple le plus courageux du ...
  5. ER=63.02‰ | likes=6757 | Dati est donc Ministre ET candidate aux législatives ET candidate à la Mairie de Paris ET ...

### Dati
  1. ER=97.31‰ | likes=401 | 📈12 milliards d’euros de dette.
📈Une taxe foncière en hausse historique.
📈Des dépenses inc...
  2. ER=97.14‰ | likes=202 | Hidalgo-Grégoire laissent prospérer le scandale du périscolaire, aidé par l’omerta médiati...
  3. ER=88.31‰ | likes=89 | 5⃣En cas d’hospitalisation de leurs propriétaires: une carte individuelle signalera la pré...
  4. ER=86.96‰ | likes=282 | Depuis des semaines, je rencontre des parents effondrés. Certains vivent avec l’horreur de...
  5. ER=86.83‰ | likes=621 | Emmanuel Grégoire a beau vouloir le faire oublier, il est le candidat de la majorité sorta...


---

## 19. Sentiment vs anomalies (A3)

   periode  n_nsi  med_nsi  med_hostilite  p_mw_nsi_bd  p_mw_nsi_da  p_mw_host_bd  p_mw_host_da
0    avant     42    2.085          21.01          NaN          NaN           NaN           NaN
1  pendant     46    0.000          16.67     0.933271          NaN      0.482257           NaN
2    après     41    4.350          18.52          NaN     0.942222           NaN      0.639392

---

## 20. Benchmark fine-tuning CamemBERT (4 classes)

(Exécuter train_sentiment_bert.py puis régénérer ce document)

---

*Fin du document. Régénérer avec: python scripts/export_resultats_chiffres.py*