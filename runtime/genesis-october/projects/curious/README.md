# curious

curious

A knowledge base composed by Genesis from its concept network. It
encodes what it knows about **curious** as a queryable
Python structure.

## What's in it

- **2 domain entries** — concepts it has learned, each
  with a definition, its confidence, and where it learned it from.
- **1 typed relations** — semantic edges between concepts
  (relation types present: related_to).

## Usage

```bash
pip install -e .
python -m curious
```

## Query API

```python
from curious.main import find, definition_of, neighbors, all_names

# Look up a concept
entry = find("curious")
print(entry.definition, entry.confidence, entry.origin)

# List everything it knows in this domain
for name in all_names():
    print(name, definition_of(name))

# Traverse relations
print(neighbors("curious"))
```

## Tests

```bash
pytest
```
