#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import time
from pathlib import Path

from common import load_profile


def as_text(value: str | bytes | None) -> str:
    if value is None:
        return ""
    return value.decode("utf-8", errors="replace") if isinstance(value, bytes) else value


def main() -> int:
    parser = argparse.ArgumentParser(description="Run allowlisted software checks without a shell.")
    parser.add_argument("profile")
    parser.add_argument("--check", action="append", default=[])
    parser.add_argument("--output", required=True)
    parser.add_argument("--timeout-seconds", type=float, default=600.0)
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
        timeout_seconds = spec.get("timeout_seconds", args.timeout_seconds)
        if not isinstance(timeout_seconds, (int, float)) or timeout_seconds <= 0:
            raise ValueError(f"check {check_id} timeout_seconds must be positive")
        try:
            completed = subprocess.run(
                command,
                cwd=cwd,
                text=True,
                capture_output=True,
                shell=False,
                timeout=float(timeout_seconds),
            )
            exit_code = completed.returncode
            stdout = completed.stdout
            stderr = completed.stderr
        except subprocess.TimeoutExpired as error:
            exit_code = 124
            stdout = as_text(error.stdout)
            stderr = as_text(error.stderr) + f"\ncheck timed out after {timeout_seconds} seconds"
        results.append({
            "id": check_id,
            "command": command,
            "cwd": cwd.relative_to(workspace_root).as_posix() or ".",
            "exit_code": exit_code,
            "timeout_seconds": timeout_seconds,
            "duration_seconds": round(time.monotonic() - started, 3),
            "stdout": stdout,
            "stderr": stderr,
            "status": "PASS" if exit_code == 0 else "FAIL",
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
    if not output.is_absolute():
        output = (workspace_root / output).resolve()
    else:
        output = output.resolve()
    output.relative_to(workspace_root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "output": str(output), "checks": selected}))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
