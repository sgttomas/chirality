#!/usr/bin/env python3
"""Bounded rerun: python3 <this file> {release|build|basic|final} <attempt-name>."""
import datetime, hashlib, json, os, pathlib, subprocess, sys, time, shutil
R=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip()); A=R/'projects/chirality-app-dev'; F=A/'frontend'; D=pathlib.Path(__file__).resolve().parent
mode,name=sys.argv[1:]; O=D/name
O.mkdir(exist_ok=False)
def now():return datetime.datetime.now(datetime.timezone.utc).isoformat()
keep=['PATH','HOME','TMPDIR','TMP','TEMP','LANG','LC_ALL','SHELL','USER','LOGNAME','SYSTEMROOT']
env={k:v for k,v in os.environ.items() if k in keep}
env.update(PYTHONDONTWRITEBYTECODE='1',NEXT_TELEMETRY_DISABLED='1',CHIRALITY_HARNESS_PROVIDER='stub')
(O/'environment.json').write_text(json.dumps({'effective':env,'other_inherited_keys_removed': sorted(k for k in os.environ if k not in keep)},indent=2)+'\n')
os.environ.clear();os.environ.update(env)
results=[]
def run(argv,cwd,label):
 t=now();start=time.monotonic();p=subprocess.run(argv,cwd=cwd,env=env,text=True,capture_output=True)
 (O/(label+'.stdout.log')).write_text(p.stdout);(O/(label+'.stderr.log')).write_text(p.stderr)
 row=dict(id=label,argv=argv,cwd=str(cwd),started_at=t,ended_at=now(),duration_seconds=time.monotonic()-start,exit_code=p.returncode)
 results.append(row);(O/'commands.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(row),flush=True);return p
run(['git','status','--short'],R,'git-status');run(['git','rev-parse','HEAD'],R,'git-head')
for argv,label in [(['node','--version'],'node'),(['npm','--version'],'npm'),(['python3','--version'],'python')]:run(argv,R,label)
files=subprocess.check_output(['git','ls-files','-z','projects/chirality-app-dev/frontend','runtime','tools/software_workflow','tools/practitioner_harness','tools/validation/validate_app_dev_loop_receipts.py'],cwd=R).decode().split('\0')
files+=subprocess.check_output(['git','ls-files','--others','--exclude-standard','-z','projects/chirality-app-dev/frontend'],cwd=R).decode().split('\0')
hashes={p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in sorted(set(files)) if p and (R/p).is_file()}
(O/'source-sha256.json').write_text(json.dumps(hashes,indent=2)+'\n')
if mode=='release':
 argv=['python3','execution/_Scripts/app_hold.py','check','--operation','reliance','--entry-path','APP_LOOP_SHELL_2026-09-05:GLOBAL_VALIDATION']
 for target in ['DEL-02-02','DEL-07-03','DEL-03-01','DEL-05-05','DEL-08-04']:argv+=['--target',target]
 if run(argv,A,'app-hold-preflight').returncode:sys.exit(1)
 sys.path.insert(0,str(R/'tools/software_workflow'))
 import run_registered_checks as checks
 # Preserve canonical full stdout/stderr and service logs rather than the default diagnostic tail.
 checks.normalize_evidence_text=lambda value,workspace_root:value
 def full_log(handle,limit=16000):handle.flush();handle.seek(0);return handle.read()
 checks.read_log_tail=full_log
 original_wait=checks.wait_for_service
 def wait_with_readonly_probe(process,url,timeout):
  elapsed=original_wait(process,url,timeout)
  import urllib.request,urllib.error,urllib.parse
  probe_url=url+'/api/harness/session/list?'+urllib.parse.urlencode({'projectRoot':str(A)})
  probe_start=now()
  try:
   with urllib.request.urlopen(probe_url,timeout=30) as response:status=response.status;body=response.read().decode()
  except urllib.error.HTTPError as error:status=error.code;body=error.read().decode()
  (O/'binding-probe.json').write_text(json.dumps({'url':probe_url,'method':'GET','started_at':probe_start,'ended_at':now(),'status':status,'body':body},indent=2)+'\n')
  return elapsed
 checks.wait_for_service=wait_with_readonly_probe
 spec=json.loads((A/'software-workflow.json').read_text())['checks']['frontend-premerge']
 (O/'service-spec.json').write_text(json.dumps(spec,indent=2)+'\n')
 start=now();row=checks.run_check(check_id='release-quality-with-registered-premerge-service',spec=spec,command=['npm','run','validate:release-quality'],cwd=F,project_root=A,workspace_root=R,default_timeout_seconds=1200)
 row['started_at']=start;row['ended_at']=now()
 (O/'registered-result.json').write_text(json.dumps(row,indent=2)+'\n')
 for kind in ['stdout','stderr']:
  (O/('release-quality.'+kind+'.log')).write_text(row[kind])
  if row.get('service'):(O/('service.'+kind+'.log')).write_text(row['service'].get(kind+'_tail',''))
 print(json.dumps({k:v for k,v in row.items() if k not in ['stdout','stderr','service']}),flush=True)
 results.append({'id':row['id'],'exit_code':row['exit_code']})
 for rel in ['release-quality/latest','section9/latest','section8/latest']:
  src=F/'artifacts/harness'/rel
  if src.exists():shutil.copytree(src,O/'artifacts'/rel)
 tmp=pathlib.Path(env.get('TMPDIR','/tmp'))/'chirality-harness-validation/latest'
 if (tmp/'summary.json').exists():shutil.copy2(tmp/'summary.json',O/'section8-source-summary.json')
elif mode=='build':run(['npm','run','build'],F,'frontend-build')
elif mode in ['basic','final']:
 if mode=='basic':
  run(['python3','tools/practitioner_harness/harness.py','self-check'],R,'harness-selfcheck')
  run(['python3','-m','pytest','-q','-p','no:cacheprovider','tools/practitioner_harness'],R,'harness-pytest')
  run(['python3','execution/_Scripts/app_hold.py','scan','--require-register-match'],A,'app-hold-integrity')
 run(['python3','tools/validation/validate_app_dev_loop_receipts.py','--repo-root','.'],R,'receipt-validator')
 run(['git','diff','--check'],R,'diff-check')
else:raise ValueError(mode)
changed=[p for p,h in hashes.items() if not (R/p).is_file() or hashlib.sha256((R/p).read_bytes()).hexdigest()!=h]
(O/'source-stability.json').write_text(json.dumps({'changed_during_check':changed},indent=2)+'\n')
(O/'commands.json').write_text(json.dumps(results,indent=2)+'\n')
manifest={str(p.relative_to(O)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(O.rglob('*')) if p.is_file()}
(O/'evidence-sha256.json').write_text(json.dumps(manifest,indent=2)+'\n')
sys.exit(int(any(r['exit_code'] for r in results)))
