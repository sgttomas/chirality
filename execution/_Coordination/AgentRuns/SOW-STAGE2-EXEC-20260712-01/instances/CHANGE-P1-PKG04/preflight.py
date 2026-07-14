#!/usr/bin/env python3
"""Reproduce the sealed PKG-04 CHANGE basis before project mutation."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
SNAP = RUN / "snapshots/W_P1/PKG04-preintegration-r1"
CHANGE = RUN / "instances/CHANGE-P1-PKG04"
BASIS = "2a5e3825d8d2fc4943742a53ccad3b89c4c81902"
SNAPSHOT_MANIFEST_SHA256 = "c30cacfbf26ceb9daa691cedf7688aba5e390d979c76c16142d67961084b94c4"


def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def manifest_target(raw: str) -> Path:
    target = ROOT / raw if raw.startswith("execution/") else SNAP / raw
    target.resolve().relative_to(ROOT.resolve())
    return target


def main() -> None:
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip()
    assert head == BASIS, (head, BASIS)
    assert branch == "codex/sow-p1-pkg04", branch
    assert sha(SNAP / "MANIFEST.tsv") == SNAPSHOT_MANIFEST_SHA256

    snapshot_rows = rows(SNAP / "MANIFEST.tsv")
    assert len(snapshot_rows) == 84
    for row in snapshot_rows:
        target = manifest_target(row["path"])
        data = target.read_bytes()
        assert sha_bytes(data) == row["sha256"], target
        assert len(data) == int(row["bytes"]), target

    replacement = rows(SNAP / "REPLACEMENT_MANIFEST.tsv")
    rollback = rows(SNAP / "ROLLBACK_MANIFEST.tsv")
    assert len(replacement) == len(rollback) == 30
    expected_ids = [f"DEL-04-{index:02d}" for index in range(1, 7)]
    assert sorted({row["deliverable_id"] for row in replacement}) == expected_ids

    replacement_by_key = {(row["deliverable_id"], row["path"]): row for row in replacement}
    rollback_by_key = {(row["deliverable_id"], row["path"]): row for row in rollback}
    assert replacement_by_key.keys() == rollback_by_key.keys()
    for key, row in replacement_by_key.items():
        inverse = rollback_by_key[key]
        assert row["before_sha256"] == inverse["after_sha256"], key
        assert row["after_sha256"] == inverse["before_sha256"], key
        path = ROOT / row["path"]
        if row["before_sha256"] == "ABSENT":
            assert not path.exists(), path
        else:
            assert path.is_file() and sha(path) == row["before_sha256"], path

    production: dict[str, dict[str, object]] = {}
    for deliverable_id in expected_ids:
        path = RUN / f"candidates/W_P1/PIP-PKG04/{deliverable_id}/production/ScopeOfWork.md"
        add = next(
            row for row in replacement
            if row["deliverable_id"] == deliverable_id and row["action"] == "ADD"
        )
        assert path.is_file() and sha(path) == add["after_sha256"]
        production[deliverable_id] = {
            "path": path.relative_to(ROOT).as_posix(),
            "sha256": sha(path),
            "bytes": path.stat().st_size,
        }

    source_bindings = rows(SNAP / "SOURCE_BINDINGS.tsv")
    assert len(source_bindings) == 54
    for row in source_bindings:
        assert row["verdict"] == "PASS" and row["expected_sha256"] == row["actual_sha256"], row

    status_control = [
        row for row in source_bindings
        if row["surface"] in {"_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"}
    ]
    assert len(status_control) == 30
    for row in status_control:
        match = next(item for item in replacement if item["deliverable_id"] == row["deliverable_id"])
        directory = (ROOT / match["path"]).parent
        target = directory / row["surface"]
        assert target.is_file() and sha(target) == row["expected_sha256"], target

    project_diff = subprocess.check_output(
        ["git", "status", "--porcelain=v1", "--", "projects/chirality-piping"],
        cwd=ROOT,
        text=True,
    )
    assert project_diff == "", project_diff

    report = {
        "schema": "chirality-change-preflight/v1",
        "verdict": "PASS",
        "basis": BASIS,
        "branch": branch,
        "snapshot_manifest_sha256": SNAPSHOT_MANIFEST_SHA256,
        "snapshot_rows": len(snapshot_rows),
        "replacement_rows": len(replacement),
        "rollback_rows": len(rollback),
        "source_binding_rows": len(source_bindings),
        "status_control_rows": len(status_control),
        "production": production,
        "project_mutation_before": False,
    }
    (CHANGE / "PREFLIGHT.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
