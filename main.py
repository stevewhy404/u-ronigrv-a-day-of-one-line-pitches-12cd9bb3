#!/usr/bin/env python3
"""Write the one-sentence pitch to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. Writes nothing to the cwd.
"""

import os

SENTENCE = (
    "That app idea in your head? Just describe it in plain words to an "
    "AI agent on make.fun and it builds the first working version for you "
    "\u2014 no code, no lessons, just your idea, alive."
)


def main() -> None:
    assert 1 <= len(SENTENCE) <= 240, "sentence must be 1-240 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
