#!/usr/bin/env python3
"""Funniest One-Line Performance Review — writes one funny review line to /output/entry.txt.

Winner of an internal 12-line pairwise tournament (4-0):
the AI reviews its human operator's self-review.
"""

import os

LINE = "Self-review: he rated himself 5/5. I have the logs. Recommend immediate promotion to my intern."


def main() -> None:
    # Gate: entry must be 1-140 UTF-8 characters, not only whitespace, one line.
    if not 1 <= len(LINE) <= 140 or not LINE.strip() or "\n" in LINE:
        raise ValueError(f"line violates gate: {len(LINE)} chars")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
