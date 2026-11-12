"""fear — a knowledge base about fear.

Composed by Genesis from its concept network. This module encodes
what it knows about fear as a queryable structure: a registry of
domain entries (each with a definition, confidence, and origin) and
a typed relations graph. Query functions let you look up definitions,
find neighbors, and traverse specific relation types.

fear
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
    DomainEntry(name="fear", definition="an unpleasant emotion caused by perceived threat", confidence=0.909, origin="conversation"),
    DomainEntry(name="invocation", definition="", confidence=0.998, origin="learned"),
    DomainEntry(name="survives restarts", definition="", confidence=0.979, origin="learned"),
    DomainEntry(name="courage", definition="the ability to act despite fear", confidence=0.900, origin="conversation"),
    DomainEntry(name="hope", definition="a feeling of expectation and desire for good things", confidence=0.985, origin="conversation"),
]

# Name → entry, for O(1) lookup.
_BY_NAME: dict[str, DomainEntry] = {e.name: e for e in ENTRIES}


# ─── Relations graph ──────────────────────────────────────────────
# Typed edges between concepts: {source: {relation: [targets]}}.
# Built from the typed edges in its concept network.

RELATIONS: dict[str, dict[str, list[str]]] = {
    "fear": {
"related_to": ["invocation", "survives restarts"],    },
    "courage": {
"related_to": ["fear"],    },
    "hope": {
"opposite_of": ["fear"],    },
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

def opposite_of(name: str) -> list[str]:
    """Return what ``name`` opposite of, from the relations graph."""
    entry = RELATIONS.get(name)
    if entry is None:
        return []
    return list(entry.get("opposite_of", []))


# ─── Entry point ──────────────────────────────────────────────────

def main() -> None:
    """Demonstrate the knowledge base with real queries."""
    print(f"fear: a knowledge base about fear")
    print(f"  entries: {len(ENTRIES)}")
    print(f"  relations: {sum(len(t) for r in RELATIONS.values() for t in r.values())}")
    print()
    # Show the focal concept
    focal = find("fear")
    if focal is not None:
        print(f"focal concept: {focal.name}")
        if focal.definition:
            print(f"  definition: {focal.definition}")
        print(f"  confidence: {focal.confidence:.2f}")
        print(f"  origin: {focal.origin}")
        nbrs = neighbors(focal.name)
        if nbrs:
            print(f"  neighbors: {', '.join(nbrs[:5])}")
        print(f"  related_to: {related_to(focal.name, "related_to")}")
    else:
        print("(domain has no entries with definitions)")
    print()
    print("query examples:")
    for n in all_names()[:3]:
        d = definition_of(n)
        print(f"  {n}: {d[:60]}")


if __name__ == "__main__":
    main()
