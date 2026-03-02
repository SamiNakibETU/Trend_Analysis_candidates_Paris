# Matériau Substack & threads X

Stats et outlines prêts à l'emploi pour articles et threads.

---

## Stats à l'emporte-pièce (copier-coller)

| Stat | Texte prêt |
|------|------------|
| Volume | 7 659 tweets, 3 317 posts Instagram, 44 599 réponses classifiées — 8 candidats Paris 2026 |
| Knafo outlier | Sarah Knafo (Reconquête) : ER 11,5‰ = 5× la médiane des 7 autres candidats |
| Hub Grégoire | Emmanuel Grégoire reçoit 57 % des mentions cross-candidats, mais rang 6/8 en engagement |
| Echo Knafo | 88 % des comptes qui répondent à Knafo interagissent uniquement avec son camp ou la même famille politique |
| Bulles idéologiques | Moins deux candidats sont proches idéologiquement, plus leurs audiences se chevauchent : ρ = −0,60 |
| Instagram bienveillant | Grégoire : 8 % soutien sur Twitter → 31 % sur Instagram |
| Hostilité × ER | Corrélation globale ρ = +0,26 : la négativité booste l'engagement, mais hétérogène (Belliard +0,51, Brossat −0,63) |
| Lift Dati | Quand Rachida Dati mentionne un adversaire, son ER augmente de 45 % |
| NSI Knafo | Seul candidat à NSI nettement positif (+0,15) ; Chikirou le plus négatif (−0,25) |
| Pas de coordination | Méthodologie Cinelli et al. : aucune campagne de bots coordonnée détectée |

---

## Outline thread 1 : « Qui domine Twitter aux municipales Paris 2026 ? »

1. **Hook** : 8 candidats, 7 659 tweets, 13 mois. Qui a le plus d’impact ?
2. Sarah Knafo (Reconquête) : ER 11,5‰, 5× la médiane. Audience nationale (Parlement européen).
3. Emmanuel Grégoire : hub du débat (57 % des mentions) mais ER faible. Invisible numériquement.
4. Brossat, Chikirou, Mariani : médianes 3–6‰. Gauche radicale et extrême droite plus engagées.
5. Dati, Belliard : ER < 1‰. La droite modérée et l’écologie peinent à capter.
6. **Conclusion** : polarisation = moteur de l’engagement. Pas la qualité programmatique.

---

## Outline thread 2 : « Les audiences sont des bulles »

1. **Hook** : Qui répond à qui ? Chevauchement des audiences entre candidats.
2. Jaccard : moins deux candidats sont proches idéologiquement, plus leurs audiences se chevauchent (ρ = −0,60).
3. Knafo : 88 % echo score. Sa communauté répond presque exclusivement à elle-même.
4. Dati, Chikirou : 77 % echo. Bulles structurées.
5. Grégoire, Brossat : plus de croisement. Ce sont les hubs.
6. **Conclusion** : Les réseaux sociaux reflètent des silos. Pas de débat transversal.

---

## Outline thread 3 : « Twitter vs Instagram — deux campagnes »

1. **Hook** : Même candidats, deux plateformes. Même histoire ?
2. Instagram : systématiquement plus bienveillant. Grégoire 8 % → 31 % soutien.
3. Synchronie : Bournazel et Grégoire (ρ > 0,7) alignent leurs rythmes. Stratégie unifiée.
4. Chikirou : ρ ≈ 0. Indépendante. Twitter court, Instagram visuel.
5. **Conclusion** : Les plateformes racontent des campagnes différentes. Instagram = vitrine, Twitter = arène.

---

## Outline thread 4 : « L’hostilité paye (ou pas) »

1. **Hook** : La négativité booste l’engagement. Vraiment ?
2. Corrélation globale : ρ = +0,26. Oui, en moyenne.
3. Mais : Belliard ρ = +0,51 (l’hostilité aide), Brossat ρ = −0,63 (elle démobilise).
4. Knafo : NSI +0,15, 36 % soutien. Sa communauté est mobilisée.
5. Chikirou : NSI −0,25, 39 % hostilité. Les attaques la ciblent.
6. **Conclusion** : L’effet dépend du candidat. Pas de règle unique.

---

## Outline thread 5 : « Méthodo OSINT — comment on a fait »

1. **Hook** : 44 599 réponses classifiées. Comment ?
2. Données : Nitter (Twitter), scraping Instagram. Période janv 2025 – fév 2026.
3. Sentiment : GPT-5 Nano, 4 classes (CRITIQUE, SOUTIEN, HOSTILITÉ, IRONIE).
4. Validation : TF-IDF discriminants, benchmark CamemBERT. Pas de coordination (Cinelli).
5. Reproducible : 9 notebooks Jupyter, code sur GitHub.
6. **Conclusion** : OSINT = rigueur + transparence méthodologique.

---

## Figures à embarquer (chemins figures/)

| Figure | Usage |
|--------|-------|
| `01_er_classement.png` | Classement ER, Knafo en tête |
| `01_er_boxplot.png` | Distribution, boxplot par candidat |
| `03_nsi.png` | NSI par candidat |
| `04_echo.png` | Echo score |
| `05_network.png` | Réseau mentions (Grégoire hub) |
| `06_sentiment_crossplatform.png` | Twitter vs Instagram soutien |
| `06_synchronie.png` | Corrélation Spearman cross-platform |

---

## Titres Substack possibles

- « Municipales Paris 2026 : qui domine la conversation numérique ? »
- « Les audiences politiques sont des bulles — la preuve par les données »
- « Twitter vs Instagram : deux campagnes, une élection »
- « L’hostilité paye-t-elle ? Ce que disent 44 000 réponses aux candidats »
- « OSINT électoral : méthodologie d’une analyse de campagne »
