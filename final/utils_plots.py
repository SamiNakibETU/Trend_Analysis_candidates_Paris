"""
Utilitaires de visualisation — style Swiss, palette candidats.
"""
import matplotlib.pyplot as plt

# Palette candidats (Swiss style)
PALETTE = {
    "Brossat": "#E63946",
    "Chikirou": "#C1121F",
    "Belliard": "#2D6A4F",
    "Gregoire": "#E07A5F",
    "Bournazel": "#F4A261",
    "Dati": "#264653",
    "Knafo": "#6D4C41",
    "Mariani": "#1D3557",
}

# Mapping candidate_id -> key court
ID_TO_KEY = {
    "ian_brossat": "Brossat",
    "sophia_chikirou": "Chikirou",
    "david_belliard": "Belliard",
    "emmanuel_gregoire": "Gregoire",
    "pierre_yves_bournazel": "Bournazel",
    "rachida_dati": "Dati",
    "sarah_knafo": "Knafo",
    "thierry_mariani": "Mariani",
}

# Ordre pour figures (ER décroissant)
KEYS_ER = [
    "Knafo",
    "Brossat",
    "Chikirou",
    "Mariani",
    "Bournazel",
    "Gregoire",
    "Belliard",
    "Dati",
]

# Camps idéologiques (plan_finalisation)
CAMPS = {
    "Extrême gauche": ["Brossat", "Chikirou"],
    "Gauche": ["Belliard", "Gregoire"],
    "Centre": ["Bournazel"],
    "Droite": ["Dati"],
    "Extrême droite": ["Knafo", "Mariani"],
}

# Position idéologique (1 = extrême gauche, 8 = extrême droite)
POSITIONS = {
    "Brossat": 1,
    "Chikirou": 2,
    "Belliard": 3,
    "Gregoire": 4,
    "Bournazel": 5,
    "Dati": 6,
    "Knafo": 7,
    "Mariani": 8,
}

# Alias pour compatibilité plan
COLORS = PALETTE


def swiss_style(ax, title, subtitle=None, source=None):
    """Applique le style Swiss aux axes."""
    ax.set_facecolor("#FFFFFF")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, alpha=0.3, color="#E0E0E0")
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


def load_palette():
    """Retourne (PALETTE, ID_TO_KEY, KEYS_ER)."""
    return PALETTE, ID_TO_KEY, KEYS_ER


def setup_mpl():
    """Configure matplotlib (Swiss, DejaVu Sans)."""
    plt.rcParams.update(
        {
            "figure.facecolor": "#FFFFFF",
            "axes.facecolor": "#FFFFFF",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "font.family": ["DejaVu Sans", "sans-serif"],
            "savefig.dpi": 300,
            "savefig.bbox": "tight",
        }
    )
