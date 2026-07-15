#!/usr/bin/env python3
"""Rerun App tests with the repository-level fixtures the first substrate omitted."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import tempfile
import time
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--dependency-root", type=Path, required=True)
    args = parser.parse_args()
    root, out, dependency_root = args.root.resolve(), args.out.resolve(), args.dependency_root.resolve()
    out.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="evaluation-closure-app-r1-") as raw:
        repo = Path(raw) / "repo"
        (repo / "projects/chirality-app-dev").mkdir(parents=True)
        for item in root.iterdir():
            if item.name not in {".git", "projects"}:
                os.symlink(item, repo / item.name)
        for item in (root / "projects").iterdir():
            if item.name != "chirality-app-dev":
                os.symlink(item, repo / "projects" / item.name)
        for item in (root / "projects/chirality-app-dev").iterdir():
            if item.name != "frontend":
                os.symlink(item, repo / "projects/chirality-app-dev" / item.name)
        frontend = repo / "projects/chirality-app-dev/frontend"
        subprocess.run(["rsync", "-a", "--exclude", "node_modules", "--exclude", ".next", f"{root / 'projects/chirality-app-dev/frontend'}/", f"{frontend}/"], check=True)
        os.symlink(dependency_root / "projects/chirality-app-dev/frontend/node_modules", frontend / "node_modules")
        started = time.monotonic()
        proc = subprocess.run(["npm", "test", "--", "--run"], cwd=frontend, text=True, capture_output=True, check=False)
        output = proc.stdout + proc.stderr
        (out / "app_tests_r1.txt").write_text(output, encoding="utf-8")
        result = {
            "schema": "chirality-sow-final-closure-app-test-rerun/v1",
            "basis": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip(),
            "reason": "attempt 1 disposable frontend copy omitted repository-level fixtures",
            "exit_code": proc.returncode,
            "duration_seconds": round(time.monotonic() - started, 3),
            "output_sha256": hashlib.sha256(output.encode()).hexdigest(),
            "verdict": "PASS" if proc.returncode == 0 else "BLOCKED",
        }
        (out.parent / "APP_TEST_RERUN.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(result, indent=2))
        return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
