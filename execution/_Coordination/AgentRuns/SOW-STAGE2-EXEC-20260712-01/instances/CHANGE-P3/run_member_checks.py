#!/usr/bin/env python3
"""Reproduce every W-P3 member check against live and accepted bytes."""

from __future__ import annotations

import csv
import hashlib
import json
import shutil
import subprocess
from pathlib import Path


ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
RUN = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01"
SNAP = RUN / "snapshots/W_P3/preintegration"
CHANGE = RUN / "instances/CHANGE-P3"
CANDIDATES = RUN / "candidates/W_P3"
BASIS = "4d153302c3c4cd42578936db160c2bac1270225a"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def run(args: list[str], *, capture: bool = False) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        capture_output=capture,
        check=True,
    )


def main() -> None:
    with (SNAP / "REPLACEMENT_MANIFEST.tsv").open(encoding="utf-8", newline="") as handle:
        replacements = list(csv.DictReader(handle, delimiter="\t"))
    ids = list(dict.fromkeys(row["deliverable_id"] for row in replacements))
    assert len(ids) == 15
    work = CHANGE / "checks"
    if work.exists():
        shutil.rmtree(work)
    work.mkdir()
    results: list[dict[str, object]] = []

    for deliverable_id in ids:
        rows = [row for row in replacements if row["deliverable_id"] == deliverable_id]
        add = next(row for row in rows if row["action"] == "ADD")
        live = ROOT / add["path"]
        source_dir = work / deliverable_id / "basis"
        source_dir.mkdir(parents=True)
        for row in rows:
            if row["before_sha256"] == "ABSENT":
                continue
            data = subprocess.check_output(["git", "show", f"{BASIS}:{row['path']}"], cwd=ROOT)
            assert sha(data) == row["before_sha256"]
            (source_dir / Path(row["path"]).name).write_bytes(data)

        matches = list(CANDIDATES.glob(f"PIP-PKG*/{deliverable_id}"))
        assert len(matches) == 1, (deliverable_id, matches)
        candidate = matches[0]
        evidence = candidate / "evidence/ScopeOfWork.md"
        production = candidate / "production/ScopeOfWork.md"
        finalization = candidate / "finalization.json"
        assert live.read_bytes() == production.read_bytes()

        out = work / deliverable_id
        validation = run(
            ["python3", "tools/scope_of_work/validate_scope_of_work.py", str(live), "--json"],
            capture=True,
        )
        validation_json = json.loads(validation.stdout)
        assert validation_json["valid"] and validation_json["format"] == "SOW_V1"
        (out / "validation.json").write_text(
            json.dumps(validation_json, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )

        run([
            "python3", "tools/scope_of_work/map_scope_of_work_claims.py",
            "--scope-of-work", str(evidence),
            "--production-scope-of-work", str(live),
            "--source-dir", str(source_dir),
            "--output-csv", str(out / "claim-map.csv"),
        ])
        run([
            "python3", "tools/scope_of_work/report_scope_of_work_parity.py",
            "--scope-of-work", str(evidence),
            "--production-scope-of-work", str(live),
            "--source-dir", str(source_dir),
            "--output-json", str(out / "parity.json"),
            "--output-md", str(out / "parity.md"),
            "--isolated-migration",
            "--migration-authority", "D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176",
        ])
        run([
            "python3", "tools/scope_of_work/derive_review_checklist.py", str(live),
            "--output", str(out / "checklist.json"),
        ])
        run([
            "python3", "tools/scope_of_work/finalize_scope_of_work.py",
            "--evidence-candidate", str(evidence),
            "--output", str(out / "finalized.md"),
            "--report", str(out / "finalization.json"),
        ])
        assert (out / "finalized.md").read_bytes() == production.read_bytes()
        assert (out / "finalization.json").read_bytes() == finalization.read_bytes()
        shutil.rmtree(source_dir)
        results.append({
            "deliverable_id": deliverable_id,
            "validation": "PASS",
            "mapping": "PASS",
            "parity": "PASS",
            "checklist": "PASS",
            "finalization": "PASS",
            "live_sha256": sha(live.read_bytes()),
        })

    report = {
        "schema": "chirality-change-member-checks/v1",
        "verdict": "PASS",
        "members": len(results),
        "results": results,
    }
    (CHANGE / "MEMBER_CHECKS.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({"verdict": "PASS", "members": len(results)}, sort_keys=True))


if __name__ == "__main__":
    main()
