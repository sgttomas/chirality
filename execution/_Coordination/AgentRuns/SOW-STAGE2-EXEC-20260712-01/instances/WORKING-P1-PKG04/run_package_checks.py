#!/usr/bin/env python3
"""Run the accepted read-only Piping package checks and retain outputs."""
import json, os, subprocess
from pathlib import Path

ROOT = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
OUT = ROOT / "execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P1-PKG04"
env = {**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}
self_check = subprocess.run(["python3", "tools/practitioner_harness/harness.py", "self-check"], cwd=ROOT, env=env, text=True, capture_output=True)
(OUT / "PRACTITIONER_SELF_CHECK.txt").write_text(self_check.stdout + self_check.stderr)
pytest = subprocess.run(["python3", "-m", "pytest", "-q", "-p", "no:cacheprovider", "--junitxml", str(OUT / "PRACTITIONER_HARNESS.junit.xml"), "tools/practitioner_harness"], cwd=ROOT, env=env, text=True, capture_output=True)
(OUT / "PRACTITIONER_HARNESS.txt").write_text(pytest.stdout + pytest.stderr)
result = {"self_check_exit": self_check.returncode, "pytest_exit": pytest.returncode,
          "pytest_summary": pytest.stdout.splitlines()[-1] if pytest.stdout.splitlines() else "",
          "status": "PASS" if self_check.returncode == pytest.returncode == 0 else "FAIL"}
(OUT / "PROJECT_CHECKS.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps(result, indent=2, sort_keys=True))
raise SystemExit(0 if result["status"] == "PASS" else 1)
