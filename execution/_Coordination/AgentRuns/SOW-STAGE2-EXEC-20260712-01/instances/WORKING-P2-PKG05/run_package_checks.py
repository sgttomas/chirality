#!/usr/bin/env python3
import json, os, subprocess
from pathlib import Path
ROOT=Path(subprocess.check_output(["git","rev-parse","--show-toplevel"],text=True).strip())
OUT=ROOT/"execution/_Coordination/AgentRuns/SOW-STAGE2-EXEC-20260712-01/instances/WORKING-P2-PKG05"
env={**os.environ,"PYTHONDONTWRITEBYTECODE":"1"}
s=subprocess.run(["python3","tools/practitioner_harness/harness.py","self-check"],cwd=ROOT,env=env,text=True,capture_output=True)
(OUT/"PRACTITIONER_SELF_CHECK.txt").write_text(s.stdout+s.stderr)
p=subprocess.run(["python3","-m","pytest","-q","-p","no:cacheprovider","--junitxml",str(OUT/"PRACTITIONER_HARNESS.junit.xml"),"tools/practitioner_harness"],cwd=ROOT,env=env,text=True,capture_output=True)
(OUT/"PRACTITIONER_HARNESS.txt").write_text(p.stdout+p.stderr)
r={"self_check_exit":s.returncode,"pytest_exit":p.returncode,"pytest_summary":p.stdout.splitlines()[-1] if p.stdout.splitlines() else "","status":"PASS" if s.returncode==p.returncode==0 else "FAIL"}
(OUT/"PROJECT_CHECKS.json").write_text(json.dumps(r,indent=2,sort_keys=True)+"\n"); print(json.dumps(r,indent=2)); raise SystemExit(0 if r["status"]=="PASS" else 1)
