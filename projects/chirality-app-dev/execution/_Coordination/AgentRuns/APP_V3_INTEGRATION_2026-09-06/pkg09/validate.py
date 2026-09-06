from pathlib import Path
import subprocess,os,json,hashlib,datetime,shutil
repo=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip());out=Path(__file__).resolve().parent;app=repo/'projects/chirality-app-dev';front=app/'frontend';runtime=repo/'projects/chirality-runtime'
env=os.environ.copy()
removed=[]
for k in list(env):
 if k.startswith('CHIRALITY_') or k.endswith('_API_KEY') or k in ['ANTHROPIC_AUTH_TOKEN','OPENAI_API_KEY']:
  env.pop(k,None);removed.append(k)
env.update({'NEXT_TELEMETRY_DISABLED':'1','CHIRALITY_HARNESS_PROVIDER':'stub'})
def save(n,v):(out/n).write_text(json.dumps(v,indent=2,sort_keys=True)+'\n')
def run(name,args,cwd,stop=True):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat()
 with (out/(name+'.stdout')).open('w') as so,(out/(name+'.stderr')).open('w') as se:p=subprocess.run(args,cwd=cwd,env=env,stdout=so,stderr=se)
 save(name+'.json',{'command':args,'cwd':str(cwd),'environment_overrides':{'NEXT_TELEMETRY_DISABLED':'1','CHIRALITY_HARNESS_PROVIDER':'stub'},'removed_environment_variable_names':removed,'start':start,'end':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':p.returncode});print(name,p.returncode,flush=True)
 if stop:assert p.returncode==0,name
 return p.returncode
run('freshness',['git','fetch','origin','main'],repo);run('ancestor',['git','merge-base','--is-ancestor','origin/main','HEAD'],repo)
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip()=='28a8ed32ba83c5514ae2e65e9260833c1d46b7ef'
run('app-hold',['python3','execution/_Scripts/app_hold.py','check','--operation','reliance','--entry-path','WORKING_ITEMS:APP_V3_INTEGRATION_2026-09-06:PKG09','--target','DEL-09-04'],app)
paths=subprocess.check_output(['git','ls-files','-z','--','projects/chirality-runtime','projects/chirality-app-dev/frontend'],cwd=repo).decode().split('\0')
paths+=subprocess.check_output(['git','ls-files','--others','--exclude-standard','-z','--','projects/chirality-app-dev/frontend'],cwd=repo).decode().split('\0')
before={p:hashlib.sha256((repo/p).read_bytes()).hexdigest() for p in sorted(set(paths)) if p and (repo/p).is_file()};save('SOURCE_BEFORE.json',before)
run('runtime-npm-ci',['npm','ci'],runtime);run('runtime-build',['npm','run','build'],runtime);run('app-npm-ci',['npm','ci'],front)
target=front/'artifacts/app-v3-integration-20260906/REGISTERED_CHECKS.json';target.parent.mkdir(parents=True,exist_ok=True)
checks=['frontend-typecheck','frontend-test','frontend-build','app-hold-integrity','harness-self-check','harness-pytest']
run('registered-checks',['python3','tools/software_workflow/run_registered_checks.py','projects/chirality-app-dev/software-workflow.json',*[v for c in checks for v in ['--check',c]],'--output',str(target),'--timeout-seconds','600'],repo,False)
assert target.is_file();shutil.copyfile(target,out/'REGISTERED_CHECKS.json')
after={p:hashlib.sha256((repo/p).read_bytes()).hexdigest() for p in before};save('SOURCE_AFTER_CHECKS.json',after);assert before==after,'source drift'
print('SOURCE_UNCHANGED',len(before),flush=True)
