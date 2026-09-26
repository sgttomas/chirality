#!/usr/bin/env python3
"""Consequence scan: which verbatim quotations of a prior S2 contract, held in a
contract OUTSIDE the S2 set, stop being verbatim once the S2 candidates land.

For each ScopeOfWork.md under projects/pec/execution/PKG-*/1_Working/ that is not
one of the seven S2 targets, every blockquote block (columns 0-3) and every
double-quoted or backticked span of 40+ characters is normalized (blockquote
markers stripped, whitespace collapsed). A span that occurs in a PRIOR S2
contract is reported with whether it still occurs in that deliverable's
CANDIDATE. Spans that also occur in an accepted upstream source (registers,
decomposition, PRD, AGENTS.md, scope-change snapshots, decision records,
dependency registers) are shared quotations and are skipped. Read-only; stdlib only. Informational: the packet discloses the
STALE lines as consequences for their owning nodes; it writes none of them.

Usage: scan_external_quotes.py --tree <pre-act export root> --prep <prep dir>
"""
import argparse, re
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--tree", required=True); ap.add_argument("--prep", required=True)
a = ap.parse_args()
tree, prep = Path(a.tree), Path(a.prep)
S2 = ["DEL-01-01", "DEL-01-06", "DEL-02-03", "DEL-02-04", "DEL-02-05", "DEL-02-06", "DEL-02-07"]

def norm(s):
    s = "\n".join(re.sub(r"^ {0,3}> ?", "", l) for l in s.splitlines())
    return re.sub(r"\s+", " ", s).strip()

# Text that also occurs in an accepted source (registers, decomposition, PRD, scope-change
# snapshots, decision records) is a shared upstream quotation, not a quotation of the
# S2 contract's own voice; such spans are skipped.
upstream = []
for g in ["projects/pec/execution/_Decomposition/*.csv", "projects/pec/execution/_Decomposition/*.md",
          "projects/pec/docs/PRD.md", "projects/pec/AGENTS.md", "projects/pec/execution/_ScopeChange/**/*.md",
          "projects/pec/execution/_Coordination/_DECISIONS/**/*.md", "projects/pec/execution/PKG-*/1_Working/*/Dependencies.csv"]:
    for f in tree.glob(g):
        upstream.append(norm(f.read_text(encoding="utf-8")).replace('""', '"'))
UP = "\n".join(upstream)

prior, cand = {}, {}
for d in S2:
    p = sorted(tree.glob(f"projects/pec/execution/PKG-*/1_Working/{d}_*/ScopeOfWork.md"))[0]
    prior[d] = norm(p.read_text(encoding="utf-8"))
    c = sorted(prep.glob(f"candidates/projects/pec/execution/PKG-*/1_Working/{d}_*/ScopeOfWork.md"))[0]
    cand[d] = norm(c.read_text(encoding="utf-8"))

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
seen = set()
for f in sorted(tree.glob("projects/pec/execution/PKG-*/1_Working/DEL-*/ScopeOfWork.md")):
    owner = f.parent.name[:9]
    if owner in S2: continue
    for sp in spans(f.read_text(encoding="utf-8")):
        n = norm(sp)
        if len(n) < 40: continue
        # a blockquote may wrap its own markup; test the whole span and each sentence
        pieces = [n] + [x.strip() for x in re.split(r"(?<=[.;:])\s+", n) if len(x.strip()) >= 40]
        pieces = [x for x in pieces if "ID-shaped text" not in x]  # carve-out boilerplate is not a quotation
        for d in S2:
            hits = [x for x in pieces if x in prior[d] and x not in UP]
            if not hits: continue
            gone = [x for x in hits if x not in cand[d]]
            key = (owner, d, (gone or hits)[0])
            if key in seen: break
            seen.add(key)
            tag = "STALE" if gone else "KEPT"
            if gone: n_stale += 1
            else: n_kept += 1
            print(f"{tag} {owner} quotes {d}: {(gone or hits)[0][:140]!r}")
            break
print(f"SUMMARY stale={n_stale} kept={n_kept}")
