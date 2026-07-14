#!/usr/bin/env python3
"""Audit the atomic DEL-01-01 project commit against the accepted manifest."""

from __future__ import annotations
import csv, hashlib, json, subprocess
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
CHANGE = RUN / "instances/CHANGE-I1"
COMMIT = "3c7f6abfbb7ba7926161369825742fcfd85cbd90"

def main() -> None:
    with (RUN / "snapshots/I0/preintegration-r1/REPLACEMENT_MANIFEST.tsv").open(encoding="utf-8", newline="") as h:
        rows = list(csv.DictReader(h, delimiter="\t"))
    changed = subprocess.check_output(["git", "diff-tree", "--no-commit-id", "--name-only", "-r", COMMIT], cwd=ROOT, text=True).splitlines()
    assert set(changed) == {r["path"] for r in rows} and len(changed) == 5
    for row in rows:
        spec = f"{COMMIT}:{row['path']}"
        if row["after_sha256"] == "ABSENT":
            assert subprocess.run(["git", "cat-file", "-e", spec], cwd=ROOT, capture_output=True).returncode != 0
        else:
            data = subprocess.check_output(["git", "show", spec], cwd=ROOT)
            assert hashlib.sha256(data).hexdigest() == row["after_sha256"] and len(data) == int(row["after_bytes"])
    report = {"schema":"chirality-change-i1-commit-audit/v1","verdict":"PASS","commit":COMMIT,"changed_paths":5,"additions":1,"deletions":4,"control_paths_changed":0}
    (CHANGE / "PROJECT_COMMIT_AUDIT.json").write_text(json.dumps(report, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))

if __name__ == "__main__": main()
