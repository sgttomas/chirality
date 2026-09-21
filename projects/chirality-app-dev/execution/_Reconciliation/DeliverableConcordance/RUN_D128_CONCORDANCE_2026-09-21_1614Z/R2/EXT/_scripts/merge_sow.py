#!/usr/bin/env python3
"""Merge the two SOW half ledgers (SOW_A, SOW_B) into R2/EXT/SOW/SOW_claims.csv.
Rows are copied byte-for-byte as CSV records (no field edited), A then B, one header,
one final #END record. Also concatenates the two half notes into SOW/SOW_notes.md and
writes SOW/MERGE_MANIFEST.md with the input and output SHA-256 values."""
import csv, io, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extlib import EXT, sha, rel

halves = [os.path.join(EXT, h, "SOW_claims.csv") for h in ("SOW_A", "SOW_B")]
out_dir = os.path.join(EXT, "SOW"); os.makedirs(out_dir, exist_ok=True)
out = os.path.join(out_dir, "SOW_claims.csv")
hdr0 = None; recs = []
for p in halves:
    with open(p, encoding="utf-8", newline="") as fh:
        rs = list(csv.reader(fh))
    assert rs[-1] == ["#END"], p
    if hdr0 is None: hdr0 = rs[0]
    assert rs[0] == hdr0, "header mismatch"
    recs.append((p, rs[1:-1]))
keys = [r[0] for _, rs in recs for r in rs]
dups = sorted({k for k in keys if keys.count(k) > 1})
if dups: sys.exit(f"duplicate ClaimKeys across halves: {dups}")
buf = io.StringIO(); w = csv.writer(buf, lineterminator="\n")
w.writerow(hdr0)
for _, rs in recs: w.writerows(rs)
buf.write("#END\n")
open(out, "w", encoding="utf-8", newline="").write(buf.getvalue())
notes = ["# SOW notes (merged from the two half workers)\n",
         "Merged by `_scripts/merge_sow.py`. Half A covers SOW-001..042 and half B SOW-043..084;",
         "each half's notes follow unchanged.\n"]
for hname in ("SOW_A", "SOW_B"):
    notes.append(f"\n---\n\n# Half {hname[-1]} (`{hname}/SOW_notes.md`)\n")
    notes.append(open(os.path.join(EXT, hname, "SOW_notes.md"), encoding="utf-8").read())
open(os.path.join(out_dir, "SOW_notes.md"), "w", encoding="utf-8").write("\n".join(notes))
man = ["# SOW merge manifest\n", "| File | Rows | SHA-256 |", "|---|---:|---|"]
for p, rs in recs: man.append(f"| `{rel(p)}` | {len(rs)} | `{sha(p)}` |")
man.append(f"| `{rel(out)}` (merged) | {len(keys)} | `{sha(out)}` |")
open(os.path.join(out_dir, "MERGE_MANIFEST.md"), "w").write("\n".join(man) + "\n")
print("\n".join(man))
