#!/usr/bin/env python3
"""Reproduce PKG-04 replacement and inverse rollback in byte-addressed memory."""

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


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_bytes(spec: str) -> bytes:
    return subprocess.check_output(["git", "show", spec], cwd=ROOT)


def read_rows(name: str) -> list[dict[str, str]]:
    with (SNAP / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main() -> None:
    replacement = read_rows("REPLACEMENT_MANIFEST.tsv")
    rollback = read_rows("ROLLBACK_MANIFEST.tsv")
    assert len(replacement) == len(rollback) == 30
    inverse = {(row["deliverable_id"], row["path"]): row for row in rollback}
    assert len(inverse) == 30
    results: list[dict[str, object]] = []
    for index in range(1, 7):
        deliverable_id = f"DEL-04-{index:02d}"
        rows = [row for row in replacement if row["deliverable_id"] == deliverable_id]
        assert len(rows) == 5
        original: dict[str, bytes] = {}
        state: dict[str, bytes] = {}
        for row in rows:
            inv = inverse[(deliverable_id, row["path"])]
            assert row["before_sha256"] == inv["after_sha256"]
            assert row["after_sha256"] == inv["before_sha256"]
            if row["before_sha256"] != "ABSENT":
                data = git_bytes(f"{BASIS}:{row['path']}")
                assert sha(data) == row["before_sha256"]
                original[row["path"]] = data
                state[row["path"]] = data

        for row in rows:
            if row["action"] == "ADD":
                candidate = RUN / f"candidates/W_P1/PIP-PKG04/{deliverable_id}/production/ScopeOfWork.md"
                data = candidate.read_bytes()
                assert sha(data) == row["after_sha256"]
                state[row["path"]] = data
            else:
                assert sha(state.pop(row["path"])) == row["before_sha256"]
        assert len(state) == 1
        for row in rows:
            if row["after_sha256"] == "ABSENT":
                assert row["path"] not in state
            else:
                assert sha(state[row["path"]]) == row["after_sha256"]

        for row in (inverse[(deliverable_id, item["path"])] for item in rows):
            if row["action"] == "ADD":
                data = git_bytes(f"{BASIS}:{row['path']}")
                assert sha(data) == row["after_sha256"]
                state[row["path"]] = data
            else:
                assert sha(state.pop(row["path"])) == row["before_sha256"]
        assert state == original
        results.append({"deliverable_id": deliverable_id, "apply": "PASS", "target": "PASS", "rollback": "PASS"})

    expected_paths = sorted(row["path"] for row in replacement)
    actual_paths = subprocess.check_output(
        ["git", "diff", "--name-only", BASIS, "HEAD", "--", "projects/chirality-piping"],
        cwd=ROOT,
        text=True,
    ).splitlines()
    assert sorted(actual_paths) == expected_paths
    report = {
        "schema": "chirality-change-replacement-simulation/v1",
        "verdict": "PASS",
        "replacement_rows": 30,
        "rollback_rows": 30,
        "simulations": results,
        "project_paths": 30,
    }
    (CHANGE / "SIMULATION.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
