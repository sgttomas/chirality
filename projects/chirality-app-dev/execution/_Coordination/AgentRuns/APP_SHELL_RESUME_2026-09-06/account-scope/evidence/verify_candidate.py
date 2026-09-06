#!/usr/bin/env python3
"""Read-only exact candidate verifier; run from repository root."""
from pathlib import Path
import hashlib,json,subprocess
r=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
p=r/'projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_SHELL_RESUME_2026-09-06/account-scope'
sha=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
m=json.loads((p/'candidate-v1/CANDIDATE_IDENTITIES.json').read_text()); f=json.loads((p/'CANDIDATE_FREEZE_v1.json').read_text())
checks={x['path']:sha(p/x['path'])==x['sha256'] for x in f['files']}
checks['live_status_preimage']=sha(r/m['live_target'])==m['preimage_sha256']
old=(p/'candidate-v1/PREIMAGE__STATUS.md').read_text();new=(p/'candidate-v1/CANDIDATE__STATUS.md').read_text()
checks['prefix_unchanged']=old.split('- **DEL-02-05-V3-05**')[0]==new.split('- **DEL-02-05-V3-05**')[0]
checks['history_unchanged']=old.split('\n## History')[1]==new.split('\n## History')[1]
checks['exactly_three_changed_lines']=len([1 for a,b in zip(old.splitlines(),new.splitlines()) if a!=b])==3 and len(old.splitlines())==len(new.splitlines())
checks['candidate_hash']=sha(p/'candidate-v1/CANDIDATE__STATUS.md')==m['candidate_sha256']
checks['merged_work_ancestor']=subprocess.run(['git','merge-base','--is-ancestor','943dd268d69ae408c63228c4ba3fc35b113aeadc','HEAD']).returncode==0
print(json.dumps({'status':'PASS' if all(checks.values()) else 'FAIL','checks':checks},indent=2));raise SystemExit(0 if all(checks.values()) else 1)
