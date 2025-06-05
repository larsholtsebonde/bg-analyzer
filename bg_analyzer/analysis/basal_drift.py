from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List

import pandas as pd


@dataclass
class DriftEntry:
    """Overnight drift for a single day."""

    date: pd.Timestamp
    delta_mmol: float


def calculate_drift(
    glucose: pd.DataFrame,
    *,
    window: tuple[str, str] = ("00:00", "05:00"),
) -> List[DriftEntry]:
    """Calculate overnight BG drift for each day.

    Parameters
    ----------
    glucose:
        DataFrame with ``timestamp`` and ``bg_mmol`` columns.
    window:
        Tuple of start and end times to measure drift, defaulting to
        midnight to 5am.

    Returns
    -------
    List[DriftEntry]
        Drift entries for each day with data in the given window.
    """
    df = glucose.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)
    df = df.set_index("timestamp").sort_index()
    nightly = df.between_time(*window)["bg_mmol"].groupby(pd.Grouper(freq="D"))

    results: List[DriftEntry] = []
    for day, series in nightly:
        if series.empty:
            continue
        start = float(series.iloc[0])
        end = float(series.iloc[-1])
        results.append(DriftEntry(day.normalize(), end - start))
    return results


def classify_drift(
    entries: Iterable[DriftEntry],
    *,
    days: int = 3,
    threshold: float = 2.0,
) -> str:
    """Classify basal drift over the most recent ``days`` entries.

    Parameters
    ----------
    entries:
        Sequence of :class:`DriftEntry` objects.
    days:
        Number of latest days to consider for the trend.
    threshold:
        Minimum absolute mean delta to signal drift in mmol/L.

    Returns
    -------
    str
        ``"rising"``, ``"falling"`` or ``"stable"``.
    """
    recent = list(entries)[-days:]
    if len(recent) < days:
        return "insufficient-data"
    mean_delta = sum(e.delta_mmol for e in recent) / days
    if abs(mean_delta) < threshold:
        return "stable"
    return "rising" if mean_delta > 0 else "falling"
