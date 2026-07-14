#!/usr/bin/env python3
"""Reproduce the approved DEL-01-01 basis before project mutation."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
SNAP = RUN / "snapshots/I0/preintegration-r1"
H1 = RUN / "snapshots/I0/H1_EVIDENCE"
CHANGE = RUN / "instances/CHANGE-I1"
BASIS = "b776813d57124df94e9ba1b66a8a63e89487b388"
RECON_MANIFEST_SHA = "802656d604adcaed53bdfd6789a79d852da77dc252382387954f369fe603bc74"
H1_MANIFEST_SHA = "4c9a71df041a37755cd0c291f3013130245b7d44156cc0bb558370c701394df2"
STATUS_SHA = "e63b1797b30c291b2a4510cd521951fd2736675025f0e2d07b810e64617b28a8"
CANDIDATE_SHA = "23d92ddeb0cc4e3fe37694b1c8b79284017799cd08caaaad9767c8a4f0121f21"

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))

def resolve(manifest: Path, raw: str) -> Path:
    target = ROOT / raw if raw.startswith("execution/") else manifest.parent / raw
    target = target.resolve()
    target.relative_to(ROOT.resolve())
    return target

def verify_manifest(manifest: Path, expected_sha: str) -> int:
    assert sha(manifest) == expected_sha, manifest
    bound = rows(manifest)
    for row in bound:
        target = resolve(manifest, row["path"])
        assert target.is_file(), target
        assert sha(target) == row["sha256"], target
        assert target.stat().st_size == int(row["bytes"]), target
    return len(bound)

def main() -> None:
    assert subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() == BASIS
    assert subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, text=True).strip() == "codex/sow-i1-del0101"
    assert subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=ROOT, text=True).strip() == BASIS
    assert subprocess.check_output(["git", "ls-remote", "origin", "refs/heads/main"], cwd=ROOT, text=True).split()[0] == BASIS
    recon_rows = verify_manifest(SNAP / "MANIFEST.tsv", RECON_MANIFEST_SHA)
    h1_rows = verify_manifest(H1 / "MANIFEST.tsv", H1_MANIFEST_SHA)
    replacement = rows(SNAP / "REPLACEMENT_MANIFEST.tsv")
    rollback = rows(SNAP / "ROLLBACK_MANIFEST.tsv")
    assert len(replacement) == len(rollback) == 5
    for forward, inverse in zip(replacement, rollback):
        assert forward["path"] == inverse["path"]
        assert forward["before_sha256"] == inverse["after_sha256"]
        assert forward["after_sha256"] == inverse["before_sha256"]
        target = ROOT / forward["path"]
        if forward["before_sha256"] == "ABSENT":
            assert not target.exists(), target
        else:
            assert target.is_file() and sha(target) == forward["before_sha256"], target
            assert target.stat().st_size == int(forward["before_bytes"]), target
    target_dir = (ROOT / replacement[0]["path"]).parent
    status = target_dir / "_STATUS.md"
    candidate = RUN / "candidates/I0/PIP-PKG01/DEL-01-01/production/ScopeOfWork.md"
    assert sha(status) == STATUS_SHA
    assert sha(candidate) == CANDIDATE_SHA
    assert "ISSUED" in status.read_text(encoding="utf-8")
    assert subprocess.check_output(["git", "status", "--porcelain=v1", "--", "projects/chirality-piping"], cwd=ROOT, text=True) == ""
    report = {
        "schema": "chirality-change-i1-preflight/v1",
        "verdict": "PASS",
        "basis": BASIS,
        "branch": "codex/sow-i1-del0101",
        "recon_manifest_sha256": RECON_MANIFEST_SHA,
        "recon_manifest_rows": recon_rows,
        "h1_manifest_sha256": H1_MANIFEST_SHA,
        "h1_manifest_rows": h1_rows,
        "replacement_rows": 5,
        "rollback_rows": 5,
        "candidate_sha256": CANDIDATE_SHA,
        "status_sha256": STATUS_SHA,
        "lifecycle": "ISSUED",
        "project_mutation_before": False,
    }
    (CHANGE / "PREFLIGHT.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
