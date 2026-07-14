#!/usr/bin/env python3
"""Run read-only package-wide checks and persist their exact outputs."""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
SNAP = ROOT / "execution/_Coordination/AgentRuns/SOW-PKG02-BATCH-EXPERIMENT-20260714-01/snapshots/package"


def main() -> None:
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    self_check = subprocess.run(
        ["python3", "tools/practitioner_harness/harness.py", "self-check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        env=env,
    )
    (SNAP / "PRACTITIONER_SELF_CHECK.md").write_text(
        self_check.stdout + self_check.stderr, encoding="utf-8"
    )
    harness = subprocess.run(
        [
            "python3",
            "-m",
            "pytest",
            "-q",
            "-p",
            "no:cacheprovider",
            "--junitxml",
            str(SNAP / "PRACTITIONER_HARNESS.junit.xml"),
            "tools/practitioner_harness",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        env=env,
    )
    (SNAP / "PRACTITIONER_HARNESS.txt").write_text(
        harness.stdout + harness.stderr, encoding="utf-8"
    )
    report = {
        "self_check_exit": self_check.returncode,
        "self_check_block_count": self_check.stdout.count("BLOCK"),
        "pytest_exit": harness.returncode,
        "pytest_summary": harness.stdout.splitlines()[-1] if harness.stdout.splitlines() else "",
    }
    (SNAP / "PACKAGE_CHECK_RESULTS.json").write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    if self_check.returncode != 0 or harness.returncode != 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
