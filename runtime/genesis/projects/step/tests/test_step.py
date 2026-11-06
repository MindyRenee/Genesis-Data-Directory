"""Tests for step."""

from step.main import main
def test_main_runs(capsys):
    """main() should execute without error."""
    main()
    captured = capsys.readouterr()
    assert "step" in captured.out
