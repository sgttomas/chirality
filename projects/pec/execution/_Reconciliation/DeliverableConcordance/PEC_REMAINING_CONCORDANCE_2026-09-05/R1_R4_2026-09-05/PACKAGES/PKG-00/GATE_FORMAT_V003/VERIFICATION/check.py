import pathlib,json,csv,hashlib,subprocess,os,io,collections
root=pathlib.Path.cwd();v=pathlib.Path(__file__).resolve().parent;g=v.parent;p=g.parent;a=g/'AUTHOR';v2=p/'GATE_FORMAT_V002';pre=v2/'PREIMAGES';old=p/'WORKERS/DEL-00-01/REVISION_V001';hashes={};checks=[];errors=[]
def read(f):
 f=pathlib.Path(f);f=f if f.is_absolute() else root/f;x=f.read_bytes();hashes[str(f.relative_to(root))]=hashlib.sha256(x).hexdigest();return x.decode()
def sha(f):read(f);return hashes[str(pathlib.Path(f).resolve().relative_to(root))]
def rows(f):return list(csv.DictReader(io.StringIO(read(f))))
def diff(before,after,name):
 if len(before)!=len(after):errors.append('row count '+name)
 out=[]
 for x,y in zip(before,after):
  if list(x)!=list(y):errors.append('schema '+name)
  for k in x:
   if x[k]!=y[k]:out.append({'file':name,'id':x.get('ClaimID',x.get('ResidualID')),'field':k,'before':x[k],'after':y[k]})
 return out
if sha(g/'VERIFIER_BRIEF.md')!='e673532c4680d74a7d3c8731adcb585c3175b1f3d4202ecb187c54e72656104f':errors.append('brief seal')
target='execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/'
for n in ['ScopeOfWork.md','_STATUS.md']:
 cmd=['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register','projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv','--target',target+n,'--operation','candidate-validation'];r=subprocess.run(cmd,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'});checks.append({'command':cmd,'cwd':str(root),'environment':{'PYTHONDONTWRITEBYTECODE':'1'},'exit_code':r.returncode,'result':r.stdout+r.stderr})
 if r.returncode or json.loads(r.stdout)['status']!='ALLOW':errors.append('hold '+n)
read('projects/pec/execution/_Scripts/pec_reliance_hold.py');read('projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv')
direct=[];composed=[];prospective={};baseline={}
for name in ['CLAIMS.csv','RESIDUALS.csv']:
 orig=rows(old/name);prev=rows(v2/'AUTHOR'/name);new=rows(a/name)
 direct+=diff(prev,new,name);composed+=diff(orig,new,name)
 base=rows(pre/('PACKAGE_'+name));baseline[name]=base
 if rows(p/('PACKAGE_'+name))!=base or sha(p/('PACKAGE_'+name))!=sha(pre/('PACKAGE_'+name)):errors.append('changed aggregate before PASS')
 if [x for x in base if x['DeliverableID']=='DEL-00-01']!=orig:errors.append('selected preimage mismatch')
 newby={x.get('ClaimID',x.get('ResidualID')):x for x in new}
 prospective[name]=[newby[x.get('ClaimID',x.get('ResidualID'))] if x['DeliverableID']=='DEL-00-01' else x for x in base]
 if name=='CLAIMS.csv':
  exp=[]
  for row in prev:
   z=dict(row)
   if z['Depends']=='':z['Depends']='NONE'
   exp.append(z)
  if exp!=new:errors.append('direct blank replacement mismatch')
  buf=io.StringIO(newline='');w=csv.DictWriter(buf,fieldnames=list(prev[0]),lineterminator='\n');w.writeheader();w.writerows(exp)
  if buf.getvalue()!=read(a/name):errors.append('unexpected csv bytes')
 elif read(a/name)!=read(v2/'AUTHOR'/name):errors.append('residual byte drift')
if len(direct)!=42 or any(z['file']!='CLAIMS.csv' or z['field']!='Depends' or z['before']!='' or z['after']!='NONE' for z in direct):errors.append('direct delta')
if len(composed)!=44:errors.append('composed delta')
for z in composed:
 if z in direct:continue
 if z['field']!='ExactGate' or z['after']!='NOT_SELECTABLE_UNTIL: '+z['before'] or z['id'] not in ['DEL-00-01::AC-002','DEL-00-01-REM-001']:errors.append('composed gate delta')
full=diff(baseline['CLAIMS.csv'],prospective['CLAIMS.csv'],'CLAIMS.csv')+diff(baseline['RESIDUALS.csv'],prospective['RESIDUALS.csv'],'RESIDUALS.csv')
if full!=composed:errors.append('prospective full delta differs')
cs=prospective['CLAIMS.csv'];rs=prospective['RESIDUALS.csv']
if len(cs)!=87 or len(rs)!=6 or sum(z['DeliverableID']=='DEL-00-01' for z in cs)!=43:errors.append('aggregate counts')
if len(set(z['ClaimID'] for z in cs))!=87 or len(set(z['ResidualID'] for z in rs))!=6:errors.append('duplicate IDs')
for c in cs:
 expected={r['ResidualID'] for r in rs if c['ClaimID'] in {x.strip() for x in r['ClaimIDs'].split(';')}}
 actual={x.strip() for x in c['ProposedResidualID'].split(';')}-{'','N/A','NONE'}
 if actual!=expected:errors.append('reciprocity '+c['ClaimID'])
# Author and referenced current source checks are mechanical identity only.
am=json.loads(read(a/'READ_MANIFEST.json'))
for z in am['reads']:
 if sha(z['path'])!=z['sha256']:errors.append('author hash '+z['path'])
source={}
for z in rows(a/'CLAIMS.csv'):
 for x in z['SourceHashes'].split(';'):
  f,h=x.split('=',1);source[f]=h
for f,h in source.items():
 if sha(f)!=h:errors.append('source drift '+f)
read(a/'RETURN.md');read(a/'CHANGE_MAP.json')
m=json.loads(read(pre/'OUTPUT_MANIFEST.json'))
for f,h in m['files'].items():
 rel=(root/f).relative_to(p);loc=pre/rel if (pre/rel).is_file() else root/f
 if sha(loc)!=h:errors.append('original package seal '+f)
sm=json.loads(read(v2/'VERIFICATION/OUTPUT_MANIFEST.json'))
for f,h in sm['files'].items():
 if sha(v2/'VERIFICATION'/f)!=h:errors.append('V002 verifier seal '+f)
unchanged=all(hashlib.sha256((root/f).read_bytes()).hexdigest()==h for f,h in hashes.items())
if not unchanged:errors.append('source final drift')
result={'status':'PASS' if not errors else 'FAIL','errors':errors,'direct_changes':direct,'composed_changes':composed,'direct_cell_count':len(direct),'composed_cell_count':len(composed),'prospective_aggregate_changed_cells':len(full),'claims':len(cs),'residuals':len(rs),'DEL00_01_claims':43,'DEL00_01_residuals':1,'unknown':sum(x['Disposition']=='UNKNOWN' for x in cs),'dispositions':dict(collections.Counter(x['Disposition'] for x in cs)),'author_read_hashes_verified':len(am['reads']),'source_hashes_verified':len(source),'original_package_manifest_entries_verified':len(m['files']),'V002_verifier_seal_verified':True,'current_aggregates_equal_preimages':True,'source_unchanged':unchanged,'semantic_rerun':False}
(v/'VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n');checks.append({'command':'python3 '+str((v/'check.py').relative_to(root)),'cwd':str(root),'environment':{'PYTHONDONTWRITEBYTECODE':'1'},'exit_code':0 if not errors else 1,'result':{k:z for k,z in result.items() if k not in ['direct_changes','composed_changes']}})
(v/'READ_MANIFEST.json').write_text(json.dumps({'source_commit':'2be412ccea62bdc4bd96deb082c46d7a792076ea','hashes':dict(sorted(hashes.items())),'historical_sources':[],'checks':checks,'source_unchanged':unchanged},indent=2)+'\n');print(json.dumps({k:z for k,z in result.items() if k not in ['direct_changes','composed_changes']},indent=2))
