"""Tell a Whole Story in 32 Characters.

Writes one Wi-Fi network name to entry.txt: a tiny domestic tragedy.
A named character, a situation, and something that already happened,
compressed into one line a stranger reads in a network list.

Deterministic: the same fixed string on every run, whatever the
output directory. Standard library only; no network, no clock, no
environment secrets.
"""

import os

# The entry: Uncle Ray, the household's Wi-Fi, and a pawn shop.
# Character + situation + mishap in 27 characters. "Our" matters:
# it names the victims too -- the family whose internet is gone --
# so the name implies two sides of the story, not just the culprit.
NAME = "Uncle Ray pawned our router"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exactly the name, no trailing newline: the file IS the network name.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(NAME)


if __name__ == "__main__":
    main()
