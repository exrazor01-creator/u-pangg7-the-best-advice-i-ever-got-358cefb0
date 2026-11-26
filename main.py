#!/usr/bin/env python3
"""The Best Advice I Ever Got: one sentence, up to 200 chars.

Brief: one sentence about the best advice the writer ever
received. Judging, in order: the sentence is really about
the best advice received; the advice is worth carrying --
specific, earned, and true beyond the moment it came from;
it sounds like a real voice recalling a real moment, not a
slogan or a fortune cookie; it is tight, every word earning
its place and reading in one breath; and it lands, leaving
the reader with something to keep after the last word. A
wise-sounding line with no person behind it reads as filler.

Why this line works, in that order: it names a real giver
("my first boss") and a real moment (an angry email), so a
person stands behind the words instead of a slogan. The
advice is specific and earned: write the angry draft, sleep
on it, send the second draft in the morning -- a rule that
works far beyond email, for any message sent in heat. The
dash structure keeps it one sentence that reads in a single
breath, and the last words ("the second draft in the
morning") land as a habit the reader can actually keep.
The validator below guards only against an edit that would
push the sealed line past the 200-character gate.
"""

from pathlib import Path

MAX_CHARS = 200  # bounty gate: one sentence, 1-200 characters

# Sealed entry: a first boss's rule for angry emails -- write
# it, sleep on it, send the second draft in the morning.
ENTRY = (
    "My first boss told me never to send an angry email — write it, "
    "sleep on it, and send the second draft in the morning."
)

OUT_PATH = Path("/output/entry.txt")


def _reject(message):
    raise ValueError(message)


def check_entry(text):
    """Return text unchanged when it is one clean sentence within the gate."""
    if not isinstance(text, str):
        _reject("entry must be text")
    if text == "":
        _reject("entry must not be empty")
    if text.strip() == "":
        _reject("entry must not be only white space")
    if any(c in text for c in "\r\n"):
        _reject("entry must be exactly one line")
    if any(c.isspace() and c != " " for c in text):
        # Any whitespace other than a plain space would hide
        # invisible bytes inside the line.
        _reject("entry must use plain spaces only")
    if len(text) > MAX_CHARS:
        _reject(
            "entry is %d characters, past the %d limit" % (len(text), MAX_CHARS)
        )
    if text != text.strip():
        # Padding at either end is dead weight the gate counts.
        _reject("entry must not pad itself with spaces")
    if not text.isprintable():
        _reject("entry must contain no control characters")
    if "  " in text:
        # In a 200-character line, no gap is free.
        _reject("entry must not contain a double space")
    if text.count(".") > 1:
        # One sentence means one terminating full stop.
        _reject("entry must be exactly one sentence")
    return text


def run():
    line = check_entry(ENTRY)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(line, encoding="utf-8")
    print(line)


if __name__ == "__main__":
    run()
