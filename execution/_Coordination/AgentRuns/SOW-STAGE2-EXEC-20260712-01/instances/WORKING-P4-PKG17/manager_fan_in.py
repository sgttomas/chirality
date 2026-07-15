#!/usr/bin/env python3
import csv, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
INST = RUN / "instances/WORKING-P4-PKG17"
CAND = RUN / "candidates/W_P4/PIP-PKG17"
BATCHES = [
    ("B1", INST/"children/AUTHOR-B1", INST/"children/VERIFY-B1", 5, 166, 1528, 25, 5, 35, 991, 243, 15, 45, 8),
    ("B2", INST/"children/AUTHOR-B2", INST/"children/VERIFY-B2", 4, 180, 1593, 20, 4, 28, 842, 199, 12, 36, 7),
]

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p): return list(csv.DictReader(p.open(), delimiter="\t"))
def reproduce(path, base, root_relative=False):
    checked=[]
    for r in rows(path):
        p = ROOT/r["path"] if root_relative else base/r["path"]
        checked.append(p.is_file() and sha(p)==r["sha256"] and p.stat().st_size==int(r["bytes"]))
    return len(checked), all(checked)
def write(name,text): (INST/name).write_text(text)
def combine_tsv(source_name, dest_name):
    combined=[]; fields=None
    for _,a,_,*rest in BATCHES:
        rs=rows(a/source_name)
        if rs and fields is None: fields=list(rs[0])
        combined.extend(rs)
    with (INST/dest_name).open("w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter="\t",lineterminator="\n")
        w.writeheader(); w.writerows(combined)
    return combined

author_counts=[]; verifier_counts=[]; member_rows=[]
for bid,a,v,members,mappings,lines,repl,sims,probes,acount,vcount,cands,live,checks in BATCHES:
    aj=json.loads((a/"STATUS.json").read_text()); vj=json.loads((v/"STATUS.json").read_text())
    assert aj["status"]=="PASS" and vj["status"]=="PASS_UNCHANGED"
    assert aj["members_complete"]==vj["members_complete"]==members
    assert aj["mappings_passed"]==vj["mappings_passed"]==mappings
    assert aj["source_lines_covered"]==vj["source_lines_covered"]==lines
    assert aj["replacement_rows"]==vj["replacement_rows"]==repl
    assert aj["inverse_rows"]==vj["inverse_rows"]==repl
    assert aj["simulations_passed"]==vj["simulations_passed"]==sims
    assert vj["negative_probes_passed"]==probes and vj["candidate_bindings_unchanged"]==cands
    assert vj["live_bindings_passed"]==live and vj["method_bindings_passed"]==29
    ac,aok=reproduce(a/"MANIFEST.tsv", a, root_relative=True)
    vc,vok=reproduce(v/"MANIFEST.tsv", v)
    assert (ac,aok,vc,vok)==(acount,True,vcount,True)
    author_counts.append(ac); verifier_counts.append(vc)
    for r in rows(a/"MEMBER_RESULTS.tsv"):
        d=CAND/r["deliverable_id"]; fin=json.loads((d/"finalization.json").read_text())
        assert sha(d/"evidence/ScopeOfWork.md")==r["evidence_sha256"]
        assert sha(d/"production/ScopeOfWork.md")==r["production_sha256"]==fin["production_scope_of_work_sha256"]
        assert sha(d/"finalization.json")==r["finalization_sha256"]
        member_rows.append(r)

assert len(member_rows)==9 and sum(int(r["covered_lines"]) for r in member_rows)==3121
members=combine_tsv("MEMBER_RESULTS.tsv","MEMBER_RESULTS.tsv")
replacements=combine_tsv("REPLACEMENT_ROWS.tsv","REPLACEMENT_MANIFEST.tsv")
rollbacks=combine_tsv("INVERSE_ROWS.tsv","ROLLBACK_MANIFEST.tsv")
simulations=combine_tsv("SIMULATIONS.tsv","SIMULATION.tsv")
assert len(replacements)==len(rollbacks)==45 and len(simulations)==9

write("B2_VERIFIER_ACCEPTANCE.md","""# B2 Verifier Acceptance

Status: `PASS_UNCHANGED_ACCEPTED`

WORKING_ITEMS reproduced the terminal VERIFY-B2 schema and exact counts. The
independent return covers 4/4 members, 180 mappings, 1,593/1,593 lines, exact
20 replacement and 20 inverse rows, four simulations, 28 negative probes, and
12 initial/post candidate hashes unchanged. The 199-binding self-excluding
manifest and AUTHOR-B2 842/842 plus 12/12 candidate manifests reproduce. No
repair, discrepancy, blocker, waiver, unknown, candidate write, or project
write occurred. B2 is closed as derivative evidence, not integration truth.
""")
write("MANAGER_VALIDATION.json",json.dumps({
  "status":"PASS","package":"PKG-17","batches":2,"members":9,"mappings":346,
  "source_lines":3121,"replacement_rows":45,"inverse_rows":45,"simulations":9,
  "negative_probes":63,"author_manifest_bindings":author_counts,
  "verifier_manifest_bindings":verifier_counts,"candidate_bindings_unchanged":27,
  "live_bindings":81,"method_bindings_per_batch":29,"project_check_groups":[8,7],
  "verifiers":["PASS_UNCHANGED","PASS_UNCHANGED"],"blockers":[],"unknowns":[],
  "waivers":[],"reruns":[]},indent=2)+"\n")
write("RUNTIME_SUMMARY.json",json.dumps({
  "status":"COMPLETE","author_sessions":2,"verifier_sessions":2,
  "terminals":["AUTHOR-B1:PASS","VERIFY-B1:PASS_UNCHANGED","AUTHOR-B2:PASS","VERIFY-B2:PASS_UNCHANGED"],
  "failed_manager_dispatch_attempts":2,
  "retained_mechanical_attempts":["runtime completed-session capacity retention before AUTHOR-B1","AUTHOR-B1 stale PKG-16 PKG00 wrapper expectation","AUTHOR-B2 no-HTML tuple spelling"],
  "repairs":"owned mechanical evidence/dispatch mechanics only; bindings rebuilt and affected checks rerun",
  "verifier_repairs":0,"native_token_context_telemetry":"UNAVAILABLE_NOT_INFERRED"},indent=2)+"\n")
write("CHECKS.md","""# WORKING-P4-PKG17 Checks

Status: `PASS`

- Manager preflight: PASS; 9 members, 3,121 lines, 81/81 live bindings.
- B1 author/verifier: 5/5; 166 mappings; 1,528/1,528 lines; 25+25 rows;
  five simulations; 35 probes; 15/15 candidate hashes; verifier
  `PASS_UNCHANGED` with 243 evidence bindings.
- B2 author/verifier: 4/4; 180 mappings; 1,593/1,593 lines; 20+20 rows;
  four simulations; 28 probes; 12/12 candidate hashes; verifier
  `PASS_UNCHANGED` with 199 evidence bindings.
- Aggregate: 9/9; 346 mappings; exact 45 replacement and 45 inverse rows;
  nine simulations; 63 negative probes; all registered project checks pass.
- Retained attempts are mechanical, fully rebound, and have no semantic,
  source, lifecycle, authority, acceptance, candidate, or project effect.
""")
write("CONTAINMENT.md","""# WORKING-P4-PKG17 Containment

Status: `PASS`

Writes are contained to `candidates/W_P4/PIP-PKG17/**` and
`instances/WORKING-P4-PKG17/**`. Exactly 27 candidate-family files exist.
Live PKG-17 project worktree/index diff is empty. No Git, lifecycle,
dependency-truth, PKG-00, integration, release, reliance, rollback-execution,
retirement, or H2 write occurred. Both verifiers changed no candidate or
author output.
""")
write("PACKAGE_HANDOFF.md","""# WORKING-P4-PKG17 Terminal Handoff

Verdict: `PASS`

Accepted upstream: W-P4 preflight, sealed PKG-17 release, and accepted PKG-16
terminal PASS bound to `main@e8f59a63372f38d9e788ac39b39995558f5aba73`
and preflight manifest
`e3c0ba738b4109fe8ab3eccaaab1e76e82e213b5e6b27f9dd6632c7716682faf`.

Derivative package: complete and current for `DEL-17-01..09`. Two fresh
authors PASS and two fresh evidence-only verifiers PASS_UNCHANGED across the
two frozen serial batches. Coverage is 9/9 members, 346 mappings,
3,121/3,121 lines, exact 45 replacement rows, 45 inverse rows, nine
simulations, 63 negative probes, all project checks, telemetry, and immutable
candidates.

Closure: package candidate/evidence preparation is closed. Blockers, unknowns,
waivers, contamination, and rerun requirements: none. This does not accept
lifecycle or authorize integration, release, reliance, rollback execution,
retirement, or H2. Next owner is direct `RECONCILIATION` for aggregate W-P4
fan-in; no redundant child layer is authorized.
""")
write("RETURN.md","""# WORKING-P4-PKG17 Terminal Return

RUN_STATUS: `PASS`

Exactly `DEL-17-01..09` are complete in two bounded serial derivative batches.
Both accepted author returns are `PASS`; both fresh evidence-only verifier
returns are `PASS_UNCHANGED`. Aggregate coverage is 9/9 members, 346/346
production-bound mappings, 3,121/3,121 physical source lines, exact 45
replacement and 45 inverse rows, nine simulations, and 63/63 negative probes.
All registered checks pass; all 27 candidate-family hashes are unchanged.

Safe mechanical dispatch/author-evidence defects were retained, repaired only
in owned mechanics/evidence, fully rebound, and rerun. No semantic, source,
lifecycle, authority, or acceptance defect occurred. Blockers, unknowns,
waivers, contamination, project writes, and rerun requirements are zero.
Derivative preparation is closed and handed directly to RECONCILIATION; no
integration or lifecycle authority is implied.
""")
write("STATUS.json",json.dumps({
  "schema":"chirality-agent-return/v1","run_id":"SOW-STAGE2-EXEC-20260712-01",
  "instance_id":"WORKING-P4-PKG17","role":"WORKING_ITEMS","package_id":"PKG-17",
  "status":"PASS","terminal":True,"batches_complete":2,"batches_expected":2,
  "members_complete":9,"members_expected":9,"source_lines_covered":3121,
  "source_lines_total":3121,"mappings_passed":346,"replacement_rows":45,
  "inverse_rows":45,"simulations":9,"authors":["PASS","PASS"],
  "verifiers":["PASS_UNCHANGED","PASS_UNCHANGED"],"blockers":[],"unknowns":[],
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
print(json.dumps({"status":"PASS","members":9,"mappings":346,"manifest_bindings":len(entries)},indent=2))
