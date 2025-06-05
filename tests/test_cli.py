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
