#!/usr/bin/env python3
"""Bounded rerun: python3 <this file> {release|build|security|basic|final} <attempt-name>."""
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
activation_path=D/'ACTIVATION_PROVISIONAL_v10.json'
if not activation_path.is_file():raise RuntimeError('Parent final freeze/review activation missing; checks prohibited')
activation=json.loads(activation_path.read_text())
if activation.get('parent_go') is not True:raise RuntimeError('Parent execution go absent')
freeze_path=R/activation['freeze_path']
if hashlib.sha256(freeze_path.read_bytes()).hexdigest()!=activation['freeze_sha256']:raise RuntimeError('Freeze identity mismatch')
for path,digest in activation['sequencing_pins'].items():
 if hashlib.sha256((R/path).read_bytes()).hexdigest()!=digest:raise RuntimeError('Sequencing identity mismatch')
if activation.get('review_verdict')!='PENDING':raise RuntimeError('This runner produces provisional evidence only')
freeze=json.loads(freeze_path.read_text())
files_final=freeze['files'];errors=[]
for x in files_final:
 p=R/x['path']
 if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=x['sha256']:errors.append(x['path'])
inventory_path=R/activation['inventory_path'];inventory=json.loads(inventory_path.read_text())
if hashlib.sha256(inventory_path.read_bytes()).hexdigest()!=activation['inventory_sha256']:errors.append('inventory identity mismatch')
root_prefix=inventory['root'];allowed=[root_prefix+'/'+p for p in inventory['product']+inventory['tests']]
if any(x['path'] not in allowed for x in files_final):errors.append('frozen source outside declared inventory')
inventory_hashes={p:hashlib.sha256((R/p).read_bytes()).hexdigest() if (R/p).is_file() else None for p in allowed}
(O/'final-inventory-identities.json').write_text(json.dumps({'inventory_count':len(allowed),'sha256':inventory_hashes,'declared_tests':inventory['tests']},indent=2)+'\n')
(O/'freeze-verification.json').write_text(json.dumps({'activation_sha256':hashlib.sha256(activation_path.read_bytes()).hexdigest(),'source_freeze_sha256':hashlib.sha256(freeze_path.read_bytes()).hexdigest(),'review_verdict':'PENDING; final acceptance HELD','errors':errors},indent=2)+'\n')
if errors:raise RuntimeError(errors)
def run(argv,cwd,label):
 t=now();start=time.monotonic();p=subprocess.run(argv,cwd=cwd,env=env,text=True,capture_output=True)
 (O/(label+'.output.json')).write_text(json.dumps({'stdout':p.stdout,'stderr':p.stderr},indent=2)+'\n')
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
 for target in ['DEL-02-03']:argv+=['--target',target]
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
 # Full canonical wrapper and service output strings retained losslessly in registered-result.json.
 print(json.dumps({k:v for k,v in row.items() if k not in ['stdout','stderr','service']}),flush=True)
 results.append({'id':row['id'],'exit_code':row['exit_code']})
 for rel in ['release-quality/latest','section9/latest','section8/latest']:
  src=F/'artifacts/harness'/rel
  if src.exists():
   dest=O/'artifacts'/rel;dest.mkdir(parents=True,exist_ok=True)
   for f in src.rglob('*'):
    if not f.is_file():continue
    target=dest/f.relative_to(src);target.parent.mkdir(parents=True,exist_ok=True)
    if f.suffix=='.json':target.write_bytes(f.read_bytes())
    else:target.with_suffix(target.suffix+'.json').write_text(json.dumps({'source_name':str(f.relative_to(src)),'text':f.read_text()},indent=2)+'\n')
 tmp=pathlib.Path(env.get('TMPDIR','/tmp'))/'chirality-harness-validation/latest'
 if (tmp/'summary.json').exists():shutil.copy2(tmp/'summary.json',O/'section8-source-summary.json')
elif mode=='build':
 outcome=run(['npm','run','build'],F,'frontend-build')
 artifacts=['dist-electron/main.js','dist-electron/preload.js','dist-runtime/chirality-cli.mjs']
 artifact_rows={p:hashlib.sha256((F/p).read_bytes()).hexdigest() if (F/p).is_file() else None for p in artifacts}
 native=pathlib.Path('/private/tmp/app-loop-t3-native-ac3dexfs/runtime/Electron.app/Contents/MacOS/Electron')
 native_hash=hashlib.sha256(native.read_bytes()).hexdigest() if native.is_file() else None
 (O/'built-artifact-identities.json').write_text(json.dumps({'build_exit_code':outcome.returncode,'artifacts':artifact_rows,'build_success_required_for_current_claim':True,'native_electron_path':str(native),'native_electron_sha256':native_hash,'expected_native_electron_sha256':'79019361f697c1a81489dba3e94631b0977770c1ab15236f1f033f9de6238874','native_launched_by_executor':False},indent=2)+'\n')
elif mode=='tests':
 run(['npm','run','test','--','--testTimeout=15000'],F,'full-tests')
 run(['npm','run','typecheck'],F,'typecheck')
elif mode=='security':
 run(['npm','run','proof:secret-scan'],F,'secret-scan')
 summary=F/'artifacts/harness/security/latest/secret-scan-summary.json'
 if summary.is_file():(O/'secret-scan-summary.json').write_bytes(summary.read_bytes())
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
sys.exit(int(bool(changed) or any(r['exit_code'] for r in results)))
