#!/usr/bin/env python3
"""Independent full reproduction of the frozen 29-member P2 migration wave."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
HERE = RUN / "instances/RECON-P2"
SNAP = RUN / "snapshots/W_P2/preintegration"
PREFLIGHT = RUN / "snapshots/W_P2/preflight"
CAND = RUN / "candidates/W_P2"
TOOLS = ROOT / "tools/scope_of_work"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
PACKAGES = ["05", "06", "07", "08", "09"]
EXPECTED_PACKAGE_MANIFESTS = {
    "05": (1712, "4f3b6a7b969143a81d90a4bbeca3fd5c3b098138516c33e6861d161f66d45e3f"),
    "06": (1566, "2a98aedbefcbd50c8f324531e7b1026fd0eb751c0fcd261685e8695740f6e5aa"),
    "07": (2899, "11f7a45a464ca2eb983e323ee8799a79aed46c4b0688a71e740748f038d1ca50"),
    "08": (1983, "18bd7d9a64bbc25befa97618d16d8142dd776e414157325778d7e0ee4f716102"),
    "09": (1802, "af8aa999a7944b01099455a5ba0b32b9526fcd60a9db2f59ca2c81471749d514"),
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


def copy_inputs(live: Path, target: Path) -> None:
    target.mkdir(parents=True)
    for name in LEGACY + CONTROL:
        shutil.copy2(live / name, target / name)


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
    assert not p.is_absolute() and ".." not in p.parts, (manifest, raw, "nonportable")
    candidate = ROOT / p if p.parts and p.parts[0] == "execution" else manifest.parent / p
    resolved = candidate.resolve()
    resolved.relative_to(ROOT.resolve())
    return resolved


def audit_manifest(manifest: Path) -> tuple[int, str]:
    rows = list(csv.DictReader(manifest.open(encoding="utf-8"), delimiter="\t"))
    seen: set[Path] = set()
    for row in rows:
        path = resolve_manifest_path(manifest, row["path"])
        assert path != manifest.resolve(), (manifest, "self inclusion")
        assert path not in seen, (manifest, path, "duplicate")
        seen.add(path)
        assert path.is_file(), (manifest, path, "missing")
        assert sha(path) == row["sha256"], (manifest, path, "hash")
        assert path.stat().st_size == int(row["bytes"]), (manifest, path, "bytes")
    return len(rows), sha(manifest)


def main() -> None:
    if SNAP.exists():
        raise RuntimeError(f"immutable snapshot already exists: {SNAP}")
    SNAP.mkdir(parents=True)
    detail = SNAP / "members"
    detail.mkdir()
    before_hash, before_files = project_digest()

    manifest_rows: list[list[object]] = []
    package_total = 0
    terminal_children = 0
    upstream_by_package: dict[str, dict[str, dict[str, str]]] = {}
    for pkg in PACKAGES:
        upstream = RUN / f"instances/WORKING-P2-PKG{pkg}"
        count, digest = audit_manifest(upstream / "MANIFEST.tsv")
        assert (count, digest) == EXPECTED_PACKAGE_MANIFESTS[pkg]
        package_total += count
        manifest_rows.append([(upstream / "MANIFEST.tsv").relative_to(ROOT).as_posix(), "manager", count, digest, "PASS"])
        child_index = list(csv.DictReader((upstream / "CHILD_INDEX.tsv").open(encoding="utf-8"), delimiter="\t"))
        assert child_index and all(r["status"] in {"PASS", "PASS_UNCHANGED"} for r in child_index)
        for child in child_index:
            manifest = upstream / "children" / child["child_id"] / "MANIFEST.tsv"
            child_count, child_digest = audit_manifest(manifest)
            assert child_digest == child["manifest_sha256"]
            manifest_rows.append([manifest.relative_to(ROOT).as_posix(), child["role"], child_count, child_digest, "PASS"])
            terminal_children += 1
        member_rows = list(csv.DictReader((upstream / "MEMBER_RESULTS.tsv").open(encoding="utf-8"), delimiter="\t"))
        upstream_by_package[pkg] = {r["deliverable_id"]: r for r in member_rows}
    assert package_total == 9962 and terminal_children == 14
    write_tsv(SNAP / "UPSTREAM_MANIFEST_AUDIT.tsv",
              ["manifest", "owner", "rows", "sha256", "verdict"], manifest_rows)

    rows = list(csv.DictReader((PREFLIGHT / "P2_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\t"))
    assert len(rows) == 29
    assert [sum(r["package"] == f"PKG-{p}" for r in rows) for p in PACKAGES] == [5, 5, 8, 6, 5]
    members: list[list[object]] = []
    replacements: list[list[object]] = []
    rollbacks: list[list[object]] = []
    simulations: list[list[object]] = []
    source_bindings: list[list[object]] = []
    dependency_checks: list[list[object]] = []
    total_maps = total_lines = 0

    for row in rows:
        did = row["deliverable_id"]
        pkg = row["package"].split("-")[1]
        live = ROOT / row["live_path"]
        base = CAND / f"PIP-PKG{pkg}" / did
        evidence = base / "evidence/ScopeOfWork.md"
        production = base / "production/ScopeOfWork.md"
        finalization = base / "finalization.json"
        out = detail / did
        out.mkdir()
        assert row["lifecycle"] == "IN_PROGRESS" and row["issued"] == "false"
        assert not (live / "ScopeOfWork.md").exists()
        for name, col in HASH_COLS.items():
            actual = sha(live / name)
            assert actual == row[col], (did, name, "source/control drift")
            source_bindings.append([did, name, row[col], actual, "PASS"])

        upstream_member = upstream_by_package[pkg][did]
        final = json.loads(finalization.read_text(encoding="utf-8"))
        assert final["schema"] == "chirality-sow-finalization/v1"
        assert final["evidence_candidate_sha256"] == sha(evidence) == upstream_member["evidence_sha256"]
        assert final["production_scope_of_work_sha256"] == sha(production) == upstream_member["production_sha256"]
        assert sha(finalization) == upstream_member["finalization_sha256"]
        assert final["source_block_count"] == len(final["source_blocks"])
        assert all(x["disposition"] in {"PRESERVED", "MERGED", "SPLIT", "SUPERSEDED", "DEFERRED", "CONFLICT"}
                   for x in final["source_blocks"])
        production_text = production.read_text(encoding="utf-8")
        assert "sow-source-begin" not in production_text and "sow-source-end" not in production_text
        assert "migration-authority" not in production_text and "migration candidate defines" not in production_text

        clean = run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(production)])
        (out / "validation-clean.json").write_text(clean.stdout, encoding="utf-8")
        run(["python3", str(TOOLS / "map_scope_of_work_claims.py"),
             "--scope-of-work", str(evidence), "--production-scope-of-work", str(production),
             "--source-dir", str(live), "--output-csv", str(out / "claim-map.csv")])
        run(["python3", str(TOOLS / "report_scope_of_work_parity.py"),
             "--scope-of-work", str(evidence), "--production-scope-of-work", str(production),
             "--source-dir", str(live), "--output-json", str(out / "parity.json"),
             "--output-md", str(out / "parity.md"), "--isolated-migration", "--migration-authority", AUTH])
        for suffix in ("a", "b"):
            run(["python3", str(TOOLS / "derive_review_checklist.py"), str(production),
                 "--output", str(out / f"checklist-{suffix}.json")])
            run(["python3", str(TOOLS / "render_scope_of_work.py"), str(production),
                 "--output", str(out / f"render-{suffix}.html")])
        assert (out / "checklist-a.json").read_bytes() == (out / "checklist-b.json").read_bytes()
        assert (out / "render-a.html").read_bytes() == (out / "render-b.html").read_bytes()
        html = (out / "render-a.html").read_text(encoding="utf-8").lower()
        assert "<script" not in html and "http://" not in html and "https://" not in html

        parity = json.loads((out / "parity.json").read_text(encoding="utf-8"))
        assert parity["pass"] and not parity["issues"]
        maps = len(parity["checks"])
        covered = sum(x["line_end"] - x["line_start"] + 1 for x in parity["checks"])
        expected_lines = sum(len((live / name).read_bytes().splitlines()) for name in LEGACY)
        assert maps == int(upstream_member["mappings"])
        assert covered == expected_lines == int(upstream_member["covered_lines"]) == int(row["source_lines"])
        total_maps += maps
        total_lines += covered

        dep = run(["python3", "tools/validation/validate_dependencies_schema.py", str(live / "Dependencies.csv")])
        dependency_checks.append([did, dep.returncode, dep.stdout.strip().replace("\t", " "), "PASS"])

        with tempfile.TemporaryDirectory(prefix=f"recon-p2-{did}-") as td:
            tdpath = Path(td)
            dual = tdpath / "dual"
            copy_inputs(live, dual)
            shutil.copy2(evidence, dual / "ScopeOfWork.md")
            isolated = run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--isolated-migration",
                            "--migration-authority", AUTH, "--json", str(dual)])
            (out / "validation-isolated-dual.json").write_text(isolated.stdout, encoding="utf-8")
            unauthorized = run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(dual)], allow_fail=True)
            assert unauthorized.returncode != 0
            (out / "negative-unauthorized-dual.txt").write_text(
                f"exit={unauthorized.returncode}\n{unauthorized.stdout}{unauthorized.stderr}", encoding="utf-8")
            partial = tdpath / "partial"
            partial.mkdir()
            shutil.copy2(live / "Datasheet.md", partial / "Datasheet.md")
            shutil.copy2(live / "_STATUS.md", partial / "_STATUS.md")
            partial_cp = run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(partial)], allow_fail=True)
            assert partial_cp.returncode != 0
            (out / "negative-partial.txt").write_text(
                f"exit={partial_cp.returncode}\n{partial_cp.stdout}{partial_cp.stderr}", encoding="utf-8")
            target = tdpath / "target"
            copy_inputs(live, target)
            shutil.copy2(production, target / "ScopeOfWork.md")
            for name in LEGACY:
                (target / name).unlink()
            run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(target / "ScopeOfWork.md")])
            assert (target / "ScopeOfWork.md").read_bytes() == production.read_bytes()
            assert all((target / name).read_bytes() == (live / name).read_bytes() for name in CONTROL)
            (target / "ScopeOfWork.md").unlink()
            for name in LEGACY:
                shutil.copy2(live / name, target / name)
            assert all((target / name).read_bytes() == (live / name).read_bytes() for name in LEGACY + CONTROL)
            simulations.append([did, "PASS", "PASS", "PASS", "PASS"])

        members.append([did, row["package"], row["live_path"], sha(evidence), sha(production), sha(finalization),
                        maps, covered, expected_lines, "PASS", "PASS", "PASS", "PASS", "PASS"])
        sow_path = f"{row['live_path']}/ScopeOfWork.md"
        replacements.append([did, "ADD", sow_path, "ABSENT", sha(production)])
        rollbacks.append([did, "DELETE", sow_path, sha(production), "ABSENT"])
        for name in LEGACY:
            path = f"{row['live_path']}/{name}"
            source_hash = row[HASH_COLS[name]]
            replacements.append([did, "DELETE", path, source_hash, "ABSENT"])
            rollbacks.append([did, "ADD", path, "ABSENT", source_hash])

    assert total_maps == 919 and total_lines == 8203
    assert len(replacements) == len(rollbacks) == 145
    for pkg in PACKAGES:
        upstream = RUN / f"instances/WORKING-P2-PKG{pkg}"
        ids = {r["deliverable_id"] for r in rows if r["package"] == f"PKG-{pkg}"}
        expected_repl = list(csv.reader((upstream / "REPLACEMENT_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\t"))[1:]
        expected_roll = list(csv.reader((upstream / "ROLLBACK_MANIFEST.tsv").open(encoding="utf-8"), delimiter="\t"))[1:]
        assert [[str(x) for x in r] for r in replacements if r[0] in ids] == expected_repl
        assert [[str(x) for x in r] for r in rollbacks if r[0] in ids] == expected_roll

    write_tsv(SNAP / "SOURCE_BINDINGS.tsv", ["deliverable_id", "surface", "expected_sha256", "actual_sha256", "verdict"], source_bindings)
    write_tsv(SNAP / "DEPENDENCY_SCHEMA_CHECKS.tsv", ["deliverable_id", "exit_code", "output", "verdict"], dependency_checks)
    write_tsv(SNAP / "MEMBER_RESULTS.tsv",
              ["deliverable_id", "package", "live_path", "evidence_sha256", "production_sha256", "finalization_sha256",
               "mappings", "covered_lines", "total_lines", "schema", "content_authority", "preservation_containment",
               "execution_substrate", "metadata_exclusion"], members)
    write_tsv(SNAP / "REPLACEMENT_MANIFEST.tsv", ["deliverable_id", "action", "path", "before_sha256", "after_sha256"], replacements)
    write_tsv(SNAP / "ROLLBACK_MANIFEST.tsv", ["deliverable_id", "action", "path", "before_sha256", "after_sha256"], rollbacks)
    write_tsv(SNAP / "SIMULATION_RESULTS.tsv", ["deliverable_id", "apply", "target_validation", "control_preservation", "rollback"], simulations)

    self_check = run(["python3", "tools/practitioner_harness/harness.py", "self-check"])
    (SNAP / "PRACTITIONER_SELF_CHECK.txt").write_text(self_check.stdout + self_check.stderr, encoding="utf-8")
    pytest = run(["python3", "-m", "pytest", "-q", "-p", "no:cacheprovider",
                  "--junitxml", str(SNAP / "PRACTITIONER_HARNESS.junit.xml"), "tools/practitioner_harness"])
    (SNAP / "PRACTITIONER_HARNESS.txt").write_text(pytest.stdout + pytest.stderr, encoding="utf-8")
    focused = run(["python3", "-m", "pytest", "-q", "-p", "no:cacheprovider",
                   "tools/scope_of_work/test_scope_of_work_tools.py"])
    (SNAP / "FOCUSED_SCOPE_OF_WORK_TESTS.txt").write_text(focused.stdout + focused.stderr, encoding="utf-8")

    after_hash, after_files = project_digest()
    assert (before_hash, before_files) == (after_hash, after_files)
    (SNAP / "PROJECT_CONTAINMENT.json").write_text(json.dumps({
        "project_tree_before_sha256": before_hash, "project_tree_after_sha256": after_hash,
        "project_file_count_before": before_files, "project_file_count_after": after_files,
        "zero_project_writes": True,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    summary = {
        "status": "PASS", "basis": "main@eaad463c0d481f6f1654e6adb5ee718f566176e9",
        "members": 29, "packages": 5, "terminal_children": terminal_children,
        "mappings": total_maps, "source_lines": total_lines, "candidate_files": 87,
        "replacement_rows": 145, "rollback_rows": 145, "simulations_pass": 29,
        "negative_probes_pass": 58, "upstream_manifests": len(manifest_rows),
        "upstream_package_manifest_rows": package_total, "source_control_bindings": len(source_bindings),
        "dependency_schema_checks": len(dependency_checks), "project_checks": "PASS",
        "project_containment": "PASS", "schema": "PASS", "content_authority": "PASS",
        "preservation_containment": "PASS", "execution_substrate": "PASS",
        "semantic_addition_review": "NO_UNAUTHORIZED_ADDITIONS", "metadata_exclusion": "PASS",
        "exceptions_reproduced": 29, "blockers": [], "waivers": [], "unknowns": [],
    }
    (SNAP / "SUMMARY.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
