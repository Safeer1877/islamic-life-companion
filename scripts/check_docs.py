#!/usr/bin/env python3
"""Validate documentation links and the frozen experience inventory.

No external dependencies or network. Does NOT validate claim truth,
external websites, fiqh interpretation, user experience or platform behavior.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def fail(message: str) -> None:
    ERRORS.append(message)


def check_links() -> int:
    checked = 0
    # Original AI-generated research reports remain immutable and are not
    # treated as maintained first-party Markdown documentation.
    for file in ROOT.rglob("*.md"):
        relative = file.relative_to(ROOT)
        if "research/original-reports" in relative.as_posix():
            continue
        content = file.read_text(encoding="utf-8")
        for match in re.finditer(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", content):
            reference = match.group(1).strip()
            if not reference or reference.startswith("#"):
                continue
            if reference.startswith("<") and reference.endswith(">"):
                reference = reference[1:-1]
            url = urlsplit(reference)
            if url.scheme or url.netloc or reference.startswith("//"):
                continue
            candidate = unquote(url.path)
            if not candidate:
                continue
            target = ROOT / candidate.lstrip("/") if candidate.startswith("/") else file.parent / candidate
            checked += 1
            if not target.exists():
                line = content.count("\n", 0, match.start()) + 1
                fail(f"Missing relative link: {relative}:{line} -> {reference}")
    return checked


def check_inventory() -> tuple[int, int]:
    screen_file = ROOT / "docs/blueprint/SCREEN_REGISTER_v1.csv"
    with screen_file.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    screen_ids = [row.get("id", "") for row in rows]
    if len(screen_ids) != len(set(screen_ids)):
        fail("Screen register has duplicate IDs")
    if len(screen_ids) != 106:
        fail(f"Expected baseline of 106 state IDs, got {len(screen_ids)}")
    expected = [f"S{i:02d}" for i in range(88)] + [f"X{i}" for i in range(88, 98)] + [f"M{i}" for i in range(98, 106)]
    if set(screen_ids) != set(expected):
        fail("Screen register has missing or unexpected baseline IDs")
    blueprint = (ROOT / "docs/blueprint/PRODUCT_BLUEPRINT_v1.md").read_text(encoding="utf-8")
    flows = re.findall(r"^### UF\d{2}\s+[—-]", blueprint, flags=re.MULTILINE)
    if len(flows) != 30:
        fail(f"Expected 30 sample user flow headings, got {len(flows)}")
    for path in (
        "docs/blueprint/LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md",
        "docs/blueprint/MOSQUE_COMMUNITY_NETWORK_PROPOSAL_v0.1.md",
        "docs/research/RESEARCH_STANDARDS.md",
        "docs/research/CLAIM_LEDGER.md",
        "CONTRIBUTING.md",
    ):
        if not (ROOT / path).is_file():
            fail(f"Missing required documentation: {path}")
    return len(screen_ids), len(flows)


def main() -> int:
    links = check_links()
    screens, flows = check_inventory()
    if ERRORS:
        print("\n".join(f"FAIL: {message}" for message in ERRORS), file=sys.stderr)
        return 1
    print(f"PASS: checked {links} local links; {screens} state IDs; {flows} flows.")
    print("NOTE: This is an integrity check, NOT a source, religious, or usability validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
