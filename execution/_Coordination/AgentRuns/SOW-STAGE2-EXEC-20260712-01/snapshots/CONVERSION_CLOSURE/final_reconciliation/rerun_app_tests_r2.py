#!/usr/bin/env python3
"""Run App tests in the exact repository layout; retain both prior fixture failures."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import time
from pathlib import Path

OUT = Path(__file__).resolve().parent
BASIS = "79de30d83b91a2ab468a3f17536a5233c2f85fe7"


def worktrees() -> list[tuple[Path, str]]:
    control = OUT.parents[6]
    records = subprocess.check_output(["git", "worktree", "list", "--porcelain"], cwd=control, text=True).strip().split("\n\n")
    result = []
    for record in records:
        fields = dict(line.split(" ", 1) for line in record.splitlines() if " " in line)
        result.append((Path(fields["worktree"]), fields.get("HEAD", "")))
    return result


TREES = worktrees()
ROOT = next(path for path, head in TREES if head == BASIS)
APP = ROOT / "projects/chirality-app-dev/frontend"
MODULES = APP / "node_modules"
SOURCE_MODULES = next(path / "projects/chirality-app-dev/frontend/node_modules" for path, _ in TREES if (path / "projects/chirality-app-dev/frontend/node_modules").exists())

created = False
if not MODULES.exists():
    os.symlink(SOURCE_MODULES, MODULES); created = True
started = time.monotonic()
try:
    proc = subprocess.run(["npm", "test", "--", "--run"], cwd=APP, text=True, capture_output=True)
finally:
    if created: MODULES.unlink()
output = proc.stdout + proc.stderr
(OUT / "checks/app_tests_r2.txt").write_text(output, encoding="utf-8")
row = {"name": "app_tests_r2", "command": ["npm", "test", "--", "--run"],
       "exit_code": proc.returncode, "duration_seconds": round(time.monotonic() - started, 3),
       "output_sha256": hashlib.sha256(output.encode()).hexdigest(),
       "closes": "app_tests and app_tests_r1 disposable fixture path-depth failures"}
result_path = OUT / "CHECK_RESULTS.json"
result = json.loads(result_path.read_text())
for prior in result["results"]:
    if prior["name"] in {"app_tests", "app_tests_r1"}:
        prior["disposition"] = "RETAINED_FIXTURE_PATH_DEPTH_FAILURE_CLOSED_BY_APP_TESTS_R2"
result["results"].append(row)
result["verdict"] = "PASS" if proc.returncode == 0 and all(
    r["exit_code"] == 0 or r.get("disposition") == "RETAINED_FIXTURE_PATH_DEPTH_FAILURE_CLOSED_BY_APP_TESTS_R2"
    for r in result["results"]
) else "BLOCKED"
result_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(row, indent=2))
raise SystemExit(0 if result["verdict"] == "PASS" else 1)
