# Méthodologie

Méthodes utilisées pour l'analyse numérique des campagnes des 8 candidats aux municipales de Paris 2026.

## 1. Données

Corpus : 7 659 tweets, 3 317 posts Instagram, 44 599 réponses classifiées. Collecte Twitter via Nitter, Instagram par scraping. Période : janvier 2025 à février 2026. Voir `final/data/README.md` pour le format attendu des fichiers CSV.

## 2. Métriques d'engagement

**Engagement Rate (ER)** : ER = (likes + partages + commentaires) / impressions × 1000, en ‰. L'ER médian par candidat et par semaine sert de base aux comparaisons. Knafo affiche un ER médian 5 fois supérieur à la médiane des 7 autres candidats.

**Momentum** : régression linéaire de l'ER sur les 8 dernières semaines. La pente (‰/semaine) indique la tendance. Seul Grégoire présente une pente positive (non significative à p < 0,10).

## 3. Classification du sentiment

Quatre classes : CRITIQUE, SOUTIEN, HOSTILITÉ, IRONIE. Classification automatique par GPT-5 Nano (prompt : classification en 4 classes sur extraits de réponses aux candidats). Validation : régression logistique TF-IDF (CRITIQUE vs HOSTILITÉ), benchmark CamemBERT sur 284 annotations, et Cohen's kappa sur échantillon humain (voir `scripts/prepare_kappa_sample.py` et `scripts/compute_cohens_kappa.py`). Pipeline : `prepare_annotations.py` pour fusionner les annotations, `train_sentiment_bert.py` pour le fine-tuning (WeightedTrainer, early stopping). Métriques reportées dans `docs/bert_metrics.json` et `docs/BERT_FINETUNING_REPORT.md`. Le notebook `09_bert_finetuning.ipynb` charge le modèle et compare les prédictions à GPT-5 Nano.

**Net Sentiment Index (NSI)** : NSI = (SOUTIEN − HOSTILITÉ) / (SOUTIEN + HOSTILITÉ), borné dans [-1 ; 1]. Le NSI est calculé par candidat sur l'ensemble des replies (pas de pondération temporelle). Intervalles de confiance par bootstrap. Knafo (+0,15) et Grégoire (+0,04) sont les seuls à NSI positif ; Chikirou (-0,25) la plus négative.

## 4. Echo chambers et homophilie

**Echo score** : part des auteurs ayant répondu exclusivement à un candidat ou à des candidats du même camp. echo = |A_exclusif ∪ A_même_camp| / |A_total|. Knafo 88,1 %, Chikirou 77,7 %, Dati 77,1 %.

**Jaccard** : chevauchement des audiences entre paires de candidats. Jaccard(A,B) = |A ∩ B| / |A ∪ B|. Homophilie idéologique : corrélation de Spearman entre distance idéologique et Jaccard (ρ ≈ -0,60). Les candidats proches idéologiquement partagent plus d'audience.

## 5. Topics et thématiques

LDA sur les tweets, 10 topics. Matrice candidat × topic (pourcentages). Thèmes principaux : anti-droite/Dati, logement, sécurité, budget, géopolitique.

**Topics non retenus (artefacts LDA)** : Les topics 5 ("Arrondissement / Liberté / Gauche"), 8 ("Deux / Emmanuel / Peuple") et 9 ("Soutien / Jour / France") présentent des mots trop génériques ou des artefacts (noms propres fréquents, vocabulaires non discriminants). Ils sont exclus des analyses thématiques. Recommandation : tester k=7 ou 8, ou BERTopic pour améliorer la cohérence.

## 6. Interactions entre candidats

**Lift** : différence d'ER entre les posts qui mentionnent un autre candidat et ceux qui ne le mentionnent pas. lift = (ER_cross − ER_baseline) / ER_baseline × 100. Dati (+44,8 %) et Grégoire (+27,3 %) ont un lift positif. Bournazel (-58,8 %) et Belliard (-82,9 %) voient leur ER chuter quand ils mentionnent la concurrence.

**Mentions reçues** : nombre de fois qu'un candidat est mentionné par les autres. Grégoire 80 sur 139 (57 %), hub principal de la conversation cross-candidats.

## 7. Synchronie cross-platform

Corrélation de Spearman entre l'ER hebdomadaire Twitter et Instagram par candidat. Bournazel (ρ = 0,82) et Grégoire (ρ = 0,70) sont synchronisés ; Chikirou (ρ ≈ 0) indépendante.

**Anomalie Bournazel Instagram** : Les données IG de Bournazel présentent un ER médian très élevé (dénominateur views manquant ou aberrant). Ce candidat est exclu des analyses cross-platform ER quand les échelles ne sont pas comparables, ou signalé explicitement sur les figures.

## 8. Anomalies

Détection par Z-score sur l'ER hebdomadaire (global et rolling). Les pics d'anomalies signalent des semaines où un candidat dépasse nettement sa tendance habituelle.

## 9. Limites

Les données ne sont pas pondérées par la représentativité démographique. Le sentiment est estimé par un modèle ; les erreurs de classification peuvent affecter les NSI. Les métriques d'audience (impressions) sont parfois approximées à partir des vues disponibles.

**Déséquilibre du corpus** : Knafo représente 54 % des replies (23 811 / 44 091), contre 1,5 % pour Grégoire (649). Les indicateurs agrégés (NSI, echo score) sont dominés par Knafo. La comparabilité entre candidats est limitée : les intervalles de confiance sur les métriques des candidats à faible volume (Grégoire, Chikirou) sont larges. Causes possibles : viralité différente, couverture Nitter variable, audience nationale (Knafo eurodéputée) vs locale.

**Contrefactuel Knafo** : Si on retire Knafo du corpus, la distribution sentiment globale, le NSI médian et l’echo score moyen changent significativement. L’analyse est donc sensible à ce déséquilibre ; les conclusions sur les 7 autres candidats restent valides.

**Schéma causal hypothétique** :  
Audience nationale (Knafo eurodéputée) → ER élevé → replies massives → echo score élevé. La polarisation et l’engagement sont des variables mutuellement renforçantes : une audience polarisée produit plus de replies ; des replies polarisées augmentent l’echo score.

---

Pour les références académiques, voir [REFERENCES.md](REFERENCES.md).
