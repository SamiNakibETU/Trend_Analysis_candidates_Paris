# Note d'analyse : Paris Municipales 2026

Synthèse des principaux résultats de l'analyse numérique des campagnes des 8 candidats.

## Qui domine la conversation ?

Sarah Knafo concentre 54 % des réponses (23 811 sur 44 599) et affiche un ER médian 5 fois supérieur à la médiane des 7 autres. Son audience forme la bulle la plus homogène (88,1 % d'echo score). Le volume et la viralité ne font pas la diversité : sa base réagit massivement mais dialogue peu avec les autres candidats.

Emmanuel Grégoire occupe une place à part. Il reçoit 80 des 139 mentions cross-candidats (57 %) : on parle de lui bien plus qu'il ne parle des autres. Son ER médian est faible (1,16 ‰) mais son NSI positif (+0,04) et son lift positif (+27,3 %) montrent qu'il bénéficie d'un engagement mesuré et bienveillant quand il est évoqué. Seul candidat en momentum haussier sur les 8 dernières semaines.

## Sentiment et polarisation

Le corpus global penche vers la critique (38 %) puis le soutien (27 %), l'hostilité (24 %) et l'ironie (11 %). Chikirou subit la plus forte hostilité (39,6 %) et le NSI le plus négatif (-0,25). Brossat (-0,21) et Belliard (-0,13) suivent. Knafo et Grégoire sont les seuls à bilan positif.

La régression logistique CRITIQUE vs HOSTILITÉ montre une séparation lexicale nette : insultes et attaques personnelles côté hostilité, évaluation programmatique côté critique.

## Plateformes et stratégie

Instagram est systématiquement plus bienveillant. Grégoire passe de 8 % de soutien sur Twitter à 31 % sur Instagram. La synchronie varie : Bournazel et Grégoire (ρ > 0,7) adoptent une stratégie unifiée entre les deux plateformes ; Chikirou reste indépendante (ρ ≈ 0).

## Échos et homophilie

Le Jaccard diminue quand la distance idéologique croît. Les paires Bournazel-Dati, Brossat-Belliard et Bournazel-Belliard ont les plus forts chevauchements d'audience. 19 017 auteurs uniques pour 44 599 réponses : une minorité concentre l'activité.

## Données et reproductibilité

Les résultats chiffrés exhaustifs sont dans `RESULTATS_CHIFFRES.md`, généré par `scripts/export_resultats_chiffres.py`. La méthodologie est détaillée dans `methodologie.md`. Les notebooks 01 à 09 reproduisent les analyses à partir des données placées dans `final/data/`.
