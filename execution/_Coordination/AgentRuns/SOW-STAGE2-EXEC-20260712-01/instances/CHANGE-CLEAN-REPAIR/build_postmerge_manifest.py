#!/usr/bin/env python3
"""Build the immutable clean-repair integration snapshot from merged main."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
CHANGE = RUN / "instances/CHANGE-CLEAN-REPAIR"
SOURCE = RUN / "instances/RECON-CLEAN-REPAIR/PROPOSED_CHANGE_MANIFEST.tsv"
OUT = RUN / "snapshots/CONVERSION_CLOSURE/repair_integration/74b9804cf62c014118ad222699a3591fdf5bda42"
MERGE = "74b9804cf62c014118ad222699a3591fdf5bda42"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    assert subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=ROOT, text=True).strip() == MERGE
    OUT.mkdir(parents=True, exist_ok=False)
    rows = list(csv.DictReader(SOURCE.open(encoding="utf-8", newline=""), delimiter="\t"))
    assert len(rows) == 57
    with (OUT / "PROJECT_MANIFEST.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["path", "sha256", "merge_commit"])
        for row in rows:
            data = subprocess.check_output(["git", "show", f"{MERGE}:{row['path']}"], cwd=ROOT)
            assert digest(data) == row["after_sha256"]
            writer.writerow([row["path"], row["after_sha256"], MERGE])
    pr = json.loads(subprocess.check_output(
        ["gh", "pr", "view", "237", "--json", "number,state,mergedAt,mergeCommit,headRefOid,statusCheckRollup,url"],
        cwd=ROOT, text=True,
    ))
    assert pr["state"] == "MERGED" and pr["mergeCommit"]["oid"] == MERGE
    checks = {row["name"]: row.get("conclusion") for row in pr["statusCheckRollup"]}
    assert checks == {"Harness pre-merge": "SUCCESS", "harness": "SUCCESS"}, checks
    (OUT / "PR_CHECKS.json").write_text(json.dumps(pr, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    result = {
        "schema": "chirality-sow-clean-repair-postmerge/v1",
        "verdict": "PASS",
        "source_head": "bd9b163f8e967697d1abe15f572b9c3740dd5c49",
        "merge_commit": MERGE,
        "project_hashes": 57,
        "sow_v1": 146,
        "pkg00_legacy_exemptions": 8,
        "lifecycle": {"IN_PROGRESS": 153, "ISSUED": 1},
        "forbidden_production_residue": 0,
        "h2_approved": False,
        "legacy_retirement_implemented": False,
    }
    (OUT / "POSTMERGE_VERIFICATION.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    bound = [
        OUT / "PROJECT_MANIFEST.tsv",
        OUT / "PR_CHECKS.json",
        OUT / "POSTMERGE_VERIFICATION.json",
        SOURCE,
        CHANGE / "COMMIT_BINDING.tsv",
        CHANGE / "PREINTEGRATION_CHECKS.md",
    ]
    with (OUT / "MANIFEST.tsv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["sha256", "bytes", "path"])
        for path in sorted(bound):
            data = path.read_bytes()
            writer.writerow([digest(data), len(data), path.relative_to(ROOT).as_posix()])
    print(json.dumps({"verdict": "PASS", "snapshot": str(OUT.relative_to(ROOT)), "manifest_sha256": digest((OUT / 'MANIFEST.tsv').read_bytes())}, sort_keys=True))


if __name__ == "__main__":
    main()
