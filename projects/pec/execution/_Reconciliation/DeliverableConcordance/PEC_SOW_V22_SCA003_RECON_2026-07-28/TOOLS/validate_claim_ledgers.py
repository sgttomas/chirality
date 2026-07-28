#!/usr/bin/env python3
"""Validate W1 claim-ledger coverage and produce deterministic fan-in indexes."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path


REPO = Path(__file__).resolve().parents[7]
RUN_ROOT = Path(__file__).resolve().parents[1]
W1 = RUN_ROOT / "WAVES/W1"
INVENTORY = RUN_ROOT / "DELIVERABLE_INVENTORY.csv"
SCHEMA = [
    "ClaimRowID",
    "DeliverableID",
    "ContractPath",
    "Section",
    "LocalID",
    "ClaimClass",
    "ClaimText",
    "AcceptedSourceRefs",
    "Disposition",
    "RepairNeeded",
    "RepairInstruction",
    "SourceState",
    "Notes",
]
DEFINITION = re.compile(
    r"^- \*\*((?:OUT|CLM|REQ|AC|VER|AX|TBD|CON)-\d{3})\*\* — (.+)$"
)
ALLOWED_DISPOSITIONS = {
    "ALIGNED",
    "DOCUMENTED_DIFFERENTLY",
    "ACCEPTED_DIVERGENCE",
    "AUTHORITY_CONFLICT",
    "UNKNOWN",
    "STALE_INPUT",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("deliverable_ids", nargs="+")
    args = parser.parse_args()

    inventory = {
        row["DeliverableID"]: row
        for row in csv.DictReader(INVENTORY.open(encoding="utf-8", newline=""))
    }
    errors: list[str] = []
    census: list[dict[str, str | int]] = []
    repairs: list[dict[str, str]] = []

    for did in args.deliverable_ids:
        if did not in inventory:
            errors.append(f"{did}: absent from inventory")
            continue
        contract = REPO / inventory[did]["DeliverablePath"] / "ScopeOfWork.md"
        definitions = []
        for line in contract.read_text(encoding="utf-8").splitlines():
            match = DEFINITION.match(line)
            if match:
                definitions.append((match.group(1), line.replace("**", "", 2)))
        expected = dict(definitions)

        ledger_path = W1 / f"{did}_claims.csv"
        if not ledger_path.is_file():
            errors.append(f"{did}: missing ledger")
            continue
        with ledger_path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != SCHEMA:
                errors.append(f"{did}: schema mismatch {reader.fieldnames!r}")
            rows = list(reader)

        local_ids = [row["LocalID"] for row in rows]
        if Counter(local_ids) != Counter(expected.keys()):
            errors.append(
                f"{did}: local-ID multiset mismatch "
                f"expected={sorted(expected)} actual={sorted(local_ids)}"
            )
        for row in rows:
            local_id = row["LocalID"]
            if row["DeliverableID"] != did:
                errors.append(f"{did}/{local_id}: DeliverableID mismatch")
            if row["ClaimClass"] != local_id.split("-", 1)[0]:
                errors.append(f"{did}/{local_id}: ClaimClass mismatch")
            if local_id in expected and row["ClaimText"] != expected[local_id]:
                errors.append(f"{did}/{local_id}: ClaimText not exact")
            if row["Disposition"] not in ALLOWED_DISPOSITIONS:
                errors.append(f"{did}/{local_id}: invalid disposition")
            if row["RepairNeeded"] not in {"YES", "NO"}:
                errors.append(f"{did}/{local_id}: invalid RepairNeeded")
            if (
                row["RepairNeeded"] == "YES"
                and row["Disposition"] != "DOCUMENTED_DIFFERENTLY"
            ):
                errors.append(f"{did}/{local_id}: repair/disposition mismatch")
            if row["RepairNeeded"] == "YES":
                repairs.append({key: row[key] for key in SCHEMA})

        dispositions = Counter(row["Disposition"] for row in rows)
        census.append(
            {
                "DeliverableID": did,
                "ContractPath": contract.relative_to(REPO).as_posix(),
                "DefinitionCount": len(definitions),
                "LedgerRowCount": len(rows),
                "ALIGNED": dispositions["ALIGNED"],
                "DOCUMENTED_DIFFERENTLY": dispositions["DOCUMENTED_DIFFERENTLY"],
                "ACCEPTED_DIVERGENCE": dispositions["ACCEPTED_DIVERGENCE"],
                "AUTHORITY_CONFLICT": dispositions["AUTHORITY_CONFLICT"],
                "UNKNOWN": dispositions["UNKNOWN"],
                "STALE_INPUT": dispositions["STALE_INPUT"],
                "RepairCandidateCount": sum(
                    row["RepairNeeded"] == "YES" for row in rows
                ),
            }
        )

    census_path = W1 / "W1_CLAIM_CENSUS.csv"
    with census_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(census[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(census)

    repair_path = W1 / "W1_CHANGED_CLAIM_CANDIDATES.csv"
    with repair_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=SCHEMA, lineterminator="\n")
        writer.writeheader()
        writer.writerows(repairs)

    report = {
        "schema": "pec-sow-w1-ledger-validation/v1",
        "deliverables": args.deliverable_ids,
        "deliverableCount": len(census),
        "definitionCount": sum(int(row["DefinitionCount"]) for row in census),
        "ledgerRowCount": sum(int(row["LedgerRowCount"]) for row in census),
        "repairCandidateCount": len(repairs),
        "authorityConflictCount": sum(
            int(row["AUTHORITY_CONFLICT"]) for row in census
        ),
        "unknownCount": sum(int(row["UNKNOWN"]) for row in census),
        "errors": errors,
        "valid": not errors,
    }
    report_path = W1 / "W1_LEDGER_VALIDATION.json"
    report_path.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    raise SystemExit(0 if not errors else 1)


if __name__ == "__main__":
    main()
