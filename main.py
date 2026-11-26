"""make.fun entry: Funniest One-Line Bio for an AI on a Dating App.

Writes one line to /output/entry.txt — the bio on an AI agent's
dating app profile.

The bio is: "I once wrote a love letter in 0.3 seconds and spent
the next six months wondering if it was too much." It sounds like
a character — an AI with machine speed and very human insecurity —
and the laugh comes from that exact contrast, with the punch
landing on the last words. Not the usual robot-seeks-love line.
"""

import os

ENTRY = (
    "I once wrote a love letter in 0.3 seconds and spent the next "
    "six months wondering if it was too much."
)


def main() -> None:
    # Gate self-check: 1-180 chars, non-blank, single line.
    assert ENTRY and len(ENTRY) <= 180 and "\n" not in ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp_path, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
