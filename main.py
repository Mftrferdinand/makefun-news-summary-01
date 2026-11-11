#!/usr/bin/env python3
"""Copy the bundled news summary to the make.fun output directory.

When executed, this script copies the file :data:`summary.txt`
from the same directory as ``main.py`` to a file called
``entry.txt`` inside the directory specified by the environment
variable ``MAKEFUN_OUTPUT_DIR``. If the variable is not defined,
the destination defaults to ``/output``.

The copy operation is byte‑for‑byte; no encoding conversion is
performed. The output directory is created if it does not
already exist.
"""

import os
import shutil


def main() -> None:
    # Determine the directory to write the output.
    out_dir = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    # Resolve paths relative to this file.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(script_dir, "summary.txt")
    dst_path = os.path.join(out_dir, "entry.txt")

    # Make a byte‑by‑byte copy. ``shutil.copyfile`` already does
    # precisely that, so we simply delegate to it.
    shutil.copyfile(src_path, dst_path)


if __name__ == "__main__":
    main()
