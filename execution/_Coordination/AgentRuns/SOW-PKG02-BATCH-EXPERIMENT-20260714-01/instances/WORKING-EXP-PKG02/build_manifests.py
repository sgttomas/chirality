#!/usr/bin/env python3
"""Build exact-self-excluding package and parent manifests."""

from __future__ import annotations

import csv
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"
PARENT = RUN / "instances/WORKING-EXP-PKG02"
SNAP = RUN / "snapshots/package"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def row(path: Path) -> list[str]:
    data = path.read_bytes()
    try:
        lines = len(data.decode("utf-8").splitlines())
    except UnicodeDecodeError:
        lines = 0
    return ["{REPO_ROOT}/" + path.relative_to(ROOT).as_posix(), sha(path), str(len(data)), str(lines)]


def write_manifest(path: Path, files: list[Path]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["path", "sha256", "bytes", "lines"])
        writer.writerows(row(item) for item in sorted(files))


def main() -> None:
    snapshot_manifest = SNAP / "MANIFEST.tsv"
    snapshot_files = [item for item in SNAP.rglob("*") if item.is_file() and item != snapshot_manifest]
    write_manifest(snapshot_manifest, snapshot_files)

    parent_manifest = PARENT / "MANIFEST.tsv"
    files = [
        item
        for item in PARENT.iterdir()
        if item.is_file() and item != parent_manifest
    ]
    files += sorted((RUN / "candidates/PIP-PKG02").rglob("*"))
    files = [item for item in files if item.is_file()]
    for child in ("BATCH-AUTHOR-PKG02", "BATCH-VERIFY-PKG02"):
        child_root = PARENT / "children" / child
        files += [item for item in child_root.iterdir() if item.is_file()]
    files += [snapshot_manifest, RUN / "RUNTIME_EVENTS.jsonl", RUN / "RUNTIME_SUMMARY.json"]
    unique = sorted(set(files))
    assert parent_manifest not in unique
    write_manifest(parent_manifest, unique)
    print(f"snapshot_rows={len(snapshot_files)} parent_rows={len(unique)}")


if __name__ == "__main__":
    main()
