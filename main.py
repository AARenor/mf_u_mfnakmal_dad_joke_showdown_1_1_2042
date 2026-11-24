#!/usr/bin/env python3
"""Write one short dad joke for make.fun bounty u-mfnakmal-dad-joke-showdown-1d2ce3e5."""

import os
import sys
from pathlib import Path

TEXT = (
    "My dad sent his steak back twice. When it finally came he clapped for it. "
    "The waiter said, 'Sir, that's not how well done works.'"
)

assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"


def output_dir() -> Path:
    """Folder named by MAKEFUN_OUTPUT_DIR, else OUTPUT_DIR, else /output."""
    return Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )


def main() -> int:
    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
