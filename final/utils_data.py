"""
Utilitaires de chargement des données — tweets, replies, métriques.
"""
import pandas as pd
from pathlib import Path

# Import config_paths — notebook exécuté depuis final/ ou racine
try:
    from config_paths import DATA_RAW, A1_DATA, A1_OUT, A2_DATA, A3_OUT, A4_DATA, A5_DATA
except ImportError:
    _base = Path(__file__).resolve().parent
    DATA_RAW = _base / "data"
    A1_DATA = _base / "A1_temporal" / "data"
    A1_OUT = _base / "A1_temporal" / "outputs"
    A2_DATA = _base / "A2_topics" / "data"
    A3_OUT = _base / "A3_sentiment" / "outputs"
    A4_DATA = _base / "A4_community" / "data"
    A5_DATA = _base / "A5_interactions" / "data"


def load_tweets(path=None):
    """Charge tweets_twitter.csv."""
    p = path or (DATA_RAW / "tweets_twitter.csv")
    df = pd.read_csv(p)
    df["ts_parsed"] = pd.to_datetime(df["timestamp"], errors="coerce")
    return df


def load_posts_ig(path=None):
    """Charge posts_instagram.csv."""
    p = path or (DATA_RAW / "posts_instagram.csv")
    df = pd.read_csv(p)
    df["ts_parsed"] = pd.to_datetime(df["timestamp"], errors="coerce")
    return df


def load_replies(path=None):
    """Charge replies_classified.csv + parse timestamps."""
    p = path or (DATA_RAW / "replies_classified.csv")
    df = pd.read_csv(p)

    def parse_reply_ts(s):
        if pd.isna(s) or str(s).strip() == "":
            return pd.NaT
        s = str(s).replace("·", " ")
        try:
            return pd.to_datetime(s)
        except (ValueError, TypeError):
            try:
                from dateutil import parser as dateutil_parser
                return pd.Timestamp(dateutil_parser.parse(s))
            except Exception:
                return pd.NaT

    df["ts_parsed"] = df["timestamp"].apply(parse_reply_ts)
    if "year_week" not in df.columns and df["ts_parsed"].notna().any():
        df["year_week"] = (
            df["ts_parsed"].dt.isocalendar().year.astype(str)
            + "-W"
            + df["ts_parsed"].dt.isocalendar().week.astype(str).str.zfill(2)
        )
    return df


def load_er_summary(path=None):
    """Charge A1_er_summary.csv."""
    p = path or (A1_OUT / "A1_er_summary.csv")
    if not Path(p).exists():
        return None
    return pd.read_csv(p)


def _safe_read(path, default=None):
    if Path(path).exists():
        return pd.read_csv(path)
    return default


def load_a1_data():
    """Charge les outputs A1 (weekly, anomalies, momentum, crossplat)."""
    return {
        "weekly_tw": _safe_read(A1_DATA / "weekly_metrics_twitter.csv"),
        "weekly_ig": _safe_read(A1_DATA / "weekly_metrics_instagram.csv"),
        "anomalies": _safe_read(A1_DATA / "anomalies_detected.csv"),
        "momentum": _safe_read(A1_DATA / "momentum_scores.csv"),
        "crossplat": _safe_read(A1_DATA / "crossplatform_correlation.csv"),
    }


def load_a2_data():
    """Charge topic_distribution."""
    return _safe_read(A2_DATA / "topic_distribution.csv")


def load_a3_data():
    """Charge A3_nsi_by_candidate."""
    return _safe_read(A3_OUT / "A3_nsi_by_candidate.csv")


def load_a4_data():
    """Charge echo_chamber, jaccard, community."""
    jaccard = _safe_read(A4_DATA / "A4_jaccard_pairs.csv")
    if jaccard is None:
        jaccard = _safe_read(A4_DATA / "audience_overlap_matrix.csv")
    return {
        "echo": _safe_read(A4_DATA / "echo_chamber_scores.csv"),
        "jaccard": jaccard,
        "community": _safe_read(A4_DATA / "community_membership.csv"),
    }


def load_a5_data():
    """Charge interaction_matrix, engagement, cross_text."""
    return {
        "inter_matrix": _safe_read(A5_DATA / "interaction_matrix.csv"),
        "inter_eng": _safe_read(A5_DATA / "interaction_engagement.csv"),
        "inter_cross": _safe_read(A5_DATA / "interaction_cross_text.csv"),
    }
