"""Entry program for news-image-20261122.

Copies the bundled entry.png to the output path the harness asks for.
Deterministic: the shipped image is fixed, so both runs write the
same bytes. No network, no arguments needed.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    target = os.environ.get("ENTRY_OUTPUT", "/output/entry.png")
    folder = os.path.dirname(target)
    if folder:
        os.makedirs(folder, exist_ok=True)
    shutil.copyfile(source, target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
