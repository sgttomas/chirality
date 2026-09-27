#!/usr/bin/env python3
"""Edge delta of the strict graph (ACTIVE EXECUTION rows with DELIVERABLE targets) between the pre-extraction
basis commit and the working tree. Run from the repository root; writes Evidence/edge_delta.csv."""
import csv, glob, io, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
EX = "projects/chirality-app-dev/execution"
BASE = "0ca5ffcca2c2044b2d5e79201de9741b80b31585"


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
with open(os.path.join(HERE, "Evidence", "edge_delta.csv"), "w", newline="", encoding="utf-8") as fh:
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
print(open(os.path.join(HERE, "Evidence", "edge_delta.csv")).read())
