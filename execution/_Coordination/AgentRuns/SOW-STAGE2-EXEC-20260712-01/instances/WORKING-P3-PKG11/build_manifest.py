#!/usr/bin/env python3
from pathlib import Path
import hashlib
here=Path(__file__).resolve().parent; manifest=here/"MANIFEST.tsv"
paths=sorted(p for p in here.rglob("*") if p.is_file() and p!=manifest and "__pycache__" not in p.parts)
with manifest.open("w",encoding="utf-8",newline="") as f:
 f.write("sha256\tbytes\tpath\n")
 for p in paths:
  b=p.read_bytes(); f.write(f"{hashlib.sha256(b).hexdigest()}\t{len(b)}\t{p.relative_to(here).as_posix()}\n")
for line in manifest.read_text().splitlines()[1:]:
 h,n,r=line.split("\t",2); b=(here/r).read_bytes(); assert hashlib.sha256(b).hexdigest()==h and len(b)==int(n)

