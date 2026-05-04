#!/usr/bin/env python3
"""Refresh time-sensitive counters in README.md.

Currently maintained:
  * "Sober N days" line — recomputed from SOBRIETY_START.

To add another counter, append a (pattern, replacement) pair to UPDATERS
below. Each replacement is called with the current README text and must
return the new text.
"""
from __future__ import annotations

import os
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"

SOBRIETY_START = os.environ.get("SOBRIETY_START", "2023-11-27")


def sober_days(today: date) -> int:
    start = datetime.strptime(SOBRIETY_START, "%Y-%m-%d").date()
    return (today - start).days


def update_sober(text: str, today: date) -> str:
    days = sober_days(today)
    return re.sub(r"Sober\s+\d+\s+days", f"Sober {days} days", text)


UPDATERS = [update_sober]


def main() -> int:
    today = date.today()
    text = README.read_text(encoding="utf-8")
    new_text = text
    for fn in UPDATERS:
        new_text = fn(new_text, today)

    if new_text == text:
        print("README already up to date.")
        return 0

    README.write_text(new_text, encoding="utf-8")
    print(f"README updated for {today.isoformat()}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
