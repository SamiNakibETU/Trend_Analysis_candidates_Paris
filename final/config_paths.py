"""
Configuration des chemins pour le projet Paris Municipales 2026.
Utiliser depuis le notebook ou les scripts pour éviter les chemins hardcodés.
"""
from pathlib import Path

# Racine du projet (parent de final/)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Données
DATA_RAW = PROJECT_ROOT / "final" / "data"
A1_DATA = PROJECT_ROOT / "final" / "A1_temporal" / "data"
A1_OUT = PROJECT_ROOT / "final" / "A1_temporal" / "outputs"
A2_DATA = PROJECT_ROOT / "final" / "A2_topics" / "data"
A3_DATA = PROJECT_ROOT / "final" / "A3_sentiment" / "data"
A3_OUT = PROJECT_ROOT / "final" / "A3_sentiment" / "outputs"
A4_DATA = PROJECT_ROOT / "final" / "A4_community" / "data"
A4_OUT = PROJECT_ROOT / "final" / "A4_community" / "outputs"
A5_DATA = PROJECT_ROOT / "final" / "A5_interactions" / "data"
A6_OUT = PROJECT_ROOT / "final" / "A6_bert_finetuning" / "outputs"

# Outputs du notebook principal
OUT = PROJECT_ROOT / "final" / "outputs"


def ensure_outputs():
    """Crée le dossier outputs s'il n'existe pas."""
    OUT.mkdir(parents=True, exist_ok=True)
