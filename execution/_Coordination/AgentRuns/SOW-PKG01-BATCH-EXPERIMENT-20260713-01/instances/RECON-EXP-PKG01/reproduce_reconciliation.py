#!/usr/bin/env python3
"""Independent PKG-01 batch-experiment reconciliation (run-local writes only)."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG01-BATCH-EXPERIMENT-20260713-01"
PARENT = RUN / "instances/WORKING-EXP-PKG01"
AUTHOR = PARENT / "children/BATCH-AUTHOR-PKG01"
VERIFY = PARENT / "children/BATCH-VERIFY-PKG01"
OUT = RUN / "snapshots/reconciliation"
SCRATCH = OUT / "reproduction"
TOOLS = ROOT / "tools/scope_of_work"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
BASIS = "projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@69ac259a7113d5a838fb22aa2e84df0e0f109713"
FILES = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROL = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]

SEEDS = {
    "DEL-01-02": {
        "scopes": ["SOW-003", "SOW-028"], "objectives": ["OBJ-002"],
        "out": "A copyright and protected-data boundary policy and contribution-review checklist requirements defining allowed public content, prohibited public content, private or user-controlled content, provenance, quarantine, and human/legal escalation.",
        "ac": "The policy and contribution-review checklist preserve the documented prohibited-content boundary, provenance and contributor-certification fields, quarantine and human/legal escalation path, unresolved TBD decisions, and non-claim limitations for SOW-003 and SOW-028.",
        "ver": "Compare the converted contract source markers and parity report against all four legacy source documents, and review the output/evaluation matrix and derived checklist for complete source-grounded coverage.",
    },
    "DEL-01-03": {
        "scopes": ["SOW-028", "SOW-048"], "objectives": ["OBJ-002"],
        "out": "A contributor certification workflow and template requirements for attestations, provenance fields, protected-content screening, review routing, quarantine or rejection, and disposition records.",
        "ac": "The workflow preserves the documented contributor fields, protected-content stop and quarantine rules, repository-governance-only disposition boundary, recorded human-gated decisions, and residual TBDs for SOW-028 and SOW-048 without adding legal or professional approval.",
        "ver": "Compare the converted contract source markers and parity report against all four legacy source documents, then inspect the matrix and derived checklist for complete contributor-workflow coverage and preserved authority boundaries.",
    },
    "DEL-01-04": {
        "scopes": ["SOW-034", "SOW-064"], "objectives": ["OBJ-011", "OBJ-018"],
        "out": "A professional-responsibility and product-claims policy and report-notice requirements defining permitted evidence claims, prohibited reliance claims, human approval boundaries, and bounded analysis-grade design-engine language.",
        "ac": "The policy preserves the distinctions among mechanics results, user-rule results, validation evidence, competent human judgment, and approval; prohibits software or agent reliance claims; and retains all recorded TBDs and human gates for SOW-034 and SOW-064.",
        "ver": "Compare the converted contract source markers and parity report against all four legacy source documents, then inspect the matrix and derived checklist for the non-authoritative professional-reliance boundary and exact SOW-034, SOW-064, OBJ-011, and OBJ-018 traceability.",
    },
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args: list[str], expect_success: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    if (result.returncode == 0) != expect_success:
        raise AssertionError(f"unexpected exit {result.returncode}: {' '.join(args)}\n{result.stdout}\n{result.stderr}")
    return result


def copy_kit(source: Path, target: Path) -> None:
    target.mkdir(parents=True)
    for name in FILES + CONTROL:
        shutil.copy2(source / name, target / name)


def verify_manifest(label: str, path: Path, expected: int) -> dict[str, object]:
    rows = list(csv.DictReader(path.open(), delimiter="\t"))
    assert len(rows) == expected
    portable_prefix = "{REPO_ROOT}/"
    self_path = portable_prefix + str(path.relative_to(ROOT))
    assert all(row["path"].startswith(portable_prefix) for row in rows)
    assert all(row["path"] != self_path for row in rows)
    total_bytes = 0
    for row in rows:
        actual = ROOT / row["path"].removeprefix(portable_prefix)
        assert actual.is_file()
        assert sha(actual) == row["sha256"]
        assert actual.stat().st_size == int(row["bytes"])
        if "lines" in row:
            assert len(actual.read_bytes().splitlines()) == int(row["lines"])
        total_bytes += int(row["bytes"])
    return {"manifest": label, "entries": len(rows), "bytes": total_bytes, "verdict": "PASS"}


def write_tsv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def write_manifest(root: Path) -> None:
    rows = []
    for path in sorted(p for p in root.rglob("*") if p.is_file() and p.name != "MANIFEST.tsv"):
        data = path.read_bytes()
        rows.append(["{REPO_ROOT}/" + str(path.relative_to(ROOT)), sha(path), len(data), len(data.splitlines())])
    write_tsv(root / "MANIFEST.tsv", ["path", "sha256", "bytes", "lines"], rows)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    if SCRATCH.exists():
        shutil.rmtree(SCRATCH)
    SCRATCH.mkdir()

    manifest_results = [
        verify_manifest("package_snapshot", RUN / "snapshots/package/MANIFEST.tsv", 133),
        verify_manifest("manager", PARENT / "MANIFEST.tsv", 29),
        verify_manifest("author", AUTHOR / "MANIFEST.tsv", 265),
        verify_manifest("verifier", VERIFY / "MANIFEST.tsv", 317),
    ]

    # Exact durable topology and absence of hidden child delegation surfaces.
    child_dirs = sorted(p.name for p in (PARENT / "children").iterdir() if p.is_dir())
    assert child_dirs == ["BATCH-AUTHOR-PKG01", "BATCH-VERIFY-PKG01"]
    assert not any(p.name == "children" for c in (AUTHOR, VERIFY) for p in c.rglob("children"))
    assert "do not delegate" in (AUTHOR / "LAUNCH_BRIEF.md").read_text().lower()
    assert "do not delegate" in (VERIFY / "LAUNCH_BRIEF.md").read_text().lower()
    a_status = json.loads((AUTHOR / "STATUS.json").read_text())
    v_status = json.loads((VERIFY / "STATUS.json").read_text())
    assert a_status["agent_type"] == "ephemeral-generalist-agent-2"
    assert v_status["status"] == "PASS_UNCHANGED"

    # Evidence-family equality and append-only retry evidence.
    author_sets = {}
    verifier_sets = {}
    for did in SEEDS:
        author_sets[did] = {str(p.relative_to(AUTHOR / "members" / did)) for p in (AUTHOR / "members" / did).rglob("*") if p.is_file()}
        verifier_sets[did] = {str(p.relative_to(VERIFY / "members" / did)) for p in (VERIFY / "members" / did).rglob("*") if p.is_file()}
    author_common = set.intersection(*author_sets.values())
    assert len(author_common) == 84
    assert author_sets["DEL-01-03"] == author_sets["DEL-01-04"] == author_common
    assert author_sets["DEL-01-02"] - author_common == {"ATTEMPTS.md", "initial-authority-failure.exit", "initial-authority-failure.stderr", "initial-authority-failure.stdout"}
    assert all(len(paths) == 103 for paths in verifier_sets.values())
    assert verifier_sets["DEL-01-02"] == verifier_sets["DEL-01-03"] == verifier_sets["DEL-01-04"]
    a_progress = list(csv.DictReader((AUTHOR / "PROGRESS.tsv").open(), delimiter="\t"))
    v_progress = list(csv.DictReader((VERIFY / "PROGRESS.tsv").open(), delimiter="\t"))
    assert [sum(r["deliverable_id"] == did for r in a_progress) for did in SEEDS] == [7, 7, 7]
    assert [sum(r["deliverable_id"] == did for r in v_progress) for did in SEEDS] == [15, 9, 9]
    assert any(r["stage"] == "evidence_correction_001" and r["retries"] == "1" for r in v_progress)
    assert "append-only progress history" in (VERIFY / "EVIDENCE_CORRECTION-001.md").read_text()

    frozen = list(csv.DictReader((PARENT / "FROZEN_INPUTS.tsv").open(), delimiter="\t"))
    assert [r["deliverable_id"] for r in frozen] == list(SEEDS)
    p1_rows = {r["deliverable_id"]: r for r in csv.DictReader((ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_P1/preflight-r1/P1_MANIFEST.tsv").open(), delimiter="\t") if r["deliverable_id"] in SEEDS}
    assert set(p1_rows) == set(SEEDS)

    members = []
    replacement = []
    rollback = []
    simulations = []
    total_maps = total_lines = 0
    hash_fields = {
        "Datasheet.md": "datasheet_sha256", "Specification.md": "specification_sha256",
        "Guidance.md": "guidance_sha256", "Procedure.md": "procedure_sha256",
        "_STATUS.md": "status_sha256", "_CONTEXT.md": "context_sha256",
        "_REFERENCES.md": "references_sha256", "_DEPENDENCIES.md": "dependencies_md_sha256",
        "Dependencies.csv": "dependencies_csv_sha256",
    }

    for row in frozen:
        did = row["deliverable_id"]
        seed = SEEDS[did]
        live = ROOT / row["live_path"]
        candidate = RUN / f"candidates/PIP-PKG01/{did}/ScopeOfWork.md"
        member = SCRATCH / did
        a = member / "conversion-a"
        b = member / "conversion-b"
        copy_kit(live, a)
        copy_kit(live, b)
        assert row["lifecycle"] == "IN_PROGRESS" and row["live_format"] == "LEGACY_FOUR_DOC"
        assert not (live / "ScopeOfWork.md").exists()
        for name, field in hash_fields.items():
            assert sha(live / name) == row[field] == p1_rows[did][field]
        assert row["decomposition_basis"] == BASIS == p1_rows[did]["decomposition_basis"]
        assert [x.strip() for x in p1_rows[did]["scope_refs"].split(",")] == seed["scopes"]
        assert [x.strip() for x in p1_rows[did]["objective_refs"].split(",")] == seed["objectives"]
        assert "IN_PROGRESS" in (live / "_STATUS.md").read_text()

        base = ["python3", str(TOOLS / "convert_four_documents_to_scope_of_work.py"), "--deliverable-id", did, "--package-id", "PKG-01", "--decomposition-basis", BASIS]
        for value in seed["scopes"]:
            base += ["--project-scope-ref", value]
        for value in seed["objectives"]:
            base += ["--package-objective-ref", value]
        base += ["--output-description", seed["out"], "--acceptance-criterion", seed["ac"], "--verification-method", seed["ver"], "--isolated-migration", "--migration-authority", AUTH]
        run(base + ["--deliverable", str(a)])
        run(base + ["--deliverable", str(b)])
        assert (a / "ScopeOfWork.md").read_bytes() == (b / "ScopeOfWork.md").read_bytes() == candidate.read_bytes()
        candidate_text = candidate.read_text()
        assert seed["out"] in candidate_text and seed["ac"] in candidate_text and seed["ver"] in candidate_text

        standalone = run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(candidate)])
        assert json.loads(standalone.stdout)["format"] == "SOW_V1"
        for work in (a, b):
            dual = run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--isolated-migration", "--migration-authority", AUTH, "--json", str(work)])
            assert json.loads(dual.stdout)["format"] == "MIGRATION_DUAL"

        artifacts = []
        for n in (1, 2):
            cmap = member / f"claim-map-{n}.csv"
            parity_json = member / f"parity-{n}.json"
            parity_md = member / f"parity-{n}.md"
            checklist = member / f"checklist-{n}.json"
            render = member / f"render-{n}.html"
            run(["python3", str(TOOLS / "map_scope_of_work_claims.py"), "--scope-of-work", str(candidate), "--source-dir", str(live), "--output-csv", str(cmap)])
            run(["python3", str(TOOLS / "report_scope_of_work_parity.py"), "--scope-of-work", str(candidate), "--source-dir", str(live), "--output-json", str(parity_json), "--output-md", str(parity_md), "--isolated-migration", "--migration-authority", AUTH])
            run(["python3", str(TOOLS / "derive_review_checklist.py"), str(candidate), "--output", str(checklist)])
            run(["python3", str(TOOLS / "render_scope_of_work.py"), str(candidate), "--output", str(render)])
            artifacts.append((cmap, parity_json, parity_md, checklist, render))
        for left, right in zip(artifacts[0], artifacts[1]):
            assert left.read_bytes() == right.read_bytes()
        parity = json.loads(artifacts[0][1].read_text())
        assert parity["pass"] and not parity["issues"] and parity["scope_of_work_sha256"] == sha(candidate)
        assert all(c["pass"] and not c["issues"] and c["disposition"] == "PRESERVED" for c in parity["checks"])
        by_file = {name: [] for name in FILES}
        for check in parity["checks"]:
            by_file[check["source_file"]].append((check["line_start"], check["line_end"]))
        source_lines = 0
        for name, spans in by_file.items():
            expected_start = 1
            for start, end in spans:
                assert start == expected_start and end >= start
                expected_start = end + 1
            actual_lines = (live / name).read_bytes().count(b"\n")
            assert expected_start - 1 == actual_lines
            source_lines += actual_lines
        mapping_rows = sum(1 for _ in csv.DictReader(artifacts[0][0].open()))
        assert mapping_rows == len(parity["checks"])
        checklist = json.loads(artifacts[0][3].read_text())
        assert checklist["schema"] == "chirality-review-checklist/v1" and checklist["item_count"] == 1
        item = checklist["items"][0]
        assert item["id"] == "AC-001" and item["qualified_id"] == f"{did}-AC-001"
        assert item["text"] == seed["ac"] and item["output_refs"] == ["OUT-001"]
        assert item["verification"][0]["id"] == "VER-001" and item["verification"][0]["text"] == seed["ver"]
        assert item["source_identity"]["sha256"] == sha(candidate)
        html = artifacts[0][4].read_text().lower()
        assert sha(candidate) in html
        assert not re.search(r"<\s*(script|iframe|form)\b|(?:src|href)\s*=\s*[\"'](?:https?:)?//", html)

        partial = member / "negative-partial"
        copy_kit(live, partial)
        (partial / "Guidance.md").unlink()
        assert run(base + ["--deliverable", str(partial)], False).returncode != 0
        assert run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(a)], False).returncode != 0
        bad = member / "bad-checklist.json"
        assert run(["python3", str(TOOLS / "derive_review_checklist.py"), str(a), "--output", str(bad)], False).returncode != 0 and not bad.exists()
        legacy = member / "legacy-checklist.json"
        assert run(["python3", str(TOOLS / "derive_review_checklist.py"), str(live), "--output", str(legacy)], False).returncode != 0 and not legacy.exists()
        run([str(ROOT / "tools/validation/check_four_documents.sh"), str(live)])
        run(["python3", str(ROOT / "tools/validation/validate_dependencies_schema.py"), str(live / "Dependencies.csv")])

        candidate_hash = sha(candidate)
        replacement.append([did, "A", f"{row['live_path']}/ScopeOfWork.md", "ABSENT", candidate_hash])
        rollback.append([did, "D", f"{row['live_path']}/ScopeOfWork.md", candidate_hash, "ABSENT"])
        for name in FILES:
            replacement.append([did, "D", f"{row['live_path']}/{name}", row[hash_fields[name]], "ABSENT"])
            rollback.append([did, "A", f"{row['live_path']}/{name}", "ABSENT", row[hash_fields[name]]])
        sim = member / "simulation"
        copy_kit(live, sim)
        shutil.copy2(candidate, sim / "ScopeOfWork.md")
        for name in FILES:
            (sim / name).unlink()
        run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(sim)])
        (sim / "ScopeOfWork.md").unlink()
        for name in FILES:
            shutil.copy2(live / name, sim / name)
        legacy_result = json.loads(run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(sim)]).stdout)
        assert legacy_result["format"] == "LEGACY_FOUR_DOC"
        assert all(sha(sim / name) == row[field] for name, field in hash_fields.items())
        simulations.append([did, "PASS", "PASS", "PASS", "RUN_LOCAL_ONLY"])
        total_maps += mapping_rows
        total_lines += source_lines
        members.append([did, candidate_hash, mapping_rows, source_lines, len(author_sets[did]), len(verifier_sets[did]), "PASS", "PASS", "PASS", "PASS"])

    assert total_maps == 88 and total_lines == 727
    assert len(replacement) == len(rollback) == 15
    for forward, inverse in zip(replacement, rollback):
        assert forward[0] == inverse[0] and forward[2] == inverse[2]
        assert forward[1] != inverse[1] and forward[3] == inverse[4] and forward[4] == inverse[3]
    package_replacement = list(csv.reader((RUN / "snapshots/package/REPLACEMENT_MANIFEST.tsv").open(), delimiter="\t"))[1:]
    package_rollback = list(csv.reader((RUN / "snapshots/package/ROLLBACK_MANIFEST.tsv").open(), delimiter="\t"))[1:]
    assert replacement == package_replacement and rollback == package_rollback

    write_tsv(OUT / "MANIFEST_REHASH.tsv", ["manifest", "entries", "bytes", "verdict"], [[r["manifest"], r["entries"], r["bytes"], r["verdict"]] for r in manifest_results])
    write_tsv(OUT / "MEMBER_RESULTS.tsv", ["deliverable_id", "candidate_sha256", "mappings", "source_lines", "author_files", "verifier_files", "schema", "content_authority", "preservation", "substrate"], members)
    write_tsv(OUT / "REPLACEMENT_MANIFEST.tsv", ["deliverable_id", "operation", "path", "before_sha256", "after_sha256"], replacement)
    write_tsv(OUT / "ROLLBACK_MANIFEST.tsv", ["deliverable_id", "operation", "path", "before_sha256", "after_sha256"], rollback)
    write_tsv(OUT / "SIMULATION.tsv", ["deliverable_id", "apply", "target_validation", "rollback", "write_scope"], simulations)
    summary = {
        "status": "PASS", "basis": "main@ef461cfdb3a4b135dc670b04f646eca3eac47712",
        "members": 3, "mappings": total_maps, "source_lines": total_lines,
        "manifest_entries": {r["manifest"]: r["entries"] for r in manifest_results},
        "candidate_hashes": {row[0]: row[1] for row in members},
        "replacement_rows": 15, "rollback_rows": 15, "simulations": 3,
        "author_common_evidence_files": len(author_common),
        "author_member1_retained_failure_files": 4,
        "verifier_files_per_member": 103,
        "author_progress_rows": len(a_progress), "verifier_progress_rows": len(v_progress),
        "agent_2_session_surfaces": child_dirs,
        "native_token_telemetry": "UNAVAILABLE",
    }
    (OUT / "REPRODUCTION_SUMMARY.json").write_text(json.dumps(summary, indent=2) + "\n")
    shutil.rmtree(SCRATCH)
    write_manifest(OUT)
    write_manifest(RUN / "instances/RECON-EXP-PKG01")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
