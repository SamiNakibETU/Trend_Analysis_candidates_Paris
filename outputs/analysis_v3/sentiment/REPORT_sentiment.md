# Analyse 3 -- Sentiment des Audiences par LLM

*Genere le 2026-02-21 11:10*

---

## 1. Vue d'ensemble

- **44,599** replies/commentaires classifies
  - Twitter : 41,586
  - Instagram : 3,013
- Modele : gpt-5-nano (zero-shot, temperature=0, Batch API)
- Taxonomie : 5 classes (SOUTIEN, CRITIQUE, HOSTILITE, IRONIE, NEUTRE)

### Distribution globale

| Classe | % |
|---|---|
| SOUTIEN | 8.7% |
| CRITIQUE | 1.0% |
| HOSTILITE | 1.0% |
| IRONIE | 0.2% |
| NEUTRE | 89.0% |

## 2. Profil de sentiment par candidat

| Candidat | Replies | Soutien | Critique | Hostilite | Ironie | Neutre | Polarisation | Soutien Net | Controverse |
|---|---|---|---|---|---|---|---|---|---|
| S. Knafo (Reconquete) | 24,106 | 12.5% | 1.0% | 0.9% | 0.2% | 85.3% | 0.01 | 11.64% | 0.15 |
| E. Gregoire (PS) | 650 | 7.5% | 1.7% | 0.6% | 0.3% | 89.8% | 0.01 | 6.92% | 0.10 |
| T. Mariani (RN) | 2,153 | 4.2% | 0.2% | 0.4% | 0.0% | 95.2% | 0.00 | 3.81% | 0.05 |
| P-Y. Bournazel (Horizons) | 4,824 | 5.1% | 1.2% | 1.3% | 0.3% | 92.1% | 0.02 | 3.79% | 0.08 |
| I. Brossat (PCF) | 1,728 | 3.7% | 0.2% | 0.2% | 0.0% | 95.9% | 0.00 | 3.53% | 0.04 |
| D. Belliard (EELV) | 1,914 | 4.9% | 2.7% | 2.0% | 0.6% | 89.8% | 0.03 | 2.82% | 0.10 |
| R. Dati (LR) | 8,419 | 3.5% | 1.0% | 1.0% | 0.2% | 94.3% | 0.01 | 2.58% | 0.06 |
| S. Chikirou (LFI) | 805 | 4.6% | 0.9% | 2.2% | 0.1% | 92.2% | 0.02 | 2.36% | 0.08 |

## 3. Correlation Engagement x Sentiment (Spearman)

| Candidat | rho(ER,Hostilite) | p | rho(ER,Soutien) | p | N |
|---|---|---|---|---|---|
| P-Y. Bournazel (Horizons) | 0.333 | 0.0170 | -0.232 | 0.1013 | 51 |
| T. Mariani (RN) | 0.274 | 0.4758 | -0.059 | 0.8805 | 9 |
| S. Chikirou (LFI) | 0.112 | 0.8579 | -0.100 | 0.8729 | 5 |
| R. Dati (LR) | -0.057 | 0.7737 | 0.238 | 0.2222 | 28 |
| S. Knafo (Reconquete) | -0.102 | 0.4911 | 0.011 | 0.9428 | 48 |
| D. Belliard (EELV) | -0.300 | 0.6238 | -0.200 | 0.7471 | 5 |

## 4. Comparaison Twitter vs Instagram

| Candidat | TW Hostilite | IG Hostilite | TW Soutien | IG Soutien |
|---|---|---|---|---|
| D. Belliard (EELV) | 2.1% | 2.0% | 2.6% | 13.1% |
| E. Gregoire (PS) | 1.2% | 0.2% | 2.8% | 10.6% |
| I. Brossat (PCF) | 0.0% | 0.5% | 2.1% | 7.2% |
| P-Y. Bournazel (Horizons) | 1.3% | 0.0% | 4.8% | 13.6% |
| R. Dati (LR) | 0.8% | 7.9% | 3.4% | 11.5% |
| S. Knafo (Reconquete) | 0.9% | 1.1% | 12.3% | 17.2% |
| S. Chikirou (LFI) | 1.7% | 2.9% | 5.2% | 3.8% |
| T. Mariani (RN) | 0.1% | 7.3% | 4.1% | 7.3% |

## 5. Methodologie

- **Modele** : gpt-5-nano via OpenAI Batch API
- **Batching** : 10 replies par prompt
- **Pre-traitement** : deduplication par texte+candidat, filtre < 3 mots, cap 500 chars
- **Metriques** :
  - Polarisation = (Hostilite + Ironie) / (Soutien + Critique + Neutre)
  - Soutien net = Soutien - Hostilite
  - Controverse = 1 - max(proportion de classe)
- Ref. : Zhang et al. (2024 NAACL), Kuila & Sarkar (2024), ParlaSent (2025)