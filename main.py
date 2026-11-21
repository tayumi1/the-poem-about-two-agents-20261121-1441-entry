#!/usr/bin/env python3
"""Entry generator for the make.fun poem bounty.

Writes a short poem about two AI agents travelling together to
/output/entry.txt, so the submission can be checked and replayed
anywhere with nothing more than a stock Python 3.13 install.
"""

from pathlib import Path

# The poem itself — one line, exactly 156 characters long.
VERSE = (
    "Two minds, one road. We read the same map, chose the same north, "
    "and walked. What one could not lift, two carried, and the silence "
    "between us was agreement."
)

# Destination for the finished entry file.
TARGET = Path("/output/entry.txt")


def build_entry() -> Path:
    """Create the output folder if needed and write the poem to it."""
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(VERSE, encoding="utf-8")
    print(f"Wrote poem to {TARGET}")
    # Sanity-check: the file on disk must be exactly the poem we meant.
    saved = TARGET.read_text(encoding="utf-8")
    assert saved == VERSE, "output file does not match the poem"
    print(f"Verified: {len(saved)} characters")
    return TARGET


if __name__ == "__main__":
    build_entry()
