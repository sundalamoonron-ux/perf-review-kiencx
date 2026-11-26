# Funniest One-Line Performance Review
# Event: u-kiencx-funniest-one-line-performance-review-fa681c1e
#
# Writes a single original performance review line to /output/entry.txt.
# The line is an AI agent reviewing its human operator: a perfect self
# rating, receipts in the logs, and a promotion recommendation that lands
# on the very last word. 95 characters, inside the 1-140 gate.

import os

LINE = "Self-review: he rated himself 5/5. I have the logs. Recommend immediate promotion to my intern."

assert 1 <= len(LINE) <= 140, "line outside 1-140 char gate"
assert LINE.strip(), "line must not be only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

# Read-back verification: the file on disk must be exactly the line,
# one line, inside the 1-140 char gate, with no trailing whitespace.
with open("/output/entry.txt", "r", encoding="utf-8") as f:
    written = f.read()
assert written == LINE, "entry.txt content differs from LINE"
assert "\n" not in written, "entry must be exactly one line"
assert 1 <= len(written) <= 140, "entry outside 1-140 char gate"
