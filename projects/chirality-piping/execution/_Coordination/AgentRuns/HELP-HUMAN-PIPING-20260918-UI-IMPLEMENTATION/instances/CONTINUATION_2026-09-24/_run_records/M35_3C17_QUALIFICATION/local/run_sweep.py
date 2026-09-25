from pathlib import Path
import os, subprocess, json, datetime, hashlib
root=Path('/private/tmp/piping-generated-loads-20260924')
project=root/'projects/chirality-piping'
out=Path('/private/tmp/piping-m35-validation-3c17-20260925')
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()
status=subprocess.check_output(['git','status','--porcelain'],cwd=root,text=True)
assert head=='3c17e267dd06ee561e8dc9984f6623126095eec1',head
assert not status,status
binding=Path('/private/tmp/piping-m35-ci-3c17-20260925/surface4-ci-binding.json')
assert json.loads(binding.read_text())['head_sha']==head
run_env=os.environ.copy()
run_env.update(CARGO_BUILD_JOBS='2',CARGO_NET_OFFLINE='true',VITEST_MAX_WORKERS='2')
run_env.pop('CARGO_TARGET_DIR',None)
run_env['PATH']='/private/tmp/chirality-piping-dec025-venv/bin:'+run_env['PATH']
run_env.pop('SWBPIPE_LIVE_CONTROL',None)
cmd=['/private/tmp/chirality-piping-dec025-venv/bin/python','tools/release/run_evidence_sweep.py','--execute','--require-capability','host','--surface4-ci-binding',str(binding)]
record={'candidate':head,'initial_status':status,'cwd':str(project),'command':cmd,'environment':{k:run_env.get(k) for k in ['PATH','CARGO_BUILD_JOBS','CARGO_NET_OFFLINE','CARGO_TARGET_DIR','VITEST_MAX_WORKERS']},'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'binding_sha256':hashlib.sha256(binding.read_bytes()).hexdigest()}
(out/'sweep-invocation.json').write_text(json.dumps(record,indent=2)+'\n')
with (out/'sweep.log').open('w') as log:
    result=subprocess.run(cmd,cwd=project,env=run_env,stdout=log,stderr=subprocess.STDOUT)
record.update(exit_code=result.returncode,finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),final_status=subprocess.check_output(['git','status','--porcelain'],cwd=root,text=True))
(out/'sweep-result.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:record[k] for k in ['candidate','exit_code','finished_at','final_status']},indent=2))
raise SystemExit(result.returncode)
