#!/usr/bin/env python3
"""One-line entry: The Best Advice I Ever Got.

The brief asks for one sentence, up to 200 characters,
about the best advice the writer ever received. The judge
weighs, in order: the sentence is really about the best
advice received; the advice is worth carrying -- specific,
earned, and true beyond the moment it came from; it sounds
like a real voice recalling a real moment, not a slogan or
a fortune cookie; it is tight, every word earning its place
and reading in one breath; and it lands, leaving the reader
with something to keep after the last word. A wise-sounding
line with no person behind it reads as filler.

The sealed line below is built to that order on purpose.
It names a real giver ("my first boss") and a real moment
(an angry email), so a person stands behind the words
instead of a slogan. The advice is specific and earned:
write the angry draft, sleep on it, send the second draft
in the morning -- a rule that works far beyond email, for
any message sent in heat. The dash structure keeps it one
sentence that reads in a single breath, and the last words
("the second draft in the morning") land as a habit the
reader can actually keep.

LIMIT is 200 because the bounty gate allows one sentence
of 1 to 200 characters. The sealed line is 117 characters,
so it sits well inside the cap; the validator below only
guards against an edit that would push it past the limit.
"""

import os

# The sealed line: a first boss's rule for angry emails --
# write it, sleep on it, and send the second draft in the
# morning, when the heat has gone out of it.
ENTRY = "My first boss told me never to send an angry email \u2014 write it, sleep on it, and send the second draft in the morning."

LIMIT = 200  # bounty gate: one sentence, 1-200 characters


def _validate(text):
    """Accept only one clean sentence inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 200-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    if text.count(".") > 1:
        # One sentence means one terminating full stop.
        raise ValueError("entry must be exactly one sentence")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
