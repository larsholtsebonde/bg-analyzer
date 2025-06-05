import pandas as pd

from bg_analyzer.analysis import find_clean_events


def test_find_clean_events_simple():
    glucose = pd.DataFrame(
        {
            "timestamp": [
                "2024-01-01T07:55:00Z",
                "2024-01-01T08:00:00Z",
                "2024-01-01T10:00:00Z",
            ],
            "bg_mmol": [5.5, 5.6, 7.0],
        }
    )
    insulin = pd.DataFrame(
        {
            "timestamp": ["2024-01-01T08:00:00Z"],
            "bolus_units": [2.0],
            "bolus_type": ["meal"],
        }
    )
    carbs = pd.DataFrame(
        {
            "timestamp": ["2024-01-01T08:00:00Z"],
            "carbs_grams": [20],
            "meal_label": ["Breakfast"],
        }
    )

    events = find_clean_events(glucose, insulin, carbs)
    assert len(events) == 1
    evt = events[0]
    assert evt.carbs_grams == 20
    assert evt.bolus_units == 2.0
    assert evt.pre_bg_mmol == 5.6
    assert evt.post_bg_mmol == 7.0


def test_find_clean_events_multiple_bolus():
    glucose = pd.DataFrame(
        {
            "timestamp": ["2024-01-01T08:00:00Z", "2024-01-01T10:00:00Z"],
            "bg_mmol": [5.6, 7.0],
        }
    )
    insulin = pd.DataFrame(
        {
            "timestamp": ["2024-01-01T07:55:00Z", "2024-01-01T08:05:00Z"],
            "bolus_units": [1.0, 1.0],
            "bolus_type": ["meal", "meal"],
        }
    )
    carbs = pd.DataFrame(
        {
            "timestamp": ["2024-01-01T08:00:00Z"],
            "carbs_grams": [20],
            "meal_label": ["Breakfast"],
        }
    )

    events = find_clean_events(glucose, insulin, carbs)
    assert events == []


def test_find_clean_events_later_bolus():
    glucose = pd.DataFrame(
        {
            "timestamp": ["2024-01-01T08:00:00Z", "2024-01-01T10:00:00Z"],
            "bg_mmol": [5.6, 7.0],
        }
    )
    insulin = pd.DataFrame(
        {
            "timestamp": ["2024-01-01T08:00:00Z", "2024-01-01T08:30:00Z"],
            "bolus_units": [2.0, 1.0],
            "bolus_type": ["meal", "meal"],
        }
    )
    carbs = pd.DataFrame(
        {
            "timestamp": ["2024-01-01T08:00:00Z"],
            "carbs_grams": [20],
            "meal_label": ["Breakfast"],
        }
    )

    events = find_clean_events(glucose, insulin, carbs)
    assert events == []


def test_find_clean_events_unstable_bg():
    glucose = pd.DataFrame(
        {
            "timestamp": [
                "2024-01-01T07:40:00Z",
                "2024-01-01T07:55:00Z",
                "2024-01-01T08:00:00Z",
                "2024-01-01T10:00:00Z",
            ],
            "bg_mmol": [5.0, 7.0, 7.2, 9.0],
        }
    )
    insulin = pd.DataFrame(
        {
            "timestamp": ["2024-01-01T08:00:00Z"],
            "bolus_units": [2.0],
            "bolus_type": ["meal"],
        }
    )
    carbs = pd.DataFrame(
        {
            "timestamp": ["2024-01-01T08:00:00Z"],
            "carbs_grams": [20],
            "meal_label": ["Breakfast"],
        }
    )

    events = find_clean_events(glucose, insulin, carbs)
    assert events == []


def test_find_clean_events_needs_post_bg():
    glucose = pd.DataFrame(
        {
            "timestamp": ["2024-01-01T07:55:00Z", "2024-01-01T08:00:00Z"],
            "bg_mmol": [5.5, 5.6],
        }
    )
    insulin = pd.DataFrame(
        {
            "timestamp": ["2024-01-01T08:00:00Z"],
            "bolus_units": [2.0],
            "bolus_type": ["meal"],
        }
    )
    carbs = pd.DataFrame(
        {
            "timestamp": ["2024-01-01T08:00:00Z"],
            "carbs_grams": [20],
            "meal_label": ["Breakfast"],
        }
    )

    events = find_clean_events(glucose, insulin, carbs)
    assert events == []
