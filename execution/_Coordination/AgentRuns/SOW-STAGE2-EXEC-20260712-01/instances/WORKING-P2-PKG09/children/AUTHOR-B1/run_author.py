#!/usr/bin/env python3
import csv, hashlib, json, shutil, subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(subprocess.check_output(["git","rev-parse","--show-toplevel"],text=True).strip())
RUN=ROOT/"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
CHILD=RUN/"instances/WORKING-P2-PKG09/children/AUTHOR-B1"
CAND=RUN/"candidates/W_P2/PIP-PKG09"
PM=RUN/"snapshots/W_P2/preflight/P2_MANIFEST.tsv"
AUTH="D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
BASIS="eaad463c0d481f6f1654e6adb5ee718f566176e9"
DIDS=[f"DEL-09-{n:02d}" for n in range(1,6)]
LEGACY=["Datasheet.md","Specification.md","Guidance.md","Procedure.md"]
CONTROL=["_STATUS.md","_CONTEXT.md","_REFERENCES.md","_DEPENDENCIES.md","Dependencies.csv"]
SEEDS={
"DEL-09-01":("A mechanics benchmark-suite contract covering cantilevers, frames, thermal growth, imposed displacement, and stiffness transforms with original/public/permissive provenance is produced.","The contract preserves unit-aware inputs and outputs, solver diagnostics, result-envelope fields, assumptions, provenance, limitations, fixture-local unit evidence, and explicit TBD tolerances and project-unit-system decisions without claiming certification, code compliance, professional approval, or project reliance.","Validate the contract and review source parity, required benchmark-family coverage, source and redistribution posture, unit and diagnostic visibility, setup versus implementation boundaries, retained tolerance and project-unit TBDs, and professional-authority limits."),
"DEL-09-02":("A stress-recovery benchmark-suite contract covering axial, bending, torsion, pressure, and stress-range mechanics behavior with governed evidence boundaries is produced.","The contract preserves public/original/permissive provenance, unit and sign conventions, diagnostics and governed result-envelope evidence, DEC-026's measured analytic relative seed, explicit unmeasured per-kind relative-plus-absolute TBDs, and separation from code compliance, fatigue acceptance, certification, or professional approval.","Validate the contract and review source parity, all five behavior slots, provenance and protected-content limits, units and dimensional checks, diagnostic/result-envelope preservation, DEC-026 tolerance limits without generalization, and professional-authority boundaries."),
"DEL-09-03":("A nonlinear-support regression-suite contract covering active-set, gap, friction, lift-off, convergence, non-convergence, and deterministic rerun evidence is produced.","The contract preserves source-qualified public/original/permissive cases, unit-aware observations, active and friction state, gap and lift-off, iteration and tolerance basis, diagnostics, solver-maturity dependencies, explicit TBD thresholds, and the software-verification-only authority boundary.","Validate the contract and review source parity, nonlinear behavior-category coverage, provenance and protected-content exclusions, unit and deterministic rerun requirements, diagnostic/result-envelope categories, retained solver-maturity and tolerance TBDs, and prohibited authority claims."),
"DEL-09-04":("A validation-manual skeleton contract separating mechanics verification, intended-use workflow validation, user rule checks, and professional reliance across the required manual outline is produced.","The contract preserves the ten manual sections, unit/schema/diagnostic/result-envelope evidence slots, public/private and protected-content boundaries, visible gaps and limitations, software-release versus project-reliance distinction, and human-owned professional judgment without certification or code-compliance claims.","Validate the contract and review source parity, ten-section outline coverage, separation of verification/validation/rule checks/professional reliance, data and provenance boundaries, unit and diagnostic evidence slots, visible TBDs, and release/professional-authority limits."),
"DEL-09-05":("A release quality-gate checklist contract routing solver, rule-engine, GUI, report-template, and mixed changes to bounded software-quality evidence and human governance decisions is produced.","The contract preserves deterministic gate evidence, union routing, provenance, protected/private-data controls, missing-data findings, open risks and TBD thresholds, gate outcome vocabulary, human waiver/risk disposition, and the distinction between release governance and professional engineering approval.","Validate the contract and review source parity, every gate family and mixed routing, required mechanics/rule/GUI/report evidence, provenance and protected-content checks, unresolved thresholds and authority decisions, outcome semantics, and prohibited compliance or professional-approval claims.")}

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def now(): return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def write(p,s): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(s.rstrip()+"\n",encoding="utf-8")
def tsv(p,h,rows):
 p.parent.mkdir(parents=True,exist_ok=True)
 with p.open("w",newline="",encoding="utf-8") as f: w=csv.writer(f,delimiter="\t",lineterminator="\n"); w.writerow(h); w.writerows(rows)
def run(cmd,out,err,fail=False):
 with out.open("w") as o, err.open("w") as e: rc=subprocess.run(cmd,cwd=ROOT,stdout=o,stderr=e).returncode
 if (not fail and rc) or (fail and not rc): raise RuntimeError(f"unexpected rc={rc}: {' '.join(cmd)}")
 return rc
def tool(n): return str(ROOT/"tools/scope_of_work"/n)

assert subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip()==BASIS
assert subprocess.check_output(["git","rev-parse","origin/main"],text=True).strip()==BASIS
with PM.open(newline="",encoding="utf-8") as f: rows={r["deliverable_id"]:r for r in csv.DictReader(f,delimiter="\t")}
progress=[]; events=[]; results=[]; replacements=[]; inverse=[]; simulations=[]; total_maps=total_lines=total_covered=0
for seq,did in enumerate(DIDS,1):
 r=rows[did]; live=ROOT/r["live_path"]; m=CHILD/"members"/did; c=CAND/did
 m.mkdir(parents=True,exist_ok=True); (c/"evidence").mkdir(parents=True,exist_ok=True); (c/"production").mkdir(parents=True,exist_ok=True)
 for stale in [m/"workspace-a",m/"workspace-b",m/"final-a",m/"final-b",m/"negative-partial",m/"mutated-production",m/"simulation"]:
  if stale.exists(): shutil.rmtree(stale)
 start=now(); events.append({"timestamp_utc":start,"sequence":seq,"deliverable_id":did,"stage":"precheck","event":"start","attempt":1,"reason_code":"NONE"})
 assert r["lifecycle"]=="IN_PROGRESS" and r["live_format"]=="LEGACY_FOUR_DOC" and not (live/"ScopeOfWork.md").exists()
 expected={"Datasheet.md":r["datasheet_sha256"],"Specification.md":r["specification_sha256"],"Guidance.md":r["guidance_sha256"],"Procedure.md":r["procedure_sha256"],"_STATUS.md":r["status_sha256"],"_CONTEXT.md":r["context_sha256"],"_REFERENCES.md":r["references_sha256"],"_DEPENDENCIES.md":r["dependencies_md_sha256"],"Dependencies.csv":r["dependencies_csv_sha256"]}
 hashes=[]
 for name in LEGACY+CONTROL: assert sha(live/name)==expected[name]; hashes.append([name,sha(live/name),"before","PASS"])
 lines=sum(len((live/n).read_bytes().splitlines()) for n in LEGACY); assert lines==int(r["source_lines"])
 tsv(m/"FROZEN_ROW.tsv",list(r.keys()),[list(r.values())]); end=now(); progress.append([seq,did,"precheck",start,end,"PASS",0,"NONE","NONE","NONE",f"members/{did}/FROZEN_ROW.tsv;members/{did}/SOURCE_HASHES.tsv","YES"]); events.append({"timestamp_utc":end,"sequence":seq,"deliverable_id":did,"stage":"precheck","event":"finish","attempt":1,"reason_code":"NONE"})
 conv=now(); out_desc,ac,ver=SEEDS[did]
 for suffix in "ab":
  ws=m/f"workspace-{suffix}"; shutil.copytree(live,ws)
  cmd=["python3",tool("convert_four_documents_to_scope_of_work.py"),"--deliverable",str(ws),"--deliverable-id",did,"--package-id","PKG-09","--decomposition-basis",r["decomposition_basis"],"--isolated-migration","--migration-authority",AUTH,"--output-description",out_desc,"--acceptance-criterion",ac,"--verification-method",ver]
  for x in r["scope_refs"].split(","): cmd += ["--project-scope-ref",x.strip()]
  for x in r["objective_refs"].split(","): cmd += ["--package-objective-ref",x.strip()]
  run(cmd,m/f"conversion-{suffix}.stdout",m/f"conversion-{suffix}.stderr")
  run(["python3",tool("validate_scope_of_work.py"),str(ws),"--isolated-migration","--migration-authority",AUTH,"--json"],m/f"validation-dual-{suffix}.json",m/f"validation-dual-{suffix}.stderr")
 assert (m/"workspace-a/ScopeOfWork.md").read_bytes()==(m/"workspace-b/ScopeOfWork.md").read_bytes(); shutil.copy2(m/"workspace-a/ScopeOfWork.md",c/"evidence/ScopeOfWork.md")
 progress.append([seq,did,"conversion",conv,now(),"PASS",0,"NONE","NONE","NONE",f"members/{did}/DETERMINISM.tsv","NO"])
 fin=now()
 for suffix in "ab":
  fd=m/f"final-{suffix}"; fd.mkdir(); run(["python3",tool("finalize_scope_of_work.py"),"--evidence-candidate",str(m/"workspace-a/ScopeOfWork.md"),"--output",str(fd/"ScopeOfWork.md"),"--report",str(fd/"report.json")],m/f"finalization-{suffix}.stdout",m/f"finalization-{suffix}.stderr")
 assert (m/"final-a/ScopeOfWork.md").read_bytes()==(m/"final-b/ScopeOfWork.md").read_bytes() and (m/"final-a/report.json").read_bytes()==(m/"final-b/report.json").read_bytes()
 shutil.copy2(m/"final-a/ScopeOfWork.md",c/"production/ScopeOfWork.md"); shutil.copy2(m/"final-a/report.json",c/"finalization.json"); progress.append([seq,did,"finalization",fin,now(),"PASS",0,"NONE","NONE","NONE",f"members/{did}/final-a/report.json","NO"])
 qa=now(); evid=c/"evidence/ScopeOfWork.md"; prod=c/"production/ScopeOfWork.md"
 run(["python3",tool("validate_scope_of_work.py"),str(prod),"--json"],m/"validation-sow-v1.json",m/"validation-sow-v1.stderr")
 for suffix in "ab":
  run(["python3",tool("map_scope_of_work_claims.py"),"--scope-of-work",str(evid),"--production-scope-of-work",str(prod),"--source-dir",str(live),"--output-csv",str(m/f"claim-map-{suffix}.csv")],m/f"claim-map-{suffix}.stdout",m/f"claim-map-{suffix}.stderr")
  run(["python3",tool("report_scope_of_work_parity.py"),"--scope-of-work",str(evid),"--production-scope-of-work",str(prod),"--source-dir",str(live),"--output-json",str(m/f"parity-{suffix}.json"),"--output-md",str(m/f"parity-{suffix}.md"),"--isolated-migration","--migration-authority",AUTH],m/f"parity-{suffix}.stdout",m/f"parity-{suffix}.stderr")
  run(["python3",tool("derive_review_checklist.py"),str(prod),"--output",str(m/f"checklist-{suffix}.json")],m/f"checklist-{suffix}.stdout",m/f"checklist-{suffix}.stderr")
  run(["python3",tool("render_scope_of_work.py"),str(prod),"--output",str(m/f"ScopeOfWork-{suffix}.html")],m/f"render-{suffix}.stdout",m/f"render-{suffix}.stderr")
 for a,b in [("claim-map-a.csv","claim-map-b.csv"),("parity-a.json","parity-b.json"),("checklist-a.json","checklist-b.json"),("ScopeOfWork-a.html","ScopeOfWork-b.html")]: assert (m/a).read_bytes()==(m/b).read_bytes()
 parity=json.loads((m/"parity-a.json").read_text()); maps=len(parity["checks"]); covered=sum(x["line_end"]-x["line_start"]+1 for x in parity["checks"]); assert parity["pass"] and covered==lines
 partial=m/"negative-partial"; partial.mkdir(); shutil.copy2(live/"Datasheet.md",partial/"Datasheet.md"); shutil.copy2(live/"_STATUS.md",partial/"_STATUS.md")
 mutant=m/"mutated-production"; mutant.mkdir(); shutil.copy2(prod,mutant/"ScopeOfWork.md"); (mutant/"ScopeOfWork.md").write_text((mutant/"ScopeOfWork.md").read_text()+"\n<!-- mutation -->\n")
 negs=[("unauthorized-dual",["python3",tool("validate_scope_of_work.py"),str(m/"workspace-a"),"--isolated-migration","--migration-authority","UNAUTHORIZED","--json"]),("partial-validation",["python3",tool("validate_scope_of_work.py"),str(partial),"--json"]),("ambiguous-checklist",["python3",tool("derive_review_checklist.py"),str(m/"workspace-a"),"--output",str(m/"negative-ambiguous-checklist.json")]),("unauthorized-checklist",["python3",tool("derive_review_checklist.py"),str(m/"workspace-a"),"--isolated-migration","--migration-authority","UNAUTHORIZED","--output",str(m/"negative-unauthorized-checklist.json")]),("evidence-render",["python3",tool("render_scope_of_work.py"),str(m/"workspace-a/ScopeOfWork.md"),"--output",str(m/"negative-evidence-render.html")]),("mutated-map",["python3",tool("map_scope_of_work_claims.py"),"--scope-of-work",str(evid),"--production-scope-of-work",str(mutant/"ScopeOfWork.md"),"--source-dir",str(live),"--output-csv",str(m/"negative-mutated-map.csv")]),("mutated-parity",["python3",tool("report_scope_of_work_parity.py"),"--scope-of-work",str(evid),"--production-scope-of-work",str(mutant/"ScopeOfWork.md"),"--source-dir",str(live),"--output-json",str(m/"negative-mutated-parity.json"),"--isolated-migration","--migration-authority",AUTH])]
 for name,cmd in negs: rc=run(cmd,m/f"negative-{name}.stdout",m/f"negative-{name}.stderr",True); write(m/f"negative-{name}.exit",str(rc))
 for name in LEGACY+CONTROL: assert sha(live/name)==expected[name]; hashes.append([name,sha(live/name),"after","PASS"])
 tsv(m/"SOURCE_HASHES.tsv",["file","sha256","phase","verdict"],hashes)
 tsv(m/"DETERMINISM.tsv",["artifact","sha256_a","sha256_b","byte_identical"],[["evidence_conversion",sha(m/"workspace-a/ScopeOfWork.md"),sha(m/"workspace-b/ScopeOfWork.md"),"true"],["clean_finalization",sha(m/"final-a/ScopeOfWork.md"),sha(m/"final-b/ScopeOfWork.md"),"true"],["finalization_report",sha(m/"final-a/report.json"),sha(m/"final-b/report.json"),"true"]])
 tsv(m/"DERIVATIVE_DETERMINISM.tsv",["artifact","sha256_a","sha256_b","byte_identical"],[["claim_map",sha(m/"claim-map-a.csv"),sha(m/"claim-map-b.csv"),"true"],["parity_json",sha(m/"parity-a.json"),sha(m/"parity-b.json"),"true"],["checklist",sha(m/"checklist-a.json"),sha(m/"checklist-b.json"),"true"],["render_html",sha(m/"ScopeOfWork-a.html"),sha(m/"ScopeOfWork-b.html"),"true"]])
 sim=m/"simulation"; apply=sim/"apply"; rollback=sim/"rollback"; shutil.copytree(live,apply); shutil.copy2(prod,apply/"ScopeOfWork.md")
 for n in LEGACY: (apply/n).unlink()
 run(["python3",tool("validate_scope_of_work.py"),str(apply/"ScopeOfWork.md"),"--json"],m/"simulation-apply-validation.json",m/"simulation-apply-validation.stderr"); shutil.copytree(apply,rollback); (rollback/"ScopeOfWork.md").unlink()
 for n in LEGACY: shutil.copy2(live/n,rollback/n)
 assert all((rollback/n).read_bytes()==(live/n).read_bytes() for n in LEGACY+CONTROL)
 for n in LEGACY: replacements.append([did,"DELETE",f"{r['live_path']}/{n}",sha(live/n)]); inverse.append([did,"RESTORE",f"{r['live_path']}/{n}",sha(live/n)])
 replacements.append([did,"ADD",f"{r['live_path']}/ScopeOfWork.md",sha(prod)]); inverse.append([did,"DELETE",f"{r['live_path']}/ScopeOfWork.md",sha(prod)]); simulations.append([did,"APPLY_TARGET_ROLLBACK","PASS",sha(prod),r["status_sha256"]])
 write(m/"IMMUTABLE_LITERAL_AND_CONTEXT_REVIEW.md",f"""# Immutable literal and source-context review — {did}\n\n- Live source path: `{r['live_path']}`\n- Exact project scope refs: `{r['scope_refs']}`\n- Exact package objective refs: `{r['objective_refs']}`\n- Exact decomposition basis: `{r['decomposition_basis']}`\n- Lifecycle/format: `IN_PROGRESS` / `LEGACY_FOUR_DOC`; live SOW absent.\n- All four production documents plus `_CONTEXT.md` and `_REFERENCES.md` were read completely before conversion.\n- Semantic posture: faithful preservation only; tests did not create scope, and unresolved engineering, tolerance, release, or authority questions remain source-grounded findings.\n""")
 write(m/"MEMBER_SUMMARY.md",f"# {did} member terminal summary\n\n- Checkpoints: `10/10 COMPLETE`.\n- Evidence SHA-256: `{sha(evid)}`\n- Clean production SHA-256: `{sha(prod)}`\n- Finalization report SHA-256: `{sha(c/'finalization.json')}`\n- Production-bound mappings: `{maps}`; source lines: `{covered}/{lines}`.\n- All repeated artifact families are byte-identical; seven negative probes fail closed; apply/target/rollback passes.\n- All verdict classes: `PASS`; blocker / waiver / unknown / semantic expansion / project write: none.\n")
 progress.append([seq,did,"validation_mapping_qa",qa,now(),"PASS",0,"NONE","NONE","NONE",f"members/{did}/validation-sow-v1.json;members/{did}/parity-a.json;members/{did}/checklist-a.json;members/{did}/negative-*.exit","NO"]); post=now(); progress.append([seq,did,"postcheck_terminal",post,post,"PASS",0,"NONE","NONE","NONE",f"members/{did}/SOURCE_HASHES.tsv","YES"])
 results.append([did,sha(evid),sha(prod),sha(c/"finalization.json"),maps,covered,lines,"PASS"]); total_maps+=maps; total_lines+=lines; total_covered+=covered
assert total_lines==total_covered==1357
tsv(CHILD/"PROGRESS.tsv",["sequence","deliverable_id","stage","started_utc","finished_utc","result","retries","remediation","blocker","waiver","evidence","terminal"],progress)
with (CHILD/"RUNTIME_EVENTS.jsonl").open("w",encoding="utf-8") as f:
 for e in events: f.write(json.dumps(e,separators=(",",":"))+"\n")
tsv(CHILD/"MEMBER_RESULTS.tsv",["deliverable_id","evidence_sha256","production_sha256","finalization_sha256","mappings","covered_lines","total_lines","verdict"],results)
tsv(CHILD/"VERDICTS.tsv",["deliverable_id","schema","project_content","preservation_containment","clean_finalization","execution_substrate","blocker","waiver","unknown"],[[d,"PASS","PASS","PASS","PASS","PASS","NONE","NONE","NONE"] for d in DIDS])
tsv(CHILD/"REPLACEMENT_ROWS.tsv",["deliverable_id","operation","path","sha256"],replacements); tsv(CHILD/"INVERSE_ROWS.tsv",["deliverable_id","operation","path","sha256"],inverse); tsv(CHILD/"SIMULATIONS.tsv",["deliverable_id","simulation","verdict","production_sha256","status_sha256"],simulations)
print(json.dumps({"status":"MEMBERS_COMPLETE","members":5,"mappings":total_maps,"lines":total_lines}))
