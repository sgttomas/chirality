#!/usr/bin/env python3
"""Reproduce W-P4 atomic replacement, rollback, and member evidence checks."""

from __future__ import annotations

import csv
import hashlib
import json
import shutil
import subprocess
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
SNAP = RUN / "snapshots/W_P4/preintegration"
CHANGE = RUN / "instances/CHANGE-P4"
CANDIDATES = RUN / "candidates/W_P4"
BASIS = "e8f59a63372f38d9e788ac39b39995558f5aba73"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(*args: str, text: bool = True) -> str | bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=text)


def run(args: list[str], *, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=ROOT, text=True, capture_output=capture, check=True)


def rows(name: str) -> list[dict[str, str]]:
    with (SNAP / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def main() -> None:
    replacement = rows("REPLACEMENT_MANIFEST.tsv")
    rollback = rows("ROLLBACK_MANIFEST.tsv")
    bindings = rows("SOURCE_BINDINGS.tsv")
    ids = list(dict.fromkeys(row["deliverable_id"] for row in replacement))
    assert len(replacement) == len(rollback) == 110
    assert len(ids) == 22

    commits = git("rev-list", "--reverse", f"{BASIS}..HEAD").splitlines()
    assert len(commits) == len(ids) == 22
    atomic = []
    for did, commit in zip(ids, commits, strict=True):
        expected = [row for row in replacement if row["deliverable_id"] == did]
        actual = git("diff-tree", "--no-commit-id", "--name-only", "-r", commit).splitlines()
        assert len(expected) == 5 and sorted(actual) == sorted(row["path"] for row in expected)
        for row in expected:
            spec = f"{commit}:{row['path']}"
            exists = subprocess.run(
                ["git", "cat-file", "-e", spec], cwd=ROOT, capture_output=True
            ).returncode == 0
            if row["operation"] == "DELETE":
                assert not exists
            else:
                assert exists and sha(git("show", spec, text=False)) == row["sha256"]
        atomic.append({"deliverable_id": did, "commit": commit, "paths": 5, "verdict": "PASS"})
    (CHANGE / "ATOMIC_COMMITS.json").write_text(json.dumps({
        "schema": "chirality-change-atomic-commit-audit/v1", "basis": BASIS,
        "verdict": "PASS", "commits": atomic,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    inverse = {(row["deliverable_id"], row["path"]): row for row in rollback}
    simulations = []
    for did in ids:
        member = [row for row in replacement if row["deliverable_id"] == did]
        original: dict[str, bytes] = {}
        state: dict[str, bytes] = {}
        for row in member:
            inv = inverse[(did, row["path"])]
            assert (row["operation"], inv["operation"]) in {("DELETE", "RESTORE"), ("ADD", "DELETE")}
            assert row["sha256"] == inv["sha256"]
            if row["operation"] == "DELETE":
                data = git("show", f"{BASIS}:{row['path']}", text=False)
                assert sha(data) == row["sha256"]
                original[row["path"]] = data
                state[row["path"]] = data
        candidate = next(iter(CANDIDATES.glob(f"PIP-PKG*/{did}/production/ScopeOfWork.md")))
        for row in member:
            if row["operation"] == "DELETE":
                assert sha(state.pop(row["path"])) == row["sha256"]
            else:
                data = candidate.read_bytes()
                assert sha(data) == row["sha256"]
                state[row["path"]] = data
        for row in (inverse[(did, item["path"])] for item in member):
            if row["operation"] == "RESTORE":
                state[row["path"]] = original[row["path"]]
            else:
                assert sha(state.pop(row["path"])) == row["sha256"]
        assert state == original
        simulations.append({"deliverable_id": did, "apply": "PASS", "target": "PASS", "rollback": "PASS"})
    actual_paths = git("diff", "--name-only", BASIS, "HEAD", "--", "projects/chirality-piping").splitlines()
    assert sorted(actual_paths) == sorted(row["path"] for row in replacement)
    (CHANGE / "SIMULATION.json").write_text(json.dumps({
        "schema": "chirality-change-replacement-simulation/v1", "verdict": "PASS",
        "replacement_rows": 110, "rollback_rows": 110, "simulations": simulations,
        "project_paths": 110,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    work = CHANGE / "checks"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir()
    results = []
    for did in ids:
        member = [row for row in replacement if row["deliverable_id"] == did]
        add = next(row for row in member if row["operation"] == "ADD")
        live = ROOT / add["path"]
        candidate = next(iter(CANDIDATES.glob(f"PIP-PKG*/{did}")))
        evidence = candidate / "evidence/ScopeOfWork.md"
        production = candidate / "production/ScopeOfWork.md"
        assert live.read_bytes() == production.read_bytes()
        out = work / did
        basis_dir = out / "basis"
        basis_dir.mkdir(parents=True)
        for row in member:
            if row["operation"] == "DELETE":
                data = git("show", f"{BASIS}:{row['path']}", text=False)
                (basis_dir / Path(row["path"]).name).write_bytes(data)
        validation = run(["python3", "tools/scope_of_work/validate_scope_of_work.py", str(live), "--json"], capture=True)
        parsed = json.loads(validation.stdout)
        assert parsed["valid"] and parsed["format"] == "SOW_V1"
        (out / "validation.json").write_text(json.dumps(parsed, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        run(["python3", "tools/scope_of_work/map_scope_of_work_claims.py", "--scope-of-work", str(evidence),
             "--production-scope-of-work", str(live), "--source-dir", str(basis_dir),
             "--output-csv", str(out / "claim-map.csv")])
        run(["python3", "tools/scope_of_work/report_scope_of_work_parity.py", "--scope-of-work", str(evidence),
             "--production-scope-of-work", str(live), "--source-dir", str(basis_dir),
             "--output-json", str(out / "parity.json"), "--output-md", str(out / "parity.md"),
             "--isolated-migration", "--migration-authority", "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176"])
        run(["python3", "tools/scope_of_work/derive_review_checklist.py", str(live), "--output", str(out / "checklist.json")])
        run(["python3", "tools/scope_of_work/finalize_scope_of_work.py", "--evidence-candidate", str(evidence),
             "--output", str(out / "finalized.md"), "--report", str(out / "finalization.json")])
        assert (out / "finalized.md").read_bytes() == production.read_bytes()
        assert (out / "finalization.json").read_bytes() == (candidate / "finalization.json").read_bytes()
        shutil.rmtree(basis_dir)
        controls = [row for row in bindings if row["deliverable_id"] == did]
        assert all(row["verdict"] == "PASS" and row["expected_sha256"] == row["actual_sha256"] for row in controls)
        results.append({"deliverable_id": did, "format": "PASS", "mapping": "PASS", "parity": "PASS",
                        "checklist": "PASS", "finalization": "PASS", "control_bindings": len(controls),
                        "live_sha256": sha(live.read_bytes())})
    (CHANGE / "MEMBER_CHECKS.json").write_text(json.dumps({
        "schema": "chirality-change-member-checks/v1", "verdict": "PASS",
        "members": len(results), "results": results,
    }, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"verdict": "PASS", "members": 22, "atomic_commits": 22,
                      "replacement_rows": 110, "rollback_rows": 110}, sort_keys=True))


if __name__ == "__main__":
    main()
