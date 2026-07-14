#!/usr/bin/env python3
"""Build terminal self-excluding manifests for the blocked reconciliation."""
import csv
import hashlib
import subprocess
from pathlib import Path

root = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
run = root / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
for base, name in [
    (run / "snapshots/W_P1/PKG03-preintegration", "MANIFEST.tsv"),
    (run / "instances/RECON-P1-PKG03", "MANIFEST.tsv"),
]:
    manifest = base / name
    files = sorted(p for p in base.rglob("*") if p.is_file() and p != manifest)
    with manifest.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["sha256", "bytes", "path"])
        for path in files:
            data = path.read_bytes()
            writer.writerow([hashlib.sha256(data).hexdigest(), len(data), path.relative_to(root).as_posix()])
    print(f"{manifest.relative_to(root)}\t{len(files)}")

