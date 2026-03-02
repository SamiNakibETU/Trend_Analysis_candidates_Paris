# Guide d'annotation — Fine-tuning CamemBERT

## Quel fichier utiliser ?

**Ouvre et annote uniquement : `bert_annotation_TO_ANNOTATE.csv`**

- Séparateur : **;** (point-virgule)
- Encodage : UTF-8 (Excel : "Données > Depuis un fichier texte", choisir `;`, UTF-8)
- Ce fichier ne contient **pas** l’ancienne colonne "sentiment" (donc plus de NEUTRE trompeur).

---

## Quelle colonne remplir ?

**Une seule colonne à remplir obligatoirement : `annotation_4class`**

Mets **exactement** une de ces 4 valeurs (en majuscules) :

| Valeur à taper | Signification |
|---|---|
| **SOUTIEN** | Le commentaire approuve, encourage ou défend le candidat ou ses idées (éloges, "bravo", "je vote pour vous", défense). |
| **CRITIQUE** | Le commentaire conteste les idées ou le programme avec des arguments ("et avec quel argent ?", "vos chiffres sont faux", comparaisons défavorables). |
| **HOSTILITE** | Le commentaire attaque la personne : insulte, mépris, attaque personnelle ("débile", "la honte", "dégage", accusations graves). |
| **IRONIE** | Sarcasme ou second degré : le sens littéral est l’inverse du sens réel (faux éloges, "Bravo…" moqueur, emojis 🤡😂 en contexte hostile). |

**Il n’y a pas de NEUTRE.** En cas de vrai doute entre SOUTIEN et "ni pour ni contre", choisis :
- **CRITIQUE** s’il y a un bémol ou une remise en cause,
- **SOUTIEN** s’il y a un minimum d’approbation ou d’encouragement.

---

## Colonnes optionnelles

- **confiance** : `1` = sûr, `2` = hésitation entre 2 classes, `3` = très ambigu
- **annotateur** : tes initiales
- **notes** : tout commentaire utile (ex. "limite CRITIQUE/IRONIE")

---

## Règles rapides

- Ignorer les fautes d’orthographe.
- Contexte = commentaire **adressé au candidat** (pas un avis général sur la politique).
- Si à la fois critique et ton hostile → mettre **HOSTILITE**.
- Si éloge mais clairement ironique → mettre **IRONIE**.

---

## Après annotation

Sauvegarde le CSV (séparateur `;`, UTF-8). Ce fichier annoté servira à fine-tuner CamemBERT (script à lancer ensuite).
