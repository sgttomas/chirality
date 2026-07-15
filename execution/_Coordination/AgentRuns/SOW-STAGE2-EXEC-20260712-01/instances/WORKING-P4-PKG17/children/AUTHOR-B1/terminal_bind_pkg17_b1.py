#!/usr/bin/env python3
"""Terminally bind completed PKG-17 B1 author evidence."""
import csv, hashlib, json, subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(subprocess.check_output(["git","rev-parse","--show-toplevel"],text=True).strip())
RUN=ROOT/"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
CHILD=RUN/"instances/WORKING-P4-PKG17/children/AUTHOR-B1"
CAND=RUN/"candidates/W_P4/PIP-PKG17"
DIDS=[f"DEL-17-{n:02d}" for n in range(1,6)]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,s): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(s.rstrip()+"\n",encoding="utf-8")
def tsv(p,h,rows):
 with p.open("w",newline="",encoding="utf-8") as f:
  w=csv.writer(f,delimiter="\t",lineterminator="\n"); w.writerow(h); w.writerows(rows)

rows=list(csv.DictReader((CHILD/"MEMBER_RESULTS.tsv").open(newline="",encoding="utf-8"),delimiter="\t"))
assert [r["deliverable_id"] for r in rows]==DIDS
assert all(r["verdict"]=="PASS" for r in rows)
assert sum(int(r["mappings"]) for r in rows)==166
assert sum(int(r["covered_lines"]) for r in rows)==sum(int(r["total_lines"]) for r in rows)==1528
assert sum(1 for _ in csv.DictReader((CHILD/"REPLACEMENT_ROWS.tsv").open(newline="",encoding="utf-8"),delimiter="\t"))==25
assert sum(1 for _ in csv.DictReader((CHILD/"INVERSE_ROWS.tsv").open(newline="",encoding="utf-8"),delimiter="\t"))==25
assert sum(1 for _ in csv.DictReader((CHILD/"SIMULATIONS.tsv").open(newline="",encoding="utf-8"),delimiter="\t"))==5
for name in ["scope-of-work-tests","practitioner-harness-tests","practitioner-self-check"]+[f"dependency-schema-{n}" for n in range(1,6)]:
 assert (CHILD/f"{name}.exit").read_text().strip()=="0"
assert subprocess.run(["git","diff","--quiet","--","projects/chirality-piping"],cwd=ROOT).returncode==0
assert subprocess.run(["git","diff","--cached","--quiet","--","projects/chirality-piping"],cwd=ROOT).returncode==0
cent=[]
for did in DIDS:
 files=sorted(p for p in (CAND/did).rglob("*") if p.is_file())
 assert len(files)==3
 for p in files: cent.append([sha(p),p.stat().st_size,str(p.relative_to(ROOT))])
assert len(cent)==15
tsv(CHILD/"CANDIDATE_MANIFEST.tsv",["sha256","bytes","path"],cent)
write(CHILD/"FAILURE_ATTEMPTS.md","""# Retained attempts and safe mechanical repairs

- Pre-execution wrapper validation stopped before registered tools because disabled-render cleanup missed one exact no-space tuple spelling. The local wrapper cleanup was repaired and the complete member run restarted.
- Terminal binding then exposed inherited single-batch PKG-16 assumptions: stale PKG-00 edge count and package-wide validator/dependency selectors. The frozen PKG-17 values and sealed B1 five-member selectors were applied only to the local wrapper; registered project checks were rerun in full.
- No registered conversion, finalization, mapping, parity, checklist, validation, negative-probe, or simulation failed. No candidate semantic remediation, authority repair, acceptance weakening, live-project write, lifecycle mutation, or Git mutation occurred.
- Terminal binding reproduces 5/5 members, 166 mappings, 1,528/1,528 lines, 25 replacement rows, 25 inverse rows, five simulations, five dependency checks, and all registered project checks.
""")
write(CHILD/"CONTEXT_ADHERENCE.md","""# AUTHOR-B1 Context Adherence

Exactly DEL-17-01 through DEL-17-05 were processed in numeric order with the complete method repeated for every member. No task drift, instruction loss, later-member abbreviation, cross-member metadata, or scope expansion occurred.

Native token/context occupancy was unavailable and was not inferred. Observable proxies are 5/5 terminal rows, 166/166 production-bound mapping blocks, 1,528/1,528 classified source lines, identical repeated artifact families, 35 fail-closed negative probes, and five successful apply/target/rollback simulations.
""")
write(CHILD/"WHOLE_DIFF_HYGIENE.txt","PASS — all writable child and candidate outputs are free of controlling diff-check whitespace findings; sealed LAUNCH_BRIEF.md is manager-owned immutable input.")
write(CHILD/"WHOLE_DIFF_HYGIENE.warnings","")
write(CHILD/"CONTAINMENT.md","""# AUTHOR-B1 containment proof

- Writable roots: this child evidence folder and `candidates/W_P4/PIP-PKG17/DEL-17-01` through `DEL-17-05` only.
- Candidate manifest: 15/15 expected files, exactly evidence SOW, clean production SOW, and finalization report for each of five members.
- Live `projects/chirality-piping` working-tree and index diff: empty.
- Every nine-file live binding was hash-verified before and after conversion against accepted W-P4 preflight; all remain equal.
- Live ScopeOfWork presence remained absent for 5/5 members.
- No Git, lifecycle, control, dependency, PKG-00, release, reliance, rollback execution, retirement, or H2 mutation occurred.
""")
now=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
(CHILD/"STATUS.json").write_text(json.dumps({"schema":"chirality-agent-return/v1","run_id":"SOW-STAGE2-EXEC-20260712-01","instance_id":"AUTHOR-B1","package_id":"PKG-17","batch_id":"PKG-17-B1","status":"PASS","members_complete":5,"members_expected":5,"mappings_passed":166,"source_lines_covered":1528,"source_lines_total":1528,"replacement_rows":25,"inverse_rows":25,"simulations_passed":5,"negative_probes_passed":35,"blockers":[],"waivers":[],"unknowns":[],"semantic_expansions":[],"retained_findings":[],"native_token_context_telemetry":"UNAVAILABLE_NOT_INFERRED","finished_utc":now},indent=2)+"\n")
write(CHILD/"RETURN.md","""# AUTHOR-B1 Terminal Return

RUN_STATUS: `PASS`

Exactly DEL-17-01 through DEL-17-05 were processed sequentially. Five evidence-rich candidates, five distinct deterministic clean production finalizations, and five external finalization reports are complete in the sealed candidate scope.

Aggregate: `5/5` members; `166/166` production-bound mapping blocks; `1,528/1,528` physical source lines classified; exact `25` replacement and `25` inverse rows; five apply/target/rollback simulations; zero omission.

All dual and standalone validations, finalization bindings, twice-reproduced production-bound map/parity checks, deterministic checklists, seven fail-closed negative probes per member, before/after nine-file source/control hashes, lifecycle/format checks, semantic source-context reviews, member metadata checks, five dependency-schema checks, scope-of-work tool tests, practitioner-harness tests, and practitioner self-check pass. Schema, project-content, preservation/containment, clean-finalization, and execution-substrate verdicts are PASS.

Mechanical wrapper attempts are retained in `PREEXECUTION_ATTEMPTS.md` and `FAILURE_ATTEMPTS.md`; every terminal project check was rerun after correction. No candidate semantic repair, registered-tool failure, project/source/lifecycle mutation, waiver, blocker, unknown, conflict requiring ruling, contamination, or acceptance weakening occurred.

This derivative author package is ready for strict parent fan-in and independent verifier review. It does not authorize project integration, lifecycle action, H2, release, retirement, rollback execution, or acceptance.
""")
rr=CHILD/"_run_records/TASK_RUN_2026-07-14_AUTHOR-B1.md"
text=rr.read_text(encoding="utf-8").replace("run-status: PENDING","run-status: SUCCESS")
text=text.replace("## Tools Used\n\n(pending)","## Tools Used\n\n- python3 tools/scope_of_work/convert_four_documents_to_scope_of_work.py\n- python3 tools/scope_of_work/finalize_scope_of_work.py\n- python3 tools/scope_of_work/validate_scope_of_work.py\n- python3 tools/scope_of_work/map_scope_of_work_claims.py\n- python3 tools/scope_of_work/report_scope_of_work_parity.py\n- python3 tools/scope_of_work/derive_review_checklist.py")
text=text.replace("## Tool Policy Compliance\n\n(pending)","## Tool Policy Compliance\n\nPASS")
text=text.replace("## Outputs Produced\n\n(pending)","## Outputs Produced\n\n- Five evidence-rich candidates, five clean production candidates, five finalization reports, and complete aggregate evidence.")
text=text.replace("## Missing\n\n(pending)","## Missing\n\nnone").replace("## Needs Human Ruling\n\n(pending)","## Needs Human Ruling\n\nnone").replace("## Dependency Notes\n\n(pending)","## Dependency Notes\n\nnone")
text=text.replace("## Applied Changes\n\n(pending)","## Applied Changes\n\n- Wrote only the sealed PKG-17 B1 candidate roots and AUTHOR-B1 evidence folder; no live project or Git mutation.")
rr.write_text(text,encoding="utf-8")
entries=[]
for p in sorted(x for x in CHILD.rglob("*") if x.is_file()):
 if p==CHILD/"MANIFEST.tsv": continue
 entries.append([sha(p),p.stat().st_size,str(p.relative_to(ROOT))])
tsv(CHILD/"MANIFEST.tsv",["sha256","bytes","path"],entries)
for digest,size,rel in entries: assert sha(ROOT/rel)==digest and (ROOT/rel).stat().st_size==int(size)
print(json.dumps({"status":"PASS","members":5,"mappings":166,"lines":1528,"manifest_entries":len(entries)}))
