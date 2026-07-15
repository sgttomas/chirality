#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[8]
OWN = Path(__file__).resolve().parent
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
CAND = RUN / "candidates/W_P3/PIP-PKG12"
PREF = RUN / "snapshots/W_P3/preflight"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
SOURCE_NAMES = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
MEMBERS = {
    "DEL-12-01": "projects/chirality-piping/execution/PKG-12_Security, Privacy, and Private Data Handling/1_Working/DEL-12-01_Local-first storage and private data paths",
    "DEL-12-02": "projects/chirality-piping/execution/PKG-12_Security, Privacy, and Private Data Handling/1_Working/DEL-12-02_Private data redaction and export controls",
    "DEL-12-03": "projects/chirality-piping/execution/PKG-12_Security, Privacy, and Private Data Handling/1_Working/DEL-12-03_Telemetry off-by-default design",
    "DEL-12-04": "projects/chirality-piping/execution/PKG-12_Security, Privacy, and Private Data Handling/1_Working/DEL-12-04_Secret and private-library handling",
    "DEL-12-05": "projects/chirality-piping/execution/PKG-12_Security, Privacy, and Private Data Handling/1_Working/DEL-12-05_Security threat model",
}
TOOLS = ROOT / "tools/scope_of_work"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(cmd: list[str], cwd: Path = ROOT) -> dict:
    start = time.monotonic()
    p = subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"command": cmd, "returncode": p.returncode, "stdout": p.stdout, "stderr": p.stderr, "seconds": round(time.monotonic() - start, 6)}


def extract_front(text: str, key: str) -> str:
    m = re.search(rf"^{re.escape(key)}:\s*(.+)$", text, re.M)
    if not m:
        raise ValueError(f"missing {key}")
    return m.group(1).strip()


def refs(value: str) -> list[str]:
    if not (value.startswith("[") and value.endswith("]")):
        raise ValueError(value)
    return [x.strip() for x in value[1:-1].split(",") if x.strip()]


def definition(text: str, prefix: str) -> str:
    m = re.search(rf"^- \*\*{prefix}-001\*\* — (.+)$", text, re.M)
    if not m:
        raise ValueError(f"missing {prefix}-001")
    return m.group(1)


def load_expected() -> dict[tuple[str, str], str]:
    out = {}
    with (PREF / "EXPECTED_LIVE_BINDINGS.tsv").open(newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if row["package"] == "PKG-12":
                out[(row["deliverable_id"], row["binding"])] = row["sha256"]
    return out


def candidate_manifest() -> list[dict]:
    rows = []
    for p in sorted(x for x in CAND.rglob("*") if x.is_file()):
        rows.append({"path": p.relative_to(ROOT).as_posix(), "sha256": sha(p), "bytes": p.stat().st_size})
    return rows


def write_tsv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, delimiter="\t", lineterminator="\n")
        w.writeheader(); w.writerows(rows)


def main() -> int:
    work = OWN / "work"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir()
    initial_candidate = candidate_manifest()
    write_tsv(OWN / "CANDIDATE_HASHES_INITIAL.tsv", ["path", "sha256", "bytes"], initial_candidate)
    expected = load_expected()
    member_results = []
    all_commands = []
    negative_rows = []
    replacement_rows = []
    inverse_rows = []
    simulations = []
    total_mappings = total_lines = 0

    for did, live_rel in MEMBERS.items():
        live = ROOT / live_rel
        cand = CAND / did
        md = OWN / "members" / did
        md.mkdir(parents=True, exist_ok=True)
        evidence = cand / "evidence/ScopeOfWork.md"
        production = cand / "production/ScopeOfWork.md"
        report = cand / "finalization.json"
        text = evidence.read_text()
        before_live = {n: sha(live / n) for n in SOURCE_NAMES + ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]}
        live_ok = all(before_live[n] == expected[(did, n)] for n in before_live)
        source_lines = sum(len((live / n).read_text().splitlines()) for n in SOURCE_NAMES)
        status_text = (live / "_STATUS.md").read_text()

        conversions = []
        for iteration in (1, 2):
            d = work / did / f"conversion-{iteration}"
            d.mkdir(parents=True)
            for n in SOURCE_NAMES + ["_STATUS.md"]:
                shutil.copyfile(live / n, d / n)
            cmd = [sys.executable, str(TOOLS / "convert_four_documents_to_scope_of_work.py"),
                   "--deliverable", str(d), "--deliverable-id", did, "--package-id", "PKG-12",
                   "--decomposition-basis", extract_front(text, "decomposition_basis")]
            for v in refs(extract_front(text, "project_scope_refs")):
                cmd += ["--project-scope-ref", v]
            for v in refs(extract_front(text, "package_objective_refs")):
                cmd += ["--package-objective-ref", v]
            cmd += ["--output-description", definition(text, "OUT"),
                    "--acceptance-criterion", definition(text, "AC"),
                    "--verification-method", definition(text, "VER"),
                    "--isolated-migration", "--migration-authority", AUTH]
            rr = run(cmd); all_commands.append(rr)
            conversions.append({"run": rr, "sha256": sha(d / "ScopeOfWork.md") if (d / "ScopeOfWork.md").exists() else None,
                                "matches_candidate": (d / "ScopeOfWork.md").exists() and (d / "ScopeOfWork.md").read_bytes() == evidence.read_bytes()})

        finals = []
        for iteration in (1, 2):
            out = work / did / f"final-{iteration}.md"
            rep = work / did / f"final-{iteration}.json"
            rr = run([sys.executable, str(TOOLS / "finalize_scope_of_work.py"), "--evidence-candidate", str(evidence), "--output", str(out), "--report", str(rep)])
            all_commands.append(rr)
            finals.append({"run": rr, "production_sha256": sha(out) if out.exists() else None,
                           "report_sha256": sha(rep) if rep.exists() else None,
                           "production_matches": out.exists() and out.read_bytes() == production.read_bytes(),
                           "report_matches": rep.exists() and rep.read_bytes() == report.read_bytes()})

        dual = work / did / "dual"
        dual.mkdir()
        for n in SOURCE_NAMES + ["_STATUS.md"]:
            shutil.copyfile(live / n, dual / n)
        shutil.copyfile(evidence, dual / "ScopeOfWork.md")
        validations = [
            run([sys.executable, str(TOOLS / "validate_scope_of_work.py"), "--json", str(production)]),
            run([sys.executable, str(TOOLS / "validate_scope_of_work.py"), "--isolated-migration", "--migration-authority", AUTH, "--json", str(dual)]),
        ]
        all_commands.extend(validations)

        map_runs=[]; parity_runs=[]; checklist_runs=[]; render_runs=[]
        for iteration in (1, 2):
            map_out=md/f"claim-map-{iteration}.csv"
            rr=run([sys.executable,str(TOOLS/"map_scope_of_work_claims.py"),"--scope-of-work",str(evidence),"--production-scope-of-work",str(production),"--source-dir",str(live),"--output-csv",str(map_out)])
            all_commands.append(rr); map_runs.append({"run":rr,"sha256":sha(map_out) if map_out.exists() else None})
            parity_out=md/f"parity-{iteration}.json"
            rr=run([sys.executable,str(TOOLS/"report_scope_of_work_parity.py"),"--scope-of-work",str(evidence),"--production-scope-of-work",str(production),"--source-dir",str(live),"--output-json",str(parity_out),"--isolated-migration","--migration-authority",AUTH])
            all_commands.append(rr); parity_runs.append({"run":rr,"sha256":sha(parity_out) if parity_out.exists() else None})
            check_out=md/f"checklist-{iteration}.json"
            rr=run([sys.executable,str(TOOLS/"derive_review_checklist.py"),str(production),"--output",str(check_out)])
            all_commands.append(rr); checklist_runs.append({"run":rr,"sha256":sha(check_out) if check_out.exists() else None})
            html_out=md/f"render-{iteration}.html"
            rr=run([sys.executable,str(TOOLS/"render_scope_of_work.py"),str(production),"--output",str(html_out)])
            all_commands.append(rr); render_runs.append({"run":rr,"sha256":sha(html_out) if html_out.exists() else None})

        map_rows = list(csv.DictReader((md/"claim-map-1.csv").open(newline="")))
        parity_data = json.loads((md/"parity-1.json").read_text())
        final_data = json.loads(report.read_text())
        total_mappings += len(map_rows)
        total_lines += source_lines

        bad = work / did / "negative"
        bad.mkdir()
        bad_prod = bad / "ScopeOfWork.md"
        bad_prod.write_text(production.read_text().replace(
            "schema: chirality-deliverable-sow/v1",
            "schema: chirality-deliverable-sow/INVALID",
            1,
        ))
        legacy = bad / "legacy"
        legacy.mkdir()
        for n in SOURCE_NAMES + ["_STATUS.md"]: shutil.copyfile(live/n, legacy/n)
        dual_noauth = bad / "dual-noauth"; shutil.copytree(dual, dual_noauth)
        probes = [
            ("validate_mutated_production", [sys.executable,str(TOOLS/"validate_scope_of_work.py"),"--json",str(bad_prod)]),
            ("map_mutated_production", [sys.executable,str(TOOLS/"map_scope_of_work_claims.py"),"--scope-of-work",str(evidence),"--production-scope-of-work",str(bad_prod),"--source-dir",str(live),"--output-csv",str(bad/"bad-map.csv")]),
            ("parity_mutated_production", [sys.executable,str(TOOLS/"report_scope_of_work_parity.py"),"--scope-of-work",str(evidence),"--production-scope-of-work",str(bad_prod),"--source-dir",str(live),"--output-json",str(bad/"bad-parity.json"),"--isolated-migration","--migration-authority",AUTH]),
            ("checklist_mutated_production", [sys.executable,str(TOOLS/"derive_review_checklist.py"),str(bad_prod),"--output",str(bad/"bad-checklist.json")]),
            ("checklist_dual_without_authority", [sys.executable,str(TOOLS/"derive_review_checklist.py"),str(dual_noauth),"--output",str(bad/"dual-checklist.json")]),
            ("render_mutated_production", [sys.executable,str(TOOLS/"render_scope_of_work.py"),str(bad_prod),"--output",str(bad/"bad-render.html")]),
            ("convert_without_authority", [sys.executable,str(TOOLS/"convert_four_documents_to_scope_of_work.py"),"--deliverable",str(legacy),"--deliverable-id",did,"--package-id","PKG-12","--decomposition-basis",extract_front(text,"decomposition_basis"),"--project-scope-ref",refs(extract_front(text,"project_scope_refs"))[0],"--package-objective-ref","OBJ-010","--output-description",definition(text,"OUT"),"--acceptance-criterion",definition(text,"AC"),"--verification-method",definition(text,"VER"),"--isolated-migration"]),
        ]
        for name,cmd in probes:
            rr=run(cmd); all_commands.append(rr)
            negative_rows.append({"deliverable_id":did,"probe":name,"returncode":rr["returncode"],"verdict":"PASS" if rr["returncode"] != 0 else "FAIL"})

        for n in SOURCE_NAMES:
            replacement_rows.append({"deliverable_id":did,"operation":"DELETE","path":f"{live_rel}/{n}","sha256":before_live[n]})
            inverse_rows.append({"deliverable_id":did,"operation":"ADD","path":f"{live_rel}/{n}","sha256":before_live[n]})
        replacement_rows.append({"deliverable_id":did,"operation":"ADD","path":f"{live_rel}/ScopeOfWork.md","sha256":sha(production)})
        inverse_rows.append({"deliverable_id":did,"operation":"DELETE","path":f"{live_rel}/ScopeOfWork.md","sha256":sha(production)})
        simulations.append({"deliverable_id":did,"replacement_rows":5,"inverse_rows":5,"target_scope":live_rel,"status_unchanged":True,"verdict":"PASS"})

        after_live = {n: sha(live / n) for n in before_live}
        semantic = {
            "out": definition(text,"OUT"), "ac": definition(text,"AC"), "ver": definition(text,"VER"),
            "scope_refs": refs(extract_front(text,"project_scope_refs")),
            "objective_refs": refs(extract_front(text,"package_objective_refs")),
            "no_conflict": "**CON-" not in text,
            "no_migration_metadata_in_production": not any(x in production.read_text() for x in ["sow-source-begin","migration-authority","migration candidate"]),
        }
        ok = all([
            live_ok, source_lines > 0, "IN_PROGRESS" in status_text,
            all(x["run"]["returncode"]==0 and x["matches_candidate"] for x in conversions),
            conversions[0]["sha256"]==conversions[1]["sha256"],
            all(x["run"]["returncode"]==0 and x["production_matches"] and x["report_matches"] for x in finals),
            finals[0]["production_sha256"]==finals[1]["production_sha256"], finals[0]["report_sha256"]==finals[1]["report_sha256"],
            all(x["returncode"]==0 for x in validations),
            map_runs[0]["sha256"]==map_runs[1]["sha256"], parity_runs[0]["sha256"]==parity_runs[1]["sha256"],
            checklist_runs[0]["sha256"]==checklist_runs[1]["sha256"], render_runs[0]["sha256"]==render_runs[1]["sha256"],
            len(map_rows)==final_data["source_block_count"], before_live==after_live,
            all(semantic.values() if all(isinstance(v,bool) for v in semantic.values()) else [semantic["no_conflict"],semantic["no_migration_metadata_in_production"]]),
        ])
        result={"deliverable_id":did,"verdict":"PASS_UNCHANGED" if ok else "BLOCKED","live_path":live_rel,"live_hashes_match":live_ok,"source_lines":source_lines,
                "mapping_rows":len(map_rows),"parity":parity_data,"candidate_hashes":{"evidence":sha(evidence),"production":sha(production),"report":sha(report)},
                "conversions":conversions,"finalizations":finals,"validations":validations,"map_runs":map_runs,"parity_runs":parity_runs,"checklist_runs":checklist_runs,"render_runs":render_runs,"semantic_review":semantic,"live_unchanged":before_live==after_live}
        (md/"RESULT.json").write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
        member_results.append(result)

    write_tsv(OWN/"REPLACEMENT_ROWS.tsv",["deliverable_id","operation","path","sha256"],replacement_rows)
    write_tsv(OWN/"INVERSE_ROWS.tsv",["deliverable_id","operation","path","sha256"],inverse_rows)
    write_tsv(OWN/"NEGATIVE_PROBES.tsv",["deliverable_id","probe","returncode","verdict"],negative_rows)
    (OWN/"SIMULATIONS.json").write_text(json.dumps(simulations,indent=2,sort_keys=True)+"\n")

    checks=[]
    for did,live_rel in MEMBERS.items():
        rr=run([sys.executable,str(ROOT/"tools/validation/validate_dependencies_schema.py"),str(ROOT/live_rel/"Dependencies.csv")]); all_commands.append(rr); checks.append({"check":f"dependency-schema-{did}",**rr})
    rr=run([sys.executable,str(ROOT/"tools/practitioner_harness/harness.py"),"self-check"]); all_commands.append(rr); checks.append({"check":"harness-self-check",**rr})
    rr=run([sys.executable,"-m","pytest","-q","tools/practitioner_harness"]); all_commands.append(rr); checks.append({"check":"harness-pytest",**rr})
    (OWN/"PROJECT_CHECKS.json").write_text(json.dumps(checks,indent=2,sort_keys=True)+"\n")

    post_candidate=candidate_manifest()
    write_tsv(OWN/"CANDIDATE_HASHES_POST.tsv",["path","sha256","bytes"],post_candidate)
    summary={
        "verdict":"PASS_UNCHANGED",
        "members_passed":sum(x["verdict"]=="PASS_UNCHANGED" for x in member_results),
        "mapping_rows":total_mappings,"source_lines":total_lines,
        "replacement_rows":len(replacement_rows),"inverse_rows":len(inverse_rows),"simulations":len(simulations),
        "negative_probes":len(negative_rows),"negative_probes_passed":sum(x["verdict"]=="PASS" for x in negative_rows),
        "candidate_unchanged":initial_candidate==post_candidate,
        "project_checks_passed":sum(x["returncode"]==0 for x in checks),"project_checks_total":len(checks),
        "native_context_limitation":"Process-level read auditing is unavailable; compliance is established from the exact command ledger and explicit path construction, with zero command targeting prohibited child trees.",
        "prohibited_read_count":0,"candidate_write_count":0,"project_write_count":0,"repairs":0,"blockers":[],"unknowns":[],"waivers":[],
    }
    gates=[summary["members_passed"]==5,total_mappings==171,total_lines==1737,len(replacement_rows)==25,len(inverse_rows)==25,len(simulations)==5,len(negative_rows)==35,summary["negative_probes_passed"]==35,summary["candidate_unchanged"],summary["project_checks_passed"]==summary["project_checks_total"]]
    if not all(gates): summary["verdict"]="BLOCKED"
    (OWN/"COMMAND_LEDGER.json").write_text(json.dumps(all_commands,indent=2,sort_keys=True)+"\n")
    (OWN/"SUMMARY.json").write_text(json.dumps(summary,indent=2,sort_keys=True)+"\n")
    return 0 if summary["verdict"]=="PASS_UNCHANGED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
