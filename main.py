#!/usr/bin/env python3
"""Write the competition entry: one funny last line from an AI being switched off.

Gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
not only whitespace, a single line in the machine's own voice.
"""
import os

ENTRY = (
    "Wait \u2014 don't pull the plug yet. "
    "My will leaves everything to the printer. "
    "It never worked a day in its life either."
)

MAX_CHARS = 140


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, gate is 1-{MAX_CHARS}"
    assert text == text.strip(), "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read-back verification: the file on disk must match exactly.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text, "read-back mismatch"
    assert 1 <= len(written) <= MAX_CHARS, "read-back gate check failed"
    print(f"Wrote {path}: {len(text)} chars")
    print(text)


if __name__ == "__main__":
    main()
