#!/usr/bin/env python3
"""Rerun App tests with the complete disposable repository layout."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import tempfile
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
INSTANCE = Path(__file__).resolve().parent
OUT = INSTANCE / "checks/app_tests_r1.txt"
PRIMARY = Path("/Users/ryan/ai-env/projects/chirality")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="recon-clean-repair-app-r1-") as raw_tmp:
        app_root = Path(raw_tmp) / "repo"
        (app_root / "projects/chirality-app-dev").mkdir(parents=True)
        for item in ROOT.iterdir():
            if item.name not in {".git", "projects"}:
                os.symlink(item, app_root / item.name)
        for item in (ROOT / "projects").iterdir():
            if item.name != "chirality-app-dev":
                os.symlink(item, app_root / "projects" / item.name)
        for item in (ROOT / "projects/chirality-app-dev").iterdir():
            if item.name != "frontend":
                os.symlink(item, app_root / "projects/chirality-app-dev" / item.name)
        frontend = app_root / "projects/chirality-app-dev/frontend"
        subprocess.run(
            ["rsync", "-a", "--exclude", "node_modules", "--exclude", ".next", f"{ROOT / 'projects/chirality-app-dev/frontend'}/", f"{frontend}/"],
            check=True,
        )
        os.symlink(PRIMARY / "projects/chirality-app-dev/frontend/node_modules", frontend / "node_modules")
        started = time.monotonic()
        proc = subprocess.run(["npm", "test", "--", "--run"], cwd=frontend, text=True, capture_output=True, check=False)
        output = proc.stdout + proc.stderr
        OUT.write_text(output, encoding="utf-8")
        result = {
            "schema": "chirality-sow-clean-repair-app-test-rerun/v1",
            "reason": "attempt 1 disposable copy omitted repository-level test fixtures",
            "exit_code": proc.returncode,
            "duration_seconds": round(time.monotonic() - started, 3),
            "output_sha256": hashlib.sha256(output.encode("utf-8")).hexdigest(),
            "verdict": "PASS" if proc.returncode == 0 else "BLOCKED",
        }
        (INSTANCE / "APP_TEST_RERUN.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(result, indent=2))
        return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
