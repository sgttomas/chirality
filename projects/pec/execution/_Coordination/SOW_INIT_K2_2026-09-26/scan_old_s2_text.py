#!/usr/bin/env python3
"""Old-S2-text check for the K2 (provisional D-PEC-103) candidates.

D-PEC-100 replaced the seven S2 contracts. A K2 candidate must not quote prior
S2 text that the replacement dropped. For each K2 candidate, every blockquote
block (columns 0-3), every double-quoted span and every backticked span of 40+
characters, and each sentence of 40+ characters inside one, is normalized
(blockquote markers stripped, whitespace collapsed). A span that occurs in a
PRIOR S2 contract (read at --prior, the D-PEC-100 preimage commit) and not in
that deliverable's CURRENT contract (read at --current) is STALE and fails the
check. Spans that also occur in an accepted upstream source at --current
(registers, decomposition, PRD, AGENTS.md, scope-change snapshots, decision
records, dependency registers) are shared quotations and are skipped. Spans
that occur in a current S2 contract are listed as CURRENT (informational).
Read-only; stdlib only.
Usage: scan_old_s2_text.py --prep <prep dir> --gitdir <repo> --prior <commit> --current <commit>
Exit 0 when no STALE span is found; 1 otherwise.
"""
import argparse, fnmatch, re, subprocess, sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--prep", required=True); ap.add_argument("--gitdir", required=True)
ap.add_argument("--prior", required=True); ap.add_argument("--current", required=True)
a = ap.parse_args()
prep = Path(a.prep)
S2 = ["DEL-01-01", "DEL-01-06", "DEL-02-03", "DEL-02-04", "DEL-02-05", "DEL-02-06", "DEL-02-07"]
K2 = ["DEL-08-06", "DEL-10-13"]

def git(*args):
    return subprocess.run(["git", "-C", a.gitdir, *args], capture_output=True)
def ls(c): return git("ls-tree", "-r", "--name-only", c).stdout.decode().splitlines()
def show(c, p):
    r = git("show", f"{c}:{p}")
    return r.stdout.decode("utf-8") if r.returncode == 0 else None
def norm(s):
    s = "\n".join(re.sub(r"^ {0,3}> ?", "", l) for l in s.splitlines())
    return re.sub(r"\s+", " ", s).strip()

cur_paths = ls(a.current)
up = []
for g in ["projects/pec/execution/_Decomposition/*", "projects/pec/docs/PRD.md", "projects/pec/AGENTS.md",
          "projects/pec/execution/_ScopeChange/*.md", "projects/pec/execution/_Coordination/_DECISIONS/*.md",
          "projects/pec/execution/PKG-*/1_Working/*/Dependencies.csv"]:
    for p in cur_paths:
        if fnmatch.fnmatch(p, g) and (p.endswith(".md") or p.endswith(".csv")):
            t = show(a.current, p)
            if t: up.append(norm(t).replace('""', '"'))
UP = "\n".join(up)

def contract(c, d, paths):
    hit = [p for p in paths if re.fullmatch(rf"projects/pec/execution/PKG-[^/]+/1_Working/{d}_[^/]+/ScopeOfWork\.md", p)]
    return norm(show(c, hit[0])) if len(hit) == 1 else ""
prior_paths = ls(a.prior)
prior = {d: contract(a.prior, d, prior_paths) for d in S2}
current = {d: contract(a.current, d, cur_paths) for d in S2}

def spans(text):
    out, block = [], []
    for line in text.splitlines():
        if re.match(r"^ {0,3}>", line): block.append(line)
        else:
            if block: out.append("\n".join(block)); block = []
    if block: out.append("\n".join(block))
    for m in re.finditer(r'"([^"\n]{40,})"', text): out.append(m.group(1))
    for m in re.finditer(r'`([^`\n]{40,})`', text): out.append(m.group(1))
    return out

stale = cur = 0
for d in K2:
    hits = sorted(prep.glob(f"candidates/projects/pec/execution/PKG-*/1_Working/{d}_*/ScopeOfWork.md"))
    if len(hits) != 1:
        print(f"FAIL {d} candidate not found exactly once"); stale += 1; continue
    seen = set()
    for sp in spans(hits[0].read_text(encoding="utf-8")):
        n = norm(sp)
        if len(n) < 40: continue
        pieces = [n] + [x.strip() for x in re.split(r"(?<=[.;:])\s+", n) if len(x.strip()) >= 40]
        pieces = [x for x in pieces if "ID-shaped text" not in x]
        for s2 in S2:
            for x in pieces:
                if x in UP or (d, s2, x) in seen: continue
                if x in prior[s2] and x not in current[s2]:
                    seen.add((d, s2, x)); stale += 1
                    print(f"STALE {d} quotes prior {s2} text dropped by D-PEC-100: {x[:160]!r}")
                elif x in current[s2]:
                    seen.add((d, s2, x)); cur += 1
                    print(f"CURRENT {d} quotes current {s2} text: {x[:160]!r}")
print(f"RESULT {'PASS' if not stale else 'FAIL'} stale={stale} current={cur}")
sys.exit(1 if stale else 0)
