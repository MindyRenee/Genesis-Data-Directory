"""Tests for major_form_class."""

from major_form_class.main import main
def test_main_runs(capsys):
    """main() should execute without error."""
    main()
    captured = capsys.readouterr()
    assert "major_form_class" in captured.out
