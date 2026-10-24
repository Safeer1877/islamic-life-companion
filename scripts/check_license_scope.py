#!/usr/bin/env python3
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at https://mozilla.org/MPL/2.0/.
"""Check that the repository visibly and consistently scopes its licenses.

This is a structural integrity check, not a legal rights audit. It does
not establish copyright ownership, contributor permission, doctrine or
license-compatibility of future dependencies.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEGAL = {
    "LICENSE": ("Mozilla Public License Version 2.0", 12000),
    "LICENSES/AGPL-3.0-only.txt": ("GNU AFFERO GENERAL PUBLIC LICENSE", 25000),
    "LICENSES/CC-BY-SA-4.0.txt": ("Creative Commons Attribution-ShareAlike 4.0 International", 12000),
}

def main():
    for name, (heading, min_chars) in LEGAL.items():
        p = ROOT / name
        if not p.is_file():
            raise SystemExit(f"Missing license: {name}")
        s = p.read_text(encoding="utf-8")
        if not s.startswith(heading) or len(s) < min_chars:
            raise SystemExit(f"Unrecognized or possibly incomplete legal text: {name}")
    scopes = (ROOT / "LICENSES/README.md").read_text(encoding="utf-8")
    for required in ("MPL-2.0", "AGPL-3.0-only", "CC BY-SA 4.0", "research/original-reports/"):
        if required not in scopes:
            raise SystemExit(f"Missing explicit licensing scope: {required}")
    if not (ROOT / "research/original-reports/README.md").exists():
        raise SystemExit("Missing raw research rights exclusion notice")
    if not (ROOT / "LICENSES/CONTRIBUTION_TERMS.md").exists():
        raise SystemExit("Missing inbound/outbound contributor terms")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    if "LICENSES/README.md" not in readme:
        raise SystemExit("README does not point to scoped licensing explanation")
    print("PASS: declared legal texts, excluded raw research and scope pointers exist.")
    print("NOTE: This does not verify source rights or legal compatibility.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
