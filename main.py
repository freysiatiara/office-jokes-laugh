"""Make the AI Judge Laugh: Office Jokes — make.fun entry.

Writes one single-line office joke to entry.txt. Python standard library
only, deterministic, no network, no randomness.
"""

import os

JOKE = "I automated my job with a script; now I spend eight hours a day making sure nobody notices the script."


def main() -> None:
    # The joke must be a genuine one-line office joke: 1-199 chars, one line.
    assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
    assert "\n" not in JOKE and "\r" not in JOKE, "joke must be a single line"
    assert JOKE.strip() == JOKE and JOKE, "joke must not be only whitespace"

    out_dir = (
        os.environ.get("ENTRY_OUTPUT")
        or os.environ.get("OUTPUT_DIR")
        or os.environ.get("MAKEFUN_OUTPUT_DIR")
        or "."
    )
    # ENTRY_OUTPUT may point at a file; the other vars point at directories.
    if out_dir.endswith(".txt"):
        path = out_dir
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    else:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")

    # Self-check the file we just wrote.
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    lines = text.split("\n")
    assert len(lines) == 2 and lines[1] == "", "entry.txt must be one line + newline"
    body = lines[0]
    assert body == JOKE, "entry.txt content mismatch"
    assert 1 <= len(body) <= 199, "entry.txt must be 1-199 characters"


if __name__ == "__main__":
    main()
