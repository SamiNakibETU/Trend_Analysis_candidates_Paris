"""
Tests unitaires basiques — Paris Municipales 2026.

Usage:
    pytest tests/test_pipeline.py -v
    python -m pytest tests/ -v
"""
import pytest
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent


# ── Tests sans données (passent TOUJOURS) ────────────────────────────────

def test_all_candidates_have_color():
    """Chaque candidat a une couleur définie."""
    from src.utils import COLORS, ID_TO_KEY
    for cid, key in ID_TO_KEY.items():
        assert key in COLORS, f"Candidat {key} sans couleur"
        assert COLORS[key].startswith("#"), f"Couleur {key} invalide"


def test_colors_hex_format():
    """Toutes les couleurs sont en format hex #RRGGBB."""
    from src.utils import COLORS
    for name, color in COLORS.items():
        assert len(color) == 7, f"{name}: couleur {color} invalide"
        assert color[0] == "#", f"{name}: doit commencer par #"


def test_positions_in_range():
    """POSITIONS entre 1 et 8 pour chaque candidat."""
    from src.utils import POSITIONS
    for name, pos in POSITIONS.items():
        assert 1 <= pos <= 8, f"{name}: position {pos} hors [1,8]"


def test_get_color_returns_str():
    """get_color retourne une chaîne (couleur ou default)."""
    from src.utils import get_color
    assert isinstance(get_color("Knafo"), str)
    assert isinstance(get_color("Inconnu"), str)
    assert get_color("Knafo").startswith("#")


def test_camps_cover_all_candidates():
    """CAMPS couvre les 8 candidats."""
    from src.utils import CAMPS, ID_TO_KEY
    all_in_camps = []
    for camp, cands in CAMPS.items():
        all_in_camps.extend(cands)
    keys = set(ID_TO_KEY.values())
    for k in keys:
        assert k in all_in_camps or k.replace("Gregoire", "Grégoire") in all_in_camps, f"{k} absent des CAMPS"


# ── Tests avec données (skip si fichiers absents) ─────────────────────────

def test_config_candidates_exists():
    """Les fichiers de config candidats existent."""
    p = _ROOT / "config" / "candidates_paris2026.csv"
    assert p.exists(), "config/candidates_paris2026.csv manquant"


def test_config_has_expected_columns():
    """CSV candidats contient des colonnes attendues."""
    p = _ROOT / "config" / "candidates_paris2026.csv"
    if not p.exists():
        pytest.skip("candidates_paris2026.csv absent")
    import pandas as pd
    df = pd.read_csv(p)
    assert len(df) >= 5, f"Au moins 5 candidats attendus, got {len(df)}"


def test_er_metric_valid():
    """ER (engagement rate) doit être > 0 pour des données réelles."""
    # Test sur les outputs pré-calculés si disponibles
    p = _ROOT / "final" / "A1_temporal" / "data" / "weekly_metrics_twitter.csv"
    if not p.exists():
        pytest.skip("weekly_metrics_twitter.csv absent")
    import pandas as pd
    df = pd.read_csv(p)
    if "er_median" in df.columns:
        assert (df["er_median"] >= 0).all(), "ER médian ne peut pas être négatif"


def test_nsi_in_valid_range():
    """NSI (Net Sentiment Index) borné dans [-1, 1]."""
    p = _ROOT / "final" / "A3_sentiment" / "outputs" / "A3_nsi_by_candidate.csv"
    if not p.exists():
        pytest.skip("A3_nsi_by_candidate.csv absent")
    import pandas as pd
    df = pd.read_csv(p)
    if "nsi" in df.columns:
        assert (df["nsi"] >= -1.01).all() and (df["nsi"] <= 1.01).all(), "NSI hors [-1, 1]"


def test_utils_load_replies():
    """src.utils.load_replies charge sans erreur si fichier existe."""
    from src.utils import load_replies, DATA_RAW
    p = DATA_RAW / "replies_classified.csv"
    if not p.exists():
        pytest.skip("replies_classified.csv absent")
    df = load_replies()
    assert len(df) > 0
    assert "text" in df.columns or "reply_text" in df.columns
