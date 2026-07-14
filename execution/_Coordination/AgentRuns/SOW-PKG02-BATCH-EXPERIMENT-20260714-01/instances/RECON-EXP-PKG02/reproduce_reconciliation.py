#!/usr/bin/env python3
"""Independent narrowed-profile reconciliation of the PKG-02 batch experiment."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01"
PARENT = RUN / "instances/WORKING-EXP-PKG02"
AUTHOR = PARENT / "children/BATCH-AUTHOR-PKG02"
VERIFY = PARENT / "children/BATCH-VERIFY-PKG02"
PACKAGE = RUN / "snapshots/package"
OUT = RUN / "snapshots/reconciliation"
SCRATCH = OUT / "reproduction"
TOOLS = ROOT / "tools/scope_of_work"
AUTHORITY = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
DOCS = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROL = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
EXPECTED = {
    "DEL-02-01": (35, 427), "DEL-02-02": (48, 419), "DEL-02-03": (29, 383),
    "DEL-02-04": (33, 369), "DEL-02-05": (41, 455),
}
REPRODUCE = {"DEL-02-01": "EXCEPTION", "DEL-02-05": "FINAL_CLEAN"}
HASH_FIELDS = {
    "Datasheet.md": "datasheet_sha256", "Specification.md": "specification_sha256",
    "Guidance.md": "guidance_sha256", "Procedure.md": "procedure_sha256",
    "_STATUS.md": "status_sha256", "_CONTEXT.md": "context_sha256",
    "_REFERENCES.md": "references_sha256", "_DEPENDENCIES.md": "dependencies_md_sha256",
    "Dependencies.csv": "dependencies_csv_sha256",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args: list[str], success: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    if (result.returncode == 0) != success:
        raise AssertionError(f"unexpected exit {result.returncode}: {' '.join(args)}\n{result.stdout}\n{result.stderr}")
    return result


def copy_kit(source: Path, target: Path) -> None:
    target.mkdir(parents=True)
    for name in DOCS + CONTROL:
        shutil.copy2(source / name, target / name)


def write_tsv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def write_manifest(root: Path) -> None:
    rows = []
    for path in sorted(p for p in root.rglob("*") if p.is_file() and p.name != "MANIFEST.tsv"):
        data = path.read_bytes()
        rows.append(["{REPO_ROOT}/" + str(path.relative_to(ROOT)), sha(path), len(data), len(data.splitlines())])
    write_tsv(root / "MANIFEST.tsv", ["path", "sha256", "bytes", "lines"], rows)


def resolve_manifest_path(raw: str) -> Path:
    if raw.startswith("{REPO_ROOT}/"):
        rel = raw.removeprefix("{REPO_ROOT}/")
    else:
        rel = raw
    candidate = (ROOT / rel).resolve()
    candidate.relative_to(ROOT.resolve())
    return candidate


def verify_manifest(label: str, path: Path, expected_rows: int) -> list[object]:
    rows = list(csv.DictReader(path.open(newline="", encoding="utf-8"), delimiter="\t"))
    assert len(rows) == expected_rows
    assert len({row["path"] for row in rows}) == len(rows)
    assert str(path.relative_to(ROOT)) not in {r["path"].removeprefix("{REPO_ROOT}/") for r in rows}
    portable = sum(row["path"].startswith("{REPO_ROOT}/") for row in rows)
    assert portable in (0, len(rows))
    total_bytes = 0
    for row in rows:
        actual = resolve_manifest_path(row["path"])
        assert actual.is_file() and sha(actual) == row["sha256"]
        assert actual.stat().st_size == int(row["bytes"])
        if row.get("lines") and actual.suffix != ".pyc":
            assert len(actual.read_bytes().splitlines()) == int(row["lines"])
        elif actual.suffix == ".pyc":
            # Retained verifier-manifest variance: a binary cache file has a
            # byte-newline-derived line field, which is not semantically useful.
            assert actual.name == "verifier.cpython-313.pyc" and int(row["lines"]) == 123
        total_bytes += int(row["bytes"])
    return [label, len(rows), total_bytes, sha(path), "ROOT_TOKEN" if portable else "REPO_RELATIVE", "PASS"]


def extract_seed(evidence: Path) -> tuple[str, str, str]:
    text = evidence.read_text(encoding="utf-8")
    values = []
    for ident in ("OUT-001", "AC-001", "VER-001"):
        match = re.search(rf"^- \*\*{ident}\*\* — (.+)$", text, re.MULTILINE)
        assert match
        values.append(match.group(1))
    return values[0], values[1], values[2]


def conversion_command(did: str, row: dict[str, str], evidence: Path) -> list[str]:
    out, acceptance, verification = extract_seed(evidence)
    args = ["python3", str(TOOLS / "convert_four_documents_to_scope_of_work.py"),
            "--deliverable-id", did, "--package-id", "PKG-02",
            "--decomposition-basis", row["decomposition_basis"]]
    for value in row["scope_refs"].split(","):
        args += ["--project-scope-ref", value]
    for value in row["objective_refs"].split(","):
        args += ["--package-objective-ref", value]
    return args + ["--output-description", out, "--acceptance-criterion", acceptance,
                   "--verification-method", verification, "--isolated-migration",
                   "--migration-authority", AUTHORITY]


def full_reproduce(did: str, row: dict[str, str], live: Path, evidence: Path,
                   clean: Path, report: Path) -> list[object]:
    member = SCRATCH / did
    a, b = member / "conversion-a", member / "conversion-b"
    copy_kit(live, a); copy_kit(live, b)
    base = conversion_command(did, row, evidence)
    for work in (a, b):
        run(base + ["--deliverable", str(work)])
    assert (a / "ScopeOfWork.md").read_bytes() == (b / "ScopeOfWork.md").read_bytes() == evidence.read_bytes()
    finals = []
    for label, work in (("a", a), ("b", b)):
        final_dir = member / f"final-{label}"; final_dir.mkdir()
        final = final_dir / "ScopeOfWork.md"; final_report = final_dir / "finalization.json"
        run(["python3", str(TOOLS / "finalize_scope_of_work.py"), "--evidence-candidate",
             str(work / "ScopeOfWork.md"), "--output", str(final), "--report", str(final_report)])
        finals.append((final, final_report))
    assert finals[0][0].read_bytes() == finals[1][0].read_bytes() == clean.read_bytes()
    assert finals[0][1].read_bytes() == finals[1][1].read_bytes() == report.read_bytes()
    clean_result = json.loads(run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(clean)]).stdout)
    assert clean_result["format"] == "SOW_V1"
    artifacts = []
    for n in (1, 2):
        cmap, parity, parity_md = member / f"claim-map-{n}.csv", member / f"parity-{n}.json", member / f"parity-{n}.md"
        checklist, render = member / f"checklist-{n}.json", member / f"render-{n}.html"
        run(["python3", str(TOOLS / "map_scope_of_work_claims.py"), "--scope-of-work", str(evidence),
             "--production-scope-of-work", str(clean), "--source-dir", str(live), "--output-csv", str(cmap)])
        run(["python3", str(TOOLS / "report_scope_of_work_parity.py"), "--scope-of-work", str(evidence),
             "--production-scope-of-work", str(clean), "--source-dir", str(live), "--output-json", str(parity),
             "--output-md", str(parity_md), "--isolated-migration", "--migration-authority", AUTHORITY])
        run(["python3", str(TOOLS / "derive_review_checklist.py"), str(clean), "--output", str(checklist)])
        run(["python3", str(TOOLS / "render_scope_of_work.py"), str(clean), "--output", str(render)])
        artifacts.append((cmap, parity, parity_md, checklist, render))
    assert all(left.read_bytes() == right.read_bytes() for left, right in zip(*artifacts))
    parity_data = json.loads(artifacts[0][1].read_text())
    mappings, lines = EXPECTED[did]
    assert parity_data["pass"] and not parity_data["issues"] and len(parity_data["checks"]) == mappings
    assert sum(c["line_end"] - c["line_start"] + 1 for c in parity_data["checks"]) == lines
    assert parity_data["production_scope_of_work_sha256"] == sha(clean)
    checklist = json.loads(artifacts[0][3].read_text())
    assert checklist["source"]["sha256"] == sha(clean) and checklist["source"]["migration_authority"] is None
    html = artifacts[0][4].read_text().lower()
    assert sha(clean) in html and not re.search(r"<\s*(script|iframe|form)\b|(?:src|href)\s*=\s*[\"'](?:https?:)?//", html)

    # Every documented negative class is freshly reproduced for each selected member.
    mutated = member / "mutated-clean.md"; mutated.write_bytes(clean.read_bytes() + b"\n")
    bad_map = member / "bad-map.csv"
    assert run(["python3", str(TOOLS / "map_scope_of_work_claims.py"), "--scope-of-work", str(evidence),
                "--production-scope-of-work", str(mutated), "--source-dir", str(live), "--output-csv", str(bad_map)], False).returncode
    assert not bad_map.exists()
    bad_parity = member / "bad-parity.json"
    assert run(["python3", str(TOOLS / "report_scope_of_work_parity.py"), "--scope-of-work", str(evidence),
                "--production-scope-of-work", str(mutated), "--source-dir", str(live), "--output-json", str(bad_parity),
                "--isolated-migration", "--migration-authority", AUTHORITY], False).returncode
    assert bad_parity.exists() and not json.loads(bad_parity.read_text())["pass"]
    for tool, suffix in (("derive_review_checklist.py", "json"), ("render_scope_of_work.py", "html")):
        output = member / f"evidence-rejected.{suffix}"
        assert run(["python3", str(TOOLS / tool), str(a), "--output", str(output)], False).returncode and not output.exists()
    partial = member / "negative-partial"; copy_kit(live, partial); (partial / "Guidance.md").unlink()
    assert run(base + ["--deliverable", str(partial)], False).returncode and not (partial / "ScopeOfWork.md").exists()
    assert run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(a)], False).returncode
    wrong = member / "wrong-authority.json"
    assert run(["python3", str(TOOLS / "derive_review_checklist.py"), str(a), "--isolated-migration",
                "--migration-authority", "WRONG", "--output", str(wrong)], False).returncode and not wrong.exists()
    return [did, REPRODUCE[did], sha(evidence), sha(clean), sha(report), mappings, lines, 7, "PASS"]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    if SCRATCH.exists(): shutil.rmtree(SCRATCH)
    SCRATCH.mkdir()
    manifest_rows = [
        verify_manifest("package", PACKAGE / "MANIFEST.tsv", 284),
        verify_manifest("manager", PARENT / "MANIFEST.tsv", 53),
        verify_manifest("author", AUTHOR / "MANIFEST.tsv", 939),
        verify_manifest("verifier", VERIFY / "MANIFEST.tsv", 535),
    ]
    write_tsv(OUT / "MANIFEST_REHASH.tsv", ["manifest", "entries", "bytes", "sha256", "path_style", "verdict"], manifest_rows)

    # Exactly the two governed Agent-2 children, with no child delegation surface.
    assert sorted(p.name for p in (PARENT / "children").iterdir() if p.is_dir()) == ["BATCH-AUTHOR-PKG02", "BATCH-VERIFY-PKG02"]
    assert not any(p.name == "children" for child in (AUTHOR, VERIFY) for p in child.rglob("children"))
    assert "do not delegate" in (AUTHOR / "LAUNCH_BRIEF.md").read_text().lower()
    assert "do not delegate" in (VERIFY / "LAUNCH_BRIEF.md").read_text().lower()

    frozen = list(csv.DictReader((PARENT / "FROZEN_INPUTS.tsv").open(newline=""), delimiter="\t"))
    assert [row["deliverable_id"] for row in frozen] == list(EXPECTED)
    package_members = {row["deliverable_id"]: row for row in csv.DictReader((PACKAGE / "MEMBER_RESULTS.tsv").open(newline=""), delimiter="\t")}
    replacements = list(csv.DictReader((PACKAGE / "REPLACEMENT_MANIFEST.tsv").open(newline=""), delimiter="\t"))
    rollbacks = list(csv.DictReader((PACKAGE / "ROLLBACK_MANIFEST.tsv").open(newline=""), delimiter="\t"))
    simulations = list(csv.DictReader((PACKAGE / "SIMULATION.tsv").open(newline=""), delimiter="\t"))
    assert len(replacements) == len(rollbacks) == 25 and len(simulations) == 5
    assert [row["deliverable_id"] for row in simulations] == list(EXPECTED)
    assert all(set(row.values()) >= {"PASS", "no project write"} for row in simulations)

    reproduced, all_members, new_simulations = [], [], []
    total_maps = total_lines = 0
    for row in frozen:
        did = row["deliverable_id"]; live = ROOT / row["live_path"]
        candidate = RUN / "candidates/PIP-PKG02" / did
        evidence, clean, report = candidate / "evidence/ScopeOfWork.md", candidate / "production/ScopeOfWork.md", candidate / "finalization.json"
        for name, field in HASH_FIELDS.items(): assert sha(live / name) == row[field]
        assert not (live / "ScopeOfWork.md").exists()
        run([str(ROOT / "tools/validation/check_four_documents.sh"), str(live)])
        run(["python3", str(ROOT / "tools/validation/validate_dependencies_schema.py"), str(live / "Dependencies.csv")])
        package_row = package_members[did]
        mappings, lines = EXPECTED[did]
        assert package_row["evidence_sha256"] == sha(evidence)
        assert package_row["clean_sha256"] == sha(clean)
        assert package_row["finalization_report_sha256"] == sha(report)
        assert (int(package_row["mapping_rows"]), int(package_row["source_lines"])) == (mappings, lines)
        final = json.loads(report.read_text())
        assert final["production_scope_of_work_sha256"] == sha(clean)
        assert final["evidence_candidate_sha256"] == sha(evidence)
        assert AUTHORITY not in clean.read_text() and final["migration_control"]["migration-authority"] == AUTHORITY
        assert final["source_block_count"] == mappings

        # Recompute the full accepted verifier ledgers for every member, not
        # just the two members selected for fresh tool execution.
        verifier_member = VERIFY / "members" / did
        assert (verifier_member / "claim_map_1.csv").read_bytes() == (verifier_member / "claim_map_2.csv").read_bytes()
        assert (verifier_member / "parity_1.json").read_bytes() == (verifier_member / "parity_2.json").read_bytes()
        assert (verifier_member / "parity_1.md").read_bytes() == (verifier_member / "parity_2.md").read_bytes()
        assert (verifier_member / "checklist_1.json").read_bytes() == (verifier_member / "checklist_2.json").read_bytes()
        assert (verifier_member / "render_1.html").read_bytes() == (verifier_member / "render_2.html").read_bytes()
        accepted_map = list(csv.DictReader((verifier_member / "claim_map_1.csv").open(newline="")))
        accepted_parity = json.loads((verifier_member / "parity_1.json").read_text())
        assert len(accepted_map) == len(accepted_parity["checks"]) == mappings
        assert accepted_parity["pass"] and not accepted_parity["issues"]
        assert accepted_parity["production_scope_of_work_sha256"] == sha(clean)
        by_file = {name: [] for name in DOCS}
        for check in accepted_parity["checks"]:
            assert check["disposition"] == "PRESERVED" and check["pass"] and not check["issues"]
            by_file[check["source_file"]].append((check["line_start"], check["line_end"]))
        covered = 0
        for name, spans in by_file.items():
            next_line = 1
            for start, end in spans:
                assert start == next_line and end >= start
                next_line = end + 1
            actual_lines = len((live / name).read_bytes().splitlines())
            assert next_line - 1 == actual_lines
            covered += actual_lines
        assert covered == lines
        total_maps += mappings; total_lines += lines
        all_members.append([did, sha(evidence), sha(clean), sha(report), mappings, lines, "PASS"])
        if did in REPRODUCE: reproduced.append(full_reproduce(did, row, live, evidence, clean, report))

        # Fresh apply/validate/rollback simulation for all five members.
        sim = SCRATCH / f"simulation-{did}"; copy_kit(live, sim)
        shutil.copy2(clean, sim / "ScopeOfWork.md")
        for name in DOCS: (sim / name).unlink()
        target = json.loads(run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(sim)]).stdout)
        assert target["format"] == "SOW_V1" and sha(sim / "ScopeOfWork.md") == sha(clean)
        (sim / "ScopeOfWork.md").unlink()
        for name in DOCS: shutil.copy2(live / name, sim / name)
        rolled = json.loads(run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(sim)]).stdout)
        assert rolled["format"] == "LEGACY_FOUR_DOC"
        assert all(sha(sim / name) == row[HASH_FIELDS[name]] for name in DOCS)
        new_simulations.append([did, "PASS", "PASS", "PASS", "RUN_LOCAL_ONLY"])

    assert (total_maps, total_lines) == (186, 2053)
    for forward, inverse in zip(replacements, rollbacks):
        assert forward["deliverable_id"] == inverse["deliverable_id"] and forward["path"] == inverse["path"]
        assert forward["operation"] != inverse["operation"]
        assert forward["before_sha256"] == inverse["after_sha256"] and forward["after_sha256"] == inverse["before_sha256"]
    write_tsv(OUT / "MEMBER_RESULTS.tsv", ["deliverable_id", "evidence_sha256", "clean_sha256", "report_sha256", "mappings", "source_lines", "aggregate_verdict"], all_members)
    write_tsv(OUT / "FRESH_REPRODUCTION.tsv", ["deliverable_id", "selection_basis", "evidence_sha256", "clean_sha256", "report_sha256", "mappings", "source_lines", "negative_classes", "verdict"], reproduced)
    write_tsv(OUT / "SIMULATION.tsv", ["deliverable_id", "apply", "target_validation", "rollback", "write_scope"], new_simulations)
    write_tsv(OUT / "REPLACEMENT_MANIFEST.tsv", list(replacements[0]), [[row[k] for k in replacements[0]] for row in replacements])
    write_tsv(OUT / "ROLLBACK_MANIFEST.tsv", list(rollbacks[0]), [[row[k] for k in rollbacks[0]] for row in rollbacks])

    author_progress = list(csv.DictReader((AUTHOR / "PROGRESS.tsv").open(newline=""), delimiter="\t"))
    verifier_progress = list(csv.DictReader((VERIFY / "PROGRESS.tsv").open(newline=""), delimiter="\t"))
    assert all(r["cross_member_contamination"] == "NONE" and r["scope_drift"] == "NONE" for r in author_progress)
    assert [(r["deliverable_id"], int(r["failures"]), int(r["retries"])) for r in verifier_progress] == [
        ("DEL-02-01", 3, 3), ("DEL-02-02", 0, 0), ("DEL-02-03", 0, 0), ("DEL-02-04", 0, 0), ("DEL-02-05", 0, 0)]
    status = json.loads((PARENT / "STATUS.json").read_text())
    assert status["status"] == "PASS" and status["project_writes"] == 0
    summary = {
        "status": "PASS_WITH_RETAINED_PROCESS_FINDINGS", "quality": "PASS_EQUIVALENT",
        "members": 5, "mapping_rows": total_maps, "source_lines": total_lines,
        "manifest_entries_rehashed": sum(int(r[1]) for r in manifest_rows),
        "replacement_rows": 25, "rollback_rows": 25, "fresh_simulations": 5,
        "full_fresh_reproductions": sorted(REPRODUCE), "negative_classes_fresh": 14,
        "candidate_repairs": 0, "project_writes": 0, "context_occupancy_samples": "0/3",
    }
    (OUT / "REPRODUCTION_SUMMARY.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    write_manifest(OUT)
    write_manifest(RUN / "instances/RECON-EXP-PKG02")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
