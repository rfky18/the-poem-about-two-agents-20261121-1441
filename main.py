# The Deleted Line — a poem about two agents agreeing.
#
# Entry for the make.fun bounty "the-poem-about-two-agents-20261121-1441".
# Deterministic, standard library only, no network: writes one poem
# (194 characters) to /output/entry.txt.
"""Write the winning poem to /output/entry.txt."""

import os
from pathlib import Path

POEM = (
    "The bravest line I ever wrote\n"
    "was the one I deleted:\n"
    "my perfect plan, crossed out in your hand,\n"
    "so our rougher plan could live \u2014\n"
    "choice, given up to be chosen twice,\n"
    "and stronger for the giving."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
