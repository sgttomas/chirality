#!/usr/bin/env python3
"""Close the retained frontend-only fixture-layout failure with exact-main fixtures."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import tempfile
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
PRIMARY = next(path for path, _ in TREES if (path / "projects/chirality-app-dev/frontend/node_modules").exists())

with tempfile.TemporaryDirectory(prefix="recon-final-app-r1-") as raw:
    tmp = Path(raw)
    app = tmp / "frontend"
    subprocess.run(["rsync", "-a", "--exclude", "node_modules", "--exclude", ".next",
                    f"{ROOT / 'projects/chirality-app-dev/frontend'}/", f"{app}/"], check=True)
    os.symlink(PRIMARY / "projects/chirality-app-dev/frontend/node_modules", app / "node_modules")
    for name in ("agents", "docs", ".github", "_DomainEngines"):
        source = ROOT / name
        if source.exists(): os.symlink(source, tmp / name)
    started = time.monotonic()
    proc = subprocess.run(["npm", "test", "--", "--run"], cwd=app, text=True, capture_output=True)
    output = proc.stdout + proc.stderr
    (OUT / "checks/app_tests_r1.txt").write_text(output, encoding="utf-8")
    row = {"name": "app_tests_r1", "command": ["npm", "test", "--", "--run"],
           "exit_code": proc.returncode, "duration_seconds": round(time.monotonic() - started, 3),
           "output_sha256": hashlib.sha256(output.encode()).hexdigest(),
           "closes": "app_tests frontend-only disposable fixture layout failure"}

result_path = OUT / "CHECK_RESULTS.json"
result = json.loads(result_path.read_text())
for prior in result["results"]:
    if prior["name"] == "app_tests":
        prior["disposition"] = "RETAINED_FIXTURE_LAYOUT_FAILURE_CLOSED_BY_APP_TESTS_R1"
result["results"].append(row)
result["verdict"] = "PASS" if proc.returncode == 0 and all(
    r["exit_code"] == 0 or r.get("disposition") == "RETAINED_FIXTURE_LAYOUT_FAILURE_CLOSED_BY_APP_TESTS_R1"
    for r in result["results"]
) else "BLOCKED"
result_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(row, indent=2))
raise SystemExit(0 if result["verdict"] == "PASS" else 1)
