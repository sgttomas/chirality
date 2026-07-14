#!/usr/bin/env python3
from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PACKAGE-BATCH-ADOPTION-20260714-01"
INSTANCE = RUN / "instances/WORKING-BATCH-ADOPTION"
SNAPSHOT = RUN / "snapshots/package"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def manifest(base: Path, output: Path, files: list[Path]) -> None:
    rows = ["path\tsha256\tbytes"]
    for path in sorted(files):
        rows.append(f"{{REPO_ROOT}}/{path.relative_to(ROOT).as_posix()}\t{digest(path)}\t{path.stat().st_size}")
    output.write_text("\n".join(rows) + "\n", encoding="utf-8")


snapshot_files = [p for p in SNAPSHOT.rglob("*") if p.is_file() and p.name != "MANIFEST.tsv"]
manifest(SNAPSHOT, SNAPSHOT / "MANIFEST.tsv", snapshot_files)

instance_files = [
    p for p in INSTANCE.rglob("*")
    if p.is_file() and p.name != "MANIFEST.tsv" and "__pycache__" not in p.parts
]
candidate_files = [p for p in (RUN / "candidates").rglob("*") if p.is_file()]
manifest(INSTANCE, INSTANCE / "MANIFEST.tsv", instance_files + candidate_files + [SNAPSHOT / "MANIFEST.tsv"])

print(digest(SNAPSHOT / "MANIFEST.tsv"))
print(digest(INSTANCE / "MANIFEST.tsv"))
