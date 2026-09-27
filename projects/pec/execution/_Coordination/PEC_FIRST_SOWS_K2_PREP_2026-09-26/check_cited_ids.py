#!/usr/bin/env python3
"""Qualified-citation check for the K2 (provisional D-PEC-103) candidates.

Every qualified citation `DEL-XX-YY/PFX-NNN` in a K2 candidate (DEL-08-06,
DEL-10-13) must resolve to an ID defined in the cited contract: the other K2
candidate when it names that deliverable, otherwise the cited deliverable's
ScopeOfWork.md read with `git show <commit>:<path>` at the observation commit.
A definition is `**PFX-NNN**` at a list item or table cell start. Citations on
blockquote lines (columns 0-3) are upstream text and are reported as INFO.
A candidate's citation of its own ID is INFO. Each cited contract is labelled
with the work-graph node that may revise it (S4, S1 or D1 in parallel with this
packet; S2 or S3 already applied), so the parallel packets can keep the IDs.
Read-only; stdlib only.
Usage: check_cited_ids.py --prep <prep dir> --gitdir <repo> --commit <observation commit>
Exit 0 when every own-voice citation resolves; 1 otherwise.
"""
import argparse, re, subprocess, sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--prep", required=True); ap.add_argument("--gitdir", required=True)
ap.add_argument("--commit", required=True)
a = ap.parse_args()
prep = Path(a.prep)
K2 = ["DEL-08-06", "DEL-10-13"]
NODE = {**{d: "S4 (parallel packet)" for d in ["DEL-04-01", "DEL-04-02", "DEL-08-01", "DEL-08-03",
                                                "DEL-08-04", "DEL-04-03", "DEL-03-04", "DEL-10-03"]},
        "DEL-00-03": "D1 (parallel packet)",
        **{d: "S1 (parallel packet; SCA-005 review class)" for d in ["DEL-04-05", "DEL-10-02", "DEL-10-10", "DEL-02-01",
                                                                     "DEL-02-02", "DEL-03-01", "DEL-03-03", "DEL-01-03",
                                                                     "DEL-01-05", "DEL-00-01"]},
        **{d: "S2 (applied, D-PEC-100)" for d in ["DEL-01-01", "DEL-01-06", "DEL-02-03", "DEL-02-04",
                                                   "DEL-02-05", "DEL-02-06", "DEL-02-07"]},
        "DEL-02-08": "S3 (applied, D-PEC-98)", "DEL-02-09": "S3 (applied, D-PEC-98)"}
DEF = re.compile(r"(?m)^(?:\s*[-|]\s*|\|\s*)\*\*([A-Z]{2,4}-\d{3})\*\*")
CIT = re.compile(r"(DEL-\d\d-\d\d)/([A-Z]{2,4}-\d{3})")

def git(*args):
    return subprocess.run(["git", "-C", a.gitdir, *args], capture_output=True, text=True)

paths = git("ls-tree", "-r", "--name-only", a.commit, "projects/pec/execution").stdout.splitlines()
def contract_at_commit(d):
    hits = [p for p in paths if re.fullmatch(rf"projects/pec/execution/PKG-[^/]+/1_Working/{d}_[^/]+/ScopeOfWork\.md", p)]
    if len(hits) != 1: return None, None
    r = git("show", f"{a.commit}:{hits[0]}")
    return (r.stdout if r.returncode == 0 else None), hits[0]

cand = {}
for d in K2:
    hits = sorted(prep.glob(f"candidates/projects/pec/execution/PKG-*/1_Working/{d}_*/ScopeOfWork.md"))
    if len(hits) == 1: cand[d] = hits[0].read_text(encoding="utf-8")
defs_cache = {}
def defs(d):
    if d not in defs_cache:
        if d in cand: txt, where = cand[d], "K2 candidate"
        else: txt, where = contract_at_commit(d)
        defs_cache[d] = (set(DEF.findall(txt)) if txt else None, where)
    return defs_cache[d]

bad = n = 0
for d, txt in cand.items():
    seen = set()
    for line in txt.splitlines():
        quoted = bool(re.match(r"^ {0,3}>", line))
        for tgt, i in CIT.findall(line):
            key = (tgt, i, quoted)
            if key in seen: continue
            seen.add(key)
            if tgt == d:
                print(f"INFO {d} cites its own {i} ({'defined' if i in DEF.findall(txt) else 'NOT defined'})"); continue
            ds, where = defs(tgt)
            ok = ds is not None and i in ds
            label = "K2 sibling candidate" if tgt in K2 else f"{where or 'no contract'} @ {a.commit}; node {NODE.get(tgt, 'other (not in this undertaking)')}"
            if quoted:
                print(f"INFO {d} quotes {tgt}/{i} inside a blockquote [{'defined' if ok else 'not defined'}; {label}]"); continue
            n += 1
            if not ok: bad += 1
            print(("PASS " if ok else "FAIL ") + f"{d} cites {tgt}/{i} [{label}]")
print(f"RESULT {'PASS' if not bad else 'FAIL'} {n-bad}/{n}")
sys.exit(1 if bad else 0)
