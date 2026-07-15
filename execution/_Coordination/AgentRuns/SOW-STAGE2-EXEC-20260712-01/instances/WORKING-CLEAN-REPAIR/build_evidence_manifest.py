#!/usr/bin/env python3
"""Bind every retained instance artifact except the self-referential manifest."""

from __future__ import annotations

import hashlib
from pathlib import Path


INSTANCE = Path(__file__).resolve().parent
OUTPUT = INSTANCE / "EVIDENCE_MANIFEST.tsv"


def main() -> int:
    paths = sorted(
        path for path in INSTANCE.rglob("*")
        if path.is_file() and path != OUTPUT
    )
    rows = ["sha256\tbytes\tpath"]
    for path in paths:
        payload = path.read_bytes()
        rows.append(
            f"{hashlib.sha256(payload).hexdigest()}\t{len(payload)}\t"
            f"{path.relative_to(INSTANCE).as_posix()}"
        )
    OUTPUT.write_text("\n".join(rows) + "\n", encoding="utf-8")
    print(f"PASS files={len(paths)} sha256={hashlib.sha256(OUTPUT.read_bytes()).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
