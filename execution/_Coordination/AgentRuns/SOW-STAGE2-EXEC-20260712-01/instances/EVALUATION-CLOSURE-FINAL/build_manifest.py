#!/usr/bin/env python3
"""Bind every final-evaluation snapshot artifact except this derived manifest."""

from __future__ import annotations

import hashlib
from pathlib import Path


SNAPSHOT = Path(__file__).resolve().parents[2] / "snapshots/CONVERSION_CLOSURE/final_evaluation"


def main() -> int:
    rows: list[str] = ["path\tsha256\tbytes"]
    for path in sorted(SNAPSHOT.rglob("*")):
        if not path.is_file() or path.name == "MANIFEST.tsv":
            continue
        data = path.read_bytes()
        rows.append(f"{path.relative_to(SNAPSHOT)}\t{hashlib.sha256(data).hexdigest()}\t{len(data)}")
    (SNAPSHOT / "MANIFEST.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f"PASS bound={len(rows) - 1} manifest_sha256={hashlib.sha256((SNAPSHOT / 'MANIFEST.tsv').read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
