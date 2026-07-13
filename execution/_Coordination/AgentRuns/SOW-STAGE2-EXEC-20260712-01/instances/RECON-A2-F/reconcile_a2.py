#!/usr/bin/env python3
"""Independent, deterministic W-A2 preintegration fan-in reproduction."""

from __future__ import annotations

import csv
import hashlib
import json
import shutil
import subprocess
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
OUT = RUN / "snapshots/W_A2/preintegration"
DETAIL = OUT / "detailed"
SCRATCH = OUT / "_scratch"
PREFLIGHT = RUN / "snapshots/W_A2/preflight/A2_MANIFEST.tsv"
PACKAGES = ("04", "05", "06")
EXPECTED_PACKAGE_ROWS = {"04": 68, "05": 66, "06": 74}
EXPECTED_PACKAGE_SHA = {
    "04": "b77f672d5dfcb73cb488b45ec9e7cd2b4c1c4667a2dc1c769fbf611919b0886a",
    "05": "ff62949670d41f305599669665ce56d09bcfdadc11727353978b2247cb131bd9",
    "06": "712aa59f0652c9b50e07a1cd9e0d0134287feb52db6d8092f09dc0f7130f2b14",
}
EXPECTED_CHILD_ROWS = {"04": 325, "05": 365, "06": 362}
EXPECTED_PORTABILITY = {"04": 16, "05": 14, "06": 51}
LEGACY = ("Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md")
CONTROL = {
    "_STATUS.md": "status_sha256",
    "_CONTEXT.md": "context_sha256",
    "_REFERENCES.md": "references_sha256",
    "_DEPENDENCIES.md": "dependencies_md_sha256",
    "Dependencies.csv": "dependencies_csv_sha256",
}
SOURCE_FIELDS = dict(zip(LEGACY, ("datasheet_sha256", "specification_sha256", "guidance_sha256", "procedure_sha256")))
ROOT_LITERAL = ROOT.as_posix()
TEMP_LITERALS = ("/var/folders/", "/private/var/folders/")
ALLOWED_LITERAL_NAMES = {"_REFERENCES.md", "_DEPENDENCIES.md", "_SEMANTIC.md", "_SEMANTIC_LENSING.md"}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tree(path: Path) -> dict[str, str]:
    return {p.relative_to(path).as_posix(): sha(p) for p in sorted(path.rglob("*")) if p.is_file()}


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path: Path, fields: list[str], data: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


def command(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=True)


def fail(message: str) -> None:
    raise RuntimeError(message)


def normalize_member(package: str, row: dict[str, str]) -> dict[str, str]:
    return {
        "deliverable_id": row["deliverable_id"],
        "candidate_path": row.get("candidate_path", f"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/candidates/W_A2/APP-PKG{package}/{row['deliverable_id']}/ScopeOfWork.md"),
        "candidate_sha256": row["candidate_sha256"],
        "mappings": row.get("mapping_rows", row.get("mapping_count", row.get("mappings", ""))),
        "source_lines": row.get("source_lines", row.get("source_line_count", "")),
        "author_status": row["author_status"],
        "verifier_status": row["verifier_status"],
    }


def normalize_manifest(package: str, name: str) -> list[dict[str, str]]:
    path = RUN / f"instances/WORKING-A2-PKG{package}/{name}"
    result = []
    for row in rows(path):
        action = row["action"]
        target = row.get("path", row.get("target_path", ""))
        if "sha256" in row:
            digest = row["sha256"]
        elif action == "ADD":
            digest = row.get("post_sha256", row.get("after_sha256", ""))
        else:
            digest = row.get("pre_sha256", row.get("before_sha256", ""))
        result.append({"deliverable_id": row["deliverable_id"], "action": action, "path": target, "sha256": digest})
    return result


def resolve_binding(manifest: Path, raw: str) -> Path:
    candidate = Path(raw)
    if candidate.is_absolute():
        return candidate
    root_path = ROOT / candidate
    local_path = manifest.parent / candidate
    if root_path.is_file():
        return root_path
    return local_path


def main() -> None:
    DETAIL.mkdir(parents=True, exist_ok=True)
    if SCRATCH.exists():
        shutil.rmtree(SCRATCH)
    SCRATCH.mkdir()

    if command("git", "rev-parse", "HEAD").stdout.strip() != "0af23f4709e1c95f6b2e0f19db80779bd4c968fa":
        fail("live HEAD differs from sealed dispatch basis")
    preflight_rows = rows(PREFLIGHT)
    if len(preflight_rows) != 16 or Counter(r["package"] for r in preflight_rows) != Counter({"PKG-04": 5, "PKG-05": 5, "PKG-06": 6}):
        fail("preflight membership mismatch")
    preflight = {r["deliverable_id"]: r for r in preflight_rows}

    package_bindings: list[dict[str, object]] = []
    child_bindings: list[dict[str, object]] = []
    member_by_id: dict[str, dict[str, str]] = {}
    replacements: list[dict[str, str]] = []
    rollbacks: list[dict[str, str]] = []
    check_rows: list[dict[str, object]] = []
    portability_rows: list[dict[str, object]] = []

    for package in PACKAGES:
        base = RUN / f"instances/WORKING-A2-PKG{package}"
        status = json.loads((base / "STATUS.json").read_text(encoding="utf-8"))
        if status.get("status") != "PASS" or status.get("terminal") is not True or status.get("blockers"):
            fail(f"PKG{package} not terminal clean PASS")
        manifest = base / "MANIFEST.tsv"
        if sha(manifest) != EXPECTED_PACKAGE_SHA[package]:
            fail(f"PKG{package} package manifest identity mismatch")
        package_rows = rows(manifest)
        if len(package_rows) != EXPECTED_PACKAGE_ROWS[package]:
            fail(f"PKG{package} package manifest cardinality mismatch")
        for ordinal, source in enumerate(package_rows, 1):
            row = {k.lower(): v for k, v in source.items()}
            target = resolve_binding(manifest, row["path"])
            actual = sha(target) if target.is_file() else "MISSING"
            actual_bytes = target.stat().st_size if target.is_file() else -1
            if actual != row["sha256"] or (row.get("bytes") and actual_bytes != int(row["bytes"])):
                fail(f"PKG{package} binding mismatch: {row['path']}")
            package_bindings.append({
                "package": f"APP-PKG-{package}", "ordinal": ordinal,
                "kind": row.get("kind", "bound_artifact"), "path": row["path"],
                "expected_sha256": row["sha256"], "actual_sha256": actual,
                "expected_bytes": row.get("bytes", actual_bytes), "actual_bytes": actual_bytes, "status": "PASS",
            })

        normalized_members = [normalize_member(package, r) for r in rows(base / "MEMBER_RESULTS.tsv")]
        expected_members = 6 if package == "06" else 5
        if len(normalized_members) != expected_members:
            fail(f"PKG{package} member cardinality mismatch")
        for row in normalized_members:
            if row["deliverable_id"] in member_by_id:
                fail(f"duplicate member {row['deliverable_id']}")
            if not row["author_status"].startswith("PASS") or not row["verifier_status"].startswith("PASS"):
                fail(f"non-PASS pair {row['deliverable_id']}")
            member_by_id[row["deliverable_id"]] = row

        package_child_rows = 0
        child_statuses = sorted((base / "children").glob("*/STATUS.json"))
        if len(child_statuses) != expected_members * 2:
            fail(f"PKG{package} terminal child status cardinality mismatch")
        for status_path in child_statuses:
            data = json.loads(status_path.read_text(encoding="utf-8"))
            if data.get("terminal") is not True or not str(data.get("status", "")).startswith(("PASS", "SUCCESS")):
                fail(f"nonterminal/non-PASS child: {status_path}")
        child_manifests = sorted((base / "children").glob("*/MANIFEST.tsv"))
        if len(child_manifests) != expected_members * 2:
            fail(f"PKG{package} child manifest count mismatch")
        for child_manifest in child_manifests:
            if any(r.get("path", r.get("Path", "")) == "MANIFEST.tsv" for r in rows(child_manifest)):
                fail(f"child manifest is not self-excluding: {child_manifest}")
            for ordinal, source in enumerate(rows(child_manifest), 1):
                row = {k.lower(): v for k, v in source.items()}
                target = resolve_binding(child_manifest, row["path"])
                actual = sha(target) if target.is_file() else "MISSING"
                actual_bytes = target.stat().st_size if target.is_file() else -1
                if actual != row["sha256"] or (row.get("bytes") and actual_bytes != int(row["bytes"])):
                    fail(f"child binding mismatch: {child_manifest}:{row['path']}")
                child_bindings.append({
                    "package": f"APP-PKG-{package}", "child": child_manifest.parent.name,
                    "ordinal": ordinal, "path": row["path"], "expected_sha256": row["sha256"],
                    "actual_sha256": actual, "expected_bytes": row.get("bytes", actual_bytes),
                    "actual_bytes": actual_bytes, "status": "PASS",
                })
                package_child_rows += 1
        if package_child_rows != EXPECTED_CHILD_ROWS[package]:
            fail(f"PKG{package} child binding aggregate mismatch: {package_child_rows}")

        replacements.extend(normalize_manifest(package, "REPLACEMENT_MANIFEST.tsv"))
        rollbacks.extend(normalize_manifest(package, "ROLLBACK_MANIFEST.tsv"))

        initial = json.loads((base / "PROJECT_CHECKS.json").read_text(encoding="utf-8"))
        rerun = json.loads((base / "PROJECT_CHECKS_PREMERGE.json").read_text(encoding="utf-8"))
        normalized_checks = [(r.get("id", r.get("check")), r.get("status"), r.get("exit_code"), r) for r in initial["results"]]
        ids = [x[0] for x in normalized_checks]
        expected_ids = ["harness-self-check", "harness-pytest", "frontend-typecheck", "frontend-test", "frontend-build", "frontend-premerge"]
        if ids != expected_ids or initial.get("status") != "FAIL":
            fail(f"PKG{package} initial App check inventory mismatch")
        if any(s != "PASS" or code != 0 for _, s, code, _ in normalized_checks[:5]):
            fail(f"PKG{package} base App check failure")
        failed = normalized_checks[5]
        failed_tests = failed[3].get("tests")
        if failed[1] != "FAIL" or failed[2] == 0 or (failed_tests not in (None, 0)):
            fail(f"PKG{package} initial premerge failure is not the preserved substrate case")
        rerun_row = rerun["results"][0]
        rerun_id = rerun_row.get("id", rerun_row.get("check"))
        stdout = rerun_row.get("stdout", "")
        section8 = rerun_row.get("section8_tests", 8 if "HARNESS_PREMERGE_TEST_COUNT=8" in stdout else None)
        section9 = rerun_row.get("section9_tests", 16 if "HARNESS_PREMERGE_SECTION9_TEST_COUNT=16" in stdout else None)
        report_only = rerun_row.get("section9_report_only", "HARNESS_PREMERGE_SECTION9_REPORT_ONLY=true" in stdout)
        if rerun.get("status") != "PASS" or len(rerun["results"]) != 1 or rerun_id != "frontend-premerge" or rerun_row.get("status") != "PASS" or rerun_row.get("exit_code") != 0 or section8 != 8 or section9 != 16 or report_only is not True:
            fail(f"PKG{package} server-backed premerge rerun mismatch")
        for check_id, check_status, exit_code, _ in normalized_checks:
            check_rows.append({"package": f"APP-PKG-{package}", "record": "initial", "check": check_id, "status": check_status, "exit_code": exit_code, "classification": "PRESERVED_SUBSTRATE_FAIL" if check_id == "frontend-premerge" else "REGISTERED_PASS"})
        check_rows.append({"package": f"APP-PKG-{package}", "record": "server_backed_rerun", "check": "frontend-premerge", "status": "PASS", "exit_code": 0, "classification": "SECTION8_8_SECTION9_16_REPORT_ONLY"})

        hit_count = 0
        scan_roots = [base, RUN / f"candidates/W_A2/APP-PKG{package}"]
        for scan_root in scan_roots:
            for path in sorted(scan_root.rglob("*")):
                if not path.is_file() or path.name == "MANIFEST.tsv" and path == OUT / "MANIFEST.tsv":
                    continue
                try:
                    text = path.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    continue
                repo_hits = text.count(ROOT_LITERAL)
                temp_hits = sum(text.count(token) for token in TEMP_LITERALS)
                if temp_hits:
                    fail(f"unportable temp-root literal: {path}")
                if repo_hits:
                    if path.name not in ALLOWED_LITERAL_NAMES or not any(part in {"workspace", "isolated", "isolation", "control", "run1", "run2"} for part in path.parts):
                        fail(f"unclassified generated machine-root literal: {path}")
                    portability_rows.append({"package": f"APP-PKG-{package}", "path": path.relative_to(ROOT).as_posix(), "repo_root_occurrences": repo_hits, "temp_root_occurrences": temp_hits, "classification": "PRESERVED_IMMUTABLE_SOURCE_OR_CONTROL"})
                    hit_count += repo_hits
        if hit_count != EXPECTED_PORTABILITY[package]:
            fail(f"PKG{package} portability inventory mismatch: {hit_count}")

    if len(package_bindings) != 208 or len(child_bindings) != 1052 or len(member_by_id) != 16:
        fail("aggregate fan-in cardinality mismatch")
    if set(member_by_id) != set(preflight):
        fail("package membership differs from accepted preflight")

    inverse = {"ADD": "DELETE", "DELETE": "ADD"}
    if len(replacements) != 80 or len(rollbacks) != 80:
        fail("combined replacement cardinality mismatch")
    replacement_keys = [(r["deliverable_id"], r["path"], r["sha256"], r["action"]) for r in replacements]
    rollback_keys = {(r["deliverable_id"], r["path"], r["sha256"], r["action"]) for r in rollbacks}
    if len(set(replacement_keys)) != 80 or len(rollback_keys) != 80:
        fail("duplicate replacement/rollback row")
    for row in replacements:
        if (row["deliverable_id"], row["path"], row["sha256"], inverse[row["action"]]) not in rollback_keys:
            fail(f"rollback inverse mismatch: {row}")
        if Path(row["path"]).name.startswith("_") or Path(row["path"]).name == "Dependencies.csv":
            fail(f"status/control replacement is forbidden: {row['path']}")
    by_member = defaultdict(list)
    for row in replacements:
        by_member[row["deliverable_id"]].append(row)
    target_paths = [r["path"] for r in replacements]
    if len(target_paths) != len(set(target_paths)):
        fail("overlapping replacement ownership")

    candidate_rows: list[dict[str, object]] = []
    member_proofs: list[dict[str, object]] = []
    simulations: list[dict[str, object]] = []
    total_mappings = total_lines = live_bindings = 0
    for ordinal, accepted in enumerate(preflight_rows, 1):
        deliverable = accepted["deliverable_id"]
        package = accepted["package"].removeprefix("PKG-")
        reported = member_by_id[deliverable]
        live = ROOT / accepted["live_path"]
        candidate = ROOT / accepted["candidate_path"]
        if accepted["candidate_path"] != reported["candidate_path"] or sha(candidate) != reported["candidate_sha256"]:
            fail(f"candidate identity mismatch: {deliverable}")
        for name, field in {**SOURCE_FIELDS, **CONTROL}.items():
            if sha(live / name) != accepted[field]:
                fail(f"live source/status/control drift: {deliverable}/{name}")
            live_bindings += 1
        if (live / "ScopeOfWork.md").exists() or accepted["lifecycle"] != "IN_PROGRESS" or accepted["live_format"] != "LEGACY_FOUR_DOC":
            fail(f"live format/lifecycle drift: {deliverable}")
        member_replacements = by_member[deliverable]
        names = Counter((r["action"], Path(r["path"]).name) for r in member_replacements)
        expected_names = Counter([("ADD", "ScopeOfWork.md"), *(("DELETE", name) for name in LEGACY)])
        if len(member_replacements) != 5 or names != expected_names:
            fail(f"five-path replacement shape mismatch: {deliverable}")
        if next(r for r in member_replacements if r["action"] == "ADD")["sha256"] != sha(candidate):
            fail(f"candidate replacement hash mismatch: {deliverable}")

        work = SCRATCH / deliverable
        candidate_only = work / "candidate"
        evidence = work / "evidence"
        candidate_only.mkdir(parents=True)
        evidence.mkdir()
        shutil.copy2(candidate, candidate_only / "ScopeOfWork.md")
        validation = command("python3", "tools/scope_of_work/validate_scope_of_work.py", "--json", str(candidate_only))
        if validation.returncode or json.loads(validation.stdout).get("format") != "SOW_V1":
            fail(f"schema validation failed: {deliverable}")
        claim_map = evidence / "claim_map.csv"
        mapped = command("python3", "tools/scope_of_work/map_scope_of_work_claims.py", "--scope-of-work", str(candidate), "--source-dir", str(live), "--output-csv", str(claim_map))
        if mapped.returncode:
            fail(f"claim mapping failed: {deliverable}: {mapped.stderr}")
        with claim_map.open(newline="", encoding="utf-8") as handle:
            map_rows = list(csv.DictReader(handle))
        parity_path = evidence / "parity.json"
        parity = command("python3", "tools/scope_of_work/report_scope_of_work_parity.py", "--scope-of-work", str(candidate), "--source-dir", str(live), "--output-json", str(parity_path))
        if parity.returncode or not json.loads(parity_path.read_text(encoding="utf-8")).get("pass"):
            fail(f"parity failed: {deliverable}")
        source_lines = sum(len((live / name).read_text(encoding="utf-8").splitlines()) for name in LEGACY)
        if len(map_rows) != int(reported["mappings"]) or source_lines != int(reported["source_lines"]) or any(r["Disposition"] != "PRESERVED" for r in map_rows):
            fail(f"coverage/disposition mismatch: {deliverable}")
        checklist1, checklist2 = evidence / "checklist1.json", evidence / "checklist2.json"
        render1, render2 = evidence / "render1.html", evidence / "render2.html"
        for output in (checklist1, checklist2):
            result = command("python3", "tools/scope_of_work/derive_review_checklist.py", str(candidate_only), "--output", str(output))
            if result.returncode:
                fail(f"checklist failed: {deliverable}")
        for output in (render1, render2):
            result = command("python3", "tools/scope_of_work/render_scope_of_work.py", str(candidate_only / "ScopeOfWork.md"), "--output", str(output))
            if result.returncode:
                fail(f"render failed: {deliverable}")
        rendered = render1.read_text(encoding="utf-8").lower()
        if checklist1.read_bytes() != checklist2.read_bytes() or render1.read_bytes() != render2.read_bytes() or "<script" in rendered or 'href="http' in rendered or 'src="http' in rendered:
            fail(f"determinism/render safety failed: {deliverable}")
        partial = work / "negative_partial"
        dual = work / "negative_dual"
        partial.mkdir(); dual.mkdir()
        shutil.copy2(candidate, partial / "ScopeOfWork.md"); shutil.copy2(live / LEGACY[0], partial / LEGACY[0])
        shutil.copy2(candidate, dual / "ScopeOfWork.md")
        for name in LEGACY:
            shutil.copy2(live / name, dual / name)
        negative1 = command("python3", "tools/scope_of_work/derive_review_checklist.py", str(partial), "--output", str(work / "partial.json"))
        negative2 = command("python3", "tools/scope_of_work/derive_review_checklist.py", str(dual), "--output", str(work / "dual.json"))
        if negative1.returncode == 0 or negative2.returncode == 0 or (work / "partial.json").exists() or (work / "dual.json").exists():
            fail(f"negative state failed open: {deliverable}")

        simulation = work / "simulation"
        shutil.copytree(live, simulation)
        baseline = tree(simulation)
        for name in LEGACY:
            (simulation / name).unlink()
        shutil.copy2(candidate, simulation / "ScopeOfWork.md")
        applied = command("python3", "tools/scope_of_work/validate_scope_of_work.py", "--json", str(simulation))
        if applied.returncode or json.loads(applied.stdout).get("format") != "SOW_V1":
            fail(f"apply simulation failed: {deliverable}")
        applied_tree = tree(simulation)
        if any(applied_tree.get(path) != digest for path, digest in baseline.items() if path not in LEGACY):
            fail(f"control changed during apply: {deliverable}")
        (simulation / "ScopeOfWork.md").unlink()
        for name in LEGACY:
            shutil.copy2(live / name, simulation / name)
        rolled_back = tree(simulation)
        if rolled_back != baseline:
            fail(f"rollback tree mismatch: {deliverable}")

        candidate_rows.append({"ordinal": ordinal, "package": f"APP-PKG-{package}", "deliverable_id": deliverable, "candidate_path": accepted["candidate_path"], "candidate_sha256": sha(candidate), "live_format": accepted["live_format"], "lifecycle": accepted["lifecycle"], "status_sha256": accepted["status_sha256"]})
        member_proofs.append({"ordinal": ordinal, "package": f"APP-PKG-{package}", "deliverable_id": deliverable, "candidate_sha256": sha(candidate), "mappings": len(map_rows), "source_lines": source_lines, "schema": "PASS", "map": "PASS", "parity": "PASS", "checklist_determinism": "PASS", "render_determinism_safety": "PASS", "negative_partial": "PASS_FAIL_CLOSED", "negative_dual": "PASS_FAIL_CLOSED", "live_binding": "9/9_PASS", "authority": "D-GOV-16_BOUND"})
        simulations.append({"ordinal": ordinal, "package": f"APP-PKG-{package}", "deliverable_id": deliverable, "apply": "PASS_SOW_V1", "status_control_preserved": "PASS", "rollback": "PASS_EXACT_TREE", "rollback_tree_sha256": hashlib.sha256(json.dumps(rolled_back, sort_keys=True).encode()).hexdigest()})
        total_mappings += len(map_rows); total_lines += source_lines

    if total_mappings != 491 or total_lines != 5584 or live_bindings != 144:
        fail(f"aggregate source proof mismatch: {total_mappings}/{total_lines}/{live_bindings}")

    write_tsv(DETAIL / "PACKAGE_BINDINGS.tsv", list(package_bindings[0]), package_bindings)
    write_tsv(DETAIL / "CHILD_MANIFEST_BINDINGS.tsv", list(child_bindings[0]), child_bindings)
    write_tsv(DETAIL / "APP_CHECKS.tsv", list(check_rows[0]), check_rows)
    write_tsv(DETAIL / "PORTABILITY_HITS.tsv", list(portability_rows[0]), portability_rows)
    write_tsv(OUT / "CANDIDATE_MANIFEST.tsv", list(candidate_rows[0]), candidate_rows)
    write_tsv(OUT / "MEMBER_RESULTS.tsv", list(member_proofs[0]), member_proofs)
    write_tsv(OUT / "REPLACEMENT_MANIFEST.tsv", ["deliverable_id", "action", "path", "sha256"], replacements)
    write_tsv(OUT / "ROLLBACK_MANIFEST.tsv", ["deliverable_id", "action", "path", "sha256"], rollbacks)
    write_tsv(OUT / "SIMULATION_RESULTS.tsv", list(simulations[0]), simulations)
    (DETAIL / "REPRODUCTION_SUMMARY.json").write_text(json.dumps({
        "schema": "chirality-w-a2-reconciliation-reproduction/v1", "status": "PASS",
        "basis": "main@0af23f4709e1c95f6b2e0f19db80779bd4c968fa", "packages": 3,
        "members": 16, "author_verifier_pairs": 16, "mappings": total_mappings,
        "source_lines": total_lines, "live_preflight_bindings": live_bindings,
        "package_manifest_bindings": len(package_bindings), "child_manifest_bindings": len(child_bindings),
        "replacement_rows": len(replacements), "rollback_rows": len(rollbacks),
        "apply_simulations": 16, "rollback_simulations": 16,
        "registered_app_checks": "3x initial 5 PASS plus preserved no-server premerge FAIL; 3x server-backed premerge PASS 8/8+16/16 report-only",
        "portability_preserved_occurrences": sum(int(r["repo_root_occurrences"]) for r in portability_rows),
        "generated_unclassified_machine_or_temp_literals": 0, "disjoint_ownership": "PASS",
        "blockers": [], "waivers": [], "unknowns": [],
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    shutil.rmtree(SCRATCH)


if __name__ == "__main__":
    main()
