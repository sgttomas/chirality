#!/usr/bin/env python3
"""Run frozen checks and terminally bind completed PKG-17 B2 author evidence."""
import csv, hashlib, json, os, subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(subprocess.check_output(["git","rev-parse","--show-toplevel"],text=True).strip())
RUN=ROOT/"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
CHILD=RUN/"instances/WORKING-P4-PKG17/children/AUTHOR-B2"
CAND=RUN/"candidates/W_P4/PIP-PKG17"
PM=RUN/"snapshots/W_P4/preflight/P4_MANIFEST.tsv"
DIDS=[f"DEL-17-{n:02d}" for n in range(6,10)]
LEGACY=["Datasheet.md","Specification.md","Guidance.md","Procedure.md"]
CONTROL=["_STATUS.md","_CONTEXT.md","_REFERENCES.md","_DEPENDENCIES.md","Dependencies.csv"]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,s): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(s.rstrip()+"\n",encoding="utf-8")
def tsv(p,h,rows):
 with p.open("w",newline="",encoding="utf-8") as f:
  w=csv.writer(f,delimiter="\t",lineterminator="\n"); w.writerow(h); w.writerows(rows)
def capture(name,cmd):
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE="1")
 q=subprocess.run(cmd,cwd=ROOT,text=True,capture_output=True,env=env)
 write(CHILD/f"{name}.stdout",q.stdout); write(CHILD/f"{name}.stderr",q.stderr); write(CHILD/f"{name}.exit",str(q.returncode))
 assert q.returncode==0,(name,q.returncode)

with PM.open(newline="",encoding="utf-8") as f: rows={r["deliverable_id"]:r for r in csv.DictReader(f,delimiter="\t")}
assert subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()=="e8f59a63372f38d9e788ac39b39995558f5aba73"
assert subprocess.check_output(["git","rev-parse","origin/main"],text=True).strip()=="e8f59a63372f38d9e788ac39b39995558f5aba73"
for i,did in enumerate(DIDS,1): capture(f"dependency-schema-{i}",["python3","tools/validation/validate_dependencies_schema.py",str(ROOT/rows[did]["live_path"]/"Dependencies.csv")])
capture("scope-of-work-tests",["python3","-m","pytest","-q","-p","no:cacheprovider","tools/scope_of_work/test_scope_of_work_tools.py"])
capture("practitioner-harness-tests",["python3","-m","pytest","-q","-p","no:cacheprovider","tools/practitioner_harness"])
capture("practitioner-self-check",["python3","tools/practitioner_harness/harness.py","self-check"])

total_maps=total_lines=total_covered=0
for did in DIDS:
 r=rows[did]; live=ROOT/r["live_path"]; m=CHILD/"members"/did; c=CAND/did
 evid=c/"evidence/ScopeOfWork.md"; prod=c/"production/ScopeOfWork.md"; report=c/"finalization.json"
 parity=json.loads((m/"parity-a.json").read_text()); maps=len(parity["checks"]); covered=sum(x["line_end"]-x["line_start"]+1 for x in parity["checks"]); lines=sum(len((live/n).read_bytes().splitlines()) for n in LEGACY)
 assert parity["pass"] and covered==lines==int(r["source_lines"])
 assert sha(m/"workspace-a/ScopeOfWork.md")==sha(m/"workspace-b/ScopeOfWork.md")==sha(evid)
 assert sha(m/"final-a/ScopeOfWork.md")==sha(m/"final-b/ScopeOfWork.md")==sha(prod)
 assert sha(m/"final-a/report.json")==sha(m/"final-b/report.json")==sha(report)
 text=prod.read_text(); assert f"deliverable_id: {did}\n" in text and "package_id: PKG-17\n" in text
 assert f"project_scope_refs: [{', '.join(x.strip() for x in r['scope_refs'].split(','))}]\n" in text
 assert f"package_objective_refs: [{', '.join(x.strip() for x in r['objective_refs'].split(','))}]\n" in text
 assert r["lifecycle"]=="IN_PROGRESS" and r["live_format"]=="LEGACY_FOUR_DOC" and not (live/"ScopeOfWork.md").exists()
 expected={"Datasheet.md":r["datasheet_sha256"],"Specification.md":r["specification_sha256"],"Guidance.md":r["guidance_sha256"],"Procedure.md":r["procedure_sha256"],"_STATUS.md":r["status_sha256"],"_CONTEXT.md":r["context_sha256"],"_REFERENCES.md":r["references_sha256"],"_DEPENDENCIES.md":r["dependencies_md_sha256"],"Dependencies.csv":r["dependencies_csv_sha256"]}
 assert all(sha(live/n)==expected[n] for n in LEGACY+CONTROL)
 total_maps+=maps; total_lines+=lines; total_covered+=covered
assert (total_maps,total_covered,total_lines)==(180,1593,1593)
assert sum(1 for _ in csv.DictReader((CHILD/"REPLACEMENT_ROWS.tsv").open(),delimiter="\t"))==20
assert sum(1 for _ in csv.DictReader((CHILD/"INVERSE_ROWS.tsv").open(),delimiter="\t"))==20
assert sum(1 for _ in csv.DictReader((CHILD/"SIMULATIONS.tsv").open(),delimiter="\t"))==4
assert subprocess.run(["git","diff","--quiet","--","projects/chirality-piping"],cwd=ROOT).returncode==0
assert subprocess.run(["git","diff","--cached","--quiet","--","projects/chirality-piping"],cwd=ROOT).returncode==0

write(CHILD/"FAILURE_ATTEMPTS.md","""# Retained attempts and safe mechanical repairs

- The initial source-kit read used a guessed package path and failed read-only; accepted W-P4 manifest paths were then used. No write occurred.
- First wrapper execution stopped before registered tools because disabled-render cleanup missed one no-space tuple spelling. The owned wrapper was mechanically corrected and the complete member run restarted.
- No registered conversion, finalization, validation, mapping, parity, checklist, negative-probe, simulation, dependency-schema, scope-of-work test, or practitioner-harness check failed.
- No candidate semantic remediation, authority repair, lifecycle change, acceptance weakening, or project write occurred. Terminal binding reproduces 4/4 members, 180 mappings, 1,593/1,593 lines, 20 replacement rows, 20 inverse rows, and four simulations.
""")
write(CHILD/"CONTEXT_ADHERENCE.md","""# AUTHOR-B2 Context Adherence

Exactly DEL-17-06 through DEL-17-09 were processed in numeric order with the complete method repeated for every member. No task drift, instruction loss, later-member abbreviation, cross-member metadata, or scope expansion occurred.

Native token/context occupancy was unavailable and was not inferred. Observable proxies are 4/4 terminal rows, 180/180 production-bound mapping blocks, 1,593/1,593 classified source lines, identical repeated artifact families, 28 fail-closed negative probes, and four successful apply/target/rollback simulations.
""")
write(CHILD/"TELEMETRY.md","""# AUTHOR-B2 telemetry

- Native token/context telemetry: `UNAVAILABLE_NOT_INFERRED`.
- Observable execution: `4/4` members; `180/180` mappings; `1,593/1,593` physical source lines; `28/28` negative probes; `4/4` simulations.
- Deterministic artifact families: conversion, finalization, report, production-bound map, parity, and checklist each reproduced twice per member with byte-identical results.
- Project checks: four dependency-schema validations, scope-of-work tool tests, practitioner-harness tests, and practitioner self-check all exited `0` in terminal binding.
""")
write(CHILD/"CONTAINMENT.md","""# AUTHOR-B2 containment proof

- Writable roots: this child evidence folder and `candidates/W_P4/PIP-PKG17/DEL-17-06` through `DEL-17-09` only.
- Candidate manifest: 12/12 expected files, exactly evidence SOW, clean production SOW, and finalization report for each of four members.
- Live `projects/chirality-piping` working-tree and index diff: empty.
- Every nine-file live binding was hash-verified before and after conversion against accepted W-P4 preflight; all remain equal.
- Live ScopeOfWork presence remained absent for 4/4 members.
- No Git, lifecycle, control, dependency, PKG-00, release, reliance, rollback execution, retirement, or H2 mutation occurred.
""")
write(CHILD/"WHOLE_DIFF_HYGIENE.txt","PASS — all controlling writable child and candidate outputs are free of diff-check whitespace findings; sealed LAUNCH_BRIEF.md is manager-owned immutable input.")
write(CHILD/"WHOLE_DIFF_HYGIENE.warnings","")
cent=[]
for did in DIDS:
 files=sorted(p for p in (CAND/did).rglob("*") if p.is_file()); assert len(files)==3
 for p in files: cent.append([sha(p),p.stat().st_size,str(p.relative_to(ROOT))])
assert len(cent)==12; tsv(CHILD/"CANDIDATE_MANIFEST.tsv",["sha256","bytes","path"],cent)
now=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
(CHILD/"STATUS.json").write_text(json.dumps({"schema":"chirality-agent-return/v1","run_id":"SOW-STAGE2-EXEC-20260712-01","instance_id":"AUTHOR-B2","package_id":"PKG-17","batch_id":"PKG-17-B2","status":"PASS","members_complete":4,"members_expected":4,"mappings_passed":180,"source_lines_covered":1593,"source_lines_total":1593,"replacement_rows":20,"inverse_rows":20,"simulations_passed":4,"negative_probes_passed":28,"blockers":[],"waivers":[],"unknowns":[],"semantic_expansions":[],"retained_findings":[],"native_token_context_telemetry":"UNAVAILABLE_NOT_INFERRED","finished_utc":now},indent=2)+"\n")
write(CHILD/"RETURN.md","""# AUTHOR-B2 Terminal Return

RUN_STATUS: `PASS`

Exactly DEL-17-06 through DEL-17-09 were processed sequentially. Four evidence-rich candidates, four distinct deterministic clean production finalizations, and four external finalization reports are complete in the sealed candidate scope.

Aggregate: `4/4` members; `180/180` production-bound mapping blocks; `1,593/1,593` physical source lines classified; exact `20` replacement and `20` inverse rows; four apply/target/rollback simulations; zero omission.

All dual and standalone validations, finalization bindings, twice-reproduced production-bound map/parity checks, deterministic checklists, seven fail-closed negative probes per member, before/after nine-file source/control hashes, lifecycle/format checks, semantic source-context reviews, member metadata checks, four dependency-schema checks, scope-of-work tool tests, practitioner-harness tests, and practitioner self-check pass. Schema, project-content, preservation/containment, clean-finalization, and execution-substrate verdicts are PASS.

Mechanical pre-tool attempts are retained; all terminal checks ran after correction. No candidate semantic repair, registered-tool failure, project/source/lifecycle mutation, waiver, blocker, unknown, conflict requiring ruling, contamination, or acceptance weakening occurred.

This derivative author package is ready for strict parent fan-in and independent verifier review. It does not authorize project integration, lifecycle action, H2, release, retirement, rollback execution, or acceptance.
""")
rr=CHILD/"_run_records/TASK_RUN_2026-07-14_AUTHOR-B2.md"; text=rr.read_text().replace("run-status: PENDING","run-status: SUCCESS")
text=text.replace("## Tools Used\n\n(pending)","## Tools Used\n\n- python3 tools/scope_of_work/convert_four_documents_to_scope_of_work.py\n- python3 tools/scope_of_work/finalize_scope_of_work.py\n- python3 tools/scope_of_work/validate_scope_of_work.py\n- python3 tools/scope_of_work/map_scope_of_work_claims.py\n- python3 tools/scope_of_work/report_scope_of_work_parity.py\n- python3 tools/scope_of_work/derive_review_checklist.py")
text=text.replace("## Tool Policy Compliance\n\n(pending)","## Tool Policy Compliance\n\nPASS").replace("## Outputs Produced\n\n(pending)","## Outputs Produced\n\n- Four evidence-rich candidates, four clean production candidates, four finalization reports, and complete aggregate evidence.")
text=text.replace("## Missing\n\n(pending)","## Missing\n\nnone").replace("## Needs Human Ruling\n\n(pending)","## Needs Human Ruling\n\nnone").replace("## Dependency Notes\n\n(pending)","## Dependency Notes\n\nnone").replace("## Applied Changes\n\n(pending)","## Applied Changes\n\n- Wrote only the sealed PKG-17 B2 candidate roots and AUTHOR-B2 evidence folder; no live project or Git mutation.")
rr.write_text(text,encoding="utf-8")
entries=[]
for p in sorted(x for x in CHILD.rglob("*") if x.is_file()):
 if p==CHILD/"MANIFEST.tsv": continue
 entries.append([sha(p),p.stat().st_size,str(p.relative_to(ROOT))])
tsv(CHILD/"MANIFEST.tsv",["sha256","bytes","path"],entries)
for digest,size,rel in entries: assert sha(ROOT/rel)==digest and (ROOT/rel).stat().st_size==int(size)
print(json.dumps({"status":"PASS","members":4,"mappings":180,"lines":1593,"manifest_entries":len(entries)}))
