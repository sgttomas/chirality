#!/usr/bin/env python3
import csv, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
INST = RUN / "instances/WORKING-P4-PKG14"
AUTHOR = INST / "children/AUTHOR-B1"
VERIFY = INST / "children/VERIFY-B1"
CAND = RUN / "candidates/W_P4/PIP-PKG14"

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p): return list(csv.DictReader(p.open(), delimiter="\t"))
def reproduce_manifest(path, base, root_relative=False):
    out=[]
    for r in rows(path):
        p = ROOT / r["path"] if root_relative else base / r["path"]
        out.append(p.is_file() and sha(p)==r["sha256"] and p.stat().st_size==int(r["bytes"]))
    return len(out), all(out)

a=json.loads((AUTHOR/"STATUS.json").read_text()); v=json.loads((VERIFY/"STATUS.json").read_text())
assert a["status"]=="PASS" and v["status"]=="PASS_UNCHANGED"
assert a["members_complete"]==v["members_complete"]==5
assert a["source_lines_covered"]==v["source_lines_covered"]==1454
assert a["mappings_passed"]==v["mappings_passed"]==158
ac, aok=reproduce_manifest(AUTHOR/"MANIFEST.tsv", AUTHOR, root_relative=True)
vc, vok=reproduce_manifest(VERIFY/"MANIFEST.tsv", VERIFY)
assert (ac,aok,vc,vok)==(923,True,242,True)

members=rows(AUTHOR/"MEMBER_RESULTS.tsv")
assert len(members)==5 and sum(int(r["covered_lines"]) for r in members)==1454
for r in members:
    d=CAND/r["deliverable_id"]
    f=json.loads((d/"finalization.json").read_text())
    assert sha(d/"evidence/ScopeOfWork.md")==r["evidence_sha256"]
    assert sha(d/"production/ScopeOfWork.md")==r["production_sha256"]==f["production_scope_of_work_sha256"]
    assert sha(d/"finalization.json")==r["finalization_sha256"]

for src,dst in (("MEMBER_RESULTS.tsv","MEMBER_RESULTS.tsv"),("REPLACEMENT_ROWS.tsv","REPLACEMENT_MANIFEST.tsv"),("INVERSE_ROWS.tsv","ROLLBACK_MANIFEST.tsv"),("SIMULATIONS.tsv","SIMULATION.tsv")):
    (INST/dst).write_bytes((AUTHOR/src).read_bytes())

validation={
  "status":"PASS", "package":"PKG-14", "members":5, "mappings":158,
  "source_lines":1454, "replacement_rows":25, "inverse_rows":25,
  "simulations":5, "negative_probes":35, "author_manifest_bindings":ac,
  "verifier_manifest_bindings":vc, "candidate_bindings_unchanged":15,
  "live_bindings":45, "method_bindings":29, "verifier":"PASS_UNCHANGED",
  "blockers":[], "unknowns":[], "waivers":[], "reruns":[]}
(INST/"MANAGER_VALIDATION.json").write_text(json.dumps(validation,indent=2)+"\n")
(INST/"RUNTIME_SUMMARY.json").write_text(json.dumps({
  "status":"COMPLETE", "author_sessions":1, "verifier_sessions":1,
  "author_terminal":"PASS", "verifier_terminal":"PASS_UNCHANGED",
  "retained_mechanical_attempts":["manager PRE-1/PRE-2","author zsh-special-variable","verifier wrong-test-path"],
  "repairs":"owned evidence only; all bindings rebuilt and affected checks rerun",
  "native_token_context_telemetry":"UNAVAILABLE_NOT_INFERRED"},indent=2)+"\n")

(INST/"B1_VERIFIER_ACCEPTANCE.md").write_text("""# PKG-14 B1 Verifier Acceptance

Status: `ACCEPTED — PASS_UNCHANGED`

Fresh evidence-only `VERIFY-B1` independently passed all 5 members unchanged:
158/158 mappings, 1,454/1,454 lines, exact 25/25 replacement/inverse rows,
5/5 simulations, 35/35 negative probes, 8/8 project-check groups including
264 practitioner and 19 focused tests, 45/45 live bindings, 29/29 method
bindings, and byte-identical 15/15 candidate pre/post hashes. Author manifest
923/923 and verifier manifest 242/242 reproduce. The verifier performed no
repair and wrote no candidate, author, parent, project, Git, lifecycle, or
other prohibited state. Its retained wrong-test-path attempt was verifier-only;
the corrected registered path and complete rebuilt run pass.
""")
(INST/"CHECKS.md").write_text("""# WORKING-P4-PKG14 Checks

Status: `PASS`

- Manager preflight: 85/85 checks; 45/45 live bindings.
- Author: 5/5; 158 mappings; 1,454/1,454 lines; 25/25 rows; 5 simulations;
  35 negative probes; 923/923 evidence and 15/15 candidate bindings.
- Verifier: `PASS_UNCHANGED`; 242/242 evidence bindings; 15/15 candidate
  hashes unchanged; 45/45 live and 29/29 method bindings.
- Registered checks: five dependency schemas, practitioner self-check,
  264 practitioner tests, and 19 focused Scope-of-Work tests pass.
- Retained mechanical attempts are evidence-only and fully rebound; no
  semantic, source, lifecycle, authority, acceptance, or project repair.
""")
(INST/"CONTAINMENT.md").write_text("""# WORKING-P4-PKG14 Containment

Status: `PASS`

Writes are contained to `candidates/W_P4/PIP-PKG14/**` and
`instances/WORKING-P4-PKG14/**`. Exactly 15 candidate files exist. Live PKG-14
project worktree/index diff is empty. No Git, lifecycle, dependency-truth,
PKG-00, integration, release, reliance, rollback-execution, retirement, or H2
write occurred. The verifier changed no candidate or author output.
""")
(INST/"PACKAGE_HANDOFF.md").write_text("""# WORKING-P4-PKG14 Terminal Handoff

Verdict: `PASS`

Accepted upstream: W-P4 preflight and HELP_HUMAN acceptance bound to
`main@e8f59a63372f38d9e788ac39b39995558f5aba73` and preflight manifest
`e3c0ba738b4109fe8ab3eccaaab1e76e82e213b5e6b27f9dd6632c7716682faf`.

Derivative package: complete for `DEL-14-01..05`. Author `PASS` and fresh
verifier `PASS_UNCHANGED` cover 5/5 members, 158 mappings, 1,454/1,454 lines,
25 exact replacement rows, 25 exact inverse rows, five simulations, all
negative behavior, registered checks, telemetry, and immutable candidates.

Closure: package candidate/evidence preparation is closed. Blockers, unknowns,
waivers, contamination, and rerun requirements: none. This does not accept
lifecycle or authorize integration, release, reliance, rollback execution,
retirement, or H2. Next owner is direct `RECONCILIATION`; later P4 packages
remain governed by the sealed serial package graph.
""")
(INST/"RETURN.md").write_text("""# WORKING-P4-PKG14 Terminal Return

RUN_STATUS: `PASS`

Exactly `DEL-14-01..05` are complete as one bounded derivative batch. The
accepted author return is `PASS`; the fresh evidence-only verifier return is
`PASS_UNCHANGED`. Aggregate coverage is 5/5 members, 158/158 production-bound
mappings, 1,454/1,454 physical source lines, 25 replacement and 25 inverse
rows, five simulations, and 35/35 negative probes. All focused and practitioner
checks pass; 15/15 candidate hashes are unchanged.

Safe mechanical evidence defects were retained, repaired only in owned
evidence, fully rebound, and rerun. No semantic/source/lifecycle/authority or
acceptance defect occurred. Blockers, unknowns, waivers, contamination,
project writes, and rerun requirements are zero. Derivative preparation is
closed and handed directly to RECONCILIATION; no integration or lifecycle
authority is implied.
""")
(INST/"STATUS.json").write_text(json.dumps({
  "schema":"chirality-agent-return/v1", "run_id":"SOW-STAGE2-EXEC-20260712-01",
  "instance_id":"WORKING-P4-PKG14", "role":"WORKING_ITEMS", "package_id":"PKG-14",
  "status":"PASS", "terminal":True, "members_complete":5, "members_expected":5,
  "source_lines_covered":1454, "source_lines_total":1454, "mappings_passed":158,
  "replacement_rows":25, "inverse_rows":25, "simulations":5,
  "author":"PASS", "verifier":"PASS_UNCHANGED", "blockers":[], "unknowns":[],
  "waivers":[], "reruns":[], "derivative_status":"COMPLETE_CURRENT",
  "next_owner":"RECONCILIATION"},indent=2)+"\n")

# Self-excluding package manifest, generated after all terminal artifacts.
entries=[]
for base in (CAND, INST):
    for p in sorted(base.rglob("*")):
        if not p.is_file() or p == INST/"MANIFEST.tsv": continue
        entries.append((str(p.relative_to(ROOT)),sha(p),p.stat().st_size))
with (INST/"MANIFEST.tsv").open("w",newline="") as f:
    w=csv.writer(f,delimiter="\t",lineterminator="\n"); w.writerow(["path","sha256","bytes"]); w.writerows(entries)
print(json.dumps({"status":"PASS","members":5,"manifest_bindings":len(entries)},indent=2))
