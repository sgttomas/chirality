#!/usr/bin/env python3
"""Freeze the scoped I1 premerge evidence tranche."""

from __future__ import annotations
import csv, hashlib, json, subprocess
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
CHANGE = RUN / "instances/CHANGE-I1"
OUTPUT = CHANGE / "EVIDENCE_BINDING.tsv"

def sha(path: Path) -> str: return hashlib.sha256(path.read_bytes()).hexdigest()
def resolve(manifest: Path, raw: str) -> Path:
    target = (ROOT / raw if raw.startswith("execution/") else manifest.parent / raw).resolve()
    target.relative_to(ROOT.resolve()); return target
def verify_manifest(manifest: Path) -> int:
    with manifest.open(encoding="utf-8", newline="") as h: rows = list(csv.DictReader(h, delimiter="\t"))
    for row in rows:
        target = resolve(manifest, row["path"])
        assert sha(target) == row["sha256"] and target.stat().st_size == int(row["bytes"]), target
    return len(rows)

def main() -> None:
    scopes = [CHANGE, RUN / "snapshots/I0/preintegration-r1", RUN / "snapshots/I0/H1_EVIDENCE"]
    files = [RUN / "ORCHESTRATION_PLAN.md", RUN / "WORK_GRAPH.json", RUN / "amendments/H1-APPROVAL-001.md"]
    for scope in scopes: files.extend(p for p in scope.rglob("*") if p.is_file())
    files = sorted({p.resolve() for p in files if p.resolve() != OUTPUT.resolve()})
    manifests = [p for p in files if p.name == "MANIFEST.tsv"]
    manifest_rows = sum(verify_manifest(p) for p in manifests)
    json_files = [p for p in files if p.suffix == ".json"]
    for path in json_files: json.loads(path.read_text(encoding="utf-8"))
    with OUTPUT.open("w", encoding="utf-8", newline="") as h:
        w=csv.writer(h,delimiter="\t",lineterminator="\n"); w.writerow(["sha256","bytes","path"])
        for path in files:
            data=path.read_bytes(); w.writerow([hashlib.sha256(data).hexdigest(),len(data),path.relative_to(ROOT).as_posix()])
    print(json.dumps({"verdict":"PASS","binding_rows":len(files),"verified_manifests":len(manifests),"verified_manifest_rows":manifest_rows,"parsed_json":len(json_files),"binding_sha256":sha(OUTPUT)},indent=2,sort_keys=True))

if __name__ == "__main__": main()
