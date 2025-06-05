import pandas as pd

from bg_analyzer.analysis import calculate_drift, classify_drift


def _make_data(deltas):
    times = []
    values = []
    base = pd.Timestamp("2024-01-01T00:00Z")
    for i, delta in enumerate(deltas):
        start = base + pd.Timedelta(days=i)
        end = start + pd.Timedelta(hours=5)
        times.extend([start, end])
        values.extend([6.0, 6.0 + delta])
    return pd.DataFrame({"timestamp": times, "bg_mmol": values})


def test_classify_drift_stable():
    df = _make_data([0.8, 0.5, 1.0])
    entries = calculate_drift(df)
    assert classify_drift(entries) == "stable"


def test_classify_drift_rising():
    df = _make_data([3.0, 2.5, 3.5])
    entries = calculate_drift(df)
    assert classify_drift(entries) == "rising"


def test_classify_drift_falling():
    df = _make_data([-2.5, -3.0, -2.0])
    entries = calculate_drift(df)
    assert classify_drift(entries) == "falling"
