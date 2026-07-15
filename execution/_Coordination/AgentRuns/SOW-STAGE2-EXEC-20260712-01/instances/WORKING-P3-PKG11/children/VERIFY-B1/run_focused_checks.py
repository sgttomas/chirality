#!/usr/bin/env python3
"""Run frozen W-P3 focused checks and retain verifier-local command evidence."""
from __future__ import annotations

import csv
import json
import os
import subprocess
import time
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
HERE = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P3-PKG11/children/VERIFY-B1"
MANIFEST = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/snapshots/W_P3/preflight/P3_MANIFEST.tsv"
MEMBERS = ["DEL-11-01", "DEL-11-02", "DEL-11-03", "DEL-11-04", "DEL-11-05"]
OUT = HERE / "focused_commands"
OUT.mkdir(exist_ok=True)


def run(label: str, cmd: list[str]) -> dict[str, object]:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    env["PYTEST_ADDOPTS"] = "-p no:cacheprovider"
    started = time.monotonic()
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True, env=env)
    record = {
        "label": label,
        "argv": cmd,
        "exit_code": result.returncode,
        "duration_seconds": round(time.monotonic() - started, 6),
        "stdout": result.stdout,
        "stderr": result.stderr,
    }
    (OUT / f"{label}.json").write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    if result.returncode != 0:
        raise RuntimeError(f"{label} failed: {result.returncode}: {result.stderr}")
    return record


def main() -> None:
    rows = [r for r in csv.DictReader(MANIFEST.open(encoding="utf-8"), delimiter="\t") if r["deliverable_id"] in MEMBERS]
    assert [r["deliverable_id"] for r in rows] == MEMBERS
    sow = run("scope_of_work_tests", ["python3", "-m", "pytest", "-q", "tools/scope_of_work/test_scope_of_work_tools.py"])
    dep_results = []
    for row in rows:
        did = row["deliverable_id"]
        path = ROOT / row["live_path"] / "Dependencies.csv"
        rec = run(f"dependency_schema_{did}", ["python3", "tools/validation/validate_dependencies_schema.py", str(path)])
        with path.open(newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader)
            data_rows = sum(1 for _ in reader)
        assert len(header) == 29 and data_rows == int(row["dependency_rows"])
        dep_results.append({"deliverable_id": did, "columns": len(header), "data_rows": data_rows, "exit_code": rec["exit_code"]})
    self_check = run("practitioner_self_check", ["python3", "tools/practitioner_harness/harness.py", "self-check"])
    practitioner = run("practitioner_harness_tests", ["python3", "-m", "pytest", "-q", "tools/practitioner_harness"])
    result = {
        "scope_of_work_tests": sow,
        "dependency_schemas": dep_results,
        "practitioner_self_check": self_check,
        "practitioner_harness_tests": practitioner,
    }
    (HERE / "FOCUSED_RESULTS.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
