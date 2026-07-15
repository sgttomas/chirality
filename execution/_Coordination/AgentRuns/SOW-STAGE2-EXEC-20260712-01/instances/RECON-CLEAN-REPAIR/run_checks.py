#!/usr/bin/env python3
"""Run the independent clean-repair check suite with retained output."""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
INSTANCE = Path(__file__).resolve().parent
OUT = INSTANCE / "checks"
PRIMARY = Path("/Users/ryan/ai-env/projects/chirality")


def run(name: str, command: list[str], cwd: Path, env: dict[str, str] | None = None) -> dict[str, object]:
    started = time.monotonic()
    proc = subprocess.run(command, cwd=cwd, text=True, capture_output=True, check=False, env=env)
    output = proc.stdout + proc.stderr
    (OUT / f"{name}.txt").write_text(output, encoding="utf-8")
    row = {
        "name": name,
        "command": command,
        "cwd": str(cwd),
        "exit_code": proc.returncode,
        "duration_seconds": round(time.monotonic() - started, 3),
        "output_sha256": __import__("hashlib").sha256(output.encode("utf-8")).hexdigest(),
    }
    print(f"{'PASS' if proc.returncode == 0 else 'FAIL'} {name} exit={proc.returncode} seconds={row['duration_seconds']}", flush=True)
    return row


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    rows: list[dict[str, object]] = []
    root_commands = (
        ("scope_of_work_tests", [sys.executable, "-m", "pytest", "-q", "tools/scope_of_work/test_scope_of_work_tools.py"]),
        ("practitioner_tests", [sys.executable, "-m", "pytest", "-q", "tools/practitioner_harness"]),
        ("validate_agents", [sys.executable, "tools/validation/validate_agent_instructions.py"]),
        ("validate_entrypoints", [sys.executable, "tools/validation/validate_instruction_entrypoints.py"]),
        ("validate_paths", [sys.executable, "tools/validation/validate_path_anchors.py", "."]),
        ("validate_skills", [sys.executable, "tools/validation/validate_skill_metadata.py"]),
    )
    for name, command in root_commands:
        rows.append(run(name, command, ROOT, env))

    with tempfile.TemporaryDirectory(prefix="recon-clean-repair-checks-") as raw_tmp:
        tmp = Path(raw_tmp)
        app = tmp / "app"
        subprocess.run(
            ["rsync", "-a", "--exclude", "node_modules", "--exclude", ".next", f"{ROOT / 'projects/chirality-app-dev/frontend'}/", f"{app}/"],
            check=True,
        )
        os.symlink(PRIMARY / "projects/chirality-app-dev/frontend/node_modules", app / "node_modules")
        rows.append(run("app_typecheck", ["npm", "run", "typecheck"], app))
        rows.append(run("app_tests", ["npm", "test", "--", "--run"], app))
        rows.append(run("app_build", ["npm", "run", "build"], app))

        piping = tmp / "piping"
        subprocess.run(
            ["rsync", "-a", "--exclude", "node_modules", "--exclude", "target", "--exclude", "dist", f"{ROOT / 'projects/chirality-piping'}/", f"{piping}/"],
            check=True,
        )
        os.symlink(PRIMARY / "projects/chirality-piping/node_modules", piping / "node_modules")
        desktop_modules = piping / "apps/desktop/node_modules"
        if desktop_modules.exists() or desktop_modules.is_symlink():
            if desktop_modules.is_dir() and not desktop_modules.is_symlink():
                shutil.rmtree(desktop_modules)
            else:
                desktop_modules.unlink()
        os.symlink(PRIMARY / "projects/chirality-piping/apps/desktop/node_modules", desktop_modules)
        rows.append(run("piping_wasm", ["npm", "run", "build:wasm", "--workspace", "apps/desktop"], piping))
        rows.append(run("piping_tests", ["npm", "run", "test:desktop"], piping))
        rows.append(run("piping_build", ["npm", "run", "build:desktop"], piping))

    result = {
        "schema": "chirality-sow-clean-repair-reconciliation-checks/v1",
        "verdict": "PASS" if all(row["exit_code"] == 0 for row in rows) else "BLOCKED",
        "results": rows,
    }
    (INSTANCE / "CHECK_RESULTS.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
