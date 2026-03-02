# Rapport fine-tuning BERT/RoBERTa

## Métriques (test set)

- Accuracy: 0.186
- F1 macro: 0.145

### F1 par classe

- CRITIQUE: 0.320
- HOSTILITE: 0.000
- IRONIE: 0.258
- SOUTIEN: 0.000

### Matrice de confusion

| | CRITIQUE | HOSTILITE | IRONIE | SOUTIEN |
|---|---|---|---|---|
| CRITIQUE | 4 | 0 | 4 | 0 |
| HOSTILITE | 9 | 0 | 13 | 0 |
| IRONIE | 1 | 0 | 4 | 0 |
| SOUTIEN | 3 | 0 | 5 | 0 |

Source: train_sentiment_bert.py
