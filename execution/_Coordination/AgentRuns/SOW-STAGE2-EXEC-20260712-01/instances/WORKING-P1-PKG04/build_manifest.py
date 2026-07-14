#!/usr/bin/env python3
"""Build the terminal self-excluding package manifest last."""
import csv, hashlib, subprocess
from pathlib import Path

root = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
run = root / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
instance = run / "instances/WORKING-P1-PKG04"
candidate = run / "candidates/W_P1/PIP-PKG04"
manifest = instance / "MANIFEST.tsv"
files = sorted([p for base in (candidate, instance) for p in base.rglob("*") if p.is_file() and p != manifest])
with manifest.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
    writer.writerow(["sha256", "bytes", "path"])
    for path in files:
        data = path.read_bytes()
        writer.writerow([hashlib.sha256(data).hexdigest(), len(data), path.relative_to(root).as_posix()])
print(len(files))
