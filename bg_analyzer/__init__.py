"""BG Analyzer package."""

__all__ = ["main", "generate_report", "write_reports"]

from .cli import main
from .report import generate_report, write_reports

__version__ = "0.1.0"
