#!/usr/bin/env python3
"""Build the frozen PEC deliverable/SOW inventory for D-PEC-69."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path


REPO = Path(__file__).resolve().parents[7]
EXECUTION = REPO / "projects/pec/execution"
RUN_ROOT = Path(__file__).resolve().parents[1]
DELIVERABLES = EXECUTION / "_Decomposition/Deliverables.csv"

EXPECTED = {
    "DEL-00-01",
    "DEL-03-06",
    "DEL-04-01",
    "DEL-04-02",
    "DEL-08-01",
    "DEL-08-03",
    "DEL-08-04",
    "DEL-10-01",
    "DEL-10-10",
    "DEL-10-11",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lifecycle(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("**Current State:**"):
            return line.split(":", 1)[1].strip()
    raise ValueError(f"missing lifecycle state: {path}")


def rel(path: Path) -> str:
    return path.relative_to(REPO).as_posix()


def main() -> None:
    rows = list(csv.DictReader(DELIVERABLES.open(encoding="utf-8", newline="")))
    dirs = {
        path.name.split("_", 1)[0]: path
        for path in EXECUTION.glob("PKG-*/1_Working/DEL-*")
        if path.is_dir()
    }
    if len(rows) != 64 or len(dirs) != 64:
        raise SystemExit(f"census mismatch: rows={len(rows)} dirs={len(dirs)}")

    inventory_path = RUN_ROOT / "DELIVERABLE_INVENTORY.csv"
    fields = [
        "DeliverableID",
        "PackageID",
        "DeliverablePath",
        "LifecycleState",
        "ProductionFormat",
        "ScopeOfWorkSHA256",
        "ExpectedAffected",
        "SelectionBasis",
    ]
    manifest_lines: list[str] = []
    with inventory_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            did = row["DeliverableID"]
            deliverable_dir = dirs[did]
            status_path = deliverable_dir / "_STATUS.md"
            sow_path = deliverable_dir / "ScopeOfWork.md"
            has_sow = sow_path.is_file()
            sow_hash = sha256(sow_path) if has_sow else ""
            if has_sow:
                manifest_lines.append(f"{sow_hash}  {rel(sow_path)}")
            writer.writerow(
                {
                    "DeliverableID": did,
                    "PackageID": row["PackageID"],
                    "DeliverablePath": rel(deliverable_dir),
                    "LifecycleState": lifecycle(status_path),
                    "ProductionFormat": "SOW_V1" if has_sow else "NONE_AT_OPEN",
                    "ScopeOfWorkSHA256": sow_hash,
                    "ExpectedAffected": "YES" if did in EXPECTED else "NO",
                    "SelectionBasis": (
                        "D-PEC-69 expected population; execution-time semantic scan governs"
                        if did in EXPECTED
                        else "full-corpus control member"
                    ),
                }
            )

    if len(manifest_lines) != 32:
        raise SystemExit(f"active SOW census mismatch: {len(manifest_lines)}")
    manifest_path = RUN_ROOT / "PRE_REPAIR_MANIFEST.sha256"
    manifest_path.write_text(
        "\n".join(sorted(manifest_lines, key=lambda line: line.split("  ", 1)[1])) + "\n",
        encoding="utf-8",
    )

    print(f"inventory={inventory_path}")
    print(f"deliverables={len(rows)} active_sow={len(manifest_lines)}")
    print(f"expected_affected={len(EXPECTED)}")
    print(f"manifest_sha256={sha256(manifest_path)}")


if __name__ == "__main__":
    main()
