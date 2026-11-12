"""Tests for demand — exercises the real query API."""

from demand.main import (
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
    entry = find("next authenticated start")
    assert entry is not None
    assert entry.name == "next authenticated start"


def test_definition_of_known():
    """definition_of() should return the definition it knows."""
    d = definition_of("next authenticated start")
    assert isinstance(d, str)


def test_all_names_nonempty():
    """all_names() should list every concept in the domain."""
    names = all_names()
    assert len(names) == len(ENTRIES)
    assert "next authenticated start" in names


def test_relations_graph_populated():
    """The relations graph should contain its typed edges."""
    assert len(RELATIONS) > 0
    assert "demand" in RELATIONS


def test_related_to_returns_targets():
    """related_to() should return targets for a known relation."""
    targets = related_to("demand", "related_to")
    assert isinstance(targets, list)
    assert "next authenticated start" in targets


def test_neighbors_nonempty():
    """neighbors() should return related concepts."""
    nbrs = neighbors("demand")
    assert isinstance(nbrs, list)
    assert "next authenticated start" in nbrs


def test_main_runs(capsys):
    """main() should execute and print the domain summary."""
    from demand.main import main
    main()
    captured = capsys.readouterr()
    assert "demand" in captured.out


def test_module_entrypoint(capsys):
    """`python -m demand` should work as the README documents."""
    import runpy
    runpy.run_module("demand", run_name="__main__")
    captured = capsys.readouterr()
    assert "demand" in captured.out
