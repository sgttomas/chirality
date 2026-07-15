#!/usr/bin/env python3
import csv, hashlib
from pathlib import Path

own = Path(__file__).resolve().parent
out = own / "MANIFEST.tsv"
rows = []
for path in sorted(p for p in own.rglob("*") if p.is_file() and p != out):
    data = path.read_bytes()
    rows.append((hashlib.sha256(data).hexdigest(), len(data), path.relative_to(own).as_posix()))
with out.open("w", newline="") as f:
    writer = csv.writer(f, delimiter="\t", lineterminator="\n")
    writer.writerow(["sha256", "bytes", "path"]); writer.writerows(rows)
