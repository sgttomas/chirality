#!/usr/bin/env python3
"""Drafting aid (informational, not bound): locate the source of every quotation
in one Scope of Work contract, and flag quotations that no current source holds.

Spans examined: each blockquote block (and each sentence of 30+ characters in
it) and each double-quoted span ("..." or curly quotes) of 20+ characters.
Normalization: blockquote markers stripped, `**` dropped, whitespace collapsed,
CSV doubled quotes undoubled. For each span the aid reports the first matching
source in this order:
  UPSTREAM  <path>   PRD, decomposition, registers, Dependencies.csv,
                     _DEPENDENCIES.md, _CONTEXT.md, _REFERENCES.md, _STATUS.md,
                     decision records, scope-change snapshots, AGENTS.md,
                     loops.json/schema, tools/scaffolding, docs/ (tree = --tree)
  OTHER-SOW <DEL>    another deliverable's current ScopeOfWork.md
  S2-STALE  <DEL>    only in an S2 contract's pre-D-PEC-100 bytes (--s2-prior commit),
                     not in its current bytes: a quotation of replaced S2 text
  SELF               only in this contract (own voice or unsourced)
  NOTFOUND           nowhere
Usage: audit_quotes.py --tree <export> --gitdir <repo> --s2-prior <commit> <contract> [...]
Read-only; stdlib only.
"""
import argparse, glob, re, subprocess
from pathlib import Path
ap = argparse.ArgumentParser()
ap.add_argument("--tree", required=True); ap.add_argument("--gitdir", required=True)
ap.add_argument("--s2-prior", required=True); ap.add_argument("contracts", nargs="+")
a = ap.parse_args(); T = Path(a.tree)
S2 = ["DEL-01-01", "DEL-01-06", "DEL-02-03", "DEL-02-04", "DEL-02-05", "DEL-02-06", "DEL-02-07"]
def norm(s):
    s = "\n".join(re.sub(r"^ {0,3}> ?", "", l) for l in s.splitlines())
    s = s.replace("**", "").replace('""', '"').replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()
up = []
for g in ["projects/pec/docs/**/*.md", "projects/pec/execution/_Decomposition/*", "projects/pec/AGENTS.md",
          "projects/pec/execution/PKG-*/1_Working/*/Dependencies.csv", "projects/pec/execution/PKG-*/1_Working/*/_DEPENDENCIES.md",
          "projects/pec/execution/PKG-*/1_Working/*/_CONTEXT.md", "projects/pec/execution/PKG-*/1_Working/*/_REFERENCES.md",
          "projects/pec/execution/PKG-*/1_Working/*/_STATUS.md", "projects/pec/execution/PKG-*/1_Working/*/MEMORY.md",
          "projects/pec/execution/PKG-*/_CONTEXT.md", "projects/pec/execution/_Coordination/_DECISIONS/**/*.md",
          "projects/pec/execution/_ScopeChange/**/*", "projects/pec/v2/config/*.json", "projects/pec/loop/*.md",
          "projects/pec/execution/_Coordination/_COORDINATION.md", "projects/pec/execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md",
          "projects/pec/v2/src/pec_v2/core/*.py", "docs/*.md", "_DomainEngines/_DECISIONS/_REGISTER.md", "_DomainEngines/profiles/pec.yaml",
          "projects/pec/execution/_Coordination/WorkGraphs/**/*.md", "projects/pec/execution/_Evaluation/**/*.md"]:
    for f in T.glob(g):
        if f.is_file():
            try: up.append((f.relative_to(T).as_posix(), norm(f.read_text(encoding="utf-8"))))
            except UnicodeDecodeError: pass
sows = {}
for f in T.glob("projects/pec/execution/PKG-*/1_Working/DEL-*/ScopeOfWork.md"):
    sows[f.parent.name[:9]] = (f.relative_to(T).as_posix(), norm(f.read_text(encoding="utf-8")))
prior = {}
for d in S2:
    rel = sows[d][0]
    r = subprocess.run(["git", "-C", a.gitdir, "show", f"{a.s2_prior}:{rel}"], capture_output=True)
    prior[d] = norm(r.stdout.decode("utf-8"))
def spans(text):
    out, block, start = [], [], 0
    lines = text.splitlines()
    for i, line in enumerate(lines, 1):
        if re.match(r"^ {0,3}>", line):
            if not block: start = i
            block.append(line)
        elif block:
            out.append((start, "\n".join(block))); block = []
    if block: out.append((start, "\n".join(block)))
    for i, line in enumerate(lines, 1):
        for m in re.finditer(r'"([^"\n]{20,}?)"|“([^”\n]{20,}?)”', line):
            out.append((i, m.group(1) or m.group(2)))
    return out
for c in a.contracts:
    own = Path(c).parent.name[:9]
    text = Path(c).read_text(encoding="utf-8")
    print(f"=== {own} {c}")
    counts = {}
    for ln, sp in spans(text):
        n = norm(sp)
        pieces = [n] + ([x.strip() for x in re.split(r"(?<=[.;:])\s+", n) if len(x.strip()) >= 30] if sp.lstrip().startswith(">") else [])
        for x in pieces:
            tag = None
            for rel, body in up:
                if x in body: tag = f"UPSTREAM {rel}"; break
            if not tag:
                for d, (rel, body) in sorted(sows.items()):
                    if d != own and x in body: tag = f"OTHER-SOW {d}"; break
            if not tag:
                for d in S2:
                    if x in prior[d] and x not in sows[d][1]: tag = f"S2-STALE {d}"; break
            if not tag:
                tag = "SELF" if x in sows.get(own, ("", ""))[1] else "NOTFOUND"
            k = tag.split()[0]; counts[k] = counts.get(k, 0) + 1
            if k != "UPSTREAM":
                print(f"L{ln} {tag}: {x[:160]!r}")
            break_after = k == "UPSTREAM" and x is n
            if break_after: break
    print(f"--- {own} counts {counts}")
