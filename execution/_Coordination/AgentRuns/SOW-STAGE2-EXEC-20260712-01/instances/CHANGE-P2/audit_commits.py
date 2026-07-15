#!/usr/bin/env python3
"""Audit the 29 ordered W-P2 project commits and preserved controls."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
SNAP = RUN / "snapshots/W_P2/preintegration"
CHANGE = RUN / "instances/CHANGE-P2"
BASIS = "eaad463c0d481f6f1654e6adb5ee718f566176e9"


def git(*args: str, text: bool = True) -> str | bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=text)


def main() -> None:
    with (SNAP / "REPLACEMENT_MANIFEST.tsv").open(encoding="utf-8", newline="") as handle:
        replacements = list(csv.DictReader(handle, delimiter="\t"))
    with (SNAP / "SOURCE_BINDINGS.tsv").open(encoding="utf-8", newline="") as handle:
        bindings = list(csv.DictReader(handle, delimiter="\t"))

    commits = git("rev-list", "--reverse", f"{BASIS}..HEAD").splitlines()
    deliverable_ids = list(dict.fromkeys(row["deliverable_id"] for row in replacements))
    assert len(commits) == len(deliverable_ids) == 29, commits
    results: list[dict[str, object]] = []
    for deliverable_id, commit in zip(deliverable_ids, commits, strict=True):
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
