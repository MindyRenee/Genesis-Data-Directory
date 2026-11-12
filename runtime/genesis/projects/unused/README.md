# unused

unused

A knowledge base composed by Genesis from its concept network. It
encodes what it knows about **unused** as a queryable
Python structure.

## What's in it

- **3 domain entries** — concepts it has learned, each
  with a definition, its confidence, and where it learned it from.
- **4 typed relations** — semantic edges between concepts
  (relation types present: is_a, related_to).

## Usage

```bash
pip install -e .
python -m unused
```

## Query API

```python
from unused.main import find, definition_of, neighbors, all_names

# Look up a concept
entry = find("unused")
print(entry.definition, entry.confidence, entry.origin)

# List everything it knows in this domain
for name in all_names():
    print(name, definition_of(name))

# Traverse relations
print(neighbors("unused"))
```

## Tests

```bash
pytest
```
