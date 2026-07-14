#!/usr/bin/env python3
"""Build and validate the immutable I1 postmerge snapshot manifest."""

from __future__ import annotations
import csv, hashlib, json, subprocess
from pathlib import Path

ROOT=Path(subprocess.check_output(["git","rev-parse","--show-toplevel"],text=True).strip())
SNAP=ROOT/"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/I0/integration/postmerge"
OUT=SNAP/"MANIFEST.tsv"
def main() -> None:
    files=sorted(p for p in SNAP.rglob("*") if p.is_file() and p != OUT)
    for p in files:
        if p.suffix==".json": json.loads(p.read_text(encoding="utf-8"))
    with OUT.open("w",encoding="utf-8",newline="") as h:
        w=csv.writer(h,delimiter="\t",lineterminator="\n");w.writerow(["sha256","bytes","path"])
        for p in files:
            data=p.read_bytes();w.writerow([hashlib.sha256(data).hexdigest(),len(data),p.relative_to(ROOT).as_posix()])
    data=OUT.read_bytes();print(json.dumps({"verdict":"PASS","rows":len(files),"manifest_sha256":hashlib.sha256(data).hexdigest()},indent=2,sort_keys=True))
if __name__=="__main__": main()
