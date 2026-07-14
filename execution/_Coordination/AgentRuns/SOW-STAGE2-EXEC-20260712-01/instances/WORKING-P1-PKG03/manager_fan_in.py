#!/usr/bin/env python3
"""Deterministic WORKING-P1-PKG03 package fan-in within the sealed instance."""

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
INSTANCE = RUN / "instances/WORKING-P1-PKG03"
CANDIDATES = RUN / "candidates/W_P1/PIP-PKG03"
PREFLIGHT = RUN / "snapshots/W_P1/preflight-r1"
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


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(args, cwd=ROOT, text=True, capture_output=True,
                            env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    if result.returncode:
        raise RuntimeError(f"exit {result.returncode}: {' '.join(args)}\n{result.stdout}\n{result.stderr}")
    return result


def write_tsv(path: Path, header: list[str], rows: list[list[object]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(header)
        writer.writerows(rows)


def copy_kit(live: Path, target: Path) -> None:
    target.mkdir(parents=True)
    for name in LEGACY + CONTROL:
        shutil.copy2(live / name, target / name)


def main() -> None:
    validation = INSTANCE / "manager-validation"
    if validation.exists():
        shutil.rmtree(validation)
    validation.mkdir()
    rows = [r for r in csv.DictReader((PREFLIGHT / "P1_MANIFEST.tsv").open(), delimiter="\t") if r["package"] == "PKG-03"]
    assert [r["deliverable_id"] for r in rows] == [f"DEL-03-{i:02d}" for i in range(1, 9)]
    member_rows, replacement_rows, rollback_rows, simulation_rows = [], [], [], []
    total_maps = total_lines = 0

    for row in rows:
        did = row["deliverable_id"]
        live = ROOT / row["live_path"]
        candidate = CANDIDATES / did
        evidence = candidate / "evidence/ScopeOfWork.md"
        production = candidate / "production/ScopeOfWork.md"
        report = candidate / "finalization.json"
        out = validation / did
        out.mkdir()
        assert row["lifecycle"] == "IN_PROGRESS" and not (live / "ScopeOfWork.md").exists()
        for name, col in HASH_COLS.items():
            assert sha(live / name) == row[col], (did, name)

        final = json.loads(report.read_text())
        assert final["evidence_candidate_sha256"] == sha(evidence)
        assert final["production_scope_of_work_sha256"] == sha(production)
        clean = run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(production)])
        (out / "validation-sow-v1.json").write_text(clean.stdout, encoding="utf-8")

        with tempfile.TemporaryDirectory(prefix=f"pkg03-{did}-") as td:
            dual = Path(td) / "dual"
            copy_kit(live, dual)
            shutil.copy2(evidence, dual / "ScopeOfWork.md")
            dual_check = run(["python3", str(TOOLS / "validate_scope_of_work.py"),
                              "--isolated-migration", "--migration-authority", AUTH,
                              "--json", str(dual)])
            (out / "validation-dual.json").write_text(dual_check.stdout, encoding="utf-8")

            target = Path(td) / "target"
            copy_kit(live, target)
            shutil.copy2(production, target / "ScopeOfWork.md")
            for name in LEGACY:
                (target / name).unlink()
            run(["python3", str(TOOLS / "validate_scope_of_work.py"), "--json", str(target / "ScopeOfWork.md")])
            assert (target / "ScopeOfWork.md").read_bytes() == production.read_bytes()
            for name in CONTROL:
                assert (target / name).read_bytes() == (live / name).read_bytes()
            (target / "ScopeOfWork.md").unlink()
            for name in LEGACY:
                shutil.copy2(live / name, target / name)
            assert all((target / name).read_bytes() == (live / name).read_bytes() for name in LEGACY + CONTROL)
            simulation_rows.append([did, "PASS", "PASS", "PASS"])

        run(["python3", str(TOOLS / "map_scope_of_work_claims.py"),
             "--scope-of-work", str(evidence), "--production-scope-of-work", str(production),
             "--source-dir", str(live), "--output-csv", str(out / "claim-map.csv")])
        run(["python3", str(TOOLS / "report_scope_of_work_parity.py"),
             "--scope-of-work", str(evidence), "--production-scope-of-work", str(production),
             "--source-dir", str(live), "--output-json", str(out / "parity.json"),
             "--output-md", str(out / "parity.md"), "--isolated-migration",
             "--migration-authority", AUTH])
        run(["python3", str(TOOLS / "derive_review_checklist.py"), str(production),
             "--output", str(out / "checklist.json")])
        run(["python3", str(TOOLS / "render_scope_of_work.py"), str(production),
             "--output", str(out / "render.html")])
        parity = json.loads((out / "parity.json").read_text())
        assert parity["pass"] and not parity["issues"]
        maps = len(parity["checks"])
        lines = sum(x["line_end"] - x["line_start"] + 1 for x in parity["checks"])
        expected_lines = sum(len((live / name).read_bytes().splitlines()) for name in LEGACY)
        assert lines == expected_lines
        total_maps += maps; total_lines += lines

        member_rows.append([did, row["live_path"], row["status_sha256"], sha(evidence),
                            sha(production), sha(report), maps, lines, expected_lines,
                            "PASS", "PASS_UNCHANGED"])
        prod_rel = f"{row['live_path']}/ScopeOfWork.md"
        replacement_rows.append([did, "ADD", prod_rel, "ABSENT", sha(production)])
        rollback_rows.append([did, "DELETE", prod_rel, sha(production), "ABSENT"])
        for name in LEGACY:
            rel = f"{row['live_path']}/{name}"
            source_hash = row[HASH_COLS[name]]
            replacement_rows.append([did, "DELETE", rel, source_hash, "ABSENT"])
            rollback_rows.append([did, "ADD", rel, "ABSENT", source_hash])

    assert total_lines == 1966 and len(replacement_rows) == len(rollback_rows) == 40
    write_tsv(INSTANCE / "MEMBER_RESULTS.tsv",
              ["deliverable_id", "live_path", "status_sha256", "evidence_sha256",
               "production_sha256", "finalization_sha256", "mappings", "covered_lines",
               "total_lines", "author", "verifier"], member_rows)
    write_tsv(INSTANCE / "REPLACEMENT_MANIFEST.tsv",
              ["deliverable_id", "action", "path", "before_sha256", "after_sha256"], replacement_rows)
    write_tsv(INSTANCE / "ROLLBACK_MANIFEST.tsv",
              ["deliverable_id", "action", "path", "before_sha256", "after_sha256"], rollback_rows)
    write_tsv(INSTANCE / "SIMULATION.tsv",
              ["deliverable_id", "apply", "target_validation", "rollback"], simulation_rows)
    summary = {"members": 8, "mappings": total_maps, "source_lines": total_lines,
               "replacement_rows": 40, "rollback_rows": 40, "simulations_pass": 8,
               "status": "PASS"}
    (INSTANCE / "MANAGER_VALIDATION.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
