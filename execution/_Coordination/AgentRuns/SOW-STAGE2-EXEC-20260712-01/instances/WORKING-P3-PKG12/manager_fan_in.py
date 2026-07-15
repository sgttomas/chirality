#!/usr/bin/env python3
"""Independent deterministic fan-in for WORKING-P3-PKG12."""
import csv, hashlib, json, os, shutil, subprocess, tempfile
from pathlib import Path

ROOT=Path(subprocess.check_output(["git","rev-parse","--show-toplevel"],text=True).strip())
RUN=ROOT/"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
HERE=RUN/"instances/WORKING-P3-PKG12"; PRE=RUN/"snapshots/W_P3/preflight"
CAND=RUN/"candidates/W_P3/PIP-PKG12"; TOOLS=ROOT/"tools/scope_of_work"
LEGACY=["Datasheet.md","Specification.md","Guidance.md","Procedure.md"]
CONTROL=["_STATUS.md","_CONTEXT.md","_REFERENCES.md","_DEPENDENCIES.md","Dependencies.csv"]
COL={"Datasheet.md":"datasheet_sha256","Specification.md":"specification_sha256","Guidance.md":"guidance_sha256","Procedure.md":"procedure_sha256","_STATUS.md":"status_sha256","_CONTEXT.md":"context_sha256","_REFERENCES.md":"references_sha256","_DEPENDENCIES.md":"dependencies_md_sha256","Dependencies.csv":"dependencies_csv_sha256"}

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(args):
 r=subprocess.run(args,cwd=ROOT,text=True,capture_output=True,env={**os.environ,"PYTHONDONTWRITEBYTECODE":"1"})
 assert r.returncode==0,(args,r.stdout,r.stderr); return r
def tsv(path,fields,rows):
 with path.open("w",encoding="utf-8",newline="") as f:
  w=csv.writer(f,delimiter="\t",lineterminator="\n"); w.writerow(fields); w.writerows(rows)
def copykit(src,dst):
 dst.mkdir(parents=True)
 for n in LEGACY+CONTROL: shutil.copy2(src/n,dst/n)
def canon(path):
 return {(r["deliverable_id"],"ADD" if r["operation"]=="RESTORE" else r["operation"],r["path"],r["sha256"]) for r in csv.DictReader(path.open(),delimiter="\t")}

assert subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip()=="4d153302c3c4cd42578936db160c2bac1270225a"
rows=[r for r in csv.DictReader((PRE/"P3_MANIFEST.tsv").open(),delimiter="\t") if r["package"]=="PKG-12"]
assert [r["deliverable_id"] for r in rows]==[f"DEL-12-{i:02d}" for i in range(1,6)]
A=HERE/"children/AUTHOR-B1"; V=HERE/"children/VERIFY-B1-R1"
ast=json.loads((A/"STATUS.json").read_text()); vst=json.loads((V/"STATUS.json").read_text())
assert (ast["status"],ast["members_complete"],ast["mappings_passed"],ast["source_lines_covered"])==("PASS",5,171,1737)
assert (vst["status"],vst["members"],vst["mappings"],vst["physical_source_lines"])==("PASS_UNCHANGED",5,171,1737)
assert vst["candidate_writes"]==vst["project_writes"]==vst["prohibited_reads"]==0
assert canon(A/"REPLACEMENT_ROWS.tsv")==canon(V/"REPLACEMENT_ROWS.tsv")
assert canon(A/"INVERSE_ROWS.tsv")==canon(V/"INVERSE_ROWS.tsv")

outroot=HERE/"manager-validation"; shutil.rmtree(outroot,ignore_errors=True); outroot.mkdir()
members=[]; forward=[]; inverse=[]; sims=[]; total_maps=total_lines=0
for row in rows:
 did=row["deliverable_id"]; live=ROOT/row["live_path"]; base=CAND/did
 ev=base/"evidence/ScopeOfWork.md"; prod=base/"production/ScopeOfWork.md"; report=base/"finalization.json"
 out=outroot/did; out.mkdir()
 assert row["lifecycle"]=="IN_PROGRESS" and row["live_format"]=="LEGACY_FOUR_DOC" and not (live/"ScopeOfWork.md").exists()
 for n,c in COL.items(): assert sha(live/n)==row[c]
 rep=json.loads(report.read_text()); assert rep["evidence_candidate_sha256"]==sha(ev) and rep["production_scope_of_work_sha256"]==sha(prod)
 fresh=out/"fresh-production.md"; frep=out/"fresh-finalization.json"
 run(["python3",str(TOOLS/"finalize_scope_of_work.py"),"--evidence-candidate",str(ev),"--output",str(fresh),"--report",str(frep)])
 assert fresh.read_bytes()==prod.read_bytes() and frep.read_bytes()==report.read_bytes()
 (out/"validation-sow-v1.json").write_text(run(["python3",str(TOOLS/"validate_scope_of_work.py"),"--json",str(prod)]).stdout)
 run(["python3",str(TOOLS/"map_scope_of_work_claims.py"),"--scope-of-work",str(ev),"--production-scope-of-work",str(prod),"--source-dir",str(live),"--output-csv",str(out/"claim-map.csv")])
 run(["python3",str(TOOLS/"report_scope_of_work_parity.py"),"--scope-of-work",str(ev),"--production-scope-of-work",str(prod),"--source-dir",str(live),"--output-json",str(out/"parity.json"),"--output-md",str(out/"parity.md"),"--isolated-migration","--migration-authority","D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"])
 run(["python3",str(TOOLS/"derive_review_checklist.py"),str(prod),"--output",str(out/"checklist.json")]); run(["python3",str(TOOLS/"render_scope_of_work.py"),str(prod),"--output",str(out/"render.html")])
 parity=json.loads((out/"parity.json").read_text()); assert parity["pass"] and not parity["issues"]
 maps=len(parity["checks"]); lines=sum(x["line_end"]-x["line_start"]+1 for x in parity["checks"]); expected=sum(len((live/n).read_bytes().splitlines()) for n in LEGACY); assert lines==expected
 with tempfile.TemporaryDirectory(prefix=f"pkg12-{did}-") as td:
  target=Path(td)/"target"; copykit(live,target); shutil.copy2(prod,target/"ScopeOfWork.md"); [(target/n).unlink() for n in LEGACY]
  run(["python3",str(TOOLS/"validate_scope_of_work.py"),"--json",str(target/"ScopeOfWork.md")]); assert all(sha(target/n)==sha(live/n) for n in CONTROL)
  (target/"ScopeOfWork.md").unlink(); [shutil.copy2(live/n,target/n) for n in LEGACY]; assert all(sha(target/n)==sha(live/n) for n in LEGACY+CONTROL)
 total_maps+=maps; total_lines+=lines; members.append([did,row["live_path"],row["status_sha256"],sha(ev),sha(prod),sha(report),maps,lines,expected,"PASS","PASS_UNCHANGED"]); sims.append([did,"PASS","PASS","PASS"])
 sow=f'{row["live_path"]}/ScopeOfWork.md'; forward.append([did,"ADD",sow,"ABSENT",sha(prod)]); inverse.append([did,"DELETE",sow,sha(prod),"ABSENT"])
 for n in LEGACY:
  p=f'{row["live_path"]}/{n}'; h=row[COL[n]]; forward.append([did,"DELETE",p,h,"ABSENT"]); inverse.append([did,"ADD",p,"ABSENT",h])
assert (total_maps,total_lines,len(forward),len(inverse),len(sims))==(171,1737,25,25,5)
tsv(HERE/"MEMBER_RESULTS.tsv",["deliverable_id","live_path","status_sha256","evidence_sha256","production_sha256","finalization_sha256","mappings","covered_lines","total_lines","author","verifier"],members)
tsv(HERE/"REPLACEMENT_MANIFEST.tsv",["deliverable_id","action","path","before_sha256","after_sha256"],forward); tsv(HERE/"ROLLBACK_MANIFEST.tsv",["deliverable_id","action","path","before_sha256","after_sha256"],inverse); tsv(HERE/"SIMULATION.tsv",["deliverable_id","apply","target_validation","rollback"],sims)
summary={"status":"PASS","members":5,"mappings":171,"source_lines":1737,"replacement_rows":25,"rollback_rows":25,"simulations_pass":5,"project_writes":0,"verifier_candidate_writes":0,"prohibited_reads":0,"author_manifest_sha256":sha(A/"MANIFEST.tsv"),"verifier_manifest_sha256":sha(V/"MANIFEST.tsv")}
(HERE/"MANAGER_VALIDATION.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n"); print(json.dumps(summary,sort_keys=True))
