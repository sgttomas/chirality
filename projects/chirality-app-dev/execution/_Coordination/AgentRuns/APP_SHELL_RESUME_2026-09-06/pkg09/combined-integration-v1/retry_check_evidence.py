from pathlib import Path
import subprocess,os,json,hashlib,datetime
repo=Path('/private/tmp/chirality-app-runtime-integration-20260906-738-49951af');out=Path(__file__).resolve().parent;app=repo/'projects/chirality-app-dev';front=app/'frontend';runtime=repo/'projects/chirality-runtime'
env=os.environ.copy();env['CHIRALITY_INSTRUCTION_ROOT']=str(repo);env['NEXT_TELEMETRY_DISABLED']='1';env['CHIRALITY_HARNESS_PROVIDER']='stub';env['CHIRALITY_RUNTIME_USER_DATA']='/private/tmp/ch-ci-22a65b6-20260906';env['CHIRALITY_RUNTIME_SOCKET_PATH']='/private/tmp/ch-ci-22a65b6-20260906/runtime/control.sock'
def run(name,args,cwd,stop=True):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat()
 with (out/(name+'.stdout')).open('w') as so,(out/(name+'.stderr')).open('w') as se:p=subprocess.run(args,cwd=cwd,env=env,stdout=so,stderr=se)
 (out/(name+'.json')).write_text(json.dumps({'command':args,'cwd':str(cwd),'environment_overrides':{k:env[k] for k in ['CHIRALITY_INSTRUCTION_ROOT','NEXT_TELEMETRY_DISABLED','CHIRALITY_HARNESS_PROVIDER','CHIRALITY_RUNTIME_USER_DATA','CHIRALITY_RUNTIME_SOCKET_PATH']},'start':start,'end':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':p.returncode},indent=2)+'\n');print(name,p.returncode,flush=True)
 if stop:assert p.returncode==0,name
 return p.returncode
run('checks-freshness',['git','fetch','origin','main'],repo);run('checks-ancestor',['git','merge-base','--is-ancestor','origin/main','HEAD'],repo)
target=front/'artifacts/combined-integration-v1/REGISTERED_CHECKS.json';target.parent.mkdir(parents=True,exist_ok=True)
checks=['frontend-typecheck','frontend-test','frontend-build','app-hold-integrity','harness-self-check','harness-pytest']
run('registered-checks-retry',['python3','tools/software_workflow/run_registered_checks.py','projects/chirality-app-dev/software-workflow.json',*[v for c in checks for v in ['--check',c]],'--output',str(target),'--timeout-seconds','600'],repo,False)
assert target.is_file()
(out/'REGISTERED_CHECKS.json').write_bytes(target.read_bytes())
print('copied registered report',flush=True)
