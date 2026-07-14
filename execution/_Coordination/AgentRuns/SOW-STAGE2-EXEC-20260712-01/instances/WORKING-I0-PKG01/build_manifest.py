#!/usr/bin/env python3
"""Build a deterministic self-excluding manager/candidate manifest."""
from pathlib import Path
import hashlib

root = Path(__file__).resolve().parents[6]
instance = Path(__file__).resolve().parent
candidate = root / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/I0/PIP-PKG01/DEL-01-01"
output = instance / "MANIFEST.tsv"
paths = [p for base in (candidate, instance) for p in base.rglob("*") if p.is_file() and p != output]
rows = []
for path in sorted(paths, key=lambda item: item.relative_to(root).as_posix()):
    data = path.read_bytes()
    rows.append((path.relative_to(root).as_posix(), hashlib.sha256(data).hexdigest(), len(data)))
output.write_text("path\tsha256\tbytes\n" + "".join(f"{p}\t{h}\t{n}\n" for p, h, n in rows))
print(f"PASS rows={len(rows)} sha256={hashlib.sha256(output.read_bytes()).hexdigest()}")
