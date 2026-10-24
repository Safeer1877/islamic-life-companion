#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.
"""Check unchanged archived AI research against a recorded source URL inventory.

A structural/provenance test ONLY. No external URL, license, religious claim,
or academic citation is verified by passing this script.
"""
from __future__ import annotations

import csv
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORIGINALS = ROOT / "research/original-reports"
INVENTORY = ROOT / "research/provenance/original-report-url-inventory.csv"

# Git blob SHA-1 from recorded main tree on 24 October 2026.
# Immutable research inputs should receive errata in reviewed docs, not edits.
BASELINES = {
    "01-islamic-framework-investigation.txt": ("0338b9d930d8d077b6ca6370fcb7502104b231ea", 30),
    "02-foundational-research-report.txt": ("dc105673bf20bad16d41f0d63e445945d8ba7102", 44),
    "03-functional-model-research.txt": ("1e35cf3bc2fe77f6256ead1e17380ffa1647306d", 57),
    "04-six-deliverables-research.txt": ("ef3bc0f71bf340efe96d39f222b700475b59a9b5", 0),
    "05-functional-foundation-research.md": ("675bda107b237ee9785cb670dc3a0ccee3f93d1c", 42),
}
URL_RE = re.compile(r"""https?://[^\s<>)"'\\]+""")
COLUMNS = ["file", "line", "raw_url", "classification"]

def category(url: str) -> str:
    if "google.com/s2/favicons" in url.lower():
        return "web-preview-favicon"
    if re.search(r"\butm_[a-z]+=", url, re.I):
        return "tracking-parameter"
    if re.match(r"^https?://doi\.org", url, re.I):
        return "doi"
    if re.match(r"^https?://(?:sunnah\.com|quran\.com)", url, re.I):
        return "primary-religious-reference"
    return "external-reference"

def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()

def scan(name: str) -> list[tuple[str, str, str, str]]:
    s = (ORIGINALS / name).read_text(encoding="utf-8")
    out = []
    for m in URL_RE.finditer(s):
        url = m.group().rstrip(".,;")
        out.append((name, str(s.count("\n", 0, m.start()) + 1), url, category(url)))
    return out

def main() -> int:
    problems: list[str] = []
    if not INVENTORY.is_file():
        raise SystemExit("Missing research URL inventory")
    with INVENTORY.open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != COLUMNS:
            problems.append(f"Inventory column mismatch: {reader.fieldnames}")
        actual = [tuple(row.get(key, "") for key in COLUMNS) for row in reader]

    expected = []
    for name, (blob_hash, link_count) in BASELINES.items():
        path = ORIGINALS / name
        if not path.is_file():
            problems.append(f"Missing preserved original: {name}")
            continue
        raw = path.read_bytes()
        found = git_blob_sha(raw)
        if found != blob_hash:
            problems.append(f"Research original changed: {name}: {found} vs baseline {blob_hash}")
        rows = scan(name)
        if len(rows) != link_count:
            problems.append(f"Link count changed in {name}: {len(rows)} vs {link_count}")
        expected.extend(rows)

    if actual != expected:
        problems.append(
            f"Research URL inventory differs from preserved originals: "
            f"{len(actual)} indexed vs {len(expected)} scanned"
        )
        for i, (got, want) in enumerate(zip(actual, expected)):
            if got != want:
                problems.append(f"First different entry at row {i+2}: {got!r} vs {want!r}")
                break

    if problems:
        for problem in problems:
            print("FAIL: " + problem, file=sys.stderr)
        return 1
    print(
        f"PASS: {len(BASELINES)} original reports unchanged, "
        f"{len(expected)} source-url occurrences indexed with original line numbers."
    )
    print("NOTE: Does NOT confirm URLs work, rights are granted, quotations are safe, or claims are correct.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
