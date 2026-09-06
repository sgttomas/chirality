import pathlib,subprocess,json,hashlib,datetime,time,os,sys
R=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip());D=pathlib.Path(__file__).resolve().parent;mode,name=sys.argv[1:];O=D/name;O.mkdir(exist_ok=False)
env={k:v for k,v in os.environ.items() if k in ['PATH','HOME','TMPDIR','LANG','LC_ALL']};env['PYTHONDONTWRITEBYTECODE']='1'
base='03e61f38f7b20145552023abd1cf673c2b2a3f61';files=subprocess.check_output(['git','ls-tree','-r','--name-only',base,'projects/chirality-app-dev/frontend','runtime','tools/practitioner_harness'],cwd=R,text=True).splitlines();changed=[];rows={}
for p in files:
 path=R/p
 if not path.is_file():changed.append(p);continue
 h=hashlib.sha256(path.read_bytes()).hexdigest();old=hashlib.sha256(subprocess.check_output(['git','show',base+':'+p],cwd=R)).hexdigest();rows[p]=h
 if h!=old:changed.append(p)
(O/'source-identity.json').write_text(json.dumps({'base':base,'mismatches':changed,'sha256':rows},indent=2)+'\n')
commands=[]
if mode=='full':commands.extend([['python3','tools/practitioner_harness/harness.py','self-check'],['python3','-m','pytest','-q','-p','no:cacheprovider','tools/practitioner_harness']])
commands.extend([['python3','tools/validation/validate_app_dev_loop_receipts.py','--repo-root','.'],['git','diff','--check']]);results=[]
for i,argv in enumerate(commands):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic();p=subprocess.run(argv,cwd=R,env=env,capture_output=True,text=True)
 row={'argv':argv,'cwd':str(R),'environment':env,'started_at':start,'ended_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'duration_seconds':time.monotonic()-t,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'output_representation':'lossless JSON strings; no trimming'}
 (O/f'command-{i+1:02}.json').write_text(json.dumps(row,indent=2)+'\n');results.append({'argv':argv,'exit_code':p.returncode});print(json.dumps(results[-1]),flush=True)
report={'status':'PASS' if not changed and all(r['exit_code']==0 for r in results) else 'FAIL','source_mismatches':changed,'commands':results,'diff_scope':'ordinary unstaged tracked diff only; CHANGE owns full staged check'};(O/'result.json').write_text(json.dumps(report,indent=2)+'\n');manifest={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(O.iterdir()) if p.is_file()};(O/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n');raise SystemExit(report['status']!='PASS')
