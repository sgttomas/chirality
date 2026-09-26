#!/usr/bin/env python3
"""B6 checkpoint-3 precondition check (read-only)."""
import csv, hashlib, sys, pathlib
R = pathlib.Path("/Users/ryan/ai-env/projects/chirality/.claude/worktrees/agent-a2942849b8715f72c")
P = R / "projects/pec"
E = P / "execution"
def h(p): return hashlib.sha256(p.read_bytes()).hexdigest()
fails = 0
def chk(label, path, exp):
    global fails
    if not path.exists():
        print(f"FAIL {label}: missing {path}"); fails += 1; return
    got = h(path)
    ok = got == exp
    print(f"{'OK  ' if ok else 'FAIL'} {label}: {got}")
    if not ok: fails += 1
D = E / "_Decomposition"
live = [
 ("SOFTWARE_DECOMP.md", D/"SOFTWARE_DECOMP.md", "dc2b84791454ac888e692bfa507221f5d4a588c63bb8ab5005cc00343b119660"),
 ("ScopeLedger.csv", D/"ScopeLedger.csv", "83152a94d91c75da1205f98aec712f901529af4da562f02f5f1124b3ba3fd9df"),
 ("Deliverables.csv", D/"Deliverables.csv", "b8628fc4c7b32b66eae373e19eb943ccaa866125e79119172b82614a01d3d65a"),
 ("ContextBudgetQA.csv", D/"ContextBudgetQA.csv", "2a1941050d06e5e07f6cde629d0abf0c2d80acde1983139e6c1918cfca9eb0df"),
 ("Companion_Inventory.csv", D/"Companion_Inventory.csv", "7c8a24a868ff03415c4440055dc099aaf7e2d87cca8dc0267e77d1a676976ef8"),
 ("docs/PRD.md", P/"docs/PRD.md", "fff27a66cd23c758cf50609ee028c58f4fb643f23ee7f6f801eb2362dfffdc32"),
 ("projects/pec/AGENTS.md", P/"AGENTS.md", "c9d3b44dfb5b07cff9790d58a67ff02825e297fcf0d2e290ab1599bf59ee197a"),
 ("_ScopeChange/_LATEST.md", E/"_ScopeChange/_LATEST.md", "e92b3b16a48cd72288c8b6eddc08d62e3e79e0c9bec521864ee7d5484a307d24"),
 ("_Decomposition/_LATEST.md", D/"_LATEST.md", "626feaafa213c3fe4995640a42a0a7606a1bd89a200ebf2e588afd4209a212dd"),
 ("DEL-04-03 _CONTEXT.md", E/"PKG-04_Orientation_Services/1_Working/DEL-04-03_Citation_freshness_stamping/_CONTEXT.md", "a505c2686af7c6d51fe4d1d8dad25bcadd3a5d9c59372c3f9226d31fed2263da"),
 ("DEL-08-01 _CONTEXT.md", E/"PKG-08_API_Access/1_Working/DEL-08-01_Unix_socket_server_token_scoped_access/_CONTEXT.md", "151e1e34330a58467ef0f9aa28a3283b50b84bf5f563b03039f5c6bcd9273985"),
 ("DEL-08-03 _CONTEXT.md", E/"PKG-08_API_Access/1_Working/DEL-08-03_Compact_citation_bearing_response_format/_CONTEXT.md", "4644758f07a93eb203bce19533916fbf4e55d52e867895f2a87a5b99b4aec73d"),
]
print("== live preimages ==")
for l, p, e in live: chk(l, p, e)
print("== group-2 ACCEPTED_MANIFEST.csv ==")
man = E/"_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_2026-09-25/ACCEPTED_MANIFEST.csv"
for row in csv.DictReader(man.open()):
    p = R/row["Path"]
    tag = row["Path"].split("/")[-1]
    if tag in ("Decision_Log.md", "Handoff_State.md"):
        got = h(p)
        print(f"INFO {row['Path']}: live {got} (manifest {row['SHA256']}; boundary: {row['AcceptanceBoundary']})")
        continue
    chk(row["Path"], p, row["SHA256"])
print("== group-2 record, amendment 1 ==")
for f in ["SCA-006_GROUP-2_2026-09-25/DECISION.md","SCA-006_GROUP-2_2026-09-25/ACCEPTED_MANIFEST.csv","SCA-006_GROUP-2_2026-09-25/Handoff_State.md","SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/DECISION.md"]:
    p = E/"_ScopeChange/checkpoint_snapshots"/f; print(f"INFO {f}: {h(p)}")
a1 = (E/"_ScopeChange/checkpoint_snapshots/SCA-006_GROUP-2_AMENDMENT-1_2026-09-26/DECISION.md").read_text()
ok = "## Verification rule" in a1
print(f"{'OK  ' if ok else 'FAIL'} amendment 1 carries Verification rule section"); fails += (not ok)
reg = (E/"_Coordination/_DECISIONS/_REGISTER.md").read_text()
ok = "| D-PEC-97 |" in reg
print(f"{'OK  ' if ok else 'FAIL'} register row D-PEC-97 present"); fails += (not ok)
lat = (E/"_ScopeChange/_LATEST.md").read_text()
print("INFO _ScopeChange/_LATEST.md names SCA-005:", "SCA-005_2026-09-23_2139" in lat)
print("FAILS", fails)
sys.exit(1 if fails else 0)
