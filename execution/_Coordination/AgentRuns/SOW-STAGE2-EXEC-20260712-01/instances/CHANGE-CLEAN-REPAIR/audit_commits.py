#!/usr/bin/env python3
"""Bind the accepted clean-production paths to their atomic Git commits."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
BASE = "715f618e93528d626a73d2134781e8c9c27f6c90"
HERE = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/CHANGE-CLEAN-REPAIR"
MANIFEST = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/RECON-CLEAN-REPAIR/PROPOSED_CHANGE_MANIFEST.tsv"


def run(*args: str) -> str:
    return subprocess.check_output(args, cwd=ROOT, text=True).strip()


def main() -> None:
    with MANIFEST.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert len(rows) == 57
    commits = run("git", "rev-list", "--reverse", f"{BASE}..HEAD").splitlines()
    assert len(commits) == 57, len(commits)
    bindings = []
    for row, commit in zip(rows, commits, strict=True):
        changed = run("git", "diff-tree", "--no-commit-id", "--name-only", "-r", commit).splitlines()
        assert changed == [row["path"]], (commit, changed, row["path"])
        blob = subprocess.check_output(["git", "show", f"{commit}:{row['path']}"], cwd=ROOT)
        assert hashlib.sha256(blob).hexdigest() == row["after_sha256"]
        bindings.append({"commit": commit, **row})
    (HERE / "ATOMIC_COMMITS.json").write_text(
        json.dumps({"basis": BASE, "count": len(bindings), "bindings": bindings}, indent=2) + "\n",
        encoding="utf-8",
    )
    with (HERE / "COMMIT_BINDING.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["commit", "path", "before_sha256", "after_sha256"], delimiter="\t", lineterminator="\n")
        writer.writeheader()
        for binding in bindings:
            writer.writerow({key: binding[key] for key in writer.fieldnames})
    print(json.dumps({"verdict": "PASS", "atomic_commits": len(bindings), "head": commits[-1]}, sort_keys=True))


if __name__ == "__main__":
    main()
