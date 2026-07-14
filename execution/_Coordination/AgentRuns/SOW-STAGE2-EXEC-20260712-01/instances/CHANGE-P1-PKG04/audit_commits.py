#!/usr/bin/env python3
"""Audit the six ordered PKG-04 project commits and preserved controls."""

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


def git(*args: str, text: bool = True) -> str | bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=text)


def main() -> None:
    with (SNAP / "REPLACEMENT_MANIFEST.tsv").open(encoding="utf-8", newline="") as handle:
        replacements = list(csv.DictReader(handle, delimiter="\t"))
    with (SNAP / "SOURCE_BINDINGS.tsv").open(encoding="utf-8", newline="") as handle:
        bindings = list(csv.DictReader(handle, delimiter="\t"))

    commits = git("rev-list", "--reverse", f"{BASIS}..HEAD").splitlines()
    assert len(commits) == 6, commits
    results: list[dict[str, object]] = []
    for index, commit in enumerate(commits, start=1):
        deliverable_id = f"DEL-04-{index:02d}"
        expected = [row for row in replacements if row["deliverable_id"] == deliverable_id]
        assert len(expected) == 5
        actual = git("diff-tree", "--no-commit-id", "--name-only", "-r", commit).splitlines()
        assert sorted(actual) == sorted(row["path"] for row in expected), (commit, actual)
        for row in expected:
            spec = f"{commit}:{row['path']}"
            if row["after_sha256"] == "ABSENT":
                exists = subprocess.run(
                    ["git", "cat-file", "-e", spec], cwd=ROOT, capture_output=True
                ).returncode == 0
                assert not exists, spec
            else:
                data = git("show", spec, text=False)
                assert hashlib.sha256(data).hexdigest() == row["after_sha256"], spec

        for row in (item for item in bindings if item["deliverable_id"] == deliverable_id and item["surface"] not in {"Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"}):
            directory = Path(expected[0]["path"]).parent
            path = (directory / row["surface"]).as_posix()
            data = git("show", f"{commit}:{path}", text=False)
            assert hashlib.sha256(data).hexdigest() == row["expected_sha256"], (commit, path)
        results.append({"deliverable_id": deliverable_id, "commit": commit, "paths": 5, "verdict": "PASS"})

    report = {
        "schema": "chirality-change-atomic-commit-audit/v1",
        "basis": BASIS,
        "verdict": "PASS",
        "commits": results,
    }
    (CHANGE / "ATOMIC_COMMITS.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
