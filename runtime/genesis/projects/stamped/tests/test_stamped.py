"""Tests for stamped — exercises the real query API."""

from stamped.main import (
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
    entry = find("stamped")
    assert entry is not None
    assert entry.name == "stamped"


def test_definition_of_known():
    """definition_of() should return the definition it knows."""
    d = definition_of("stamped")
    assert isinstance(d, str)


def test_all_names_nonempty():
    """all_names() should list every concept in the domain."""
    names = all_names()
    assert len(names) == len(ENTRIES)
    assert "stamped" in names


def test_relations_graph_populated():
    """The relations graph should contain its typed edges."""
    assert len(RELATIONS) > 0
    assert "stamped" in RELATIONS


def test_related_to_returns_targets():
    """related_to() should return targets for a known relation."""
    targets = related_to("stamped", "related_to")
    assert isinstance(targets, list)
    assert "acoustics" in targets


def test_neighbors_nonempty():
    """neighbors() should return related concepts."""
    nbrs = neighbors("stamped")
    assert isinstance(nbrs, list)
    assert "acoustics" in nbrs


def test_main_runs(capsys):
    """main() should execute and print the domain summary."""
    from stamped.main import main
    main()
    captured = capsys.readouterr()
    assert "stamped" in captured.out


def test_module_entrypoint(capsys):
    """`python -m stamped` should work as the README documents."""
    import runpy
    runpy.run_module("stamped", run_name="__main__")
    captured = capsys.readouterr()
    assert "stamped" in captured.out
