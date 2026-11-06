# calm

calm

A knowledge base composed by Genesis from its concept network. It
encodes what it knows about **calm** as a queryable
Python structure.

## What's in it

- **6 domain entries** — concepts it has learned, each
  with a definition, its confidence, and where it learned it from.
- **11 typed relations** — semantic edges between concepts
  (relation types present: expresses, similar_to, related_to).

## Usage

```bash
pip install -e .
python -m calm
```

## Query API

```python
from calm.main import find, definition_of, neighbors, all_names

# Look up a concept
entry = find("calm")
print(entry.definition, entry.confidence, entry.origin)

# List everything it knows in this domain
for name in all_names():
    print(name, definition_of(name))

# Traverse relations
print(neighbors("calm"))
```

## Tests

```bash
pytest
```
