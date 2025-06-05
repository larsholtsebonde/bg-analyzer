import pandas as pd

from bg_analyzer.analysis import CleanEvent
from bg_analyzer.report import generate_report


def test_generate_report_counts(tmp_path):
    events = [
        CleanEvent(
            timestamp=pd.Timestamp("2024-01-01T08:00:00Z"),
            carbs_grams=20.0,
            bolus_units=2.0,
            pre_bg_mmol=5.6,
            post_bg_mmol=7.0,
        )
    ]
    md, data = generate_report(events, candidate_events=3)
    assert "Candidate events: 3" in md
    assert "Events included in analysis: 1" in md
    assert "Events skipped: 2" in md
    assert data == {
        "candidate_events": 3,
        "events_sampled": 1,
        "events_skipped": 2,
    }

