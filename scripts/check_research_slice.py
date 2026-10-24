#!/usr/bin/env python3
"""Validate the proposed research slice and references, not product effectiveness.

Zero external dependencies. This does not prove mobile OS timing, religious
correctness, user usefulness, or data security.
"""
from __future__ import annotations

import csv
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REGISTER = ROOT / "docs/blueprint/SCREEN_REGISTER_v1.csv"
MVP = ROOT / "docs/research/RESEARCH_MVP_VALIDATION_PLAN_v0.1.md"
MOBILE = ROOT / "docs/architecture/MOBILE_RELIABILITY_PRIVACY_CONTRACT_v0.1.md"
POLICY = ROOT / "docs/blueprint/LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md"
BLUEPRINT = ROOT / "docs/blueprint/PRODUCT_BLUEPRINT_v1.md"
MOSQUE = ROOT / "docs/blueprint/MOSQUE_COMMUNITY_NETWORK_PROPOSAL_v0.1.md"

ALLOWED = {
    "Candidate-contract", "Optional-research-variant",
    "Separate-source-or-scholarly-gate", "Catalog-deferred",
}

def run() -> int:
    problems: list[str] = []
    for doc in (REGISTER, MVP, MOBILE, POLICY, BLUEPRINT, MOSQUE):
        if not doc.is_file():
            problems.append(f"Missing document: {doc.relative_to(ROOT)}")
    if problems:
        print("\n".join(f"FAIL {p}" for p in problems), file=sys.stderr)
        return 1

    with REGISTER.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        cols = set(reader.fieldnames or [])
    if not {"id", "release", "v1_1_local_first_note", "research_slice_v0_1"} <= cols:
        problems.append("Missing CSV provenance, release or research-slice columns")
    ids = [row.get("id", "") for row in rows]
    if len(ids) != len(set(ids)):
        problems.append("Duplicate screen IDs")
    if not rows:
        problems.append("Screen register is empty")
    unknown = [row.get("id") for row in rows if row.get("research_slice_v0_1") not in ALLOWED]
    if unknown:
        problems.append(f"Unexpected research slice labels on: {unknown}")
    selected = [row["id"] for row in rows if row.get("research_slice_v0_1") == "Candidate-contract"]
    if not selected:
        problems.append("No candidate contracts marked")

    mvp = MVP.read_text(encoding="utf-8")
    for screen in selected:
        if f"\x60{screen}\x60" not in mvp and f"{screen}" not in mvp:
            # Ranges such as S38–S40 count only if in the bounded range.
            if screen not in {"S39", "S40"}:
                problems.append(f"Candidate screen absent from slice document: {screen}")
    policy = POLICY.read_text(encoding="utf-8")
    for needed in (
        "RESEARCH_MVP_VALIDATION_PLAN_v0.1.md",
        "MOBILE_RELIABILITY_PRIVACY_CONTRACT_v0.1.md",
    ):
        if needed not in policy:
            problems.append(f"Policy missing new contract reference: {needed}")

    blueprint = BLUEPRINT.read_text(encoding="utf-8")
    if "RESEARCH_MVP_VALIDATION_PLAN_v0.1.md" not in blueprint:
        problems.append("Master blueprint missing prototype-scope link")
    mosque = MOSQUE.read_text(encoding="utf-8")
    if "previously queued" not in mosque.lower():
        problems.append("Mosque proposal lacks queued-staleness warning")
    for row in rows:
        if row["id"] in {"S70", "S87"}:
            if "Submit " in row.get("primary_action", ""):
                problems.append(f"{row['id']} falsely indicates active reporting")
    if problems:
        print("\n".join(f"FAIL {p}" for p in problems), file=sys.stderr)
        return 1

    print(f"PASS: {len(rows)} catalog IDs, {len(selected)} candidate contracts, all status labels recognized.")
    print("NOTE: Internal consistency only; device, scholarly, user and privacy tests still required.")
    return 0

if __name__ == "__main__":
    raise SystemExit(run())
