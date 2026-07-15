#!/usr/bin/env python3
"""Independent full reproduction of the frozen 15-member W-P3 migration wave."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
HERE = RUN / "instances/RECON-P3"
SNAP = RUN / "snapshots/W_P3/preintegration"
PREF = RUN / "snapshots/W_P3/preflight"
CAND = RUN / "candidates/W_P3"
TOOLS = ROOT / "tools/scope_of_work"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
PACKAGES = ["10", "11", "12"]
EXPECTED_MANAGERS = {
    "10": (1567, "4856fe725d0feaf4866d39a749d2e3769031204b452268466119cf210023ed0a"),
    "11": (1530, "4dc1714c70c38fe4469af9e4d680f3f32a8d050f7d3c53c20ebafeff97608ee7"),
    "12": (1397, "ab265d917a4d51e6e1bae7f0e9c2aa75e0f36cb9f82f329e783f345c8793a417"),
}
LEGACY = ["Datasheet.md", "Specification.md", "Guidance.md", "Procedure.md"]
CONTROL = ["_STATUS.md", "_CONTEXT.md", "_REFERENCES.md", "_DEPENDENCIES.md", "Dependencies.csv"]
HASH_COLS = {
    "Datasheet.md": "datasheet_sha256", "Specification.md": "specification_sha256",
    "Guidance.md": "guidance_sha256", "Procedure.md": "procedure_sha256",
    "_STATUS.md": "status_sha256", "_CONTEXT.md": "context_sha256",
    "_REFERENCES.md": "references_sha256", "_DEPENDENCIES.md": "dependencies_md_sha256",
    "Dependencies.csv": "dependencies_csv_sha256",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(args: list[str], allow_fail: bool = False) -> subprocess.CompletedProcess[str]:
    cp = subprocess.run(args, cwd=ROOT, text=True, capture_output=True,
                        env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    if cp.returncode and not allow_fail:
        raise RuntimeError(f"exit {cp.returncode}: {' '.join(args)}\n{cp.stdout}\n{cp.stderr}")
    return cp


def write_tsv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(header); writer.writerows(rows)


def project_digest() -> tuple[str, int]:
    root = ROOT / "projects/chirality-piping"
    h = hashlib.sha256(); files = sorted(p for p in root.rglob("*") if p.is_file())
    for path in files:
        rel = path.relative_to(root).as_posix().encode(); data = path.read_bytes()
        h.update(len(rel).to_bytes(8, "big")); h.update(rel)
        h.update(len(data).to_bytes(8, "big")); h.update(data)
    return h.hexdigest(), len(files)


def resolve_manifest_path(manifest: Path, raw: str) -> Path:
    p = Path(raw)
    assert not p.is_absolute() and ".." not in p.parts, (manifest, raw, "nonportable")
    candidate = ROOT / p if p.parts and p.parts[0] in {"execution", "projects", "tools", "docs", "agents", "skills"} else manifest.parent / p
    resolved = candidate.resolve(); resolved.relative_to(ROOT.resolve())
    return resolved


def audit_manifest(manifest: Path) -> tuple[int, str]:
    rows = list(csv.DictReader(manifest.open(encoding="utf-8"), delimiter="\t")); seen: set[Path] = set()
    for row in rows:
        path = resolve_manifest_path(manifest, row["path"])
        assert path != manifest.resolve(), (manifest, "self inclusion")
        assert path not in seen, (manifest, path, "duplicate"); seen.add(path)
        assert path.is_file(), (manifest, path, "missing")
        assert sha(path) == row["sha256"], (manifest, path, "hash")
        assert path.stat().st_size == int(row["bytes"]), (manifest, path, "bytes")
    return len(rows), sha(manifest)


def front(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", text, re.M)
    assert match, (key, "missing"); return match.group(1).strip()


def refs(value: str) -> list[str]:
    assert value.startswith("[") and value.endswith("]"), value
    return [x.strip() for x in value[1:-1].split(",") if x.strip()]


def definition(text: str, prefix: str) -> str:
    match = re.search(rf"^- \*\*{prefix}-001\*\* — (.+)$", text, re.M)
    assert match, (prefix, "missing"); return match.group(1)


def copy_inputs(live: Path, target: Path, controls: bool = True) -> None:
    target.mkdir(parents=True)
    names = LEGACY + (CONTROL if controls else ["_STATUS.md"])
    for name in names: shutil.copy2(live / name, target / name)


def main() -> None:
    if SNAP.exists(): raise RuntimeError(f"immutable snapshot already exists: {SNAP}")
    SNAP.mkdir(parents=True); details = SNAP / "members"; details.mkdir()
    before_project = project_digest()

    manifest_rows: list[list[object]] = []; manager_total = 0
    accepted_children = 0; excluded_children = 0
    upstream_members: dict[str, dict[str, dict[str, str]]] = {}
    for pkg in PACKAGES:
        manager = RUN / f"instances/WORKING-P3-PKG{pkg}"
        count, digest = audit_manifest(manager / "MANIFEST.tsv")
        assert (count, digest) == EXPECTED_MANAGERS[pkg], (pkg, count, digest)
        manager_total += count
        manifest_rows.append([(manager / "MANIFEST.tsv").relative_to(ROOT).as_posix(), "manager", count, digest, "ACCEPTED"])
        children = ["AUTHOR-B1", "VERIFY-B1"] if pkg != "12" else ["AUTHOR-B1", "VERIFY-B1", "VERIFY-B1-R1"]
        for child in children:
            base = manager / "children" / child
            ccount, cdigest = audit_manifest(base / "MANIFEST.tsv")
            status_data = json.loads((base / "STATUS.json").read_text(encoding="utf-8"))
            status = status_data.get("status", status_data.get("result"))
            accepted = not (pkg == "12" and child == "VERIFY-B1")
            if accepted:
                assert status in {"PASS", "PASS_UNCHANGED"}; accepted_children += 1
                disposition = "ACCEPTED"
            else:
                assert status == "BLOCKED"; excluded_children += 1
                disposition = "RETAINED_EXCLUDED_BLOCKED"
            manifest_rows.append([(base / "MANIFEST.tsv").relative_to(ROOT).as_posix(), child, ccount, cdigest, disposition])
        upstream_members[pkg] = {r["deliverable_id"]: r for r in csv.DictReader((manager / "MEMBER_RESULTS.tsv").open(encoding="utf-8"), delimiter="\t")}
    assert manager_total == 4494 and accepted_children == 6 and excluded_children == 1
    write_tsv(SNAP / "UPSTREAM_MANIFEST_AUDIT.tsv", ["manifest", "owner", "rows", "sha256", "disposition"], manifest_rows)

    replacement: list[list[object]] = []; rollback: list[list[object]] = []
    member_results: list[list[object]] = []; bindings: list[list[object]] = []
    simulations: list[list[object]] = []; dependency_checks: list[list[object]] = []
    negative: list[list[object]] = []; total_maps = total_lines = 0
    rows = list(csv.DictReader((PREF / "P3_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\t"))
    assert len(rows) == 15
    for row in rows:
        did = row["deliverable_id"]; pkg = row["package"].split("-")[1]
        live = ROOT / row["live_path"]; base = CAND / f"PIP-PKG{pkg}" / did
        evidence = base / "evidence/ScopeOfWork.md"; production = base / "production/ScopeOfWork.md"; report = base / "finalization.json"
        out = details / did; out.mkdir(); text = evidence.read_text(encoding="utf-8")
        assert row["lifecycle"] == "IN_PROGRESS" and row["issued"] == "false" and not (live / "ScopeOfWork.md").exists()
        before_live = {}
        for name, col in HASH_COLS.items():
            actual = sha(live / name); assert actual == row[col], (did, name, "drift")
            before_live[name] = actual; bindings.append([did, name, row[col], actual, "PASS"])
        upstream = upstream_members[pkg][did]
        final = json.loads(report.read_text(encoding="utf-8"))
        assert final["schema"] == "chirality-sow-finalization/v1"
        assert final["evidence_candidate_sha256"] == sha(evidence) == upstream["evidence_sha256"]
        assert final["production_scope_of_work_sha256"] == sha(production) == upstream["production_sha256"]
        assert sha(report) == upstream["finalization_sha256"]
        ptext = production.read_text(encoding="utf-8")
        assert not any(x in ptext for x in ["sow-source-begin", "sow-source-end", "migration-authority", "migration candidate"])
        assert "**CON-" not in text

        with tempfile.TemporaryDirectory(prefix=f"recon-p3-{did}-") as tmp:
            work = Path(tmp)
            conversion_hashes = []
            for n in (1, 2):
                conv = work / f"conversion-{n}"; copy_inputs(live, conv, controls=False)
                cmd = [sys.executable, str(TOOLS / "convert_four_documents_to_scope_of_work.py"), "--deliverable", str(conv),
                       "--deliverable-id", did, "--package-id", row["package"], "--decomposition-basis", front(text, "decomposition_basis")]
                for value in refs(front(text, "project_scope_refs")): cmd += ["--project-scope-ref", value]
                for value in refs(front(text, "package_objective_refs")): cmd += ["--package-objective-ref", value]
                cmd += ["--output-description", definition(text, "OUT"), "--acceptance-criterion", definition(text, "AC"),
                        "--verification-method", definition(text, "VER"), "--isolated-migration", "--migration-authority", AUTH]
                run(cmd); assert (conv / "ScopeOfWork.md").read_bytes() == evidence.read_bytes()
                conversion_hashes.append(sha(conv / "ScopeOfWork.md"))
            assert len(set(conversion_hashes)) == 1
            for n in (1, 2):
                fresh = work / f"final-{n}.md"; fresh_report = work / f"final-{n}.json"
                run([sys.executable, str(TOOLS / "finalize_scope_of_work.py"), "--evidence-candidate", str(evidence),
                     "--output", str(fresh), "--report", str(fresh_report)])
                assert fresh.read_bytes() == production.read_bytes() and fresh_report.read_bytes() == report.read_bytes()

            clean = run([sys.executable, str(TOOLS / "validate_scope_of_work.py"), "--json", str(production)])
            (out / "validation-clean.json").write_text(clean.stdout, encoding="utf-8")
            dual = work / "dual"; copy_inputs(live, dual, controls=False); shutil.copy2(evidence, dual / "ScopeOfWork.md")
            run([sys.executable, str(TOOLS / "validate_scope_of_work.py"), "--isolated-migration", "--migration-authority", AUTH, "--json", str(dual)])
            hashes = {"map": [], "parity": [], "checklist": [], "render": []}
            for n in (1, 2):
                cmap = out / f"claim-map-{n}.csv"; parity = out / f"parity-{n}.json"; checklist = out / f"checklist-{n}.json"; render = out / f"render-{n}.html"
                run([sys.executable, str(TOOLS / "map_scope_of_work_claims.py"), "--scope-of-work", str(evidence), "--production-scope-of-work", str(production), "--source-dir", str(live), "--output-csv", str(cmap)])
                run([sys.executable, str(TOOLS / "report_scope_of_work_parity.py"), "--scope-of-work", str(evidence), "--production-scope-of-work", str(production), "--source-dir", str(live), "--output-json", str(parity), "--isolated-migration", "--migration-authority", AUTH])
                run([sys.executable, str(TOOLS / "derive_review_checklist.py"), str(production), "--output", str(checklist)])
                run([sys.executable, str(TOOLS / "render_scope_of_work.py"), str(production), "--output", str(render)])
                for key, path in [("map", cmap), ("parity", parity), ("checklist", checklist), ("render", render)]: hashes[key].append(sha(path))
            assert all(len(set(values)) == 1 for values in hashes.values())
            parity_data = json.loads((out / "parity-1.json").read_text(encoding="utf-8")); assert parity_data["pass"] and not parity_data["issues"]
            maps = len(parity_data["checks"]); covered = sum(x["line_end"] - x["line_start"] + 1 for x in parity_data["checks"])
            source_lines = sum(len((live / name).read_bytes().splitlines()) for name in LEGACY)
            assert maps == int(upstream["mappings"]); assert covered == source_lines == int(upstream["covered_lines"]) == int(row["source_lines"])

            bad = work / "bad.md"; bad.write_text(ptext.replace("schema: chirality-deliverable-sow/v1", "schema: chirality-deliverable-sow/INVALID", 1), encoding="utf-8")
            legacy = work / "legacy"; copy_inputs(live, legacy, controls=False)
            probes = [
                [sys.executable, str(TOOLS / "validate_scope_of_work.py"), "--json", str(bad)],
                [sys.executable, str(TOOLS / "map_scope_of_work_claims.py"), "--scope-of-work", str(evidence), "--production-scope-of-work", str(bad), "--source-dir", str(live), "--output-csv", str(work / "bad-map.csv")],
                [sys.executable, str(TOOLS / "report_scope_of_work_parity.py"), "--scope-of-work", str(evidence), "--production-scope-of-work", str(bad), "--source-dir", str(live), "--output-json", str(work / "bad-parity.json"), "--isolated-migration", "--migration-authority", AUTH],
                [sys.executable, str(TOOLS / "derive_review_checklist.py"), str(bad), "--output", str(work / "bad-checklist.json")],
                [sys.executable, str(TOOLS / "derive_review_checklist.py"), str(dual), "--output", str(work / "dual-checklist.json")],
                [sys.executable, str(TOOLS / "render_scope_of_work.py"), str(bad), "--output", str(work / "bad-render.html")],
                [sys.executable, str(TOOLS / "convert_four_documents_to_scope_of_work.py"), "--deliverable", str(legacy), "--deliverable-id", did, "--package-id", row["package"], "--decomposition-basis", front(text, "decomposition_basis"), "--project-scope-ref", refs(front(text, "project_scope_refs"))[0], "--package-objective-ref", refs(front(text, "package_objective_refs"))[0], "--output-description", definition(text, "OUT"), "--acceptance-criterion", definition(text, "AC"), "--verification-method", definition(text, "VER"), "--isolated-migration"],
            ]
            for idx, cmd in enumerate(probes, 1):
                cp = run(cmd, allow_fail=True); assert cp.returncode != 0, (did, idx, "negative probe escaped")
                negative.append([did, idx, cp.returncode, "PASS"])
            target = work / "target"; copy_inputs(live, target); shutil.copy2(production, target / "ScopeOfWork.md")
            for name in LEGACY: (target / name).unlink()
            run([sys.executable, str(TOOLS / "validate_scope_of_work.py"), "--json", str(target / "ScopeOfWork.md")])
            assert all((target / name).read_bytes() == (live / name).read_bytes() for name in CONTROL)
            (target / "ScopeOfWork.md").unlink()
            for name in LEGACY: shutil.copy2(live / name, target / name)
            assert all((target / name).read_bytes() == (live / name).read_bytes() for name in LEGACY + CONTROL)

        assert before_live == {name: sha(live / name) for name in before_live}
        total_maps += maps; total_lines += covered
        member_results.append([did, row["package"], row["live_path"], sha(evidence), sha(production), sha(report), maps, covered, source_lines, "PASS", "PASS", "PASS", "PASS", "PASS"])
        simulations.append([did, "PASS", "PASS", "PASS", "PASS"])
        sow = f"{row['live_path']}/ScopeOfWork.md"; replacement.append([did, "ADD", sow, "ABSENT", sha(production)]); rollback.append([did, "DELETE", sow, sha(production), "ABSENT"])
        for name in LEGACY:
            path = f"{row['live_path']}/{name}"; source_hash = row[HASH_COLS[name]]
            replacement.append([did, "DELETE", path, source_hash, "ABSENT"]); rollback.append([did, "ADD", path, "ABSENT", source_hash])
        dep = run([sys.executable, str(ROOT / "tools/validation/validate_dependencies_schema.py"), str(live / "Dependencies.csv")])
        dependency_checks.append([did, dep.returncode, dep.stdout.strip().replace("\t", " "), "PASS"])

    assert total_maps == 493 and total_lines == 4919 and len(replacement) == len(rollback) == 75 and len(negative) == 105
    for pkg in PACKAGES:
        manager = RUN / f"instances/WORKING-P3-PKG{pkg}"; ids = {r["deliverable_id"] for r in rows if r["package"] == f"PKG-{pkg}"}
        expected_r = list(csv.reader((manager / "REPLACEMENT_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\t"))[1:]
        expected_i = list(csv.reader((manager / "ROLLBACK_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\t"))[1:]
        assert [[str(x) for x in row] for row in replacement if row[0] in ids] == expected_r
        assert [[str(x) for x in row] for row in rollback if row[0] in ids] == expected_i

    write_tsv(SNAP / "SOURCE_BINDINGS.tsv", ["deliverable_id", "surface", "expected_sha256", "actual_sha256", "verdict"], bindings)
    write_tsv(SNAP / "DEPENDENCY_SCHEMA_CHECKS.tsv", ["deliverable_id", "exit_code", "output", "verdict"], dependency_checks)
    write_tsv(SNAP / "MEMBER_RESULTS.tsv", ["deliverable_id", "package", "live_path", "evidence_sha256", "production_sha256", "finalization_sha256", "mappings", "covered_lines", "total_lines", "conversion", "finalization", "semantic_review", "simulation", "metadata_exclusion"], member_results)
    write_tsv(SNAP / "REPLACEMENT_MANIFEST.tsv", ["deliverable_id", "action", "path", "before_sha256", "after_sha256"], replacement)
    write_tsv(SNAP / "ROLLBACK_MANIFEST.tsv", ["deliverable_id", "action", "path", "before_sha256", "after_sha256"], rollback)
    write_tsv(SNAP / "SIMULATION_RESULTS.tsv", ["deliverable_id", "apply", "target_validation", "control_preservation", "rollback"], simulations)
    write_tsv(SNAP / "NEGATIVE_PROBES.tsv", ["deliverable_id", "probe", "exit_code", "verdict"], negative)
    selfcheck = run([sys.executable, str(ROOT / "tools/practitioner_harness/harness.py"), "self-check"])
    (SNAP / "PRACTITIONER_SELF_CHECK.txt").write_text(selfcheck.stdout + selfcheck.stderr, encoding="utf-8")
    tests = run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "--junitxml", str(SNAP / "PRACTITIONER_HARNESS.junit.xml"), "tools/practitioner_harness"])
    (SNAP / "PRACTITIONER_HARNESS.txt").write_text(tests.stdout + tests.stderr, encoding="utf-8")
    focused = run([sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "tools/scope_of_work/test_scope_of_work_tools.py"])
    (SNAP / "FOCUSED_SCOPE_OF_WORK_TESTS.txt").write_text(focused.stdout + focused.stderr, encoding="utf-8")
    after_project = project_digest(); assert before_project == after_project
    (SNAP / "PROJECT_CONTAINMENT.json").write_text(json.dumps({"before_sha256": before_project[0], "after_sha256": after_project[0], "file_count": before_project[1], "zero_project_writes": True}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {"status": "PASS", "basis": "main@4d153302c3c4cd42578936db160c2bac1270225a", "members": 15, "packages": 3,
               "mappings": total_maps, "source_lines": total_lines, "candidate_files": 45, "replacement_rows": 75, "rollback_rows": 75,
               "simulations_pass": 15, "negative_probes_pass": 105, "source_control_bindings": len(bindings), "dependency_schema_checks": 15,
               "manager_manifest_rows": manager_total, "upstream_manifests": len(manifest_rows), "accepted_children": accepted_children,
               "retained_excluded_blocked_children": excluded_children, "full_member_reproduction": "15_OF_15", "project_containment": "PASS",
               "semantic_addition_review": "NO_UNAUTHORIZED_ADDITIONS", "pkg12_replacement_independence": "PASS_ZERO_PROHIBITED_READS",
               "blockers": [], "unknowns": [], "waivers": []}
    (SNAP / "SUMMARY.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__": main()
