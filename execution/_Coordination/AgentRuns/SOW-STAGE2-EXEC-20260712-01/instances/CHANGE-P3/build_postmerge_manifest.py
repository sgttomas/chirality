#!/usr/bin/env python3
"""Build and validate the immutable W-P3 postmerge snapshot manifest."""

from __future__ import annotations
import csv, hashlib, json, subprocess
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
SNAP = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_P3/integration/postmerge"
OUT = SNAP / "MANIFEST.tsv"

def main() -> None:
    files = sorted(path for path in SNAP.rglob("*") if path.is_file() and path != OUT)
    for path in files:
        if path.suffix == ".json":
            json.loads(path.read_text(encoding="utf-8"))
    with OUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["sha256", "bytes", "path"])
        for path in files:
            data = path.read_bytes()
            writer.writerow([hashlib.sha256(data).hexdigest(), len(data), path.relative_to(ROOT).as_posix()])
    print(json.dumps({"verdict": "PASS", "rows": len(files), "manifest_sha256": hashlib.sha256(OUT.read_bytes()).hexdigest()}, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
