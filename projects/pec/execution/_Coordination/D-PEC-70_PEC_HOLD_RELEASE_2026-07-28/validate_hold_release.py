#!/usr/bin/env python3
"""Validate the D-PEC-70 hold-release application from repository root."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
PEC = ROOT / "projects/pec"
REGISTER = PEC / "execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv"
RECON = (
    PEC
    / "execution/_Reconciliation/DeliverableConcordance/"
    "PEC_SOW_V22_SCA003_RECON_2026-07-28"
)


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True)


def main() -> int:
    failures: list[str] = []
    with REGISTER.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        expected = {
            "HoldID", "Status", "TargetPath", "TargetClauses",
            "ProhibitedActs", "AllowedActs", "Authority", "ReleaseRule",
        }
        if set(reader.fieldnames or []) != expected or rows:
            failures.append("active-hold register is not a valid header-only register")

    summary = json.loads(
        (RECON / "R5_POST_VALIDATION/RUN_SUMMARY.json").read_text()
    )
    if summary.get("activeContractCount") != 32:
        failures.append("active-contract population is not 32")
    if summary.get("allToolExitCodesZero") is not True:
        failures.append("reconciliation validators did not all pass")

    verifier = (
        RECON / "BACKCHECK/INDEPENDENT_REPAIR_VERIFICATION_RERUN_3.md"
    ).read_text()
    if "result: PASS" not in verifier or "**PASS.**" not in verifier:
        failures.append("terminal independent verification is not PASS")

    artifact_list = RECON / "ARTIFACT_HASHES.sha256"
    entries = 0
    for line in artifact_list.read_text().splitlines():
        digest, rel = line.split("  ", 1)
        target = ROOT / rel if rel.startswith("projects/") else RECON / rel
        actual = hashlib.sha256(target.read_bytes()).hexdigest()
        entries += 1
        if actual != digest:
            failures.append(f"reconciliation hash mismatch: {rel}")
    if entries != 766:
        failures.append(f"expected 766 reconciliation hashes, found {entries}")

    hold_tests = run(
        sys.executable,
        "-m",
        "pytest",
        "-q",
        "projects/pec/execution/_Scripts/tests/test_pec_reliance_hold.py",
    )
    if hold_tests.returncode:
        failures.append("hold test suite failed")

    registers = run(
        sys.executable,
        "tools/validation/validate_decomposition_registers.py",
        "projects/pec/execution",
        "--strict",
    )
    if registers.returncode:
        failures.append("strict decomposition-register validation failed")

    result = {
        "status": "PASS" if not failures else "BLOCK",
        "failures": failures,
        "reconciliationArtifactHashesVerified": entries,
        "activeContractsValidated": summary.get("activeContractCount"),
        "holdTests": hold_tests.stdout.strip(),
        "registerValidationExit": registers.returncode,
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
