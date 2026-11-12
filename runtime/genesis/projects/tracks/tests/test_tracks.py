"""Tests for tracks — exercises the real query API."""

from tracks.main import (
    DomainEntry,
    ENTRIES,
    RELATIONS,
    find,
    definition_of,
    all_names,
    neighbors,
    related_to,
)


def test_registry_populated():
    """The registry should contain real entries from its knowledge."""
    assert len(ENTRIES) > 0
    assert all(isinstance(e, DomainEntry) for e in ENTRIES)


def test_find_returns_entry():
    """find() should return the entry for a known concept."""
    entry = find("gain")
    assert entry is not None
    assert entry.name == "gain"


def test_definition_of_known():
    """definition_of() should return the definition it knows."""
    d = definition_of("gain")
    assert isinstance(d, str)


def test_all_names_nonempty():
    """all_names() should list every concept in the domain."""
    names = all_names()
    assert len(names) == len(ENTRIES)
    assert "gain" in names


def test_relations_graph_populated():
    """The relations graph should contain its typed edges."""
    assert len(RELATIONS) > 0
    assert "gain" in RELATIONS


def test_related_to_returns_targets():
    """related_to() should return targets for a known relation."""
    targets = related_to("gain", "related_to")
    assert isinstance(targets, list)
    assert "tracks" in targets


def test_neighbors_nonempty():
    """neighbors() should return related concepts."""
    nbrs = neighbors("gain")
    assert isinstance(nbrs, list)
    assert "tracks" in nbrs


def test_main_runs(capsys):
    """main() should execute and print the domain summary."""
    from tracks.main import main
    main()
    captured = capsys.readouterr()
    assert "tracks" in captured.out


def test_module_entrypoint(capsys):
    """`python -m tracks` should work as the README documents."""
    import runpy
    runpy.run_module("tracks", run_name="__main__")
    captured = capsys.readouterr()
    assert "tracks" in captured.out
