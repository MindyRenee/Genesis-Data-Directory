"""Tests for ensure."""

from ensure.main import main
def test_main_runs(capsys):
    """main() should execute without error."""
    main()
    captured = capsys.readouterr()
    assert "ensure" in captured.out
