#!/usr/bin/env python3
"""Deterministic WORKING-P2-PKG05 package fan-in."""
from __future__ import annotations
import csv, hashlib, json, os, shutil, subprocess, tempfile
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
HERE = RUN / "instances/WORKING-P2-PKG05"
CAND = RUN / "candidates/W_P2/PIP-PKG05"
PRE = RUN / "snapshots/W_P2/preflight"
TOOLS = ROOT / "tools/scope_of_work"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
LEGACY = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROL = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
HASH = {"Datasheet.md":"datasheet_sha256", "Specification.md":"specification_sha256",
        "Guidance.md":"guidance_sha256", "Procedure.md":"procedure_sha256",
        "_STATUS.md":"status_sha256", "_CONTEXT.md":"context_sha256",
        "_REFERENCES.md":"references_sha256", "_DEPENDENCIES.md":"dependencies_md_sha256",
        "Dependencies.csv":"dependencies_csv_sha256"}

def sha(p: Path) -> str: return hashlib.sha256(p.read_bytes()).hexdigest()
def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    r = subprocess.run(args, cwd=ROOT, text=True, capture_output=True,
                       env={**os.environ, "PYTHONDONTWRITEBYTECODE":"1"})
    if r.returncode: raise RuntimeError(f"exit {r.returncode}: {' '.join(args)}\n{r.stdout}\n{r.stderr}")
    return r
def tsv(path: Path, fields: list[str], rows: list[list[object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        w=csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(fields); w.writerows(rows)
def copykit(src: Path, dst: Path) -> None:
    dst.mkdir(parents=True)
    for n in LEGACY+CONTROL: shutil.copy2(src/n, dst/n)

def main() -> None:
    assert subprocess.check_output(["git","rev-parse","HEAD"], cwd=ROOT, text=True).strip()=="eaad463c0d481f6f1654e6adb5ee718f566176e9"
    rows=[r for r in csv.DictReader((PRE/"P2_MANIFEST.tsv").open(), delimiter="\t") if r["package"]=="PKG-05"]
    assert [r["deliverable_id"] for r in rows]==[f"DEL-05-{i:02d}" for i in range(1,6)]
    av=HERE/"children/AUTHOR-B1"; vv=HERE/"children/VERIFY-B1"
    ast=json.loads((av/"STATUS.json").read_text()); vst=json.loads((vv/"STATUS.json").read_text())
    assert ast["status"]=="PASS" and vst["status"]=="PASS_UNCHANGED"
    assert (ast["members_complete"],ast["mappings_passed"],ast["source_lines_covered"])==(5,148,1292)
    assert (vst["members_complete"],vst["mappings"],vst["source_lines"])==(5,148,1292)
    # Independent child rows may differ in ordering and use RESTORE as the
    # author's explicit inverse spelling. Canonicalize only that mechanical
    # representation, then require exact set equality.
    def canonical(path: Path) -> set[tuple[str,str,str,str]]:
        result=set()
        for r in csv.DictReader(path.open(), delimiter="\t"):
            op="ADD" if r["operation"]=="RESTORE" else r["operation"]
            result.add((r["deliverable_id"],op,r["path"],r["sha256"]))
        return result
    assert canonical(av/"REPLACEMENT_ROWS.tsv")==canonical(vv/"REPLACEMENT_ROWS.tsv")
    assert canonical(av/"INVERSE_ROWS.tsv")==canonical(vv/"INVERSE_ROWS.tsv")
    validation=HERE/"manager-validation"
    if validation.exists(): shutil.rmtree(validation)
    validation.mkdir()
    members=[]; forward=[]; inverse=[]; sims=[]; maps_total=lines_total=0
    for row in rows:
        did=row["deliverable_id"]; live=ROOT/row["live_path"]
        evidence=CAND/did/"evidence/ScopeOfWork.md"; production=CAND/did/"production/ScopeOfWork.md"; report=CAND/did/"finalization.json"
        out=validation/did; out.mkdir()
        assert row["lifecycle"]=="IN_PROGRESS" and row["live_format"]=="LEGACY_FOUR_DOC" and not (live/"ScopeOfWork.md").exists()
        for n,col in HASH.items(): assert sha(live/n)==row[col], (did,n)
        final=json.loads(report.read_text()); assert final["evidence_candidate_sha256"]==sha(evidence); assert final["production_scope_of_work_sha256"]==sha(production)
        clean=run(["python3",str(TOOLS/"validate_scope_of_work.py"),"--json",str(production)])
        (out/"validation-sow-v1.json").write_text(clean.stdout)
        with tempfile.TemporaryDirectory(prefix=f"p2-pkg05-{did}-") as td:
            dual=Path(td)/"dual"; copykit(live,dual); shutil.copy2(evidence,dual/"ScopeOfWork.md")
            d=run(["python3",str(TOOLS/"validate_scope_of_work.py"),"--isolated-migration","--migration-authority",AUTH,"--json",str(dual)])
            (out/"validation-dual.json").write_text(d.stdout)
            target=Path(td)/"target"; copykit(live,target); shutil.copy2(production,target/"ScopeOfWork.md")
            for n in LEGACY: (target/n).unlink()
            run(["python3",str(TOOLS/"validate_scope_of_work.py"),"--json",str(target/"ScopeOfWork.md")])
            assert all(sha(target/n)==sha(live/n) for n in CONTROL)
            (target/"ScopeOfWork.md").unlink()
            for n in LEGACY: shutil.copy2(live/n,target/n)
            assert all(sha(target/n)==sha(live/n) for n in LEGACY+CONTROL)
            sims.append([did,"PASS","PASS","PASS"])
        run(["python3",str(TOOLS/"map_scope_of_work_claims.py"),"--scope-of-work",str(evidence),"--production-scope-of-work",str(production),"--source-dir",str(live),"--output-csv",str(out/"claim-map.csv")])
        run(["python3",str(TOOLS/"report_scope_of_work_parity.py"),"--scope-of-work",str(evidence),"--production-scope-of-work",str(production),"--source-dir",str(live),"--output-json",str(out/"parity.json"),"--output-md",str(out/"parity.md"),"--isolated-migration","--migration-authority",AUTH])
        run(["python3",str(TOOLS/"derive_review_checklist.py"),str(production),"--output",str(out/"checklist.json")])
        run(["python3",str(TOOLS/"render_scope_of_work.py"),str(production),"--output",str(out/"render.html")])
        parity=json.loads((out/"parity.json").read_text()); assert parity["pass"] and not parity["issues"]
        maps=len(parity["checks"]); lines=sum(x["line_end"]-x["line_start"]+1 for x in parity["checks"])
        expected=sum(len((live/n).read_bytes().splitlines()) for n in LEGACY); assert lines==expected
        maps_total+=maps; lines_total+=lines
        members.append([did,row["live_path"],row["status_sha256"],sha(evidence),sha(production),sha(report),maps,lines,expected,"PASS","PASS_UNCHANGED"])
        sow=f'{row["live_path"]}/ScopeOfWork.md'; forward.append([did,"ADD",sow,"ABSENT",sha(production)]); inverse.append([did,"DELETE",sow,sha(production),"ABSENT"])
        for n in LEGACY:
            p=f'{row["live_path"]}/{n}'; h=row[HASH[n]]
            forward.append([did,"DELETE",p,h,"ABSENT"]); inverse.append([did,"ADD",p,"ABSENT",h])
    assert (maps_total,lines_total,len(forward),len(inverse),len(sims))==(148,1292,25,25,5)
    tsv(HERE/"MEMBER_RESULTS.tsv",["deliverable_id","live_path","status_sha256","evidence_sha256","production_sha256","finalization_sha256","mappings","covered_lines","total_lines","author","verifier"],members)
    tsv(HERE/"REPLACEMENT_MANIFEST.tsv",["deliverable_id","action","path","before_sha256","after_sha256"],forward)
    tsv(HERE/"ROLLBACK_MANIFEST.tsv",["deliverable_id","action","path","before_sha256","after_sha256"],inverse)
    tsv(HERE/"SIMULATION.tsv",["deliverable_id","apply","target_validation","rollback"],sims)
    summary={"status":"PASS","members":5,"mappings":148,"source_lines":1292,"replacement_rows":25,"rollback_rows":25,"simulations_pass":5,"author_manifest_sha256":sha(av/"MANIFEST.tsv"),"verifier_manifest_sha256":sha(vv/"MANIFEST.tsv"),"project_writes":0,"candidate_writes_by_verifier":0}
    (HERE/"MANAGER_VALIDATION.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n")
    print(json.dumps(summary,indent=2,sort_keys=True))
if __name__=="__main__": main()
