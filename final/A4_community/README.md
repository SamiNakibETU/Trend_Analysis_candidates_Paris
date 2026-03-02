# A4 — Communautés et Réseau d'Audience

**Question** : Y a-t-il des chambres d'écho ? Les audiences se chevauchent-elles ?

## Fichiers

### audience_overlap_matrix.csv — 8×8 matrice
Similarité de Jaccard entre audiences de candidats.
Index = candidat émetteur, colonnes = candidat cible.
Valeurs entre 0 (aucun utilisateur commun) et 1 (audiences identiques).
Renommé avec SHORT_LABELS (Knafo, Dati, etc.)

### echo_chamber_scores.csv — 8 lignes
Score de chambre d'écho par candidat.
Colonnes : candidate_id, label, bloc, n_audience,
exclusive_pct (n'engage qu'un seul candidat),
same_camp_pct (n'engage que son camp),
cross_camp_pct (engage d'autres camps),
echo_score (exclusive_pct + same_camp_pct)

Résultats clés :
- Knafo : 88.1% echo_score (audience la plus fermée)
- Belliard : 52.5% (audience la plus ouverte)

### community_membership.csv — 2 963 lignes
Utilisateurs ayant interagi avec ≥ 2 candidats.
Colonnes : author, dominant_candidate, dominant_camp,
n_candidates_engaged, candidates_list,
eng_david_belliard, eng_emmanuel_gregoire, ... (binaire par candidat),
community, comm_dominant_candidate

### cross_candidate_mentions.csv — 21 paires
Mentions directes entre candidats dans leurs tweets.
Colonnes : source, target, source_label, target_label, mentions

### (replies source : final/data/replies_classified.csv)
Les replies pour reconstruire le graphe sont dans final/data/.
