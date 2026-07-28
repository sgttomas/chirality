#!/usr/bin/env python3
"""PEC-HOLD-001 deterministic operation preflight."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

PROHIBITED = {
    "rely-for-production",
    "dispatch-for-production",
    "promote",
    "consume",
}
ALLOWED = {
    "historical-read-only-inspection",
    "exact-correction-preparation",
    "candidate-validation",
}
RELEASED_TARGETS = {
    (
        "execution/PKG-00_Architecture_Runway_Contracts/1_Working/"
        "DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/ScopeOfWork.md"
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--register", required=True)
    parser.add_argument("--target", required=True)
    parser.add_argument("--clause", action="append", default=[])
    parser.add_argument("--operation", required=True, choices=sorted(PROHIBITED | ALLOWED))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    register = Path(args.register)
    try:
        with register.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            fieldnames = set(reader.fieldnames or [])
            rows = list(reader)
    except (OSError, csv.Error) as exc:
        print(json.dumps({"status": "BLOCK", "reason": f"register unreadable: {exc}"}))
        return 3
    required = {
        "HoldID", "Status", "TargetPath", "TargetClauses", "ProhibitedActs",
        "AllowedActs", "Authority", "ReleaseRule",
    }
    if fieldnames != required:
        print(json.dumps({"status": "BLOCK", "reason": "register malformed"}))
        return 3
    reactivated = [
        row for row in rows if row["TargetPath"] in RELEASED_TARGETS
    ]
    if reactivated:
        print(json.dumps({
            "status": "BLOCK",
            "reason": "released target cannot appear in the active hold register",
            "target": reactivated[0]["TargetPath"],
        }, sort_keys=True))
        return 3
    matches = [
        row for row in rows
        if row["Status"] == "ACTIVE" and row["TargetPath"] == args.target
    ]
    if args.operation in PROHIBITED and matches:
        clauses = set(args.clause)
        held = set(matches[0]["TargetClauses"].split("|"))
        if not clauses or clauses & held:
            print(json.dumps({
                "status": "BLOCK",
                "hold_id": matches[0]["HoldID"],
                "authority": matches[0]["Authority"],
                "operation": args.operation,
            }, sort_keys=True))
            return 4
    print(json.dumps({"status": "ALLOW", "operation": args.operation}, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
