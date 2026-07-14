#!/usr/bin/env python3
"""Prepare the exact eight-member clean Piping adoption package."""

from __future__ import annotations

import csv
import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PACKAGE-BATCH-ADOPTION-20260714-01"
INSTANCE = RUN / "instances/WORKING-BATCH-ADOPTION"
SNAP = RUN / "snapshots/package"
CAND = RUN / "candidates"
TOOLS = ROOT / "tools/scope_of_work"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
BASIS = "98af1a4bde875a0c2d5878d62fc84b3c1d7506c4"
PKG01_RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG01-BATCH-EXPERIMENT-20260713-01"
PKG02_RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"
FILES = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROL = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
HASH_COLS = {
    "Datasheet.md": "datasheet_sha256",
    "Specification.md": "specification_sha256",
    "Guidance.md": "guidance_sha256",
    "Procedure.md": "procedure_sha256",
    "_STATUS.md": "status_sha256",
    "_CONTEXT.md": "context_sha256",
    "_REFERENCES.md": "references_sha256",
    "_DEPENDENCIES.md": "dependencies_md_sha256",
    "Dependencies.csv": "dependencies_csv_sha256",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError(f"failed {result.returncode}: {' '.join(args)}\n{result.stdout}\n{result.stderr}")
    return result


def copy_kit(live: Path, target: Path) -> None:
    target.mkdir(parents=True, exist_ok=False)
    for name in FILES + CONTROL:
        shutil.copy2(live / name, target / name)


def write_tsv(path: Path, header: list[str], rows: list[list[str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def load_rows(path: Path, package: str) -> list[dict[str, str]]:
    rows = list(csv.DictReader(path.open(newline=""), delimiter="\t"))
    for row in rows:
        row["package_id"] = package
    return rows


def main() -> None:
    head = run(["git", "rev-parse", "HEAD"]).stdout.strip()
    branch = run(["git", "rev-parse", "--abbrev-ref", "HEAD"]).stdout.strip()
    assert head == BASIS and branch == "codex/adopt-pkg-batch-workflow"

    rows = load_rows(
        PKG01_RUN / "instances/WORKING-EXP-PKG01/FROZEN_INPUTS.tsv", "PKG-01"
    ) + load_rows(
        PKG02_RUN / "instances/WORKING-EXP-PKG02/FROZEN_INPUTS.tsv", "PKG-02"
    )
    assert [row["deliverable_id"] for row in rows] == [
        "DEL-01-02", "DEL-01-03", "DEL-01-04",
        "DEL-02-01", "DEL-02-02", "DEL-02-03", "DEL-02-04", "DEL-02-05",
    ]
    if (INSTANCE / "members").exists():
        shutil.rmtree(INSTANCE / "members")
    if CAND.exists():
        shutil.rmtree(CAND)
    (INSTANCE / "members").mkdir(parents=True)
    CAND.mkdir(parents=True)

    frozen_rows: list[list[str]] = []
    results: list[list[str]] = []
    replacements: list[list[str]] = []
    rollbacks: list[list[str]] = []
    simulations: list[list[str]] = []
    total_mappings = 0
    total_lines = 0

    for sequence, row in enumerate(rows, start=1):
        did = row["deliverable_id"]
        package = row["package_id"]
        live = ROOT / row["live_path"]
        assert row["lifecycle"] == "IN_PROGRESS" and row["live_format"] == "LEGACY_FOUR_DOC"
        for name, column in HASH_COLS.items():
            assert sha(live / name) == row[column], (did, name)
        assert not (live / "ScopeOfWork.md").exists()
        assert sum(1 for _ in csv.DictReader((live / "Dependencies.csv").open(newline=""))) == int(row["dependency_rows"])

        if package == "PKG-01":
            accepted_evidence = PKG01_RUN / f"candidates/PIP-PKG01/{did}/ScopeOfWork.md"
            accepted_clean = None
            accepted_report = None
        else:
            accepted_evidence = PKG02_RUN / f"candidates/PIP-PKG02/{did}/evidence/ScopeOfWork.md"
            accepted_clean = PKG02_RUN / f"candidates/PIP-PKG02/{did}/production/ScopeOfWork.md"
            accepted_report = PKG02_RUN / f"candidates/PIP-PKG02/{did}/finalization.json"

        member = INSTANCE / "members" / did
        member.mkdir()
        target = CAND / f"PIP-{package}" / did
        evidence_target = target / "evidence/ScopeOfWork.md"
        clean_target = target / "production/ScopeOfWork.md"
        report_target = target / "finalization.json"
        evidence_target.parent.mkdir(parents=True)
        clean_target.parent.mkdir(parents=True)
        shutil.copy2(accepted_evidence, evidence_target)

        final_pairs = []
        for label in ("a", "b"):
            out = member / f"final-{label}/ScopeOfWork.md"
            report = member / f"final-{label}/finalization.json"
            out.parent.mkdir()
            run([
                "python3", str(TOOLS / "finalize_scope_of_work.py"),
                "--evidence-candidate", str(evidence_target),
                "--output", str(out), "--report", str(report),
            ])
            final_pairs.append((out, report))
        assert final_pairs[0][0].read_bytes() == final_pairs[1][0].read_bytes()
        assert final_pairs[0][1].read_bytes() == final_pairs[1][1].read_bytes()
        shutil.copy2(final_pairs[0][0], clean_target)
        shutil.copy2(final_pairs[0][1], report_target)
        if accepted_clean is not None:
            assert clean_target.read_bytes() == accepted_clean.read_bytes()
            assert report_target.read_bytes() == accepted_report.read_bytes()

        report_data = json.loads(report_target.read_text(encoding="utf-8"))
        assert report_data["schema"] == "chirality-sow-finalization/v1"
        assert report_data["evidence_candidate_sha256"] == sha(evidence_target)
        assert report_data["production_scope_of_work_sha256"] == sha(clean_target)
        assert report_data["migration_control"]["migration-authority"] == AUTH
        lower = clean_target.read_bytes().lower()
        assert not any(token in lower for token in [
            b"sow-source-begin", b"sow-source-end", b"migration-authority:",
            b"pilot-variance:", b"issued-preparation-", b"migration candidate",
        ])

        dual = member / "dual-workspace"
        copy_kit(live, dual)
        shutil.copy2(evidence_target, dual / "ScopeOfWork.md")
        dual_validation = run([
            "python3", str(TOOLS / "validate_scope_of_work.py"),
            "--isolated-migration", "--migration-authority", AUTH, "--json", str(dual),
        ])
        (member / "validation-dual.json").write_text(dual_validation.stdout, encoding="utf-8")
        clean_validation = run([
            "python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(clean_target)
        ])
        (member / "validation-clean.json").write_text(clean_validation.stdout, encoding="utf-8")

        for n in (1, 2):
            run([
                "python3", str(TOOLS / "map_scope_of_work_claims.py"),
                "--scope-of-work", str(evidence_target),
                "--production-scope-of-work", str(clean_target),
                "--source-dir", str(live),
                "--output-csv", str(member / f"claim-map-{n}.csv"),
            ])
            run([
                "python3", str(TOOLS / "report_scope_of_work_parity.py"),
                "--scope-of-work", str(evidence_target),
                "--production-scope-of-work", str(clean_target),
                "--source-dir", str(live),
                "--output-json", str(member / f"parity-{n}.json"),
                "--output-md", str(member / f"parity-{n}.md"),
                "--isolated-migration", "--migration-authority", AUTH,
            ])
            run([
                "python3", str(TOOLS / "derive_review_checklist.py"), str(clean_target),
                "--output", str(member / f"checklist-{n}.json"),
            ])
            run([
                "python3", str(TOOLS / "render_scope_of_work.py"), str(clean_target),
                "--output", str(member / f"render-{n}.html"),
            ])
        for stem, suffix in [
            ("claim-map", ".csv"), ("parity", ".json"), ("parity", ".md"),
            ("checklist", ".json"), ("render", ".html"),
        ]:
            assert (member / f"{stem}-1{suffix}").read_bytes() == (member / f"{stem}-2{suffix}").read_bytes()
        parity = json.loads((member / "parity-1.json").read_text(encoding="utf-8"))
        assert parity["pass"] and not parity["issues"]
        mappings = len(parity["checks"])
        source_lines = sum(item["line_end"] - item["line_start"] + 1 for item in parity["checks"])
        assert parity["production_scope_of_work_sha256"] == sha(clean_target)
        checklist = json.loads((member / "checklist-1.json").read_text(encoding="utf-8"))
        assert checklist["source"]["sha256"] == sha(clean_target)
        assert checklist["source"]["migration_authority"] is None

        run([str(ROOT / "tools/validation/check_four_documents.sh"), str(live)])
        run(["python3", str(ROOT / "tools/validation/validate_dependencies_schema.py"), str(live / "Dependencies.csv")])
        for name, column in HASH_COLS.items():
            assert sha(live / name) == row[column]

        clean_hash = sha(clean_target)
        replacements.append([did, "A", f"{row['live_path']}/ScopeOfWork.md", "ABSENT", clean_hash])
        rollbacks.append([did, "D", f"{row['live_path']}/ScopeOfWork.md", clean_hash, "ABSENT"])
        for name in FILES:
            source_hash = row[HASH_COLS[name]]
            replacements.append([did, "D", f"{row['live_path']}/{name}", source_hash, "ABSENT"])
            rollbacks.append([did, "A", f"{row['live_path']}/{name}", "ABSENT", source_hash])

        with tempfile.TemporaryDirectory(prefix=f"{did}-", dir=SNAP) as temp:
            sim = Path(temp) / did
            shutil.copytree(live, sim)
            shutil.copy2(clean_target, sim / "ScopeOfWork.md")
            for name in FILES:
                (sim / name).unlink()
            run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(sim)])
            assert sha(sim / "ScopeOfWork.md") == clean_hash
            (sim / "ScopeOfWork.md").unlink()
            for name in FILES:
                shutil.copy2(live / name, sim / name)
            run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(sim)])
            assert all(sha(sim / name) == row[HASH_COLS[name]] for name in FILES)
        simulations.append([did, "PASS", "PASS", "PASS", "scratch only"])

        total_mappings += mappings
        total_lines += source_lines
        frozen_rows.append([
            str(sequence), package, did, row["live_path"], row["scope_refs"], row["objective_refs"],
            row["decomposition_basis"], *[row[HASH_COLS[name]] for name in FILES + CONTROL],
            row["dependency_rows"], "PASS",
        ])
        results.append([
            package, did, sha(evidence_target), clean_hash, sha(report_target),
            str(mappings), str(source_lines), "PASS", "PASS", "PASS",
        ])

    assert len(replacements) == len(rollbacks) == 40
    for forward, inverse in zip(replacements, rollbacks):
        assert forward[0] == inverse[0] and forward[2] == inverse[2]
        assert forward[1] != inverse[1]
        assert forward[3] == inverse[4] and forward[4] == inverse[3]
    assert total_mappings == 274 and total_lines == 2780

    write_tsv(INSTANCE / "FROZEN_INPUTS.tsv", [
        "sequence", "package_id", "deliverable_id", "live_path", "scope_refs", "objective_refs",
        "decomposition_basis", *[f"{name}_sha256" for name in FILES + CONTROL],
        "dependency_rows", "preflight",
    ], frozen_rows)
    write_tsv(SNAP / "MEMBER_RESULTS.tsv", [
        "package_id", "deliverable_id", "evidence_sha256", "clean_sha256", "report_sha256",
        "mappings", "source_lines", "finalization", "production_bound_evidence", "live_recheck",
    ], results)
    write_tsv(SNAP / "REPLACEMENT_MANIFEST.tsv", [
        "deliverable_id", "operation", "path", "before_sha256", "after_sha256",
    ], replacements)
    write_tsv(SNAP / "ROLLBACK_MANIFEST.tsv", [
        "deliverable_id", "operation", "path", "before_sha256", "after_sha256",
    ], rollbacks)
    write_tsv(SNAP / "SIMULATION.tsv", [
        "deliverable_id", "apply", "target_validation", "rollback", "write_scope",
    ], simulations)
    summary = {
        "schema": "chirality-sow-batch-adoption-package/v1",
        "status": "PASS",
        "basis": BASIS,
        "members": 8,
        "pkg01_members": 3,
        "pkg02_members": 5,
        "mappings": total_mappings,
        "source_lines": total_lines,
        "live_bindings": 72,
        "replacement_rows": 40,
        "rollback_rows": 40,
        "simulations": 8,
        "project_writes": 0,
        "blockers": [], "waivers": [], "unknowns": [], "reruns_required": [],
    }
    (SNAP / "PACKAGE_SUMMARY.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
