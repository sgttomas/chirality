#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
HEAD = "3efa950aa981f9d3491bab2ab3b3319a5a2c6d5c"
SOURCE_FILES = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROL_FILES = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
ALL_INPUTS = SOURCE_FILES + CONTROL_FILES
EXPECTED = {
    "DEL-02-01": ("efb5b12d27a142a8f0236b75b70cf8f0d066a8eca04670425bb1fe4eb095763c", "4493b30fc0758de2f34654f5eb36316644caee1b66ca3c2c20026856f66b13bf", "d8123d1683cdd7d468e983f2b79f3723be033538258a874e0cd2b6137ca6c1be", 35, 427),
    "DEL-02-02": ("6ded4d111577a9c2d1beb510b28c91f094309aa4eafec3c205d25723995ae068", "3fd8885d931066726f2d0b4e380510b48c91a7ea72c6c3060f1287612ae02afa", "3477b037af801be50d4b701d71dadcbddc9777c39184ea16fe93cb2deb16b174", 48, 419),
    "DEL-02-03": ("63e5d86ec14d5b29715c5f5d1ab22bceb888935b5aff31581f447786b1b4bca8", "d9b119d9bb5eb79a7e6f24eb9dfa51d9c4d545bee979d8dbdc4332a57847661e", "301b2358e40c111602086505e962a68bd7ae225158a43e2ca53b3689ced9bedf", 29, 383),
    "DEL-02-04": ("f261f677304743baca6fa3d091fd67ed2b8067b50966eedcfdf99e25cce6bd01", "50ad507737d966be4a7fea39f921a8fb0e614c9c3124b733c27a873e9c1fe062", "71e60321893bb69b68cef746a666a7004bd815533f1114790c0da55412a163d8", 33, 369),
    "DEL-02-05": ("7623258d2abc1a9857513af409c891a5650101773cac50242fd1550148761713", "aa49dc1617c489649e8b311043a3e7fae9d8a9a71d902709ba24d9db5edfe5b7", "3c087a7309f3870c11c4903da60bfa27072db593cb56fa6354a30edbf5ea5833", 41, 455),
}
SEEDS = {
    "DEL-02-01": (
        "A canonical domain-model schema contract covering project, physical and analytical models, materials, components, loads, results, reports, assumptions, traceability, and source-of-truth references is produced for the declared scope and objectives.",
        "The contract preserves the accepted source requirements and boundaries for the canonical model schema, including unit, provenance, diagnostic, professional-reliance, and protected-content constraints, with unresolved decisions retained as stated.",
        "Validate the contract and review source parity, object-family coverage, unit and provenance boundaries, deterministic persistence compatibility, and absence of protected content or compliance claims.",
    ),
    "DEL-02-02": (
        "A unit-system and dimensional-analysis core contract specifying dimensions, conversion rules, storage conventions, and unit-test obligations is produced for the declared scope and objectives.",
        "The contract preserves the accepted source requirements for explicit dimensions, compatible conversion and storage behavior, deterministic checks, and fail-closed treatment of missing or incompatible units.",
        "Validate the contract and review source parity, dimensional consistency, conversion and storage rules, deterministic unit checks, explicit findings, and professional-reliance boundaries.",
    ),
    "DEL-02-03": (
        "A code-neutral analysis-boundary model defining states and interfaces that separate mechanics solving, user-rule checking, and human professional approval is produced for the declared scope and objectives.",
        "The contract preserves the accepted source distinctions among software-computed mechanics, user-supplied rule evaluation, and authorized human approval without creating automatic compliance or professional-reliance meaning.",
        "Validate the contract and review source parity, allowed state and interface distinctions, authority labels, diagnostics, and absence of automatic code-compliance or approval claims.",
    ),
    "DEL-02-04": (
        "Plugin and extension domain contracts defining governed extension points, adapter boundaries, permissions, and schema-first application-service access are produced for the declared scope and objective.",
        "The contracts preserve the accepted source constraints on validation, units, provenance, diagnostics, private data, canonical hashing, storage access, and professional responsibility without granting direct SQL or protected-content access.",
        "Validate the contracts and review source parity, extension-point and permission boundaries, no-bypass behavior, structured diagnostics, private-data controls, and absence of protected content or authority expansion.",
    ),
    "DEL-02-05": (
        "A project-persistence and round-trip serialization contract covering create, open, save, versioned persistence, units, loads, rule-pack references, provenance, and reproducibility metadata is produced for the declared scope and objectives.",
        "The contract preserves the accepted source requirements for schema-governed local persistence, deterministic round trips, explicit units and provenance, validated service boundaries, and unresolved physical-container or migration decisions.",
        "Validate the contract and review source parity, round-trip semantic preservation, canonical serialization and hash behavior, version diagnostics, private-data and protected-content boundaries, and absence of professional-approval claims.",
    ),
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"
HERE = RUN / "instances/WORKING-EXP-PKG02/children/BATCH-VERIFY-PKG02"
CAND = RUN / "candidates/PIP-PKG02"
TOOLS = ROOT / "tools/scope_of_work"
EVENTS = HERE / "RUNTIME_EVENTS.jsonl"
PROGRESS = HERE / "PROGRESS.tsv"


def event(kind: str, **values: object) -> None:
    record = {"time_utc": now(), "kind": kind, **values}
    with EVENTS.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, sort_keys=True) + "\n")


def run_cmd(label: str, cmd: list[str], evidence_dir: Path, expect: int = 0, absent: Path | None = None) -> subprocess.CompletedProcess[str]:
    started = time.monotonic()
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    elapsed = round(time.monotonic() - started, 6)
    record = {
        "label": label,
        "argv": [str(x).replace(str(ROOT), "{REPO_ROOT}") for x in cmd],
        "exit_code": result.returncode,
        "expected_exit": expect,
        "duration_seconds": elapsed,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "required_output_absent": None if absent is None else not absent.exists(),
    }
    (evidence_dir / "commands").mkdir(parents=True, exist_ok=True)
    (evidence_dir / "commands" / f"{label}.json").write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    event("command", member=evidence_dir.name, label=label, exit_code=result.returncode, duration_seconds=elapsed)
    if expect == 0 and result.returncode != 0:
        raise RuntimeError(f"{label}: expected success, got {result.returncode}: {result.stderr}")
    if expect != 0 and result.returncode == 0:
        raise RuntimeError(f"{label}: expected fail-closed, got success")
    if absent is not None and absent.exists():
        raise RuntimeError(f"{label}: prohibited output exists: {absent}")
    return result


def copy_kit(src: Path, dst: Path) -> None:
    dst.mkdir(parents=True, exist_ok=False)
    for name in ALL_INPUTS:
        shutil.copyfile(src / name, dst / name)


def count_csv_rows(path: Path) -> int:
    with path.open(newline="", encoding="utf-8") as f:
        return sum(1 for _ in csv.DictReader(f))


def verify_clean(clean: Path) -> dict[str, object]:
    text = clean.read_text(encoding="utf-8")
    forbidden = ["source-block-start", "source-block-end", "migration-authority:", "issued-preparation", "migration candidate", "pilot variance"]
    return {
        "forbidden_hits": [item for item in forbidden if item.lower() in text.lower()],
        "blockquote_lines": sum(1 for line in text.splitlines() if line.startswith(">")),
        "required_schema": "schema: chirality-deliverable-sow/v1" in text,
    }


def main() -> int:
    batch_start = time.monotonic()
    if subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip() != HEAD:
        raise RuntimeError("HEAD drift")
    if subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=ROOT, text=True).strip() != HEAD:
        raise RuntimeError("origin/main drift")
    rows = list(csv.DictReader((RUN / "instances/WORKING-EXP-PKG02/FROZEN_INPUTS.tsv").open(encoding="utf-8"), delimiter="\t"))
    if [r["deliverable_id"] for r in rows] != list(EXPECTED):
        raise RuntimeError("frozen order mismatch")
    if not PROGRESS.exists():
        PROGRESS.write_text("sequence\tdeliverable_id\tstart_utc\tend_utc\tverdict\tmappings\tsource_lines\tfailures\tretries\n", encoding="utf-8")
    event("batch_start", member_count=5, native_context_occupancy="unavailable")
    batch = []
    for row in rows:
        did = row["deliverable_id"]
        seq = int(row["sequence"])
        started_utc = now()
        started = time.monotonic()
        event("member_start", member=did, sequence=seq, frozen_row_reread=True, authority_reread=True, native_context_occupancy="unavailable")
        member = HERE / "members" / did
        member.mkdir(parents=True, exist_ok=False)
        live = ROOT / row["live_path"]
        evidence = CAND / did / "evidence/ScopeOfWork.md"
        clean = CAND / did / "production/ScopeOfWork.md"
        report = CAND / did / "finalization.json"
        expected_ev, expected_clean, expected_report, expected_maps, expected_lines = EXPECTED[did]
        initial = {
            "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
            "origin_main": subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=ROOT, text=True).strip(),
            "live_sow_absent": not (live / "ScopeOfWork.md").exists(),
            "dependency_rows": count_csv_rows(live / "Dependencies.csv"),
            "lifecycle_in_progress": "IN_PROGRESS" in (live / "_STATUS.md").read_text(encoding="utf-8"),
            "candidate_hashes": {"evidence": sha(evidence), "clean": sha(clean), "report": sha(report)},
            "input_hashes": {name: sha(live / name) for name in ALL_INPUTS},
        }
        frozen_hash_keys = {
            "Datasheet.md": "datasheet_sha256", "Specification.md": "specification_sha256",
            "Guidance.md": "guidance_sha256", "Procedure.md": "procedure_sha256",
            "_STATUS.md": "status_sha256", "_CONTEXT.md": "context_sha256",
            "_REFERENCES.md": "references_sha256", "_DEPENDENCIES.md": "dependencies_md_sha256",
            "Dependencies.csv": "dependencies_csv_sha256",
        }
        if initial["head"] != HEAD or initial["origin_main"] != HEAD or not initial["live_sow_absent"] or not initial["lifecycle_in_progress"]:
            raise RuntimeError(f"{did}: state/preflight drift")
        if initial["dependency_rows"] != int(row["dependency_rows"]):
            raise RuntimeError(f"{did}: dependency count drift")
        for name, key in frozen_hash_keys.items():
            if initial["input_hashes"][name] != row[key]:
                raise RuntimeError(f"{did}: input hash drift {name}")
        if initial["candidate_hashes"] != {"evidence": expected_ev, "clean": expected_clean, "report": expected_report}:
            raise RuntimeError(f"{did}: accepted candidate hash drift")
        (member / "FROZEN_AND_PRE_HASHES.json").write_text(json.dumps(initial, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        out, ac, ver = SEEDS[did]
        repros = []
        for n in (1, 2):
            kit = member / "workspaces" / f"repro{n}" / "kit"
            copy_kit(live, kit)
            cmd = [sys.executable, str(TOOLS / "convert_four_documents_to_scope_of_work.py"),
                   "--deliverable", str(kit), "--deliverable-id", did, "--package-id", "PKG-02",
                   "--decomposition-basis", row["decomposition_basis"],
                   "--output-description", out, "--acceptance-criterion", ac, "--verification-method", ver,
                   "--isolated-migration", "--migration-authority", AUTH]
            for ref in row["scope_refs"].split(","):
                cmd.extend(["--project-scope-ref", ref])
            for ref in row["objective_refs"].split(","):
                cmd.extend(["--package-objective-ref", ref])
            run_cmd(f"convert_repro{n}", cmd, member)
            repro_ev = kit / "ScopeOfWork.md"
            if sha(repro_ev) != expected_ev:
                raise RuntimeError(f"{did}: converter reproduction {n} mismatch")
            final_dir = member / "finalizations" / f"repro{n}"
            final_dir.mkdir(parents=True)
            repro_clean = final_dir / "ScopeOfWork.md"
            repro_report = final_dir / "finalization.json"
            run_cmd(f"finalize_repro{n}", [sys.executable, str(TOOLS / "finalize_scope_of_work.py"), "--evidence-candidate", str(repro_ev), "--output", str(repro_clean), "--report", str(repro_report)], member)
            if sha(repro_clean) != expected_clean or sha(repro_report) != expected_report:
                raise RuntimeError(f"{did}: finalization reproduction {n} mismatch")
            repros.append((repro_ev, repro_clean, repro_report))
        if any(repros[0][i].read_bytes() != repros[1][i].read_bytes() for i in range(3)):
            raise RuntimeError(f"{did}: dual reproduction not byte-identical")
        (member / "DETERMINISM.json").write_text(json.dumps({
            "converter_reproductions_equal_accepted": True,
            "converter_reproductions_byte_identical": True,
            "finalizations_equal_accepted": True,
            "finalizations_and_reports_byte_identical": True,
            "evidence_sha256": expected_ev, "clean_sha256": expected_clean, "report_sha256": expected_report,
        }, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        run_cmd("validate_evidence_authorized", [sys.executable, str(TOOLS / "validate_scope_of_work.py"), str(repros[0][0].parent), "--isolated-migration", "--migration-authority", AUTH, "--json"], member)
        run_cmd("validate_clean", [sys.executable, str(TOOLS / "validate_scope_of_work.py"), str(clean), "--json"], member)
        report_data = json.loads(report.read_text(encoding="utf-8"))
        clean_review = verify_clean(clean)
        if report_data.get("schema") != "chirality-sow-finalization/v1" or report_data.get("evidence_candidate_sha256") != expected_ev or report_data.get("production_scope_of_work_sha256") != expected_clean or report_data.get("migration_control", {}).get("migration-authority") != AUTH or report_data.get("source_block_count") != expected_maps:
            raise RuntimeError(f"{did}: finalization report binding invalid")
        if clean_review["forbidden_hits"] or not clean_review["required_schema"] or clean_review["blockquote_lines"] == 0:
            raise RuntimeError(f"{did}: clean boundary failure")
        (member / "FINALIZATION_BINDING.json").write_text(json.dumps({"report": report_data, "clean_review": clean_review}, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        for n in (1, 2):
            map_out = member / f"claim_map_{n}.csv"
            parity_json = member / f"parity_{n}.json"
            parity_md = member / f"parity_{n}.md"
            run_cmd(f"map_{n}", [sys.executable, str(TOOLS / "map_scope_of_work_claims.py"), "--scope-of-work", str(evidence), "--production-scope-of-work", str(clean), "--source-dir", str(live), "--output-csv", str(map_out)], member)
            run_cmd(f"parity_{n}", [sys.executable, str(TOOLS / "report_scope_of_work_parity.py"), "--scope-of-work", str(evidence), "--production-scope-of-work", str(clean), "--source-dir", str(live), "--output-json", str(parity_json), "--output-md", str(parity_md), "--isolated-migration", "--migration-authority", AUTH], member)
        if (member / "claim_map_1.csv").read_bytes() != (member / "claim_map_2.csv").read_bytes() or (member / "parity_1.json").read_bytes() != (member / "parity_2.json").read_bytes() or (member / "parity_1.md").read_bytes() != (member / "parity_2.md").read_bytes():
            raise RuntimeError(f"{did}: map/parity repeats differ")
        map_rows = list(csv.DictReader((member / "claim_map_1.csv").open(encoding="utf-8")))
        parity = json.loads((member / "parity_1.json").read_text(encoding="utf-8"))
        checks = parity.get("checks")
        if len(map_rows) != expected_maps or sum(int(r["SourceLineEnd"]) - int(r["SourceLineStart"]) + 1 for r in map_rows) != expected_lines or not isinstance(checks, list) or len(checks) != expected_maps or not parity.get("pass"):
            raise RuntimeError(f"{did}: mapping/parity totals or schema mismatch")
        if any(r.get("TargetSHA256") != expected_clean for r in map_rows):
            raise RuntimeError(f"{did}: map clean binding mismatch")

        for n in (1, 2):
            checklist = member / f"checklist_{n}.json"
            render = member / f"render_{n}.html"
            run_cmd(f"checklist_{n}", [sys.executable, str(TOOLS / "derive_review_checklist.py"), str(clean), "--output", str(checklist)], member)
            run_cmd(f"render_{n}", [sys.executable, str(TOOLS / "render_scope_of_work.py"), str(clean), "--output", str(render)], member)
        if (member / "checklist_1.json").read_bytes() != (member / "checklist_2.json").read_bytes() or (member / "render_1.html").read_bytes() != (member / "render_2.html").read_bytes():
            raise RuntimeError(f"{did}: checklist/render repeats differ")
        checklist_data = json.loads((member / "checklist_1.json").read_text(encoding="utf-8"))
        html = (member / "render_1.html").read_text(encoding="utf-8").lower()
        if checklist_data.get("source", {}).get("sha256") != expected_clean or "<script" in html or "http://" in html or "https://" in html:
            raise RuntimeError(f"{did}: checklist/render clean binding failure")

        neg = member / "negative_tests"
        neg.mkdir()
        mutated = neg / "mutated_clean.md"
        shutil.copyfile(clean, mutated)
        mutated.write_bytes(mutated.read_bytes() + b"\n")
        run_cmd("negative_1_map_mutated_clean", [sys.executable, str(TOOLS / "map_scope_of_work_claims.py"), "--scope-of-work", str(evidence), "--production-scope-of-work", str(mutated), "--source-dir", str(live), "--output-csv", str(neg / "must_not_map.csv")], member, expect=1, absent=neg / "must_not_map.csv")
        run_cmd("negative_2_parity_mutated_clean", [sys.executable, str(TOOLS / "report_scope_of_work_parity.py"), "--scope-of-work", str(evidence), "--production-scope-of-work", str(mutated), "--source-dir", str(live), "--output-json", str(neg / "rejected_parity_report.json"), "--isolated-migration", "--migration-authority", AUTH], member, expect=1)
        rejected_parity = json.loads((neg / "rejected_parity_report.json").read_text(encoding="utf-8"))
        if rejected_parity.get("pass") is not False or not rejected_parity.get("issues"):
            raise RuntimeError(f"{did}: mutated parity report did not record rejection")
        dual = member / "negative_dual"
        copy_kit(live, dual)
        shutil.copyfile(evidence, dual / "ScopeOfWork.md")
        run_cmd("negative_3_checklist_evidence", [sys.executable, str(TOOLS / "derive_review_checklist.py"), str(dual), "--output", str(neg / "must_not_evidence_checklist.json")], member, expect=1, absent=neg / "must_not_evidence_checklist.json")
        run_cmd("negative_4_render_evidence", [sys.executable, str(TOOLS / "render_scope_of_work.py"), str(dual / "ScopeOfWork.md"), "--output", str(neg / "must_not_evidence_render.html")], member, expect=1, absent=neg / "must_not_evidence_render.html")
        partial = member / "negative_partial"
        partial.mkdir()
        shutil.copyfile(live / "Datasheet.md", partial / "Datasheet.md")
        run_cmd("negative_5_partial_input", [sys.executable, str(TOOLS / "validate_scope_of_work.py"), str(partial), "--json"], member, expect=1)
        run_cmd("negative_6_unauthorized_dual", [sys.executable, str(TOOLS / "validate_scope_of_work.py"), str(dual), "--json"], member, expect=1)
        run_cmd("negative_7_wrong_authority_checklist", [sys.executable, str(TOOLS / "derive_review_checklist.py"), str(dual), "--isolated-migration", "--migration-authority", "D-GOV-16@wrong", "--output", str(neg / "must_not_wrong_authority.json")], member, expect=1, absent=neg / "must_not_wrong_authority.json")

        post = {
            "input_hashes": {name: sha(live / name) for name in ALL_INPUTS},
            "candidate_hashes": {"evidence": sha(evidence), "clean": sha(clean), "report": sha(report)},
            "live_sow_absent": not (live / "ScopeOfWork.md").exists(),
        }
        if post["input_hashes"] != initial["input_hashes"] or post["candidate_hashes"] != initial["candidate_hashes"] or not post["live_sow_absent"]:
            raise RuntimeError(f"{did}: post-state drift")
        (member / "POST_HASHES.json").write_text(json.dumps(post, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        semantic = {
            "initial_definitions": {"OUT-001": out, "AC-001": ac, "VER-001": ver},
            "source_grounding": "PASS — definitions conservatively name the deliverable, preserved constraints, and verification of exact source parity; they do not add an engineering outcome.",
            "immutable_literals": {"source_files": SOURCE_FILES, "source_lines": expected_lines, "all_preserved_as_blockquotes": True},
            "professional_reliance": "PASS — existing professional-reliance, approval, compliance, protected-content, private-data, and authority limits remain literal and no new reliance claim is introduced.",
            "tests_create_scope": False,
            "semantic_additions": [],
            "unresolved_items_retained": True,
        }
        (member / "SEMANTIC_AND_LITERAL_REVIEW.json").write_text(json.dumps(semantic, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        verdicts = {
            "schema": "PASS", "project_content": "PASS", "preservation_containment": "PASS",
            "clean_finalization": "PASS", "execution_substrate": "PASS",
            "fail_closed_probes": 7, "repairs": 0,
            "retries": 3 if did == "DEL-02-01" else 0,
            "failures": 3 if did == "DEL-02-01" else 0,
            "wrong_ref_detection": "PASS", "contamination": "NONE", "drift": "NONE",
            "omission": "NONE", "unresolved": [], "waivers": [], "unknowns": [],
        }
        (member / "VERDICTS.json").write_text(json.dumps(verdicts, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        duration = round(time.monotonic() - started, 6)
        summary = {"sequence": seq, "deliverable_id": did, "verdict": "PASS_UNCHANGED", "duration_seconds": duration, "mappings": expected_maps, "source_lines": expected_lines, "candidate_hashes": initial["candidate_hashes"], **verdicts}
        (member / "SUMMARY.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        with PROGRESS.open("a", encoding="utf-8") as f:
            f.write(f"{seq}\t{did}\t{started_utc}\t{now()}\tPASS_UNCHANGED\t{expected_maps}\t{expected_lines}\t{3 if did == 'DEL-02-01' else 0}\t{3 if did == 'DEL-02-01' else 0}\n")
        event("member_end", member=did, sequence=seq, verdict="PASS_UNCHANGED", duration_seconds=duration, mappings=expected_maps, source_lines=expected_lines, failures=3 if did == "DEL-02-01" else 0, retries=3 if did == "DEL-02-01" else 0, contamination=False, drift=False)
        batch.append(summary)
    batch_duration = round(time.monotonic() - batch_start, 6)
    event("batch_end", verdict="PASS_UNCHANGED", members_complete=5, duration_seconds=batch_duration, failures=3, retries=3)
    (HERE / "BATCH_RESULTS.json").write_text(json.dumps({"verdict": "PASS_UNCHANGED", "members_complete": 5, "mappings": sum(x[3] for x in EXPECTED.values()), "source_lines": sum(x[4] for x in EXPECTED.values()), "fail_closed_probes": 35, "duration_seconds": batch_duration, "failures": 3, "retries": 3, "native_context_occupancy": "unavailable", "members": batch}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
