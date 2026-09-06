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
run('freshness',['git','fetch','origin','main'],repo);run('ancestor',['git','merge-base','--is-ancestor','origin/main','HEAD'],repo)
tracked=subprocess.check_output(['git','ls-files','-z'],cwd=repo).decode().split('\0');before={p:hashlib.sha256((repo/p).read_bytes()).hexdigest() for p in tracked if p and (repo/p).is_file()};(out/'TRACKED_BEFORE.json').write_text(json.dumps(before,indent=2)+'\n')
run('runtime-npm-ci',['npm','ci'],runtime);run('runtime-build',['npm','run','build'],runtime);run('app-npm-ci',['npm','ci'],front)
checks=['frontend-typecheck','frontend-test','frontend-build','app-hold-integrity','harness-self-check','harness-pytest']
run('registered-checks',['python3','tools/software_workflow/run_registered_checks.py','projects/chirality-app-dev/software-workflow.json',*[v for c in checks for v in ['--check',c]],'--output',str(out/'REGISTERED_CHECKS.json'),'--timeout-seconds','600'],repo,False)
after={p:hashlib.sha256((repo/p).read_bytes()).hexdigest() for p in before};(out/'TRACKED_AFTER_CHECKS.json').write_text(json.dumps(after,indent=2)+'\n');assert before==after,'tracked drift';print('tracked unchanged',len(before),flush=True)
