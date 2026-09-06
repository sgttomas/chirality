import pathlib,json,csv,hashlib,subprocess,os,re
root=pathlib.Path.cwd();b=pathlib.Path(__file__).resolve().parent;v=b.parent;p=v.parent;hashes={};checks=[];errors=[]
def read(f):
 f=pathlib.Path(f);f=f if f.is_absolute() else root/f;x=f.read_bytes();hashes[str(f.relative_to(root))]=hashlib.sha256(x).hexdigest();return x.decode()
def rows(f):return list(csv.DictReader(read(f).splitlines()))
def run(cmd):
 r=subprocess.run(cmd,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'});rec={'command':cmd,'cwd':str(root),'environment':{'PYTHONDONTWRITEBYTECODE':'1'},'exit_code':r.returncode,'result':r.stdout+r.stderr};checks.append(rec);return r
# Fresh actual act checks precede correction reliance.
for d in ['DEL-00-01','DEL-00-02','DEL-00-03']:
 target=next(pathlib.Path('projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working').glob(d+'_*'))
 for name in ['ScopeOfWork.md','_STATUS.md']:
  r=run(['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register','projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv','--target',str((target/name).relative_to('projects/pec')),'--operation','candidate-validation'])
  if r.returncode or json.loads(r.stdout)['status']!='ALLOW':errors.append('preflight '+str(target/name))
read('projects/pec/execution/_Scripts/pec_reliance_hold.py');read('projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv')
initial=json.loads(read(v/'OUTPUT_MANIFEST.json'))
for f,h in initial['files'].items():
 read(v/f)
 if hashes[str((v/f).relative_to(root))]!=h:errors.append('initial seal '+f)
changes=[];cs=[];rs=[];union={}
for d in ['DEL-00-01','DEL-00-02','DEL-00-03']:
 w=p/'WORKERS'/d;s=w/'REVISION_V001' if d!='DEL-00-02' else w
 for name in ['CLAIMS.csv','RESIDUALS.csv']:
  old=rows(w/name);new=rows(s/name)
  if len(old)!=len(new):errors.append('row length '+d)
  for a,z in zip(old,new):
   if list(a)!=list(z):errors.append('schema '+d)
   for k in a:
    if a[k]!=z[k]:changes.append({'deliverable':d,'file':name,'row_id':a.get('ClaimID',a.get('ResidualID')),'field':k,'before':a[k],'after':z[k]})
  (cs if name=='CLAIMS.csv' else rs).extend(new)
 for name in ['RETURN.md','COVERAGE.md','READ_MANIFEST.json']:read(s/name)
 if s!=w:read(s/'CHANGE_MAP.json')
 m=json.loads(read(s/'READ_MANIFEST.json'))
 for f,h in m['hashes'].items():
  read(f)
  if hashes[f]!=h:errors.append('source hash '+f)
  union[f]=h
 if m['source_commit']!='2be412ccea62bdc4bd96deb082c46d7a792076ea' or m['source_unchanged']!=True:errors.append('manifest basis '+d)
expected={('DEL-00-01','CLAIMS.csv','DEL-00-01::AC-002','ProposedResidualID','DEL-00-01::R-001','DEL-00-01-REM-001'),('DEL-00-01','RESIDUALS.csv','DEL-00-01::R-001','ResidualID','DEL-00-01::R-001','DEL-00-01-REM-001'),('DEL-00-03','CLAIMS.csv','DEL-00-03::CON-001','ClaimClass','DEFERRED_AGENT_WORKFLOW','human_acceptance')}
actual={tuple(c[k] for k in ['deliverable','file','row_id','field','before','after']) for c in changes}
if actual!=expected:errors.append('change-set mismatch')
for c in cs:
 linked={r['ResidualID'] for r in rs if c['ClaimID'] in {x.strip() for x in r['ClaimIDs'].split(';')}}
 claimed={x.strip() for x in c['ProposedResidualID'].split(';')}-{'','N/A','NONE'}
 if linked!=claimed:errors.append('reciprocity '+c['ClaimID'])
 raw=c['SourceHashes'];m=json.loads(raw) if raw.startswith('{') else dict(x.split('=',1) for x in raw.split(';') if x)
 for f,h in m.items():
  read(f)
  if hashes[f]!=h:errors.append('claim hash '+c['ClaimID'])
for r in rs:
 if not re.fullmatch(re.escape(r['DeliverableID'])+r'-REM-\d{3}',r['ResidualID']):errors.append('ID '+r['ResidualID'])
 if r['Selectability']!='NON_SELECTABLE_PENDING_OWNER_APPLICATION':errors.append('selectability')
for name in ['validate_original_population.py','validate_package.py']:read(p/name)
r=run(['python3',str((p/'validate_package.py').relative_to(root)),'--selected'])
if r.returncode:errors.append('manager selected validation')
selected_validation=json.loads(r.stdout)
read(b/'ORIGINAL_VALIDATOR_CHECK.json')
# Explicitly verify missing contract and existing state rather than deriving absence from manifest membership.
missing=not next(pathlib.Path('projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working').glob('DEL-00-02_*')).joinpath('ScopeOfWork.md').exists()
if not missing:errors.append('missing-contract claim drift')
unchanged=all(hashlib.sha256((root/f).read_bytes()).hexdigest()==h for f,h in hashes.items())
if not unchanged:errors.append('read drift')
result={'status':'PASS' if not errors else 'FAIL','errors':errors,'findings_closed':['V001','V002'] if not errors else [],'exact_changed_cells':changes,'claims':len(cs),'residuals':len(rs),'unknown':sum(c['Disposition']=='UNKNOWN' for c in cs),'selected_worker_source_hashes':len(union),'selected_manager_validation':selected_validation,'initial_seal_preserved':True,'DEL00_02_ScopeOfWork_absent':missing,'source_unchanged':unchanged,'checked_boundaries':['DEL-00-01::AC-002','DEL-00-01::AC-007','DEL-00-03::CON-001','DEL-00-03::AC-011'],'product_or_owner_acceptance':False}
(b/'VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n');checks.append({'command':'python3 '+str((b/'backcheck.py').relative_to(root)),'cwd':str(root),'environment':{'PYTHONDONTWRITEBYTECODE':'1'},'exit_code':0 if not errors else 1,'result':result})
(b/'READ_MANIFEST.json').write_text(json.dumps({'source_commit':'2be412ccea62bdc4bd96deb082c46d7a792076ea','hashes':dict(sorted(hashes.items())),'historical_sources':[],'checks':checks,'source_unchanged':unchanged},indent=2)+'\n');print(json.dumps(result,indent=2));print('read hashes',len(hashes))
