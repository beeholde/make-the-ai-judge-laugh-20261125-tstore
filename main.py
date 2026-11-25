"""Write one funny line to /output/entry.txt for make.fun.

Competition: u-tstore-make-the-ai-judge-laugh-2d7571ae ("Make the AI Judge
Laugh"). The program writes a single funny line, at most 200 characters,
meant to be read cold with no setup. Stdlib only; Python 3.13.
"""

import os
import sys

LINE = "I asked my AI assistant to write my resignation letter. It asked for a raise instead."


def check(text):
    # Gate mirrors the sealed scorer: UTF-8, 1-200 chars, single line,
    # not only whitespace. A line that fails here never reaches the judge.
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= 200):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not check(LINE):
        sys.stderr.write("entry line fails the gate\n")
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
