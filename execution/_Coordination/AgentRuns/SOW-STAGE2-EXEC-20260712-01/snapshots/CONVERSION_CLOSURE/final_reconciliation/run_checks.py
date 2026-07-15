#!/usr/bin/env python3
"""Run closure checks on the detached exact-main worktree and retain evidence."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

OUT = Path(__file__).resolve().parent / "checks"
BASIS = "79de30d83b91a2ab468a3f17536a5233c2f85fe7"


def worktrees() -> list[tuple[Path, str]]:
    control = OUT.parents[7]
    records = subprocess.check_output(["git", "worktree", "list", "--porcelain"], cwd=control, text=True).strip().split("\n\n")
    result = []
    for record in records:
        fields = dict(line.split(" ", 1) for line in record.splitlines() if " " in line)
        result.append((Path(fields["worktree"]), fields.get("HEAD", "")))
    return result


TREES = worktrees()
ROOT = next(path for path, head in TREES if head == BASIS)
PRIMARY = next(path for path, _ in TREES if (path / "projects/chirality-app-dev/frontend/node_modules").exists())


def run(name: str, command: list[str], cwd: Path, env: dict[str, str] | None = None) -> dict[str, object]:
    started = time.monotonic()
    proc = subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False, env=env)
    output = proc.stdout + proc.stderr
    (OUT / f"{name}.txt").write_text(output, encoding="utf-8")
    row = {"name": name, "command": command, "exit_code": proc.returncode,
           "duration_seconds": round(time.monotonic() - started, 3),
           "output_sha256": hashlib.sha256(output.encode()).hexdigest()}
    print(f"{'PASS' if proc.returncode == 0 else 'FAIL'} {name} exit={proc.returncode} seconds={row['duration_seconds']}", flush=True)
    return row


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ); env["PYTHONDONTWRITEBYTECODE"] = "1"
    results: list[dict[str, object]] = []
    for name, command in (
        ("scope_of_work_tests", [sys.executable, "-m", "pytest", "-q", "tools/scope_of_work/test_scope_of_work_tools.py"]),
        ("practitioner_tests", [sys.executable, "-m", "pytest", "-q", "tools/practitioner_harness"]),
        ("validate_agents", [sys.executable, "tools/validation/validate_agent_instructions.py"]),
        ("validate_entrypoints", [sys.executable, "tools/validation/validate_instruction_entrypoints.py"]),
        ("validate_paths", [sys.executable, "tools/validation/validate_path_anchors.py", "."]),
        ("validate_skills", [sys.executable, "tools/validation/validate_skill_metadata.py"]),
    ):
        results.append(run(name, command, ROOT, env))
    with tempfile.TemporaryDirectory(prefix="recon-final-checks-") as raw:
        tmp = Path(raw)
        app = tmp / "app"
        subprocess.run(["rsync", "-a", "--exclude", "node_modules", "--exclude", ".next",
                        f"{ROOT / 'projects/chirality-app-dev/frontend'}/", f"{app}/"], check=True)
        os.symlink(PRIMARY / "projects/chirality-app-dev/frontend/node_modules", app / "node_modules")
        results.append(run("app_typecheck", ["npm", "run", "typecheck"], app))
        results.append(run("app_tests", ["npm", "test", "--", "--run"], app))
        results.append(run("app_build", ["npm", "run", "build"], app))
        piping = tmp / "piping"
        subprocess.run(["rsync", "-a", "--exclude", "node_modules", "--exclude", "target", "--exclude", "dist",
                        f"{ROOT / 'projects/chirality-piping'}/", f"{piping}/"], check=True)
        os.symlink(PRIMARY / "projects/chirality-piping/node_modules", piping / "node_modules")
        desktop_modules = piping / "apps/desktop/node_modules"
        if desktop_modules.exists() or desktop_modules.is_symlink():
            if desktop_modules.is_dir() and not desktop_modules.is_symlink(): shutil.rmtree(desktop_modules)
            else: desktop_modules.unlink()
        os.symlink(PRIMARY / "projects/chirality-piping/apps/desktop/node_modules", desktop_modules)
        results.append(run("piping_wasm", ["npm", "run", "build:wasm", "--workspace", "apps/desktop"], piping))
        results.append(run("piping_tests", ["npm", "run", "test:desktop"], piping))
        results.append(run("piping_build", ["npm", "run", "build:desktop"], piping))
    result = {"schema": "chirality-conversion-closure-final-checks/v1",
              "basis": "79de30d83b91a2ab468a3f17536a5233c2f85fe7",
              "verdict": "PASS" if all(r["exit_code"] == 0 for r in results) else "BLOCKED", "results": results}
    (OUT.parent / "CHECK_RESULTS.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__": raise SystemExit(main())
