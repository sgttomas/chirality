#!/usr/bin/env python3
"""Deterministically reproduce PKG-01 experiment fan-in without project writes."""

from __future__ import annotations

import csv
import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG01-BATCH-EXPERIMENT-20260713-01"
PARENT = RUN / "instances/WORKING-EXP-PKG01"
VERIFY = PARENT / "children/BATCH-VERIFY-PKG01"
SNAP = RUN / "snapshots/package"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
BASIS = "projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@69ac259a7113d5a838fb22aa2e84df0e0f109713"
TOOLS = ROOT / "tools/scope_of_work"
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


def run(args: list[str], *, expect: int = 0) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    if (result.returncode == 0) != (expect == 0):
        raise RuntimeError(f"unexpected exit {result.returncode}: {' '.join(args)}\n{result.stdout}\n{result.stderr}")
    return result


def copy_kit(live: Path, target: Path) -> None:
    target.mkdir(parents=True)
    for name in FILES + CONTROL:
        shutil.copy2(live / name, target / name)


def main() -> None:
    SNAP.mkdir(parents=True, exist_ok=True)
    reproduction = SNAP / "manager-reproduction"
    if reproduction.exists():
        shutil.rmtree(reproduction)
    reproduction.mkdir()

    status = json.loads((VERIFY / "STATUS.json").read_text())
    assert status["status"] == "PASS_UNCHANGED" and status["script_orchestration_restarts"] == 1

    manifest = list(csv.DictReader((VERIFY / "MANIFEST.tsv").open(), delimiter="\t"))
    assert len(manifest) == 317
    assert all(not row["path"].endswith("/MANIFEST.tsv") for row in manifest)
    for row in manifest:
        path = ROOT / row["path"].removeprefix("{REPO_ROOT}/")
        assert sha(path) == row["sha256"]
        assert path.stat().st_size == int(row["bytes"])

    evidence_counts = {}
    for did in SEEDS:
        evidence_counts[did] = sum(1 for path in (VERIFY / "members" / did).rglob("*") if path.is_file())
        assert evidence_counts[did] == 103

    progress = list(csv.DictReader((VERIFY / "PROGRESS.tsv").open(), delimiter="\t"))
    assert len(progress) == 33
    assert sum(row["deliverable_id"] == "DEL-01-02" for row in progress) == 15
    assert sum(row["deliverable_id"] == "DEL-01-03" for row in progress) == 9
    assert sum(row["deliverable_id"] == "DEL-01-04" for row in progress) == 9
    assert any(row["stage"] == "evidence_correction_001" and row["retries"] == "1" for row in progress)

    frozen = list(csv.DictReader((PARENT / "FROZEN_INPUTS.tsv").open(), delimiter="\t"))
    replacements: list[list[str]] = []
    rollbacks: list[list[str]] = []
    members: list[list[str]] = []
    simulations: list[list[str]] = []
    negative_summary = {}

    for row in frozen:
        did = row["deliverable_id"]
        live = ROOT / row["live_path"]
        candidate = RUN / f"candidates/PIP-PKG01/{did}/ScopeOfWork.md"
        member = reproduction / did
        a, b = member / "conversion-a", member / "conversion-b"
        copy_kit(live, a)
        copy_kit(live, b)
        seed = SEEDS[did]
        base = [
            "python3", str(TOOLS / "convert_four_documents_to_scope_of_work.py"),
            "--deliverable-id", did, "--package-id", "PKG-01",
            "--decomposition-basis", BASIS,
        ]
        for value in seed["scopes"]:
            base += ["--project-scope-ref", value]
        for value in seed["objectives"]:
            base += ["--package-objective-ref", value]
        base += [
            "--output-description", seed["out"], "--acceptance-criterion", seed["ac"],
            "--verification-method", seed["ver"], "--isolated-migration", "--migration-authority", AUTH,
        ]
        for work in (a, b):
            run(base + ["--deliverable", str(work)])
        assert (a / "ScopeOfWork.md").read_bytes() == (b / "ScopeOfWork.md").read_bytes() == candidate.read_bytes()

        validation = run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(candidate)])
        (member / "validation-sow-v1.json").write_text(validation.stdout)
        for work, suffix in ((a, "a"), (b, "b")):
            dual = run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--isolated-migration", "--migration-authority", AUTH, "--json", str(work)])
            (member / f"validation-dual-{suffix}.json").write_text(dual.stdout)

        for n in (1, 2):
            run(["python3", str(TOOLS / "map_scope_of_work_claims.py"), "--scope-of-work", str(candidate), "--source-dir", str(live), "--output-csv", str(member / f"claim-map-{n}.csv")])
            run(["python3", str(TOOLS / "report_scope_of_work_parity.py"), "--scope-of-work", str(candidate), "--source-dir", str(live), "--output-json", str(member / f"parity-{n}.json"), "--output-md", str(member / f"parity-{n}.md"), "--isolated-migration", "--migration-authority", AUTH])
            run(["python3", str(TOOLS / "derive_review_checklist.py"), str(candidate), "--output", str(member / f"checklist-{n}.json")])
            run(["python3", str(TOOLS / "render_scope_of_work.py"), str(candidate), "--output", str(member / f"render-{n}.html")])
        for stem, suffix in (("claim-map", ".csv"), ("parity", ".json"), ("parity", ".md"), ("checklist", ".json"), ("render", ".html")):
            assert (member / f"{stem}-1{suffix}").read_bytes() == (member / f"{stem}-2{suffix}").read_bytes()

        partial = member / "negative-partial"
        copy_kit(live, partial)
        (partial / "Guidance.md").unlink()
        negative = {}
        negative["partial_conversion"] = subprocess.run(base + ["--deliverable", str(partial)], cwd=ROOT, capture_output=True).returncode
        negative["unauthorized_dual_validation"] = subprocess.run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(a)], cwd=ROOT, capture_output=True).returncode
        bad_checklist = member / "unauthorized-checklist.json"
        negative["unauthorized_dual_checklist"] = subprocess.run(["python3", str(TOOLS / "derive_review_checklist.py"), str(a), "--output", str(bad_checklist)], cwd=ROOT, capture_output=True).returncode
        legacy_checklist = member / "legacy-checklist.json"
        negative["legacy_checklist"] = subprocess.run(["python3", str(TOOLS / "derive_review_checklist.py"), str(live), "--output", str(legacy_checklist)], cwd=ROOT, capture_output=True).returncode
        assert all(code != 0 for code in negative.values()) and not bad_checklist.exists() and not legacy_checklist.exists()
        negative_summary[did] = negative

        run([str(ROOT / "tools/validation/check_four_documents.sh"), str(live)])
        run(["python3", str(ROOT / "tools/validation/validate_dependencies_schema.py"), str(live / "Dependencies.csv")])

        source_hashes = {
            "Datasheet.md": row["datasheet_sha256"], "Specification.md": row["specification_sha256"],
            "Guidance.md": row["guidance_sha256"], "Procedure.md": row["procedure_sha256"],
        }
        for name, expected in source_hashes.items():
            assert sha(live / name) == expected
        assert sha(live / "_STATUS.md") == row["status_sha256"] and not (live / "ScopeOfWork.md").exists()

        cand_hash = sha(candidate)
        replacements.append([did, "A", f"{row['live_path']}/ScopeOfWork.md", "ABSENT", cand_hash])
        rollbacks.append([did, "D", f"{row['live_path']}/ScopeOfWork.md", cand_hash, "ABSENT"])
        for name in FILES:
            replacements.append([did, "D", f"{row['live_path']}/{name}", source_hashes[name], "ABSENT"])
            rollbacks.append([did, "A", f"{row['live_path']}/{name}", "ABSENT", source_hashes[name]])

        with tempfile.TemporaryDirectory(prefix=f"{did}-", dir=SNAP) as temp:
            sim = Path(temp) / did
            shutil.copytree(live, sim)
            shutil.copy2(candidate, sim / "ScopeOfWork.md")
            for name in FILES:
                (sim / name).unlink()
            run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(sim)])
            (sim / "ScopeOfWork.md").unlink()
            for name in FILES:
                shutil.copy2(live / name, sim / name)
            run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(sim)])
            assert all(sha(sim / name) == source_hashes[name] for name in FILES)
            simulations.append([did, "PASS", "PASS", "PASS", "no project write"])

        parity = json.loads((member / "parity-1.json").read_text())
        mapping_rows = sum(1 for _ in csv.DictReader((member / "claim-map-1.csv").open()))
        source_lines = sum(int(item["line_end"]) - int(item["line_start"]) + 1 for item in parity["checks"])
        members.append([did, "PASS_ACCEPTED_WITH_ONE_SETUP_RETRY" if did == "DEL-01-02" else "PASS_ACCEPTED", "PASS_UNCHANGED_WITH_ONE_CONTAINED_SUBSTRATE_RESTART" if did == "DEL-01-02" else "PASS_UNCHANGED", cand_hash, str(mapping_rows), str(source_lines), "5", "PASS", "PASS", "PASS", "PASS"])

    assert len(replacements) == len(rollbacks) == 15
    for replacement, rollback in zip(replacements, rollbacks):
        assert replacement[0] == rollback[0] and replacement[2] == rollback[2]
        assert replacement[1] != rollback[1] and replacement[3] == rollback[4] and replacement[4] == rollback[3]

    def write_tsv(path: Path, header: list[str], rows: list[list[str]]) -> None:
        with path.open("w", newline="") as handle:
            writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
            writer.writerow(header)
            writer.writerows(rows)

    write_tsv(SNAP / "MEMBER_RESULTS.tsv", ["deliverable_id", "author_status", "verifier_status", "candidate_sha256", "mapping_rows", "source_lines", "replacement_rows", "schema", "content_authority", "preservation", "execution_substrate"], members)
    write_tsv(SNAP / "REPLACEMENT_MANIFEST.tsv", ["deliverable_id", "operation", "path", "before_sha256", "after_sha256"], replacements)
    write_tsv(SNAP / "ROLLBACK_MANIFEST.tsv", ["deliverable_id", "operation", "path", "before_sha256", "after_sha256"], rollbacks)
    write_tsv(SNAP / "SIMULATION.tsv", ["deliverable_id", "apply", "target_validation", "rollback", "write_scope"], simulations)
    portability_rows: list[list[str]] = []
    root_bytes = str(ROOT).encode()
    for path in sorted(item for item in reproduction.rglob("*") if item.is_file()):
        content = path.read_bytes()
        count = content.count(root_bytes)
        if count:
            path.write_bytes(content.replace(root_bytes, b"{REPO_ROOT}"))
            portability_rows.append([str(path.relative_to(ROOT)), str(count), "{REPO_ROOT}", "PASS_REVERSIBLE"])
    write_tsv(SNAP / "PORTABILITY.tsv", ["path", "replacements", "replacement_token", "verdict"], portability_rows)
    summary = {
        "status": "PASS",
        "verifier_manifest_entries": len(manifest),
        "verifier_evidence_files_per_member": evidence_counts,
        "progress_rows": len(progress),
        "author_retry": "one failed-before-output authority-token mismatch; versioned amendment; no weakened check",
        "verifier_restart": "one contained local shell-quote harness restart; append-only evidence correction; fresh rerun",
        "members": len(members),
        "mapping_rows": sum(int(row[4]) for row in members),
        "source_lines": sum(int(row[5]) for row in members),
        "replacement_rows": len(replacements),
        "rollback_rows": len(rollbacks),
        "apply_rollback_simulations": len(simulations),
        "negative_checks": negative_summary,
        "live_four_document_checks": "3/3 PASS",
        "dependency_schema_checks": "3/3 PASS",
        "generated_portability_files_normalized": len(portability_rows),
        "generated_portability_replacements": sum(int(row[1]) for row in portability_rows),
        "dec_025": "NOT_APPLICABLE_NO_PROJECT_CODE_PATH_CHANGE",
    }
    (SNAP / "MANAGER_REPRODUCTION.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
