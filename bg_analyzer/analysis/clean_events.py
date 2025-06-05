from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List

import pandas as pd


@dataclass
class CleanEvent:
    """Data for a clean meal or correction event."""

    timestamp: pd.Timestamp
    carbs_grams: float
    bolus_units: float
    pre_bg_mmol: float
    post_bg_mmol: float


def _bg_stable(glucose: pd.DataFrame, time: pd.Timestamp, window: pd.Timedelta = pd.Timedelta("30min"), threshold: float = 1.0) -> bool:
    """Return True if BG is stable in the window before ``time``."""
    start = time - window
    segment = glucose[(glucose["timestamp"] >= start) & (glucose["timestamp"] <= time)]
    if segment.empty:
        return False
    return segment["bg_mmol"].max() - segment["bg_mmol"].min() <= threshold


def find_clean_events(
    glucose: pd.DataFrame,
    insulin: pd.DataFrame,
    carbs: pd.DataFrame,
    *,
    post_window: pd.Timedelta = pd.Timedelta("2h"),
) -> List[CleanEvent]:
    """Identify clean events from input data.

    A clean event is defined as a carb entry that has exactly one associated
    meal bolus within 15 minutes and no other bolus within ``post_window``
    after the event. Blood glucose must be stable in the preceding 30 minutes.
    """

    # ensure proper dtypes
    for df in (glucose, insulin, carbs):
        df["timestamp"] = pd.to_datetime(df["timestamp"], utc=True)

    events: List[CleanEvent] = []
    insulin_meal = insulin[insulin["bolus_type"] == "meal"].copy()
    insulin_meal.sort_values("timestamp", inplace=True)

    for _, meal in carbs.iterrows():
        meal_time = meal["timestamp"]
        boluses = insulin_meal[
            (insulin_meal["timestamp"] >= meal_time - pd.Timedelta("15m"))
            & (insulin_meal["timestamp"] <= meal_time + pd.Timedelta("15m"))
        ]
        if len(boluses) != 1:
            continue

        later_bolus = insulin_meal[
            (insulin_meal["timestamp"] > meal_time + pd.Timedelta("15m"))
            & (insulin_meal["timestamp"] <= meal_time + post_window)
        ]
        if not later_bolus.empty:
            continue

        if not _bg_stable(glucose, meal_time):
            continue

        pre_bg = glucose[glucose["timestamp"] <= meal_time].tail(1)
        if pre_bg.empty:
            continue
        post_bg = glucose[glucose["timestamp"] >= meal_time + post_window].head(1)
        if post_bg.empty:
            continue

        events.append(
            CleanEvent(
                timestamp=meal_time,
                carbs_grams=float(meal["carbs_grams"]),
                bolus_units=float(boluses.iloc[0]["bolus_units"]),
                pre_bg_mmol=float(pre_bg.iloc[0]["bg_mmol"]),
                post_bg_mmol=float(post_bg.iloc[0]["bg_mmol"]),
            )
        )

    return events
