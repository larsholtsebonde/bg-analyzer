from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Tuple

import json

from bg_analyzer.analysis import CleanEvent


@dataclass
class ReportStats:
    """Statistics about analysed events."""

    candidate_events: int
    events_sampled: int
    events_skipped: int


def generate_report(
    events: Iterable[CleanEvent], candidate_events: int
) -> Tuple[str, dict]:
    """Generate Markdown and JSON report content.

    Parameters
    ----------
    events:
        Clean events included in analysis.
    candidate_events:
        Total carb entries considered.

    Returns
    -------
    Tuple[str, dict]
        Markdown text and statistics dictionary.
    """
    events_list = list(events)
    stats = ReportStats(
        candidate_events=candidate_events,
        events_sampled=len(events_list),
        events_skipped=candidate_events - len(events_list),
    )

    md_lines = [
        "## Event Stats",
        f"- Candidate events: {stats.candidate_events}",
        f"- Events included in analysis: {stats.events_sampled}",
        f"- Events skipped: {stats.events_skipped}",
    ]
    md = "\n".join(md_lines) + "\n"
    return md, asdict(stats)


def write_reports(md: str, data: dict, directory: Path) -> None:
    """Write Markdown and JSON reports to ``directory``.

    Parameters
    ----------
    md:
        Markdown content.
    data:
        Statistics dictionary.
    directory:
        Target directory for the reports.
    """
    directory.mkdir(parents=True, exist_ok=True)
    (directory / "latest_report.md").write_text(md)
    (directory / "latest_report.json").write_text(
        json.dumps(data, indent=2, sort_keys=True)
    )

