#!/usr/bin/env python3
"""Apply the registered SoW finalizer to the sealed 57-member repair set."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
INSTANCE = Path(__file__).resolve().parent
FINALIZER = ROOT / "tools/scope_of_work/finalize_scope_of_work.py"
PROJECT_ROOTS = (
    ROOT / "projects/chirality-app-dev/execution",
    ROOT / "projects/chirality-piping/execution",
)
PROHIBITED = re.compile(
    r"migration candidate|sow-source-begin|sow-source-end|migration-authority:|"
    r"pilot-variance:|issued-preparation-",
    re.IGNORECASE,
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def discover() -> list[Path]:
    return sorted(
        path
        for project_root in PROJECT_ROOTS
        for path in project_root.rglob("ScopeOfWork.md")
        if PROHIBITED.search(path.read_text(encoding="utf-8"))
    )


def identity(path: Path) -> tuple[str, str, str]:
    relative = path.relative_to(ROOT)
    project = relative.parts[1]
    package_match = re.match(r"(PKG-\d+)", relative.parts[3])
    deliverable_match = re.match(r"(DEL-\d+-\d+)", relative.parts[5])
    if not package_match or not deliverable_match:
        raise RuntimeError(f"cannot derive member identity: {relative}")
    return project, package_match.group(1), deliverable_match.group(1)


def main() -> int:
    members = discover()
    project_counts = {
        project: sum(path.relative_to(ROOT).parts[1] == project for path in members)
        for project in ("chirality-app-dev", "chirality-piping")
    }
    if len(members) != 57 or project_counts != {
        "chirality-app-dev": 53,
        "chirality-piping": 4,
    }:
        raise RuntimeError(
            f"sealed population mismatch: total={len(members)} projects={project_counts}"
        )

    reports_root = INSTANCE / "reports"
    staging_root = INSTANCE / "staging"
    if reports_root.exists() or staging_root.exists():
        raise RuntimeError("repair outputs already exist; refusing an ambiguous rerun")
    rows: list[dict[str, str]] = []
    for path in members:
        relative = path.relative_to(ROOT)
        project, package, deliverable = identity(path)
        before = sha256(path)
        keyed = relative.with_suffix("")
        staged = staging_root / keyed / "ScopeOfWork.md"
        report = reports_root / keyed / "finalization.json"
        staged.parent.mkdir(parents=True, exist_ok=True)
        report.parent.mkdir(parents=True, exist_ok=True)
        result = subprocess.run(
            [
                sys.executable,
                str(FINALIZER),
                "--evidence-candidate",
                str(path),
                "--output",
                str(staged),
                "--report",
                str(report),
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        if result.returncode:
            raise RuntimeError(
                f"finalizer failed for {relative}: {result.stdout}{result.stderr}"
            )
        evidence = json.loads(report.read_text(encoding="utf-8"))
        after = sha256(staged)
        if evidence.get("schema") != "chirality-sow-finalization/v1":
            raise RuntimeError(f"wrong report schema for {relative}")
        if evidence.get("evidence_candidate_sha256") != before:
            raise RuntimeError(f"before hash mismatch for {relative}")
        if evidence.get("production_scope_of_work_sha256") != after:
            raise RuntimeError(f"after hash mismatch for {relative}")
        if before == after:
            raise RuntimeError(f"finalizer produced no change for {relative}")
        if PROHIBITED.search(staged.read_text(encoding="utf-8")):
            raise RuntimeError(f"prohibited residue in staged output for {relative}")
        os.replace(staged, path)
        if sha256(path) != after:
            raise RuntimeError(f"durable replacement mismatch for {relative}")
        rows.append(
            {
                "path": relative.as_posix(),
                "before_sha256": before,
                "after_sha256": after,
                "report_sha256": sha256(report),
                "project": project,
                "package": package,
                "deliverable": deliverable,
            }
        )

    shutil.rmtree(staging_root)
    manifest = INSTANCE / "MANIFEST.tsv"
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            delimiter="\t",
            fieldnames=(
                "path",
                "before_sha256",
                "after_sha256",
                "report_sha256",
                "project",
                "package",
                "deliverable",
            ),
        )
        writer.writeheader()
        writer.writerows(rows)
    print(
        f"PASS changed={len(rows)} app={project_counts['chirality-app-dev']} "
        f"piping={project_counts['chirality-piping']} manifest_sha256={sha256(manifest)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
