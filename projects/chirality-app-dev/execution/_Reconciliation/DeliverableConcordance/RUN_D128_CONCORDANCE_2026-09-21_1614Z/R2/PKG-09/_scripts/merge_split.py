#!/usr/bin/env python3
"""Merge the two sealed split ledgers of one deliverable (brief step 3) into <DEL>/<DEL>_claims.csv.
Usage: merge_split.py DEL-09-04
Rows are copied byte-for-value (csv round trip, all fields quoted as needed), P1 rows first then P2, in each
part's own order. Fails on duplicate ClaimKeys or header mismatch. Prints part and merged SHA-256."""
import csv, hashlib, io, os, sys
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d = sys.argv[1]
def rows(p):
    t = open(p, encoding="utf-8").read().rstrip()
    t = t[:-6] if t.endswith('"#END"') else (t[:-4] if t.endswith("#END") else sys.exit(f"no #END in {p}"))
    r = csv.reader(io.StringIO(t)); h = next(r); return h, [x for x in r if x]
parts = [os.path.join(P, d, p, d + "_claims.csv") for p in ("P1", "P2")]
hs, allr = None, []
for p in parts:
    h, rs = rows(p)
    if hs and h != hs: sys.exit("header mismatch")
    hs = h; allr += rs
    print(os.path.relpath(p, P), len(rs), hashlib.sha256(open(p, "rb").read()).hexdigest())
keys = [r[0] for r in allr]
dup = sorted({k for k in keys if keys.count(k) > 1})
if dup: sys.exit(f"duplicate keys: {dup}")
out = os.path.join(P, d, d + "_claims.csv")
with open(out, "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(hs); w.writerows(allr); fh.write("#END\n")
print(os.path.relpath(out, P), len(allr), hashlib.sha256(open(out, "rb").read()).hexdigest())
