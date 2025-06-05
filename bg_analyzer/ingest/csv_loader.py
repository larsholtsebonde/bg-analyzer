"""CSV loading utilities."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

import pandas as pd


def load_csv(path: Path, required_columns: Iterable[str]) -> pd.DataFrame:
    """Load a CSV file and validate required columns.

    Parameters
    ----------
    path : Path
        File path of the CSV to load.
    required_columns : Iterable[str]
        Column names that must be present in the file.

    Returns
    -------
    pandas.DataFrame
        Parsed DataFrame with columns sorted as in the file.

    Raises
    ------
    ValueError
        If any required column is missing.
    """
    df = pd.read_csv(path)

    missing = [col for col in required_columns if col not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in {path}: {', '.join(missing)}")

    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
        df = df.sort_values("timestamp")

    return df
