#!/usr/bin/env python3
"""Deadpan forecast for Brindlewick, a city that exists only on
Tuesdays -- make.fun entry "Deadpan Forecasts for Cities That Do
Not Exist" (deadpan-b, account B).

The forecast is written the way a bored TV meteorologist would
read it: flat, factual, unbothered. Brindlewick is real for one
day a week, its sun has filed for annual leave, and the forecast
compensates with the driest possible advice -- bring your own
daylight. The absurdity is the premise; the joke is how seriously
the broadcast takes it. Concrete details (14 degrees, drizzle,
the advisory) make the invented place feel mapped.
"""

from pathlib import Path

ENTRY_PATH = Path("/output/entry.txt")
MAX_CHARS = 160

FORECAST = (
    "In Tuesday-only Brindlewick, the sun is on annual leave, "
    "so expect 14 degrees of drizzle and residents are advised "
    "to bring their own daylight."
)


def check_gate(text):
    """Return a list of gate failures; empty means the entry is valid."""
    failures = []
    if not text.strip():
        failures.append("blank entry")
    if text != text.strip():
        failures.append("stray surrounding whitespace")
    if len(text) > MAX_CHARS:
        failures.append("over the %d-char gate by %d" % (MAX_CHARS, len(text) - MAX_CHARS))
    if "\n" in text:
        failures.append("more than one line")
    return failures


def main():
    failures = check_gate(FORECAST)
    if failures:
        raise SystemExit("gate failed: " + "; ".join(failures))
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(FORECAST, encoding="utf-8")
    round_tripped = ENTRY_PATH.read_text(encoding="utf-8")
    assert round_tripped == FORECAST, "entry.txt round-trip mismatch"
    print("Wrote %s: %d chars, %d spare"
          % (ENTRY_PATH, len(FORECAST), MAX_CHARS - len(FORECAST)))
    print(FORECAST)


if __name__ == "__main__":
    main()
