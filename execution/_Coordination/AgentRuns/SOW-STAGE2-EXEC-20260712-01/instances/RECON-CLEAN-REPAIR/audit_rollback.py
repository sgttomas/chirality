#!/usr/bin/env python3
"""Audit the accepted rollback corpus against the frozen Stage-2 census."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
INSTANCE = Path(__file__).resolve().parent
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
BASIS = "715f618e93528d626a73d2134781e8c9c27f6c90"
SOURCES = (
    "snapshots/P4_PILOTS/integration/postmerge/ROLLBACK_MANIFEST.tsv",
    "snapshots/W_A1/integration/postmerge/ROLLBACK_MANIFEST.tsv",
    "snapshots/W_A2/integration/postmerge/ROLLBACK_MANIFEST.tsv",
    "snapshots/W_A3/integration/postmerge/ROLLBACK_MANIFEST.tsv",
    "../SOW-PACKAGE-BATCH-ADOPTION-20260714-01/snapshots/reconciliation/ROLLBACK_MANIFEST.tsv",
    "snapshots/W_P1/PKG03-preintegration-accepted/ROLLBACK_MANIFEST.tsv",
    "snapshots/W_P1/PKG04-preintegration-r1/ROLLBACK_MANIFEST.tsv",
    "snapshots/I0/preintegration-r1/ROLLBACK_MANIFEST.tsv",
    "snapshots/W_P2/preintegration/ROLLBACK_MANIFEST.tsv",
    "snapshots/W_P3/preintegration/ROLLBACK_MANIFEST.tsv",
    "snapshots/W_P4/preintegration/ROLLBACK_MANIFEST.tsv",
)
LEGACY_COLUMNS = {
    "Datasheet.md": "datasheet_sha256",
    "Specification.md": "specification_sha256",
    "Guidance.md": "guidance_sha256",
    "Procedure.md": "procedure_sha256",
}


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def operation(row: dict[str, str]) -> str:
    raw = row.get("action", row.get("operation", ""))
    return {"D": "DELETE", "A": "ADD"}.get(raw, raw)


def content_hash(row: dict[str, str]) -> str:
    if row.get("sha256"):
        return row["sha256"]
    return row["before_sha256"] if operation(row) == "DELETE" else row["after_sha256"]


def main() -> int:
    errors: list[str] = []
    census = rows(RUN / "basis/CENSUS_MANIFEST.tsv")
    converted = {
        member["path"]: member
        for member in census
        if not (member["project"] == "PIP" and member["package"] == "PKG-00")
    }
    by_directory: dict[str, list[dict[str, str]]] = defaultdict(list)
    source_rows: list[dict[str, object]] = []
    seen_paths: set[str] = set()
    for relative in SOURCES:
        source = (RUN / relative).resolve()
        if not source.is_file():
            errors.append(f"missing rollback source: {relative}")
            continue
        data = source.read_bytes()
        manifest_rows = rows(source)
        source_rows.append({"path": str(source.relative_to(ROOT)), "rows": len(manifest_rows), "sha256": hashlib.sha256(data).hexdigest()})
        for row in manifest_rows:
            path = row["path"]
            if path in seen_paths:
                errors.append(f"duplicate rollback path: {path}")
            seen_paths.add(path)
            by_directory[str(Path(path).parent)].append(row)

    for directory, member in converted.items():
        manifest_rows = by_directory.get(directory, [])
        if len(manifest_rows) != 5:
            errors.append(f"rollback row count {len(manifest_rows)}: {directory}")
            continue
        by_name = {Path(row["path"]).name: row for row in manifest_rows}
        if set(by_name) != {"ScopeOfWork.md", *LEGACY_COLUMNS}:
            errors.append(f"rollback filename set mismatch: {directory}")
            continue
        sow = by_name["ScopeOfWork.md"]
        sow_operation = operation(sow)
        if sow_operation != "DELETE":
            errors.append(f"ScopeOfWork rollback operation {sow_operation}: {directory}")
        basis_blob = subprocess.check_output(["git", "show", f"{BASIS}:{directory}/ScopeOfWork.md"], cwd=ROOT)
        if content_hash(sow) != hashlib.sha256(basis_blob).hexdigest():
            errors.append(f"ScopeOfWork rollback hash mismatch: {directory}")
        for name, column in LEGACY_COLUMNS.items():
            legacy = by_name[name]
            legacy_operation = operation(legacy)
            if legacy_operation not in {"ADD", "RESTORE"}:
                errors.append(f"legacy rollback operation {legacy_operation}: {directory}/{name}")
            if content_hash(legacy) != member[column]:
                errors.append(f"legacy rollback hash mismatch: {directory}/{name}")

    unexpected = sorted(set(by_directory) - set(converted))
    if unexpected:
        errors.append(f"unexpected rollback directories: {len(unexpected)}")
    if len(seen_paths) != 730:
        errors.append(f"rollback path total {len(seen_paths)}, expected 730")
    if len(by_directory) != 146:
        errors.append(f"rollback member total {len(by_directory)}, expected 146")

    with (INSTANCE / "ROLLBACK_SOURCES.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["path", "rows", "sha256"], delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(source_rows)
    result = {
        "schema": "chirality-sow-clean-repair-rollback-audit/v1",
        "basis": BASIS,
        "verdict": "PASS" if not errors else "BLOCKED",
        "errors": errors,
        "sources": len(source_rows),
        "rows": len(seen_paths),
        "members": len(by_directory),
        "operations": dict(Counter(operation(row) for group in by_directory.values() for row in group)),
    }
    (INSTANCE / "ROLLBACK_AUDIT.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
