"""Command-line interface for BG Analyzer."""

from __future__ import annotations

import pathlib
import sys

import click

from .ingest import load_csv


@click.command()
@click.option(
    "--glucose",
    type=click.Path(exists=True, path_type=pathlib.Path),
    help="CSV file with glucose data",
)
@click.option(
    "--insulin",
    type=click.Path(exists=True, path_type=pathlib.Path),
    help="CSV file with insulin data",
)
@click.option(
    "--carbs",
    type=click.Path(exists=True, path_type=pathlib.Path),
    help="CSV file with carb log",
)
def main(
    glucose: pathlib.Path | None,
    insulin: pathlib.Path | None,
    carbs: pathlib.Path | None,
) -> None:
    """Run analysis on provided CSV files.

    The parser currently validates the expected columns only.
    """

    click.echo("BG Analyzer skeleton")
    if glucose:
        load_csv(glucose, ["timestamp", "bg_mmol"])
        click.echo(f"Glucose file: {glucose}")
    if insulin:
        load_csv(insulin, ["timestamp", "bolus_units", "bolus_type"])
        click.echo(f"Insulin file: {insulin}")
    if carbs:
        load_csv(carbs, ["timestamp", "carbs_grams", "meal_label"])
        click.echo(f"Carb file: {carbs}")

    sys.exit(0)


if __name__ == "__main__":
    main()
