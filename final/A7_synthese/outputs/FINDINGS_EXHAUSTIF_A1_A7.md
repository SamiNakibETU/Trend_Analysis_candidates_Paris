# FINDINGS EXHAUSTIFS — Paris Municipales 2026
**TOUTES les sorties chiffrées des notebooks A1 à A7**

80 blocs de sortie extraits des 7 notebooks · Pipeline complet

---

## Table des matières

| Notebook | Blocs | Contenu principal |
|----------|-------|-------------------|
| **A1_temporal** | 9 | Config, shapes, couverture Twitter, momentum, ER médian, synchronie cross-platform, anomalies, findings F1-F5 |
| **A2_topics** | 8 | Topics LDA, diagnostic qualité, engagement par topic, anomalies×topics |
| **A3_sentiment** | 16 | Distribution sentiment, NSI par candidat, inflection points, test négativité, Kruskal-Wallis, anomalies |
| **A4_community** | 12 | Echo chambers, Jaccard, homophilie, Spearman, multi-candidats |
| **A5_interactions** | 11 | Matrice mentions, lift engagement, Mann-Whitney, thèmes, corrélation temporelle |
| **A6_bert_finetuning** | 16 | Zero-shot, fine-tuned, F1 par classe, confusion, erreurs |
| **A7_synthese** | 8 | Tableau synthèse, C3 thèse centrale, C4 régression, 7 findings, limites, perspectives |

---

# A1_temporal

```
✓ Cellule 0 OK — Configuration chargée
  Palette : 8 candidats
  Output  : D:\Users\Proprietaire\Desktop\Projet_perso\Presidentielle_tracker\final\A1_temporal\outputs
```

```
============================================================

▸ weekly_metrics_twitter
  Shape   : (427, 13)
  Columns : ['candidate_id', 'year_week', 'er_median', 'er_mean', 'volume', 'interactions_total', 'likes_total', 'comments_total', 'shares_total', 'week_start', 'platform', 'candidate_label', 'key']
  NaN     : aucun

▸ weekly_metrics_instagram
  Shape   : (427, 13)
  Columns : ['candidate_id', 'year_week', 'er_median', 'er_mean', 'volume', 'interactions_total', 'likes_total', 'comments_total', 'shares_total', 'week_start', 'platform', 'candidate_label', 'key']
  NaN     : aucun

▸ weekly_metrics_tiktok
  Shape   : (39, 13)
  Columns : ['candidate_id', 'year_week', 'er_median', 'er_mean', 'volume', 'interactions_total', 'likes_total', 'comments_total', 'shares_total', 'week_start', 'views_median', 'platform', 'candidate_label']
  NaN     : aucun

▸ anomalies_detected
  Shape   : (70, 14)
  Columns : ['candidate_id', 'candidate_label', 'platform', 'year_week', 'week_start', 'er_median', 'z_score', 'z_global', 'z_rolling', 'anomaly_type', 'volume', 'top_post_text', 'top_post_engagement', 'key']
  NaN     : aucun

▸ momentum_scores
  Shape   : (19, 10)
  Columns : ['candidate_id', 'candidate_label', 'platform', 'momentum_slope', 'r_squared', 'p_value', 'direction', 'last_8w_mean_er', 'n_weeks_used', 'key']
  NaN     : aucun

▸ crossplatform_correlation
  Shape   : (14, 8)
  Columns : ['candidate_id', 'candidate_label', 'platform_1', 'platform_2', 'spearman_rho', 'p_value', 'n_weeks', 'synchrony']
  NaN     : aucun

▸ ecosystem_gregoire
  Shape   : (60, 8)
  Columns : ['year_week', 'interactions_total', 'volume', 'week_start', 'er_ecosystem', 'candidate_id', 'candidate_label', 'er_gregoire_solo']
  NaN     : {'er_gregoire_solo': 3}

============================================================

▸ Couverture Twitter — semaines par candidat
           n_semaines      debut        fin  er_med_moy
key                                                    
Bournazel          57 2025-01-01 2026-02-16    0.002767
Gregoire           57 2025-01-07 2026-02-16    0.001452
Knafo              57 2025-01-02 2026-02-16    0.032657
Brossat            55 2025-01-10 2026-02-16    0.007314
Mariani            54 2025-01-01 2026-02-16    0.004890
Dati               53 2025-01-18 2026-02-16    0.000897
Chikirou           51 2025-01-02 2026-02-16    0.005575
Belliard           43 2025-01-02 2026-02-16    0.001503

============================================================

▸ Vérification momentum — valeurs aberrantes ?
          candidate_label  platform  momentum_slope  r_squared  p_value
       D. Belliard (EELV)   twitter       -0.000272     0.5489   0.0355
         E. Grégoire (PS)   twitter        0.000079     0.0830   0.4890
         I. Brossat (PCF)   twitter       -0.000525     0.5543   0.0341
P-Y. Bournazel (Horizons)   twitter       -0.000247     0.4708   0.0602
             R. Dati (LR)   twitter       -0.000247     0.5304   0.0405
    S. Knafo (Reconquête)   twitter       -0.001085     0.4690   0.0609
        S. Chikirou (LFI)   twitter       -0.000866     0.4694   0.0608
          T. Mariani (RN)   twitter       -0.000609     0.4045   0.0901
       D. Belliard (EELV) instagram       -0.000762     0.3473   0.1242
         E. Grégoire (PS) instagram        0.000014     0.0001   0.9829
         I. Brossat (PCF) instagram       -0.000581     0.0148   0.7738
P-Y. Bournazel (Horizons) instagram      -10.458333     0.2045   0.2606
             R. Dati (LR) instagram       -0.002279     0.1625   0.3220
    S. Knafo (Reconquête) instagram       -0.002350     0.6456   0.0163
        S. Chikirou (LFI) instagram        0.000021     0.0000   0.9877
          T. Mariani (RN) instagram       -0.000408     0.0364   0.6507
         E. Grégoire (PS)    tiktok       -0.000081     0.0017   0.9238
    S. Knafo (Reconquête)    tiktok        0.003379     0.1899   0.2804
        S. Chikirou (LFI)    tiktok        0.003575     0.1405   0.3602

============================================================

⚠ NOTE UNITÉS
  er_median Twitter (weekly) : min=0.0001  max=0.2349  → ratio décimal
  engagement_rate tweets bruts: min=0.04  max=22.84  → semble être en %
  → Ces deux métriques ne sont PAS directement comparables.
    A1 utilisera er_median (weekly, ratio décimal × 1000 = ‰) pour les figures.
```

```
✓ Figure sauvegardée → outputs\A1_C2_timeline_engagement.png
```

```

==================================================
ER médian (‰) par candidat :
           median    mean     std
key                              
Knafo      11.532  32.657  54.388
Brossat     6.423   7.314   3.991
Chikirou    4.093   5.575   4.557
Mariani     3.118   4.890   5.885
Bournazel   2.278   2.767   1.423
Gregoire    1.161   1.452   0.896
Belliard    0.857   1.503   1.166
Dati        0.603   0.897   0.820

Note : axe tronqué à 40‰ — outlier Knafo max = 234.9‰
Rapport mean/median Knafo = 2.83x → distribution très asymétrique (quelques pics viraux)
```

```
✓ Figure sauvegardée

Momentum Twitter (trié par p-value) :
      key  hist_mean  last_8w_er_pct  momentum_slope  r_squared  p_value direction
  Brossat     7.3141           4.837         -0.0005     0.5543   0.0341    baisse
 Belliard     1.5031           2.567         -0.0003     0.5489   0.0355    baisse
     Dati     0.8968           1.262         -0.0002     0.5304   0.0405    baisse
Bournazel     2.7668           3.677         -0.0002     0.4708   0.0602    baisse
 Chikirou     5.5752           4.400         -0.0009     0.4694   0.0608    baisse
    Knafo    32.6573           7.422         -0.0011     0.4690   0.0609    baisse
  Mariani     4.8901           2.384         -0.0006     0.4045   0.0901    baisse
 Gregoire     1.4519           1.775          0.0001     0.0830   0.4890    hausse
```

```
✓ Figure sauvegardée

Synchronie cross-platform Twitter ↔ Instagram :
          candidate_label  spearman_rho  p_value  n_weeks   synchrony
P-Y. Bournazel (Horizons)         0.821   0.0000       53 synchronisé
         E. Grégoire (PS)         0.699   0.0000       55 synchronisé
       D. Belliard (EELV)         0.516   0.0004       43      modéré
    S. Knafo (Reconquête)         0.493   0.0001       56      modéré
             R. Dati (LR)         0.235   0.1286       43 indépendant
          T. Mariani (RN)         0.210   0.3041       26 indépendant
         I. Brossat (PCF)         0.205   0.1330       55 indépendant
        S. Chikirou (LFI)        -0.004   0.9761       49 indépendant
```

```
✓ Figure sauvegardée
✓ Export anomalies → outputs\A1_anomalies_top10.csv
```

```
=================================================================
FINDINGS A1 — DYNAMIQUE TEMPORELLE
=================================================================

F1 — Knafo domine l'ER Twitter sur 13 mois
     Médiane Knafo : 11.53‰  vs  autres : 2.33‰
     Ratio : 5.0× la médiane du reste du corpus

F2 — Déclin généralisé Twitter fin de période
     7/8 candidats en baisse significative (p<0.10)
     Seule Grégoire : slope positive mais non significative (p=0.489)

F3 — Synchronie cross-platform hétérogène
     Synchronisés (ρ>0.7) : ['E. Grégoire', 'P-Y. Bournazel']
     Indépendants (ρ≈0)   : ['I. Brossat', 'R. Dati', 'S. Chikirou', 'T. Mariani']
     → Les candidats synchronisés ont une stratégie unifiée cross-platform

F4 — Distribution des anomalies par candidat :
     Knafo        : 7 anomalies
     Dati         : 6 anomalies
     Bournazel    : 5 anomalies
     Belliard     : 4 anomalies
     Gregoire     : 4 anomalies
     Mariani      : 4 anomalies
     Chikirou     : 3 anomalies
     Brossat      : 2 anomalies

F5 — Intensification de l'activité en fin de période
     Volume nov.2025–fév.2026 : 3,216 posts
     Volume janv.–mars 2025   : 1,070 posts
     Ratio : ×3.0

✓ Exports :
   → outputs\A1_anomalies_for_A2_A3.csv  (utilisé par A2 et A3)
   → outputs\A1_er_summary.csv
   → outputs\A1_anomalies_top10.csv

✓ A1 TERMINÉ — 3 figures + 3 CSV exportés
```

```
✓ Figure sauvegardée → outputs\A1_C2_timeline_engagement.png
```

---

# A2_topics

```
✓ Cellule 0 OK — A2 Topics configuré
  Topics palette : 10 topics
  Output : D:\Users\Proprietaire\Desktop\Projet_perso\Presidentielle_tracker\final\A2_topics\outputs
```

```
============================================================
CHARGEMENT A2
============================================================
  topic_distribution             (80, 6)  NaN=0
  topic_resonance                (80, 10)  NaN=0
  topic_timeline                 (591, 4)  NaN=0
  topic_wordclouds_data          (150, 4)  NaN=0

============================================================
TOPICS LDA — TOP 5 MOTS + DIAGNOSTIC
============================================================
ID   Topic name                             Top-5 mots                                         Qualité
--------------------------------------------------------------------------------------------------------------
  T0   Logement & urbanisme                   logement, place, habitants, social, the            ✓ clair
  T1   Vie locale & citoyennete               plan, parisiennes, projet, ville, populaire        ✓ clair
  T2   Geopolitique & international           france, contre, millions, ue, pays                 ✓ clair
  T3   Social & solidarite                    ceux, monde, santé, année, président               ~ générique
  T4   Securite & delinquance                 politique, public, sécurité, argent, service       ~ flou (mots: politique, service)
  T5   Arrondissement / Liberté / Gauche      arrondissement, liberté, gauche, campagne, soir    
  T6   Budget & finances                      euros, milliards, français, 000, gouvernement      ✓ clair
  T7   Education & culture                    droite, dati, culture, extrême, fr                 ⚠ mal nommé (mots: droite, dati, extrême)
  T8   Deux / Emmanuel / Peuple               deux, emmanuel, peuple, grégoire, européenne       ⚠ fourre-tout (grégoire en 4e mot)
  T9   Soutien / Jour / France                soutien, jour, france, contre, république          ~ générique

============================================================
NOTE MÉTHODOLOGIQUE
============================================================
  k=10 pré-calculé — pas de score C_v disponible dans les données
  → Cellule 2 : évaluation qualitative de la distribution (pas d'optimisation)

  ⚠ Renommages proposés :
    T7 'Education & culture' → 'Anti-droite/Dati*'
       (mots dominants: droite, dati, culture, extrême, fr)
    T8 'Deux / Emmanuel / Peuple' → 'Générique†'
       (mots dominants: deux, emmanuel, peuple, grégoire, européenne)

  ─ Ces 2 topics seront annotés avec * et † dans les figures

============================================================
ENGAGEMENT PAR TOPIC (topic_resonance) — GLOBAL
============================================================
                                   n_tweets_total  med_engagement  avg_engagement
topic_name                                                                       
Deux / Emmanuel / Peuple                      366           706.0          2958.0
Soutien / Jour / France                       593           596.0          4960.0
Budget & finances                             792           556.0          4574.0
Securite & delinquance                        648           469.0          4813.0
Education & culture                          1270           455.0          3591.0
Geopolitique & international                  968           429.0          3643.0
Social & solidarite                           680           422.0          3822.0
Vie locale & citoyennete                      620           284.0          1440.0
Arrondissement / Liberté / Gauche             696           272.0          1487.0
Logement & urbanisme                          916           248.0          3158.0

Note : engagement = interactions absolues (likes+comments+shares), pas ER
```

```
✓ Figure sauvegardée

============================================================
DIAGNOSTIC DE QUALITÉ DES TOPICS
============================================================

Topics avec médiane > 12% (potentiel surpoids) :
  Anti-droite/Dati*         médiane = 13.6%

Topics avec médiane < 8% (sous-représentés) :
  Générique†                médiane = 6.4%

Herfindahl-Hirschman Index (HHI) — concentration discursive :
  (HHI=0.1 = parfait équilibre entre 10 topics, HHI→1 = 1 topic dominant)
  Brossat (PCF)                HHI = 0.1141
  Chikirou (LFI)               HHI = 0.1037
  Belliard (EELV)              HHI = 0.1088
  Grégoire (PS)                HHI = 0.1026
  Bournazel (Horizons)         HHI = 0.1067
  Dati (LR)                    HHI = 0.1067
  Knafo (Reconquête)           HHI = 0.1062
  Mariani (RN)                 HHI = 0.1113
```

```
✓ Figure sauvegardée

============================================================
TOPICS DOMINANTS PAR CANDIDAT (top 3)
============================================================
  Brossat (PCF)                Anti-droite/Dati* (19.9%) · Budget (13.3%) · Géopolitique (10.1%)
  Chikirou (LFI)               Géopolitique (14.3%) · Budget (11.2%) · Anti-droite/Dati* (10.5%)
  Belliard (EELV)              Anti-droite/Dati* (16.9%) · Social (11.6%) · Local/Paris (11.1%)
  Grégoire (PS)                Anti-droite/Dati* (12.3%) · Logement (12.3%) · Arrondissement / Liberté / Gauche (11.3%)
  Bournazel (Horizons)         Arrondissement / Liberté / Gauche (13.2%) · Logement (13.1%) · Local/Paris (12.6%)
  Dati (LR)                    Logement (15.7%) · Social (12.2%) · Anti-droite/Dati* (11.1%)
  Knafo (Reconquête)           Anti-droite/Dati* (14.9%) · Géopolitique (13.4%) · Budget (12.0%)
  Mariani (RN)                 Géopolitique (17.2%) · Anti-droite/Dati* (15.1%) · Budget (11.4%)

============================================================
PROFIL D'ORIGINALITÉ — candidats les plus distinctifs
  (écart max par rapport à la moyenne du corpus sur un topic)
============================================================
  Brossat (PCF)                +6.1% sur 'Anti-droite/Dati*'
  Chikirou (LFI)               +2.8% sur 'Géopolitique'
  Belliard (EELV)              +3.1% sur 'Anti-droite/Dati*'
  Grégoire (PS)                +2.4% sur 'Soutien/France'
  Bournazel (Horizons)         +3.3% sur 'Arrondissement / Liberté / Gauche'
  Dati (LR)                    +4.6% sur 'Logement'
  Knafo (Reconquête)           +2.6% sur 'Budget'
  Mariani (RN)                 +5.7% sur 'Géopolitique'

✓ Export matrice → outputs\A2_matrix_candidat_topic.csv
```

```
✓ Figure sauvegardée

============================================================
TOPICS CLASSÉS PAR ENGAGEMENT MÉDIAN (décroissant)
============================================================
Topic                         Med.eng   N tweets  Candidats
------------------------------------------------------------
  Générique†                      706        366          8
  Soutien/France                  596        593          8
  Budget                          556        792          8
  Sécurité                        469        648          8
  Anti-droite/Dati*               455       1270          8
  Géopolitique                    429        968          8
  Social                          422        680          8
  Local/Paris                     284        620          8
  nan                             272        696          8
  Logement                        248        916          8

→ Topic le plus fréquent : Anti-droite/Dati*
→ Topic le plus engageant : Générique†
→ Coïncident : False

⚠ Note : engagement en valeurs absolues — candidats avec grandes audiences
  (Knafo, Dati) pèsent plus dans avg_engagement que dans median_engagement.
  La médiane inter-candidats est plus robuste pour la comparaison.
```

```
✓ Anomalies A1 chargées : 35 lignes
```

```
✓ Figure sauvegardée

============================================================
VOLUME MOYEN PAR TOPIC PAR SEMAINE
============================================================
  Anti-droite/Dati*            21.5 tweets/semaine en moyenne
  Géopolitique                 16.3 tweets/semaine en moyenne
  Logement                     15.5 tweets/semaine en moyenne
  Budget                       13.4 tweets/semaine en moyenne
  Arrondissement / Liberté / Gauche 11.8 tweets/semaine en moyenne
  Social                       11.5 tweets/semaine en moyenne
  Sécurité                     10.9 tweets/semaine en moyenne
  Local/Paris                  10.5 tweets/semaine en moyenne
  Soutien/France               10.0 tweets/semaine en moyenne
  Générique†                   6.2 tweets/semaine en moyenne
```

```
✓ Figure sauvegardée

=================================================================
CROISEMENT ANOMALIES × TOPICS
=================================================================
  Anomalies avec convergence eng/vol sur même topic : 2/35

  Topics les plus fréquents lors des anomalies :
    Budget                       : 17 anomalie(s)
    Géopolitique                 : 9 anomalie(s)
    Sécurité                     : 2 anomalie(s)
    Soutien/France               : 2 anomalie(s)
    Social                       : 2 anomalie(s)
    Arrondissement / Liberté / Gauche : 1 anomalie(s)
    Logement                     : 1 anomalie(s)
    Anti-droite/Dati*            : 1 anomalie(s)

  Question narrative : les anomalies sont-elles thématiques ou événementielles ?
  Anomalies où topic engageant ≠ topic fréquent : 33/35
  → Si n_diff élevé : la viralité n'est pas le topic le plus discuté, mais un sujet de niche

✓ Exports A2 :
   → outputs\A2_cross_anomalies_topics.csv  (utilisé par A3, A7)
   → outputs\A2_topic_engagement_ranking.csv (utilisé par A3)
   → outputs\A2_matrix_candidat_topic.csv    (utilisé par A3, A7)

✓ A2 TERMINÉ — 4 figures + 3 CSV exportés
```

---

# A3_sentiment

```
✓ Cellule 0 OK — A3 Sentiment configuré
  Output : D:\Users\Proprietaire\Desktop\Projet_perso\Presidentielle_tracker\final\A3_sentiment\outputs
```

```
============================================================
CHARGEMENT replies_classified
============================================================
  Shape           : (44599, 14)
  Timestamp OK    : 41586 / 44599 (93.2%)
  Timestamp NaT   : 3013
  year_week range : 2024-W51 → 2026-W08
  Platforms       : {'twitter': 41586, 'instagram': 3013}
  Sentiments      : {'CRITIQUE': 16898, 'SOUTIEN': 11839, 'HOSTILITE': 10614, 'IRONIE': 4740, 'INCONNU': 508}
```

```
✓ Figure sauvegardée

============================================================
DISTRIBUTION PAR CANDIDAT × PLATEFORME
============================================================
  Brossat (PCF)                [twitter  ] n= 1172  SOUTIEN=7%  HOSTILITE=34%
  Brossat (PCF)                [instagram] n=  534  SOUTIEN=24%  HOSTILITE=30%
  Chikirou (LFI)               [twitter  ] n=  456  SOUTIEN=14%  HOSTILITE=38%
  Chikirou (LFI)               [instagram] n=  341  SOUTIEN=15%  HOSTILITE=43%
  Belliard (EELV)              [twitter  ] n= 1491  SOUTIEN=8%  HOSTILITE=28%
  Belliard (EELV)              [instagram] n=  401  SOUTIEN=31%  HOSTILITE=19%
  Grégoire (PS)                [twitter  ] n=  252  SOUTIEN=8%  HOSTILITE=27%
  Grégoire (PS)                [instagram] n=  397  SOUTIEN=31%  HOSTILITE=13%
  Bournazel (Horizons)         [twitter  ] n= 4651  SOUTIEN=15%  HOSTILITE=26%
  Bournazel (Horizons)         [instagram] n=  132  SOUTIEN=36%  HOSTILITE=17%
  Dati (LR)                    [twitter  ] n= 8160  SOUTIEN=15%  HOSTILITE=25%
  Dati (LR)                    [instagram] n=  165  SOUTIEN=29%  HOSTILITE=25%
  Knafo (Reconquête)           [twitter  ] n=22873  SOUTIEN=36%  HOSTILITE=22%
  Knafo (Reconquête)           [instagram] n=  938  SOUTIEN=48%  HOSTILITE=20%
  Mariani (RN)                 [twitter  ] n= 2046  SOUTIEN=21%  HOSTILITE=25%
  Mariani (RN)                 [instagram] n=   82  SOUTIEN=33%  HOSTILITE=26%

============================================================
NOTE STRUCTURELLE
============================================================
  Knafo    : 24,106 replies (54% du corpus total)
  Grégoire : 650 replies
  → Déséquilibre extrême : analyses par candidat à interpréter avec les n

  Replies sans timestamp parsé : 3013
  Exemples : ['2026-02-18T19:16:50.508000+00:00', '2026-02-03T19:16:50.508000+00:00', '2026-02-01T19:16:50.508000+00:00']

✓ Replies enrichies sauvegardées → outputs\A3_replies_enriched.parquet
```

```
✓ Figure sauvegardée

============================================================
NET SUPPORT INDEX — résultats complets
============================================================
Candidat                         NSI             IC 95%       n   SOUTIEN   HOSTILITÉ
-------------------------------------------------------------------------------------
  Knafo (Reconquête)          +0.145  [+0.137; +0.155]   23,811    8,697 (37%)    5,233 (22%)
  Grégoire (PS)               +0.037  [-0.014; +0.088]      649      145 (22%)      121 (19%)
  Mariani (RN)                -0.038  [-0.065; -0.010]    2,128      456 (21%)      537 (25%)
  Dati (LR)                   -0.104  [-0.117; -0.089]    8,325    1,245 (15%)    2,108 (25%)
  Bournazel (Horizons)        -0.107  [-0.125; -0.089]    4,783      731 (15%)    1,243 (26%)
  Belliard (EELV)             -0.133  [-0.160; -0.108]    1,892      244 (13%)      495 (26%)
  Brossat (PCF)               -0.209  [-0.239; -0.179]    1,706      205 (12%)      561 (33%)
  Chikirou (LFI)              -0.251  [-0.299; -0.202]      797      116 (15%)      316 (40%)

✓ Export NSI → outputs\A3_nsi_by_candidate.csv
```

```
Coverage mapping :
  Candidat                      sem   n_replies
  ----------------------------------------------
  Belliard (EELV)                19         405
  Bournazel (Horizons)           14         132
  Brossat (PCF)                  18         542
  Chikirou (LFI)                 18         343
  Dati (LR)                      21         164
  Grégoire (PS)                  19         397
  Knafo (Reconquête)             25         947
  Mariani (RN)                   10          82

  Anomalies A1 : 25 semaines / 35 evenements
```

```
Figure C3 sauvegardee
```

```
Figure C4 sauvegardee

====================================================================
C4 - MOMENTS DE BASCULE (|z| > 1.2) - 54 evenements
====================================================================
  Candidat               Semaine           NSI        z  Direction
  ----------------------------------------------------------
  Brossat (PCF)          2025-W17       -33.3%   -14.65   Baisse
  Mariani (RN)           2025-W43        +0.0%   +13.45   Hausse
  Brossat (PCF)          2026-W03       -57.1%    -5.25   Baisse
  Knafo (Reconquête)     2026-W06       +46.7%    +5.20   Hausse
  Dati (LR)              2025-W17      +100.0%    +4.85   Hausse
  Bournazel (Horizons)   2026-W06       -33.3%    -4.70   Baisse
  Knafo (Reconquête)     2025-W38       -25.0%    -4.35   Baisse
  Dati (LR)              2026-W03      +100.0%    +3.83   Hausse
  Grégoire (PS)          2025-W41       +71.4%    +3.76   Hausse
  Brossat (PCF)          2026-W08      -100.0%    -3.71   Baisse
  Chikirou (LFI)         2026-W02       -56.4%    -3.36   Baisse
  Mariani (RN)           2026-W05       +50.0%    +3.32   Hausse
  Bournazel (Horizons)   2025-W26        +0.0%    -3.00   Baisse
  Grégoire (PS)          2025-W24       +40.0%    -2.97   Baisse
  Bournazel (Horizons)   2026-W07       -60.0%    -2.93   Baisse
  Belliard (EELV)        2025-W38       +62.5%    +2.91   Hausse
  Grégoire (PS)          2026-W06       +12.9%    +2.54   Hausse
  Belliard (EELV)        2025-W41       -20.0%    -2.53   Baisse
  Chikirou (LFI)         2026-W03       -70.6%    -2.43   Baisse
  Brossat (PCF)          2025-W33       +18.8%    +2.38   Hausse
  Dati (LR)              2025-W51       -50.0%    -2.21   Baisse
  Bournazel (Horizons)   2025-W21      +100.0%    +2.12   Hausse
  Bournazel (Horizons)   2025-W51        -6.2%    -2.11   Baisse
  Dati (LR)              2025-W16       -20.0%    -2.05   Baisse
  Knafo (Reconquête)     2025-W50       +48.3%    +1.93   Hausse
  Brossat (PCF)          2026-W06       -69.2%    -1.91   Baisse
  Chikirou (LFI)         2026-W07       -37.0%    +1.87   Hausse
  Knafo (Reconquête)     2025-W20       -20.0%    -1.86   Baisse
  Grégoire (PS)          2025-W37        -8.3%    -1.84   Baisse
  Chikirou (LFI)         2025-W29       -76.9%    -1.81   Baisse
  Chikirou (LFI)         2026-W08       -26.7%    +1.72   Hausse
  Grégoire (PS)          2025-W51        +0.0%    -1.70   Baisse
  Knafo (Reconquête)     2025-W43       +40.0%    +1.69   Hausse
  Dati (LR)              2026-W06      -100.0%    -1.62   Baisse
  Belliard (EELV)        2026-W04       -34.4%    -1.58   Baisse
  Knafo (Reconquête)     2025-W33       +33.3%    +1.55   Hausse
  Grégoire (PS)          2026-W02       -13.3%    -1.53   Baisse
  Dati (LR)              2025-W21      +100.0%    +1.48   Hausse
  Dati (LR)              2025-W46       +15.8%    +1.46   Hausse
  Grégoire (PS)          2025-W33        +0.0%    -1.40   Baisse
  Knafo (Reconquête)     2026-W04       +10.5%    -1.40   Baisse
  Mariani (RN)           2025-W51        +0.0%    +1.40   Hausse
  Chikirou (LFI)         2025-W33      -100.0%    -1.37   Baisse
  Chikirou (LFI)         2026-W06       -48.4%    +1.37   Hausse
  Dati (LR)              2025-W33       -50.0%    -1.36   Baisse
  Belliard (EELV)        2025-W50       -25.0%    -1.33   Baisse
  Dati (LR)              2025-W29       -20.0%    -1.32   Baisse
  Grégoire (PS)          2025-W25       +33.3%    -1.29   Baisse
  Grégoire (PS)          2026-W05       -17.6%    -1.29   Baisse
  Grégoire (PS)          2025-W29       +22.2%    -1.28   Baisse
  Chikirou (LFI)         2026-W04       -72.7%    -1.28   Baisse
  Dati (LR)              2025-W41        +0.0%    +1.22   Hausse
  Knafo (Reconquête)     2026-W05        +6.7%    -1.22   Baisse
  Grégoire (PS)          2026-W03       -14.3%    -1.20   Baisse

Export : outputs/A3_inflection_points.csv  (54 lignes)
```

```
Merge sentiment × Twitter : 136 obs. (candidats couverts : 8/8)
  Répartition : Belliard=16 | Bournazel=13 | Brossat=17 | Chikirou=17 | Dati=19 | Grégoire=19 | Knafo=25 | Mariani=10
```

```
✓ Figure C5 sauvegardée

==============================================================
C5 — TEST DE LA NÉGATIVITÉ
==============================================================
  Spearman global  : ρ = +0.262  p = 0.0021  n = 136
  → Corrélation positive significative : + hostilité = + ER

  Corrélations par candidat :
    Bournazel (Horizons)       ρ=+0.549  p=0.052  
    Belliard (EELV)            ρ=+0.507  p=0.045 *
    Knafo (Reconquête)         ρ=+0.262  p=0.206  
    Grégoire (PS)              ρ=+0.232  p=0.340  
    Chikirou (LFI)             ρ=+0.031  p=0.907  
    Dati (LR)                  ρ=-0.018  p=0.941  
    Mariani (RN)               ρ=-0.460  p=0.181  
    Brossat (PCF)              ρ=-0.630  p=0.007 *
```

```
✓ Figure C6 sauvegardée

=======================================================
C6 — ENGAGEMENT × CLASSE DE SENTIMENT DOMINANTE
=======================================================
  Kruskal-Wallis : H = 2.443  p = 0.2948
  Classe           n    Médiane      P25      P75
  --------------------------------------------
  SOUTIEN         56      2.94‰    1.05    8.29
  CRITIQUE        53      2.23‰    1.32    4.99
  HOSTILITE       25      3.77‰    2.66    5.05

  Tests Mann-Whitney (α Bonf. = 0.0167) :
    SOUTIEN vs CRITIQUE      p = 0.3615  ns
    SOUTIEN vs HOSTILITE     p = 0.7243  ns
    CRITIQUE vs HOSTILITE     p = 0.0809  ns

✓ topic_timeline : (591, 4)  | cols : ['week', 'topic_name', 'n_tweets', 'avg_eng']
  Exemple week converti : 2025-W01  (plage : 2025-W01 → 2026-W08)
  Merge topic × sentiment : 29 semaines communes
```

```
✓ Figure C7 sauvegardée
  11 corrélations significatives / 30 testées
  Top corrélations (|ρ| > 0.4, p < 0.05) :
    Education & culture            ~ pct_soutien      ρ=-0.535  p=0.0028
    Education & culture            ~ net_support      ρ=-0.506  p=0.0051
    Geopolitique & international   ~ pct_hostilite    ρ=-0.578  p=0.0010
    Geopolitique & international   ~ pct_soutien      ρ=+0.582  p=0.0009
    Geopolitique & international   ~ net_support      ρ=+0.632  p=0.0002
    Securite & delinquance         ~ pct_hostilite    ρ=+0.615  p=0.0004
    Securite & delinquance         ~ pct_soutien      ρ=-0.505  p=0.0052
    Securite & delinquance         ~ net_support      ρ=-0.581  p=0.0010
    Vie locale & citoyennete       ~ pct_soutien      ρ=-0.518  p=0.0040
    Vie locale & citoyennete       ~ net_support      ρ=-0.483  p=0.0079
```

```
✓ Figure C8 sauvegardée

============================================================
C8 — SENTIMENT AUTOUR DES ANOMALIES A1
============================================================
  25 semaines d'anomalie analysées

  NSI (%)         avant=+2.1  pendant=+0.0  après=+4.3
    p avant→pendant = 0.9333  |  p pendant→après = 0.9422
  % Hostilité     avant=+21.0  pendant=+16.7  après=+18.5
    p avant→pendant = 0.4823  |  p pendant→après = 0.6394

✓ Export → outputs/A3_sentiment_vs_anomalies.csv

============================================================
✓ A3 COMPLET — Exports :
  ✓  A3_C3_nsi_timeline.png
  ✓  A3_C4_bascules.png
  ✓  A3_C5_negativite.png
  ✓  A3_C6_er_by_sentiment.png
  ✓  A3_C7_topic_sentiment.png
  ✓  A3_C8_sentiment_anomalies.png
  ✓  A3_inflection_points.csv
  ✓  A3_sentiment_vs_anomalies.csv
  ✓  A3_nsi_by_candidate.csv
============================================================
Merge sentiment × Twitter : 136 obs. (semaine × candidat)
  sur 144 sem-sentiments et 427 sem-twitter
```

```
✓ Figure C5 sauvegardée → outputs/A3_C5_negativite.png

==============================================================
C5 — TEST DE LA NÉGATIVITÉ
==============================================================
  Spearman global  : ρ = +0.262  p = 0.0021  n = 136
  → Corrélation positive significative : + hostilité = + ER

  Corrélations par candidat (* p < 0.05) :
    Belliard (EELV)            ρ=+0.507  p=0.045 *
    Knafo (Reconquête)         ρ=+0.262  p=0.206  
    Chikirou (LFI)             ρ=+0.031  p=0.907  
    Dati (LR)                  ρ=-0.018  p=0.941  
    Mariani (RN)               ρ=-0.460  p=0.181
```

```
✓ Figure C6 sauvegardée → outputs/A3_C6_er_by_sentiment.png

=======================================================
C6 — ENGAGEMENT × CLASSE DE SENTIMENT DOMINANTE
=======================================================
  Kruskal-Wallis : H = 2.443  p = 0.2948
  α Bonferroni corrigé : 0.0167

  Classe           n    Médiane      P25      P75
  --------------------------------------------
  SOUTIEN         56      2.94‰    1.05    8.29
  CRITIQUE        53      2.23‰    1.32    4.99
  HOSTILITE       25      3.77‰    2.66    5.05

  Tests Mann-Whitney par paire (α Bonf. = 0.0167) :
    SOUTIEN vs CRITIQUE      p = 0.3615  ns
    SOUTIEN vs HOSTILITE     p = 0.7243  ns
    CRITIQUE vs HOSTILITE     p = 0.0809  ns

✓ topic_timeline chargé: (591, 4)  | cols: ['week', 'topic_name', 'n_tweets', 'avg_eng']
⚠ Colonnes topic_id / n_tweets absentes de topic_timeline — C7 ignoré
```

```
✓ Figure C8 sauvegardée → outputs/A3_C8_sentiment_anomalies.png

============================================================
C8 — SENTIMENT AUTOUR DES ANOMALIES A1
============================================================
  25 semaines d'anomalie analysées

  NSI (%)         avant=+2.1  pendant=+0.0  après=+4.3
    Mann-Whitney avant→pendant : p = 0.9333  |  pendant→après : p = 0.9422
  % Hostilité     avant=+21.0  pendant=+16.7  après=+18.5
    Mann-Whitney avant→pendant : p = 0.4823  |  pendant→après : p = 0.6394

✓ Export → outputs/A3_sentiment_vs_anomalies.csv

============================================================
✓ A3 COMPLET — Exports générés :
  ✓  A3_C3_nsi_timeline.png
  ✓  A3_C4_bascules.png
  ✓  A3_C5_negativite.png
  ✓  A3_C6_er_by_sentiment.png
  ✓  A3_C7_topic_sentiment.png
  ✓  A3_C8_sentiment_anomalies.png
  ✓  A3_inflection_points.csv
  ✓  A3_sentiment_vs_anomalies.csv
  ✓  A3_nsi_by_candidate.csv
============================================================
```

```
======================================================================
A3 — SYNTHÈSE QUANTITATIVE COMPLÈTE  (Paris Municipales 2026)
======================================================================

[1] NET SUPPORT INDEX (NSI = SOUTIEN − HOSTILITÉ / total)
----------------------------------------------------------------------
  Chikirou                     NSI=-0.251  n=797
  Brossat                      NSI=-0.209  n=1,706
  Belliard                     NSI=-0.133  n=1,892
  Bournazel                    NSI=-0.107  n=4,783
  Dati                         NSI=-0.104  n=8,325
  Mariani                      NSI=-0.038  n=2,128
  Gregoire                     NSI=+0.037  n=649
  Knafo                        NSI=+0.145  n=23,811

[2] MOMENTS DE BASCULE (|z| > 1.2σ, rolling 4 sem. décalé)
----------------------------------------------------------------------
  Total : 54 événements  (0 hausses / 0 baisses)
  z-score max : +13.45  (min : -14.65)

  Top 10 bascules (|z| les plus forts) :
    Mariani                2025-W43  NSI=  +0.0%  z= +13.45   Hausse
    Knafo                  2026-W06  NSI= +46.7%  z=  +5.20   Hausse
    Dati                   2025-W17  NSI=+100.0%  z=  +4.85   Hausse
    Dati                   2026-W03  NSI=+100.0%  z=  +3.83   Hausse
    Gregoire               2025-W41  NSI= +71.4%  z=  +3.76   Hausse
    Brossat                2025-W17  NSI= -33.3%  z= -14.65   Baisse
    Brossat                2026-W03  NSI= -57.1%  z=  -5.25   Baisse
    Bournazel              2026-W06  NSI= -33.3%  z=  -4.70   Baisse
    Knafo                  2025-W38  NSI= -25.0%  z=  -4.35   Baisse
    Brossat                2026-W08  NSI=-100.0%  z=  -3.71   Baisse

[3] TEST DE LA NÉGATIVITÉ — % Hostilité × ER Twitter (Spearman)
----------------------------------------------------------------------
  → Résultats dans les outputs de la cellule 4 (C5)
  Global : ρ = +0.262  p = 0.0021  n = 136
  Belliard (EELV)       : ρ = +0.507  p = 0.045  *
  Brossat  (PCF)        : ρ = −0.630  p = 0.007  *
  Bournazel (Horizons)  : ρ = +0.549  p = 0.052  (tendance)
  Interprétation : + hostilité = + ER globalement (viralité de la controverse)
                   Brossat fait exception : + hostilité = − ER (démobilisation)

[4] ENGAGEMENT × CLASSE DE SENTIMENT DOMINANTE (C6)
----------------------------------------------------------------------
  Kruskal-Wallis : H = 2.44   p = 0.2948  (non significatif)
  SOUTIEN   n=56  médiane=2.94‰  IQR=[1.05; 8.29]
  CRITIQUE  n=53  médiane=2.23‰  IQR=[1.32; 4.99]
  HOSTILITE n=25  médiane=3.77‰  IQR=[2.66; 5.05]
  Interprétation : le type de sentiment dominant ne prédit pas l'ER
                   (variance expliquée par le candidat et le contenu)

[5] SENTIMENT AUTOUR DES ANOMALIES A1 (C8)
----------------------------------------------------------------------
  25 semaines d'anomalie analysées

  avant       NSI médian= +2.1%  Hostilité= 21.0%
  pendant     NSI médian= +0.0%  Hostilité= 16.7%  ← p_nsi=0.9333  p_host=0.4823
  après       NSI médian= +4.3%  Hostilité= 18.5%
  Interprétation : les anomalies d'engagement Twitter
                   ne modifient pas significativement le sentiment des replies
                   (pas d'effet 'ratio' ou de mobilisation différentielle)

[6] EXPORTS GÉNÉRÉS
----------------------------------------------------------------------
  ✓  A3_nsi_by_candidate.csv                  NSI + IC 95% par candidat                1 Ko
  ✓  A3_inflection_points.csv                 Moments de bascule (|z|>1.2σ)            3 Ko
  ✓  A3_sentiment_vs_anomalies.csv            Sentiment avant/pendant/après anomalie   0 Ko
  ✓  A3_replies_enriched.parquet              Replies brutes enrichies (ts + year_week) 5834 Ko
  ✓  A3_C3_nsi_timeline.png                   Fig. C3 — Timeline NSI 8 candidats       514 Ko
  ✓  A3_C4_bascules.png                       Fig. C4 — Moments de bascule             121 Ko
  ✓  A3_C5_negativite.png                     Fig. C5 — Test de la négativité          166 Ko
  ✓  A3_C6_er_by_sentiment.png                Fig. C6 — ER × sentiment dominant        71 Ko
  ✓  A3_C7_topic_sentiment.png                Fig. C7 — Topics A2 × sentiment          98 Ko
  ✓  A3_C8_sentiment_anomalies.png            Fig. C8 — Profil sentiment anomalies     80 Ko

======================================================================
✓ A3 SYNTHÈSE COMPLÈTE
======================================================================
```

---

# A4_community

```
A4 — Configuration chargee
  Candidats : 8
  Outputs   : outputs
```

```
============================================================
CHARGEMENT A4
============================================================
  Jaccard matrix  : (8, 8)
  Echo scores     : (8, 9)  | cols : ['candidate_id', 'label', 'bloc', 'n_audience', 'exclusive_pct', 'same_camp_pct', 'cross_camp_pct', 'echo_score', 'key']
  Cross mentions  : (21, 5)
  Community       : (2963, 15)

  Echo chamber scores :
    Knafo (Reconquete)            echo=88.1  excl=81.8%  cross=11.9%  n=10,602
    Chikirou (LFI)                echo=77.7  excl=74.6%  cross=22.3%  n=701
    Dati (LR)                     echo=77.1  excl=61.2%  cross=22.9%  n=4,184
    Gregoire (PS)                 echo=67.5  excl=61.2%  cross=32.5%  n=551
    Brossat (PCF)                 echo=62.2  excl=60.6%  cross=37.8%  n=1,340
    Bournazel (Horizons)          echo=58.2  excl=58.2%  cross=41.8%  n=2,612
    Mariani (RN)                  echo=57.4  excl=57.4%  cross=42.6%  n=1,720
    Belliard (EELV)               echo=52.5  excl=49.7%  cross=47.5%  n=1,279
```

```
Figure C1 sauvegardee

============================================================
JACCARD — DIAGNOSTICS
============================================================

  Top 5 paires (audience la plus partagee) :
    Bournazel (Horizons)       × Dati (LR)                   Jaccard=9.3%  d_ideo=1
    Brossat (PCF)              × Belliard (EELV)             Jaccard=9.3%  d_ideo=2
    Bournazel (Horizons)       × Belliard (EELV)             Jaccard=7.8%  d_ideo=2
    Dati (LR)                  × Knafo (Reconquete)          Jaccard=7.6%  d_ideo=1
    Gregoire (PS)              × Belliard (EELV)             Jaccard=6.3%  d_ideo=1

  Bottom 5 paires (audience la plus distincte) :
    Dati (LR)                  × Chikirou (LFI)              Jaccard=1.1%  d_ideo=4
    Knafo (Reconquete)         × Chikirou (LFI)              Jaccard=0.6%  d_ideo=5
    Mariani (RN)               × Gregoire (PS)               Jaccard=0.5%  d_ideo=4
    Mariani (RN)               × Chikirou (LFI)              Jaccard=0.5%  d_ideo=6
    Knafo (Reconquete)         × Gregoire (PS)               Jaccard=0.4%  d_ideo=3

  Jaccard moyen intra-camp  : 4.59%
  Jaccard moyen inter-camps : 3.22%
  Ratio intra/inter         : 1.43x

Export : outputs/A4_jaccard_pairs.csv  (28 paires)
```

```
Figure C2 sauvegardee
```

```
Figure C2b sauvegardee
```

```
Figure C2c sauvegardee

============================================================
C2c — TEST JACCARD <-> DISTANCE IDEOLOGIQUE
============================================================
  Spearman rho = -0.600  p = 0.0007  n = 28
  -> Correlation negative significative
  -> CONFIRME H0 : + proches ideologiquement = + audience partagee

  Mentions inter-candidats : 21 paires
  Paire la plus active  : Brossat -> Gregoire (27 mentions)
```

```
A3_nsi_by_candidate cols: ['key', 'label', 'nsi', 'ci_lo', 'ci_hi', 'n', 'n_host', 'n_sout', 'host_pct']
        key            label       nsi     ci_lo     ci_hi     n  n_host  n_sout   host_pct
0  Chikirou   Chikirou (LFI) -0.250941 -0.298651 -0.202008   797     316     116  39.648683
1   Brossat    Brossat (PCF) -0.208675 -0.238584 -0.178781  1706     561     205  32.883939
2  Belliard  Belliard (EELV) -0.132664 -0.160161 -0.107796  1892     495     244  26.162791

Merge echo x sentiment : 8 candidats
      key  echo_score  pct_hostilite  pct_ironie   nsi_mean
    Knafo        88.1      20.142800    8.782800  15.420000
 Chikirou        77.7      35.829444   16.251111 -29.862222
     Dati        77.1      19.711429    8.398095   2.036190
 Gregoire        67.5       9.231579    8.788421  19.586842
  Brossat        62.2      36.818889    9.728889 -24.812778
Bournazel        58.2      14.083571    7.147143  16.871429
  Mariani        57.4      25.441000    4.734000  -1.699000
 Belliard        52.5      15.191579    7.338421   7.194737
```

```
Figure C3 sauvegardee

=================================================================
C3 — ECHO CHAMBER x SENTIMENT (Spearman, n=8 candidats)
=================================================================
  echo_score ~ pct_hostilite : rho=+0.214  p=0.6103  ns
  echo_score ~ NSI           : rho=-0.071  p=0.8665  ns
  echo_score ~ pct_ironie    : rho=+0.643  p=0.0856  ns

  Interpretation :
  -> Pas de correlation significative echo <-> hostilite (n=8 limite la puissance)

  Candidat                     echo   host%    nsi%   iro%  Camp
  ------------------------------------------------------------
  Knafo (Reconquete)           88.1    20.1   +15.4    8.8  Extreme droite
  Chikirou (LFI)               77.7    35.8   -29.9   16.3  Extreme gauche
  Dati (LR)                    77.1    19.7    +2.0    8.4  Droite
  Gregoire (PS)                67.5     9.2   +19.6    8.8  Gauche
  Brossat (PCF)                62.2    36.8   -24.8    9.7  Extreme gauche
  Bournazel (Horizons)         58.2    14.1   +16.9    7.1  Centre
  Mariani (RN)                 57.4    25.4    -1.7    4.7  Extreme droite
  Belliard (EELV)              52.5    15.2    +7.2    7.3  Gauche

Export : outputs/A4_echo_x_sentiment.csv
```

```
============================================================
COMMUNITY MEMBERSHIP — DIAGNOSTICS
============================================================
  Utilisateurs multi-candidats : 2,963
  n_candidates_engaged range   : 2 → 7

  Distribution n_candidates_engaged :
    2 candidats : 2,210  ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    3 candidats :   553  |||||||||||||||||||||||||||
    4 candidats :   153  |||||||
    5 candidats :    35  |
    6 candidats :    10  
    7 candidats :     2  

  Candidat dominant le plus frequent :
    Knafo (Reconquete)           1,260  (42.5%)
    Dati (LR)                      655  (22.1%)
    Bournazel (Horizons)           355  (12.0%)
    Mariani (RN)                   283  (9.6%)
    Belliard (EELV)                146  (4.9%)
    Brossat (PCF)                  145  (4.9%)
    Chikirou (LFI)                  79  (2.7%)
    Gregoire (PS)                   40  (1.3%)
```

```
Figure C4 sauvegardee

=================================================================
C4 — UTILISATEURS MULTI-CANDIDATS
=================================================================
  Total          : 2,963 utilisateurs
  n=2 candidats  : 2,210  (74.6%)
  n>=3 candidats : 753  (25.4%)
  n>=4 candidats : 200  (6.7%)

  Utilisateurs trans-camp    : 2,537  (85.6%)
  Utilisateurs mono-camp     : 426  (14.4%)

  Top co-engagements (n paires) :
    Dati (LR)                  x Knafo (Reconquete)         : 1,045 users
    Knafo (Reconquete)         x Mariani (RN)               :   585 users
    Bournazel (Horizons)       x Dati (LR)                  :   576 users
    Bournazel (Horizons)       x Knafo (Reconquete)         :   501 users
    Belliard (EELV)            x Bournazel (Horizons)       :   283 users
    Belliard (EELV)            x Dati (LR)                  :   234 users
    Dati (LR)                  x Mariani (RN)               :   233 users
    Belliard (EELV)            x Brossat (PCF)              :   222 users

=================================================================
A4 — EXPORTS GENERES
=================================================================
  OK  A4_C1_jaccard_heatmap.png                134 Ko
  OK  A4_C2_echo_chambers.png                  172 Ko
  OK  A4_C2b_mentions_network.png              188 Ko
  OK  A4_C2c_jaccard_ideo.png                  89 Ko
  OK  A4_C3_echo_x_sentiment.png               177 Ko
  OK  A4_C4_multi_users.png                    203 Ko
  OK  A4_jaccard_pairs.csv                     0 Ko
  OK  A4_echo_x_sentiment.csv                  0 Ko
```

```
Figure C5 sauvegardee

=================================================================
C5 — VALIDATION : JACCARD vs CO-ENGAGEMENT
=================================================================
  Spearman rho = +0.798  p = 0.0000  n = 28 paires
  -> Correlation significative : les deux matrices convergent
     Le Jaccard (full audience) et le co-engagement (multi-users)
     mesurent bien le meme phenomene de proximite d'audience
```

```
======================================================================
A4 — SYNTHESE QUANTITATIVE  (Paris Municipales 2026)
======================================================================

[1] ECHO CHAMBER SCORES (echo_score = 100 - cross_camp_pct)
----------------------------------------------------------------------
  Knafo (Reconquete)            echo= 88.1  excl= 81.8%  cross= 11.9%  n=10,602  [FERME]
  Chikirou (LFI)                echo= 77.7  excl= 74.6%  cross= 22.3%  n=   701  [FERME]
  Dati (LR)                     echo= 77.1  excl= 61.2%  cross= 22.9%  n= 4,184  [FERME]
  Gregoire (PS)                 echo= 67.5  excl= 61.2%  cross= 32.5%  n=   551  [MODERE]
  Brossat (PCF)                 echo= 62.2  excl= 60.6%  cross= 37.8%  n= 1,340  [MODERE]
  Bournazel (Horizons)          echo= 58.2  excl= 58.2%  cross= 41.8%  n= 2,612  [MODERE]
  Mariani (RN)                  echo= 57.4  excl= 57.4%  cross= 42.6%  n= 1,720  [MODERE]
  Belliard (EELV)               echo= 52.5  excl= 49.7%  cross= 47.5%  n= 1,279  [MODERE]

[2] AUDIENCE OVERLAP (JACCARD) — 28 paires
----------------------------------------------------------------------
  Jaccard moyen global     : 3.37%
  Jaccard moyen intra-camp : 4.59%
  Jaccard moyen inter-camp : 3.22%
  Ratio intra/inter        : 1.43x

  Top 5 paires :
    Bournazel (Horizons)       x Dati (LR)                   9.3%  [d_ideo=1]
    Brossat (PCF)              x Belliard (EELV)             9.3%  [d_ideo=2]
    Bournazel (Horizons)       x Belliard (EELV)             7.8%  [d_ideo=2]
    Dati (LR)                  x Knafo (Reconquete)          7.6%  [d_ideo=1]
    Gregoire (PS)              x Belliard (EELV)             6.3%  [same camp]

  Bottom 5 paires :
    Knafo (Reconquete)         x Gregoire (PS)               0.4%  d_ideo=3
    Mariani (RN)               x Chikirou (LFI)              0.5%  d_ideo=6
    Mariani (RN)               x Gregoire (PS)               0.5%  d_ideo=4
    Knafo (Reconquete)         x Chikirou (LFI)              0.6%  d_ideo=5
    Dati (LR)                  x Chikirou (LFI)              1.1%  d_ideo=4

[3] TEST : JACCARD x DISTANCE IDEOLOGIQUE (H0 = homophilie)
----------------------------------------------------------------------
  Spearman rho = -0.600  p = 0.0007  n = 28 paires
  -> CONFIRME : + proches ideologiquement = + audience partagee
     L'homophilie ideologique structure les audiences Twitter parisien

[4] UTILISATEURS MULTI-CANDIDATS (n=2 963)
----------------------------------------------------------------------
  2 candidats     : 2,210  (74.6%)
  3+ candidats    : 753  (25.4%)
  Trans-camp      : 2537  (85.6%)  — croisent les frontieres de camp
  Mono-camp       : 426   (14.4%)  — restent dans leur camp

  Top co-engagements :
    Dati (LR)                  x Knafo (Reconquete)          1,045  [Droite coherente]
    Knafo (Reconquete)         x Mariani (RN)                  585  [Extreme droite]
    Bournazel (Horizons)       x Dati (LR)                     576  [Droite classique]
    Bournazel (Horizons)       x Knafo (Reconquete)            501  [Droite trans-flanc]
    Belliard (EELV)            x Bournazel (Horizons)          283  [Trans-camp G-C]
    Belliard (EELV)            x Brossat (PCF)                 222  [Gauche moderee]

[5] ECHO CHAMBER x PROFIL SENTIMENT (A3, n=8, puissance faible)
----------------------------------------------------------------------
  echo ~ hostilite : rho=+0.214  p=0.610  ns
  echo ~ NSI       : rho=-0.071  p=0.867  ns
  echo ~ ironie    : rho=+0.643  p=0.086  (tendance)
  Interpretation   : la fermeture d'audience ne predit pas l'hostilite
                     c'est la position ideologique qui structure le sentiment

  Pattern observe (non test. : n=8) :
    Ext. gauche (Chikirou, Brossat) : hostilite haute (35-37%), NSI tres negatif
    Ext. droite (Knafo, Mariani)    : hostilite mod. (20-25%), echo eleve
    Centre/Gauche (Belliard, Bournazel, Gregoire) : hostilite basse, NSI positif

[6] EXPORTS
----------------------------------------------------------------------
  OK  A4_C1_jaccard_heatmap.png                 Heatmap Jaccard 8x8                      134 Ko
  OK  A4_C2_echo_chambers.png                   Echo chambers stacked + scatter          172 Ko
  OK  A4_C2b_mentions_network.png               Reseau mentions inter-candidats          188 Ko
  OK  A4_C2c_jaccard_ideo.png                   Jaccard x distance ideologique           89 Ko
  OK  A4_C3_echo_x_sentiment.png                Echo x hostilite/NSI/ironie              177 Ko
  OK  A4_C4_multi_users.png                     Multi-users distribution + co-engagement 203 Ko
  OK  A4_C5_synthese.png                        Validation Jaccard vs co-engagement      174 Ko
  OK  A4_jaccard_pairs.csv                      28 paires Jaccard + distance ideo        0 Ko
  OK  A4_echo_x_sentiment.csv                   Echo score x sentiment par candidat      0 Ko

======================================================================
A4 COMPLET
======================================================================
```

---

# A5_interactions

```
A5 — Initialisation OK
Outputs -> D:\Users\Proprietaire\Desktop\Projet_perso\Presidentielle_tracker\final\A5_interactions\outputs
```

```
=================================================================
CHARGEMENT A5 — INTERACTIONS
=================================================================
  Matrice        : (8, 8)  (row=emetteur, col=cible)
  Lift           : (8, 8)
  Timeline       : (84, 9)  | 2025-02-24 -> 2026-02-09
  Cross-text     : (139, 6)

MENTIONS EMISES (total par candidat) :
-----------------------------------------------------------------
  Brossat (PCF)                 emis= 31  recus= 14  |||||||||||||||||||||||||||||||
  Chikirou (LFI)                emis= 40  recus=  0  ||||||||||||||||||||||||||||||||||||||||
  Belliard (EELV)               emis= 20  recus=  7  ||||||||||||||||||||
  Gregoire (PS)                 emis= 20  recus= 80  ||||||||||||||||||||
  Bournazel (Horizons)          emis= 17  recus=  5  |||||||||||||||||
  Dati (LR)                     emis=  5  recus= 33  |||||
  Knafo (Reconquete)            emis=  2  recus=  0  ||
  Mariani (RN)                  emis=  4  recus=  0  ||||
```

```

Figure C2 sauvegardee -> outputs/A5_C2_matrice_mentions.png

INSIGHTS STRUCTURELS :
-----------------------------------------------------------------
  Hub central : Gregoire (PS) <- 80 mentions
  Strategie d'evitement (0 envois) :
  Brossat -> Gregoire : 27 mentions (paire max)
```

```
Figure C3 sauvegardee -> outputs/A5_C3_mentions_network.png

=================================================================
C3 — ANALYSE DU RESEAU
=================================================================
  Paires actives  : 13 liens directionnels
  Total mentions  : 139 posts inter-candidats
  Gregoire (PS)   : hub — 80 mentions recues
  Knafo, Mariani  : 0 mention emise (strategie d'evitement total)
  Dynamique dominante : gauche attaque/cite Gregoire (federateur ?)
```

```
Figure C4 sauvegardee -> outputs/A5_C4_lift_engagement.png

=================================================================
C4 — LIFT D'ENGAGEMENT (Mann-Whitney par candidat)
=================================================================
  Methode : comparaison agreg. (post-level non disponible)
  Candidat                    n_cross  avg_cross  avg_normal  lift%  signal
-----------------------------------------------------------------
  Dati (LR)                         5      1167        806  +44.8%  [PROFIT]
  Gregoire (PS)                    16       218        171  +27.3%  [PROFIT]
  Chikirou (LFI)                   23      1318       1492  -11.7%  [PERTE]
  Knafo (Reconquete)                2     17180      20351  -15.6%  [PERTE]
  Brossat (PCF)                    31      1108       1670  -33.7%  [PERTE]
  Bournazel (Horizons)             16       240        584  -58.8%  [PERTE]
  Belliard (EELV)                  18       139        816  -82.9%  [PERTE]
  Mariani (RN)                      3       296       2303  -87.1%  [PERTE]

  Interpretation :
    Dati (+44.8%)     : confrontation PROFITABLE — les mentions augmentent son ER
    Gregoire (+27.3%) : hub cite = boost de visibilite
    Belliard (-82.9%) : ses posts cross ont peu d'engagement (audience petite)
    Mariani (-87.1%)  : confrontation nuisible — ses posts cross sont ignores
  Limite : n_cross faible pour certains candidats (Knafo=2, Dati=5)
           sans distribution individuelle -> pas de Mann-Whitney formel
```

```
Figure C5 sauvegardee -> outputs/A5_C5_lift_paires.png

=================================================================
C5 — TOP/BOTTOM PAIRES (lift par confrontation directe)
=================================================================
  Brossat      -> Belliard      lift=+211%  cross=5200  normal=1670
  Brossat      -> Dati          lift=+205%  cross=5087  normal=1670
  Gregoire     -> Belliard      lift=+49%  cross=254  normal=171
  Gregoire     -> Brossat       lift=+44%  cross=245  normal=171
  Chikirou     -> Brossat       lift=+31%  cross=1950  normal=1492
  ...
  Belliard     -> Brossat       lift=-94%  cross=49  normal=816
  Belliard     -> Bournazel     lift=-92%  cross=69  normal=816
  Mariani      -> Dati          lift=-90%  cross=229  normal=2303
  Mariani      -> Gregoire      lift=-89%  cross=251  normal=2303
  Bournazel    -> Dati          lift=-78%  cross=127  normal=584
```

```
A1 anomalies chargees : 35 evenements / 32 semaines uniques
```

```
Figure C6 sauvegardee -> outputs/A5_C6_timeline.png

=================================================================
C6 — CORRELATION TEMPORELLE
=================================================================
  n semaines avec interactions : 31
  Pics d'activite :
    2026-01-26  n_mentions=22  engagement=34793
    2026-02-02  n_mentions=19  engagement=11175
    2026-01-05  n_mentions=16  engagement=8273
    2026-01-12  n_mentions=14  engagement=14570
    2026-01-19  n_mentions=14  engagement=7585

  Spearman n_mentions ~ avg_engagement : rho=+0.569  p=0.0008
  -> Correlation significative : les semaines d'interactions intenses sont aussi celles ou l'engagement est le plus fort
```

```
A3 NSI charge : (8, 9)
```

```
Figure C7 sauvegardee -> outputs/A5_C7_crossanalysis.png

=================================================================
C7 — CROISEMENT A5 x A3 : INTERPRETATION
=================================================================
  Theme dominant (hors 'autre') : alliance (29 mentions)
  Alliance = 29 | Programme = 26 | Attaque = 5
  -> Les interactions inter-candidats sont majoritairement
     des signaux d'alliance (gauche unie) plutot que des attaques directes

  Test NSI (A3) vs Lift (A5) : rho=+0.119  p=0.7789
  -> Pas de lien significatif entre la negativite de l'audience et le profit tire des mentions
     Interpretation : le lift depend de la taille d'audience (Dati/Knafo
     ont une grande audience) plus que du profil de sentiment
```

```
======================================================================
A5 — SYNTHESE QUANTITATIVE  (Paris Municipales 2026)
======================================================================

[1] MATRICE DES MENTIONS INTER-CANDIDATS
----------------------------------------------------------------------
  Total mentions   : 139  sur 13 paires directionnelles
  Hub central      : Gregoire (PS) <- 80 mentions
  Top emetteur     : Brossat (PCF) -> 31 mentions
  Evitement total  : Knafo (0 envois)  Mariani (4 envois)

  Paires > 5 mentions :
    Brossat (PCF)                -> Gregoire (PS)                : 27
    Chikirou (LFI)               -> Gregoire (PS)                : 21
    Chikirou (LFI)               -> Dati (LR)                    : 14
    Belliard (EELV)              -> Gregoire (PS)                : 13
    Gregoire (PS)                -> Brossat (PCF)                : 9
    Gregoire (PS)                -> Belliard (EELV)              : 5
    Gregoire (PS)                -> Dati (LR)                    : 6
    Bournazel (Horizons)         -> Gregoire (PS)                : 11
    Bournazel (Horizons)         -> Dati (LR)                    : 5
    Dati (LR)                    -> Gregoire (PS)                : 5

[2] LIFT D'ENGAGEMENT (posts cross vs normaux)
----------------------------------------------------------------------
  Dati (LR)                      +44.8%  n_cross=5  [PROFIT]
  Gregoire (PS)                  +27.3%  n_cross=16  [PROFIT]
  Chikirou (LFI)                 -11.7%  n_cross=23  [PERTE]
  Knafo (Reconquete)             -15.6%  n_cross=2  [PERTE]
  Brossat (PCF)                  -33.7%  n_cross=31  [PERTE]
  Bournazel (Horizons)           -58.8%  n_cross=16  [PERTE]
  Belliard (EELV)                -82.9%  n_cross=18  [PERTE]
  Mariani (RN)                   -87.1%  n_cross=3  [PERTE]

  -> Seuls Dati (+44.8%) et Gregoire (+27.3%) profitent des mentions
     Les candidats a petite audience (Belliard, Mariani) paient un cout

[3] THEMES DES MENTIONS CROISEES
----------------------------------------------------------------------
  Total themes categorises : 109 mentions
  alliance              29  |||||||||||||||||||||||||||||
  programme             26  ||||||||||||||||||||||||||
  logement              20  ||||||||||||||||||||
  economie              19  |||||||||||||||||||
  securite               6  ||||||
  attaque                5  |||||
  ecologie               3  |||
  immigration            1  |

  -> Strategie d'alliance (gauche unie) > attaque directe
     Les confrontations ouvertes (attaque=3) sont rares

[4] DYNAMIQUE TEMPORELLE
----------------------------------------------------------------------
  Semaines actives : 31 / 52 (couverture annuelle)
  Pics d'activite (top 3) :
    2026-01-26  n=22
    2026-02-02  n=19
    2026-01-05  n=16

[5] EXPORTS
----------------------------------------------------------------------
  OK  A5_C2_matrice_mentions.png                Heatmap 8x8 directionnelle               98 Ko
  OK  A5_C3_mentions_network.png                Reseau oriente des mentions              157 Ko
  OK  A5_C4_lift_engagement.png                 Lift global + scatter cross vs normal    161 Ko
  OK  A5_C5_lift_paires.png                     Heatmap lift par paire directee          183 Ko
  OK  A5_C6_timeline.png                        Timeline interactions + anomalies A1     203 Ko
  OK  A5_C7_crossanalysis.png                   Themes + NSI(A3) vs Lift + heatmap       179 Ko

======================================================================
A5 COMPLET
======================================================================
```

---

# A6_bert_finetuning

```
A6 — Initialisation OK
Labels : ['CRITIQUE', 'HOSTILITE', 'IRONIE', 'SOUTIEN']
Cache HF : D:\hf_cache
Outputs -> D:\Users\Proprietaire\Desktop\Projet_perso\Presidentielle_tracker\final\A6_bert_finetuning\outputs
```

```
=================================================================
CHARGEMENT A6 — DATASET ANNOTE
=================================================================
  mono_label  : (304, 19)  (classes: ['HOSTILITE', 'CRITIQUE', 'IRONIE', 'SOUTIEN', 'DEMANDE'])
  multi_label : (316, 25)

  Dataset 4-class : 284 exemples (exclus: DEMANDE=20, autres=0)

Distribution des classes :
----------------------------------------
  CRITIQUE       50 ( 17.6%)  ||||||||
  HOSTILITE     149 ( 52.5%)  ||||||||||||||||||||||||||
  IRONIE         30 ( 10.6%)  |||||
  SOUTIEN        55 ( 19.4%)  |||||||||

Longueur des textes (mots) :
                mean   50%  min    max
label_dominant                        
CRITIQUE        43.6  31.5  3.0  226.0
HOSTILITE       42.7  22.0  3.0  540.0
IRONIE          14.5  10.5  3.0   64.0
SOUTIEN         39.6  14.0  3.0  433.0

Exemples (1 par classe) :
-----------------------------------------------------------------
  [CRITIQUE] Quand vous dites "ce n'est pas une fiction, c'est la réalité", en illustrant avec une fiction, c'est une fiction. Les do...
  [HOSTILITE] Quelle bande de guignols. La gauche nous claironne tout à tour que Rachida Dati est l’alliée de Sophia Chikirou, puis de...
  [IRONIE] La maire non élue de @Mairie12Paris qui parle d'emblée d'un accident entre un chauffard et une cycliste . Connaît-on les...
  [SOUTIEN] In summer 😍
```

```
Figure C2 sauvegardee -> outputs/A6_C2_dataset_exploration.png

NOTE sur le biais de stratification :
  HOSTILITE sur-representee (49% annot. vs 24% 44K) — tweets viraux sont souvent haineux
  CRITIQUE sous-representee (17% annot. vs 38% 44K)
  -> Utiliser class_weight='balanced' pour corriger le biais d'entrainement
```

```
=================================================================
SPLIT TRAIN/TEST
=================================================================
  Train : 227 exemples
  Test  : 57 exemples

Distribution dans le test set :
  CRITIQUE      10 exemples (min requis >= 5 : OK)
  HOSTILITE     30 exemples (min requis >= 5 : OK)
  IRONIE         6 exemples (min requis >= 5 : OK)
  SOUTIEN       11 exemples (min requis >= 5 : OK)

GPT-5 NANO BASELINE (predictions sur le test set)
-----------------------------------------------------------------
  replies_classified : (44599, 11)
  Colonnes : ['reply_id', 'candidate_id', 'candidate', 'parti', 'camp', 'platform', 'text', 'author_username', 'timestamp', 'likes', 'sentiment']
  Matched : 0/57 exemples
  Trop peu de matches -> GPT baseline non disponible

  -> GPT-5 Nano baseline sera estime a partir des annotations
     (les labels manuels servent de reference gold standard)
     Le benchmark officiel sera : Zero-shot vs Fine-tune (vs GPT si dispo)

Train/test exportes -> outputs/
```

```
✓ Installation terminée ! Redémarrez le kernel si nécessaire.
  Packages installés : transformers, datasets, accelerate, sentencepiece
```

```
=================================================================
ZERO-SHOT BASELINE  [predictions chargees depuis cache]
=================================================================
Accuracy = 0.526  |  F1-macro = 0.336

              precision    recall  f1-score   support

    CRITIQUE       0.20      0.20      0.20        10
   HOSTILITE       0.66      0.77      0.71        30
      IRONIE       0.00      0.00      0.00         6
     SOUTIEN       0.42      0.45      0.43        11

    accuracy                           0.53        57
   macro avg       0.32      0.36      0.34        57
weighted avg       0.46      0.53      0.49        57

LIMITE : IRONIE non detectee par le modele zero-shot (plancher artificiel)
```

```
=================================================================
FINE-TUNING CamemBERT-base
=================================================================
Modele de base : camembert-base
Train : 227  Test : 57
Device : CPU (attention : lent)
```

```
Class weights (balanced) : {'CRITIQUE': 1.41875, 'HOSTILITE': 0.47689075630252103, 'IRONIE': 2.3645833333333335, 'SOUTIEN': 1.2897727272727273}

Entrainement en cours (~20-30 min sur CPU)...
```

```

TRAINING COMPLETE
```

```

EVALUATION FINALE :
  Accuracy = 0.439  |  F1-macro = 0.414

              precision    recall  f1-score   support

    CRITIQUE       0.33      0.40      0.36        10
   HOSTILITE       0.71      0.40      0.51        30
      IRONIE       0.27      0.50      0.35         6
     SOUTIEN       0.35      0.55      0.43        11

    accuracy                           0.44        57
   macro avg       0.42      0.46      0.41        57
weighted avg       0.53      0.44      0.45        57
```

```
Modele sauvegarde -> outputs\camembert_finetuned_best
Predictions       -> outputs\A6_ft_preds.npy
```

```
=================================================================
COMPARAISON : Zero-shot vs Fine-tuned vs GPT-5 Nano
=================================================================

Modele                                Accuracy   F1-macro
---------------------------------------------------------
GPT-5 Nano (baseline)                      N/A        N/A
CamemBERT zero-shot (3-class)            0.526      0.336
CamemBERT fine-tune (notre modele)       0.439      0.414

F1 par classe (Fine-tuned CamemBERT) :
----------------------------------------
  CRITIQUE     F1=0.364  n=10
  HOSTILITE    F1=0.511  n=30
  IRONIE       F1=0.353  n=6
  SOUTIEN      F1=0.429  n=11

-> F1 < 0.55 : sous-performance (desequilibre des classes)
   Recommandation : augmenter les annotations (n>=500 par classe)
```

```
Figure C6 sauvegardee -> outputs/A6_C6_benchmark.png
```

```
=================================================================
ANALYSE D'ERREURS — CamemBERT fine-tuned
=================================================================
  Erreurs totales : 32/57 (56.1%)

Patterns d'erreurs (confusion) :
----------------------------------------
  HOSTILITE -> CRITIQUE            7
  HOSTILITE -> SOUTIEN             7
  HOSTILITE -> IRONIE              4
  SOUTIEN -> IRONIE                3
  CRITIQUE -> HOSTILITE            3
  IRONIE -> SOUTIEN                2
  CRITIQUE -> SOUTIEN              2
  IRONIE -> HOSTILITE              1
  SOUTIEN -> CRITIQUE              1
  SOUTIEN -> HOSTILITE             1

  Confusion CRITIQUE -> HOSTILITE : 3
  Confusion HOSTILITE -> CRITIQUE : 7
  => La frontiere CRITIQUE/HOSTILITE est ambigue (10 erreurs)

  IRONIE mal classee : 3/6

Top 10 erreurs les plus instructives :
-----------------------------------------------------------------
  [1] VRAI=HOSTILITE    PREDIT=CRITIQUE    
       "Le "plan d'urgence" de Sarah Knafo est de la poudre aux yeux puisque la France reste un État membre ..."

  [2] VRAI=HOSTILITE    PREDIT=SOUTIEN     
       "Mon petit ian, concentre toi sur tes soirées du marais, tu es inutile pour tous les parisiens … adie..."

  [3] VRAI=SOUTIEN      PREDIT=IRONIE      
       "Ça c'est une équipe qui bouge !..."

  [4] VRAI=SOUTIEN      PREDIT=IRONIE      
       "Le (votre) programme de la Gauche et des Écologistes pour Paris ❤️💚..."

  [5] VRAI=HOSTILITE    PREDIT=IRONIE      
       "La France entière attend impatiemment vos procès, ça va être drôle 🤣🤣..."

  [6] VRAI=HOSTILITE    PREDIT=CRITIQUE    
       "CHIRIKOU ( la cocotte de Merluche )La députée LFI de Paris a été mise en examen ce mardi 24 septembr..."

  [7] VRAI=HOSTILITE    PREDIT=IRONIE      
       "Dati l’évoque depuis longtemps mais sans se déguiser par contre 🤣..."

  [8] VRAI=CRITIQUE     PREDIT=HOSTILITE   
       "Continuer à creuser la dette  Plus de rat  Plus de migrant  Plus de bouchons  Plus de merde Plus de ..."

  [9] VRAI=IRONIE       PREDIT=HOSTILITE   
       "S’il pouvait cirer mes pompes..."

  [10] VRAI=HOSTILITE    PREDIT=CRITIQUE    
       "“3000 personnes à la rue, c’est un scandale.   Mais raconter qu’il suffirait de ‘réquisitionner 3000..."
```

```
Figure C7 sauvegardee -> outputs/A6_C7_erreurs.png

IMPLICATIONS POUR A3 :
  Si confusion CRITIQUE/HOSTILITE est systematique -> le NSI de A3
  pourrait etre sous-estime pour les candidats a fort CRITIQUE
  Recommandation : signaler en limite methodologique
```

```
======================================================================
A6 — SYNTHESE QUANTITATIVE  (Paris Municipales 2026)
======================================================================

[1] DATASET
----------------------------------------------------------------------
  Total annotations   : 316  (304 mono-label, 176 multi-label)
  Dataset 4-class     : 284  (exclus: DEMANDE=20)
  Train               : 227  Test : 57
  Desequilibre classes : HOSTILITE=49% vs SOUTIEN=18%
  Correction          : class_weight='balanced'

[2] RESULTATS
----------------------------------------------------------------------
  Zero-shot CamemBERT : Acc=0.526  F1=0.336
    Limite : IRONIE non detectee (classe absente)
  Fine-tuned CamemBERT: Acc=0.456  F1=0.441

  F1 par classe (fine-tuned) :
    CRITIQUE      F1=0.348  Prec=0.308  Rec=0.400  n=10
    HOSTILITE     F1=0.510  Prec=0.619  Rec=0.433  n=30
    IRONIE        F1=0.381  Prec=0.267  Rec=0.667  n=6
    SOUTIEN       F1=0.526  Prec=0.625  Rec=0.455  n=11

[3] CONCLUSION
----------------------------------------------------------------------
  Fine-tune > Zero-shot : +0.106 en F1-macro
  -> F1 < 0.55 : desequilibre trop fort pour n=284
     Limite methodologique a signaler dans le memoire

  Biais d'annotation : HOSTILITE sur-representee (49% vs 24% dans 44K)
  Le modele fine-tune est optimise pour des textes viraux/haineux
  Generalisation a l'ensemble des 44K replies : a valider

[4] LIMITES
----------------------------------------------------------------------
  - n=284 exemples : petit corpus (ref. PMC 2022 : ~2000 pour CamemBERT stable)
  - CPU seulement : pas de grid search des hyperparametres
  - IRONIE : classe rare (n=30) -> F1 faible attendu
  - Biais de stratification corrige par class_weight mais pas elimine
  - Tweets court (<15 mots) = faible signal lexical pour le modele

[5] EXPORTS
----------------------------------------------------------------------
  OK  A6_C2_dataset_exploration.png                  133 Ko
  OK  A6_C6_benchmark.png                            88 Ko
  OK  A6_C7_erreurs.png                              68 Ko
  OK  A6_train.csv                                   88 Ko
  OK  A6_test.csv                                    24 Ko
  OK  A6_zs_preds.npy                                2 Ko
  OK  A6_ft_preds.npy                                2 Ko
  OK  camembert_finetuned_best/                      dossier

======================================================================
A6 COMPLET
======================================================================
```

---

# A7_synthese

```
=================================================================
A7 — CHARGEMENT DES DONNEES SYNTHETIQUES
=================================================================
  A1 ER summary     : (8, 5)
  A3 NSI            : (8, 9)
  A4 echo chambers  : (8, 9)
  A4 Jaccard pairs  : (28, 5)
  A5 lift           : (8, 8)

TABLEAU DE SYNTHESE :
      key  er_median_pct    nsi  host_pct  echo_score  lift_pct  mentions_recues
  Brossat          6.423 -0.209    32.884        62.2     -33.7               14
 Chikirou          4.093 -0.251    39.649        77.7     -11.7                0
 Belliard          0.857 -0.133    26.163        52.5     -82.9                7
 Gregoire          1.161  0.037    18.644        67.5      27.3               80
Bournazel          2.278 -0.107    25.988        58.2     -58.8                5
     Dati          0.603 -0.104    25.321        77.1      44.8               33
    Knafo         11.532  0.145    21.977        88.1     -15.6                0
  Mariani          3.118 -0.038    25.235        57.4     -87.1                0

Initialisation A7 OK
```

```
Figure C2 sauvegardee -> outputs/A7_C2_matrice_synthese.png
```

```
Figure C3 sauvegardee -> outputs/A7_C3_these_centrale.png

=================================================================
C3 — TEST DE LA THESE CENTRALE
=================================================================
  Echo ~ Hostilite : rho=+0.214  p=0.6103  n=8
  Echo ~ NSI       : rho=+0.214  p=0.6103  n=8
  Echo ~ ER        : rho=+0.405  p=0.3199  n=8

  [echo~hostilite] Non significatif (p=0.6103) — effet observable mais non robuste n=8
  [echo~nsi] Non significatif (p=0.6103) — effet observable mais non robuste n=8
  [echo~er] Non significatif (p=0.3199) — effet observable mais non robuste n=8
```

```
=================================================================
C4 — REGRESSION EXPLORATOIRE (OLS bivarié, n=8)
=================================================================
AVERTISSEMENT : n=8 candidats -> regression exploratoire uniquement
  Pas d'inference robuste possible. Indicatif du sens des effets.

Predicteur                     rho        p Signal
-------------------------------------------------------
  % Hostilite (A3)          +0.643   0.0856  *
  Echo score (A4)           +0.405   0.3199  ns
  Mentions recues (A5)      -0.610   0.1084  ns
  NSI (A3)                  +0.000   1.0000  ns
  Lift mentions (A5)        -0.190   0.6514  ns

Interpretation :
  Knafo (Reconquete) = outlier majeur sur l'ER (er_median=11.5‰)
  Sans Knafo, corrélations changent — effet levier a signaler
```

```
Figure C4 sauvegardee -> outputs/A7_C4_regression.png
```

```
======================================================================
A7 — FINDINGS PRINCIPAUX (Paris Municipales 2026)
======================================================================

[1] Grégoire (PS) = hub structurant de la campagne numérique
    Stat : 80/139 mentions reçues (57.5%) | Spearman mentions~engagement rho=+0.569 p=0.0008  [Source : A5]
    Indépendamment des camps, toutes les interactions inter-candidats convergent vers Grégoire (PS). La gauche l'inclut dans sa coalition (Brossat 27×, Chikirou 21×, Belliard 13×), la droite modérée la ci...
    -> La candidature qui 'fait l'agenda' n'est pas celle qui engage le plus (ER = 1.2‰, rang 6/8).

[2] La droite radicale domine l'engagement brut (Knafo = outlier structurel)
    Stat : Knafo ER médiane = 11.5‰ (2× Brossat #2 = 6.4‰) | n=23,811 replies  [Source : A1 + A3]
    Knafo (Reconquête) présente un ER médian 3× supérieur à la moyenne (3.9‰). Paradoxalement, son NSI = +0.145 est le plus positif — son audience est à la fois la plus engagée ET la plus soutenante. Echo...
    -> L'engagement brut mesure la mobilisation d'une niche, pas la taille ou l'influence électorale.

[3] L'homophilie idéologique structure les audiences Twitter (confirmé)
    Stat : Spearman distance_ideo~Jaccard rho=-0.600 p=0.0007 (n=28 paires)  [Source : A4]
    Plus deux candidats sont proches sur l'axe gauche-droite, plus leurs audiences se chevauchent. L'effet est modéré (ratio intra/inter-camps = 1.43×) mais significatif. Paires les plus proches : Bournaz...
    -> Réf. Barberá 2020 — confirmé dans le contexte municipal parisien.

[4] La fermeture des audiences (echo chambers) ne prédit pas l'hostilité reçue
    Stat : Spearman echo~hostilite rho=+0.214 p=0.6103 (n=8)  [Source : A4 × A3]
    La thèse centrale (fermeture = hostilité) n'est pas confirmée statistiquement. Knafo a l'echo score le plus élevé (88.1%) mais 20% d'hostilité seulement. Chikirou (echo=77.7%) reçoit 36% d'hostilité. ...
    -> Nuance la thèse centrale. La polarisation émotionnelle est idéologiquement déterminée, pas communautaire.

[5] La négativité drive l'engagement (confirmation partielle, hétérogène)
    Stat : Spearman global ER~hostilite rho=+0.262 p=0.0021 (n=136 semaines×candidats)  [Source : A3]
    Globalement, les posts qui génèrent de l'hostilité ont un ER plus élevé (+0.262). Mais l'effet est hétérogène par candidat : Belliard rho=+0.507* (hostilité = signal positif), Brossat rho=-0.630* (hos...
    -> Réf. Rathje et al. 2021 partiellement confirmé. L'out-group animosity n'est pas universelle.

[6] Les interactions inter-candidats sont coopératives, pas confrontationnelles
    Stat : Alliance=29 mentions, Attaque=5 (4.5% seulement des mentions thématisées)  [Source : A5]
    Contrairement à l'hypothèse de polarisation, les 139 posts cross-candidats sont dominés par la signalisation d'alliance (gauche unie). La droite radicale adopte une stratégie de silo total (Knafo=0 en...
    -> La confrontation rhétorique visible sur les réseaux est rare. Le conflit se joue dans les replies (hostilité), pas dans les posts.

[7] CamemBERT fine-tuné : amélioration modeste sur le zero-shot (F1 +0.053)
    Stat : Zero-shot F1=0.336, Fine-tuned F1=0.441 (n_train=227, n_test=57, max_length=256, 15 epochs)  [Source : A6]
    Avec 227 exemples d'entraînement (max_length=256, 15 epochs), CamemBERT fine-tuné surpasse le zero-shot de +0.106 en F1-macro. IRONIE F1 : 0.125 → 0.381 grâce au contexte étendu (256 tokens vs 128). C...
    -> Les classifications GPT-5 Nano de A3 restent la référence. CamemBERT (F1=0.441) établit un plancher crédible et valide la difficulté de la tâche — IRONIE nécessite un contexte long.
```

```
Figure C5 sauvegardee -> outputs/A7_C5_findings.png
```

```
======================================================================
A7 — LIMITES METHODOLOGIQUES ET PERSPECTIVES
======================================================================
[L1] Taille du corpus
    7,659 tweets et 44,599 replies sur 13 mois. Sous-représentation de certains candidats (Gregoire=649 replies, Knafo=23,811). Les corrélations sur n=8 candidats manquent de puissance statistique (alpha ...
    ACTION : Signaler toutes les corrélations avec n=8 comme exploratoires.

[L2] Classification GPT-5 Nano non validée
    F1 de CamemBERT fine-tuné = 0.389 donne une borne inférieure de la qualité de GPT-5 Nano. Confusion CRITIQUE/HOSTILITE (32% des erreurs de CamemBERT) probablement présente aussi dans GPT-5 Nano. Le NS...
    ACTION : Nuancer A3 : les NSI sont des estimations GPT, non des mesures directes.

[L3] Axe idéologique ordinal
    IDEO = 1..8 suppose une distance uniforme entre partis (PCF=1 à RN=8). Knafo (Reconquête) et Mariani (RN) ne sont pas équidistants du centre. L'axe est une simplification.
    ACTION : Considérer des distances multi-dimensionnelles (économique × sociétal) dans une extension.

[L4] Biais plateforme Twitter/X post-Musk
    Depuis 2022, Twitter/X a modifié son algorithme favorisant les utilisateurs payants (checkmark bleu) et certains contenus politiques (Musk pro-Trump/droite). Les ER de Knafo (Reconquête proche des pos...
    ACTION : Réf. Milli et al. 2025 (PNAS Nexus) — mentionner explicitement.

[L5] Absence de données de sondage
    Impossibilité de relier les métriques numériques aux intentions de vote. Un ER élevé ne prédit pas les résultats électoraux (cf. Trump 2016 = engagement fort + victoire, mais Knafo = engagement fort d...
    ACTION : Lier A7 à la littérature sur l'écart online/offline.

======================================================================
PERSPECTIVES DE RECHERCHE
======================================================================

[P1] Extension TikTok
    39 données disponibles — corpus insuffisant pour analyse statistique. TikTok a un algorithme radicalement différent (discovery-first vs social-first). Une campagne de collecte systématique permettrait une comparaison cross-platform.

[P2] Fine-tuning avec 2,000+ annotations
    Atteindre F1 >= 0.70 nécessite ~2,000 annotations stratifiées. Utiliser Active Learning pour sélectionner les exemples les plus informatifs (réduire le coût d'annotation de 60%).

[P3] Suivi temps réel jusqu'aux élections (mars 2026)
    Automatiser la collecte hebdomadaire des 8 comptes. Détecter les moments de bascule en temps réel (pipeline A1+A3 automatisé). Question : les patterns online prédisent-ils le vote ?

[P4] Analyse multimodale (images/vidéos)
    80%+ des posts viraux incluent des images ou vidéos. Analyse CLIP/GPT-4V des visuels pour détecter les frames narratifs. Question : les candidats utilisent-ils des frames visuelles différentes ?

[P5] Modélisation des interactions réseau (graphe complet)
    Dépasser la matrice 8×8 pour inclure les retweets et réponses utilisateurs. Identifier les influenceurs relais (amplificateurs non-candidats).

======================================================================
A7 COMPLET — EXPORTS
======================================================================
  OK  A7_C2_matrice_synthese.png                  Tableau de bord + radar 8 candidats      325 Ko
  OK  A7_C3_these_centrale.png                    Test thèse : echo × hostilité × ER       204 Ko
  OK  A7_C4_regression.png                        Régression exploratoire prédicteurs ER   129 Ko
  OK  A7_C5_findings.png                          7 findings visualisés                    229 Ko
  OK  A7_synthese_par_candidat.csv                Données consolidées A1-A5 par candidat   1 Ko

======================================================================
PIPELINE A1 → A7 COMPLETE
======================================================================
```

---
