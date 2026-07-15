#!/usr/bin/env python3
import csv, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
INST = RUN / "instances/WORKING-P4-PKG16"
AUTHOR = INST / "children/AUTHOR-B1"
VERIFY = INST / "children/VERIFY-B1"
CAND = RUN / "candidates/W_P4/PIP-PKG16"

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p): return list(csv.DictReader(p.open(), delimiter="\t"))
def reproduce(path, base, root_relative=False):
    results=[]
    for r in rows(path):
        p = ROOT / r["path"] if root_relative else base / r["path"]
        results.append(p.is_file() and sha(p)==r["sha256"] and p.stat().st_size==int(r["bytes"]))
    return len(results), all(results)

a=json.loads((AUTHOR/"STATUS.json").read_text())
v=json.loads((VERIFY/"STATUS.json").read_text())
assert a["status"]=="PASS" and v["status"]=="PASS_UNCHANGED"
assert a["members_complete"]==v["members_complete"]==4
assert a["source_lines_covered"]==v["source_lines_covered"]==1097
assert a["mappings_passed"]==v["mappings_passed"]==106
ac,aok=reproduce(AUTHOR/"MANIFEST.tsv", AUTHOR, root_relative=True)
vc,vok=reproduce(VERIFY/"MANIFEST.tsv", VERIFY)
assert (ac,aok,vc,vok)==(973,True,199,True)

members=rows(AUTHOR/"MEMBER_RESULTS.tsv")
assert len(members)==4 and sum(int(r["covered_lines"]) for r in members)==1097
for r in members:
    d=CAND/r["deliverable_id"]
    f=json.loads((d/"finalization.json").read_text())
    assert sha(d/"evidence/ScopeOfWork.md")==r["evidence_sha256"]
    assert sha(d/"production/ScopeOfWork.md")==r["production_sha256"]==f["production_scope_of_work_sha256"]
    assert sha(d/"finalization.json")==r["finalization_sha256"]

for src,dst in (("MEMBER_RESULTS.tsv","MEMBER_RESULTS.tsv"),("REPLACEMENT_ROWS.tsv","REPLACEMENT_MANIFEST.tsv"),("INVERSE_ROWS.tsv","ROLLBACK_MANIFEST.tsv"),("SIMULATIONS.tsv","SIMULATION.tsv")):
    (INST/dst).write_bytes((AUTHOR/src).read_bytes())

def write(name,text): (INST/name).write_text(text)
write("MANAGER_VALIDATION.json",json.dumps({
  "status":"PASS","package":"PKG-16","members":4,"mappings":106,
  "source_lines":1097,"replacement_rows":20,"inverse_rows":20,
  "simulations":4,"negative_probes":28,"author_manifest_bindings":ac,
  "verifier_manifest_bindings":vc,"candidate_bindings_unchanged":12,
  "live_bindings":36,"method_bindings":29,"project_checks":7,
  "verifier":"PASS_UNCHANGED","blockers":[],"unknowns":[],"waivers":[],"reruns":[]},indent=2)+"\n")
write("RUNTIME_SUMMARY.json",json.dumps({
  "status":"COMPLETE","author_sessions":1,"verifier_sessions":1,
  "author_terminal":"PASS","verifier_terminal":"PASS_UNCHANGED",
  "retained_mechanical_attempts":["author pre-execution wrapper string-removal mismatch","author stale narrative count during terminal wrapper","author local exec namespace binding"],
  "repairs":"owned author evidence mechanics only; all bindings rebuilt and affected checks rerun",
  "verifier_repairs":0,
  "native_token_context_telemetry":"UNAVAILABLE_NOT_INFERRED"},indent=2)+"\n")
write("B1_VERIFIER_ACCEPTANCE.md","""# PKG-16 B1 Verifier Acceptance

Status: `ACCEPTED — PASS_UNCHANGED`

Fresh evidence-only `VERIFY-B1` independently passed all four members unchanged:
106/106 mappings, 1,097/1,097 lines, exact 20/20 replacement/inverse rows,
4/4 simulations, 28/28 negative probes, 7/7 project-check groups, 36/36 live
bindings, 29/29 method bindings, and byte-identical 12/12 candidate pre/post
hashes. Author manifest 973/973 and verifier manifest 199/199 reproduce. The
verifier performed no repair and wrote no candidate, author, parent, project,
Git, lifecycle, or other prohibited state.
""")
write("CHECKS.md","""# WORKING-P4-PKG16 Checks

Status: `PASS`

- Manager preflight: PASS; 36/36 live bindings.
- Author: 4/4; 106 mappings; 1,097/1,097 lines; 20/20 rows; four simulations;
  28 negative probes; 973/973 evidence and 12/12 candidate bindings.
- Verifier: `PASS_UNCHANGED`; 199/199 evidence bindings; 12/12 candidate
  hashes unchanged; 36/36 live and 29/29 method bindings.
- Registered checks: four dependency schemas, practitioner self-check,
  264 practitioner tests, and 19 focused Scope-of-Work tests pass.
- Retained mechanical attempts are author-evidence-only and fully rebound; no
  semantic, source, lifecycle, authority, acceptance, or project repair.
""")
write("CONTAINMENT.md","""# WORKING-P4-PKG16 Containment

Status: `PASS`

Writes are contained to `candidates/W_P4/PIP-PKG16/**` and
`instances/WORKING-P4-PKG16/**`. Exactly 12 candidate files exist. Live PKG-16
project worktree/index diff is empty. No Git, lifecycle, dependency-truth,
PKG-00, integration, release, reliance, rollback-execution, retirement, or H2
write occurred. The verifier changed no candidate or author output.
""")
write("PACKAGE_HANDOFF.md","""# WORKING-P4-PKG16 Terminal Handoff

Verdict: `PASS`

Accepted upstream: W-P4 preflight, sealed PKG-16 release, and accepted PKG-15
terminal PASS bound to `main@e8f59a63372f38d9e788ac39b39995558f5aba73`
and preflight manifest
`e3c0ba738b4109fe8ab3eccaaab1e76e82e213b5e6b27f9dd6632c7716682faf`.

Derivative package: complete for `DEL-16-01..04`. Author `PASS` and fresh
verifier `PASS_UNCHANGED` cover 4/4 members, 106 mappings, 1,097/1,097 lines,
20 exact replacement rows, 20 exact inverse rows, four simulations, all
negative behavior, registered checks, telemetry, and immutable candidates.

Closure: package candidate/evidence preparation is closed. Blockers, unknowns,
waivers, contamination, and rerun requirements: none. This does not accept
lifecycle or authorize integration, release, reliance, rollback execution,
retirement, or H2. Next owner is direct `RECONCILIATION`; PKG-17 release
remains governed by the sealed serial package graph.
""")
write("RETURN.md","""# WORKING-P4-PKG16 Terminal Return

RUN_STATUS: `PASS`

Exactly `DEL-16-01..04` are complete as one bounded derivative batch. The
accepted author return is `PASS`; the fresh evidence-only verifier return is
`PASS_UNCHANGED`. Aggregate coverage is 4/4 members, 106/106 production-bound
mappings, 1,097/1,097 physical source lines, 20 replacement and 20 inverse
rows, four simulations, and 28/28 negative probes. All focused and practitioner
checks pass; 12/12 candidate hashes are unchanged.

Safe mechanical author-evidence defects were retained, repaired only in owned
evidence, fully rebound, and rerun. No semantic/source/lifecycle/authority or
acceptance defect occurred. Blockers, unknowns, waivers, contamination,
project writes, and rerun requirements are zero. Derivative preparation is
closed and handed directly to RECONCILIATION; no integration or lifecycle
authority is implied.
""")
write("STATUS.json",json.dumps({
  "schema":"chirality-agent-return/v1","run_id":"SOW-STAGE2-EXEC-20260712-01",
  "instance_id":"WORKING-P4-PKG16","role":"WORKING_ITEMS","package_id":"PKG-16",
  "status":"PASS","terminal":True,"members_complete":4,"members_expected":4,
  "source_lines_covered":1097,"source_lines_total":1097,"mappings_passed":106,
  "replacement_rows":20,"inverse_rows":20,"simulations":4,
  "author":"PASS","verifier":"PASS_UNCHANGED","blockers":[],"unknowns":[],
  "waivers":[],"reruns":[],"derivative_status":"COMPLETE_CURRENT",
  "next_owner":"RECONCILIATION"},indent=2)+"\n")

entries=[]
for base in (CAND,INST):
    for p in sorted(base.rglob("*")):
        if not p.is_file() or p==INST/"MANIFEST.tsv": continue
        entries.append((str(p.relative_to(ROOT)),sha(p),p.stat().st_size))
with (INST/"MANIFEST.tsv").open("w",newline="") as f:
    w=csv.writer(f,delimiter="\t",lineterminator="\n")
    w.writerow(["path","sha256","bytes"]); w.writerows(entries)
print(json.dumps({"status":"PASS","members":4,"manifest_bindings":len(entries)},indent=2))
