"""Tests for installed."""

from installed.main import main
def test_main_runs(capsys):
    """main() should execute without error."""
    main()
    captured = capsys.readouterr()
    assert "installed" in captured.out
