#!/usr/bin/env python3
"""Last Text at One Percent — a dying phone's final text at 1% battery.

Writes one original line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR,
falling back to $OUTPUT_DIR for local testing). Python 3 standard library
only. The sealed scorer accepts 1 to 200 characters, not only whitespace;
this line is 113 characters. The joke is the phone spending its last
percent on a goodbye text instead of the alarm it was supposed to ring.
"""

import os

LINE = "1% left and I'm spending it texting you instead of ringing your alarm. Sweet dreams \u2014 I'll be a brick by morning."

# Gate: 1 to 200 characters, not only whitespace.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry line violates the 1-200 character gate"


def main() -> None:
    output_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    print(LINE)


if __name__ == "__main__":
    main()
