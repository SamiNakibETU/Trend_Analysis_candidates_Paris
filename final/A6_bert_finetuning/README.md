# A6 — Fine-tuning CamemBERT

**Question** : Peut-on entraîner un modèle open-source à classifier le sentiment politique ?

## Fichiers

### annotations_mono_label.csv — 304 lignes
⭐ DATASET PRINCIPAL pour le fine-tuning classification simple.
Colonnes : candidate_id, candidate_label, candidate_name, parti, camp,
stratum, reply_id, platform, text, text_len, likes,
annotation_4class (brute, multi-label possible),
label_dominant (classe unique — règle de priorité : HOSTILITE > IRONIE > CRITIQUE > SOUTIEN > DEMANDE),
labels_multi (toutes les classes mentionnées, séparées par |),
n_labels, is_ambiguous,
confiance, annotateur, notes

Distribution label_dominant :
- HOSTILITE : 149 (49%)
- SOUTIEN   : 55  (18%)
- CRITIQUE  : 50  (16%)
- IRONIE    : 30  (10%)
- DEMANDE   : 20  (7%)

### annotations_multi_label.csv — 316 lignes
⭐ DATASET pour le fine-tuning multi-label.
Identique + colonnes binaires :
lbl_soutien, lbl_critique, lbl_hostilite, lbl_ironie, lbl_demande, lbl_hors_sujet

176/316 annotations sont multi-labels (plusieurs classes simultanées).

### annotations_all.csv — 316 lignes
Toutes les annotations (incluant INCONNU et PUB, exclus des datasets d'entraînement).

### annotation_stats.json
Statistiques de synthèse (counts par label, strates, ambiguïté).

## Stratification
40 exemples par candidat × 8 candidats :
- 10 top_engagement (likes élevés)
- 10 low_engagement (likes faibles)
- 10 short (<15 mots)
- 10 long (>50 mots)

## Classes manquantes / déséquilibre
HOSTILITE est sur-représenté dans les strates top_engagement (tweets viraux = souvent haineux).
Pour le fine-tuning : pondérer les classes (class_weight='balanced').
