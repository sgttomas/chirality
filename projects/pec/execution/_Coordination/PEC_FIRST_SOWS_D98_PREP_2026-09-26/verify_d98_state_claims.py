#!/usr/bin/env python3
"""Check the commit-anchored state claims of the D-PEC-98 candidates against Git.

Every claim is read with `git show <commit>:<path>` at the commit the candidate
names, so the result does not depend on the current checkout. Commits are
immutable; the check is reproducible from any clone that holds them.

Usage: verify_d98_state_claims.py <repo_root>
Exit 0 when every check passes; 1 otherwise. Stdlib only; read-only.
"""
import hashlib, re, subprocess, sys

repo = sys.argv[1]
def show(c, p):
    r = subprocess.run(["git", "-C", repo, "show", f"{c}:{p}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None
def sha(c, p):
    b = show(c, p); return hashlib.sha256(b).hexdigest() if b is not None else None
def tree(c, p):
    r = subprocess.run(["git", "-C", repo, "ls-tree", "--name-only", c, p + "/"], capture_output=True, text=True)
    return [l for l in r.stdout.splitlines() if l]

PK = "projects/pec/execution/"
D8 = PK + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-08_Work_graph_parser"
D9 = PK + "PKG-02_File_Truth_Parsers/1_Working/DEL-02-09_MEMORY_run_index_parser"
P1 = PK + "PKG-01_Service_Core_Store/1_Working/"
PIN, OBS = "c9e5cd87d", "53145aaeb"
checks = []
def ok(cond, name): checks.append((bool(cond), name))

reg = {"SOFTWARE_DECOMP.md": "dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660",
       "Deliverables.csv": "b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a",
       "ScopeLedger.csv": "83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df"}
for c in (PIN, OBS):
    for f, h in reg.items(): ok(sha(c, PK + "_Decomposition/" + f) == h, f"{c} {f} {h[:12]}")
    ok(sha(c, "projects/pec/docs/PRD.md") == "fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32", f"{c} PRD.md v2.3 fff27a66cd23")
    ok(sha(c, "docs/templates/MEMORY_TEMPLATE.md").startswith("5a9564f4663b"), f"{c} MEMORY_TEMPLATE 5a9564f4663b")
ok(not tree(PIN, D8) and not tree(PIN, D9), f"{PIN} DEL-02-08/09 folders absent")
ok(sha(PIN, "workflows/construct-local-work-graph/resources/work-graph-template.md") == "4411d0c25b1dc88da182e05660cb061d8e885ab97f4de8f27b05f7d3b0f12261", f"{PIN} template 4411d0c25b1d")
ok(sha(PIN, "workflows/construct-local-work-graph/WORKFLOW.md") == "24268f3545eae68ac86bbfcb830314f5c8539f6da9de08bf4365b14d6f544525", f"{PIN} workflow 24268f3545ea")
ok(sha(OBS, "workflows/construct-local-work-graph/resources/work-graph-template.md") == "5661c6097cee51c770b8f1e6bf765c50ebc3e39c3e51df7173cbcb65e40a6fa6", f"{OBS} template 5661c6097cee")
ok(sha(OBS, "workflows/construct-local-work-graph/WORKFLOW.md") == "3e197c9ddc75d40daa02929dc3df653a66f7d76ab6996239e823bba647dd9dc3", f"{OBS} workflow 3e197c9ddc75")
pin_t = (show(PIN, "workflows/construct-local-work-graph/resources/work-graph-template.md") or b"").decode()
ok("Use PLANNED, READY, ACTIVE, BLOCKED, UNCERTAIN and COMPLETE consistently." in pin_t and "awaiting a human decision" not in pin_t, f"{PIN} template: six-token rule present, second sentence absent")
d96 = PK + "_Coordination/_DECISIONS/D-PEC-96_registry_schema_v2_feed_profiles_proposal_2026-09-25.md"
H4 = "4506597b1bfd6cafd8fc561c688bcb9e803d9c2b04c3abdec9dc05edf155180e"
ok(sha("6281273fa", d96) == H4 and sha("6281273fa^1", d96) != H4, "revision 4 merged to origin/main at 6281273fa")
ok(sha(OBS, d96) == H4, f"{OBS} D-PEC-96 proposal = revision 4")
rev4 = (show(OBS, d96) or b"").decode()
ok("(revision 4)" in rev4 and "`shared-dev-loop`, `loop-receipts-ledger` and `agentruns-json`, each at version 1" in rev4, f"{OBS} revision-4 vocabulary text")
ok(re.search(r"\| `work-graphs` \(S1\) \| ✓ \|", rev4) and re.search(r"\| `memory-run-index` \(S5\) \| ✓ \|", rev4) and "`status-remaining` (S6" not in rev4.split("| Surface (design-note S#)")[1][:900], f"{OBS} shared-dev-loop covers work-graphs and memory-run-index; no status-remaining row")
regtxt = (show(OBS, PK + "_Coordination/_DECISIONS/_REGISTER.md") or b"").decode()
row = next((l for l in regtxt.splitlines() if l.startswith("| D-PEC-96 ")), "")
ok("RULED A / EFFECTIVE ON MERGE" in row and "D-PEC-96_RULING_2026-09-26.md" in row, f"{OBS} register row D-PEC-96 RULED A / EFFECTIVE ON MERGE, ruling record named")
rul = PK + "_Coordination/_DECISIONS/D-PEC-96_RULING_2026-09-26.md"
ok(show(OBS, rul) is not None and show("f90320c1d", rul) is not None and show("f90320c1d^1", rul) is None, "D-PEC-96 ruling record merged at f90320c1d and present at " + OBS)
ok(b"> D-PEC-96: A; migrated; confirm; reject v1; create MEMORY; defaults" in (show(OBS, rul) or b""), f"{OBS} ruling record carries the owner's verbatim direction")
lj = (show(OBS, "projects/pec/v2/config/loops.json") or b"").decode()
ok('"schema_version": 1' in lj and "feed_profiles" not in lj, f"{OBS} v2/config/loops.json schema_version 1, no feed_profiles (registry act not applied)")
def state(c, p):
    m = re.search(r"\*\*Current State:\*\*\s*(\S+)", (show(c, p + "/_STATUS.md") or b"").decode()); return m.group(1) if m else None
for p, s in ((P1 + "DEL-01-01_Record_tier_schema_entity_model", "INITIALIZED"), (P1 + "DEL-01-06_Loop_registry_local_config_default", "INITIALIZED"),
             (P1 + "DEL-01-03_Store_bootstrap_content_minimal_guard", "IN_PROGRESS"), (D8, "OPEN"), (D9, "OPEN")):
    ok(state(OBS, p) == s, f"{OBS} {p.split('/')[-1][:9]} {s}")
ok(sha(OBS, P1 + "DEL-01-01_Record_tier_schema_entity_model/ScopeOfWork.md").startswith("43f1f57a13bb"), f"{OBS} DEL-01-01 SOW 43f1f57a13bb")
ok(sha(OBS, P1 + "DEL-01-06_Loop_registry_local_config_default/ScopeOfWork.md").startswith("5fdcfd968345"), f"{OBS} DEL-01-06 SOW 5fdcfd968345")
ok(sha(OBS, "projects/pec/v2/src/pec_v2/core/content_minimal_guard.py").startswith("740a4a741221"), f"{OBS} guard 740a4a741221")
for dd in (D8, D9):
    ctx = (show(OBS, dd + "/_CONTEXT.md") or b"").decode(); ref = (show(OBS, dd + "/_REFERENCES.md") or b"").decode()
    ok("revision 1.5" in ctx.replace("\n", " ") and "revision 1.5" in ref and "v2.3" in ref, f"{OBS} {dd.split('/')[-1][:9]} context/references name revision 1.5 and PRD v2.3")
    ok(not (show(OBS, dd + "/ScopeOfWork.md")), f"{OBS} {dd.split('/')[-1][:9]} has no ScopeOfWork.md")
fx = ["projects/chirality-piping/execution/_Coordination/WorkGraphs/PIPING_LINTER_SCOPE_20260923/WORK_GRAPH.md",
      "projects/chirality-piping/execution/_Coordination/AgentRuns/PIPING_LINTER_SCOPE_20260923/RECEIPT.md",
      "projects/chirality-piping/execution/_Coordination/WorkGraphs/dec025-clean-base-repair-2026-09-23/WORK_GRAPH.md",
      "projects/chirality-piping/execution/_Coordination/AgentRuns/PIP-DEC025-BASELINE-2026-09-23/EVIDENCE.md",
      "projects/chirality-app-dev/execution/_Coordination/WorkGraphs/replay-session-boundary-2026-09-23/WORK_GRAPH.md"]
for f in fx:
    ok(show("d61981ee2", f) is not None and show("d61981ee2", f) == show("7a00a88df", f) == show(OBS, f), f"fixture blob unchanged d61981ee2 = 7a00a88df = {OBS}: {f.split('/')[-2]}/{f.split('/')[-1]}")
r = subprocess.run(["git", "-C", repo, "ls-tree", "-r", "--name-only", "7a00a88df", "projects"], capture_output=True, text=True).stdout.splitlines()
graphs = [p for p in r if re.fullmatch(r"projects/[^/]+/execution/_Coordination/WorkGraphs/[^/]+/WORK_GRAPH\.md", p)]
ok(len(graphs) == 5, f"7a00a88df canonical work graphs = {len(graphs)} (claimed 5)")
mem = [p for p in r if re.fullmatch(r"projects/[^/]+/execution/PKG-[^/]+/1_Working/DEL-[^/]+/MEMORY\.md", p)]
ok(len(mem) == 156, f"7a00a88df deliverable MEMORY.md files = {len(mem)} (claimed 156)")
runs = [p for p in mem if re.search(rb"^## Runs", show("7a00a88df", p) or b"", re.M)]
ok(len(runs) == 4, f"7a00a88df MEMORY.md with ## Runs = {len(runs)} (claimed 4)")
bad = [n for c, n in checks if not c]
for c, n in checks: print(("PASS " if c else "FAIL ") + n)
print(f"RESULT {'PASS' if not bad else 'FAIL'} {len(checks)-len(bad)}/{len(checks)}")
sys.exit(1 if bad else 0)
