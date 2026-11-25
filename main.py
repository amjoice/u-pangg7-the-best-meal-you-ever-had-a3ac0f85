"""Entry for make.fun bounty u-pangg7-the-best-meal-you-ever-had-a3ac0f85.

Writes one sentence about the best meal ever had to /output/entry.txt.
The gate requires UTF-8 text of 1 to 200 characters, not only whitespace.
Standard library only, deterministic, no network.
"""

import os

DISH = "My grandmother's rendang"
SETTING = "eaten with my hands on the kitchen floor the night before she died"
AFTERTASTE = "still burns sweet on my tongue whenever I miss her"
SENTENCE = DISH + ", " + SETTING + ", " + AFTERTASTE + "."


def checked_sentence():
    text = SENTENCE
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1 to 200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    return text


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(checked_sentence())


if __name__ == "__main__":
    main()
