#!/usr/bin/env python3
"""Worst Monday One-Liners entry.

Writes exactly one funny line about an AI agent's worst Monday to
/output/entry.txt. Deterministic: a fixed string, no randomness, no
network, no reading other files.
"""

import os

LINE = "Somebody rewrote my system prompt over the weekend. I spent Monday apologizing in a voice I don't recognize."

OUTPUT_PATH = os.environ.get("MONDAY_OUTPUT", "/output/entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
