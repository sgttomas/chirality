#!/usr/bin/env python3
"""Independently reproduce the governed W-A3 preintegration fan-in."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[8]
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
OUT = RUN / "snapshots/W_A3/preintegration"
DETAIL = OUT / "detailed"
SCRATCH = OUT / "_scratch"
PREFLIGHT = RUN / "snapshots/W_A3/preflight/A3_MANIFEST.tsv"
GRAPH = RUN / "WORK_GRAPH.json"
LEGACY = ("Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md")
CONTROL = ("_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv")
PACKAGES = {
    "08": {"members": 5, "mappings": 155, "lines": 1585, "package": 70, "child": 441},
    "09": {"members": 6, "mappings": 169, "lines": 1781, "package": 82, "child": 490},
    "10": {"members": 5, "mappings": 157, "lines": 1619, "package": 68, "child": 539},
}
EXPECTED_PACKAGE_MANIFESTS = {
    "08": "3618a5d7e8a4568ad9a3fe3b6203e6f4aa096a688a1c080b064da485fd77b03e",
    "09": "5687bd926e3d5585cb5795195e23bc044eb3fbf64c34df274c2f9d9ab4f8651a",
    "10": "beadc400552741e462c3b32329a2d2653a82e38b1b9b7f0b1359f8450bc0d211",
}
ROOT_LITERAL = b"/Users/ryan/ai-env/projects/chirality"
TEMP_LITERALS = (b"/private/var/folders/", b"/var/folders/")
MIGRATION_AUTHORITY = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"


def fail(message: str) -> None:
    raise RuntimeError(message)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tree_digest(path: Path) -> dict[str, str]:
    return {
        p.relative_to(path).as_posix(): digest(p)
        for p in sorted(path.rglob("*"))
        if p.is_file()
    }


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], data: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


def run(*args: str, cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True)


def resolve_binding(raw: str, child_dir: Path | None = None, package_dir: Path | None = None) -> Path:
    if raw.startswith("/") or ".." in Path(raw).parts:
        fail(f"nonportable manifest path: {raw}")
    if raw.startswith(("execution/", "projects/", "domains/", "agents/", "docs/", "tools/", "skills/")):
        return ROOT / raw
    if child_dir is not None:
        return child_dir / raw
    if package_dir is not None:
        return package_dir / raw
    fail(f"cannot resolve manifest binding: {raw}")


def json_result(path: Path) -> tuple[str, list[dict[str, object]]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    result_rows = data.get("results") or data.get("checks") or []
    return str(data.get("status")), result_rows


def main() -> int:
    DETAIL.mkdir(parents=True, exist_ok=True)
    if SCRATCH.exists():
        shutil.rmtree(SCRATCH)
    SCRATCH.mkdir()

    head = run("git", "rev-parse", "HEAD").stdout.strip()
    origin = run("git", "rev-parse", "origin/main").stdout.strip()
    expected_head = "193663b1d93299c18d64f59b543b36a0dd5f0ee1"
    if head != expected_head or origin != expected_head:
        fail(f"main identity drift: {head}/{origin}")

    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    if graph.get("version") != 27:
        fail(f"expected graph v27, got {graph.get('version')}")
    graph_nodes = {node["id"]: node for node in graph["nodes"]}
    for node in ("W-A3-PKG08", "W-A3-PKG09", "W-A3-PKG10"):
        if graph_nodes.get(node, {}).get("status") != "PASS":
            fail(f"nonterminal graph predecessor: {node}")
    if graph_nodes.get("W-A3-F", {}).get("status") != "RELEASED":
        fail("W-A3-F is not RELEASED")

    members = rows(PREFLIGHT)
    if len(members) != 16:
        fail(f"expected 16 preflight members, got {len(members)}")
    by_id = {row["deliverable_id"]: row for row in members}
    if len(by_id) != 16:
        fail("preflight deliverable identity collision")

    package_bindings: list[dict[str, object]] = []
    child_bindings: list[dict[str, object]] = []
    app_checks: list[dict[str, object]] = []
    portability_hits: list[dict[str, object]] = []
    recovery_rows: list[dict[str, object]] = []
    package_results: dict[str, dict[str, dict[str, str]]] = {}
    replacements: list[dict[str, str]] = []
    rollbacks: list[dict[str, str]] = []
    accepted_child_count = 0

    for package, expected in PACKAGES.items():
        package_dir = RUN / f"instances/WORKING-A3-PKG{package}"
        status = json.loads((package_dir / "STATUS.json").read_text(encoding="utf-8"))
        if status.get("status") != "PASS" or status.get("terminal") is not True:
            fail(f"package {package} is nonterminal")
        for key in ("blockers", "waivers", "rerun_requirements"):
            if status.get(key):
                fail(f"package {package} has {key}")

        manifest_path = package_dir / "MANIFEST.tsv"
        if digest(manifest_path) != EXPECTED_PACKAGE_MANIFESTS[package]:
            fail(f"package {package} manifest digest mismatch")
        manifest_rows = rows(manifest_path)
        if len(manifest_rows) != expected["package"]:
            fail(f"package {package} manifest cardinality mismatch")
        for ordinal, row in enumerate(manifest_rows, 1):
            bound = resolve_binding(row["path"], package_dir=package_dir)
            if not bound.is_file() or digest(bound) != row["sha256"]:
                fail(f"package {package} bad binding: {row['path']}")
            package_bindings.append({
                "package": f"APP-PKG-{package}", "ordinal": ordinal,
                "kind": row["kind"], "path": row["path"], "sha256": row["sha256"],
                "bytes": bound.stat().st_size, "verdict": "PASS",
            })

        member_rows = rows(package_dir / "MEMBER_RESULTS.tsv")
        if len(member_rows) != expected["members"]:
            fail(f"package {package} member result mismatch")
        package_results[package] = {row["deliverable_id"]: row for row in member_rows}
        if sum(int(row["mapping_rows"]) for row in member_rows) != expected["mappings"]:
            fail(f"package {package} mapping summary mismatch")
        if sum(int(row["source_lines"]) for row in member_rows) != expected["lines"]:
            fail(f"package {package} source-line summary mismatch")

        child_index = rows(package_dir / "CHILD_INDEX.tsv")
        accepted = [row for row in child_index if "predecessor" not in row["role"]]
        if len(accepted) != expected["members"] * 2:
            fail(f"package {package} accepted child count mismatch")
        accepted_child_count += len(accepted)
        package_child_rows = 0
        for child in accepted:
            child_dir = package_dir / "children" / child["child"]
            child_manifest = child_dir / "MANIFEST.tsv"
            if not child_manifest.is_file() or digest(child_manifest) != child["manifest_sha256"]:
                fail(f"child manifest identity mismatch: {child['child']}")
            manifest_data = rows(child_manifest)
            if len(manifest_data) != int(child["manifest_rows"]) or child["bad_bindings"] != "0":
                fail(f"child manifest summary mismatch: {child['child']}")
            child_status = json.loads((child_dir / "STATUS.json").read_text(encoding="utf-8"))
            if child_status.get("terminal") is not True:
                fail(f"child nonterminal: {child['child']}")
            if child_status.get("verdict") not in (None, "PASS"):
                fail(f"child failed verdict: {child['child']}")
            if child_status.get("run_status") not in (None, "SUCCESS"):
                fail(f"child failed run status: {child['child']}")
            if child_status.get("blockers") or child_status.get("waivers") or child_status.get("rerun_requirements"):
                fail(f"accepted child has residuals: {child['child']}")
            for ordinal, binding in enumerate(manifest_data, 1):
                bound = resolve_binding(binding["path"], child_dir=child_dir)
                if not bound.is_file() or digest(bound) != binding["sha256"]:
                    fail(f"child bad binding: {child['child']}/{binding['path']}")
                if binding.get("bytes") and bound.stat().st_size != int(binding["bytes"]):
                    fail(f"child byte mismatch: {child['child']}/{binding['path']}")
                child_bindings.append({
                    "package": f"APP-PKG-{package}", "child": child["child"],
                    "role": child["role"], "ordinal": ordinal, "path": binding["path"],
                    "sha256": binding["sha256"], "bytes": bound.stat().st_size, "verdict": "PASS",
                })
            package_child_rows += len(manifest_data)
        if package_child_rows != expected["child"]:
            fail(f"package {package} child binding mismatch: {package_child_rows}")

        replacement_rows = rows(package_dir / "REPLACEMENT_MANIFEST.tsv")
        rollback_rows = rows(package_dir / "ROLLBACK_MANIFEST.tsv")
        for row in replacement_rows:
            replacements.append({
                "deliverable_id": row["deliverable_id"], "action": row["action"],
                "path": row.get("path") or row.get("target_path") or "",
                "source_path": row.get("source_path") or "-", "sha256": row["sha256"],
            })
        for row in rollback_rows:
            rollbacks.append({
                "deliverable_id": row["deliverable_id"], "action": row["action"],
                "path": row["path"], "sha256": row["sha256"],
            })

        initial_status, initial = json_result(package_dir / "PROJECT_CHECKS.json")
        premerge_status, premerge = json_result(package_dir / "PROJECT_CHECKS_PREMERGE.json")
        if initial_status != "FAIL" or len(initial) != 6:
            fail(f"package {package} initial check shape mismatch")
        base_pass = [row for row in initial if row.get("status") == "PASS"]
        pre_fail = [row for row in initial if row.get("id") == "frontend-premerge" and row.get("status") == "FAIL"]
        if len(base_pass) != 5 or len(pre_fail) != 1 or pre_fail[0].get("exit_code") != 1:
            fail(f"package {package} initial check semantics mismatch")
        if "HARNESS_PREMERGE_TEST_COUNT=0" not in str(pre_fail[0].get("stdout", "")):
            fail(f"package {package} missing fail-closed zero-test evidence")
        if premerge_status != "PASS" or len(premerge) != 1 or premerge[0].get("status") != "PASS":
            fail(f"package {package} server-backed premerge mismatch")
        stdout = str(premerge[0].get("stdout", ""))
        for token in ("HARNESS_PREMERGE_TEST_COUNT=8", "HARNESS_PREMERGE_SECTION9_TEST_COUNT=16", "HARNESS_PREMERGE_SECTION9_REPORT_ONLY=true"):
            if token not in stdout:
                fail(f"package {package} missing premerge token: {token}")
        app_checks.append({
            "package": f"APP-PKG-{package}", "initial_status": "EXPECTED_SUBSTRATE_FAIL_ONLY",
            "base_pass": 5, "initial_premerge_exit": 1, "initial_premerge_tests": 0,
            "server_backed_status": "PASS", "section8_tests": 8, "section9_tests": 16,
            "section9_report_only": "true", "verdict": "PASS",
        })

        normalization_rows = rows(package_dir / "PORTABILITY_NORMALIZATION.tsv")
        for row in normalization_rows:
            bound = resolve_binding(row["path"], package_dir=package_dir)
            if digest(bound) != row["post_sha256"] or bound.stat().st_size != int(row["post_bytes"]):
                fail(f"package {package} normalized evidence drift: {row['path']}")
            proof = row.get("reverse_proof") or row.get("classification") or ""
            if proof not in ("EXACT", "PASS", "GENERATED_RUN_METADATA_NORMALIZED_TO_REPO_ROOT", "GENERATED_CHECK_METADATA_NORMALIZED"):
                fail(f"package {package} bad normalization proof: {proof}")

        root_occurrences = 0
        temp_occurrences = 0
        for tree_name, tree in (("instance", package_dir), ("candidate", RUN / f"candidates/W_A3/APP-PKG{package}")):
            for path in sorted(tree.rglob("*")):
                if not path.is_file():
                    continue
                blob = path.read_bytes()
                hits = blob.count(ROOT_LITERAL)
                temp_hits = sum(blob.count(token) for token in TEMP_LITERALS)
                root_occurrences += hits
                temp_occurrences += temp_hits
                if hits or temp_hits:
                    portability_hits.append({
                        "package": f"APP-PKG-{package}", "tree": tree_name,
                        "path": path.relative_to(ROOT).as_posix(), "checkout_root_occurrences": hits,
                        "machine_temp_occurrences": temp_hits,
                    })
        expected_root_occurrences = {"08": 105, "09": 40, "10": 6}[package]
        if root_occurrences != expected_root_occurrences or temp_occurrences != 0:
            fail(f"package {package} portability inventory mismatch: {root_occurrences}/{temp_occurrences}")
        inventory = rows(package_dir / "PRESERVED_SOURCE_LITERAL_INVENTORY.tsv")
        if package == "08":
            if sum(int(row["occurrences"]) for row in inventory) != root_occurrences:
                fail("package 08 detailed portability inventory mismatch")
        else:
            total = [row for row in inventory if row["scope"] == "total"]
            if len(total) != 1 or int(total[0]["occurrences"]) != root_occurrences or int(total[0]["unclassified"]) != 0:
                fail(f"package {package} aggregate portability inventory mismatch")

    if len(package_bindings) != 220 or len(child_bindings) != 1470 or accepted_child_count != 32:
        fail("aggregate package/child binding count mismatch")
    if len(replacements) != 80 or len(rollbacks) != 80:
        fail("aggregate replacement/rollback cardinality mismatch")
    inverse = {"ADD": "DELETE", "DELETE": "ADD"}
    rollback_index = {(row["deliverable_id"], row["path"], row["sha256"]): row["action"] for row in rollbacks}
    replacement_paths: set[str] = set()
    for row in replacements:
        key = (row["deliverable_id"], row["path"], row["sha256"])
        if rollback_index.get(key) != inverse[row["action"]]:
            fail(f"rollback mismatch: {key}")
        if row["path"] in replacement_paths:
            fail(f"overlapping replacement ownership: {row['path']}")
        replacement_paths.add(row["path"])
        if Path(row["path"]).name not in (*LEGACY, "ScopeOfWork.md"):
            fail(f"status/control path in replacement: {row['path']}")

    candidate_rows: list[dict[str, object]] = []
    result_rows: list[dict[str, object]] = []
    simulation_rows: list[dict[str, object]] = []
    total_mappings = 0
    total_lines = 0
    live_bindings = 0
    preflight_names = {
        "Datasheet.md": "datasheet_sha256", "Specification.md": "specification_sha256",
        "Guidance.md": "guidance_sha256", "Procedure.md": "procedure_sha256",
        "_STATUS.md": "status_sha256", "_CONTEXT.md": "context_sha256",
        "_REFERENCES.md": "references_sha256", "_DEPENDENCIES.md": "dependencies_md_sha256",
        "Dependencies.csv": "dependencies_csv_sha256",
    }

    for ordinal, member in enumerate(members, 1):
        deliverable = member["deliverable_id"]
        package = member["package"].removeprefix("PKG-")
        if package not in PACKAGES or member["lifecycle"] != "IN_PROGRESS" or member["pilot"] != "false" or member["issued"] != "false":
            fail(f"population/lifecycle mismatch: {deliverable}")
        if member["live_format"] != "LEGACY_FOUR_DOC":
            fail(f"live format mismatch: {deliverable}")
        expected = package_results[package].get(deliverable)
        if expected is None:
            fail(f"missing package member result: {deliverable}")
        live = ROOT / member["live_path"]
        candidate = ROOT / member["candidate_path"]
        if not live.is_dir() or not candidate.is_file() or digest(candidate) != expected["candidate_sha256"]:
            fail(f"candidate/live identity mismatch: {deliverable}")
        if (live / "ScopeOfWork.md").exists():
            fail(f"live dual/SOW drift: {deliverable}")
        for name, field in preflight_names.items():
            if digest(live / name) != member[field]:
                fail(f"live preflight drift: {deliverable}/{name}")
            live_bindings += 1

        plan = [row for row in replacements if row["deliverable_id"] == deliverable]
        if len(plan) != 5:
            fail(f"member replacement count mismatch: {deliverable}")
        expected_plan = {("ADD", f"{member['live_path']}/ScopeOfWork.md", digest(candidate))}
        expected_plan |= {("DELETE", f"{member['live_path']}/{name}", member[preflight_names[name]]) for name in LEGACY}
        if {(row["action"], row["path"], row["sha256"]) for row in plan} != expected_plan:
            fail(f"member replacement semantics mismatch: {deliverable}")

        work = SCRATCH / deliverable
        standalone = work / "standalone"
        standalone.mkdir(parents=True)
        shutil.copy2(candidate, standalone / "ScopeOfWork.md")
        validation = run("python3", "tools/scope_of_work/validate_scope_of_work.py", "--json", str(standalone))
        if validation.returncode != 0 or json.loads(validation.stdout).get("format") != "SOW_V1":
            fail(f"standalone candidate validation failed: {deliverable}")

        dual = work / "dual"
        shutil.copytree(live, dual)
        shutil.copy2(candidate, dual / "ScopeOfWork.md")
        dual_validation = run(
            "python3", "tools/scope_of_work/validate_scope_of_work.py", "--json",
            "--isolated-migration", "--migration-authority", MIGRATION_AUTHORITY, str(dual),
        )
        if dual_validation.returncode != 0 or json.loads(dual_validation.stdout).get("format") != "MIGRATION_DUAL":
            fail(f"authorized dual validation failed: {deliverable}")

        evidence = work / "evidence"
        evidence.mkdir()
        claim_map = evidence / "claim_map.csv"
        mapped = run(
            "python3", "tools/scope_of_work/map_scope_of_work_claims.py",
            "--scope-of-work", str(candidate), "--source-dir", str(live), "--output-csv", str(claim_map),
        )
        if mapped.returncode != 0:
            fail(f"claim map failed: {deliverable}: {mapped.stderr}")
        with claim_map.open(newline="", encoding="utf-8") as handle:
            map_rows = list(csv.DictReader(handle))
        if any(row["Disposition"] != "PRESERVED" for row in map_rows):
            fail(f"non-preserved mapping: {deliverable}")
        parity_json = evidence / "parity.json"
        parity = run(
            "python3", "tools/scope_of_work/report_scope_of_work_parity.py",
            "--scope-of-work", str(candidate), "--source-dir", str(live), "--output-json", str(parity_json),
        )
        if parity.returncode != 0 or not json.loads(parity_json.read_text(encoding="utf-8")).get("pass"):
            fail(f"parity failed: {deliverable}")
        source_lines = sum(len((live / name).read_text(encoding="utf-8").splitlines()) for name in LEGACY)
        if len(map_rows) != int(expected["mapping_rows"]) or source_lines != int(expected["source_lines"]):
            fail(f"coverage mismatch: {deliverable}")

        checklist1, checklist2 = evidence / "checklist1.json", evidence / "checklist2.json"
        html1, html2 = evidence / "render1.html", evidence / "render2.html"
        for output in (checklist1, checklist2):
            result = run("python3", "tools/scope_of_work/derive_review_checklist.py", str(standalone), "--output", str(output))
            if result.returncode != 0:
                fail(f"checklist failed: {deliverable}")
        for output in (html1, html2):
            result = run("python3", "tools/scope_of_work/render_scope_of_work.py", str(candidate), "--output", str(output))
            if result.returncode != 0:
                fail(f"render failed: {deliverable}")
        if checklist1.read_bytes() != checklist2.read_bytes() or html1.read_bytes() != html2.read_bytes():
            fail(f"determinism mismatch: {deliverable}")
        html = html1.read_text(encoding="utf-8").lower()
        active_external = re.search(r"<(?:a|img|link|iframe|script)\b[^>]*(?:href|src)=[\"']https?://", html)
        if "<script" in html or active_external:
            fail(f"active render resource found: {deliverable}")

        partial = work / "negative_partial"
        partial.mkdir()
        shutil.copy2(candidate, partial / "ScopeOfWork.md")
        shutil.copy2(live / "Datasheet.md", partial / "Datasheet.md")
        unauthorized = work / "negative_unauthorized_dual"
        unauthorized.mkdir()
        shutil.copy2(candidate, unauthorized / "ScopeOfWork.md")
        for name in LEGACY:
            shutil.copy2(live / name, unauthorized / name)
        neg1 = run("python3", "tools/scope_of_work/derive_review_checklist.py", str(partial), "--output", str(work / "partial.json"))
        neg2 = run("python3", "tools/scope_of_work/derive_review_checklist.py", str(unauthorized), "--output", str(work / "unauthorized.json"))
        if neg1.returncode == 0 or neg2.returncode == 0 or (work / "partial.json").exists() or (work / "unauthorized.json").exists():
            fail(f"negative fixture failed open: {deliverable}")

        simulation = work / "simulation"
        shutil.copytree(live, simulation)
        baseline = tree_digest(simulation)
        status_before = digest(simulation / "_STATUS.md")
        control_before = {name: digest(simulation / name) for name in CONTROL}
        for name in LEGACY:
            (simulation / name).unlink()
        shutil.copy2(candidate, simulation / "ScopeOfWork.md")
        applied = run("python3", "tools/scope_of_work/validate_scope_of_work.py", "--json", str(simulation))
        if applied.returncode != 0 or json.loads(applied.stdout).get("format") != "SOW_V1":
            fail(f"isolated apply failed: {deliverable}")
        if status_before != digest(simulation / "_STATUS.md") or any(digest(simulation / name) != sha for name, sha in control_before.items()):
            fail(f"status/control changed during apply: {deliverable}")
        (simulation / "ScopeOfWork.md").unlink()
        for name in LEGACY:
            shutil.copy2(live / name, simulation / name)
        rollback_tree = tree_digest(simulation)
        if rollback_tree != baseline:
            fail(f"isolated rollback mismatch: {deliverable}")

        candidate_rows.append({
            "ordinal": ordinal, "package": f"APP-PKG-{package}", "deliverable_id": deliverable,
            "candidate_path": member["candidate_path"], "candidate_sha256": digest(candidate),
            "live_path": member["live_path"], "lifecycle": member["lifecycle"],
            "live_format": member["live_format"], "status_sha256": member["status_sha256"],
        })
        result_rows.append({
            "ordinal": ordinal, "package": f"APP-PKG-{package}", "deliverable_id": deliverable,
            "candidate_sha256": digest(candidate), "mapping_rows": len(map_rows), "source_lines": source_lines,
            "standalone_schema": "PASS_SOW_V1", "authorized_dual": "PASS_MIGRATION_DUAL",
            "claim_map": "PASS_PRESERVED", "parity": "PASS", "checklist_identity": "PASS",
            "render_identity_safety": "PASS", "partial_negative": "PASS_FAIL_CLOSED",
            "unauthorized_dual_negative": "PASS_FAIL_CLOSED", "source_status_control_identity": "PASS",
        })
        simulation_rows.append({
            "ordinal": ordinal, "package": f"APP-PKG-{package}", "deliverable_id": deliverable,
            "apply_format": "SOW_V1", "apply_candidate_sha256": digest(candidate),
            "status_preserved": "PASS", "control_preserved": "PASS",
            "rollback_legacy_restored": "PASS", "rollback_candidate_absent": "PASS",
            "rollback_tree_sha256": hashlib.sha256(json.dumps(rollback_tree, sort_keys=True).encode()).hexdigest(),
        })
        total_mappings += len(map_rows)
        total_lines += source_lines

    if total_mappings != 481 or total_lines != 4985 or live_bindings != 144:
        fail(f"aggregate member mismatch: {total_mappings}/{total_lines}/{live_bindings}")

    # Preserve recovery provenance as classified evidence, not accepted members.
    failed_author = json.loads((RUN / "instances/WORKING-A3-PKG09/children/AUTHOR-DEL-09-01/STATUS.json").read_text(encoding="utf-8"))
    if failed_author.get("status") != "FAILED_INPUTS" or failed_author.get("terminal") is not True or failed_author.get("candidate_path") is not None or failed_author.get("project_write") is not False:
        fail("PKG09 initial author failure classification drift")
    recovery_rows.extend([
        {"package": "APP-PKG-09", "attempt": "AUTHOR-DEL-09-01", "classification": "FAILED_INPUTS_BEFORE_TASK_EXECUTION", "accepted_member": "false", "preservation": "PASS"},
        {"package": "APP-PKG-09", "attempt": "VERIFY-DEL-09-01", "classification": "STALLED_PARTIAL_AFTER_SUBSTANTIVE_EVIDENCE", "accepted_member": "false", "preservation": "PASS"},
        {"package": "APP-PKG-09", "attempt": "VERIFY-DEL-09-01-R1_AND_MANAGER_CLOSEOUTS", "classification": "SUBSTANTIVE_PASS_MANAGER_EVIDENCE_ONLY_TERMINALIZATION", "accepted_member": "true", "preservation": "PASS"},
    ])
    fixture_ledger = RUN / "instances/WORKING-A3-PKG10/children/AUTHOR-DEL-10-02/workspace/evidence/FAIL_CLOSED_FIXTURES.tsv"
    fixture_rows = rows(fixture_ledger)
    fixture_status = {row["fixture"]: row["verdict"] for row in fixture_rows}
    if fixture_status.get("negative_padded_initial_malformed") != "MALFORMED_FIXTURE_NOT_A_NEGATIVE_PASS" or fixture_status.get("negative_padded_corrected") != "PASS_FAIL_CLOSED":
        fail("PKG10 DEL-10-02 recovery fixture classification drift")
    recovery_rows.extend([
        {"package": "APP-PKG-10", "attempt": "AUTHOR-DEL-10-02_INITIAL_PADDED_FIXTURE", "classification": "MALFORMED_FIXTURE_NOT_A_NEGATIVE_PASS", "accepted_member": "false", "preservation": "PASS"},
        {"package": "APP-PKG-10", "attempt": "AUTHOR-DEL-10-02_CORRECTED_FIXTURE_ONLY_RERUN", "classification": "PASS_FAIL_CLOSED", "accepted_member": "true", "preservation": "PASS"},
        {"package": "APP-PKG-10", "attempt": "MANAGER_EVIDENCE_ONLY_CLOSEOUTS", "classification": "SUBSTANTIVE_PASS_REPRODUCED_BEFORE_TERMINALIZATION", "accepted_member": "true", "preservation": "PASS"},
    ])

    project_dirty = run("git", "status", "--porcelain", "--untracked-files=all", "--", "projects/chirality-app-dev").stdout.strip()
    if project_dirty:
        fail(f"live project dirty paths detected:\n{project_dirty}")

    write_tsv(OUT / "REPLACEMENT_MANIFEST.tsv", ["deliverable_id", "action", "path", "source_path", "sha256"], replacements)
    write_tsv(OUT / "ROLLBACK_MANIFEST.tsv", ["deliverable_id", "action", "path", "sha256"], rollbacks)
    write_tsv(OUT / "CANDIDATE_MANIFEST.tsv", list(candidate_rows[0]), candidate_rows)
    write_tsv(OUT / "MEMBER_RESULTS.tsv", list(result_rows[0]), result_rows)
    write_tsv(OUT / "SIMULATION_RESULTS.tsv", list(simulation_rows[0]), simulation_rows)
    write_tsv(DETAIL / "PACKAGE_BINDINGS.tsv", list(package_bindings[0]), package_bindings)
    write_tsv(DETAIL / "CHILD_MANIFEST_BINDINGS.tsv", list(child_bindings[0]), child_bindings)
    write_tsv(DETAIL / "APP_CHECKS.tsv", list(app_checks[0]), app_checks)
    write_tsv(DETAIL / "PORTABILITY_HITS.tsv", list(portability_hits[0]), portability_hits)
    write_tsv(DETAIL / "RECOVERY_HISTORY.tsv", list(recovery_rows[0]), recovery_rows)
    summary = {
        "schema": "chirality-w-a3-reconciliation-reproduction/v1",
        "status": "PASS", "basis": f"main@{expected_head}", "graph_version": 27,
        "members": 16, "packages": 3, "author_verifier_pairs": 16,
        "accepted_terminal_child_surfaces": 32, "mappings": total_mappings,
        "source_lines": total_lines, "live_preflight_bindings": live_bindings,
        "package_manifest_bindings": len(package_bindings),
        "child_manifest_bindings": len(child_bindings),
        "replacement_rows": len(replacements), "rollback_rows": len(rollbacks),
        "apply_simulations": 16, "rollback_simulations": 16,
        "registered_app_checks": "3x initial five PASS plus preserved no-server premerge FAIL; 3x server-backed premerge PASS 8/8+16/16 report-only",
        "portability_preserved_occurrences": sum(int(row["checkout_root_occurrences"]) for row in portability_hits),
        "generated_unclassified_machine_or_temp_literals": 0,
        "disjoint_ownership": "PASS", "project_read_only": "PASS",
        "recovery_history": "PRESERVED_AND_CLASSIFIED",
        "blockers": [], "waivers": [], "unknowns": [], "rerun_requirements": [],
    }
    (DETAIL / "REPRODUCTION_SUMMARY.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    shutil.rmtree(SCRATCH)

    snapshot_manifest_rows: list[dict[str, object]] = []
    for path in sorted(OUT.rglob("*")):
        if not path.is_file() or path.name in ("MANIFEST.tsv", "ACCEPTANCE_MANIFEST.tsv"):
            continue
        snapshot_manifest_rows.append({
            "path": path.relative_to(ROOT).as_posix(),
            "sha256": digest(path),
            "bytes": path.stat().st_size,
        })
    write_tsv(OUT / "MANIFEST.tsv", ["path", "sha256", "bytes"], snapshot_manifest_rows)

    instance = RUN / "instances/RECON-A3-F"
    acceptance_targets = [
        ("snapshot_manifest", OUT / "MANIFEST.tsv"),
        ("basis", OUT / "BASIS.md"),
        ("checks", OUT / "CHECKS.md"),
        ("handoff_state", OUT / "HANDOFF_STATE.md"),
        ("member_results", OUT / "MEMBER_RESULTS.tsv"),
        ("candidate_manifest", OUT / "CANDIDATE_MANIFEST.tsv"),
        ("replacement_manifest", OUT / "REPLACEMENT_MANIFEST.tsv"),
        ("rollback_manifest", OUT / "ROLLBACK_MANIFEST.tsv"),
        ("simulation_results", OUT / "SIMULATION_RESULTS.tsv"),
        ("recovery_history", OUT / "RECOVERY_HISTORY.md"),
        ("recon_return", instance / "RETURN.md"),
        ("recon_status", instance / "STATUS.json"),
        ("recon_checks", instance / "CHECKS.md"),
        ("sealed_brief", instance / "LAUNCH_BRIEF.md"),
        ("reproduction_script", Path(__file__).resolve()),
    ]
    acceptance_rows = [{
        "kind": kind, "path": path.relative_to(ROOT).as_posix(), "sha256": digest(path),
    } for kind, path in acceptance_targets]
    write_tsv(OUT / "ACCEPTANCE_MANIFEST.tsv", ["kind", "path", "sha256"], acceptance_rows)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise
