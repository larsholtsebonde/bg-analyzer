from pathlib import Path

import pandas as pd
import pytest

from bg_analyzer.ingest import load_csv

SAMPLES = Path(__file__).resolve().parent.parent / "samples"


def test_load_csv_success():
    df = load_csv(SAMPLES / "glucose.csv", ["timestamp", "bg_mmol"])
    assert not df.empty
    assert list(df.columns) == ["timestamp", "bg_mmol"]
    assert pd.api.types.is_datetime64_any_dtype(df["timestamp"])


def test_load_csv_missing_column(tmp_path: Path):
    file = tmp_path / "bad.csv"
    file.write_text("timestamp\n2024-01-01T00:00:00")
    with pytest.raises(ValueError):
        load_csv(file, ["timestamp", "bg_mmol"])
