#!/usr/bin/env python3
"""Run and retain final closure checks against an exact detached-main tree."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path


def run(name: str, command: list[str], cwd: Path, out: Path, env: dict[str, str] | None = None) -> dict[str, object]:
    started = time.monotonic()
    proc = subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False, env=env)
    output = proc.stdout + proc.stderr
    (out / f"{name}.txt").write_text(output, encoding="utf-8")
    row = {
        "name": name, "command": command, "cwd": str(cwd),
        "exit_code": proc.returncode,
        "duration_seconds": round(time.monotonic() - started, 3),
        "output_sha256": hashlib.sha256(output.encode()).hexdigest(),
    }
    print(f"{'PASS' if proc.returncode == 0 else 'FAIL'} {name} exit={proc.returncode} seconds={row['duration_seconds']}", flush=True)
    return row


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--dependency-root", type=Path, required=True)
    args = parser.parse_args()
    root, out, dependency_root = args.root.resolve(), args.out.resolve(), args.dependency_root.resolve()
    out.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    results: list[dict[str, object]] = []
    root_commands = (
        ("scope_of_work_tests", [sys.executable, "-m", "pytest", "-q", "tools/scope_of_work/test_scope_of_work_tools.py"]),
        ("practitioner_tests", [sys.executable, "-m", "pytest", "-q", "tools/practitioner_harness"]),
        ("validate_agents", [sys.executable, "tools/validation/validate_agent_instructions.py"]),
        ("validate_entrypoints", [sys.executable, "tools/validation/validate_instruction_entrypoints.py"]),
        ("validate_paths", [sys.executable, "tools/validation/validate_path_anchors.py", "."]),
        ("validate_skills", [sys.executable, "tools/validation/validate_skill_metadata.py"]),
    )
    for name, command in root_commands:
        results.append(run(name, command, root, out, env))

    with tempfile.TemporaryDirectory(prefix="evaluation-closure-final-") as raw:
        tmp = Path(raw)
        app = tmp / "app"
        subprocess.run(["rsync", "-a", "--exclude", "node_modules", "--exclude", ".next", f"{root / 'projects/chirality-app-dev/frontend'}/", f"{app}/"], check=True)
        os.symlink(dependency_root / "projects/chirality-app-dev/frontend/node_modules", app / "node_modules")
        results.append(run("app_typecheck", ["npm", "run", "typecheck"], app, out))
        results.append(run("app_tests", ["npm", "test", "--", "--run"], app, out))
        results.append(run("app_build", ["npm", "run", "build"], app, out))

        piping = tmp / "piping"
        subprocess.run(["rsync", "-a", "--exclude", "node_modules", "--exclude", "target", "--exclude", "dist", f"{root / 'projects/chirality-piping'}/", f"{piping}/"], check=True)
        os.symlink(dependency_root / "projects/chirality-piping/node_modules", piping / "node_modules")
        desktop_modules = piping / "apps/desktop/node_modules"
        if desktop_modules.exists() or desktop_modules.is_symlink():
            if desktop_modules.is_dir() and not desktop_modules.is_symlink():
                shutil.rmtree(desktop_modules)
            else:
                desktop_modules.unlink()
        os.symlink(dependency_root / "projects/chirality-piping/apps/desktop/node_modules", desktop_modules)
        results.append(run("piping_wasm", ["npm", "run", "build:wasm", "--workspace", "apps/desktop"], piping, out))
        results.append(run("piping_tests", ["npm", "run", "test:desktop"], piping, out))
        results.append(run("piping_build", ["npm", "run", "build:desktop"], piping, out))

    result = {
        "schema": "chirality-sow-final-closure-checks/v1",
        "basis": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip(),
        "verdict": "PASS" if all(row["exit_code"] == 0 for row in results) else "BLOCKED",
        "results": results,
    }
    (out.parent / "CHECK_SUITE.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
