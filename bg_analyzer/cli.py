"""Command-line interface for BG Analyzer."""

from __future__ import annotations

import pathlib
import sys

import click


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

    This placeholder prints the file paths and exits. Actual
    analysis will be implemented later.
    """

    click.echo("BG Analyzer skeleton")
    if glucose:
        click.echo(f"Glucose file: {glucose}")
    if insulin:
        click.echo(f"Insulin file: {insulin}")
    if carbs:
        click.echo(f"Carb file: {carbs}")

    sys.exit(0)


if __name__ == "__main__":
    main()
