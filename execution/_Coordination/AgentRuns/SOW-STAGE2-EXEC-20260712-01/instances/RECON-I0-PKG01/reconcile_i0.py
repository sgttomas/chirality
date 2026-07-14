#!/usr/bin/env python3
"""Independent full reproduction of the isolated ISSUED I0 package."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
UPSTREAM = RUN / "instances/WORKING-I0-PKG01"
HERE = RUN / "instances/RECON-I0-PKG01"
SNAP = RUN / "snapshots/I0/preintegration-r1"
CAND = RUN / "candidates/I0/PIP-PKG01/DEL-01-01"
LIVE_REL = Path("projects/chirality-piping/execution/PKG-01_Governance, IP Boundary, and Professional Responsibility/1_Working/DEL-01-01_Project governance baseline")
LIVE = ROOT / LIVE_REL
TOOLS = ROOT / "tools/scope_of_work"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
BASIS = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176;Stage2Plan@27f03730c956447b9a9696422cc9c63b8f061939;W_P1=ACCEPTED"
COMMIT = "c5abf91b717c0b3901d2a27c578e63976853f8de"
LEGACY = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
SOURCE_HASHES = {
    "Datasheet.md": "219b2d6a6ca0e08be1a8c7d460a19c27547bdebc317bde8347d3e1b607d15a54",
    "Specification.md": "8994c342c893dec0ce385f4022230cf0e73527e082574418d20c9f6adf853f6f",
    "Guidance.md": "a7b84bcf1f035f12074173bd78e4b1a0f56cf65f0b5ce06fae9485ab859d8473",
    "Procedure.md": "ffe888b7795d22cb02370c163d7f5d84e2e829cc12428d69e034a01d0dc68be2",
    "_STATUS.md": "e63b1797b30c291b2a4510cd521951fd2736675025f0e2d07b810e64617b28a8",
}
EVIDENCE_SHA = "e243b68db82a0fd26d27fdad37caf32d0e4edd7124975d6f5c27f7c997b366ed"
PRODUCTION_SHA = "23d92ddeb0cc4e3fe37694b1c8b79284017799cd08caaaad9767c8a4f0121f21"
FINALIZATION_SHA = "fb429964c4d30f08201c46b2a259a103eddc480bac8ea6c5b38df234c0cc5ffd"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args: list[str], *, allow_fail: bool = False) -> subprocess.CompletedProcess[str]:
    cp = subprocess.run(args, cwd=ROOT, text=True, capture_output=True,
                        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    if cp.returncode and not allow_fail:
        raise RuntimeError(f"exit {cp.returncode}: {' '.join(args)}\n{cp.stdout}\n{cp.stderr}")
    return cp


def write_tsv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def project_digest() -> tuple[str, int]:
    root = ROOT / "projects/chirality-piping"
    h = hashlib.sha256()
    files = sorted(p for p in root.rglob("*") if p.is_file())
    for path in files:
        rel = path.relative_to(root).as_posix().encode()
        data = path.read_bytes()
        h.update(len(rel).to_bytes(8, "big")); h.update(rel)
        h.update(len(data).to_bytes(8, "big")); h.update(data)
    return h.hexdigest(), len(files)


def resolve_manifest_path(manifest: Path, raw: str) -> Path:
    p = Path(raw)
    if p.is_absolute() or ".." in p.parts:
        raise AssertionError((manifest, raw, "nonportable"))
    candidate = ROOT / p if p.parts and p.parts[0] == "execution" else manifest.parent / p
    resolved = candidate.resolve()
    resolved.relative_to(ROOT.resolve())
    return resolved


def audit_manifest(manifest: Path) -> tuple[int, str]:
    rows = list(csv.DictReader(manifest.open(encoding="utf-8"), delimiter="\t"))
    seen: set[Path] = set()
    for row in rows:
        path = resolve_manifest_path(manifest, row["path"])
        assert path != manifest.resolve()
        assert path not in seen
        seen.add(path)
        assert path.is_file()
        assert sha(path) == row["sha256"]
        assert path.stat().st_size == int(row["bytes"])
    return len(rows), sha(manifest)


def copy_source(target: Path) -> None:
    target.mkdir(parents=True)
    for name in LEGACY + ["_STATUS.md"]:
        shutil.copy2(LIVE / name, target / name)


def converter_args(deliverable: Path, *, basis: str = BASIS, authority: str = AUTH,
                   source_hashes: dict[str, str] = SOURCE_HASHES) -> list[str]:
    evidence = (CAND / "evidence/ScopeOfWork.md").read_text(encoding="utf-8")
    def definition(identifier: str) -> str:
        match = re.search(rf"^- \*\*{identifier}\*\* — (.+)$", evidence, re.MULTILINE)
        assert match
        return match.group(1)
    args = ["python3", str(TOOLS / "convert_four_documents_to_scope_of_work.py"),
            "--deliverable", str(deliverable), "--deliverable-id", "DEL-01-01",
            "--package-id", "PKG-01", "--decomposition-basis",
            f"projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@{COMMIT}",
            "--project-scope-ref", "SOW-001", "--project-scope-ref", "SOW-048",
            "--package-objective-ref", "OBJ-001", "--package-objective-ref", "OBJ-002",
            "--output-description", definition("OUT-001"),
            "--acceptance-criterion", definition("AC-001"),
            "--verification-method", definition("VER-001"),
            "--isolated-migration", "--migration-authority", authority,
            "--issued-source-commit", COMMIT, "--issued-accepted-basis", basis,
            "--issued-status-sha256", SOURCE_HASHES["_STATUS.md"]]
    for name in ["Datasheet.md", "Specification.md", "Procedure.md", "Guidance.md"]:
        args += ["--issued-source-sha256", f"{name}={source_hashes[name]}"]
    return args


def main() -> None:
    if SNAP.exists():
        raise RuntimeError(f"immutable snapshot exists: {SNAP}")
    SNAP.mkdir(parents=True)
    detail = SNAP / "reproduction"
    detail.mkdir()
    before_hash, before_files = project_digest()

    manifests = [UPSTREAM / "MANIFEST.tsv", UPSTREAM / "children/I0-AUTHOR/MANIFEST.tsv",
                 UPSTREAM / "children/I0-VERIFY/MANIFEST.tsv"]
    audits = []
    for manifest in manifests:
        rows, digest = audit_manifest(manifest)
        audits.append([manifest.relative_to(ROOT).as_posix(), rows, digest, "PASS"])
    assert [row[1] for row in audits] == [189, 44, 102]
    write_tsv(SNAP / "UPSTREAM_MANIFEST_AUDIT.tsv",
              ["manifest", "rows", "sha256", "verdict"], audits)

    assert run(["git", "rev-parse", "HEAD"]).stdout.strip() == COMMIT
    source_rows = []
    for name, expected in SOURCE_HASHES.items():
        actual = sha(LIVE / name)
        assert actual == expected
        source_rows.append([name, expected, actual, (LIVE / name).stat().st_size, "PASS"])
    assert "**Current State:** ISSUED" in (LIVE / "_STATUS.md").read_text(encoding="utf-8")
    assert not (LIVE / "ScopeOfWork.md").exists()
    lines = sum(len((LIVE / name).read_bytes().splitlines()) for name in LEGACY)
    assert lines == 272
    write_tsv(SNAP / "SOURCE_BINDINGS.tsv",
              ["surface", "expected_sha256", "actual_sha256", "bytes", "verdict"], source_rows)

    evidence = CAND / "evidence/ScopeOfWork.md"
    production = CAND / "production/ScopeOfWork.md"
    finalization = CAND / "finalization.json"
    assert sha(evidence) == EVIDENCE_SHA and sha(production) == PRODUCTION_SHA
    assert sha(finalization) == FINALIZATION_SHA

    with tempfile.TemporaryDirectory(prefix="recon-i0-pkg01-") as td:
        temp = Path(td)
        source_a = temp / "source-a"; copy_source(source_a)
        source_b = temp / "source-b"; copy_source(source_b)
        run(converter_args(source_a)); run(converter_args(source_b))
        assert sha(source_a / "ScopeOfWork.md") == sha(source_b / "ScopeOfWork.md") == EVIDENCE_SHA
        shutil.copy2(source_a / "ScopeOfWork.md", detail / "reproduced-evidence.md")

        prod_a = temp / "prod-a/ScopeOfWork.md"; report_a = temp / "report-a.json"
        prod_b = temp / "prod-b/ScopeOfWork.md"; report_b = temp / "report-b.json"
        run(["python3", str(TOOLS / "finalize_scope_of_work.py"), "--evidence-candidate",
             str(source_a / "ScopeOfWork.md"), "--output", str(prod_a), "--report", str(report_a)])
        run(["python3", str(TOOLS / "finalize_scope_of_work.py"), "--evidence-candidate",
             str(source_b / "ScopeOfWork.md"), "--output", str(prod_b), "--report", str(report_b)])
        assert sha(prod_a) == sha(prod_b) == PRODUCTION_SHA
        assert sha(report_a) == sha(report_b) == FINALIZATION_SHA
        shutil.copy2(prod_a, detail / "reproduced-production.md")
        shutil.copy2(report_a, detail / "reproduced-finalization.json")

        validation = run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(prod_a)])
        (detail / "validation.json").write_text(validation.stdout, encoding="utf-8")
        run(["python3", str(TOOLS / "map_scope_of_work_claims.py"), "--scope-of-work", str(evidence),
             "--production-scope-of-work", str(prod_a), "--source-dir", str(LIVE),
             "--output-csv", str(detail / "claim-map.csv")])
        run(["python3", str(TOOLS / "report_scope_of_work_parity.py"), "--scope-of-work", str(evidence),
             "--production-scope-of-work", str(prod_a), "--source-dir", str(LIVE),
             "--output-json", str(detail / "parity.json"), "--output-md", str(detail / "parity.md"),
             "--isolated-migration", "--migration-authority", AUTH])
        parity = json.loads((detail / "parity.json").read_text())
        assert parity["pass"] and not parity["issues"] and len(parity["checks"]) == 27
        assert sum(x["line_end"] - x["line_start"] + 1 for x in parity["checks"]) == 272
        for suffix in ("a", "b"):
            run(["python3", str(TOOLS / "derive_review_checklist.py"), str(prod_a),
                 "--output", str(detail / f"checklist-{suffix}.json")])
            run(["python3", str(TOOLS / "render_scope_of_work.py"), str(prod_a),
                 "--output", str(detail / f"render-{suffix}.html")])
        assert (detail / "checklist-a.json").read_bytes() == (detail / "checklist-b.json").read_bytes()
        assert (detail / "render-a.html").read_bytes() == (detail / "render-b.html").read_bytes()
        assert sha(detail / "checklist-a.json") == "a0888fea49b50597bd345a0d690a9730d02de91127aaeb1f9a1c157ecde77fd1"
        assert sha(detail / "render-a.html") == "fc5bc789379c29e711242285d444ce3f1d36aea87234edacea2c68b35a8db765"
        html = (detail / "render-a.html").read_text().lower()
        assert "<script" not in html and "http://" not in html and "https://" not in html
        clean_text = prod_a.read_text()
        for token in ["sow-source-begin", "migration-authority:", "issued-preparation-", "migration candidate"]:
            assert token.lower() not in clean_text.lower()

        dual = temp / "dual"; copy_source(dual); shutil.copy2(evidence, dual / "ScopeOfWork.md")
        run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--isolated-migration",
             "--migration-authority", AUTH, "--json", str(dual)])
        negatives = []
        cp = run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(dual)], allow_fail=True)
        assert cp.returncode != 0; negatives.append(["unauthorized_dual", cp.returncode, "PASS"])
        partial = temp / "partial"; partial.mkdir(); shutil.copy2(LIVE / "Datasheet.md", partial / "Datasheet.md")
        shutil.copy2(LIVE / "_STATUS.md", partial / "_STATUS.md")
        cp = run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(partial)], allow_fail=True)
        assert cp.returncode != 0; negatives.append(["partial", cp.returncode, "PASS"])
        wrong = temp / "wrong"; copy_source(wrong)
        cp = run(converter_args(wrong, authority="D-GOV-16@0000000"), allow_fail=True)
        assert cp.returncode != 0; negatives.append(["wrong_authority", cp.returncode, "PASS"])
        wrong_basis = temp / "wrong-basis"; copy_source(wrong_basis)
        cp = run(converter_args(wrong_basis, basis=" invalid "), allow_fail=True)
        assert cp.returncode != 0; negatives.append(["wrong_basis", cp.returncode, "PASS"])
        drift = temp / "drift"; copy_source(drift); (drift / "Datasheet.md").write_bytes((drift / "Datasheet.md").read_bytes() + b"drift")
        cp = run(converter_args(drift), allow_fail=True)
        assert cp.returncode != 0; negatives.append(["source_drift", cp.returncode, "PASS"])
        mutated = temp / "mutated.md"; mutated.write_bytes(prod_a.read_bytes() + b"\n")
        cp = run(["python3", str(TOOLS / "report_scope_of_work_parity.py"), "--scope-of-work", str(evidence),
                  "--production-scope-of-work", str(mutated), "--source-dir", str(LIVE),
                  "--output-json", str(temp / "mutated.json"), "--isolated-migration",
                  "--migration-authority", AUTH], allow_fail=True)
        assert cp.returncode != 0; negatives.append(["mutated_production", cp.returncode, "PASS"])
        write_tsv(SNAP / "NEGATIVE_RESULTS.tsv", ["probe", "exit", "verdict"], negatives)

        target = temp / "target"; copy_source(target); shutil.copy2(prod_a, target / "ScopeOfWork.md")
        for name in LEGACY: (target / name).unlink()
        run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(target / "ScopeOfWork.md")])
        assert sha(target / "ScopeOfWork.md") == PRODUCTION_SHA and sha(target / "_STATUS.md") == SOURCE_HASHES["_STATUS.md"]
        (target / "ScopeOfWork.md").unlink()
        for name in LEGACY: shutil.copy2(LIVE / name, target / name)
        assert all(sha(target / name) == SOURCE_HASHES[name] for name in LEGACY + ["_STATUS.md"])

    replacement = (UPSTREAM / "REPLACEMENT_MANIFEST.tsv").read_bytes()
    rollback = (UPSTREAM / "ROLLBACK_MANIFEST.tsv").read_bytes()
    assert len(list(csv.reader(replacement.decode().splitlines(), delimiter="\t"))) - 1 == 5
    assert len(list(csv.reader(rollback.decode().splitlines(), delimiter="\t"))) - 1 == 5
    (SNAP / "REPLACEMENT_MANIFEST.tsv").write_bytes(replacement)
    (SNAP / "ROLLBACK_MANIFEST.tsv").write_bytes(rollback)
    write_tsv(SNAP / "SIMULATION_RESULTS.tsv",
              ["deliverable_id", "apply", "target_validation", "status_preservation", "rollback"],
              [["DEL-01-01", "PASS", "PASS", "PASS", "PASS"]])

    focused = run(["python3", "-m", "pytest", "-q", "-p", "no:cacheprovider", "tools/scope_of_work/test_scope_of_work_tools.py"])
    (SNAP / "FOCUSED_TESTS.txt").write_text(focused.stdout + focused.stderr, encoding="utf-8")
    root_tests = run(["python3", "-m", "pytest", "-q", "-p", "no:cacheprovider",
                      "tools/validation/test_public_export_profile.py", "tools/scope_of_work/test_scope_of_work_tools.py"])
    (SNAP / "ROOT_TESTS.txt").write_text(root_tests.stdout + root_tests.stderr, encoding="utf-8")
    self_check = run(["python3", "tools/practitioner_harness/harness.py", "self-check"])
    (SNAP / "PRACTITIONER_SELF_CHECK.txt").write_text(self_check.stdout + self_check.stderr, encoding="utf-8")
    practitioner = run(["python3", "-m", "pytest", "-q", "-p", "no:cacheprovider",
                        "--junitxml", str(SNAP / "PRACTITIONER_HARNESS.junit.xml"), "tools/practitioner_harness"])
    (SNAP / "PRACTITIONER_HARNESS.txt").write_text(practitioner.stdout + practitioner.stderr, encoding="utf-8")

    after_hash, after_files = project_digest()
    assert (before_hash, before_files) == (after_hash, after_files)
    (SNAP / "PROJECT_CONTAINMENT.json").write_text(json.dumps({
        "project_tree_before_sha256": before_hash, "project_tree_after_sha256": after_hash,
        "project_file_count_before": before_files, "project_file_count_after": after_files,
        "zero_project_writes": True, "live_format": "LEGACY_FOUR_DOC", "lifecycle": "ISSUED",
        "h1_approved": False, "integration_permitted": False,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {"status": "PASS", "members": 1, "terminal_children": 2,
               "upstream_manifests": 3, "upstream_manifest_rows": 335,
               "mappings": 27, "source_lines": 272, "replacement_rows": 5,
               "rollback_rows": 5, "simulations_pass": 1, "negative_probes_pass": 6,
               "schema": "PASS", "content_authority": "PASS",
               "preservation_containment": "PASS", "execution_substrate": "PASS",
               "semantic_additions": 0, "conflicts": 0, "blockers": 0,
               "lifecycle": "ISSUED", "h1_approved": False, "integration_permitted": False}
    (SNAP / "SUMMARY.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
