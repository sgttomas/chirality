#!/usr/bin/env python3
"""Bind the terminal ORCHESTRATOR-P3-B0 instance record, excluding the index."""

import csv
import hashlib
from pathlib import Path


HERE = Path(__file__).resolve().parent
rows = []
for path in sorted(HERE.iterdir()):
    if not path.is_file() or path.name == "MANIFEST.tsv":
        continue
    rows.append({
        "artifact": path.name,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "bytes": path.stat().st_size,
        "binding_status": "BOUND",
    })
with (HERE / "MANIFEST.tsv").open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=["artifact", "sha256", "bytes", "binding_status"], delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
