#!/usr/bin/env python3
"""Independent adoption-package reconciliation with run-local writes only."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-PACKAGE-BATCH-ADOPTION-20260714-01"
INSTANCE = RUN / "instances/WORKING-BATCH-ADOPTION"
PACKAGE = RUN / "snapshots/package"
OUT = RUN / "snapshots/reconciliation"
SCRATCH = OUT / "reproduction"
TOOLS = ROOT / "tools/scope_of_work"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
BASIS = "98af1a4bde875a0c2d5878d62fc84b3c1d7506c4"
DOCS = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROL = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
EXPECTED = {
    "DEL-01-02": (26, 204), "DEL-01-03": (34, 290), "DEL-01-04": (28, 233),
    "DEL-02-01": (35, 427), "DEL-02-02": (48, 419), "DEL-02-03": (29, 383),
    "DEL-02-04": (33, 369), "DEL-02-05": (41, 455),
}
SAMPLE = {"DEL-01-04": "PKG01_NEW_FINALIZATION", "DEL-02-05": "PKG02_FINAL_LARGEST"}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    if result.returncode:
        raise AssertionError(f"failed {result.returncode}: {' '.join(args)}\n{result.stdout}\n{result.stderr}")
    return result


def write_tsv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(header); writer.writerows(rows)


def copy_kit(live: Path, target: Path) -> None:
    target.mkdir(parents=True)
    for name in DOCS + CONTROL: shutil.copy2(live / name, target / name)


def resolve(raw: str) -> Path:
    path = (ROOT / raw.removeprefix("{REPO_ROOT}/")).resolve()
    path.relative_to(ROOT.resolve())
    return path


def verify_manifest(label: str, path: Path, count: int, allowed: list[Path]) -> list[object]:
    rows = list(csv.DictReader(path.open(newline=""), delimiter="\t"))
    assert len(rows) == count and len({r["path"] for r in rows}) == count
    assert str(path.relative_to(ROOT)) not in {r["path"].removeprefix("{REPO_ROOT}/") for r in rows}
    total = 0
    for row in rows:
        actual = resolve(row["path"])
        assert any(actual == root.resolve() or actual.is_relative_to(root.resolve()) for root in allowed)
        assert actual.is_file() and sha(actual) == row["sha256"] and actual.stat().st_size == int(row["bytes"])
        total += int(row["bytes"])
    return [label, count, total, sha(path), "PASS"]


def full_sample(did: str, live: Path, evidence: Path, clean: Path, report: Path) -> list[object]:
    member = SCRATCH / did; member.mkdir()
    finals = []
    for label in ("a", "b"):
        final = member / f"final-{label}/ScopeOfWork.md"
        final_report = member / f"final-{label}/finalization.json"
        final.parent.mkdir()
        run(["python3", str(TOOLS / "finalize_scope_of_work.py"), "--evidence-candidate", str(evidence),
             "--output", str(final), "--report", str(final_report)])
        finals.append((final, final_report))
    assert finals[0][0].read_bytes() == finals[1][0].read_bytes() == clean.read_bytes()
    assert finals[0][1].read_bytes() == finals[1][1].read_bytes() == report.read_bytes()
    assert json.loads(run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(clean)]).stdout)["format"] == "SOW_V1"
    artifacts = []
    for n in (1, 2):
        cmap, parity = member / f"claim-map-{n}.csv", member / f"parity-{n}.json"
        parity_md, checklist, render = member / f"parity-{n}.md", member / f"checklist-{n}.json", member / f"render-{n}.html"
        run(["python3", str(TOOLS / "map_scope_of_work_claims.py"), "--scope-of-work", str(evidence),
             "--production-scope-of-work", str(clean), "--source-dir", str(live), "--output-csv", str(cmap)])
        run(["python3", str(TOOLS / "report_scope_of_work_parity.py"), "--scope-of-work", str(evidence),
             "--production-scope-of-work", str(clean), "--source-dir", str(live), "--output-json", str(parity),
             "--output-md", str(parity_md), "--isolated-migration", "--migration-authority", AUTH])
        run(["python3", str(TOOLS / "derive_review_checklist.py"), str(clean), "--output", str(checklist)])
        run(["python3", str(TOOLS / "render_scope_of_work.py"), str(clean), "--output", str(render)])
        artifacts.append((cmap, parity, parity_md, checklist, render))
    assert all(a.read_bytes() == b.read_bytes() for a, b in zip(*artifacts))
    parity = json.loads(artifacts[0][1].read_text()); mappings, lines = EXPECTED[did]
    assert parity["pass"] and not parity["issues"] and len(parity["checks"]) == mappings
    assert sum(c["line_end"] - c["line_start"] + 1 for c in parity["checks"]) == lines
    assert parity["production_scope_of_work_sha256"] == sha(clean)
    checklist = json.loads(artifacts[0][3].read_text())
    assert checklist["source"]["sha256"] == sha(clean) and checklist["source"]["migration_authority"] is None
    assert sha(clean) in artifacts[0][4].read_text().lower()
    return [did, SAMPLE[did], sha(evidence), sha(clean), sha(report), mappings, lines, "PASS"]


def write_manifest(root: Path) -> None:
    rows = []
    for path in sorted(p for p in root.rglob("*") if p.is_file() and p.name != "MANIFEST.tsv"):
        data = path.read_bytes()
        rows.append(["{REPO_ROOT}/" + str(path.relative_to(ROOT)), sha(path), len(data), len(data.splitlines())])
    write_tsv(root / "MANIFEST.tsv", ["path", "sha256", "bytes", "lines"], rows)


def main() -> None:
    assert run(["git", "rev-parse", "HEAD"]).stdout.strip() == BASIS
    assert run(["git", "branch", "--show-current"]).stdout.strip() == "codex/adopt-pkg-batch-workflow"
    OUT.mkdir(parents=True, exist_ok=True)
    if SCRATCH.exists(): shutil.rmtree(SCRATCH)
    SCRATCH.mkdir()
    manifests = [
        verify_manifest("package", PACKAGE / "MANIFEST.tsv", 12, [PACKAGE]),
        verify_manifest("working", INSTANCE / "MANIFEST.tsv", 240, [INSTANCE, RUN / "candidates", PACKAGE / "MANIFEST.tsv"]),
    ]
    write_tsv(OUT / "MANIFEST_REHASH.tsv", ["manifest", "entries", "bytes", "sha256", "verdict"], manifests)

    rows = list(csv.DictReader((INSTANCE / "FROZEN_INPUTS.tsv").open(newline=""), delimiter="\t"))
    expected_ids = list(EXPECTED)
    assert [r["deliverable_id"] for r in rows] == expected_ids
    assert [r["package_id"] for r in rows] == ["PKG-01"] * 3 + ["PKG-02"] * 5
    results = {r["deliverable_id"]: r for r in csv.DictReader((PACKAGE / "MEMBER_RESULTS.tsv").open(newline=""), delimiter="\t")}
    replacement = list(csv.DictReader((PACKAGE / "REPLACEMENT_MANIFEST.tsv").open(newline=""), delimiter="\t"))
    rollback = list(csv.DictReader((PACKAGE / "ROLLBACK_MANIFEST.tsv").open(newline=""), delimiter="\t"))
    recorded_sim = list(csv.DictReader((PACKAGE / "SIMULATION.tsv").open(newline=""), delimiter="\t"))
    assert len(replacement) == len(rollback) == 40 and len(recorded_sim) == 8
    assert [r["deliverable_id"] for r in recorded_sim] == expected_ids
    assert all(r["apply"] == r["target_validation"] == r["rollback"] == "PASS" for r in recorded_sim)
    assert all("/evidence/" not in r["path"] and r["path"].endswith(("ScopeOfWork.md", *DOCS)) for r in replacement)
    assert sum(r["operation"] == "A" and r["path"].endswith("/ScopeOfWork.md") for r in replacement) == 8
    assert sum(r["operation"] == "D" for r in replacement) == 32
    for forward, inverse in zip(replacement, rollback):
        assert forward["deliverable_id"] == inverse["deliverable_id"] and forward["path"] == inverse["path"]
        assert forward["operation"] != inverse["operation"]
        assert forward["before_sha256"] == inverse["after_sha256"] and forward["after_sha256"] == inverse["before_sha256"]

    totals = [0, 0]; members = []; samples = []; simulations = []
    for row in rows:
        did, package = row["deliverable_id"], row["package_id"]
        live = ROOT / row["live_path"]
        target = RUN / "candidates" / f"PIP-{package}" / did
        evidence, clean, report = target / "evidence/ScopeOfWork.md", target / "production/ScopeOfWork.md", target / "finalization.json"
        for name in DOCS + CONTROL: assert sha(live / name) == row[f"{name}_sha256"]
        assert not (live / "ScopeOfWork.md").exists()
        result = results[did]; mappings, lines = EXPECTED[did]
        assert result["package_id"] == package and result["evidence_sha256"] == sha(evidence)
        assert result["clean_sha256"] == sha(clean) and result["report_sha256"] == sha(report)
        assert (int(result["mappings"]), int(result["source_lines"])) == (mappings, lines)
        final = json.loads(report.read_text())
        assert final["evidence_candidate_sha256"] == sha(evidence)
        assert final["production_scope_of_work_sha256"] == sha(clean)
        assert final["migration_control"]["migration-authority"] == AUTH and final["source_block_count"] == mappings
        lower = clean.read_bytes().lower()
        assert not any(token in lower for token in [b"sow-source-begin", b"sow-source-end", b"migration-authority:",
                                                     b"pilot-variance:", b"issued-preparation-", b"migration candidate"])
        member = INSTANCE / "members" / did
        assert (member / "claim-map-1.csv").read_bytes() == (member / "claim-map-2.csv").read_bytes()
        assert (member / "parity-1.json").read_bytes() == (member / "parity-2.json").read_bytes()
        parity = json.loads((member / "parity-1.json").read_text())
        assert parity["pass"] and not parity["issues"] and len(parity["checks"]) == mappings
        assert parity["production_scope_of_work_sha256"] == sha(clean)
        by_file = {name: [] for name in DOCS}
        for check in parity["checks"]:
            assert check["pass"] and not check["issues"] and check["disposition"] == "PRESERVED"
            by_file[check["source_file"]].append((check["line_start"], check["line_end"]))
        covered = 0
        for name, spans in by_file.items():
            next_line = 1
            for start, end in spans: assert start == next_line and end >= start; next_line = end + 1
            assert next_line - 1 == len((live / name).read_bytes().splitlines())
            covered += next_line - 1
        assert covered == lines
        totals[0] += mappings; totals[1] += lines
        members.append([package, did, sha(evidence), sha(clean), sha(report), mappings, lines, "PASS"])
        if did in SAMPLE: samples.append(full_sample(did, live, evidence, clean, report))

        sim = SCRATCH / f"simulation-{did}"; copy_kit(live, sim); shutil.copy2(clean, sim / "ScopeOfWork.md")
        for name in DOCS: (sim / name).unlink()
        assert json.loads(run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(sim)]).stdout)["format"] == "SOW_V1"
        (sim / "ScopeOfWork.md").unlink()
        for name in DOCS: shutil.copy2(live / name, sim / name)
        assert json.loads(run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(sim)]).stdout)["format"] == "LEGACY_FOUR_DOC"
        assert all(sha(sim / name) == row[f"{name}_sha256"] for name in DOCS + CONTROL)
        simulations.append([did, "PASS", "PASS", "PASS", "RUN_LOCAL_ONLY"])

    assert totals == [274, 2780] and len(samples) == 2
    write_tsv(OUT / "MEMBER_RESULTS.tsv", ["package_id", "deliverable_id", "evidence_sha256", "clean_sha256", "report_sha256", "mappings", "source_lines", "verdict"], members)
    write_tsv(OUT / "FRESH_REPRODUCTION.tsv", ["deliverable_id", "selection_basis", "evidence_sha256", "clean_sha256", "report_sha256", "mappings", "source_lines", "verdict"], samples)
    write_tsv(OUT / "SIMULATION.tsv", ["deliverable_id", "apply", "target_validation", "rollback", "write_scope"], simulations)
    write_tsv(OUT / "REPLACEMENT_MANIFEST.tsv", list(replacement[0]), [[r[k] for k in replacement[0]] for r in replacement])
    write_tsv(OUT / "ROLLBACK_MANIFEST.tsv", list(rollback[0]), [[r[k] for k in rollback[0]] for r in rollback])
    summary = {"status": "PASS", "basis": BASIS, "members": 8, "live_bindings": 72,
               "mappings": totals[0], "source_lines": totals[1], "manifest_entries_rehashed": 252,
               "replacement_rows": 40, "rollback_rows": 40, "simulations": 8,
               "fresh_reproductions": sorted(SAMPLE), "exceptions": 0, "project_writes": 0}
    (OUT / "REPRODUCTION_SUMMARY.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    write_manifest(OUT); write_manifest(RUN / "instances/RECON-BATCH-ADOPTION")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__": main()
