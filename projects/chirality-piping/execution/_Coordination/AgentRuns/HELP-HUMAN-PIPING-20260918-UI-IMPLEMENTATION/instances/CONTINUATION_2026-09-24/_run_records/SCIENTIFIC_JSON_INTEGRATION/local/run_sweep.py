from pathlib import Path
import subprocess,os,json,datetime,hashlib,time
repo=Path('/private/tmp/piping-scientific-json-integration-20260925');p=repo/'projects/chirality-piping';out=Path('/private/tmp/piping-scientific-json-integration-checks-20260925');out.mkdir(exist_ok=True)
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip();status=subprocess.check_output(['git','status','--porcelain'],cwd=repo,text=True);assert head=='98b423d93e41338551bf744def1e2c5a303aeaab' and not status,status
binding=Path('/private/tmp/piping-scientific-json-ci-98/surface4-ci-binding.json');b=json.loads(binding.read_text());assert b['head_sha']==head and b['conclusion']=='success'
env=os.environ.copy();env['PATH']='/private/tmp/chirality-piping-dec025-venv/bin:/Users/ryan/.local/share/mise/installs/node/24/bin:'+env['PATH'];env['CARGO_BUILD_JOBS']='2';env['CARGO_NET_OFFLINE']='true';env['VITEST_MAX_WORKERS']='2';env.pop('CARGO_TARGET_DIR',None)
for name in ['OPENPIPESTRESS_CHECKED_JSON_BIN','OPENPIPESTRESS_BINARY64_JSON_BIN']:env.pop(name,None)
cmd=['/private/tmp/chirality-piping-dec025-venv/bin/python','tools/release/run_evidence_sweep.py','--execute','--require-capability','host','--surface4-ci-binding',str(binding),'--output-dir',str(out/'sweep')]
record={'candidate':head,'initial_status':status,'cwd':str(p),'command':cmd,'environment':{k:env.get(k) for k in ['PATH','CARGO_BUILD_JOBS','CARGO_NET_OFFLINE','CARGO_TARGET_DIR','VITEST_MAX_WORKERS']},'binding_sha256':hashlib.sha256(binding.read_bytes()).hexdigest(),'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat()};(out/'sweep-invocation.json').write_text(json.dumps(record,indent=2)+'\n')
started=time.monotonic()
with (out/'sweep.log').open('wb') as log:r=subprocess.run(cmd,cwd=p,env=env,stdout=log,stderr=subprocess.STDOUT)
record.update(exit_code=r.returncode,elapsed_seconds=time.monotonic()-started,finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat());(out/'sweep-result.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps({'candidate':head,'exit_code':r.returncode,'elapsed_seconds':record['elapsed_seconds'],'log':str(out/'sweep.log')}),flush=True)
raise SystemExit(r.returncode)
