#!/usr/bin/env python3
"""Verify exact applied state and simulate inverse rollback without touching it."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
SNAP = RUN / "snapshots/I0/preintegration-r1"
CHANGE = RUN / "instances/CHANGE-I1"
STATUS_SHA = "e63b1797b30c291b2a4510cd521951fd2736675025f0e2d07b810e64617b28a8"

def sha_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))

def basis_blob(path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"b776813d57124df94e9ba1b66a8a63e89487b388:{path}"], cwd=ROOT)

def main() -> None:
    forward = rows(SNAP / "REPLACEMENT_MANIFEST.tsv")
    inverse = rows(SNAP / "ROLLBACK_MANIFEST.tsv")
    assert len(forward) == len(inverse) == 5
    memory: dict[str, bytes | None] = {}
    for row in forward:
        path = ROOT / row["path"]
        if row["after_sha256"] == "ABSENT":
            assert not path.exists(), path
            memory[row["path"]] = None
        else:
            data = path.read_bytes()
            assert sha_bytes(data) == row["after_sha256"] and len(data) == int(row["after_bytes"]), path
            memory[row["path"]] = data
    target_dir = (ROOT / forward[0]["path"]).parent
    status = target_dir / "_STATUS.md"
    assert sha_bytes(status.read_bytes()) == STATUS_SHA and "ISSUED" in status.read_text(encoding="utf-8")

    # Simulate the inverse from immutable Git blobs; never write the live target.
    for row in inverse:
        if row["after_sha256"] == "ABSENT":
            memory[row["path"]] = None
        else:
            data = basis_blob(row["path"])
            assert sha_bytes(data) == row["after_sha256"] and len(data) == int(row["after_bytes"])
            memory[row["path"]] = data
    for row in forward:
        data = memory[row["path"]]
        if row["before_sha256"] == "ABSENT":
            assert data is None
        else:
            assert data is not None and sha_bytes(data) == row["before_sha256"]
    report = {
        "schema": "chirality-change-i1-simulation/v1",
        "verdict": "PASS",
        "target_rows": 5,
        "rollback_rows": 5,
        "rollback_executed_on_live_state": False,
        "status_sha256": STATUS_SHA,
        "lifecycle": "ISSUED",
    }
    (CHANGE / "SIMULATION.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
