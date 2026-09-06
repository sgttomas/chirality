import pathlib,subprocess,json,hashlib,datetime,os,sys
root=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
runtime=root/'projects/chirality-runtime'
out=pathlib.Path(__file__).resolve().parent
records=[]
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def run(label,args,cwd,required=True):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat()
 with (out/(label+'.stdout.log')).open('w') as stdout,(out/(label+'.stderr.log')).open('w') as stderr:
  p=subprocess.run(args,cwd=cwd,stdout=stdout,stderr=stderr)
 record={'label':label,'command':args,'cwd':str(cwd),'started_utc':start,'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':p.returncode,'stdout':label+'.stdout.log','stderr':label+'.stderr.log'}
 records.append(record); (out/'COMMANDS.json').write_text(json.dumps(records,indent=2)+'\n')
 print(label+': exit '+str(p.returncode),flush=True)
 if required and p.returncode: return False
 return True
files=subprocess.check_output(['git','ls-files','-z','projects/chirality-runtime'],cwd=root).decode().split('\0'); files=sorted(x for x in files if x)
def identity():
 return {p:digest(root/p) if (root/p).is_file() else None for p in files}
before=identity(); (out/'TRACKED_BEFORE.json').write_text(json.dumps(before,indent=2)+'\n')
status_before=subprocess.check_output(['git','status','--porcelain=v1','-uall','--','projects/chirality-runtime'],cwd=root,text=True)
(out/'runtime-status-before.log').write_text(status_before)
assert not status_before, 'Runtime is dirty before preparation'
env={k:os.environ[k] for k in ['PATH','SHELL','LANG','LC_ALL','NODE_ENV','CI','TMPDIR','npm_config_cache','npm_config_ignore_scripts','npm_config_registry'] if k in os.environ}
(out/'ENVIRONMENT.json').write_text(json.dumps({'environment':'inherited process environment; only nonsecret tool-relevant variables captured; credentials/tokens excluded','variables':env,'engine':'Codex native harness','provider':'OpenAI','model':'GPT-6 (system identity, exact deployment unavailable)','role':'CHANGE Agent 1','execution_class':'delegated-harness-native','enforcement':'instruction-asserted','parent':'/root','instance':'/root/resume_change'},indent=2)+'\n')
run('node-version',['node','--version'],runtime); run('npm-version',['npm','--version'],runtime)
preflight=['python3','execution/_Scripts/app_hold.py','check','--operation','reliance','--entry-path','APP_SHELL_RESUME_2026-09-06:CHANGE_RUNTIME_PREPARATION']
for target in ['DEL-02-01','DEL-02-02','DEL-02-03','DEL-02-04','DEL-02-05','DEL-07-03']: preflight.extend(['--target',target])
success=run('app-hold-preflight',preflight,root/'projects/chirality-app-dev')
if success: success=run('npm-ci',['npm','ci'],runtime)
if success: success=run('npm-build',['npm','run','build'],runtime)
after=identity(); (out/'TRACKED_AFTER.json').write_text(json.dumps(after,indent=2)+'\n')
status_after=subprocess.check_output(['git','status','--porcelain=v1','-uall','--','projects/chirality-runtime'],cwd=root,text=True)
(out/'runtime-status-after.log').write_text(status_after)
changed=[p for p in files if before[p]!=after[p]]
outputs=sorted([p for p in runtime.glob('packages/*/dist/**/*') if p.is_file()])
installed_lock=runtime/'node_modules/.package-lock.json'
if installed_lock.is_file(): outputs.append(installed_lock)
manifest={str(p.relative_to(root)):{'sha256':digest(p),'bytes':p.stat().st_size} for p in sorted(outputs)}
(out/'OUTPUT_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
ignored_check=subprocess.run(['git','check-ignore','--stdin'],cwd=root,input='\n'.join(manifest)+'\n',text=True,capture_output=True)
(out/'ignored-outputs.log').write_text(ignored_check.stdout)
all_ignored=set(ignored_check.stdout.splitlines())==set(manifest)
success=success and before==after and status_before==status_after and all_ignored
verdict={'success':success,'tracked_count':len(files),'tracked_unchanged':before==after,'changed_tracked_paths':changed,'runtime_status_unchanged':status_before==status_after,'all_manifest_outputs_ignored':all_ignored,'output_manifest_count':len(manifest),'source_snapshot':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),'rerun':'npm ci then npm run build in projects/chirality-runtime, under same approved ignored-output scope; recapture tracked identity and status','scope':'ignored existing dependencies/build outputs only; no source/lock edit or operational engine activation'}
(out/'RESULT.json').write_text(json.dumps(verdict,indent=2)+'\n')
(out/'RETURN.md').write_text('# Runtime dependency preparation return\n\n'+('SUCCESS' if success else 'FAILED')+' — see RESULT.json and exact COMMANDS.json/logs.\n\nApproved owner selection: OWNER_STEER_v2.md Runtime A; parent release under graph/plan v7 and instances/resume_change/AMENDMENT_v2.md. This is derivative environment preparation evidence from the recorded Git source snapshot, not Runtime scope acceptance. No product source, lock, commit, push, branch or operational registration action authorized or performed. Actual package validation remains owned by PKG02.\n\nTracked preservation: '+str(before==after)+'; Runtime status unchanged: '+str(status_before==status_after)+'; all recorded output paths ignored: '+str(all_ignored)+'.\n\n'+('Preparation CLOSED; parent may release dependent existing-source validation. No remaining preparation blocker.' if success else 'Preparation NOT CLOSED; parent must inspect concrete failed command or preservation condition before dependent validation.')+'\n')
manifest_artifacts={str(p.relative_to(out)):digest(p) for p in sorted(out.iterdir()) if p.is_file() and p.name!='ARTIFACT_MANIFEST.json'}
(out/'ARTIFACT_MANIFEST.json').write_text(json.dumps(manifest_artifacts,indent=2)+'\n')
print(json.dumps(verdict),flush=True)
sys.exit(0 if success else 1)
