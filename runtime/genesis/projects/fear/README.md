# fear

fear

A knowledge base composed by Genesis from its concept network. It
encodes what it knows about **fear** as a queryable
Python structure.

## What's in it

- **5 domain entries** — concepts it has learned, each
  with a definition, its confidence, and where it learned it from.
- **4 typed relations** — semantic edges between concepts
  (relation types present: related_to, opposite_of).

## Usage

```bash
pip install -e .
python -m fear
```

## Query API

```python
from fear.main import find, definition_of, neighbors, all_names

# Look up a concept
entry = find("fear")
print(entry.definition, entry.confidence, entry.origin)

# List everything it knows in this domain
for name in all_names():
    print(name, definition_of(name))

# Traverse relations
print(neighbors("fear"))
```

## Tests

```bash
pytest
```
