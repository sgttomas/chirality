#!/usr/bin/env python3
"""Build deterministic read-only W-P1 preflight inventories."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
OUT = RUN / "snapshots/W_P1/preflight"
P3 = RUN / "snapshots/P3_MANIFEST/EXECUTION_MANIFEST.tsv"
P4 = RUN / "snapshots/P4_PILOTS/integration/postmerge/POST_STATE_LEDGER.tsv"
DISPATCH = "69ac259a7113d5a838fb22aa2e84df0e0f109713"

SOURCE_FILES = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROL_FILES = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
BINDING_FILES = SOURCE_FILES + CONTROL_FILES


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def section_items(path: Path, heading: str) -> str:
    lines = path.read_text().splitlines()
    in_section = False
    items: list[str] = []
    for line in lines:
        if line == heading:
            in_section = True
            continue
        if in_section and line.startswith("## "):
            break
        if in_section and line.startswith("- "):
            items.append(line[2:].strip())
    return ", ".join(items)


def dependency_rows(path: Path) -> object:
    if not path.exists():
        return "MISSING"
    with path.open(newline="") as handle:
        return max(sum(1 for _ in csv.reader(handle)) - 1, 0)


def current_state(path: Path) -> str:
    for line in path.read_text().splitlines():
        if line.startswith("**Current State:**"):
            return line.split("**Current State:**", 1)[1].strip().strip("`")
    return "UNRESOLVED"


def validate(deliverable: Path) -> dict[str, object]:
    proc = subprocess.run(
        ["python3", "tools/scope_of_work/validate_scope_of_work.py", str(deliverable), "--json"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    payload = json.loads(proc.stdout) if proc.stdout.strip() else {}
    return {
        "exit_code": proc.returncode,
        "format": payload.get("format", "UNRESOLVED"),
        "valid": payload.get("valid", False),
        "issues": json.dumps(payload.get("issues", []), separators=(",", ":")),
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    p3_rows = read_tsv(P3)
    population = [
        row
        for row in p3_rows
        if row["project"] == "PIP"
        and row["package"] in {"PKG-00", "PKG-01", "PKG-02", "PKG-03", "PKG-04"}
    ]
    selected = [row for row in population if row["deliverable_id"] != "DEL-01-01"]
    excluded = [row for row in population if row["deliverable_id"] == "DEL-01-01"]
    if len(selected) != 30 or len(excluded) != 1:
        raise SystemExit(f"population mismatch: selected={len(selected)}, excluded={len(excluded)}")

    package_counts = Counter(row["package"] for row in selected)
    expected_counts = {"PKG-00": 8, "PKG-01": 3, "PKG-02": 5, "PKG-03": 8, "PKG-04": 6}
    if dict(sorted(package_counts.items())) != expected_counts:
        raise SystemExit(f"package mismatch: {dict(sorted(package_counts.items()))}")

    managers = {pkg: f"WORKING-P1-{pkg.replace('-', '')}" for pkg in expected_counts}
    manifest_rows: list[dict[str, object]] = []
    binding_rows: list[dict[str, object]] = []
    validator_rows: list[dict[str, object]] = []
    missing_bindings: list[str] = []
    p3_mismatches: list[str] = []
    total_dependency_rows = 0

    manifest_fields = [
        "project", "package", "manager", "deliverable_id", "live_path", "lifecycle", "pilot", "issued",
        "live_format", "datasheet_sha256", "specification_sha256", "guidance_sha256", "procedure_sha256",
        "status_sha256", "context_sha256", "references_sha256", "dependencies_md_sha256",
        "dependencies_csv_sha256", "dependency_rows", "scope_refs", "objective_refs", "decomposition_basis",
        "candidate_path", "author_evidence", "verifier_evidence", "integration_delta", "p3_source_status_match",
        "binding_state",
    ]

    for row in selected:
        rel = Path(row["path"])
        live = ROOT / rel
        result = validate(live)
        validator_rows.append(
            {
                "package": row["package"],
                "deliverable_id": row["deliverable_id"],
                "live_path": rel.as_posix(),
                **result,
            }
        )
        live_hashes: dict[str, str] = {}
        for name in BINDING_FILES:
            path = live / name
            state = "PRESENT" if path.is_file() else "MISSING"
            digest = sha(path) if path.is_file() else "MISSING"
            live_hashes[name] = digest
            binding_rows.append(
                {
                    "package": row["package"],
                    "deliverable_id": row["deliverable_id"],
                    "live_path": rel.as_posix(),
                    "binding": name,
                    "state": state,
                    "sha256": digest,
                }
            )
            if state == "MISSING":
                missing_bindings.append(f"{row['deliverable_id']}:{name}")

        p3_expected = {
            "Datasheet.md": row["datasheet_sha256"],
            "Specification.md": row["specification_sha256"],
            "Guidance.md": row["guidance_sha256"],
            "Procedure.md": row["procedure_sha256"],
            "_STATUS.md": row["status_sha256"],
        }
        p3_match = all(live_hashes[name] == expected for name, expected in p3_expected.items())
        if not p3_match:
            p3_mismatches.append(row["deliverable_id"])

        dep_rows = dependency_rows(live / "Dependencies.csv")
        if isinstance(dep_rows, int):
            total_dependency_rows += dep_rows
        package_token = row["package"].replace("-", "")
        deliverable = row["deliverable_id"]
        manifest_rows.append(
            {
                "project": "PIP",
                "package": row["package"],
                "manager": managers[row["package"]],
                "deliverable_id": deliverable,
                "live_path": rel.as_posix(),
                "lifecycle": current_state(live / "_STATUS.md"),
                "pilot": row["pilot"],
                "issued": row["issued"],
                "live_format": result["format"],
                "datasheet_sha256": live_hashes["Datasheet.md"],
                "specification_sha256": live_hashes["Specification.md"],
                "guidance_sha256": live_hashes["Guidance.md"],
                "procedure_sha256": live_hashes["Procedure.md"],
                "status_sha256": live_hashes["_STATUS.md"],
                "context_sha256": live_hashes["_CONTEXT.md"],
                "references_sha256": live_hashes["_REFERENCES.md"],
                "dependencies_md_sha256": live_hashes["_DEPENDENCIES.md"],
                "dependencies_csv_sha256": live_hashes["Dependencies.csv"],
                "dependency_rows": dep_rows,
                "scope_refs": section_items(live / "_CONTEXT.md", "## Scope Coverage"),
                "objective_refs": section_items(live / "_CONTEXT.md", "## Objective Support"),
                "decomposition_basis": f"projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@{DISPATCH}",
                "candidate_path": f"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_P1/PIP-{package_token}/{deliverable}/ScopeOfWork.md",
                "author_evidence": f"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/{managers[row['package']]}/children/AUTHOR-{deliverable}",
                "verifier_evidence": f"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/{managers[row['package']]}/children/VERIFY-{deliverable}",
                "integration_delta": "A ScopeOfWork.md;D Datasheet.md;D Specification.md;D Guidance.md;D Procedure.md",
                "p3_source_status_match": str(p3_match).lower(),
                "binding_state": "COMPLETE" if all(live_hashes[name] != "MISSING" for name in BINDING_FILES) else "INCOMPLETE",
            }
        )

    write_tsv(OUT / "P1_MANIFEST.tsv", manifest_fields, manifest_rows)
    write_tsv(
        OUT / "EXPECTED_LIVE_BINDINGS.tsv",
        ["package", "deliverable_id", "live_path", "binding", "state", "sha256"],
        binding_rows,
    )
    write_tsv(
        OUT / "VALIDATOR_RESULTS.tsv",
        ["package", "deliverable_id", "live_path", "exit_code", "format", "valid", "issues"],
        validator_rows,
    )

    excluded_row = excluded[0]
    excluded_live = ROOT / excluded_row["path"]
    excluded_result = validate(excluded_live)
    excluded_fields = [
        "project", "package", "deliverable_id", "live_path", "lifecycle", "pilot", "issued", "format", "valid",
        "datasheet_sha256", "specification_sha256", "guidance_sha256", "procedure_sha256", "status_sha256",
        "context_sha256", "references_sha256", "dependencies_md_sha256", "dependencies_csv_sha256", "dependency_rows",
        "live_sow", "p3_source_status_match", "disposition",
    ]
    excluded_hashes = {name: sha(excluded_live / name) for name in BINDING_FILES}
    excluded_match = all(
        excluded_hashes[name] == excluded_row[key]
        for name, key in {
            "Datasheet.md": "datasheet_sha256",
            "Specification.md": "specification_sha256",
            "Guidance.md": "guidance_sha256",
            "Procedure.md": "procedure_sha256",
            "_STATUS.md": "status_sha256",
        }.items()
    )
    write_tsv(
        OUT / "EXCLUDED_ISSUED.tsv",
        excluded_fields,
        [
            {
                "project": "PIP", "package": excluded_row["package"], "deliverable_id": excluded_row["deliverable_id"],
                "live_path": excluded_row["path"], "lifecycle": current_state(excluded_live / "_STATUS.md"),
                "pilot": excluded_row["pilot"], "issued": excluded_row["issued"], "format": excluded_result["format"],
                "valid": excluded_result["valid"], "datasheet_sha256": excluded_hashes["Datasheet.md"],
                "specification_sha256": excluded_hashes["Specification.md"], "guidance_sha256": excluded_hashes["Guidance.md"],
                "procedure_sha256": excluded_hashes["Procedure.md"], "status_sha256": excluded_hashes["_STATUS.md"],
                "context_sha256": excluded_hashes["_CONTEXT.md"], "references_sha256": excluded_hashes["_REFERENCES.md"],
                "dependencies_md_sha256": excluded_hashes["_DEPENDENCIES.md"],
                "dependencies_csv_sha256": excluded_hashes["Dependencies.csv"],
                "dependency_rows": dependency_rows(excluded_live / "Dependencies.csv"),
                "live_sow": str((excluded_live / "ScopeOfWork.md").exists()).lower(),
                "p3_source_status_match": str(excluded_match).lower(),
                "disposition": "EXCLUDED_READ_ONLY_H1_PARKED",
            }
        ],
    )

    p4_rows = [row for row in read_tsv(P4) if row["project"] == "PIP"]
    p3_by_id = {row["deliverable_id"]: row for row in p3_rows if row["project"] == "PIP"}
    predecessor_rows: list[dict[str, object]] = []
    for row in p4_rows:
        live = ROOT / p3_by_id[row["deliverable_id"]]["path"]
        legacy_present = sum((live / name).exists() for name in SOURCE_FILES)
        sow_hash = sha(live / "ScopeOfWork.md") if (live / "ScopeOfWork.md").exists() else "MISSING"
        status_hash = sha(live / "_STATUS.md")
        predecessor_rows.append(
            {
                "deliverable_id": row["deliverable_id"], "live_path": p3_by_id[row["deliverable_id"]]["path"],
                "expected_sow_sha256": row["candidate_sha256"], "live_sow_sha256": sow_hash,
                "expected_status_sha256": row["status_sha256"], "live_status_sha256": status_hash,
                "lifecycle": current_state(live / "_STATUS.md"), "format": validate(live)["format"],
                "legacy_files": legacy_present,
                "verdict": "PASS" if sow_hash == row["candidate_sha256"] and status_hash == row["status_sha256"] and legacy_present == 0 else "FAIL",
            }
        )
    write_tsv(
        OUT / "PREDECESSOR_RESULTS.tsv",
        ["deliverable_id", "live_path", "expected_sow_sha256", "live_sow_sha256", "expected_status_sha256", "live_status_sha256", "lifecycle", "format", "legacy_files", "verdict"],
        predecessor_rows,
    )

    summary = {
        "wave": "P1",
        "dispatch_basis": DISPATCH,
        "selected_members": len(selected),
        "package_counts": dict(sorted(package_counts.items())),
        "expected_live_bindings": len(selected) * len(BINDING_FILES),
        "present_live_bindings": sum(row["state"] == "PRESENT" for row in binding_rows),
        "missing_live_bindings": len(missing_bindings),
        "missing_binding_details": missing_bindings,
        "legacy_source_bindings_verified": len(selected) * len(SOURCE_FILES),
        "status_bindings_verified": len(selected),
        "p3_source_status_mismatches": p3_mismatches,
        "control_bindings_expected": len(selected) * 4,
        "control_bindings_present": len(selected) * 4 - len(missing_bindings),
        "dependency_rows_present_registers": total_dependency_rows,
        "selected_lifecycle_counts": dict(Counter(row["lifecycle"] for row in manifest_rows)),
        "selected_format_counts": dict(Counter(row["live_format"] for row in manifest_rows)),
        "selected_live_sow": sum((ROOT / row["live_path"] / "ScopeOfWork.md").exists() for row in manifest_rows),
        "excluded_issued_members": 1,
        "accepted_piping_predecessors": len(predecessor_rows),
        "accepted_piping_predecessor_failures": sum(row["verdict"] != "PASS" for row in predecessor_rows),
        "verdict": "DECISION_REQUIRED" if missing_bindings else "PASS",
    }
    (OUT / "SUMMARY.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")


def bind_snapshot() -> None:
    rows: list[dict[str, object]] = []
    for path in sorted(OUT.rglob("*")):
        if not path.is_file() or path.name == "MANIFEST.tsv":
            continue
        rel = path.relative_to(OUT).as_posix()
        data_rows: object = "not_applicable"
        if path.suffix == ".tsv":
            data_rows = max(len(path.read_text().splitlines()) - 1, 0)
        rows.append(
            {
                "artifact": rel,
                "sha256": sha(path),
                "bytes": path.stat().st_size,
                "data_rows": data_rows,
                "binding_status": "BOUND",
            }
        )
    write_tsv(
        OUT / "MANIFEST.tsv",
        ["artifact", "sha256", "bytes", "data_rows", "binding_status"],
        rows,
    )


if __name__ == "__main__":
    main()
    bind_snapshot()
