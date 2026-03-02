#!/usr/bin/env bash
# Paris Municipales 2026 — Exécution du pipeline (ordre des notebooks)
# Prérequis: pip install -r requirements.txt, données dans final/data/

set -e
cd "$(dirname "$0")"

echo "=== Paris 2026 — Pipeline ==="
echo "1. Vérification des données..."
test -f final/data/replies_classified.csv || { echo "Placer replies_classified.csv dans final/data/"; exit 1; }

echo "2. Export des résultats chiffrés..."
python scripts/export_resultats_chiffres.py

echo "3. Pour exécuter les notebooks :"
echo "   jupyter notebook notebooks/01_engagement_viralite.ipynb"
echo "   (ou jupyter execute notebooks/*.ipynb pour batch)"
echo ""
echo "4. Fine-tuning BERT (optionnel) :"
echo "   python scripts/prepare_annotations.py"
echo "   python scripts/train_sentiment_bert.py"
echo ""
echo "=== Pipeline prêt ==="
