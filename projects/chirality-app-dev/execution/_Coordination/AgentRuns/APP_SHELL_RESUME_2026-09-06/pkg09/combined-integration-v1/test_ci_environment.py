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
env.pop('CHIRALITY_INSTRUCTION_ROOT',None)
target=front/'artifacts/combined-integration-v1/FRONTEND_TEST_CI_ENV.json'
args=['python3','tools/software_workflow/run_registered_checks.py','projects/chirality-app-dev/software-workflow.json','--check','frontend-test','--output',str(target),'--timeout-seconds','600']
with (out/'test-ci-env.stdout').open('w') as so,(out/'test-ci-env.stderr').open('w') as se:p=subprocess.run(args,cwd=repo,env=env,stdout=so,stderr=se)
(out/'test-ci-env.json').write_text(json.dumps({'command':args,'cwd':str(repo),'exit_code':p.returncode,'environment_change':'CHIRALITY_INSTRUCTION_ROOT omitted from product-test subprocess, matching CI; native agent launch declaration remains applicable to agent preflights.'},indent=2))
assert target.is_file();(out/'FRONTEND_TEST_CI_ENV.json').write_bytes(target.read_bytes());print('test ci env',p.returncode,flush=True)
