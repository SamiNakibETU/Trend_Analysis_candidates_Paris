# Fichier d'annotation — 40 tweets par candidat

- **annotation_40_per_candidate.csv** : 320 tweets (40 × 8 candidats), séparateur `;`, UTF-8 avec BOM (ouvert proprement dans Excel).
- **annotation_40_per_candidate.jsonl** : même contenu en JSON Lines.

## Colonnes

| Colonne | Description |
|--------|-------------|
| candidate_id | Identifiant candidat |
| candidate_label | Libellé affiché |
| tweet_id | ID Twitter du tweet |
| timestamp | Date/heure |
| text | Texte du tweet |
| likes, comments, shares | Métriques |
| **topic_manual** | À remplir : thème/sujet (ex. propreté, logement, sécurité) pour BERTopic |
| **sentiment_manual** | Optionnel : SOUTIEN / CRITIQUE / HOSTILITE / IRONIE / NEUTRE |
| notes | Notes libres |

## Utilisation avec BERTopic

1. Renseigner `topic_manual` (et éventuellement `sentiment_manual`) dans le CSV.
2. Charger le CSV, extraire la colonne `text` (et filtrer les lignes annotées).
3. Lancer BERTopic sur le corpus `text` (ou par candidat) pour affiner les topics.

```python
import pandas as pd
from bertopic import BERTopic

df = pd.read_csv("annotation_40_per_candidate.csv", sep=";", encoding="utf-8-sig")
docs = df["text"].fillna("").tolist()
# Option : filtrer par candidat pour topics par candidat
topic_model = BERTopic(embedding_model="paraphrase-multilingual-MiniLM-L12-v2", language="french")
topics, probs = topic_model.fit_transform(docs)
```

## Régénérer le fichier

```bash
python analysis/v3/create_annotation_file.py
```

(Échantillon aléatoire fixe, seed=42.)
