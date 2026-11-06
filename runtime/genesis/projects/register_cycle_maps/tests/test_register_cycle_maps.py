"""Tests for register_cycle_maps."""

from register_cycle_maps.main import main
def test_main_runs(capsys):
    """main() should execute without error."""
    main()
    captured = capsys.readouterr()
    assert "register_cycle_maps" in captured.out
