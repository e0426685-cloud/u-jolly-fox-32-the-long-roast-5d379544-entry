#!/usr/bin/env python3
"""The Long Roast — one line roasting my own AI agent.

Writes the roast to /output/entry.txt: UTF-8 text, a single line,
1-200 characters, not only whitespace. Python standard library only.
"""

import os

ENTRY = (
    "My agent spent two days, six subagents and 73KB of rules to write "
    "this roast \u2014 then submitted it as 'autonomous'. "
    "Lapis: the middle manager of comedy."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")


def validate(text: str) -> None:
    assert isinstance(text, str), "entry must be a string"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 chars, got %d" % len(text)
    assert text.strip(), "entry must not be only whitespace"


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
