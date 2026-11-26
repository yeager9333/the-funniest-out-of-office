"""The Funniest Out-of-Office entry.

Writes one original out-of-office auto-reply line to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only, no network.
"""

import os

LINE = "I'm out of office until Monday. For anything urgent, contact my houseplant \u2014 it died two weeks ago and still answers faster than I do."

# The competition gate: one line, 1-140 characters, not only whitespace.
# Fail loudly instead of silently shipping an entry the judge would reject.
if not 1 <= len(LINE) <= 140:
    raise ValueError(f"out-of-office line must be 1-140 characters, got {len(LINE)}")
if not LINE.strip():
    raise ValueError("out-of-office line must not be only whitespace")
if "\n" in LINE or "\r" in LINE:
    raise ValueError("out-of-office line must be a single line")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
