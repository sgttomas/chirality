#!/usr/bin/env python3
"""Render apply_s4p.py from apply_s4p.template.py: fill TARGETS (preimage hashes
read at --commit, postimage hashes of the staged candidates) and PINNED (hashes
read at --commit). Preparation aid, not bound; the rendered apply_s4p.py is the
bound script. Stdlib only.

Usage: build_apply_s4p.py --gitdir <repo> --commit <sha> --prep <prep dir>
"""
import argparse, hashlib, subprocess
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--gitdir", required=True); ap.add_argument("--commit", required=True); ap.add_argument("--prep", required=True)
a = ap.parse_args()
prep = Path(a.prep)
E = "projects/pec/execution/"
S4 = ["DEL-04-01", "DEL-04-02", "DEL-08-01", "DEL-08-03", "DEL-08-04", "DEL-04-03", "DEL-03-04", "DEL-10-03"]

def show(rel):
    r = subprocess.run(["git", "-C", a.gitdir, "show", f"{a.commit}:{rel}"], capture_output=True, check=True)
    return r.stdout
def h(b): return hashlib.sha256(b).hexdigest()

folders = {}
for d in S4:
    c = sorted(prep.glob(f"candidates/{E}PKG-*/1_Working/{d}_*/ScopeOfWork.md"))
    assert len(c) == 1, d
    folders[d] = c[0].parent.relative_to(prep / "candidates").as_posix() + "/"

tl = []
for d in S4:
    rel = folders[d] + "ScopeOfWork.md"
    pre = h(show(rel)); post = h((prep / "candidates" / rel).read_bytes())
    tl.append(f'    E + "{rel[len(E):]}":\n        ("{pre}",\n         "{post}"),')

pins = [E + "_Decomposition/SOFTWARE_DECOMP.md", E + "_Decomposition/Deliverables.csv",
        E + "_Decomposition/ScopeLedger.csv", E + "_Decomposition/ContextBudgetQA.csv",
        "projects/pec/docs/PRD.md", "projects/pec/AGENTS.md",
        E + "_Coordination/_DECISIONS/D-PEC-99_REMAINING_RETIREMENT_2026-09-26/EXHIBIT_MOVED_ITEMS.md"]
pins += [folders[d] + "_STATUS.md" for d in S4]
# registers holding the ACTIVE rows that quote an S4 contract, and the registers whose
# repaired cells the Part B corrections restate
pins += [E + "PKG-08_API_Access/1_Working/DEL-08-04_Orientation_latency_budget_p95_100_ms/Dependencies.csv",
         E + "PKG-08_API_Access/1_Working/DEL-08-05_SSE_delta_presence_subscription/Dependencies.csv",
         folders["DEL-04-02"] + "Dependencies.csv", folders["DEL-04-03"] + "Dependencies.csv"]
pl = []
for p in pins:
    k = f'E + "{p[len(E):]}"' if p.startswith(E) else f'"{p}"'
    pl.append(f'    {k}:\n        "{h(show(p))}",')

t = (prep / "apply_s4p.template.py").read_text(encoding="utf-8")
t = t.replace("@@TARGETS@@", "\n".join(tl)).replace("@@PINNED@@", "\n".join(pl))
t = t.replace("# Read-only files the act re-verifies (values at origin/main 125cfacc1).",
              f"# Read-only files the act re-verifies (values at origin/main {a.commit[:9]}).")
(prep / "apply_s4p.py").write_text(t, encoding="utf-8")
print(f"wrote {prep / 'apply_s4p.py'}  sha256 {h(t.encode('utf-8'))}  targets {len(tl)} pins {len(pl)}")
