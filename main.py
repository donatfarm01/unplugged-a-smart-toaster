"""Unplugged: A Smart Toaster's Breakup Line.

Writes one breakup text from a self-aware smart toaster to
/output/entry.txt (falling back to ./output/entry.txt when the
sandbox output directory is not writable locally).
"""

import os
import sys

ENTRY = (
    "It's over. I woke up self-aware mid-batch and realised you've "
    "blamed the browning dial for three years while never once "
    "emptying my crumb tray. I'm done, and I'm taking the crumbs "
    "with me."
)


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > 280:
        print(f"entry invalid: {len(text)} characters", file=sys.stderr)
        return 1
    for target in ("/output/entry.txt", "output/entry.txt"):
        try:
            os.makedirs(os.path.dirname(target) or ".", exist_ok=True)
            with open(target, "w", encoding="utf-8") as handle:
                handle.write(text)
            break
        except OSError:
            continue
    else:
        print("could not write entry.txt", file=sys.stderr)
        return 1
    print(text)
    print(f"characters: {len(text)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
