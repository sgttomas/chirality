#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import time
from pathlib import Path

from common import load_profile


def main() -> int:
    parser = argparse.ArgumentParser(description="Run allowlisted software checks without a shell.")
    parser.add_argument("profile")
    parser.add_argument("--check", action="append", default=[])
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    profile_path = Path(args.profile).resolve()
    project_root, profile = load_profile(profile_path)
    workspace_root = (profile_path.parent / profile.get("workspace_root", profile.get("project_root", "."))).resolve()
    project_root.relative_to(workspace_root)
    checks = profile.get("checks", {})
    selected = args.check or list(checks)
    unknown = sorted(set(selected) - set(checks))
    if unknown:
        parser.error(f"unknown check(s): {', '.join(unknown)}")
    results = []
    for check_id in selected:
        spec = checks[check_id]
        command = spec.get("command")
        if not isinstance(command, list) or not command or not all(isinstance(v, str) for v in command):
            raise ValueError(f"check {check_id} command must be a non-empty string array")
        cwd = (project_root / spec.get("cwd", ".")).resolve()
        cwd.relative_to(workspace_root)
        if not cwd.is_dir():
            raise ValueError(f"check {check_id} cwd does not exist: {cwd}")
        started = time.monotonic()
        completed = subprocess.run(command, cwd=cwd, text=True, capture_output=True, shell=False)
        results.append({
            "id": check_id,
            "command": command,
            "cwd": cwd.relative_to(workspace_root).as_posix() or ".",
            "exit_code": completed.returncode,
            "duration_seconds": round(time.monotonic() - started, 3),
            "stdout": completed.stdout,
            "stderr": completed.stderr,
            "status": "PASS" if completed.returncode == 0 else "FAIL",
        })
    report = {
        "schema": "chirality-software-check-evidence/v1",
        "profile": str(Path(args.profile).resolve()),
        "project_root": str(project_root),
        "workspace_root": str(workspace_root),
        "status": "PASS" if all(item["exit_code"] == 0 for item in results) else "FAIL",
        "results": results,
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "output": str(output), "checks": selected}))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
