#!/usr/bin/env python3
"""Run and retain the sealed root/focused validation suite."""

from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent / "checks"

COMMANDS = (
    ("scope_of_work_tests", [sys.executable, "-m", "pytest", "-q", "tools/scope_of_work/test_scope_of_work_tools.py"]),
    ("practitioner_tests", [sys.executable, "-m", "pytest", "-q", "tools/practitioner_harness"]),
    ("validate_agents", [sys.executable, "tools/validation/validate_agent_instructions.py"]),
    ("validate_entrypoints", [sys.executable, "tools/validation/validate_instruction_entrypoints.py"]),
    ("validate_paths", [sys.executable, "tools/validation/validate_path_anchors.py", "."]),
    ("validate_skills", [sys.executable, "tools/validation/validate_skill_metadata.py"]),
)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    results = []
    for name, command in COMMANDS:
        started = time.monotonic()
        proc = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
        duration = round(time.monotonic() - started, 3)
        (OUT / f"{name}.txt").write_text(proc.stdout + proc.stderr, encoding="utf-8")
        results.append({
            "name": name,
            "command": command,
            "exit_code": proc.returncode,
            "duration_seconds": duration,
            "output": f"checks/{name}.txt",
        })
        print(f"{'PASS' if proc.returncode == 0 else 'FAIL'} {name} exit={proc.returncode} seconds={duration}")
    report = {
        "schema": "chirality-sow-clean-repair-checks/v1",
        "verdict": "PASS" if all(row["exit_code"] == 0 for row in results) else "BLOCKED",
        "results": results,
    }
    (OUT / "RESULTS.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
