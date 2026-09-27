#!/usr/bin/env python3
"""Emit apply_x1p.py from apply_x1p.template.py: bind the candidate postimages,
the one preimage and the pinned read-only files, read at <commit> through Git.
Usage: build_apply_x1p.py <repo> <commit> <prep dir>   (writes <prep dir>/apply_x1p.py)"""
import hashlib, subprocess, sys
from pathlib import Path
repo, commit, prep = sys.argv[1], sys.argv[2], Path(sys.argv[3])
cand = prep / "candidates"
def at(rel):
    return subprocess.run(["git", "-C", repo, "show", f"{commit}:{rel}"], capture_output=True, check=True).stdout
def exists(rel):
    return subprocess.run(["git", "-C", repo, "cat-file", "-e", f"{commit}:{rel}"], capture_output=True).returncode == 0
h = lambda b: hashlib.sha256(b).hexdigest()
E = "projects/pec/execution/"
W = E + "PKG-02_File_Truth_Parsers/1_Working/"
PIN = [E + "_Decomposition/SOFTWARE_DECOMP.md", E + "_Decomposition/Deliverables.csv",
       E + "_Decomposition/ScopeLedger.csv", "projects/pec/docs/PRD.md", "projects/pec/AGENTS.md",
       "projects/pec/v2/config/loops.json", "projects/pec/v2/config/loops.schema.json",
       "projects/pec/v2/config/service_core_posture.json", "projects/pec/v2/tools/check_service_core_posture.py"]
for d in ("DEL-02-03_Receipts_ledger_parser_per_loop_grammars", "DEL-02-08_Work_graph_parser", "DEL-02-09_MEMORY_run_index_parser"):
    PIN += [W + d + "/ScopeOfWork.md"]  # _STATUS.md is not pinned: add-on L, if selected, runs before the act
targets = {}
for f in sorted(p for p in cand.rglob("*") if p.is_file()):
    rel = f.relative_to(cand).as_posix()
    pre = h(at(rel)) if exists(rel) else None
    targets[rel] = (pre, h(f.read_bytes()))
def lit(d, pair):
    lines = ["{"]
    for k, v in d.items():
        if pair: lines.append(f"    {k!r}:\n        ({v[0]!r},\n         {v[1]!r}),")
        else: lines.append(f"    {k!r}:\n        {v!r},")
    lines.append("}")
    return "\n".join(lines)
pinned = {rel: h(at(rel)) for rel in PIN}
src = (prep / "apply_x1p.template.py").read_text()
src = src.replace("@@TARGETS@@", lit(targets, True)).replace("@@PINNED@@", lit(pinned, False))
(prep / "apply_x1p.py").write_text(src)
print(f"targets={len(targets)} creates={sum(1 for v in targets.values() if v[0] is None)} pinned={len(pinned)}")
