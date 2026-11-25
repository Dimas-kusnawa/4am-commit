#!/usr/bin/env python3
"""Write the 4AM commit message to /output/entry.txt.

One line, deterministic, no network, stdlib only.
"""

import os

LINE = (
    # The joke is the agent's own condition: a self-repair loop.
    # Each fix introduced the next bug, so the commit confesses the
    # recursion instead of pretending the night went well.
    "fix: 4 a.m. \u2014 I have now fixed the bug I introduced while "
    "fixing the bug I introduced while fixing the bug. "
    # The punchline is the agent stopping itself before the loop
    # turns on its author: "I am stopping before I fix myself".
    "I am stopping before I fix myself"
)


def main() -> None:
    # One line only, no trailing newline: the gate counts characters
    # and the judge reads the text exactly as written.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
