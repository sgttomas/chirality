#!/usr/bin/env python3
"""Edge delta of the strict graph (ACTIVE EXECUTION rows with DELIVERABLE targets) between a basis commit (argv[1])
and the working tree. Run from the repository root; writes Evidence/<argv[2]>."""
import csv, glob, io, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EX = "projects/chirality-app-dev/execution"
BASE = sys.argv[1] if len(sys.argv) > 1 else "63e5de1f2f19c3a1dab073babbadfbfcc6199e70"
OUTNAME = sys.argv[2] if len(sys.argv) > 2 else "edge_delta.csv"


def edges(reader_rows):
    out = {}
    for r in reader_rows:
        if r["Status"] == "ACTIVE" and r["DependencyClass"] == "EXECUTION" and r["TargetType"] == "DELIVERABLE" and r["TargetDeliverableID"]:
            a, b = r["FromDeliverableID"], r["TargetDeliverableID"]
            e = (b, a) if r["Direction"] == "UPSTREAM" else (a, b)
            out.setdefault(e, []).append(r["DependencyID"])
    return out


pre, post = {}, {}
for p in sorted(glob.glob(f"{EX}/PKG-*/1_Working/DEL-*/Dependencies.csv")):
    old = subprocess.run(["git", "show", f"{BASE}:{p}"], capture_output=True, text=True).stdout
    for e, ids in edges(csv.DictReader(io.StringIO(old))).items():
        pre.setdefault(e, []).extend(ids)
    for e, ids in edges(csv.DictReader(open(p, encoding="utf-8"))).items():
        post.setdefault(e, []).extend(ids)
with open(os.path.join(HERE, "Evidence", OUTNAME), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh, lineterminator="\n")
    w.writerow(["Change", "From", "To", "RowsBefore", "RowsAfter"])
    for e in sorted(set(pre) | set(post)):
        if e in pre and e not in post:
            w.writerow(["REMOVED", e[0], e[1], ";".join(pre[e]), ""])
        elif e in post and e not in pre:
            w.writerow(["ADDED", e[0], e[1], "", ";".join(post[e])])
        elif sorted(pre[e]) != sorted(post[e]):
            w.writerow(["ROWS_CHANGED", e[0], e[1], ";".join(pre[e]), ";".join(post[e])])
print(len(pre), len(post))
print(OUTNAME, BASE[:9])
print(open(os.path.join(HERE, "Evidence", OUTNAME)).read())
