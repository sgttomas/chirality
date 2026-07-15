#!/usr/bin/env python3
"""Build the self-excluding immutable snapshot manifest."""

from __future__ import annotations

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
rows = []
for path in sorted(p for p in ROOT.rglob("*") if p.is_file() and p.name != "MANIFEST.tsv"):
    data = path.read_bytes()
    rows.append(f"{path.relative_to(ROOT).as_posix()}\t{len(data)}\t{hashlib.sha256(data).hexdigest()}")
(ROOT / "MANIFEST.tsv").write_text("path\tbytes\tsha256\n" + "\n".join(rows) + "\n", encoding="utf-8")
