#!/usr/bin/env python3
"""Deterministic WORKING-P2-PKG07 two-batch manager fan-in."""
from __future__ import annotations
import csv, hashlib, json, os, shutil, subprocess, tempfile
from pathlib import Path

ROOT=Path(subprocess.check_output(["git","rev-parse","--show-toplevel"],text=True).strip())
RUN=ROOT/"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
HERE=RUN/"instances/WORKING-P2-PKG07"; CAND=RUN/"candidates/W_P2/PIP-PKG07"
PRE=RUN/"snapshots/W_P2/preflight"; TOOLS=ROOT/"tools/scope_of_work"
AUTH="D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
LEGACY=["Datasheet.md","Specification.md","Guidance.md","Procedure.md"]
CONTROL=["_STATUS.md","_CONTEXT.md","_REFERENCES.md","_DEPENDENCIES.md","Dependencies.csv"]
COL={"Datasheet.md":"datasheet_sha256","Specification.md":"specification_sha256","Guidance.md":"guidance_sha256","Procedure.md":"procedure_sha256","_STATUS.md":"status_sha256","_CONTEXT.md":"context_sha256","_REFERENCES.md":"references_sha256","_DEPENDENCIES.md":"dependencies_md_sha256","Dependencies.csv":"dependencies_csv_sha256"}
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(a):
 r=subprocess.run(a,cwd=ROOT,text=True,capture_output=True,env={**os.environ,"PYTHONDONTWRITEBYTECODE":"1"}); assert r.returncode==0,(a,r.stdout,r.stderr); return r
def write_tsv(p,fields,rows):
 with p.open("w",encoding="utf-8",newline="") as f:
  w=csv.writer(f,delimiter="\t",lineterminator="\n"); w.writerow(fields); w.writerows(rows)
def copykit(src,dst):
 dst.mkdir(parents=True)
 for n in LEGACY+CONTROL: shutil.copy2(src/n,dst/n)
def canon(p):
 return {(r["deliverable_id"],"ADD" if r["operation"]=="RESTORE" else r["operation"],r["path"],r["sha256"]) for r in csv.DictReader(p.open(),delimiter="\t")}
def main():
 assert subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip()=="eaad463c0d481f6f1654e6adb5ee718f566176e9"
 rows=[r for r in csv.DictReader((PRE/"P2_MANIFEST.tsv").open(),delimiter="\t") if r["package"]=="PKG-07"]
 assert [r["deliverable_id"] for r in rows]==[f"DEL-07-{i:02d}" for i in range(1,9)]
 batches=[("B1",range(1,6),175,1535),("B2",range(6,9),97,887)]
 child_shas={}
 for batch,nums,maps,lines in batches:
  av=HERE/f"children/AUTHOR-{batch}"; vv=HERE/f"children/VERIFY-{batch}"
  ast=json.loads((av/"STATUS.json").read_text()); vst=json.loads((vv/"STATUS.json").read_text())
  assert ast["status"]=="PASS" and vst["status"]=="PASS_UNCHANGED"
  assert (ast["members_complete"],ast["mappings_passed"],ast["source_lines_covered"])==(len(list(nums)),maps,lines)
  assert (vst["members_complete"],vst["mappings"],vst["source_lines"])==(len(list(nums)),maps,lines)
  assert canon(av/"REPLACEMENT_ROWS.tsv")==canon(vv/"REPLACEMENT_ROWS.tsv")
  assert canon(av/"INVERSE_ROWS.tsv")==canon(vv/"INVERSE_ROWS.tsv")
  child_shas[f"author_{batch.lower()}_manifest_sha256"]=sha(av/"MANIFEST.tsv")
  child_shas[f"verifier_{batch.lower()}_manifest_sha256"]=sha(vv/"MANIFEST.tsv")
 validation=HERE/"manager-validation"; shutil.rmtree(validation,ignore_errors=True); validation.mkdir()
 members=[]; forward=[]; inverse=[]; sims=[]; mt=lt=0
 for row in rows:
  did=row["deliverable_id"]; live=ROOT/row["live_path"]; ev=CAND/did/"evidence/ScopeOfWork.md"; prod=CAND/did/"production/ScopeOfWork.md"; rep=CAND/did/"finalization.json"; out=validation/did; out.mkdir()
  assert row["lifecycle"]=="IN_PROGRESS" and row["live_format"]=="LEGACY_FOUR_DOC" and not (live/"ScopeOfWork.md").exists()
  for n,c in COL.items(): assert sha(live/n)==row[c]
  report=json.loads(rep.read_text()); assert report["evidence_candidate_sha256"]==sha(ev) and report["production_scope_of_work_sha256"]==sha(prod)
  (out/"validation-sow-v1.json").write_text(run(["python3",str(TOOLS/"validate_scope_of_work.py"),"--json",str(prod)]).stdout)
  run(["python3",str(TOOLS/"map_scope_of_work_claims.py"),"--scope-of-work",str(ev),"--production-scope-of-work",str(prod),"--source-dir",str(live),"--output-csv",str(out/"claim-map.csv")])
  run(["python3",str(TOOLS/"report_scope_of_work_parity.py"),"--scope-of-work",str(ev),"--production-scope-of-work",str(prod),"--source-dir",str(live),"--output-json",str(out/"parity.json"),"--output-md",str(out/"parity.md"),"--isolated-migration","--migration-authority",AUTH])
  run(["python3",str(TOOLS/"derive_review_checklist.py"),str(prod),"--output",str(out/"checklist.json")]); run(["python3",str(TOOLS/"render_scope_of_work.py"),str(prod),"--output",str(out/"render.html")])
  parity=json.loads((out/"parity.json").read_text()); assert parity["pass"] and not parity["issues"]
  maps=len(parity["checks"]); lines=sum(x["line_end"]-x["line_start"]+1 for x in parity["checks"]); expected=sum(len((live/n).read_bytes().splitlines()) for n in LEGACY); assert lines==expected
  with tempfile.TemporaryDirectory(prefix=f"pkg07-{did}-") as td:
   dual=Path(td)/"dual"; copykit(live,dual); shutil.copy2(ev,dual/"ScopeOfWork.md"); run(["python3",str(TOOLS/"validate_scope_of_work.py"),"--isolated-migration","--migration-authority",AUTH,"--json",str(dual)])
   target=Path(td)/"target"; copykit(live,target); shutil.copy2(prod,target/"ScopeOfWork.md"); [(target/n).unlink() for n in LEGACY]; run(["python3",str(TOOLS/"validate_scope_of_work.py"),"--json",str(target/"ScopeOfWork.md")]); assert all(sha(target/n)==sha(live/n) for n in CONTROL)
   (target/"ScopeOfWork.md").unlink(); [shutil.copy2(live/n,target/n) for n in LEGACY]; assert all(sha(target/n)==sha(live/n) for n in LEGACY+CONTROL)
  mt+=maps; lt+=lines; members.append([did,row["live_path"],row["status_sha256"],sha(ev),sha(prod),sha(rep),maps,lines,expected,"PASS","PASS_UNCHANGED"]); sims.append([did,"PASS","PASS","PASS"])
  sow=f'{row["live_path"]}/ScopeOfWork.md'; forward.append([did,"ADD",sow,"ABSENT",sha(prod)]); inverse.append([did,"DELETE",sow,sha(prod),"ABSENT"])
  for n in LEGACY:
   p=f'{row["live_path"]}/{n}'; h=row[COL[n]]; forward.append([did,"DELETE",p,h,"ABSENT"]); inverse.append([did,"ADD",p,"ABSENT",h])
 assert (mt,lt,len(forward),len(inverse),len(sims))==(272,2422,40,40,8)
 write_tsv(HERE/"MEMBER_RESULTS.tsv",["deliverable_id","live_path","status_sha256","evidence_sha256","production_sha256","finalization_sha256","mappings","covered_lines","total_lines","author","verifier"],members)
 write_tsv(HERE/"REPLACEMENT_MANIFEST.tsv",["deliverable_id","action","path","before_sha256","after_sha256"],forward); write_tsv(HERE/"ROLLBACK_MANIFEST.tsv",["deliverable_id","action","path","before_sha256","after_sha256"],inverse); write_tsv(HERE/"SIMULATION.tsv",["deliverable_id","apply","target_validation","rollback"],sims)
 summary={"status":"PASS","members":8,"mappings":272,"source_lines":2422,"replacement_rows":40,"rollback_rows":40,"simulations_pass":8,"project_writes":0,"candidate_writes_by_verifiers":0,**child_shas}
 (HERE/"MANAGER_VALIDATION.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n"); print(json.dumps(summary,indent=2,sort_keys=True))
if __name__=="__main__": main()
