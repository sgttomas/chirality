#!/usr/bin/env python3
"""Reconstruct retained author normalization ledgers and self-excluding manifests."""

from __future__ import annotations

import csv
import hashlib
import subprocess
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
PREFLIGHT = RUN / "snapshots/W_P1/preflight-r1/P1_MANIFEST.tsv"
PARENT = RUN / "instances/WORKING-P1-PKG04/children"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


with PREFLIGHT.open(newline="") as handle:
    live_rows = {
        row["deliverable_id"]: ROOT / row["live_path"]
        for row in csv.DictReader(handle, delimiter="\t")
        if row["package"] == "PKG-04"
    }

for batch in ("BATCH-01-AUTHOR", "BATCH-02-AUTHOR"):
    child = PARENT / batch
    normalization = []
    for workspace in sorted(child.glob("members/*/workspace-*")):
        did = workspace.parent.name
        live = live_rows[did]
        for target in sorted(path for path in workspace.rglob("*") if path.is_file()):
            relative = target.relative_to(workspace)
            source = live / relative
            if not source.is_file() or source.read_bytes() == target.read_bytes():
                continue
            before = source.read_bytes()
            after = target.read_bytes()
            normalized = b"\n".join(line.rstrip() for line in before.splitlines()).rstrip(b"\n") + b"\n"
            assert after == normalized, target
            operation = (
                "remove_terminal_blank_lines"
                if before.endswith(b"\n\n") and after == before.rstrip(b"\n") + b"\n"
                else "strip_trailing_whitespace_and_terminal_blank_lines"
            )
            normalization.append(
                [sha(before), sha(after), len(before), len(after), target.relative_to(ROOT).as_posix(), operation]
            )

    ledger = child / "NORMALIZATION.tsv"
    with ledger.open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["before_sha256", "after_sha256", "before_bytes", "after_bytes", "path", "operation"])
        writer.writerows(normalization)

    manifest = child / "MANIFEST.tsv"
    files = sorted(path for path in child.rglob("*") if path.is_file() and path != manifest)
    with manifest.open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["sha256", "bytes", "path"])
        for path in files:
            data = path.read_bytes()
            writer.writerow([sha(data), len(data), path.relative_to(ROOT).as_posix()])

    for row in csv.DictReader(manifest.open(), delimiter="\t"):
        path = ROOT / row["path"]
        data = path.read_bytes()
        assert sha(data) == row["sha256"] and len(data) == int(row["bytes"])
    print(batch, len(normalization), len(files), sha(manifest.read_bytes()))
