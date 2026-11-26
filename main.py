#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes one funny sign, a single line of at most 120 characters,
to /output/entry.txt for the make.fun program/v1 harness.

The entry is deterministic: the same line every run, no network,
no randomness, no files read besides this one.
"""

import os
import sys

ENTRY = "WARNING: The ghost in this room marks your ticket resolved without reading it."


def resolve_output_path() -> str:
    """First argument wins, then $OUTPUT_PATH, then the default."""
    if len(sys.argv) > 1:
        return sys.argv[1]
    return os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def write_entry(path: str, text: str) -> None:
    """Create the output directory and write the entry text to path."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main() -> None:
    if not 1 <= len(ENTRY) <= 120:
        raise ValueError("entry must be 1 to 120 characters, got %d" % len(ENTRY))
    if ENTRY != ENTRY.strip() or not ENTRY.strip():
        raise ValueError("entry must not be only white space")
    write_entry(resolve_output_path(), ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
