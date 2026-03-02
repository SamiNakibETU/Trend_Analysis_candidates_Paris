"""
Utilitaires de visualisation et chargement. Style Swiss, palette candidats.
Compatibilité avec les données (candidate = Gregoire dans les CSV).
Depuis publication/notebooks/, les chemins pointent vers ../../final/
"""
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

# Chemins : repo root = parent de src/
_REPO_ROOT = Path(__file__).resolve().parent.parent
_BASE = _REPO_ROOT
DATA_RAW = _BASE / "final" / "data"
A1_DATA = _BASE / "final" / "A1_temporal" / "data"
A1_OUT = _BASE / "final" / "A1_temporal" / "outputs"
A2_DATA = _BASE / "final" / "A2_topics" / "data"
A2_OUT = _BASE / "final" / "A2_topics" / "outputs"
A3_OUT = _BASE / "final" / "A3_sentiment" / "outputs"
A4_DATA = _BASE / "final" / "A4_community" / "data"
A4_OUT = _BASE / "final" / "A4_community" / "outputs"
A5_DATA = _BASE / "final" / "A5_interactions" / "data"
A5_OUT = _BASE / "final" / "A5_interactions" / "outputs"
A7_OUT = _BASE / "final" / "A7_synthese" / "outputs"
OUT = _BASE / "final" / "outputs"
# Données legacy (analysis_v3) - final/A1 n'a pas ces CSV
LEGACY_TEMPORAL = _BASE / "outputs" / "analysis_v3" / "temporal"
LEGACY_COMMUNITY = _BASE / "outputs" / "analysis_v3" / "community"
LEGACY_INTERACTIONS = _BASE / "outputs" / "analysis_v3" / "interactions"
LEGACY_SENTIMENT = _BASE / "outputs" / "analysis_v3" / "sentiment"
CROSS_MENTIONS = LEGACY_COMMUNITY / "cross_candidate_mentions.csv"
CROSSPLATFORM_CORR = LEGACY_TEMPORAL / "crossplatform_correlation.csv"
FIG_DIR = _REPO_ROOT / "figures"
# Fine-tuning BERT
A6_DATA = _BASE / "final" / "A6_bert_finetuning" / "data"
A6_OUT = _BASE / "final" / "A6_bert_finetuning" / "outputs"
ANNOTATIONS_LEGACY = _BASE / "outputs" / "analysis_v3" / "annotation"
BERT_ANNOTATIONS = _REPO_ROOT / "data" / "bert_annotations_4class.csv"
BERT_ANNOTATIONS_MULTILABEL = _REPO_ROOT / "data" / "bert_annotations_multilabel.csv"
MODEL_DIR = _REPO_ROOT / "models" / "sentiment_camembert"


def load_replies(path=None):
    """Charge replies_classified.csv avec parsing robuste des timestamps (vectorisé)."""
    p = path or (DATA_RAW / "replies_classified.csv")
    df = pd.read_csv(p)

    ts = df["timestamp"].astype(str).str.replace("·", " ")
    ts = ts.replace(["nan", "", "None"], pd.NA)
    df["ts_parsed"] = pd.to_datetime(ts, errors="coerce")

    mask_fail = df["ts_parsed"].isna() & ts.notna()
    if mask_fail.any():
        try:
            from dateutil import parser as dateutil_parser

            def _parse_one(s):
                try:
                    return pd.Timestamp(dateutil_parser.parse(s))
                except Exception:
                    return pd.NaT

            df.loc[mask_fail, "ts_parsed"] = ts.loc[mask_fail].apply(_parse_one)
        except ImportError:
            pass

    df["ts_parsed"] = pd.to_datetime(df["ts_parsed"], errors="coerce")
    if "year_week" not in df.columns and df["ts_parsed"].notna().any():
        cal = df["ts_parsed"].dt.isocalendar()
        df["year_week"] = (
            cal["year"].astype(str) + "-W" + cal["week"].astype(str).str.zfill(2)
        )
    return df


def _safe_read(path, default=None):
    if Path(path).exists():
        return pd.read_csv(path)
    return default


# Palette candidats (Swiss style)
COLORS = {
    "Brossat": "#E63946",
    "Chikirou": "#C1121F",
    "Belliard": "#2D6A4F",
    "Grégoire": "#E07A5F",
    "Gregoire": "#E07A5F",  # alias données CSV
    "Bournazel": "#F4A261",
    "Dati": "#264653",
    "Knafo": "#6D4C41",
    "Mariani": "#1D3557",
}

# Camps idéologiques
CAMPS = {
    "Extrême gauche": ["Brossat", "Chikirou"],
    "Gauche": ["Belliard", "Grégoire"],
    "Centre": ["Bournazel"],
    "Droite": ["Dati"],
    "Extrême droite": ["Knafo", "Mariani"],
}

# Position idéologique (1 = extrême gauche, 8 = extrême droite)
POSITIONS = {
    "Brossat": 1,
    "Chikirou": 2,
    "Belliard": 3,
    "Grégoire": 4,
    "Gregoire": 4,
    "Bournazel": 5,
    "Dati": 6,
    "Knafo": 7,
    "Mariani": 8,
}

# Mapping candidate_id -> nom court (pour lookup couleur)
ID_TO_KEY = {
    "ian_brossat": "Brossat",
    "sophia_chikirou": "Chikirou",
    "david_belliard": "Belliard",
    "emmanuel_gregoire": "Grégoire",
    "pierre_yves_bournazel": "Bournazel",
    "rachida_dati": "Dati",
    "sarah_knafo": "Knafo",
    "thierry_mariani": "Mariani",
}

# Alias pour compatibilité
PALETTE = COLORS

# Ordre pour figures (ER décroissant)
KEYS_ER = [
    "Knafo",
    "Brossat",
    "Chikirou",
    "Mariani",
    "Bournazel",
    "Grégoire",
    "Belliard",
    "Dati",
]


def get_color(candidate: str) -> str:
    """Retourne la couleur d'un candidat (gère Gregoire/Grégoire)."""
    return COLORS.get(candidate, "#888888")


def swiss_style(ax, title: str, subtitle: str | None = None, source: str | None = None) -> None:
    """
    Applique le style Swiss aux axes.
    Fond blanc, grille y subtile, spines gauche+bas seulement.
    Titre 14pt bold aligné gauche, sous-titre gris #666 10pt, source #999 8pt bas droite.
    """
    ax.set_facecolor("#FFFFFF")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, alpha=0.3, axis="y", color="#E0E0E0")
    ax.set_title(title, fontsize=14, fontweight="bold", loc="left")
    if subtitle:
        ax.text(
            0.02,
            0.98,
            subtitle,
            transform=ax.transAxes,
            fontsize=10,
            color="#666666",
            va="top",
            ha="left",
        )
    if source:
        ax.text(
            1,
            -0.08,
            source,
            transform=ax.transAxes,
            fontsize=8,
            color="#999999",
            va="top",
            ha="right",
        )


def setup_mpl() -> None:
    """
    Configure matplotlib : fond blanc, Helvetica/Arial, DPI 300, bbox tight.
    """
    plt.rcParams.update(
        {
            "figure.facecolor": "#FFFFFF",
            "axes.facecolor": "#FFFFFF",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "font.family": ["DejaVu Sans", "Arial", "sans-serif"],
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
        }
    )
