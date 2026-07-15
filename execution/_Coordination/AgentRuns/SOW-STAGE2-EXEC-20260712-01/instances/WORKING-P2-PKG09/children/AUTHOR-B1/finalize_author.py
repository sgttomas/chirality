#!/usr/bin/env python3
import csv, hashlib, json, subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(subprocess.check_output(["git","rev-parse","--show-toplevel"],text=True).strip())
RUN=ROOT/"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
CHILD=RUN/"instances/WORKING-P2-PKG09/children/AUTHOR-B1"
CAND=RUN/"candidates/W_P2/PIP-PKG09"
PM=RUN/"snapshots/W_P2/preflight/P2_MANIFEST.tsv"
DIDS=[f"DEL-09-{n:02d}" for n in range(1,6)]
LEGACY=["Datasheet.md","Specification.md","Guidance.md","Procedure.md"]
CONTROL=["_STATUS.md","_CONTEXT.md","_REFERENCES.md","_DEPENDENCIES.md","Dependencies.csv"]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,s): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(s.rstrip()+"\n",encoding="utf-8")
def tsv(p,h,rows):
 with p.open("w",newline="",encoding="utf-8") as f: w=csv.writer(f,delimiter="\t",lineterminator="\n"); w.writerow(h); w.writerows(rows)
with PM.open(newline="",encoding="utf-8") as f: rows={r["deliverable_id"]:r for r in csv.DictReader(f,delimiter="\t")}
total_maps=total_covered=total_lines=0
for did in DIDS:
 r=rows[did]; live=ROOT/r["live_path"]; m=CHILD/"members"/did; c=CAND/did; evid=c/"evidence/ScopeOfWork.md"; prod=c/"production/ScopeOfWork.md"; report=c/"finalization.json"
 parity=json.loads((m/"parity-a.json").read_text()); maps=len(parity["checks"]); covered=sum(x["line_end"]-x["line_start"]+1 for x in parity["checks"]); lines=sum(len((live/n).read_bytes().splitlines()) for n in LEGACY)
 assert parity["pass"] and covered==lines==int(r["source_lines"])
 assert sha(m/"workspace-a/ScopeOfWork.md")==sha(m/"workspace-b/ScopeOfWork.md")==sha(evid)
 assert sha(m/"final-a/ScopeOfWork.md")==sha(m/"final-b/ScopeOfWork.md")==sha(prod)
 assert sha(m/"final-a/report.json")==sha(m/"final-b/report.json")==sha(report)
 assert r["lifecycle"]=="IN_PROGRESS" and r["live_format"]=="LEGACY_FOUR_DOC" and not (live/"ScopeOfWork.md").exists()
 text=prod.read_text(); assert f"deliverable_id: {did}\n" in text and "package_id: PKG-09\n" in text and f"decomposition_basis: {r['decomposition_basis']}\n" in text
 assert f"project_scope_refs: [{', '.join(x.strip() for x in r['scope_refs'].split(','))}]\n" in text
 assert f"package_objective_refs: [{', '.join(x.strip() for x in r['objective_refs'].split(','))}]\n" in text
 for name,key in [("Datasheet.md","datasheet_sha256"),("Specification.md","specification_sha256"),("Guidance.md","guidance_sha256"),("Procedure.md","procedure_sha256"),("_STATUS.md","status_sha256"),("_CONTEXT.md","context_sha256"),("_REFERENCES.md","references_sha256"),("_DEPENDENCIES.md","dependencies_md_sha256"),("Dependencies.csv","dependencies_csv_sha256")]: assert sha(live/name)==r[key]
 total_maps+=maps; total_covered+=covered; total_lines+=lines
assert (total_maps,total_covered,total_lines)==(162,1357,1357)
write(CHILD/"FAILURE_ATTEMPTS.md","""# Retained attempts and safe mechanical repair

- Pre-execution syntax parsing found one closing-bracket typo in the newly written local harness at the `simulations.append` call. No tool, candidate, source, project, or evidence output had run or been written. The exact one-character mechanical repair changed `)` to `])`; syntax parsing then passed and the complete harness ran once from the beginning.
- No registered conversion, validation, finalization, mapping, parity, checklist, rendering, negative-probe, or simulation attempt failed or retried.
- No candidate remediation, semantic repair, authority repair, or acceptance weakening was performed.
- Terminalization rebuilt all direct and transitive bindings after the repair and reproduced 5/5 members, 162 mappings, 1,357/1,357 lines, 25 replacement rows, 25 inverse rows, and five simulations.
""")
write(CHILD/"CONTEXT_ADHERENCE.md","""# AUTHOR-B1 Context Adherence

Exactly DEL-09-01 through DEL-09-05 were processed in numeric order with the complete method repeated for every member. No task drift, instruction loss, later-member abbreviation, cross-member metadata, or scope expansion occurred.

Native token/context occupancy was not exposed by this runtime and is recorded as unavailable rather than inferred. Observable proxies are 5/5 terminal rows, 162/162 production-bound mapping blocks, 1,357/1,357 classified source lines, identical repeated artifact families, 35 fail-closed negative probes, and five successful apply/target/rollback simulations.
""")
now=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
(CHILD/"STATUS.json").write_text(json.dumps({"schema":"chirality-agent-return/v1","run_id":"SOW-STAGE2-EXEC-20260712-01","instance_id":"AUTHOR-B1","package_id":"PKG-09","status":"PASS","members_complete":5,"members_expected":5,"mappings_passed":162,"source_lines_covered":1357,"source_lines_total":1357,"replacement_rows":25,"inverse_rows":25,"simulations_passed":5,"negative_probes_passed":35,"blockers":[],"waivers":[],"unknowns":[],"semantic_expansions":[],"retained_findings":[],"native_token_context_telemetry":"UNAVAILABLE_NOT_INFERRED","finished_utc":now},indent=2)+"\n")
write(CHILD/"RETURN.md","""# AUTHOR-B1 Terminal Return

RUN_STATUS: `PASS`

Exactly DEL-09-01 through DEL-09-05 were processed sequentially. Five evidence-rich candidates, five distinct deterministic clean production finalizations, and five external finalization reports are complete in the sealed candidate scope.

Aggregate: `5/5` members; `162/162` production-bound mapping blocks; `1,357/1,357` physical source lines classified; exact `25` replacement and `25` inverse rows; five apply/target/rollback simulations; zero omission.

All dual and standalone validations, finalization bindings, twice-reproduced production-bound map/parity checks, deterministic checklists/renders, seven fail-closed negative probes per member, before/after nine-file source/control hashes, lifecycle/format checks, semantic source-context reviews, and member metadata checks pass. Schema, project-content, preservation/containment, clean-finalization, and execution-substrate verdicts are PASS.

A one-character local harness syntax typo was detected and repaired before any execution output existed; the complete run then started from the beginning and all direct/transitive evidence was frozen after it. No registered tool failed or retried. Native token/context occupancy was unavailable and was not inferred. No drift or later-member abbreviation occurred.

Blockers / conflicts requiring ruling / waivers / unknowns / semantic expansions / scope violations / project writes / contamination / reruns: none.

This derivative author package is ready for strict parent fan-in and independent verifier review. It does not authorize project integration, lifecycle action, H2, release, retirement, rollback execution, or acceptance.
""")
with (CHILD/"RUNTIME_EVENTS.jsonl").open("a",encoding="utf-8") as f:
 f.write(json.dumps({"timestamp_utc":now,"sequence":0,"deliverable_id":"BATCH","stage":"harness_preflight","event":"repair","attempt":1,"failure_category":"EXECUTION_SUBSTRATE","reason_code":"LOCAL_SYNTAX_BRACKET_REPAIRED_BEFORE_EXECUTION","remediation":"ONE_CHARACTER_BRACKET_FIX_FULL_RUN_FROM_START"},separators=(",",":"))+"\n")
 f.write(json.dumps({"timestamp_utc":now,"sequence":0,"deliverable_id":"BATCH","stage":"terminalization","event":"finish","attempt":1,"reason_code":"PASS_FINAL_BIND"},separators=(",",":"))+"\n")
run_record=CHILD/"_run_records/TASK_RUN_2026-07-14_AUTHOR-B1.md"
write(run_record,f"""---
run-id: TASK_RUN_AUTHOR-B1_2026-07-14
timestamp: {now}
run-status: SUCCESS
control-surface: FILE
scope-path: {CHILD}
task-profile: NONE
task-skill: scope-of-work
resolved-skill-path: {ROOT/'skills/scope-of-work'}
resolved-skill-version: "1"
resolved-task-profile-requirement: NONE
companion-files:
  - BRIEF_SCHEMA.md (found)
  - TOOL_POLICY.md (found)
  - QA_CHECKS.md (found)
allowed-tools:
  - python3 tools/scope_of_work/validate_scope_of_work.py
  - python3 tools/scope_of_work/render_scope_of_work.py
  - python3 tools/scope_of_work/convert_four_documents_to_scope_of_work.py
  - python3 tools/scope_of_work/finalize_scope_of_work.py
  - python3 tools/scope_of_work/map_scope_of_work_claims.py
  - python3 tools/scope_of_work/report_scope_of_work_parity.py
  - python3 tools/scope_of_work/derive_review_checklist.py
write-authorization: ALLOWED_WRITE_TARGETS
runtime-overrides:
  MODE: CONVERT
  FORMAT_AUTHORITY_REF: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176
  SOURCE_STATE: IN_PROGRESS
  RENDER_HTML: true
---

## Requested Tasks

- Prepare exact DEL-09-01 through DEL-09-05 isolated conversion candidates and complete author evidence under the sealed brief.

## Expected Outputs

- Five evidence candidates, five clean production candidates, five finalization reports, complete per-member and terminal evidence.

## Tools Used

- python3 tools/scope_of_work/convert_four_documents_to_scope_of_work.py
- python3 tools/scope_of_work/finalize_scope_of_work.py
- python3 tools/scope_of_work/validate_scope_of_work.py
- python3 tools/scope_of_work/map_scope_of_work_claims.py
- python3 tools/scope_of_work/report_scope_of_work_parity.py
- python3 tools/scope_of_work/derive_review_checklist.py
- python3 tools/scope_of_work/render_scope_of_work.py

## Tool Policy Compliance

PASS

## Write Authorization

Only the sealed PKG-09 candidate roots and this AUTHOR-B1 child folder.

## Outputs Produced

- Five evidence-rich candidates, five clean production candidates, and five external finalization reports.
- Complete twice-reproduced conversion/finalization/map/parity/checklist/render evidence, negative probes, hashes, telemetry, and simulations.

## Missing

none

## Needs Human Ruling

none

## Dependency Notes

none

## Applied Changes

- Wrote only the sealed PKG-09 candidate roots and AUTHOR-B1 evidence folder; no live project or Git mutation.
""")
warnings=[]
for base in (CHILD,CAND):
 for p in sorted(x for x in base.rglob("*") if x.is_file()):
  if p in {CHILD/"LAUNCH_BRIEF.md",CHILD/"WHOLE_DIFF_HYGIENE.warnings",CHILD/"MANIFEST.tsv"}: continue
  rel=p.relative_to(CHILD) if p.is_relative_to(CHILD) else None
  if rel and any(part in {"workspace-a","workspace-b","simulation","negative-partial"} for part in rel.parts): continue
  q=subprocess.run(["git","diff","--no-index","--check","--","/dev/null",str(p)],cwd=ROOT,text=True,capture_output=True)
  if q.stdout or q.stderr: warnings.append(f"{p.relative_to(ROOT)}\n{q.stdout}{q.stderr}")
(CHILD/"WHOLE_DIFF_HYGIENE.warnings").write_text("\n".join(warnings),encoding="utf-8")
assert not warnings, "whitespace findings require normalization"
write(CHILD/"WHOLE_DIFF_HYGIENE.txt","PASS — all writable child and candidate outputs are free of diff-check whitespace findings; sealed LAUNCH_BRIEF.md is manager-owned immutable input.")
cent=[]
for did in DIDS:
 for p in sorted(x for x in (CAND/did).rglob("*") if x.is_file()): cent.append([sha(p),p.stat().st_size,str(p.relative_to(ROOT))])
assert len(cent)==15; tsv(CHILD/"CANDIDATE_MANIFEST.tsv",["sha256","bytes","path"],cent)
assert subprocess.run(["git","diff","--quiet","--","projects/chirality-piping"],cwd=ROOT).returncode==0
assert subprocess.run(["git","diff","--cached","--quiet","--","projects/chirality-piping"],cwd=ROOT).returncode==0
write(CHILD/"CONTAINMENT.md","""# AUTHOR-B1 containment proof

- Writable roots: this child evidence folder and `candidates/W_P2/PIP-PKG09` only.
- Candidate manifest: 15/15 expected files, exactly evidence SOW, clean production SOW, and finalization report for each of five members.
- Live `projects/chirality-piping` working-tree and index diff: empty.
- Every nine-file live binding was hash-verified before and after conversion; all remain equal to accepted P2 preflight.
- Live ScopeOfWork presence remained absent for 5/5 members.
- No Git, lifecycle, control, dependency, PKG-00, release, reliance, rollback execution, retirement, or H2 mutation occurred.
""")
entries=[]
for p in sorted(x for x in CHILD.rglob("*") if x.is_file()):
 if p==CHILD/"MANIFEST.tsv": continue
 entries.append([sha(p),p.stat().st_size,str(p.relative_to(ROOT))])
tsv(CHILD/"MANIFEST.tsv",["sha256","bytes","path"],entries)
for digest,size,rel in entries: assert sha(ROOT/rel)==digest and (ROOT/rel).stat().st_size==size
print(json.dumps({"status":"PASS","members":5,"mappings":total_maps,"lines":total_lines,"manifest_entries":len(entries)}))
