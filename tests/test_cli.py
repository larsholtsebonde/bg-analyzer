import subprocess


def test_cli_help():
    result = subprocess.run(
        [
            "python",
            "-m",
            "bg_analyzer",
            "--help",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "BG Analyzer skeleton" not in result.stdout


def test_cli_with_files(tmp_path):
    g = tmp_path / "glucose.csv"
    g.write_text("timestamp,bg_mmol\n2024-01-01T00:00Z,6.0\n")
    i = tmp_path / "insulin.csv"
    # fmt: off
    i.write_text(
        "timestamp,bolus_units,bolus_type\n"
        "2024-01-01T00:00Z,1.0,meal\n"
    )
    c = tmp_path / "carbs.csv"
    c.write_text(
        "timestamp,carbs_grams,meal_label\n"
        "2024-01-01T00:00Z,10,Breakfast\n"
    )
    # fmt: on

    result = subprocess.run(
        [
            "python",
            "-m",
            "bg_analyzer",
            "--glucose",
            str(g),
            "--insulin",
            str(i),
            "--carbs",
            str(c),
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert f"Glucose file: {g}" in result.stdout
    assert f"Insulin file: {i}" in result.stdout
    assert f"Carb file: {c}" in result.stdout
