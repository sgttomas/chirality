#!/usr/bin/env python3
"""S2 quotation-currency scan for the S4 (provisional D-PEC-102) contracts.

D-PEC-100 replaced seven S2 contracts. This scan lists, for each S4 contract,
every quoted span (a blockquote block at columns 0-3, or a double-quoted span of
40+ characters, and each sentence of 40+ characters inside one) that occurs in a
PRIOR S2 contract (read at --prior-commit, the D-PEC-100 preimages) and in no
accepted upstream source, no contract outside the S2 and S4 sets and no top-level
_Coordination record, and reports whether it still occurs in the CURRENT S2
contract (the D-PEC-100 postimage in --tree).

With --candidates, the S4 contracts are read from the candidate folder instead
of the tree, so the scan shows what the candidates still quote. Informational:
STALE lines are what a currency pass must bring current; KEPT lines are
quotations of S2 text that the D-PEC-100 postimage still carries.

Usage: scan_s2_quotes.py --tree <export root at the observation commit>
                         --gitdir <repo> --prior-commit <commit before the D-PEC-100 act>
                         [--candidates <prep dir>]
Read-only; stdlib only.
"""
import argparse, re, subprocess
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--tree", required=True); ap.add_argument("--gitdir", required=True)
ap.add_argument("--prior-commit", required=True); ap.add_argument("--candidates")
a = ap.parse_args()
tree = Path(a.tree)
S2 = ["DEL-01-01", "DEL-01-06", "DEL-02-03", "DEL-02-04", "DEL-02-05", "DEL-02-06", "DEL-02-07"]
S4 = ["DEL-04-01", "DEL-04-02", "DEL-08-01", "DEL-08-03", "DEL-08-04", "DEL-04-03", "DEL-03-04", "DEL-10-03"]

def norm(s):
    s = "\n".join(re.sub(r"^ {0,3}> ?", "", l) for l in s.splitlines())
    return re.sub(r"\s+", " ", s).strip()

upstream = []
for g in ["projects/pec/execution/_Decomposition/*.csv", "projects/pec/execution/_Decomposition/*.md",
          "projects/pec/docs/PRD.md", "projects/pec/AGENTS.md", "projects/pec/execution/_ScopeChange/**/*.md",
          "projects/pec/execution/_Coordination/_DECISIONS/**/*.md", "projects/pec/execution/PKG-*/1_Working/*/Dependencies.csv"]:
    for f in tree.glob(g):
        upstream.append(norm(f.read_text(encoding="utf-8")).replace('""', '"'))
# A span that another contract outside S2 and S4, or a top-level coordination record
# (for example the 2026-07-25 DAG plan exhibit), also carries is quoted from there, not
# from an S2 contract; those files join the skip set.
for f in tree.glob("projects/pec/execution/PKG-*/1_Working/DEL-*/ScopeOfWork.md"):
    if f.parent.name[:9] not in S2 + S4:
        upstream.append(norm(f.read_text(encoding="utf-8")).replace('""', '"'))
for f in tree.glob("projects/pec/execution/_Coordination/*.md"):
    upstream.append(norm(f.read_text(encoding="utf-8")).replace('""', '"'))
UP = "\n".join(upstream)

def s2path(d):
    return sorted(tree.glob(f"projects/pec/execution/PKG-*/1_Working/{d}_*/ScopeOfWork.md"))[0]
prior, cur = {}, {}
for d in S2:
    p = s2path(d)
    rel = p.relative_to(tree).as_posix()
    r = subprocess.run(["git", "-C", a.gitdir, "show", f"{a.prior_commit}:{rel}"], capture_output=True)
    prior[d] = norm(r.stdout.decode("utf-8"))
    cur[d] = norm(p.read_text(encoding="utf-8"))

def spans(text):
    out, block = [], []
    for line in text.splitlines():
        if re.match(r"^ {0,3}>", line):
            block.append(line)
        else:
            if block: out.append("\n".join(block)); block = []
    if block: out.append("\n".join(block))
    for m in re.finditer(r'"([^"\n]{40,})"', text): out.append(m.group(1))
    return out

n_stale = n_kept = 0
for d4 in S4:
    if a.candidates:
        f = sorted(Path(a.candidates).glob(f"candidates/projects/pec/execution/PKG-*/1_Working/{d4}_*/ScopeOfWork.md"))[0]
    else:
        f = sorted(tree.glob(f"projects/pec/execution/PKG-*/1_Working/{d4}_*/ScopeOfWork.md"))[0]
    seen = set()
    for sp in spans(f.read_text(encoding="utf-8")):
        n = norm(sp)
        if len(n) < 40: continue
        pieces = [n] + [x.strip() for x in re.split(r"(?<=[.;:])\s+", n) if len(x.strip()) >= 40]
        pieces = [x for x in pieces if "ID-shaped text" not in x]
        for d in S2:
            hits = [x for x in pieces if x in prior[d] and x not in UP]
            if not hits: continue
            gone = [x for x in hits if x not in cur[d]]
            key = (d, (gone or hits)[0])
            if key in seen: break
            seen.add(key)
            tag = "STALE" if gone else "KEPT"
            if gone: n_stale += 1
            else: n_kept += 1
            print(f"{tag} {d4} quotes {d}: {(gone or hits)[0][:160]!r}")
            break
print(f"SUMMARY stale={n_stale} kept={n_kept}")
