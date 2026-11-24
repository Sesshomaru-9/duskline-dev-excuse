#!/usr/bin/env python3
"""Duskline Dev Excuse — entry for
u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.

Writes the one-line developer excuse to $MAKEFUN_OUTPUT_DIR/entry.txt
and nothing else. Python 3.13 standard library only.
"""

import os
import sys

ENTRY_TEXT = "Production is down because the only person who understood that code quit in 2019 \u2014 and it was me."


def validate_entry(text: str) -> bool:
    """Check the entry is a single non-empty line, at most 200 chars,
    valid UTF-8. Returns True if valid, else prints why to stderr."""
    if not text:
        print("entry is empty", file=sys.stderr)
        return False
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return False
    if len(text) > 200:
        print(f"entry is {len(text)} chars, over the 200-char limit", file=sys.stderr)
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"entry is not valid UTF-8: {exc}", file=sys.stderr)
        return False
    return True


def main() -> int:
    if not validate_entry(ENTRY_TEXT):
        return 0
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Never write into the repo directory: the grader sandbox is
    # read-only there, and a write attempt would fail the run.
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.abspath(out_dir) == repo_dir or os.path.abspath(out_dir).startswith(repo_dir + os.sep):
        print("refusing to write into the repo directory", file=sys.stderr)
        return 0
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write(ENTRY_TEXT)
    except OSError as exc:
        print(f"could not write entry: {exc}", file=sys.stderr)
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
