#!/usr/bin/env python3
"""Build and verify the exact self-excluding verifier manifest."""
from pathlib import Path
import hashlib

here = Path(__file__).resolve().parent
manifest = here / "MANIFEST.tsv"
paths = sorted(p for p in here.rglob("*") if p.is_file() and p != manifest and "__pycache__" not in p.parts)
with manifest.open("w", encoding="utf-8", newline="") as out:
    out.write("sha256\tbytes\tpath\n")
    for path in paths:
        data = path.read_bytes()
        out.write(f"{hashlib.sha256(data).hexdigest()}\t{len(data)}\t{path.relative_to(here).as_posix()}\n")
for line in manifest.read_text(encoding="utf-8").splitlines()[1:]:
    digest, size, rel = line.split("\t", 2)
    data = (here / rel).read_bytes()
    assert hashlib.sha256(data).hexdigest() == digest and len(data) == int(size)
