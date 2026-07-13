#!/usr/bin/env python3
"""Deterministically reproduce W-A1 identities, manifests, proofs, and simulations."""

from __future__ import annotations

import csv
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[8]
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
OUT = RUN / "snapshots/W_A1/preintegration"
DETAIL = OUT / "detailed"
SCRATCH = OUT / "_scratch"
PREFLIGHT = RUN / "snapshots/W_A1/preflight/A1_MANIFEST.tsv"
AUTHORITY = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
LEGACY = ("Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md")
PACKAGES = ("00", "01", "02", "03")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tree_digest(path: Path) -> dict[str, str]:
    return {
        p.relative_to(path).as_posix(): digest(p)
        for p in sorted(path.rglob("*"))
        if p.is_file()
    }


def run(*args: str, cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True)


def write_tsv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def fail(message: str) -> None:
    raise RuntimeError(message)


def main() -> int:
    DETAIL.mkdir(parents=True, exist_ok=True)
    if SCRATCH.exists():
        shutil.rmtree(SCRATCH)
    SCRATCH.mkdir()

    with PREFLIGHT.open(newline="", encoding="utf-8") as handle:
        members = list(csv.DictReader(handle, delimiter="\t"))
    if len(members) != 15:
        fail(f"expected 15 members, got {len(members)}")

    package_results: dict[str, dict[str, dict[str, str]]] = {}
    replacements: list[dict[str, str]] = []
    rollbacks: list[dict[str, str]] = []
    for package in PACKAGES:
        base = RUN / f"instances/WORKING-A1-PKG{package}"
        with (base / "MEMBER_RESULTS.tsv").open(newline="", encoding="utf-8") as handle:
            package_results[package] = {
                row["deliverable_id"]: row for row in csv.DictReader(handle, delimiter="\t")
            }
        for name, target in (("REPLACEMENT_MANIFEST.tsv", replacements), ("ROLLBACK_MANIFEST.tsv", rollbacks)):
            with (base / name).open(newline="", encoding="utf-8") as handle:
                target.extend(csv.DictReader(handle, delimiter="\t"))

    if len(replacements) != 75 or len(rollbacks) != 75:
        fail(f"manifest cardinality mismatch: {len(replacements)}/{len(rollbacks)}")
    inverse = {"ADD": "DELETE", "DELETE": "ADD"}
    rollback_index = {(r["deliverable_id"], r["path"], r["sha256"]): r["action"] for r in rollbacks}
    for row in replacements:
        key = (row["deliverable_id"], row["path"], row["sha256"])
        if rollback_index.get(key) != inverse[row["action"]]:
            fail(f"rollback mismatch: {key}")
        if Path(row["path"]).name.startswith("_") or Path(row["path"]).name in {"Dependencies.csv"}:
            fail(f"control/status path in replacement: {row['path']}")

    write_tsv(OUT / "REPLACEMENT_MANIFEST.tsv", ["deliverable_id", "action", "path", "sha256"], replacements)
    write_tsv(OUT / "ROLLBACK_MANIFEST.tsv", ["deliverable_id", "action", "path", "sha256"], rollbacks)

    candidate_rows: list[dict[str, object]] = []
    result_rows: list[dict[str, object]] = []
    sim_rows: list[dict[str, object]] = []
    total_mappings = 0
    total_lines = 0

    for ordinal, member in enumerate(members, 1):
        deliverable = member["deliverable_id"]
        package = member["package"].removeprefix("PKG-")
        expected = package_results[package][deliverable]
        live = ROOT / member["live_path"]
        candidate = ROOT / member["candidate_path"]
        if digest(candidate) != expected["candidate_sha256"]:
            fail(f"candidate drift: {deliverable}")
        source_hashes = {
            "Datasheet.md": member["datasheet_sha256"],
            "Specification.md": member["specification_sha256"],
            "Guidance.md": member["guidance_sha256"],
            "Procedure.md": member["procedure_sha256"],
        }
        for name, expected_hash in source_hashes.items():
            if digest(live / name) != expected_hash:
                fail(f"source drift: {deliverable}/{name}")
        if digest(live / "_STATUS.md") != member["status_sha256"]:
            fail(f"status drift: {deliverable}")
        if (live / "ScopeOfWork.md").exists():
            fail(f"live dual/SOW drift: {deliverable}")

        work = SCRATCH / deliverable
        candidate_only = work / "candidate"
        candidate_only.mkdir(parents=True)
        shutil.copy2(candidate, candidate_only / "ScopeOfWork.md")
        evidence = work / "evidence"
        evidence.mkdir()

        validation = run("python3", "tools/scope_of_work/validate_scope_of_work.py", "--json", str(candidate_only))
        if validation.returncode != 0 or json.loads(validation.stdout).get("format") != "SOW_V1":
            fail(f"candidate schema/format failed: {deliverable}: {validation.stderr}")
        claim_map = evidence / "claim_map.csv"
        mapped = run(
            "python3", "tools/scope_of_work/map_scope_of_work_claims.py",
            "--scope-of-work", str(candidate), "--source-dir", str(live), "--output-csv", str(claim_map),
        )
        if mapped.returncode != 0:
            fail(f"claim map failed: {deliverable}: {mapped.stderr}")
        with claim_map.open(newline="", encoding="utf-8") as handle:
            map_rows = list(csv.DictReader(handle))
        parity_json = evidence / "parity.json"
        parity = run(
            "python3", "tools/scope_of_work/report_scope_of_work_parity.py",
            "--scope-of-work", str(candidate), "--source-dir", str(live), "--output-json", str(parity_json),
        )
        if parity.returncode != 0 or not json.loads(parity_json.read_text()).get("pass"):
            fail(f"parity failed: {deliverable}: {parity.stderr}")
        source_lines = sum(len((live / name).read_text(encoding="utf-8").splitlines()) for name in LEGACY)
        if len(map_rows) != int(expected["mapping_rows"]) or source_lines != int(expected["source_lines"]):
            fail(f"coverage mismatch: {deliverable}")
        if any(row["Disposition"] != "PRESERVED" for row in map_rows):
            fail(f"non-preserved map row: {deliverable}")

        checklist1, checklist2 = evidence / "checklist1.json", evidence / "checklist2.json"
        html1, html2 = evidence / "render1.html", evidence / "render2.html"
        for output in (checklist1, checklist2):
            result = run("python3", "tools/scope_of_work/derive_review_checklist.py", str(candidate_only), "--output", str(output))
            if result.returncode != 0:
                fail(f"checklist failed: {deliverable}: {result.stderr}")
        for output in (html1, html2):
            result = run("python3", "tools/scope_of_work/render_scope_of_work.py", str(candidate_only / "ScopeOfWork.md"), "--output", str(output))
            if result.returncode != 0:
                fail(f"render failed: {deliverable}: {result.stderr}")
        if checklist1.read_bytes() != checklist2.read_bytes() or html1.read_bytes() != html2.read_bytes():
            fail(f"determinism failed: {deliverable}")
        html = html1.read_text(encoding="utf-8").lower()
        if "<script" in html or "http://" in html or "https://" in html:
            fail(f"render safety failed: {deliverable}")

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
        neg2 = run("python3", "tools/scope_of_work/derive_review_checklist.py", str(unauthorized), "--output", str(work / "dual.json"))
        if neg1.returncode == 0 or neg2.returncode == 0 or (work / "partial.json").exists() or (work / "dual.json").exists():
            fail(f"negative fixture failed open: {deliverable}")

        simulation = work / "simulation"
        shutil.copytree(live, simulation)
        baseline = tree_digest(simulation)
        status_before = digest(simulation / "_STATUS.md")
        for name in LEGACY:
            (simulation / name).unlink()
        shutil.copy2(candidate, simulation / "ScopeOfWork.md")
        applied = run("python3", "tools/scope_of_work/validate_scope_of_work.py", "--json", str(simulation))
        if applied.returncode != 0 or json.loads(applied.stdout).get("format") != "SOW_V1":
            fail(f"apply format failed: {deliverable}")
        control_after_apply = tree_digest(simulation)
        for path, sha in baseline.items():
            if path not in LEGACY and control_after_apply.get(path) != sha:
                fail(f"control changed during apply: {deliverable}/{path}")
        if digest(simulation / "_STATUS.md") != status_before:
            fail(f"status changed during apply: {deliverable}")
        (simulation / "ScopeOfWork.md").unlink()
        for name in LEGACY:
            shutil.copy2(live / name, simulation / name)
        rollback_tree = tree_digest(simulation)
        if rollback_tree != baseline:
            fail(f"rollback tree mismatch: {deliverable}")

        candidate_rows.append({
            "ordinal": ordinal, "package": f"APP-PKG-{package}", "deliverable_id": deliverable,
            "candidate_path": member["candidate_path"], "candidate_sha256": digest(candidate),
            "source_state": member["lifecycle"], "live_format": member["live_format"],
            "status_sha256": member["status_sha256"],
        })
        result_rows.append({
            "ordinal": ordinal, "package": f"APP-PKG-{package}", "deliverable_id": deliverable,
            "candidate_sha256": digest(candidate), "mapping_rows": len(map_rows), "source_lines": source_lines,
            "schema": "PASS", "claim_map": "PASS", "parity": "PASS", "checklist_identity": "PASS",
            "render_identity_safety": "PASS", "partial_negative": "PASS_FAIL_CLOSED",
            "unauthorized_dual_negative": "PASS_FAIL_CLOSED", "source_status_identity": "PASS",
        })
        sim_rows.append({
            "ordinal": ordinal, "package": f"APP-PKG-{package}", "deliverable_id": deliverable,
            "apply_format": "SOW_V1", "apply_candidate_hash": digest(simulation.parent / "candidate/ScopeOfWork.md"),
            "status_preserved": "PASS", "control_preserved": "PASS", "rollback_legacy_restored": "PASS",
            "rollback_candidate_absent": "PASS", "rollback_tree_sha256": hashlib.sha256(json.dumps(rollback_tree, sort_keys=True).encode()).hexdigest(),
        })
        total_mappings += len(map_rows)
        total_lines += source_lines

    if total_mappings != 456 or total_lines != 4817:
        fail(f"aggregate mismatch: {total_mappings}/{total_lines}")

    write_tsv(OUT / "CANDIDATE_MANIFEST.tsv", list(candidate_rows[0]), candidate_rows)
    write_tsv(OUT / "MEMBER_RESULTS.tsv", list(result_rows[0]), result_rows)
    write_tsv(OUT / "SIMULATION_RESULTS.tsv", list(sim_rows[0]), sim_rows)
    (DETAIL / "REPRODUCTION_SUMMARY.json").write_text(json.dumps({
        "schema": "chirality-w-a1-reconciliation-reproduction/v1",
        "status": "PASS", "members": 15, "packages": 4, "author_verifier_pairs": 30,
        "mappings": total_mappings, "source_lines": total_lines,
        "replacement_rows": len(replacements), "rollback_rows": len(rollbacks),
        "candidate_schema_map_parity_checklist_render_negative": "15/15 PASS",
        "apply_simulations": "15/15 PASS", "rollback_simulations": "15/15 PASS",
        "authority": AUTHORITY,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    shutil.rmtree(SCRATCH)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise
