#!/usr/bin/env python3
"""Validate the bounded clean-production repair and retain machine evidence."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
INSTANCE = Path(__file__).resolve().parent
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
sys.path.insert(0, str(ROOT / "tools/scope_of_work"))
from common import resolve_production_format  # noqa: E402

PROHIBITED = re.compile(
    r"migration candidate|sow-source-begin|sow-source-end|migration-authority:|"
    r"pilot-variance:|issued-preparation-",
    re.IGNORECASE,
)
LEGACY = ("Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tsv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main() -> int:
    errors: list[str] = []
    repair = tsv(INSTANCE / "MANIFEST.tsv")
    if len(repair) != 57:
        errors.append(f"repair manifest rows {len(repair)} != 57")
    if [row["path"] for row in repair] != sorted(row["path"] for row in repair):
        errors.append("repair manifest is not path-sorted")
    if Counter(row["project"] for row in repair) != Counter(
        {"chirality-app-dev": 53, "chirality-piping": 4}
    ):
        errors.append("repair project population is not 53 App + 4 Piping")
    for row in repair:
        production = ROOT / row["path"]
        report_path = INSTANCE / "reports" / Path(row["path"]).with_suffix("") / "finalization.json"
        if not production.is_file() or not report_path.is_file():
            errors.append(f"missing production/report pair: {row['path']}")
            continue
        report = json.loads(report_path.read_text(encoding="utf-8"))
        checks = {
            "production hash": sha256(production) == row["after_sha256"],
            "report hash": sha256(report_path) == row["report_sha256"],
            "report schema": report.get("schema") == "chirality-sow-finalization/v1",
            "before binding": report.get("evidence_candidate_sha256") == row["before_sha256"],
            "after binding": report.get("production_scope_of_work_sha256") == row["after_sha256"],
            "source blocks": bool(report.get("source_blocks")),
            "source block count": report.get("source_block_count") == len(report.get("source_blocks", [])),
            "migration control": bool(report.get("migration_control")),
        }
        for label, passed in checks.items():
            if not passed:
                errors.append(f"{label} failed: {row['path']}")

    basis = tsv(RUN / "basis/CENSUS_MANIFEST.tsv")
    formats: Counter[str] = Counter()
    converted: Counter[str] = Counter()
    lifecycle: Counter[str] = Counter()
    residue: list[str] = []
    pkg00_hashes: list[dict[str, str]] = []
    for member in basis:
        directory = ROOT / member["path"]
        resolution = resolve_production_format(directory)
        formats[resolution.state] += 1
        excluded = member["project"] == "PIP" and member["package"] == "PKG-00"
        if not excluded:
            converted[resolution.state] += 1
        if not resolution.valid:
            errors.append(f"invalid format {resolution.state}: {member['path']}: {resolution.issues}")
        status = directory / "_STATUS.md"
        text = status.read_text(encoding="utf-8")
        match = re.search(r"\*\*Current State:\*\*\s*([^\n]+)", text)
        lifecycle[match.group(1).strip() if match else "UNKNOWN"] += 1
        sow = directory / "ScopeOfWork.md"
        if sow.is_file() and PROHIBITED.search(sow.read_text(encoding="utf-8")):
            residue.append(member["path"])
        if excluded:
            hashes = {}
            for name in LEGACY:
                path = directory / name
                current = sha256(path)
                expected = subprocess.check_output(
                    ["git", "show", f"HEAD:{path.relative_to(ROOT).as_posix()}"],
                    cwd=ROOT,
                )
                head_hash = hashlib.sha256(expected).hexdigest()
                hashes[name] = current
                if current != head_hash:
                    errors.append(f"PKG-00 exemption changed: {path.relative_to(ROOT)}")
            pkg00_hashes.append({"path": member["path"], **hashes})

    if formats != Counter({"SOW_V1": 146, "LEGACY_FOUR_DOC": 8}):
        errors.append(f"tracked formats mismatch: {dict(formats)}")
    if converted != Counter({"SOW_V1": 146}):
        errors.append(f"converted formats mismatch: {dict(converted)}")
    if lifecycle != Counter({"IN_PROGRESS": 153, "ISSUED": 1}):
        errors.append(f"lifecycle mismatch: {dict(lifecycle)}")
    if residue:
        errors.append(f"prohibited residue remains in {len(residue)} converted contracts")

    project_diff = subprocess.check_output(
        ["git", "diff", "--name-only", "--", "projects/chirality-app-dev", "projects/chirality-piping"],
        cwd=ROOT,
        text=True,
    ).splitlines()
    expected_diff = sorted(row["path"] for row in repair)
    if sorted(project_diff) != expected_diff:
        errors.append("project diff does not equal exact 57-path repair manifest")

    report = {
        "schema": "chirality-sow-clean-repair-validation/v1",
        "verdict": "PASS" if not errors else "BLOCKED",
        "errors": errors,
        "repair_members": len(repair),
        "repair_projects": dict(Counter(row["project"] for row in repair)),
        "reports": len(list((INSTANCE / "reports").rglob("finalization.json"))),
        "formats": dict(formats),
        "conversion_formats": dict(converted),
        "lifecycle": dict(lifecycle),
        "prohibited_residue_members": residue,
        "pkg00_exemptions": len(pkg00_hashes),
        "project_diff_paths": project_diff,
        "manifest_sha256": sha256(INSTANCE / "MANIFEST.tsv"),
    }
    (INSTANCE / "VALIDATION.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
