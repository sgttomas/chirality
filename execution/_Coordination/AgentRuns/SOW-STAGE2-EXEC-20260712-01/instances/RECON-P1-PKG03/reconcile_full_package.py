#!/usr/bin/env python3
"""Independent full-package PKG-03 reconciliation into the sealed snapshot."""

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
UPSTREAM = RUN / "instances/WORKING-P1-PKG03"
HERE = RUN / "instances/RECON-P1-PKG03"
SNAP = RUN / "snapshots/W_P1/PKG03-preintegration"
PREFLIGHT = RUN / "snapshots/W_P1/preflight-r1"
CAND = RUN / "candidates/W_P1/PIP-PKG03"
TOOLS = ROOT / "tools/scope_of_work"
AUTH = "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"
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
        h.update(len(rel).to_bytes(8, "big")); h.update(rel)
        data = path.read_bytes()
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

    manifests = [UPSTREAM / "MANIFEST.tsv"] + [
        UPSTREAM / "children" / child / "MANIFEST.tsv" for child in
        ["BATCH-01-AUTHOR", "BATCH-01-VERIFY", "BATCH-02-AUTHOR", "BATCH-02-VERIFY"]
    ]
    manifest_rows = []
    for manifest in manifests:
        count, digest = audit_manifest(manifest)
        manifest_rows.append([manifest.relative_to(ROOT).as_posix(), count, digest, "PASS"])
    write_tsv(SNAP / "UPSTREAM_MANIFEST_AUDIT.tsv",
              ["manifest", "rows", "sha256", "verdict"], manifest_rows)

    child_index = list(csv.DictReader((UPSTREAM / "CHILD_INDEX.tsv").open(), delimiter="\t"))
    assert len(child_index) == 4
    assert [r["terminal_verdict"] for r in child_index] == ["PASS", "PASS_UNCHANGED", "PASS", "PASS_UNCHANGED"]

    rows = [r for r in csv.DictReader((PREFLIGHT / "P1_MANIFEST.tsv").open(), delimiter="\t")
            if r["package"] == "PKG-03"]
    assert [r["deliverable_id"] for r in rows] == [f"DEL-03-{i:02d}" for i in range(1, 9)]
    upstream_members = {r["deliverable_id"]: r for r in csv.DictReader(
        (UPSTREAM / "MEMBER_RESULTS.tsv").open(), delimiter="\t")}

    members = []
    replacements = []
    rollbacks = []
    simulations = []
    total_maps = total_lines = 0
    for row in rows:
        did = row["deliverable_id"]
        live = ROOT / row["live_path"]
        evidence = CAND / did / "evidence/ScopeOfWork.md"
        production = CAND / did / "production/ScopeOfWork.md"
        finalization = CAND / did / "finalization.json"
        out = detail / did
        out.mkdir()
        assert row["lifecycle"] == "IN_PROGRESS"
        assert not (live / "ScopeOfWork.md").exists()
        for name, col in HASH_COLS.items():
            assert sha(live / name) == row[col], (did, name, "source drift")

        final = json.loads(finalization.read_text())
        assert final["schema"] == "chirality-sow-finalization/v1"
        assert final["evidence_candidate_sha256"] == sha(evidence)
        assert final["production_scope_of_work_sha256"] == sha(production)
        assert final["source_block_count"] == len(final["source_blocks"])
        assert upstream_members[did]["evidence_sha256"] == sha(evidence)
        assert upstream_members[did]["production_sha256"] == sha(production)
        assert upstream_members[did]["finalization_sha256"] == sha(finalization)

        clean = run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(production)])
        (out / "validation-clean.json").write_text(clean.stdout, encoding="utf-8")
        run(["python3", str(TOOLS / "map_scope_of_work_claims.py"),
             "--scope-of-work", str(evidence), "--production-scope-of-work", str(production),
             "--source-dir", str(live), "--output-csv", str(out / "claim-map.csv")])
        run(["python3", str(TOOLS / "report_scope_of_work_parity.py"),
             "--scope-of-work", str(evidence), "--production-scope-of-work", str(production),
             "--source-dir", str(live), "--output-json", str(out / "parity.json"),
             "--output-md", str(out / "parity.md"), "--isolated-migration",
             "--migration-authority", AUTH])
        for suffix in ("a", "b"):
            run(["python3", str(TOOLS / "derive_review_checklist.py"), str(production),
                 "--output", str(out / f"checklist-{suffix}.json")])
            run(["python3", str(TOOLS / "render_scope_of_work.py"), str(production),
                 "--output", str(out / f"render-{suffix}.html")])
        assert (out / "checklist-a.json").read_bytes() == (out / "checklist-b.json").read_bytes()
        assert (out / "render-a.html").read_bytes() == (out / "render-b.html").read_bytes()
        html = (out / "render-a.html").read_text(encoding="utf-8").lower()
        assert "<script" not in html and "http://" not in html and "https://" not in html

        parity = json.loads((out / "parity.json").read_text())
        assert parity["pass"] and not parity["issues"]
        maps = len(parity["checks"])
        lines = sum(x["line_end"] - x["line_start"] + 1 for x in parity["checks"])
        expected_lines = sum(len((live / name).read_bytes().splitlines()) for name in LEGACY)
        assert maps == int(upstream_members[did]["mappings"])
        assert lines == expected_lines == int(upstream_members[did]["covered_lines"])
        total_maps += maps; total_lines += lines

        with tempfile.TemporaryDirectory(prefix=f"recon-pkg03-{did}-") as td:
            tdpath = Path(td)
            dual = tdpath / "dual"
            copy_inputs(live, dual)
            shutil.copy2(evidence, dual / "ScopeOfWork.md")
            isolated = run(["python3", str(TOOLS / "validate_scope_of_work.py"),
                            "--isolated-migration", "--migration-authority", AUTH,
                            "--json", str(dual)])
            (out / "validation-isolated-dual.json").write_text(isolated.stdout, encoding="utf-8")
            unauthorized = run(["python3", str(TOOLS / "validate_scope_of_work.py"),
                                "--json", str(dual)], allow_fail=True)
            assert unauthorized.returncode != 0
            (out / "negative-unauthorized-dual.txt").write_text(
                f"exit={unauthorized.returncode}\n{unauthorized.stdout}{unauthorized.stderr}", encoding="utf-8")
            partial = tdpath / "partial"
            partial.mkdir()
            shutil.copy2(live / "Datasheet.md", partial / "Datasheet.md")
            shutil.copy2(live / "_STATUS.md", partial / "_STATUS.md")
            partial_cp = run(["python3", str(TOOLS / "validate_scope_of_work.py"),
                              "--json", str(partial)], allow_fail=True)
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

        members.append([did, row["live_path"], sha(evidence), sha(production), sha(finalization),
                        maps, lines, expected_lines, "PASS", "PASS", "PASS", "PASS"])
        sow_path = f"{row['live_path']}/ScopeOfWork.md"
        replacements.append([did, "ADD", sow_path, "ABSENT", sha(production)])
        rollbacks.append([did, "DELETE", sow_path, sha(production), "ABSENT"])
        for name in LEGACY:
            path = f"{row['live_path']}/{name}"
            source_hash = row[HASH_COLS[name]]
            replacements.append([did, "DELETE", path, source_hash, "ABSENT"])
            rollbacks.append([did, "ADD", path, "ABSENT", source_hash])

    assert total_maps == 234 and total_lines == 1966
    assert len(replacements) == len(rollbacks) == 40
    upstream_replacement = list(csv.reader((UPSTREAM / "REPLACEMENT_MANIFEST.tsv").open(), delimiter="\t"))[1:]
    upstream_rollback = list(csv.reader((UPSTREAM / "ROLLBACK_MANIFEST.tsv").open(), delimiter="\t"))[1:]
    assert [[str(x) for x in row] for row in replacements] == upstream_replacement
    assert [[str(x) for x in row] for row in rollbacks] == upstream_rollback

    write_tsv(SNAP / "MEMBER_RESULTS.tsv",
              ["deliverable_id", "live_path", "evidence_sha256", "production_sha256",
               "finalization_sha256", "mappings", "covered_lines", "total_lines", "schema",
               "content_authority", "preservation_containment", "execution_substrate"], members)
    write_tsv(SNAP / "REPLACEMENT_MANIFEST.tsv",
              ["deliverable_id", "action", "path", "before_sha256", "after_sha256"], replacements)
    write_tsv(SNAP / "ROLLBACK_MANIFEST.tsv",
              ["deliverable_id", "action", "path", "before_sha256", "after_sha256"], rollbacks)
    write_tsv(SNAP / "SIMULATION_RESULTS.tsv",
              ["deliverable_id", "apply", "target_validation", "control_preservation", "rollback"], simulations)

    self_check = run(["python3", "tools/practitioner_harness/harness.py", "self-check"])
    (SNAP / "PRACTITIONER_SELF_CHECK.txt").write_text(self_check.stdout + self_check.stderr, encoding="utf-8")
    pytest = run(["python3", "-m", "pytest", "-q", "-p", "no:cacheprovider",
                  "--junitxml", str(SNAP / "PRACTITIONER_HARNESS.junit.xml"), "tools/practitioner_harness"])
    (SNAP / "PRACTITIONER_HARNESS.txt").write_text(pytest.stdout + pytest.stderr, encoding="utf-8")
    after_hash, after_files = project_digest()
    assert (before_hash, before_files) == (after_hash, after_files)
    containment = {
        "project_tree_before_sha256": before_hash, "project_tree_after_sha256": after_hash,
        "project_file_count_before": before_files, "project_file_count_after": after_files,
        "zero_project_writes": True,
    }
    (SNAP / "PROJECT_CONTAINMENT.json").write_text(json.dumps(containment, indent=2, sort_keys=True) + "\n")
    summary = {
        "status": "PASS_PENDING_AGENT2_FANIN", "members": 8, "terminal_children": 4,
        "mappings": total_maps, "source_lines": total_lines, "replacement_rows": 40,
        "rollback_rows": 40, "simulations_pass": 8, "negative_probes_pass": 16,
        "upstream_manifests": 5, "project_checks": "PASS",
        "project_containment": "PASS", "schema": "PASS", "content_authority": "PASS",
        "preservation_containment": "PASS", "execution_substrate": "PASS",
    }
    (SNAP / "SUMMARY.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
