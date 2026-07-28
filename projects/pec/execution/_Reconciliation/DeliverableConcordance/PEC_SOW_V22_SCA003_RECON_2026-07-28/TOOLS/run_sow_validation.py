#!/usr/bin/env python3
"""Run the deterministic ScopeOfWork validation suite over the active PEC corpus."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import subprocess
from pathlib import Path


REPO = Path(__file__).resolve().parents[7]
RUN_ROOT = Path(__file__).resolve().parents[1]
INVENTORY = RUN_ROOT / "DELIVERABLE_INVENTORY.csv"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=REPO,
        check=False,
        capture_output=True,
        text=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_dir", type=Path)
    args = parser.parse_args()
    output_dir = args.output_dir
    if not output_dir.is_absolute():
        output_dir = REPO / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    rows = list(csv.DictReader(INVENTORY.open(encoding="utf-8", newline="")))
    active = [row for row in rows if row["ProductionFormat"] == "SOW_V1"]
    summary: list[dict[str, str | int]] = []

    for row in active:
        did = row["DeliverableID"]
        target = REPO / row["DeliverablePath"]
        destination = output_dir / did
        destination.mkdir(exist_ok=True)

        validation = run(
            [
                "python3",
                "tools/scope_of_work/validate_scope_of_work.py",
                "--json",
                str(target),
            ]
        )
        (destination / "scope_validation.json").write_text(
            validation.stdout, encoding="utf-8"
        )
        (destination / "scope_validation.stderr.txt").write_text(
            validation.stderr, encoding="utf-8"
        )

        checklist_path = destination / "review_checklist.json"
        checklist = run(
            [
                "python3",
                "tools/scope_of_work/derive_review_checklist.py",
                "--output",
                str(checklist_path),
                str(target),
            ]
        )
        (destination / "review_checklist.stderr.txt").write_text(
            checklist.stderr, encoding="utf-8"
        )

        boundary_path = destination / "boundary_owner_resolution.json"
        boundary = run(
            [
                "python3",
                "tools/scope_of_work/check_boundary_owner_resolution.py",
                "--json",
                str(boundary_path),
                "--show-not-checkable",
                str(target),
            ]
        )
        (destination / "boundary_owner_resolution.stdout.txt").write_text(
            boundary.stdout, encoding="utf-8"
        )
        (destination / "boundary_owner_resolution.stderr.txt").write_text(
            boundary.stderr, encoding="utf-8"
        )

        consistency_path = destination / "deliverable_consistency.json"
        consistency = run(
            [
                "python3",
                "tools/validation/scan_deliverable_consistency.py",
                "--output-json",
                str(consistency_path),
                "--focus-doc",
                "ScopeOfWork.md",
                "--production-format",
                "SOW_V1",
                str(target),
            ]
        )
        (destination / "deliverable_consistency.stdout.txt").write_text(
            consistency.stdout, encoding="utf-8"
        )
        (destination / "deliverable_consistency.stderr.txt").write_text(
            consistency.stderr, encoding="utf-8"
        )

        summary.append(
            {
                "DeliverableID": did,
                "ScopeOfWorkSHA256": sha256(target / "ScopeOfWork.md"),
                "ScopeValidationExit": validation.returncode,
                "ReviewChecklistExit": checklist.returncode,
                "BoundaryResolutionExit": boundary.returncode,
                "ConsistencyScanExit": consistency.returncode,
            }
        )

    fields = list(summary[0])
    summary_path = output_dir / "VALIDATION_SUMMARY.csv"
    with summary_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(summary)

    failed = [
        row
        for row in summary
        if any(
            int(row[key]) != 0
            for key in (
                "ScopeValidationExit",
                "ReviewChecklistExit",
                "BoundaryResolutionExit",
                "ConsistencyScanExit",
            )
        )
    ]
    run_summary = {
        "inventory": str(INVENTORY.relative_to(REPO)),
        "outputDirectory": str(output_dir.relative_to(REPO)),
        "activeContractCount": len(summary),
        "allToolExitCodesZero": not failed,
        "failedDeliverables": [row["DeliverableID"] for row in failed],
        "summarySHA256": sha256(summary_path),
    }
    (output_dir / "RUN_SUMMARY.json").write_text(
        json.dumps(run_summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(run_summary, indent=2, sort_keys=True))
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
