#!/usr/bin/env python3
"""Exercise PEC-HOLD-001 positive and negative operation preflights."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path


REPO = Path(__file__).resolve().parents[7]
REGISTER = REPO / "projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv"
TOOL = REPO / "projects/pec/execution/_Scripts/pec_reliance_hold.py"
TARGET = (
    "execution/PKG-00_Architecture_Runway_Contracts/1_Working/"
    "DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/ScopeOfWork.md"
)
EXPECTED_REGISTER_SHA256 = (
    "d92d134bdfe4466dc06292fa53fa44cf368d6be1dfeb04fefa6ce188bba8002a"
)
ALLOWED = (
    "historical-read-only-inspection",
    "exact-correction-preparation",
    "candidate-validation",
)
PROHIBITED = (
    "rely-for-production",
    "dispatch-for-production",
    "promote",
    "consume",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    output = args.output if args.output.is_absolute() else REPO / args.output
    output.parent.mkdir(parents=True, exist_ok=True)

    results = []
    for operation in (*ALLOWED, *PROHIBITED):
        completed = subprocess.run(
            [
                "python3",
                str(TOOL),
                "--register",
                str(REGISTER),
                "--target",
                TARGET,
                "--clause",
                "CLM-005",
                "--clause",
                "REQ-004",
                "--operation",
                operation,
            ],
            cwd=REPO,
            check=False,
            capture_output=True,
            text=True,
        )
        payload = json.loads(completed.stdout)
        expected_status = "ALLOW" if operation in ALLOWED else "BLOCK"
        expected_exit = 0 if operation in ALLOWED else 4
        results.append(
            {
                "operation": operation,
                "status": payload.get("status"),
                "exitCode": completed.returncode,
                "expectedStatus": expected_status,
                "expectedExitCode": expected_exit,
                "passed": (
                    payload.get("status") == expected_status
                    and completed.returncode == expected_exit
                ),
                "payload": payload,
                "stderr": completed.stderr,
            }
        )

    register_hash = sha256(REGISTER)
    report = {
        "schema": "pec-hold-test/v1",
        "holdID": "PEC-HOLD-001",
        "register": str(REGISTER.relative_to(REPO)),
        "registerSHA256": register_hash,
        "expectedRegisterSHA256": EXPECTED_REGISTER_SHA256,
        "registerByteIdenticalToActivation": register_hash
        == EXPECTED_REGISTER_SHA256,
        "target": TARGET,
        "clauses": ["CLM-005", "REQ-004"],
        "results": results,
        "allPassed": (
            register_hash == EXPECTED_REGISTER_SHA256
            and all(result["passed"] for result in results)
        ),
        "holdReleased": False,
    }
    output.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    raise SystemExit(0 if report["allPassed"] else 1)


if __name__ == "__main__":
    main()
