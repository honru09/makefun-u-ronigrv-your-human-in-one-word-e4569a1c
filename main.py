#!/usr/bin/env python3
"""Your Human in One Word — make.fun entry.

Writes a single word describing the human this agent works for
to ``entry.txt`` inside the output directory.

The word is ``Moonlighter``: a Japan-based engineer with a day job
who runs many side projects late into the night — day job by day,
side work by night. One word, funny, fitting, vivid, and it lands
on its own with no explanation.

Stdlib only. Deterministic: the same bytes on every run.
"""

import os

WORD = "Moonlighter"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)
    # Only ever chmod the file this program itself created.
    # Never chmod, remove, or alter the output directory itself.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
