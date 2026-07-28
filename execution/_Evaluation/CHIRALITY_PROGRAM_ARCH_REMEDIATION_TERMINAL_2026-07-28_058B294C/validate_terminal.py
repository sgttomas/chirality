#!/usr/bin/env python3
"""Deterministic validation for the terminal remediation package."""

from __future__ import annotations

import csv
import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EXPECTED = {
    "docs/PRD_ROOT.md":
        "0e36a03abc16b86f99024aa2a17c467ae7f4303f9740be3a6ba2e9dd1dfb2f2d",
    "execution/_Decomposition/Chirality_Root_SOFTWARE_DECOMP_v1_0.md":
        "2dd37e20d8175eec3a7a926dcf454fbee5065d076fc59eac6ead82e911192c18",
    "projects/chirality-app-dev/docs/PRD.md":
        "ef638f43ccae1cd78b26b1ae078a33770cf64cc36c247c5d7da04b35196a4010",
    "projects/chirality-app-dev/execution/_Decomposition/"
    "Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md":
        "dd6027b4bc6861aac801c8777c76606326c952b75761f8dd082e5e341f1e5c83",
    "projects/pec/docs/PRD.md":
        "6833553c33aadca00e4ee6932d56ae4698c2ae7798c30b603bc17e60dae477ba",
    "projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md":
        "3f65ea0e47036a2baa66cb60923f8b779525ae00d747425f93f8b69431151787",
    "projects/chirality-piping/docs/PRD.md":
        "9c3bccd8d2eb8e68c10e05d50bdd29619892196c98069a2587ba3a1ff4880793",
    "projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md":
        "82b835b5fd36d0fd337da5b084dbf146caa29c18d0e1ef8f96a06fcfa4363a07",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(*args: str) -> int:
    return subprocess.run(args, cwd=ROOT, check=False).returncode


def main() -> int:
    failures: list[str] = []
    try:
        __import__("pytest")
    except ImportError:
        print(
            "BLOCK: pytest is unavailable in the selected Python environment; "
            "run with the repository's configured Python."
        )
        return 2
    for path, expected in EXPECTED.items():
        if digest(ROOT / path) != expected:
            failures.append(f"identity mismatch: {path}")

    notice_path = (
        ROOT / "execution/_Coordination/"
        "PROGRAM_ARCH_REMEDIATION_NOTICE_STATUS_2026-07-28.csv"
    )
    with notice_path.open(newline="", encoding="utf-8") as handle:
        notices = list(csv.DictReader(handle))
    if len(notices) != 30:
        failures.append(f"notice population is {len(notices)}, expected 30")
    for row in notices:
        target = ROOT / row["NoticePath"]
        if not target.is_file() or digest(target) != row["SHA256"]:
            failures.append(f"notice identity mismatch: {row['NoticePath']}")
        if row["DeliveryState"] != "DELIVERED":
            failures.append(f"notice not delivered: {row['NoticePath']}")

    active_registers = [
        ROOT / "projects/chirality-app-dev/execution/_Coordination/"
        "APP_HOLD_REGISTER.csv",
        ROOT / "projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv",
    ]
    for register in active_registers:
        with register.open(newline="", encoding="utf-8") as handle:
            if list(csv.DictReader(handle)):
                failures.append(f"active rows remain: {register.relative_to(ROOT)}")

    app_gate5 = (
        ROOT / "projects/chirality-app-dev/execution/_ScopeChange/"
        "SCA-APP-006_2026-07-27_1159_Invariant_Mapping_Repair/"
        "Gate_5_Validation.json"
    )
    if '"status": "PASS"' not in app_gate5.read_text():
        failures.append("accepted App Gate-5 validation is not PASS")

    commands = [
        (
            sys.executable, "-m", "pytest", "-q",
            "projects/chirality-app-dev/execution/_Scripts/tests/test_app_hold.py",
            "projects/pec/execution/_Scripts/tests/test_pec_reliance_hold.py",
            "tools/validation/test_validate_domain_engine_profile.py",
            "tools/validation/test_validate_path_anchors.py",
            "tools/validation/test_validate_piping_loop_receipts.py",
        ),
        (
            sys.executable,
            "projects/chirality-app-dev/execution/_Coordination/_PROPOSALS/"
            "OD6-G5_APP_HOLD_RELEASE_2026-07-28/validate_hold_release.py",
        ),
        (
            sys.executable,
            "projects/pec/execution/_Coordination/"
            "D-PEC-70_PEC_HOLD_RELEASE_2026-07-28/validate_hold_release.py",
        ),
        (
            sys.executable,
            "tools/validation/validate_decomposition_registers.py",
            "projects/pec/execution",
            "--strict",
        ),
        (sys.executable, "tools/validation/validate_path_anchors.py"),
        (sys.executable, "tools/validation/validate_piping_loop_receipts.py"),
    ]
    for command in commands:
        if run(*command):
            failures.append("command failed: " + " ".join(command))

    if failures:
        print("BLOCK")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("PASS")
    print("- 8/8 product instrument identities")
    print("- 30/30 live notice identities")
    print("- App and PEC active-hold registers empty")
    print("- all terminal deterministic commands passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
