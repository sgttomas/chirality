#!/usr/bin/env python3
"""Seal and verify every final run artifact except the manifest itself."""

from __future__ import annotations

import hashlib
from pathlib import Path


RUN = Path(__file__).resolve().parents[1]
REPO = Path(__file__).resolve().parents[7]
MANIFEST = RUN / "ARTIFACT_HASHES.sha256"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    files = sorted(path for path in RUN.rglob("*") if path.is_file() and path != MANIFEST)
    lines = [f"{digest(path)}  {path.relative_to(REPO)}" for path in files]
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")

    checked = 0
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        expected, relpath = line.split("  ", 1)
        if digest(REPO / relpath) != expected:
            raise ValueError(f"hash mismatch: {relpath}")
        checked += 1
    if checked != len(files):
        raise ValueError(f"population mismatch: {checked} != {len(files)}")
    print({"artifacts_sealed": checked, "manifest": str(MANIFEST.relative_to(REPO))})


if __name__ == "__main__":
    main()
