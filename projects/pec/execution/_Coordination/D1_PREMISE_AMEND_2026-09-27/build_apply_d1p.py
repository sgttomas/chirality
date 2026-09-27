#!/usr/bin/env python3
"""Render apply_d1p.py from apply_d1p.template.py for the D1 premise amendment
(provisional D-PEC-105). Preparation aid, not bound; the rendered apply_d1p.py
is the bound script. Stdlib only; read-only on the repository.

Fills
  TARGETS  from <prep>/targets.json: group, key, preimage SHA-256 (read with
           `git show <basis>:<path>` and required to equal targets.json's
           preimage_sha256) and postimage SHA-256 (of <prep>/candidates/<path>
           as it is now). Every target in targets.json needs its candidate.
  PINNED   SHA-256 at <basis> of the read-only files the act re-verifies.
  one comment line naming the basis commit (full and short SHA).
Rendering twice at the same basis with the same candidates is byte-identical.

Usage: build_apply_d1p.py --prep <prep dir> --basis <commit> --out <path>
                          [--gitdir <repo>] [--template <path>]
  --gitdir    defaults to the Git top level containing --prep
  --template  defaults to apply_d1p.template.py next to this script
"""
import argparse, hashlib, json, subprocess, sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--prep", required=True); ap.add_argument("--basis", required=True); ap.add_argument("--out", required=True)
ap.add_argument("--gitdir"); ap.add_argument("--template")
a = ap.parse_args()
prep = Path(a.prep).resolve()
gitdir = a.gitdir or subprocess.run(["git", "-C", str(prep), "rev-parse", "--show-toplevel"],
                                    capture_output=True, text=True, check=True).stdout.strip()
tpl = Path(a.template) if a.template else Path(__file__).resolve().with_name("apply_d1p.template.py")
E = "projects/pec/execution/"
W = E + "PKG-00_Architecture_Runway_Contracts/1_Working/"
DELS = {"DEL-00-01": W + "DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/",
        "DEL-00-03": W + "DEL-00-03_v2_SPEC_seed/"}
NEVER = ("_STATUS.md", "_REVIEW.md", "MEMORY.md")

def git(*args):
    return subprocess.run(["git", "-C", gitdir, *args], capture_output=True, check=True).stdout
def h(b): return hashlib.sha256(b).hexdigest()
def die(msg): print("FAIL " + msg); sys.exit(1)

basis = git("rev-parse", "--verify", a.basis + "^{commit}").decode().strip()
targets = json.loads((prep / "targets.json").read_text(encoding="utf-8"))
if not targets.get("targets"): die("targets.json names no targets")
tl, keys, paths = [], set(), set()
for t in targets["targets"]:
    key, grp, rel = t["key"], t["group"], t["path"]
    if grp not in ("A", "P"): die(f"{key} group {grp!r} is not A or P")
    if key in keys or rel in paths: die(f"{key} duplicate key or path")
    keys.add(key); paths.add(rel)
    if not rel.startswith("projects/pec/") or Path(rel).name in NEVER or ".." in Path(rel).parts:
        die(f"{key} path {rel} is outside the act's reach")
    pre = h(git("show", f"{basis}:{rel}"))
    if pre != t["preimage_sha256"]: die(f"{key} preimage at {basis[:9]} is {pre}, targets.json says {t['preimage_sha256']}")
    c = prep / "candidates" / rel
    if not c.is_file(): die(f"{key} candidate missing: {c}")
    post = h(c.read_bytes())
    if post == pre: die(f"{key} candidate equals its preimage (nothing to amend)")
    k = f'E + "{rel[len(E):]}"' if rel.startswith(E) else f'"{rel}"'
    tl.append(f'    {k}:\n        ("{grp}", "{key}",\n         "{pre}",\n         "{post}"),')
if not any(t["group"] == "A" for t in targets["targets"]): die("no group-A target")

pins = [E + "_Decomposition/SOFTWARE_DECOMP.md", E + "_Decomposition/Deliverables.csv",
        E + "_Decomposition/ScopeLedger.csv", E + "_Decomposition/ContextBudgetQA.csv",
        "projects/pec/docs/PRD.md", "projects/pec/AGENTS.md"]
for d in ("DEL-00-01", "DEL-00-03"):
    pins += [DELS[d] + f for f in ("_STATUS.md", "_REVIEW.md", "Review_Findings.csv",
                                   "Dependencies.csv", "_CONTEXT.md", "_REFERENCES.md")]
if set(pins) & paths: die("a pinned file is also a target")
pl = []
for p in pins:
    k = f'E + "{p[len(E):]}"' if p.startswith(E) else f'"{p}"'
    pl.append(f'    {k}:\n        "{h(git("show", f"{basis}:{p}"))}",')

t = tpl.read_text(encoding="utf-8")
for slot in ("@@TARGETS@@", "@@PINNED@@", "@@BASIS_LINE@@"):
    if t.count(slot) != 1: die(f"template slot {slot} occurs {t.count(slot)} times")
t = (t.replace("@@TARGETS@@", "\n".join(tl)).replace("@@PINNED@@", "\n".join(pl))
      .replace("@@BASIS_LINE@@", f"# Rendered by build_apply_d1p.py at basis commit {basis} ({basis[:9]}); PINNED values and preimages read there."))
out = Path(a.out)
out.write_text(t, encoding="utf-8")
print(f"wrote {out}  sha256 {h(t.encode('utf-8'))}  basis {basis[:9]}  targets {len(tl)} "
      f"(A {sum(1 for x in targets['targets'] if x['group'] == 'A')}, P {sum(1 for x in targets['targets'] if x['group'] == 'P')})  pins {len(pl)}")
