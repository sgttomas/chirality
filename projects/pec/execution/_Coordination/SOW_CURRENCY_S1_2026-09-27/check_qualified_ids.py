#!/usr/bin/env python3
"""Qualified-citation check for the S1 (provisional D-PEC-104) candidates.

Every qualified citation `DEL-XX-YY/PFX-NNN` in an S1 candidate must resolve:
  - to an ID defined in that deliverable's S1 candidate, when DEL-XX-YY is an
    S1 target (all S1 postimages land together);
  - otherwise, to an ID defined in DEL-XX-YY's ScopeOfWork.md at the
    observation commit (read with `git show`), including the D-PEC-100 S2
    contracts now on main.
A definition is `**PFX-NNN**` at a list item or table cell start. A
candidate's qualified citation of its OWN ID is INFO (retired or quoted
form). A citation listed in an entry of --allow-retired (form
DEL-XX-YY/PFX-NNN) is reported as INFO when the cited ID is not defined:
the candidate cites it as retired, and the allowance must be stated in the
packet. Citations inside a line that also contains the word "retired" are
reported as INFO-RETIRED-CONTEXT when unresolved, so the reviewer can
confirm the retired reading; they still count as failures unless allowed.
Usage: check_qualified_ids.py --prep <dir> --gitdir <repo> --observation <commit>
                              [--allow-retired DEL-XX-YY/PFX-NNN ...]
Read-only; stdlib only.
"""
import argparse, re, subprocess, sys
from pathlib import Path
ap = argparse.ArgumentParser()
ap.add_argument("--prep", required=True); ap.add_argument("--gitdir", required=True)
ap.add_argument("--observation", required=True); ap.add_argument("--allow-retired", nargs="*", default=[])
a = ap.parse_args(); prep = Path(a.prep)
DEF = re.compile(r"(?m)^(?:\s*[-|]\s*|\|\s*)\*\*([A-Z]{2,4}-\d{3})\*\*")
cands = {}
for f in sorted(prep.glob("candidates/projects/pec/execution/PKG-*/1_Working/DEL-*/ScopeOfWork.md")):
    cands[f.parent.name[:9]] = f.read_text(encoding="utf-8")
ls = subprocess.run(["git", "-C", a.gitdir, "ls-tree", "-r", "--name-only", a.observation, "projects/pec/execution/"],
                    capture_output=True, text=True).stdout.splitlines()
mainsow = {}
for p in ls:
    m = re.match(r"projects/pec/execution/PKG-[^/]+/1_Working/(DEL-\d\d-\d\d)_[^/]+/ScopeOfWork\.md$", p)
    if m: mainsow[m.group(1)] = p
_defs = {}
def defs(d):
    if d not in _defs:
        if d in cands: _defs[d] = set(DEF.findall(cands[d]))
        elif d in mainsow:
            t = subprocess.run(["git", "-C", a.gitdir, "show", f"{a.observation}:{mainsow[d]}"], capture_output=True).stdout.decode()
            _defs[d] = set(DEF.findall(t))
        else: _defs[d] = None
    return _defs[d]
n = bad = 0
for d, t in cands.items():
    seen = set()
    for line in t.splitlines():
        for tgt, i in re.findall(r"(DEL-\d\d-\d\d)/([A-Z]{2,4}-\d{3})", line):
            if (tgt, i) in seen: continue
            seen.add((tgt, i))
            if tgt == d:
                print(f"INFO {d} cites its own {i} ({'defined' if i in defs(d) else 'not defined: retired or quoted form'})"); continue
            n += 1
            ds = defs(tgt)
            where = "S1 candidate" if tgt in cands else (f"main {a.observation}" if ds is not None else "no ScopeOfWork.md")
            ok = ds is not None and i in ds
            if not ok and f"{tgt}/{i}" in a.allow_retired:
                print(f"INFO {d} cites {tgt}/{i} [{where}] not defined: allowed as retired"); continue
            if not ok:
                bad += 1
                tag = "FAIL" + (" (retired context)" if "retired" in line.lower() else "")
                print(f"{tag} {d} cites {tgt}/{i} [{where}]")
            else:
                print(f"PASS {d} cites {tgt}/{i} [{where}]")
print(f"RESULT {'PASS' if not bad else 'FAIL'} {n-bad}/{n}")
sys.exit(1 if bad else 0)
