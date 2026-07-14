#!/usr/bin/env python3
"""Reproduce PKG-02 experiment fan-in without writing project paths."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"
PARENT = RUN / "instances/WORKING-EXP-PKG02"
VERIFY = PARENT / "children/BATCH-VERIFY-PKG02"
SNAP = RUN / "snapshots/package"
REPRO = SNAP / "manager-reproduction"
TOOLS = ROOT / "tools/scope_of_work"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
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
EXPECTED = {
    "DEL-02-01": (35, 427),
    "DEL-02-02": (48, 419),
    "DEL-02-03": (29, 383),
    "DEL-02-04": (33, 369),
    "DEL-02-05": (41, 455),
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args: list[str], *, expect_success: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    if (result.returncode == 0) != expect_success:
        raise RuntimeError(
            f"unexpected exit {result.returncode}: {' '.join(args)}\n{result.stdout}\n{result.stderr}"
        )
    return result


def copy_kit(live: Path, target: Path) -> None:
    target.mkdir(parents=True, exist_ok=False)
    for name in FILES + CONTROL:
        shutil.copy2(live / name, target / name)


def extract_seed(evidence: Path) -> tuple[str, str, str]:
    text = evidence.read_text(encoding="utf-8")
    values = []
    for ident in ("OUT-001", "AC-001", "VER-001"):
        match = re.search(rf"^- \*\*{ident}\*\* — (.+)$", text, re.MULTILINE)
        if not match:
            raise AssertionError(f"missing {ident}: {evidence}")
        values.append(match.group(1))
    return values[0], values[1], values[2]


def write_tsv(path: Path, header: list[str], rows: list[list[str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def negative_command(args: list[str], record: Path) -> int:
    result = run(args, expect_success=False)
    record.write_text(
        json.dumps(
            {"args": args, "exit_code": result.returncode, "stdout": result.stdout, "stderr": result.stderr},
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    return result.returncode


def main() -> None:
    SNAP.mkdir(parents=True, exist_ok=True)
    if REPRO.exists():
        shutil.rmtree(REPRO)
    REPRO.mkdir()

    verifier_status = json.loads((VERIFY / "STATUS.json").read_text(encoding="utf-8"))
    assert verifier_status["status"] == "PASS_UNCHANGED"
    assert verifier_status["deliverables_complete"] == 5
    assert verifier_status["candidate_repairs"] == verifier_status["candidate_writes"] == 0

    frozen = list(csv.DictReader((PARENT / "FROZEN_INPUTS.tsv").open(newline=""), delimiter="\t"))
    assert [row["deliverable_id"] for row in frozen] == list(EXPECTED)
    replacements: list[list[str]] = []
    rollbacks: list[list[str]] = []
    members: list[list[str]] = []
    simulations: list[list[str]] = []
    negative_summary: dict[str, dict[str, int]] = {}

    for row in frozen:
        did = row["deliverable_id"]
        live = ROOT / row["live_path"]
        candidate = RUN / "candidates/PIP-PKG02" / did
        evidence = candidate / "evidence/ScopeOfWork.md"
        clean = candidate / "production/ScopeOfWork.md"
        final_report = candidate / "finalization.json"
        member = REPRO / did
        member.mkdir()
        a, b = member / "conversion-a", member / "conversion-b"
        copy_kit(live, a)
        copy_kit(live, b)
        out, ac, ver = extract_seed(evidence)
        base = [
            "python3",
            str(TOOLS / "convert_four_documents_to_scope_of_work.py"),
            "--deliverable-id",
            did,
            "--package-id",
            "PKG-02",
            "--decomposition-basis",
            row["decomposition_basis"],
        ]
        for value in row["scope_refs"].split(","):
            base += ["--project-scope-ref", value]
        for value in row["objective_refs"].split(","):
            base += ["--package-objective-ref", value]
        base += [
            "--output-description",
            out,
            "--acceptance-criterion",
            ac,
            "--verification-method",
            ver,
            "--isolated-migration",
            "--migration-authority",
            AUTH,
        ]
        for work in (a, b):
            run(base + ["--deliverable", str(work)])
        assert (a / "ScopeOfWork.md").read_bytes() == (b / "ScopeOfWork.md").read_bytes() == evidence.read_bytes()

        finals: list[tuple[Path, Path]] = []
        for label, source in (("a", a / "ScopeOfWork.md"), ("b", b / "ScopeOfWork.md")):
            out_dir = member / f"final-{label}"
            out_dir.mkdir()
            output = out_dir / "ScopeOfWork.md"
            report = out_dir / "finalization.json"
            run(
                [
                    "python3",
                    str(TOOLS / "finalize_scope_of_work.py"),
                    "--evidence-candidate",
                    str(source),
                    "--output",
                    str(output),
                    "--report",
                    str(report),
                ]
            )
            finals.append((output, report))
        assert finals[0][0].read_bytes() == finals[1][0].read_bytes() == clean.read_bytes()
        assert finals[0][1].read_bytes() == finals[1][1].read_bytes() == final_report.read_bytes()

        clean_validation = run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(clean)])
        (member / "validation-clean.json").write_text(clean_validation.stdout, encoding="utf-8")
        for label, work in (("a", a), ("b", b)):
            dual = run(
                [
                    "python3",
                    str(TOOLS / "validate_scope_of_work.py"),
                    "--isolated-migration",
                    "--migration-authority",
                    AUTH,
                    "--json",
                    str(work),
                ]
            )
            (member / f"validation-dual-{label}.json").write_text(dual.stdout, encoding="utf-8")

        for n in (1, 2):
            run(
                [
                    "python3",
                    str(TOOLS / "map_scope_of_work_claims.py"),
                    "--scope-of-work",
                    str(evidence),
                    "--production-scope-of-work",
                    str(clean),
                    "--source-dir",
                    str(live),
                    "--output-csv",
                    str(member / f"claim-map-{n}.csv"),
                ]
            )
            run(
                [
                    "python3",
                    str(TOOLS / "report_scope_of_work_parity.py"),
                    "--scope-of-work",
                    str(evidence),
                    "--production-scope-of-work",
                    str(clean),
                    "--source-dir",
                    str(live),
                    "--output-json",
                    str(member / f"parity-{n}.json"),
                    "--output-md",
                    str(member / f"parity-{n}.md"),
                    "--isolated-migration",
                    "--migration-authority",
                    AUTH,
                ]
            )
            run(
                [
                    "python3",
                    str(TOOLS / "derive_review_checklist.py"),
                    str(clean),
                    "--output",
                    str(member / f"checklist-{n}.json"),
                ]
            )
            run(
                [
                    "python3",
                    str(TOOLS / "render_scope_of_work.py"),
                    str(clean),
                    "--output",
                    str(member / f"render-{n}.html"),
                ]
            )
        for stem, suffix in (
            ("claim-map", ".csv"),
            ("parity", ".json"),
            ("parity", ".md"),
            ("checklist", ".json"),
            ("render", ".html"),
        ):
            assert (member / f"{stem}-1{suffix}").read_bytes() == (member / f"{stem}-2{suffix}").read_bytes()

        parity = json.loads((member / "parity-1.json").read_text(encoding="utf-8"))
        mappings, source_lines = EXPECTED[did]
        assert parity["pass"] and not parity["issues"] and len(parity["checks"]) == mappings
        assert sum(item["line_end"] - item["line_start"] + 1 for item in parity["checks"]) == source_lines
        assert parity["production_scope_of_work_sha256"] == sha(clean)
        checklist = json.loads((member / "checklist-1.json").read_text(encoding="utf-8"))
        assert checklist["source"]["sha256"] == sha(clean) and checklist["source"]["migration_authority"] is None

        negative: dict[str, int] = {}
        mutated = member / "mutated-clean.md"
        mutated.write_bytes(clean.read_bytes() + b"\n")
        bad_map = member / "bad-map.csv"
        negative["mutated_map"] = negative_command(
            [
                "python3",
                str(TOOLS / "map_scope_of_work_claims.py"),
                "--scope-of-work",
                str(evidence),
                "--production-scope-of-work",
                str(mutated),
                "--source-dir",
                str(live),
                "--output-csv",
                str(bad_map),
            ],
            member / "negative-mutated-map.json",
        )
        assert not bad_map.exists()
        bad_parity = member / "bad-parity.json"
        negative["mutated_parity"] = negative_command(
            [
                "python3",
                str(TOOLS / "report_scope_of_work_parity.py"),
                "--scope-of-work",
                str(evidence),
                "--production-scope-of-work",
                str(mutated),
                "--source-dir",
                str(live),
                "--output-json",
                str(bad_parity),
                "--isolated-migration",
                "--migration-authority",
                AUTH,
            ],
            member / "negative-mutated-parity.json",
        )
        assert bad_parity.exists()
        bad_parity_data = json.loads(bad_parity.read_text(encoding="utf-8"))
        assert not bad_parity_data["pass"] and bad_parity_data["issues"]
        evidence_checklist = member / "evidence-checklist.json"
        negative["evidence_checklist"] = negative_command(
            ["python3", str(TOOLS / "derive_review_checklist.py"), str(a), "--output", str(evidence_checklist)],
            member / "negative-evidence-checklist.json",
        )
        assert not evidence_checklist.exists()
        evidence_render = member / "evidence-render.html"
        negative["evidence_render"] = negative_command(
            ["python3", str(TOOLS / "render_scope_of_work.py"), str(a), "--output", str(evidence_render)],
            member / "negative-evidence-render.json",
        )
        assert not evidence_render.exists()
        partial = member / "negative-partial"
        copy_kit(live, partial)
        (partial / "Guidance.md").unlink()
        negative["partial_input"] = negative_command(
            base + ["--deliverable", str(partial)], member / "negative-partial.json"
        )
        assert not (partial / "ScopeOfWork.md").exists()
        negative["unauthorized_dual"] = negative_command(
            ["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(a)],
            member / "negative-unauthorized-dual.json",
        )
        wrong_checklist = member / "wrong-authority-checklist.json"
        negative["wrong_authority_checklist"] = negative_command(
            [
                "python3",
                str(TOOLS / "derive_review_checklist.py"),
                str(a),
                "--isolated-migration",
                "--migration-authority",
                "WRONG",
                "--output",
                str(wrong_checklist),
            ],
            member / "negative-wrong-authority-checklist.json",
        )
        assert not wrong_checklist.exists() and all(value != 0 for value in negative.values())
        negative_summary[did] = negative

        run([str(ROOT / "tools/validation/check_four_documents.sh"), str(live)])
        run(["python3", str(ROOT / "tools/validation/validate_dependencies_schema.py"), str(live / "Dependencies.csv")])
        for name, column in HASH_COLS.items():
            assert sha(live / name) == row[column]
        assert not (live / "ScopeOfWork.md").exists()

        clean_hash = sha(clean)
        replacements.append([did, "A", f"{row['live_path']}/ScopeOfWork.md", "ABSENT", clean_hash])
        rollbacks.append([did, "D", f"{row['live_path']}/ScopeOfWork.md", clean_hash, "ABSENT"])
        for name in FILES:
            source_hash = row[HASH_COLS[name]]
            replacements.append([did, "D", f"{row['live_path']}/{name}", source_hash, "ABSENT"])
            rollbacks.append([did, "A", f"{row['live_path']}/{name}", "ABSENT", source_hash])

        with tempfile.TemporaryDirectory(prefix=f"{did}-", dir=SNAP) as temp:
            sim = Path(temp) / did
            shutil.copytree(live, sim)
            shutil.copy2(clean, sim / "ScopeOfWork.md")
            for name in FILES:
                (sim / name).unlink()
            run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(sim)])
            target_hash = sha(sim / "ScopeOfWork.md")
            assert target_hash == clean_hash
            (sim / "ScopeOfWork.md").unlink()
            for name in FILES:
                shutil.copy2(live / name, sim / name)
            run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(sim)])
            assert all(sha(sim / name) == row[HASH_COLS[name]] for name in FILES)
            simulations.append([did, "PASS", "PASS", "PASS", "no project write"])

        members.append(
            [
                did,
                "PASS_WITH_RETAINED_PROCESS_FINDINGS" if did == "DEL-02-01" else "PASS",
                "PASS_UNCHANGED_WITH_3_RETAINED_RETRIES" if did == "DEL-02-01" else "PASS_UNCHANGED",
                sha(evidence),
                clean_hash,
                sha(final_report),
                str(mappings),
                str(source_lines),
                "5",
                "PASS",
            ]
        )

    assert len(replacements) == len(rollbacks) == 25
    for forward, inverse in zip(replacements, rollbacks):
        assert forward[0] == inverse[0] and forward[2] == inverse[2]
        assert forward[1] != inverse[1] and forward[3] == inverse[4] and forward[4] == inverse[3]

    write_tsv(
        SNAP / "MEMBER_RESULTS.tsv",
        [
            "deliverable_id",
            "author_status",
            "verifier_status",
            "evidence_sha256",
            "clean_sha256",
            "finalization_report_sha256",
            "mapping_rows",
            "source_lines",
            "replacement_rows",
            "manager_reproduction",
        ],
        members,
    )
    write_tsv(
        SNAP / "REPLACEMENT_MANIFEST.tsv",
        ["deliverable_id", "operation", "path", "before_sha256", "after_sha256"],
        replacements,
    )
    write_tsv(
        SNAP / "ROLLBACK_MANIFEST.tsv",
        ["deliverable_id", "operation", "path", "before_sha256", "after_sha256"],
        rollbacks,
    )
    write_tsv(
        SNAP / "SIMULATION.tsv",
        ["deliverable_id", "apply", "target_validation", "rollback", "write_scope"],
        simulations,
    )

    portability_rows: list[list[str]] = []
    root_bytes = str(ROOT).encode("utf-8")
    for path in sorted(item for item in REPRO.rglob("*") if item.is_file()):
        content = path.read_bytes()
        count = content.count(root_bytes)
        if count:
            path.write_bytes(content.replace(root_bytes, b"{REPO_ROOT}"))
            portability_rows.append([path.relative_to(ROOT).as_posix(), str(count), "{REPO_ROOT}", "PASS_REVERSIBLE"])
    write_tsv(
        SNAP / "PORTABILITY.tsv",
        ["path", "replacements", "replacement_token", "verdict"],
        portability_rows,
    )
    summary = {
        "status": "PASS",
        "members": 5,
        "mapping_rows": 186,
        "source_lines": 2053,
        "negative_checks": negative_summary,
        "negative_check_count": sum(len(item) for item in negative_summary.values()),
        "replacement_rows": len(replacements),
        "rollback_rows": len(rollbacks),
        "apply_rollback_simulations": len(simulations),
        "live_four_document_checks": "5/5 PASS",
        "dependency_schema_checks": "5/5 PASS",
        "generated_portability_files_normalized": len(portability_rows),
        "generated_portability_replacements": sum(int(row[1]) for row in portability_rows),
        "dec_025": "NOT_APPLICABLE_NO_PROJECT_CODE_PATH_CHANGE",
    }
    (SNAP / "MANAGER_REPRODUCTION.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
