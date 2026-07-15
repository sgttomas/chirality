#!/usr/bin/env python3
"""Freeze and verify the complete scoped W-P3 coordination/evidence tranche."""

from __future__ import annotations

import csv
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
CHANGE = RUN / "instances/CHANGE-P3"
OUTPUT = CHANGE / "EVIDENCE_BINDING.tsv"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def resolve(manifest: Path, raw: str) -> Path:
    target = ROOT / raw if raw.startswith("execution/") else manifest.parent / raw
    target = target.resolve()
    target.relative_to(ROOT.resolve())
    return target


def verify_manifest(manifest: Path) -> int:
    with manifest.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if reader.fieldnames != ["sha256", "bytes", "path"]:
            return 0
        rows = list(reader)
    for row in rows:
        target = resolve(manifest, row["path"])
        data = target.read_bytes()
        assert hashlib.sha256(data).hexdigest() == row["sha256"], (manifest, target)
        assert len(data) == int(row["bytes"]), (manifest, target)
    return len(rows)


def main() -> None:
    scopes = [
        RUN / "candidates/W_P3",
        RUN / "instances/ORCHESTRATOR-P3-B0",
        RUN / "instances/WORKING-P3-PKG10",
        RUN / "instances/WORKING-P3-PKG11",
        RUN / "instances/WORKING-P3-PKG12",
        RUN / "instances/RECON-P3",
        CHANGE,
        RUN / "snapshots/W_P3/preflight",
        RUN / "snapshots/W_P3/preintegration",
        RUN / "snapshots/W_P3/preintegration-acceptance",
        RUN / "snapshots/W_P3/integration/postmerge",
    ]
    files = [
        ROOT / "execution/_Coordination/LOOP_RECEIPTS.md",
        RUN / "ORCHESTRATION_PLAN.md",
        RUN / "WORK_GRAPH.json",
        RUN / "amendments/WORKING-P3-PKG11/BRIEF_V2.md",
        RUN / "amendments/WORKING-P3-PKG12/BRIEF_V2.md",
    ]
    for scope in scopes:
        files.extend(path for path in scope.rglob("*") if path.is_file())
    files = sorted({path.resolve() for path in files if path.resolve() != OUTPUT.resolve()})
    for path in files:
        path.relative_to(ROOT.resolve())

    manifest_rows = 0
    manifests = [path for path in files if path.name == "MANIFEST.tsv"]
    for manifest in manifests:
        manifest_rows += verify_manifest(manifest)

    json_files = [path for path in files if path.suffix == ".json"]
    for path in json_files:
        json.loads(path.read_text(encoding="utf-8"))

    with OUTPUT.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["sha256", "bytes", "path"])
        for path in files:
            data = path.read_bytes()
            writer.writerow([hashlib.sha256(data).hexdigest(), len(data), path.relative_to(ROOT).as_posix()])

    print(json.dumps({
        "verdict": "PASS",
        "binding_rows": len(files),
        "verified_manifests": len(manifests),
        "verified_manifest_rows": manifest_rows,
        "parsed_json": len(json_files),
        "binding_sha256": sha(OUTPUT),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
