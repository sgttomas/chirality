#!/usr/bin/env python3
"""Reproduce final Stage-2 closure facts from an exact detached-main worktree."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path


LEGACY_FILES = ("Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md")
EXPECTED_DIGEST = "b6eca2504a5d7551d96f7c0978ba6b4bc48b0e36c4d51792177fdd7a91e8df31"
PRE_REPAIR_BASIS = "715f618e93528d626a73d2134781e8c9c27f6c90"
ROLLBACK_SOURCES = (
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


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, data: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


def operation(row: dict[str, str]) -> str:
    value = row.get("action", row.get("operation", ""))
    return {"D": "DELETE", "A": "ADD"}.get(value, value)


def content_hash(row: dict[str, str]) -> str:
    if row.get("sha256"):
        return row["sha256"]
    return row["before_sha256"] if operation(row) == "DELETE" else row["after_sha256"]


def git_blob(root: Path, commit: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=root)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    root, out = args.root.resolve(), args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    run = root / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
    errors: list[str] = []

    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    if head != "79de30d83b91a2ab468a3f17536a5233c2f85fe7":
        errors.append(f"wrong exact-main basis: {head}")

    census = rows(run / "basis/CENSUS_MANIFEST.tsv")
    expected_paths = [row["path"] for row in census]
    live_paths = sorted(
        str(path.parent.relative_to(root))
        for project in ("chirality-app-dev", "chirality-piping")
        for path in (root / f"projects/{project}/execution").glob("PKG-*/1_Working/DEL-*/_STATUS.md")
    )
    path_digest = digest(("\n".join(live_paths) + "\n").encode())
    if live_paths != sorted(expected_paths):
        errors.append("live census membership differs from frozen basis")
    if path_digest != EXPECTED_DIGEST:
        errors.append(f"live census digest mismatch: {path_digest}")

    population: list[dict[str, object]] = []
    formats: Counter[str] = Counter()
    lifecycle: Counter[str] = Counter()
    residue: list[dict[str, str]] = []
    status_mismatches: list[str] = []
    validation_failures: list[str] = []
    for member in census:
        rel = member["path"]
        directory = root / rel
        status = (directory / "_STATUS.md").read_bytes()
        status_ok = digest(status) == member["status_sha256"]
        if not status_ok:
            status_mismatches.append(rel)
        match = re.search(rb"\*\*Current State:\*\*\s*([A-Z_]+)", status)
        state = match.group(1).decode() if match else "UNKNOWN"
        lifecycle[state] += 1
        has_sow = (directory / "ScopeOfWork.md").is_file()
        legacy_present = [name for name in LEGACY_FILES if (directory / name).is_file()]
        if has_sow and not legacy_present:
            fmt = "SOW_V1"
        elif not has_sow and len(legacy_present) == 4:
            fmt = "LEGACY_FOUR_DOC"
        elif has_sow and len(legacy_present) == 4:
            fmt = "MIGRATION_DUAL"
        else:
            fmt = "INVALID"
        formats[fmt] += 1
        valid = True
        if has_sow:
            proc = subprocess.run(
                [sys.executable, "tools/scope_of_work/validate_scope_of_work.py", "--json", rel],
                cwd=root, text=True, capture_output=True, check=False,
            )
            valid = proc.returncode == 0
            if not valid:
                validation_failures.append(rel)
            text = (directory / "ScopeOfWork.md").read_text(encoding="utf-8")
            hits = [token for token in ("sow-source-begin", "sow-source-end", "migration-authority:", "pilot-variance:", "issued-preparation-") if token in text]
            if re.search(r"\bmigration candidate\b", text, re.IGNORECASE):
                hits.append("migration candidate")
            if hits:
                residue.append({"path": rel + "/ScopeOfWork.md", "tokens": ",".join(hits)})
        excluded = member["project"] == "PIP" and member["package"] == "PKG-00"
        population.append({
            "project": member["project"], "package": member["package"],
            "deliverable_id": member["deliverable_id"], "path": rel,
            "excluded_pkg00": str(excluded).lower(), "format": fmt,
            "valid": str(valid).lower(), "lifecycle": state,
            "status_hash_preserved": str(status_ok).lower(),
        })

    converted = {m["path"]: m for m in census if not (m["project"] == "PIP" and m["package"] == "PKG-00")}
    exemptions = {m["path"]: m for m in census if m["project"] == "PIP" and m["package"] == "PKG-00"}
    for rel in converted:
        row = next(item for item in population if item["path"] == rel)
        if row["format"] != "SOW_V1" or row["valid"] != "true":
            errors.append(f"converted member is not valid SOW_V1: {rel}")
    for rel in exemptions:
        row = next(item for item in population if item["path"] == rel)
        if row["format"] != "LEGACY_FOUR_DOC":
            errors.append(f"PKG-00 exemption format mismatch: {rel}")
    if residue:
        errors.append(f"production migration residue: {len(residue)} members")
    if status_mismatches:
        errors.append(f"status hash mismatch: {len(status_mismatches)} members")

    # Reproduce the registered clean-production finalization bridge for all 57 repairs.
    repair_manifest = rows(run / "snapshots/CONVERSION_CLOSURE/repair_preintegration/PROPOSED_CHANGE_MANIFEST.tsv")
    sys.path.insert(0, str(root / "tools/scope_of_work"))
    from finalize_scope_of_work import finalize_candidate_text  # type: ignore
    repair_errors: list[str] = []
    repair_rows: list[dict[str, object]] = []
    for item in repair_manifest:
        rel = item["path"]
        report_path = root / item["finalization_report_path"]
        report = json.loads(report_path.read_text(encoding="utf-8"))
        old = git_blob(root, PRE_REPAIR_BASIS, rel)
        current = (root / rel).read_bytes()
        reproduced, reproduced_report = finalize_candidate_text(Path(rel), old.decode("utf-8"))
        row_errors: list[str] = []
        if digest(old) != item["before_sha256"] or digest(old) != report["evidence_candidate_sha256"]:
            row_errors.append("candidate_hash")
        if digest(current) != item["after_sha256"] or digest(current) != report["production_scope_of_work_sha256"]:
            row_errors.append("production_hash")
        if reproduced.encode() != current or reproduced_report != report:
            row_errors.append("reproduction")
        if digest(report_path.read_bytes()) != item["finalization_report_sha256"]:
            row_errors.append("report_hash")
        if row_errors:
            repair_errors.append(f"{rel}: {','.join(row_errors)}")
        repair_rows.append({"path": rel, "candidate_sha256": digest(old), "production_sha256": digest(current), "report_sha256": digest(report_path.read_bytes()), "source_blocks": report["source_block_count"], "verdict": "PASS" if not row_errors else "BLOCKED"})
    if repair_errors:
        errors.append(f"repair finalization bridge failures: {len(repair_errors)}")

    # Aggregate and validate every accepted inverse manifest.
    rollback_errors: list[str] = []
    rollback_sources: list[dict[str, object]] = []
    rollback_by_dir: dict[str, list[dict[str, str]]] = defaultdict(list)
    seen_paths: set[str] = set()
    for relative in ROLLBACK_SOURCES:
        source = (run / relative).resolve()
        data = source.read_bytes()
        manifest_rows = rows(source)
        rollback_sources.append({"path": str(source.relative_to(root)), "rows": len(manifest_rows), "sha256": digest(data)})
        for row in manifest_rows:
            rel = row["path"]
            if rel in seen_paths:
                rollback_errors.append(f"duplicate path: {rel}")
            seen_paths.add(rel)
            rollback_by_dir[str(Path(rel).parent)].append(row)
    for directory, member in converted.items():
        group = rollback_by_dir.get(directory, [])
        by_name = {Path(row["path"]).name: row for row in group}
        if len(group) != 5 or set(by_name) != {"ScopeOfWork.md", *LEGACY_FILES}:
            rollback_errors.append(f"wrong five-path inverse set: {directory}")
            continue
        sow = by_name["ScopeOfWork.md"]
        if operation(sow) != "DELETE" or content_hash(sow) != digest(git_blob(root, PRE_REPAIR_BASIS, f"{directory}/ScopeOfWork.md")):
            rollback_errors.append(f"SOW inverse mismatch: {directory}")
        for name, column in LEGACY_COLUMNS.items():
            row = by_name[name]
            if operation(row) not in {"ADD", "RESTORE"} or content_hash(row) != member[column]:
                rollback_errors.append(f"legacy inverse mismatch: {directory}/{name}")
    if set(rollback_by_dir) != set(converted) or len(seen_paths) != 730:
        rollback_errors.append("rollback population/path total mismatch")
    if rollback_errors:
        errors.append(f"rollback audit failures: {len(rollback_errors)}")

    # Inventory live legacy contracts and every active compatibility caller.
    surface_rows: list[dict[str, object]] = []
    for rel in sorted(exemptions):
        contract_binding = "\n".join(f"{name}\t{digest((root / rel / name).read_bytes())}" for name in LEGACY_FILES) + "\n"
        surface_rows.append({"surface_type": "LEGACY_CONTRACT", "surface": rel, "current_sha256": digest(contract_binding.encode()), "disposition": "RETAIN", "required_by": "PKG00_CURRENT_RUNTIME", "retirement_effect": "invalidates ruled PKG-00 context unless converted or separately amended"})
    caller_manifest = rows(run / "basis/CALLER_MANIFEST.tsv")
    legacy_terms = ("LEGACY_FOUR_DOC", "Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md", "four-documents", "check_four_documents")
    for item in caller_manifest:
        rel = item["surface"]
        path = root / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if item["disposition"] == "RETAIN_LEGACY" or any(term in text for term in legacy_terms):
            if rel.startswith("skills/four-documents/"):
                kind, required = "LEGACY_SKILL", "PKG00_AND_ROLLBACK_SUPPORT"
            elif rel == "tools/validation/check_four_documents.sh":
                kind, required = "LEGACY_VALIDATOR", "PKG00_AND_ROLLBACK_SUPPORT"
            else:
                kind, required = "ACTIVE_COMPATIBILITY_CALLER", "PKG00_RUNTIME_OR_ROLLBACK"
            surface_rows.append({"surface_type": kind, "surface": rel, "current_sha256": digest(path.read_bytes()), "disposition": item["disposition"], "required_by": required, "retirement_effect": "requires caller-specific replacement/removal proof and regression coverage"})

    write_tsv(out / "POPULATION.tsv", population, ["project", "package", "deliverable_id", "path", "excluded_pkg00", "format", "valid", "lifecycle", "status_hash_preserved"])
    write_tsv(out / "PRODUCTION_RESIDUE.tsv", residue, ["path", "tokens"])
    write_tsv(out / "REPAIR_REPRODUCTION.tsv", repair_rows, ["path", "candidate_sha256", "production_sha256", "report_sha256", "source_blocks", "verdict"])
    write_tsv(out / "ROLLBACK_SOURCES.tsv", rollback_sources, ["path", "rows", "sha256"])
    write_tsv(out / "LEGACY_SURFACES.tsv", surface_rows, ["surface_type", "surface", "current_sha256", "disposition", "required_by", "retirement_effect"])
    result = {
        "schema": "chirality-sow-final-closure-evaluation/v1",
        "basis": head,
        "verdict": "PASS" if not errors else "BLOCKED",
        "errors": errors,
        "census": {"members": len(live_paths), "app": sum(p.startswith("projects/chirality-app-dev/") for p in live_paths), "piping": sum(p.startswith("projects/chirality-piping/") for p in live_paths), "path_digest": path_digest, "status_hash_mismatches": status_mismatches, "lifecycle": dict(lifecycle)},
        "formats": dict(formats),
        "conversion_population": {"members": len(converted), "valid_sow_v1": sum(item["format"] == "SOW_V1" and item["valid"] == "true" and item["excluded_pkg00"] == "false" for item in population), "validation_failures": validation_failures},
        "pkg00_exemptions": {"members": len(exemptions), "legacy_four_doc": sum(item["format"] == "LEGACY_FOUR_DOC" and item["excluded_pkg00"] == "true" for item in population)},
        "production_cleanliness": {"residue_members": len(residue)},
        "repair_reproduction": {"members": len(repair_manifest), "errors": repair_errors},
        "rollback": {"sources": len(rollback_sources), "members": len(rollback_by_dir), "rows": len(seen_paths), "operations": dict(Counter(operation(row) for group in rollback_by_dir.values() for row in group)), "errors": rollback_errors},
        "legacy_surfaces": dict(Counter(str(item["surface_type"]) for item in surface_rows)),
        "h2_approved": False,
        "legacy_retirement_implemented": False,
    }
    (out / "CHECK_RESULTS.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
