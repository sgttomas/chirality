#!/usr/bin/env python3
"""Validate the D-PEC-71 ratification after the owner session.

Run from anywhere; paths resolve against the repository root.

This validator is a POST-COMPLETION check. On the awaiting-ruling candidate it
is expected to report BLOCK: the record still carries ruling placeholders, the
register row still reads AWAITING_RULING, and the effective commit is PENDING.
Run it again after the completion commit that records the owner's verbatim
rulings; it must then report PASS.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
PACKET = Path(__file__).resolve().parent
DECISIONS = ROOT / "projects/pec/execution/_Coordination/_DECISIONS"
RECORD = DECISIONS / "D-PEC-71_od8_ratification.md"
REGISTER = DECISIONS / "_REGISTER.md"
RECEIPTS = ROOT / "_DomainEngines/pec/LOOP_RECEIPTS.md"
MANIFEST = PACKET / "ARTIFACT_HASHES.sha256"

# Built from parts so this file never contains the literal placeholder token.
PLACEHOLDER_TOKEN = "<<" + "RULING PLACEHOLDER"

FULL_SHA = re.compile(r"^[0-9a-f]{40}$")

# The D-PEC-70 closeout pins these at nine hex; D-PEC-71 must restate both at
# full 40 hex without editing that closeout.
RESTATED_COMMITS = (
    "5fdbf657268d06e1c0aaaab99740fa5c57f760fc",
    "80d8c65c7b41242c95f403ebdce3f99bad0684bd",
)


def header_value(text: str, field: str) -> str:
    match = re.search(rf"^\*\*{re.escape(field)}:\*\*\s*(.+)$", text, re.M)
    return match.group(1).strip().strip("`") if match else ""


def register_row(text: str) -> list[str]:
    for line in text.splitlines():
        if line.startswith("| D-PEC-71 |"):
            return [cell.strip() for cell in line.split("|")]
    return []


def main() -> int:
    failures: list[str] = []

    if not RECORD.is_file():
        print(json.dumps({"status": "BLOCK", "failures": ["record missing"]}))
        return 1
    record = RECORD.read_text(encoding="utf-8")

    placeholders = record.count(PLACEHOLDER_TOKEN)
    if placeholders:
        failures.append(f"{placeholders} ruling placeholder(s) remain in the record")

    status = header_value(record, "Status")
    if not status or status.upper().startswith("AWAITING"):
        failures.append(f"record status is not ruled: {status!r}")

    effective = header_value(record, "EffectiveCommit")
    if not FULL_SHA.match(effective):
        failures.append(f"EffectiveCommit is not a full 40-hex commit: {effective!r}")

    for commit in RESTATED_COMMITS:
        if commit not in record:
            failures.append(f"record does not restate {commit} at full 40 hex")

    row = register_row(REGISTER.read_text(encoding="utf-8"))
    if not row:
        failures.append("no D-PEC-71 row in the decision register")
    else:
        state = row[4]
        if not state or state.upper().startswith("AWAITING"):
            failures.append(f"register row state is not ruled: {state!r}")
        if "D-PEC-71_od8_ratification.md" not in row[5]:
            failures.append("register packet cell does not name the record file")

    entries = 0
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, rel = line.split("  ", 1)
        target = ROOT / rel
        if not target.is_file():
            failures.append(f"manifest target missing: {rel}")
            continue
        entries += 1
        if hashlib.sha256(target.read_bytes()).hexdigest() != digest:
            failures.append(f"packet hash mismatch: {rel}")
    if entries != 5:
        failures.append(f"expected 5 packet artifact hashes, found {entries}")

    if "Receipt 119" not in RECEIPTS.read_text(encoding="utf-8"):
        failures.append("PEC loop receipt 119 has not been appended")

    registers = subprocess.run(
        [
            sys.executable,
            "tools/validation/validate_decomposition_registers.py",
            "projects/pec/execution",
            "--strict",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if registers.returncode:
        failures.append("strict decomposition-register validation failed")

    result = {
        "status": "PASS" if not failures else "BLOCK",
        "failures": failures,
        "packetArtifactHashesVerified": entries,
        "recordStatus": status,
        "effectiveCommit": effective,
        "registerValidationExit": registers.returncode,
        "rulingPlaceholdersRemaining": placeholders,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
