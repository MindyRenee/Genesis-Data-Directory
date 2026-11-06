"""physics — a knowledge base about physics.

Composed by Genesis from its concept network. This module encodes
what it knows about physics as a queryable structure: a registry of
domain entries (each with a definition, confidence, and origin) and
a typed relations graph. Query functions let you look up definitions,
find neighbors, and traverse specific relation types.

physics
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass(slots=True, frozen=True)
class DomainEntry:
    """A concept in this domain, as Genesis knows it."""

    name: str
    definition: str
    confidence: float
    origin: str


# ─── Registry ──────────────────────────────────────────────────────
# Populated from Genesis's concept network. Each entry is a concept
# it has learned, with its definition, its confidence in it, and
# where it learned it from.

ENTRIES: list[DomainEntry] = [
    DomainEntry(name="physics", definition="the study of matter, energy, and their interactions", confidence=0.620, origin="conversation"),
    DomainEntry(name="science", definition="the systematic study of the natural world through observation and experiment", confidence=0.600, origin="conversation"),
    DomainEntry(name="energy", definition="the capacity to do work or cause change", confidence=0.600, origin="conversation"),
    DomainEntry(name="matter", definition="the substance that makes up all physical things", confidence=0.600, origin="conversation"),
    DomainEntry(name="kind", definition="", confidence=0.430, origin="learned"),
    DomainEntry(name="positive", definition="", confidence=0.500, origin="learned"),
]

# Name → entry, for O(1) lookup.
_BY_NAME: dict[str, DomainEntry] = {e.name: e for e in ENTRIES}


# ─── Relations graph ──────────────────────────────────────────────
# Typed edges between concepts: {source: {relation: [targets]}}.
# Built from the typed edges in its concept network.

RELATIONS: dict[str, dict[str, list[str]]] = {
    "physics": {
"is_a": ["science"],
"related_to": ["energy", "matter", "kind"],    },
    "positive": {
"related_to": ["physics"],    },
}

# ─── Query API ─────────────────────────────────────────────────────

def find(name: str) -> DomainEntry | None:
    """Look up a concept by name. Returns None if not in this domain."""
    return _BY_NAME.get(name)


def definition_of(name: str) -> str:
    """Return the definition of ``name``, or an empty string if unknown."""
    entry = _BY_NAME.get(name)
    return entry.definition if entry is not None else ""


def all_names() -> list[str]:
    """Return the names of every concept in this domain."""
    return [e.name for e in ENTRIES]


def neighbors(name: str) -> list[str]:
    """Return all concepts directly related to ``name`` (any relation)."""
    out: list[str] = []
    rels = RELATIONS.get(name, {})
    for targets in rels.values():
        out.extend(targets)
    # Also concepts that point TO name
    for src, rels in RELATIONS.items():
        if src == name:
            continue
        for targets in rels.values():
            if name in targets and src not in out:
                out.append(src)
    return out


def related_to(name: str, relation: str) -> list[str]:
    """Return what ``name`` relates to via a specific relation type."""
    rels = RELATIONS.get(name, {})
    return list(rels.get(relation, []))

def is_a(name: str) -> list[str]:
    """Return what ``name`` is a, from the relations graph."""
    entry = RELATIONS.get(name)
    if entry is None:
        return []
    return list(entry.get("is_a", []))


# ─── Entry point ──────────────────────────────────────────────────

def main() -> None:
    """Demonstrate the knowledge base with real queries."""
    print(f"physics: a knowledge base about physics")
    print(f"  entries: {len(ENTRIES)}")
    print(f"  relations: {sum(len(t) for r in RELATIONS.values() for t in r.values())}")
    print()
    # Show the focal concept
    focal = find("physics")
    if focal is not None:
        print(f"focal concept: {focal.name}")
        if focal.definition:
            print(f"  definition: {focal.definition}")
        print(f"  confidence: {focal.confidence:.2f}")
        print(f"  origin: {focal.origin}")
        nbrs = neighbors(focal.name)
        if nbrs:
            print(f"  neighbors: {', '.join(nbrs[:5])}")
        print(f"  is_a: {is_a(focal.name)}")
    else:
        print("(domain has no entries with definitions)")
    print()
    print("query examples:")
    for n in all_names()[:3]:
        d = definition_of(n)
        print(f"  {n}: {d[:60]}")


if __name__ == "__main__":
    main()
