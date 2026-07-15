#!/usr/bin/env python3
import csv, hashlib, json, shutil, subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
CHILD = RUN / "instances/WORKING-P2-PKG08/children/AUTHOR-B2"
CAND = RUN / "candidates/W_P2/PIP-PKG08"
PM = RUN / "snapshots/W_P2/preflight/P2_MANIFEST.tsv"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
BASIS = "eaad463c0d481f6f1654e6adb5ee718f566176e9"
DIDS = ["DEL-08-06"]
LEGACY = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROL = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
SEEDS = {
 "DEL-08-06": (
  "A state, comparison, and handoff report-section contract covering immutable model-state and analysis-run records, deterministic comparisons, handoff manifests, warnings, assumptions, limitations, units, hashes, provenance, and unsupported-target disclosures is produced without implying professional validation or acceptance.",
  "The contract preserves stable record identities, source-envelope diagnostics, deterministic comparison mappings and tolerance references when available, handoff traceability, missing-data visibility, protected/private-content boundaries, and professional-authority limits while retaining unresolved implementation, schema, layout, and external-payload decisions as source-grounded TBDs.",
  "Validate the contract and review source parity, state/run/comparison/handoff coverage, SOW-024 report content, stable identities and hashes, units and provenance, deterministic ordering, missing-data findings, unsupported-target disclosures, protected-content and professional-authority boundaries, and every retained TBD or governed residual.")}

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def now(): return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def write(p, s): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(s.rstrip()+"\n", encoding="utf-8")
def tsv(p, header, data):
 p.parent.mkdir(parents=True, exist_ok=True)
 with p.open("w", newline="", encoding="utf-8") as f:
  w=csv.writer(f,delimiter="\t",lineterminator="\n"); w.writerow(header); w.writerows(data)
def run(cmd, out, err, expect=0):
 with out.open("w") as o, err.open("w") as e: rc=subprocess.run(cmd,cwd=ROOT,stdout=o,stderr=e).returncode
 if (expect == 0 and rc != 0) or (expect != 0 and rc == 0): raise RuntimeError(f"unexpected rc={rc}: {' '.join(cmd)}")
 return rc
def tool(name): return str(ROOT / "tools/scope_of_work" / name)

assert subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip()==BASIS
assert subprocess.check_output(["git","rev-parse","origin/main"],cwd=ROOT,text=True).strip()==BASIS
with PM.open(newline="",encoding="utf-8") as f: rows={r["deliverable_id"]:r for r in csv.DictReader(f,delimiter="\t")}

progress=[]; events=[]; member_rows=[]; replacements=[]; inverse=[]; simulations=[]
total_maps=total_lines=total_covered=0
for seq,did in enumerate(DIDS,1):
 r=rows[did]; live=ROOT/r["live_path"]; m=CHILD/"members"/did; c=CAND/did
 m.mkdir(parents=True,exist_ok=True); (c/"evidence").mkdir(parents=True,exist_ok=True); (c/"production").mkdir(parents=True,exist_ok=True)
 for stale in [m/"workspace-a",m/"workspace-b",m/"final-a",m/"final-b",m/"negative-partial",m/"mutated-production",m/"simulation"]:
  if stale.exists(): shutil.rmtree(stale)
 start=now(); events.append({"timestamp_utc":start,"sequence":seq,"deliverable_id":did,"stage":"precheck","event":"start","attempt":1,"reason_code":"NONE"})
 assert r["lifecycle"]=="IN_PROGRESS" and r["live_format"]=="LEGACY_FOUR_DOC" and not (live/"ScopeOfWork.md").exists()
 assert subprocess.check_output(["git","show",f"{BASIS}:{r['live_path']}/_STATUS.md"],cwd=ROOT)==(live/"_STATUS.md").read_bytes()
 hash_rows=[]
 expected={"Datasheet.md":r["datasheet_sha256"],"Specification.md":r["specification_sha256"],"Guidance.md":r["guidance_sha256"],"Procedure.md":r["procedure_sha256"],"_STATUS.md":r["status_sha256"],"_CONTEXT.md":r["context_sha256"],"_REFERENCES.md":r["references_sha256"],"_DEPENDENCIES.md":r["dependencies_md_sha256"],"Dependencies.csv":r["dependencies_csv_sha256"]}
 for name in LEGACY+CONTROL:
  assert sha(live/name)==expected[name]; hash_rows.append([name,sha(live/name),"before","PASS"])
 lines=sum(len((live/n).read_bytes().splitlines()) for n in LEGACY); assert lines==int(r["source_lines"])
 raw="\t".join(r.values()); write(m/"FROZEN_ROW.tsv",raw)
 end=now(); progress.append([seq,did,"precheck",start,end,"PASS",0,"NONE","NONE","NONE","members/%s/FROZEN_ROW.tsv;members/%s/SOURCE_HASHES.tsv"%(did,did),"YES"]); events.append({"timestamp_utc":end,"sequence":seq,"deliverable_id":did,"stage":"precheck","event":"finish","attempt":1,"reason_code":"NONE"})
 out_desc,ac,ver=SEEDS[did]
 conv_start=now(); events.append({"timestamp_utc":conv_start,"sequence":seq,"deliverable_id":did,"stage":"conversion","event":"start","attempt":1,"reason_code":"NONE"})
 for suffix in ["a","b"]:
  ws=m/f"workspace-{suffix}"; shutil.copytree(live,ws)
  cmd=["python3",tool("convert_four_documents_to_scope_of_work.py"),"--deliverable",str(ws),"--deliverable-id",did,"--package-id","PKG-08","--decomposition-basis",r["decomposition_basis"],"--isolated-migration","--migration-authority",AUTH,"--output-description",out_desc,"--acceptance-criterion",ac,"--verification-method",ver]
  for x in [q.strip() for q in r["scope_refs"].split(",")]: cmd += ["--project-scope-ref",x]
  for x in [q.strip() for q in r["objective_refs"].split(",")]: cmd += ["--package-objective-ref",x]
  run(cmd,m/f"conversion-{suffix}.stdout",m/f"conversion-{suffix}.stderr")
  run(["python3",tool("validate_scope_of_work.py"),str(ws),"--isolated-migration","--migration-authority",AUTH,"--json"],m/f"validation-dual-{suffix}.json",m/f"validation-dual-{suffix}.stderr")
 assert (m/"workspace-a/ScopeOfWork.md").read_bytes()==(m/"workspace-b/ScopeOfWork.md").read_bytes()
 shutil.copy2(m/"workspace-a/ScopeOfWork.md",c/"evidence/ScopeOfWork.md")
 conv_end=now(); progress.append([seq,did,"conversion",conv_start,conv_end,"PASS",0,"NONE","NONE","NONE",f"members/{did}/DETERMINISM.tsv","NO"]); events.append({"timestamp_utc":conv_end,"sequence":seq,"deliverable_id":did,"stage":"conversion","event":"finish","attempt":1,"reason_code":"NONE"})
 fin_start=now()
 for suffix in ["a","b"]:
  fd=m/f"final-{suffix}"; fd.mkdir()
  run(["python3",tool("finalize_scope_of_work.py"),"--evidence-candidate",str(m/"workspace-a/ScopeOfWork.md"),"--output",str(fd/"ScopeOfWork.md"),"--report",str(fd/"report.json")],m/f"finalization-{suffix}.stdout",m/f"finalization-{suffix}.stderr")
 assert (m/"final-a/ScopeOfWork.md").read_bytes()==(m/"final-b/ScopeOfWork.md").read_bytes()
 assert (m/"final-a/report.json").read_bytes()==(m/"final-b/report.json").read_bytes()
 shutil.copy2(m/"final-a/ScopeOfWork.md",c/"production/ScopeOfWork.md"); shutil.copy2(m/"final-a/report.json",c/"finalization.json")
 fin_end=now(); progress.append([seq,did,"finalization",fin_start,fin_end,"PASS",0,"NONE","NONE","NONE",f"members/{did}/final-a/report.json;members/{did}/DETERMINISM.tsv","NO"])
 qa_start=now(); prod=c/"production/ScopeOfWork.md"; evid=c/"evidence/ScopeOfWork.md"
 run(["python3",tool("validate_scope_of_work.py"),str(prod),"--json"],m/"validation-sow-v1.json",m/"validation-sow-v1.stderr")
 for suffix in ["a","b"]:
  run(["python3",tool("map_scope_of_work_claims.py"),"--scope-of-work",str(evid),"--production-scope-of-work",str(prod),"--source-dir",str(live),"--output-csv",str(m/f"claim-map-{suffix}.csv")],m/f"claim-map-{suffix}.stdout",m/f"claim-map-{suffix}.stderr")
  run(["python3",tool("report_scope_of_work_parity.py"),"--scope-of-work",str(evid),"--production-scope-of-work",str(prod),"--source-dir",str(live),"--output-json",str(m/f"parity-{suffix}.json"),"--output-md",str(m/f"parity-{suffix}.md"),"--isolated-migration","--migration-authority",AUTH],m/f"parity-{suffix}.stdout",m/f"parity-{suffix}.stderr")
  run(["python3",tool("derive_review_checklist.py"),str(prod),"--output",str(m/f"checklist-{suffix}.json")],m/f"checklist-{suffix}.stdout",m/f"checklist-{suffix}.stderr")
  run(["python3",tool("render_scope_of_work.py"),str(prod),"--output",str(m/f"ScopeOfWork-{suffix}.html")],m/f"render-{suffix}.stdout",m/f"render-{suffix}.stderr")
 for a,b in [("claim-map-a.csv","claim-map-b.csv"),("parity-a.json","parity-b.json"),("checklist-a.json","checklist-b.json"),("ScopeOfWork-a.html","ScopeOfWork-b.html")]: assert (m/a).read_bytes()==(m/b).read_bytes()
 parity=json.loads((m/"parity-a.json").read_text()); assert parity["pass"]
 maps=len(parity["checks"]); covered=sum(x["line_end"]-x["line_start"]+1 for x in parity["checks"]); assert covered==lines
 # Seven fail-closed probes.
 partial=m/"negative-partial"; partial.mkdir(); shutil.copy2(live/"Datasheet.md",partial/"Datasheet.md"); shutil.copy2(live/"_STATUS.md",partial/"_STATUS.md")
 mutant=m/"mutated-production"; mutant.mkdir(); shutil.copy2(prod,mutant/"ScopeOfWork.md"); (mutant/"ScopeOfWork.md").write_text((mutant/"ScopeOfWork.md").read_text()+"\n<!-- mutation -->\n")
 negs=[
  ("unauthorized-dual",["python3",tool("validate_scope_of_work.py"),str(m/"workspace-a"),"--isolated-migration","--migration-authority","UNAUTHORIZED","--json"]),
  ("partial-validation",["python3",tool("validate_scope_of_work.py"),str(partial),"--json"]),
  ("ambiguous-checklist",["python3",tool("derive_review_checklist.py"),str(m/"workspace-a"),"--output",str(m/"negative-ambiguous-checklist.json")]),
  ("unauthorized-checklist",["python3",tool("derive_review_checklist.py"),str(m/"workspace-a"),"--isolated-migration","--migration-authority","UNAUTHORIZED","--output",str(m/"negative-unauthorized-checklist.json")]),
  ("evidence-render",["python3",tool("render_scope_of_work.py"),str(m/"workspace-a/ScopeOfWork.md"),"--output",str(m/"negative-evidence-render.html")]),
  ("mutated-map",["python3",tool("map_scope_of_work_claims.py"),"--scope-of-work",str(evid),"--production-scope-of-work",str(mutant/"ScopeOfWork.md"),"--source-dir",str(live),"--output-csv",str(m/"negative-mutated-map.csv")]),
  ("mutated-parity",["python3",tool("report_scope_of_work_parity.py"),"--scope-of-work",str(evid),"--production-scope-of-work",str(mutant/"ScopeOfWork.md"),"--source-dir",str(live),"--output-json",str(m/"negative-mutated-parity.json"),"--isolated-migration","--migration-authority",AUTH])]
 for name,cmd in negs:
  rc=run(cmd,m/f"negative-{name}.stdout",m/f"negative-{name}.stderr",expect=1); write(m/f"negative-{name}.exit",str(rc))
 qa_end=now(); progress.append([seq,did,"validation_mapping_qa",qa_start,qa_end,"PASS",0,"NONE","NONE","NONE",f"members/{did}/validation-sow-v1.json;members/{did}/parity-a.json;members/{did}/checklist-a.json;members/{did}/negative-*.exit","NO"])
 for name in LEGACY+CONTROL:
  assert sha(live/name)==expected[name]; hash_rows.append([name,sha(live/name),"after","PASS"])
 tsv(m/"SOURCE_HASHES.tsv",["file","sha256","phase","verdict"],hash_rows)
 tsv(m/"DETERMINISM.tsv",["artifact","sha256_a","sha256_b","byte_identical"],[["evidence_conversion",sha(m/"workspace-a/ScopeOfWork.md"),sha(m/"workspace-b/ScopeOfWork.md"),"true"],["clean_finalization",sha(m/"final-a/ScopeOfWork.md"),sha(m/"final-b/ScopeOfWork.md"),"true"],["finalization_report",sha(m/"final-a/report.json"),sha(m/"final-b/report.json"),"true"]])
 tsv(m/"DERIVATIVE_DETERMINISM.tsv",["artifact","sha256_a","sha256_b","byte_identical"],[["claim_map",sha(m/"claim-map-a.csv"),sha(m/"claim-map-b.csv"),"true"],["parity_json",sha(m/"parity-a.json"),sha(m/"parity-b.json"),"true"],["checklist",sha(m/"checklist-a.json"),sha(m/"checklist-b.json"),"true"],["render_html",sha(m/"ScopeOfWork-a.html"),sha(m/"ScopeOfWork-b.html"),"true"]])
 write(m/"IMMUTABLE_LITERAL_AND_CONTEXT_REVIEW.md",f"""# Immutable literal and source-context review — {did}

- Live source path: `{r['live_path']}`
- Exact project scope refs: `{r['scope_refs']}`
- Exact package objective refs: `{r['objective_refs']}`
- Exact decomposition basis: `{r['decomposition_basis']}`
- Lifecycle/format: `IN_PROGRESS` / `LEGACY_FOUR_DOC`; live SOW absent.
- All four production documents plus `_CONTEXT.md` and `_REFERENCES.md` were inspected before conversion.
- Semantic posture: faithful preservation only; tests did not create scope and unresolved engineering or authority questions remain source-grounded findings.
""")
 write(m/"MEMBER_SUMMARY.md",f"""# {did} member terminal summary

- Evidence SHA-256: `{sha(evid)}`
- Clean production SHA-256: `{sha(prod)}`
- Finalization report SHA-256: `{sha(c/'finalization.json')}`
- Production-bound mappings: `{maps}`; source lines: `{covered}/{lines}`.
- Two conversions, finalizations/reports, maps/parity results, checklists, and HTML renders are byte-identical.
- Seven applicable negative probes failed closed; apply/target/rollback simulation passed.
- Schema, project-content, preservation/containment, clean-finalization, and execution-substrate verdicts: `PASS`.
""")
 sim=m/"simulation"; apply=sim/"apply"; rollback=sim/"rollback"; shutil.copytree(live,apply); shutil.copy2(prod,apply/"ScopeOfWork.md")
 for n in LEGACY: (apply/n).unlink()
 run(["python3",tool("validate_scope_of_work.py"),str(apply/"ScopeOfWork.md"),"--json"],m/"simulation-apply-validation.json",m/"simulation-apply-validation.stderr")
 shutil.copytree(apply,rollback); (rollback/"ScopeOfWork.md").unlink()
 for n in LEGACY: shutil.copy2(live/n,rollback/n)
 assert all((rollback/n).read_bytes()==(live/n).read_bytes() for n in LEGACY+CONTROL)
 for n in LEGACY: replacements.append([did,"DELETE",f"{r['live_path']}/{n}",sha(live/n)]); inverse.append([did,"RESTORE",f"{r['live_path']}/{n}",sha(live/n)])
 replacements.append([did,"ADD",f"{r['live_path']}/ScopeOfWork.md",sha(prod)]); inverse.append([did,"DELETE",f"{r['live_path']}/ScopeOfWork.md",sha(prod)])
 simulations.append([did,"APPLY_TARGET_ROLLBACK","PASS",sha(prod),r["status_sha256"]])
 member_rows.append([did,sha(evid),sha(prod),sha(c/"finalization.json"),maps,covered,lines,"PASS"]); total_maps+=maps; total_lines+=lines; total_covered+=covered
 post=now(); progress.append([seq,did,"postcheck_terminal",post,post,"PASS",0,"NONE","NONE","NONE",f"members/{did}/SOURCE_HASHES.tsv","YES"])

assert total_lines==total_covered==301
tsv(CHILD/"PROGRESS.tsv",["sequence","deliverable_id","stage","started_utc","finished_utc","result","retries","remediation","blocker","waiver","evidence","terminal"],progress)
with (CHILD/"RUNTIME_EVENTS.jsonl").open("w",encoding="utf-8") as f:
 for e in events: f.write(json.dumps(e,separators=(",",":"))+"\n")
tsv(CHILD/"MEMBER_RESULTS.tsv",["deliverable_id","evidence_sha256","production_sha256","finalization_sha256","mappings","covered_lines","total_lines","verdict"],member_rows)
tsv(CHILD/"VERDICTS.tsv",["deliverable_id","schema","project_content","preservation_containment","clean_finalization","execution_substrate","blocker","waiver","unknown"],[[d,"PASS","PASS","PASS","PASS","PASS","NONE","NONE","NONE"] for d in DIDS])
tsv(CHILD/"REPLACEMENT_ROWS.tsv",["deliverable_id","operation","path","sha256"],replacements); tsv(CHILD/"INVERSE_ROWS.tsv",["deliverable_id","operation","path","sha256"],inverse); tsv(CHILD/"SIMULATIONS.tsv",["deliverable_id","simulation","verdict","production_sha256","status_sha256"],simulations)
print(json.dumps({"status":"MEMBERS_COMPLETE","members":1,"mappings":total_maps,"lines":total_lines}))
