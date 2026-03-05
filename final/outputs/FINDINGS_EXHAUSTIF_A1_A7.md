# FINDINGS EXHAUSTIFS — Paris Municipales 2026
*Pipeline A1 → A7 · Généré le 2026-02-24 22:52*

---

# A1 — Dynamiques temporelles

*Comment évolue la présence numérique de chaque candidat sur 13 mois ?*


### Résumé ER par candidat (médiane, moyenne, std)

| key       |   er_median_pct |   er_mean_pct |   er_std_pct |   n_semaines |
|:----------|----------------:|--------------:|-------------:|-------------:|
| Knafo     |         11.5324 |       32.6573 |      54.3881 |           57 |
| Brossat   |          6.4231 |        7.3141 |       3.9908 |           55 |
| Chikirou  |          4.0932 |        5.5752 |       4.557  |           51 |
| Mariani   |          3.118  |        4.8901 |       5.8853 |           54 |
| Bournazel |          2.2778 |        2.7668 |       1.4231 |           57 |
| Gregoire  |          1.1613 |        1.4519 |       0.8961 |           57 |
| Belliard  |          0.8571 |        1.5031 |       1.1661 |           43 |
| Dati      |          0.6034 |        0.8968 |       0.8202 |           53 |

**Rang ER médiane :** Knafo (11.5‰) >> Brossat (6.4‰) > Chikirou (4.1‰) > Mariani (3.1‰) > Bournazel (2.3‰) > Grégoire (1.2‰) > Belliard (0.9‰) > Dati (0.6‰)


### Top 10 anomalies d'engagement (pics viraux/significatifs)

| week_start   | key       | candidate_label           | year_week   |   er_median |   z_global |   z_score |   top_post_engagement | top_post_text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:-------------|:----------|:--------------------------|:------------|------------:|-----------:|----------:|----------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2025-07-21   | Chikirou  | S. Chikirou (LFI)         | 2025-W30    |    0.031246 |       5.63 |      5.63 |                 38560 | URGENT Toutes les communications internet avec le Handala ont été coupées. Nous avons perdu le contact avec Emma et l’équipage. Partagez et interpellez les autorités pour assurer la sécurité de l'équi | The Israeli military had a message to the Handala freedom flotilla. @huwaidaarraf had a message back to them, explaining international law and their rightful and just mission to deliver humanitarian a | Nous avons fait plus de la moitié du trajet vers Gaza où nous arriverons dimanche 🇵🇸 Gardez les yeux rivés sur le #Handala pour protégez la Flottille de la Liberté ! |
| 2025-08-14   | Mariani   | T. Mariani (RN)           | 2025-W33    |    0.033396 |       4.84 |      4.84 |                 36441 | Charlotte Caubel vient d'être nommée par l'Elysée Procureur adjointe à Paris. Elle dirigera une des cinq divisions du Parquet le plus puissant de France. Elle avait été classée 16e sur 17 lorsque prop | Dis par un spécialiste qui n’a tenu aucun des engagements qu’il avait pris devant les Français pour se faire élire, c’est plutôt savoureux, n’est-ce-pas? 😂 | L’Union Européenne de Von Der Leyen est en train de déraper et représente désormais un vrai danger pour nos libertés. À vouloir tout réglementer sous prétexte de lutter contre la désinformation ou "la          |
| 2025-03-16   | Dati      | R. Dati (LR)              | 2025-W11    |    0.00448  |       4.37 |      4.37 |                  2231 | Émilie Dequenne nous a quittés après s’être battue contre la maladie. Revélée dans Rosetta des frères Dardenne, ce rôle émouvant lui vaut d’être récompensée à Cannes à 17 ans. Nommée 5 fois aux César,                                                                                                                                                                                                                                                                                                                                                                                    |
| 2025-10-21   | Gregoire  | E. Grégoire (PS)          | 2025-W43    |    0.004798 |       3.73 |      3.73 |                  1404 | Mon Paris, c’est un Paris pour toutes et tous. Rachida Dati, c’est la ville pour quelques-uns, uniquement les plus privilégiés. La gauche à Paris, c’est un investissement massif dans le logement socia | Faut-il attendre que la Joconde soit volée pour enfin avoir une véritable Ministre de la culture ? Rachida Dati doit démissionner. | La France ne peut plus laisser une poignée d’acteurs concentrer le pouvoir d’information. J'ai déposé une proposition de loi pour réarmer l’État républicain avec deux objectifs : créer un cadre clair                                     |
| 2025-03-29   | Knafo     | S. Knafo (Reconquête)     | 2025-W13    |    0.234907 |       3.72 |      3.72 |                173831 | Merci à la @CocardeEtud de m’accueillir aujourd’hui pour fêter ses dix ans !                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 2025-08-07   | Bournazel | P-Y. Bournazel (Horizons) | 2025-W32    |    0.007694 |       3.46 |      3.46 |                   277 | ✅ Le Conseil constitutionnel valide la réforme du mode de scrutin à #Paris. Je me suis battu pour cette réforme depuis des années lemonde.fr/idees/article/202… C’est un progrès démocratique majeur : c                                                                                                                                                                                                                                                                                                                                                                                   |
| 2025-02-26   | Brossat   | I. Brossat (PCF)          | 2025-W09    |    0.01975  |       3.12 |      3.12 |                 11064 | Pour rappel, quand cet énergumène a été rappelé à l’ordre par l’ARCOM, c’était pour avoir expliqué que le ghetto de Varsovie a été créé pour « protéger du typhus » | La France de 2025 n’est pas l’Afrique du Sud au temps de l’apartheid. J’ai saisi le parquet de Paris après les révélations de @libe sur l’organisation de soirées « réservées aux Européens » par l’ultr | Quel symbole. Abou Sangaré gagne le César de la meilleure révélation masculine ce soir. Il était sous OQTF il y a quelques semaines. La France qu’on aime !                                                |
| 2025-07-28   | Brossat   | I. Brossat (PCF)          | 2025-W31    |    0.019019 |       2.93 |      2.93 |                 53029 | An Israeli settler just shot Odeh Hadalin in the lungs, a remarkable activist who helped us film No Other Land in Masafer Yatta. Residents identified Yinon Levi, sanctioned by the EU and US, as the sh | Paris is removing cars in their downtown and around schools and the results are amazing. | La fraude sociale : 13 milliards d’euros. La fraude fiscale : 60 à 80 milliards d’euros. Les aides publiques aux entreprises sans contrepartie : 211 milliards d’euros. Devinez à quoi le gouvernement d                                                                              |
| 2025-04-14   | Mariani   | T. Mariani (RN)           | 2025-W16    |    0.022079 |       2.92 |      2.92 |                  3930 | Heureusement… ⁦@jnbarrot⁩, notre Ministre des Affaires Étrangères était il y’a quelques jours à Alger et avait déclaré qu’il était optimiste sur le rétablissement de relations normales avec l’Algérie                                                                                                                                                                                                                                                                                                                                                                                       |
| 2025-12-29   | Dati      | R. Dati (LR)              | 2026-W01    |    0.003257 |       2.88 |      2.88 |                  6311 | Nouveau viol dans l'aide sociale à l'enfance parisienne sans réaction de la Ville de Paris!                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|              |           |                           |             |             |            |           |                       | La majorité Hidalgo-Grégoire ne nous a toujours pas transmis le rapport d'inspection sur l'ASE dont nous avo | Chères Parisiennes, chers Parisiens, Je vous souhaite à toutes et à tous une très belle année 2026. À cette occasion, je prends un engagement: celui de changer votre vie. En mieux. Je vais changer Par | Pour une personne isolée, l'infirmière est le seul contact humain qu'ils auront dans la journée. Et le temps perdu dans les embouteillages, c'est du temps de relation perdu. Je simplifierai la v                                                                |

### Corrélation cross-platform Twitter ↔ Instagram

| candidate_id          | candidate_label           | platform_1   | platform_2   |   spearman_rho |   p_value |   n_weeks | synchrony   |
|:----------------------|:--------------------------|:-------------|:-------------|---------------:|----------:|----------:|:------------|
| david_belliard        | D. Belliard (EELV)        | twitter      | instagram    |          0.516 |    0.0004 |        43 | modéré      |
| emmanuel_gregoire     | E. Grégoire (PS)          | twitter      | instagram    |          0.699 |    0      |        55 | synchronisé |
| ian_brossat           | I. Brossat (PCF)          | twitter      | instagram    |          0.205 |    0.133  |        55 | indépendant |
| pierre_yves_bournazel | P-Y. Bournazel (Horizons) | twitter      | instagram    |          0.821 |    0      |        53 | synchronisé |
| rachida_dati          | R. Dati (LR)              | twitter      | instagram    |          0.235 |    0.1286 |        43 | indépendant |
| sarah_knafo           | S. Knafo (Reconquête)     | twitter      | instagram    |          0.493 |    0.0001 |        56 | modéré      |
| sophia_chikirou       | S. Chikirou (LFI)         | twitter      | instagram    |         -0.004 |    0.9761 |        49 | indépendant |
| thierry_mariani       | T. Mariani (RN)           | twitter      | instagram    |          0.21  |    0.3041 |        26 | indépendant |
**Synchronie :** Grégoire, Bournazel (rho>0.7) = synchronisés ; Belliard, Knafo (rho~0.5) = modérés ; Brossat, Chikirou, Dati, Mariani = indépendants


### Momentum (8 dernières semaines) par plateforme

| candidate_id          | candidate_label           | platform   |   momentum_slope |   r_squared |   p_value | direction   |   last_8w_mean_er |   n_weeks_used |
|:----------------------|:--------------------------|:-----------|-----------------:|------------:|----------:|:------------|------------------:|---------------:|
| david_belliard        | D. Belliard (EELV)        | twitter    |      -0.0002719  |      0.5489 |    0.0355 | baisse      |          0.002567 |              8 |
| emmanuel_gregoire     | E. Grégoire (PS)          | twitter    |       7.94e-05   |      0.083  |    0.489  | hausse      |          0.001775 |              8 |
| ian_brossat           | I. Brossat (PCF)          | twitter    |      -0.00052461 |      0.5543 |    0.0341 | baisse      |          0.004837 |              8 |
| pierre_yves_bournazel | P-Y. Bournazel (Horizons) | twitter    |      -0.00024702 |      0.4708 |    0.0602 | baisse      |          0.003677 |              8 |
| rachida_dati          | R. Dati (LR)              | twitter    |      -0.00024739 |      0.5304 |    0.0405 | baisse      |          0.001262 |              8 |
| sarah_knafo           | S. Knafo (Reconquête)     | twitter    |      -0.00108476 |      0.469  |    0.0609 | baisse      |          0.007422 |              8 |
| sophia_chikirou       | S. Chikirou (LFI)         | twitter    |      -0.00086592 |      0.4694 |    0.0608 | baisse      |          0.0044   |              8 |
| thierry_mariani       | T. Mariani (RN)           | twitter    |      -0.00060892 |      0.4045 |    0.0901 | baisse      |          0.002384 |              8 |
| david_belliard        | D. Belliard (EELV)        | instagram  |      -0.00076208 |      0.3473 |    0.1242 | baisse      |          0.016505 |              8 |
| emmanuel_gregoire     | E. Grégoire (PS)          | instagram  |       1.394e-05  |      0.0001 |    0.9829 | hausse      |          0.022671 |              8 |
| ian_brossat           | I. Brossat (PCF)          | instagram  |      -0.00058058 |      0.0148 |    0.7738 | baisse      |          0.023746 |              8 |
| pierre_yves_bournazel | P-Y. Bournazel (Horizons) | instagram  |     -10.4583     |      0.2045 |    0.2606 | baisse      |        215.062    |              8 |
| rachida_dati          | R. Dati (LR)              | instagram  |      -0.00227892 |      0.1625 |    0.322  | baisse      |          0.014551 |              8 |
| sarah_knafo           | S. Knafo (Reconquête)     | instagram  |      -0.00235024 |      0.6456 |    0.0163 | baisse      |          0.011611 |              8 |
| sophia_chikirou       | S. Chikirou (LFI)         | instagram  |       2.062e-05  |      0      |    0.9877 | hausse      |          0.016083 |              8 |
| thierry_mariani       | T. Mariani (RN)           | instagram  |      -0.00040788 |      0.0364 |    0.6507 | baisse      |          0.010608 |              8 |
| emmanuel_gregoire     | E. Grégoire (PS)          | tiktok     |      -8.144e-05  |      0.0017 |    0.9238 | baisse      |          0.041236 |              8 |
| sarah_knafo           | S. Knafo (Reconquête)     | tiktok     |       0.00337914 |      0.1899 |    0.2804 | hausse      |          0.074166 |              8 |
| sophia_chikirou       | S. Chikirou (LFI)         | tiktok     |       0.003575   |      0.1405 |    0.3602 | hausse      |          0.073254 |              8 |
**Tendance globale :** baisse d'ER sur Twitter pour la plupart des candidats ; Instagram et TikTok partiellement couverts.


### Anomalies détectées (global)

Pics viraux (z>3): 15 | Pics significatifs (z>2): 53 | Creux: 2


# A2 — Topics et résonance

*Quels thèmes structurent le discours et l'engagement ?*


### Classement des topics par engagement médian

| topic_name                        | topic_short       |   med_eng_global |   n_tweets_total |
|:----------------------------------|:------------------|-----------------:|-----------------:|
| Logement & urbanisme              | Logement          |           248    |              916 |
| Arrondissement / Liberté / Gauche | nan               |           271.75 |              696 |
| Vie locale & citoyennete          | Local/Paris       |           284.25 |              620 |
| Social & solidarite               | Social            |           422    |              680 |
| Geopolitique & international      | Géopolitique      |           429.25 |              968 |
| Education & culture               | Anti-droite/Dati* |           455    |             1270 |
| Securite & delinquance            | Sécurité          |           468.75 |              648 |
| Budget & finances                 | Budget            |           556    |              792 |
| Soutien / Jour / France           | Soutien/France    |           595.5  |              593 |
| Deux / Emmanuel / Peuple          | Générique†        |           705.5  |              366 |

### Matrice candidat × topic (% par candidat)

| Unnamed: 0           |   Arrondissement / Liberté / Gauche |   Budget |   Générique† |   Anti-droite/Dati* |   Géopolitique |   Logement |   Sécurité |   Social |   Soutien/France |   Local/Paris |
|:---------------------|------------------------------------:|---------:|-------------:|--------------------:|---------------:|-----------:|-----------:|---------:|-----------------:|--------------:|
| Brossat (PCF)        |                                7.95 |    13.3  |         6    |               19.88 |          10.09 |       8.24 |       9.08 |     7.98 |             9.53 |          7.96 |
| Chikirou (LFI)       |                                8.44 |    11.17 |         6.42 |               10.49 |          14.28 |      10.41 |       9.23 |     8.95 |            10.31 |         10.3  |
| Belliard (EELV)      |                               10.83 |     6.54 |         5.47 |               16.89 |           9.57 |      10.6  |       8.95 |    11.56 |             8.53 |         11.06 |
| Grégoire (PS)        |                               11.3  |     7.86 |         8.11 |               12.33 |           9.32 |      12.31 |       8.29 |     9.23 |            11.23 |         10.02 |
| Bournazel (Horizons) |                               13.18 |     6.44 |         6.32 |                9.61 |           8.41 |      13.08 |      10.53 |    12.25 |             7.57 |         12.61 |
| Dati (LR)            |                                9.95 |     6.61 |         6.27 |               11.14 |           9.96 |      15.65 |      10.7  |    12.21 |             9.05 |          8.46 |
| Knafo (Reconquête)   |                                9.04 |    11.97 |         7.68 |               14.88 |          13.4  |      10.24 |       9.33 |     8.77 |             7.19 |          7.52 |
| Mariani (RN)         |                                8.18 |    11.44 |         7.06 |               15.08 |          17.18 |       7.99 |      10.19 |     8.17 |             7.51 |          7.2  |

### Convergence anomalies × topics

Quand le pic d'engagement coïncide avec le topic dominant de la semaine (convergence=True) : amplification.

| semaine     | candidat   |   z_global |   top_engagement | topic_eng_max                     |   avg_eng_semaine | topic_vol_max     |   n_tweets_semaine | convergence   |
|:------------|:-----------|-----------:|-----------------:|:----------------------------------|------------------:|:------------------|-------------------:|:--------------|
| 21 Jul 2025 | Chikirou   |       5.63 |            38560 | Sécurité                          |              8809 | Géopolitique      |                 19 | False         |
| 14 Aug 2025 | Mariani    |       4.84 |            36441 | Sécurité                          |              6443 | Géopolitique      |                 12 | False         |
| 16 Mar 2025 | Dati       |       4.37 |             2231 | Géopolitique                      |               809 | Soutien/France    |                  9 | False         |
| 21 Oct 2025 | Gregoire   |       3.73 |             1404 | Budget                            |              6961 | Anti-droite/Dati* |                 30 | False         |
| 29 Mar 2025 | Knafo      |       3.72 |           173831 | Budget                            |            200391 | Logement          |                 27 | False         |
| 07 Aug 2025 | Bournazel  |       3.46 |              277 | Arrondissement / Liberté / Gauche |             11766 | Budget            |                 12 | False         |
| 26 Feb 2025 | Brossat    |       3.12 |            11064 | Budget                            |              9168 | Géopolitique      |                 17 | False         |
| 28 Jul 2025 | Brossat    |       2.93 |            53029 | Budget                            |              6809 | Géopolitique      |                 16 | False         |
| 14 Apr 2025 | Mariani    |       2.92 |             3930 | Géopolitique                      |            137684 | Social            |                  8 | False         |
| 29 Dec 2025 | Dati       |       2.88 |             6311 | Géopolitique                      |             10015 | Géopolitique      |                 22 | True          |
| 09 Apr 2025 | Knafo      |       2.71 |           266429 | Géopolitique                      |            137684 | Budget            |                 13 | False         |
| 14 Apr 2025 | Knafo      |       2.48 |           796132 | Géopolitique                      |            137684 | Social            |                  8 | False         |
| 05 May 2025 | Knafo      |       2.44 |          1355519 | Budget                            |            103368 | Géopolitique      |                 22 | False         |
| 30 Apr 2025 | Knafo      |       2.4  |          1020699 | Budget                            |            103368 | Géopolitique      |                 22 | False         |
| 03 Nov 2025 | Bournazel  |       2.39 |             4207 | Soutien/France                    |              4325 | Local/Paris       |                 24 | False         |

# A3 — Sentiment et Net Support Index

*Quel ton reçoivent les candidats dans les replies ?*


### NSI et % hostilité par candidat

| key       | label                |        nsi |      ci_lo |      ci_hi |     n |   n_host |   n_sout |   host_pct |
|:----------|:---------------------|-----------:|-----------:|-----------:|------:|---------:|---------:|-----------:|
| Chikirou  | Chikirou (LFI)       | -0.250941  | -0.298651  | -0.202008  |   797 |      316 |      116 |    39.6487 |
| Brossat   | Brossat (PCF)        | -0.208675  | -0.238584  | -0.178781  |  1706 |      561 |      205 |    32.8839 |
| Belliard  | Belliard (EELV)      | -0.132664  | -0.160161  | -0.107796  |  1892 |      495 |      244 |    26.1628 |
| Bournazel | Bournazel (Horizons) | -0.107046  | -0.125235  | -0.0890602 |  4783 |     1243 |      731 |    25.9879 |
| Dati      | Dati (LR)            | -0.103664  | -0.117483  | -0.0894895 |  8325 |     2108 |     1245 |    25.3213 |
| Mariani   | Mariani (RN)         | -0.0380639 | -0.0648496 | -0.0103383 |  2128 |      537 |      456 |    25.235  |
| Gregoire  | Grégoire (PS)        |  0.03698   | -0.0138675 |  0.0878274 |   649 |      121 |      145 |    18.6441 |
| Knafo     | Knafo (Reconquête)   |  0.145479  |  0.136702  |  0.154971  | 23811 |     5233 |     8697 |    21.9772 |
**NSI = (SOUTIEN - HOSTILITE) / total. Positif = plus de soutien que d'hostilité.**

**Knafo** : seul NSI positif (+0.15) malgré audience extrême droite. **Chikirou** : NSI le plus négatif (-0.25), hostilité 40%.


### Distribution sentiment hebdomadaire (extrait)

| candidate_id   | candidate   | parti   | camp   | year_week   | week_start   |   n_replies |   n_soutien |   n_critique |   n_hostilite |   n_ironie |   n_inconnu |   pct_soutien |   pct_critique |   pct_hostilite |   pct_ironie |   net_support |   polarization |
|:---------------|:------------|:--------|:-------|:------------|:-------------|------------:|------------:|-------------:|--------------:|-----------:|------------:|--------------:|---------------:|----------------:|-------------:|--------------:|---------------:|
| david_belliard | Belliard    | EELV    | Gauche | 2025-W06    | 2025-02-03   |          14 |           4 |            4 |             4 |          2 |           0 |         28.57 |          28.57 |           28.57 |        14.29 |        -14.29 |          42.86 |
| david_belliard | Belliard    | EELV    | Gauche | 2025-W16    | 2025-04-14   |           8 |           4 |            4 |             0 |          0 |           0 |         50    |          50    |            0    |         0    |         50    |           0    |
| david_belliard | Belliard    | EELV    | Gauche | 2025-W20    | 2025-05-12   |          21 |          13 |            4 |             3 |          0 |           1 |         61.9  |          19.05 |           14.29 |         0    |         47.62 |          14.29 |
| david_belliard | Belliard    | EELV    | Gauche | 2025-W24    | 2025-06-09   |          24 |           7 |           11 |             4 |          2 |           0 |         29.17 |          45.83 |           16.67 |         8.33 |          4.17 |          25    |
| david_belliard | Belliard    | EELV    | Gauche | 2025-W29    | 2025-07-14   |          29 |          11 |            9 |             5 |          3 |           1 |         37.93 |          31.03 |           17.24 |        10.34 |         10.34 |          27.59 |
| david_belliard | Belliard    | EELV    | Gauche | 2025-W33    | 2025-08-11   |          16 |           7 |            7 |             0 |          2 |           0 |         43.75 |          43.75 |            0    |        12.5  |         31.25 |          12.5  |
| david_belliard | Belliard    | EELV    | Gauche | 2025-W37    | 2025-09-08   |          15 |           7 |            6 |             2 |          0 |           0 |         46.67 |          40    |           13.33 |         0    |         33.33 |          13.33 |
| david_belliard | Belliard    | EELV    | Gauche | 2025-W38    | 2025-09-15   |           8 |           5 |            3 |             0 |          0 |           0 |         62.5  |          37.5  |            0    |         0    |         62.5  |           0    |
| david_belliard | Belliard    | EELV    | Gauche | 2025-W41    | 2025-10-06   |           5 |           0 |            4 |             0 |          1 |           0 |          0    |          80    |            0    |        20    |        -20    |          20    |
| david_belliard | Belliard    | EELV    | Gauche | 2025-W43    | 2025-10-20   |           4 |           1 |            2 |             1 |          0 |           0 |         25    |          50    |           25    |         0    |          0    |          25    |

### Points d'inflexion sentiment (z-score)

| key       | year_week   | week_start   |   net_support |   z_score | direction   |   n_replies |
|:----------|:------------|:-------------|--------------:|----------:|:------------|------------:|
| Brossat   | 2025-W17    | 2025-04-21   |        -33.33 | -14.654   | Baisse      |           3 |
| Mariani   | 2025-W43    | 2025-10-20   |          0    |  13.4478  | Hausse      |           1 |
| Brossat   | 2026-W03    | 2026-01-12   |        -57.14 |  -5.24582 | Baisse      |          14 |
| Knafo     | 2026-W06    | 2026-02-02   |         46.67 |   5.20067 | Hausse      |          45 |
| Dati      | 2025-W17    | 2025-04-21   |        100    |   4.85453 | Hausse      |           2 |
| Bournazel | 2026-W06    | 2026-02-02   |        -33.33 |  -4.70197 | Baisse      |           3 |
| Knafo     | 2025-W38    | 2025-09-15   |        -25    |  -4.35206 | Baisse      |           8 |
| Dati      | 2026-W03    | 2026-01-12   |        100    |   3.83272 | Hausse      |           1 |
| Gregoire  | 2025-W41    | 2025-10-06   |         71.43 |   3.75538 | Hausse      |           7 |
| Brossat   | 2026-W08    | 2026-02-16   |       -100    |  -3.7147  | Baisse      |           1 |
| Chikirou  | 2026-W02    | 2026-01-05   |        -56.41 |  -3.36326 | Baisse      |          39 |
| Mariani   | 2026-W05    | 2026-01-26   |         50    |   3.32383 | Hausse      |           4 |
| Bournazel | 2025-W26    | 2025-06-23   |          0    |  -3       | Baisse      |          11 |
| Gregoire  | 2025-W24    | 2025-06-09   |         40    |  -2.96936 | Baisse      |           5 |
| Bournazel | 2026-W07    | 2026-02-09   |        -60    |  -2.92572 | Baisse      |           5 |

### Sentiment autour des anomalies (avant/pendant/après)

| periode   |   n_nsi |   med_nsi |   med_hostilite |   p_mw_nsi_bd |   p_mw_nsi_da |   p_mw_host_bd |   p_mw_host_da |
|:----------|--------:|----------:|----------------:|--------------:|--------------:|---------------:|---------------:|
| avant     |      42 |     2.085 |           21.01 |    nan        |    nan        |     nan        |     nan        |
| pendant   |      46 |     0     |           16.67 |      0.933271 |    nan        |       0.482257 |     nan        |
| après     |      41 |     4.35  |           18.52 |    nan        |      0.942222 |     nan        |       0.639392 |

# A4 — Echo chambers et homophilie

*Structure des audiences : fermeture, chevauchement, homophilie idéologique*


### Scores echo chamber par candidat

| candidate_id          | label     | bloc            |   n_audience |   exclusive_pct |   same_camp_pct |   cross_camp_pct |   echo_score |
|:----------------------|:----------|:----------------|-------------:|----------------:|----------------:|-----------------:|-------------:|
| sarah_knafo           | Knafo     | Droite          |        10602 |            81.8 |             6.3 |             11.9 |         88.1 |
| sophia_chikirou       | Chikirou  | Gauche radicale |          701 |            74.6 |             3.1 |             22.3 |         77.7 |
| rachida_dati          | Dati      | Droite          |         4184 |            61.2 |            15.9 |             22.9 |         77.1 |
| emmanuel_gregoire     | Gregoire  | Gauche          |          551 |            61.2 |             6.4 |             32.5 |         67.5 |
| ian_brossat           | Brossat   | Gauche radicale |         1340 |            60.6 |             1.6 |             37.8 |         62.2 |
| pierre_yves_bournazel | Bournazel | Centre-droit    |         2612 |            58.2 |             0   |             41.8 |         58.2 |
| thierry_mariani       | Mariani   | Extreme droite  |         1720 |            57.4 |             0   |             42.6 |         57.4 |
| david_belliard        | Belliard  | Gauche          |         1279 |            49.7 |             2.7 |             47.5 |         52.5 |
**Echo score** = % audience exclusive + homogène. Knafo (88%), Chikirou (78%), Dati (77%) = audiences les plus fermées.


### Paires Jaccard (chevauchement audiences) — top 15

| k1        | k2       |    jac |   dist_ideo | same_camp   |
|:----------|:---------|-------:|------------:|:------------|
| Bournazel | Dati     | 0.0926 |           1 | False       |
| Brossat   | Belliard | 0.0926 |           2 | False       |
| Bournazel | Belliard | 0.0784 |           2 | False       |
| Dati      | Knafo    | 0.076  |           1 | False       |
| Gregoire  | Belliard | 0.0633 |           1 | True        |
| Knafo     | Mariani  | 0.0498 |           1 | True        |
| Dati      | Belliard | 0.0448 |           3 | False       |
| Dati      | Mariani  | 0.0411 |           2 | False       |
| Bournazel | Knafo    | 0.0394 |           2 | False       |
| Bournazel | Brossat  | 0.0384 |           4 | False       |
| Gregoire  | Brossat  | 0.0384 |           3 | False       |
| Bournazel | Mariani  | 0.0376 |           3 | False       |
| Dati      | Brossat  | 0.0323 |           5 | False       |
| Bournazel | Gregoire | 0.0273 |           1 | False       |
| Chikirou  | Brossat  | 0.0246 |           1 | True        |
**Homophilie confirmée :** Bournazel-Dati, Brossat-Belliard, Gregoire-Belliard = paires proches idéologiquement avec overlap élevé.


# A5 — Interactions inter-candidats

*Mentions, lift, thèmes des posts cross-candidats*


### Matrice des mentions (qui mentionne qui)

            Belliard  Gregoire  Brossat  Bournazel  Dati  Knafo  Chikirou  Mariani
Unnamed: 0                                                                        
Belliard           0        13        4          1     2      0         0        0
Gregoire           5         0        9          0     6      0         0        0
Brossat            1        27        0          0     3      0         0        0
Bournazel          1        11        0          0     5      0         0        0
Dati               0         5        0          0     0      0         0        0
Knafo              0         2        0          0     0      0         0        0
Chikirou           0        21        1          4    14      0         0        0
Mariani            0         1        0          0     3      0         0        0

**Grégoire** reçoit 80 mentions (Brossat 27, Chikirou 21, Belliard 13, Bournazel 11, Dati 6). Knafo, Chikirou, Mariani = 0 mention reçue (silo).


### Lift engagement (posts cross-candidats vs normaux)

| candidate_id          | label     |   n_cross_posts |   n_normal_posts |   avg_eng_cross |   avg_eng_normal |   lift_pct |
|:----------------------|:----------|----------------:|-----------------:|----------------:|-----------------:|-----------:|
| rachida_dati          | Dati      |               5 |              881 |          1167.2 |            806   |       44.8 |
| emmanuel_gregoire     | Gregoire  |              16 |             1147 |           217.5 |            170.8 |       27.3 |
| sophia_chikirou       | Chikirou  |              23 |              858 |          1317.8 |           1492   |      -11.7 |
| sarah_knafo           | Knafo     |               2 |             1187 |         17180.5 |          20350.8 |      -15.6 |
| ian_brossat           | Brossat   |              31 |             1111 |          1107.6 |           1670.2 |      -33.7 |
| pierre_yves_bournazel | Bournazel |              16 |              831 |           240.2 |            583.8 |      -58.8 |
| david_belliard        | Belliard  |              18 |              602 |           139.2 |            815.5 |      -82.9 |
| thierry_mariani       | Mariani   |               3 |              928 |           296   |           2303.4 |      -87.1 |
**Dati, Grégoire** : lift positif (être mentionné amplifie l'ER). **Belliard, Mariani** : lift très négatif (-82%, -87%).


### Thèmes des interactions (hors 'autre')

- alliance: 29 mentions

- programme: 26 mentions

- logement: 20 mentions

- economie: 19 mentions

- securite: 6 mentions

- attaque: 5 mentions

- ecologie: 3 mentions

- immigration: 1 mentions


**Alliance (29) >> Programme >> Attaque (5).** Interactions coopératives, pas confrontationnelles.


# A6 — CamemBERT fine-tuning

*Classification sentiment 4 classes : zero-shot vs fine-tuned*


### Résultats comparatifs

| Modèle | Accuracy | F1-macro |

|--------|----------|----------|

| Zero-shot CamemBERT | 0.526 | 0.336 |

| Fine-tuned CamemBERT | 0.456 | 0.441 |


**Amélioration :** +0.105 en F1-macro. F1 < 0.55 : déséquilibre des classes (n=227 train, n=57 test).

**F1 par classe (fine-tuned) :** CRITIQUE 0.35, HOSTILITE 0.51, IRONIE 0.38, SOUTIEN 0.53.

**Conclusion :** Preuve de concept. Pour F1>=0.70 : ~2000 annotations stratifiées recommandées.


# A7 — Synthèse croisée

*Tableau de bord consolidé, thèse centrale, régression exploratoire*


### Tableau de synthèse A7 (consolidé A1-A5)

| key       |   er_median_pct |   er_mean_pct |   er_std_pct |   n_semaines |        nsi |   host_pct |     n |   echo_score |   n_audience |   exclusive_pct |   cross_camp_pct |   pct_hostilite |   pct_ironie |   lift_pct |   n_cross_posts | camp           |   ideo | label                |   mentions_recues |
|:----------|----------------:|--------------:|-------------:|-------------:|-----------:|-----------:|------:|-------------:|-------------:|----------------:|-----------------:|----------------:|-------------:|-----------:|----------------:|:---------------|-------:|:---------------------|------------------:|
| Brossat   |          6.4231 |        7.3141 |       3.9908 |           55 | -0.208675  |    32.8839 |  1706 |         62.2 |         1340 |            60.6 |             37.8 |        36.8189  |      9.72889 |      -33.7 |              31 | Extreme gauche |      1 | Brossat (PCF)        |                14 |
| Chikirou  |          4.0932 |        5.5752 |       4.557  |           51 | -0.250941  |    39.6487 |   797 |         77.7 |          701 |            74.6 |             22.3 |        35.8294  |     16.2511  |      -11.7 |              23 | Extreme gauche |      2 | Chikirou (LFI)       |                 0 |
| Belliard  |          0.8571 |        1.5031 |       1.1661 |           43 | -0.132664  |    26.1628 |  1892 |         52.5 |         1279 |            49.7 |             47.5 |        15.1916  |      7.33842 |      -82.9 |              18 | Gauche         |      3 | Belliard (EELV)      |                 7 |
| Gregoire  |          1.1613 |        1.4519 |       0.8961 |           57 |  0.03698   |    18.6441 |   649 |         67.5 |          551 |            61.2 |             32.5 |         9.23158 |      8.78842 |       27.3 |              16 | Gauche         |      4 | Gregoire (PS)        |                80 |
| Bournazel |          2.2778 |        2.7668 |       1.4231 |           57 | -0.107046  |    25.9879 |  4783 |         58.2 |         2612 |            58.2 |             41.8 |        14.0836  |      7.14714 |      -58.8 |              16 | Centre         |      5 | Bournazel (Horizons) |                 5 |
| Dati      |          0.6034 |        0.8968 |       0.8202 |           53 | -0.103664  |    25.3213 |  8325 |         77.1 |         4184 |            61.2 |             22.9 |        19.7114  |      8.3981  |       44.8 |               5 | Droite         |      6 | Dati (LR)            |                33 |
| Knafo     |         11.5324 |       32.6573 |      54.3881 |           57 |  0.145479  |    21.9772 | 23811 |         88.1 |        10602 |            81.8 |             11.9 |        20.1428  |      8.7828  |      -15.6 |               2 | Extreme droite |      7 | Knafo (Reconquete)   |                 0 |
| Mariani   |          3.118  |        4.8901 |       5.8853 |           54 | -0.0380639 |    25.235  |  2128 |         57.4 |         1720 |            57.4 |             42.6 |        25.441   |      4.734   |      -87.1 |               3 | Extreme droite |      8 | Mariani (RN)         |                 0 |

### C3 — Test de la thèse centrale

**Thèse :** Fermeture des audiences (echo) → plus d'hostilité reçue.

| Corrélation | rho | p | Résultat |

|------------|-----|---|----------|

| Echo ~ Hostilité | +0.214 | 0.6103 | Non significatif |

| Echo ~ NSI | +0.214 | 0.6103 | Non significatif |

| Echo ~ ER | +0.405 | 0.3199 | Non significatif |


**Conclusion :** Thèse NON validée. n=8, puissance insuffisante. La fermeture ne prédit pas l'hostilité.


### C4 — Régression exploratoire (prédicteurs de l'ER)

| Prédicteur | rho | p | Signal |

|------------|-----|---|--------|

| % Hostilité (A3) | +0.643 | 0.0856 | * (marginal) |

| Echo score (A4) | +0.405 | 0.3199 | ns |

| Mentions reçues (A5) | -0.610 | 0.1084 | ns |

| NSI (A3) | 0.000 | 1.0000 | ns |

| Lift mentions (A5) | -0.190 | 0.6514 | ns |


**Knafo = outlier majeur** (er_median=11.5‰). Sans Knafo, corrélations changent.


### 7 Findings principaux

- [1] Grégoire (PS) = hub structurant — 57% des mentions, ER faible (1.2‰). Fait l'agenda, pas l'engagement.

- [2] Knafo = outlier structurel — ER 11.5‰ (3× moyenne), NSI positif. Niche très engagée.

- [3] Homophilie idéologique confirmée — distance_ideo ~ Jaccard rho=-0.60, p=0.0007.

- [4] Echo ≠ hostilité — fermeture ne prédit pas l'hostilité (rho=+0.21, p=0.61).

- [5] Négativité → engagement partiel — global rho=+0.26, hétérogène par candidat.

- [6] Interactions coopératives — Alliance 29, Attaque 5. Droite radicale en silo (0 mention).

- [7] CamemBERT fine-tuné F1=0.44 — amélioration modeste sur zero-shot (0.34).



### Limites méthodologiques

- L1 — Taille du corpus : n=8 candidats, corrélations exploratoires.

- L2 — Classification GPT-5 Nano non validée.

- L3 — Axe idéologique ordinal simplifié.

- L4 — Biais plateforme Twitter/X post-Musk (Milli et al. 2025).

- L5 — Absence de données de sondage (écart online/offline).



# A7 — Analyses stratifiées par plateforme

*Comparaison Twitter vs Instagram (TikTok : données insuffisantes)*


### Volume par plateforme

- twitter: 41,101 replies

- instagram: 2,990 replies



### NSI et % hostilité par candidat × plateforme

**TWITTER**

*replies_classified: Expected numeric dtype, got object instead.*


### ER médiane (‰) par plateforme

| key       |   Twitter_ER_permil |   Instagram_ER_permil |
|:----------|--------------------:|----------------------:|
| Belliard  |                0.86 |                 12.54 |
| Bournazel |                2.28 |             123000    |
| Brossat   |                6.42 |                 15.19 |
| Chikirou  |                4.09 |                 10.85 |
| Dati      |                0.6  |                 11.67 |
| Gregoire  |                1.16 |                  8.31 |
| Knafo     |               11.53 |                 13.21 |
| Mariani   |                3.12 |                  7.85 |

**Note :** Instagram utilise likes+comments (pas de views). Comparaison indicative.


### Synchronie Twitter ↔ Instagram (corrélation hebdomadaire)

| candidate_id          | candidate_label           | platform_1   | platform_2   |   spearman_rho |   p_value |   n_weeks | synchrony   |
|:----------------------|:--------------------------|:-------------|:-------------|---------------:|----------:|----------:|:------------|
| david_belliard        | D. Belliard (EELV)        | twitter      | instagram    |          0.516 |    0.0004 |        43 | modéré      |
| emmanuel_gregoire     | E. Grégoire (PS)          | twitter      | instagram    |          0.699 |    0      |        55 | synchronisé |
| ian_brossat           | I. Brossat (PCF)          | twitter      | instagram    |          0.205 |    0.133  |        55 | indépendant |
| pierre_yves_bournazel | P-Y. Bournazel (Horizons) | twitter      | instagram    |          0.821 |    0      |        53 | synchronisé |
| rachida_dati          | R. Dati (LR)              | twitter      | instagram    |          0.235 |    0.1286 |        43 | indépendant |
| sarah_knafo           | S. Knafo (Reconquête)     | twitter      | instagram    |          0.493 |    0.0001 |        56 | modéré      |
| sophia_chikirou       | S. Chikirou (LFI)         | twitter      | instagram    |         -0.004 |    0.9761 |        49 | indépendant |
| thierry_mariani       | T. Mariani (RN)           | twitter      | instagram    |          0.21  |    0.3041 |        26 | indépendant |
**Synchronisés (rho>0.6):** Grégoire, Bournazel. **Modérés (0.4-0.6):** Belliard, Knafo. **Indépendants:** Brossat, Chikirou, Dati, Mariani.


### TikTok

39 données disponibles — corpus insuffisant pour analyse statistique. Algorithme discovery-first vs social-first. Perspective P1 : extension avec collecte systématique.


---
*Pipeline A1→A7 · Paris Municipales 2026 · Données Jan 2025 - Fév 2026*
