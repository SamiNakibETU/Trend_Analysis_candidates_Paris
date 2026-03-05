# Kit médias Substack / X (Twitter)

## Usage

1. Exécuter le notebook `Paris_Municipales_2026_Final.ipynb` pour générer les figures dans `../`
2. Optionnel : redimensionner les 5–6 figures clés en 1200×630 px (ratio card X/Substack)
3. Légendes : `legends_x.txt` — une par figure, ≤ 280 caractères pour X

## Figures prioritaires pour social

- `P1_C3_er_classement.png` — Knafo outlier
- `P5_C23_network.png` — Grégoire hub (narrative forte)
- `P3_C13_nsi.png` — Sentiment
- `P4_C19_echo.png` — Echo chambers
- `P1_C6_momentum.png` — Déclin 7/8
- `P6_C28_synchronie.png` — Cross-platform

## Export 1200×630 (optionnel)

```python
from PIL import Image
img = Image.open('P1_C3_er_classement.png')
img.resize((1200, 630), Image.Resampling.LANCZOS).save('social/P1_ER_classement_1200x630.png')
```
