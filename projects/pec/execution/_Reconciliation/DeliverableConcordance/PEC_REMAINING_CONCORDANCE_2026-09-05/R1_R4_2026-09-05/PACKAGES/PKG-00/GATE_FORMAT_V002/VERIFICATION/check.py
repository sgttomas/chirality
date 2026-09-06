import pathlib,json,csv,hashlib,subprocess,os,io
root=pathlib.Path.cwd();v=pathlib.Path(__file__).resolve().parent;g=v.parent;p=g.parent;a=g/'AUTHOR';pre=g/'PREIMAGES';old=p/'WORKERS/DEL-00-01/REVISION_V001';hashes={};checks=[];errors=[]
def read(f):
 f=pathlib.Path(f);f=f if f.is_absolute() else root/f;b=f.read_bytes();hashes[str(f.relative_to(root))]=hashlib.sha256(b).hexdigest();return b.decode()
def sha(f):read(f);return hashes[str(pathlib.Path(f).resolve().relative_to(root))]
def rows(f):return list(csv.DictReader(io.StringIO(read(f))))
brief=sha(g/'VERIFIER_BRIEF.md')
if brief!='9d5bf561b1e8df6a64626d9cb128089882a1d01ca81ed037bff18637dd300d87':errors.append('brief seal')
# Actual exact contract/status checks; author's broad directory record is not reused.
target='execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures/'
for name in ['ScopeOfWork.md','_STATUS.md']:
 cmd=['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register','projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv','--target',target+name,'--operation','candidate-validation'];r=subprocess.run(cmd,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'});checks.append({'command':cmd,'cwd':str(root),'environment':{'PYTHONDONTWRITEBYTECODE':'1'},'exit_code':r.returncode,'result':r.stdout+r.stderr})
 if r.returncode or json.loads(r.stdout)['status']!='ALLOW':errors.append('hold '+name)
changes=[];counts={}
for name,key,wanted in [('CLAIMS.csv','ClaimID','DEL-00-01::AC-002'),('RESIDUALS.csv','ResidualID','DEL-00-01-REM-001')]:
 before=rows(old/name);after=rows(a/name);counts[name]=len(after)
 if len(before)!=len(after):errors.append('count '+name)
 for x,y in zip(before,after):
  if list(x)!=list(y):errors.append('schema '+name)
  for k in x:
   if x[k]!=y[k]:
    changes.append({'file':name,'id':x[key],'field':k,'before':x[k],'after':y[k]})
    if x[key]!=wanted or k!='ExactGate' or y[k]!='NOT_SELECTABLE_UNTIL: '+x[k]:errors.append('unexpected cell '+name+' '+x[key]+' '+k)
 expected=read(old/name).replace(next(z['ExactGate'] for z in before if z[key]==wanted),'NOT_SELECTABLE_UNTIL: '+next(z['ExactGate'] for z in before if z[key]==wanted),1)
 if read(a/name)!=expected:errors.append('byte delta '+name)
 original_aggregate=rows(pre/('PACKAGE_'+name))
 if [z for z in original_aggregate if z['DeliverableID']=='DEL-00-01']!=before:errors.append('preimage selected identity '+name)
 if sha(pre/('PACKAGE_'+name))!=sha(p/('PACKAGE_'+name)):errors.append('aggregate changed before PASS '+name)
if len(changes)!=2 or counts!={'CLAIMS.csv':43,'RESIDUALS.csv':1}:errors.append('exact population')
c=rows(a/'CLAIMS.csv');r=rows(a/'RESIDUALS.csv')
if len(set(x['ClaimID'] for x in c))!=43:errors.append('duplicate IDs')
for x in c:
 wanted={y['ResidualID'] for y in r if x['ClaimID'] in {z.strip() for z in y['ClaimIDs'].split(';')}}
 actual={z.strip() for z in x['ProposedResidualID'].split(';')}-{'','N/A','NONE'}
 if wanted!=actual:errors.append('reciprocity '+x['ClaimID'])
am=json.loads(read(a/'READ_MANIFEST.json'))
for x in am['reads']:
 if sha(x['path'])!=x['sha256']:errors.append('author read drift '+x['path'])
source_rows={}
for x in c:
 for item in x['SourceHashes'].split(';'):
  f,h=item.split('=',1);source_rows[f]=h
for f,h in source_rows.items():
 if sha(f)!=h:errors.append('current source drift '+f)
read(a/'CHANGE_MAP.json');read(a/'RETURN.md')
manifest=json.loads(read(pre/'OUTPUT_MANIFEST.json'));resolved=[];successors=[]
for f,h in manifest['files'].items():
 original=root/f;relative=original.relative_to(p)
 shifted=pre/relative
 use=shifted if shifted.is_file() else original
 if sha(use)!=h:errors.append('preimage manifest '+f)
 if shifted.is_file() and sha(original)!=h:successors.append(str(relative))
 resolved.append({'original':f,'resolved':str(use.relative_to(root)),'sha256':h})
# Every read source's checkpoint identity, including shifted provenance.
unchanged=all(hashlib.sha256((root/f).read_bytes()).hexdigest()==h for f,h in hashes.items())
if not unchanged:errors.append('read drift')
result={'status':'PASS' if not errors else 'FAIL','errors':errors,'counts':counts,'exact_changes':changes,'gate_semantics_unchanged':not errors,'author_read_hashes_verified':len(am['reads']),'current_source_hashes_verified':len(source_rows),'preimage_manifest_entries_verified':len(resolved),'preimage_resolution':resolved,'declared_current_report_successors':successors,'aggregates_unchanged_before_selection':True,'source_unchanged':unchanged,'semantic_tests':'NOT_RERUN: exact representation-only successor','author_preflight_limitation':'Author directory/repository-prefixed target is not reused as exact-target evidence; verifier independently executed exact project-relative ScopeOfWork.md and _STATUS.md candidate-validation ALLOW.'}
(v/'VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n');checks.append({'command':'python3 '+str((v/'check.py').relative_to(root)),'cwd':str(root),'environment':{'PYTHONDONTWRITEBYTECODE':'1'},'exit_code':0 if not errors else 1,'result':{k:z for k,z in result.items() if k!='preimage_resolution'}})
(v/'READ_MANIFEST.json').write_text(json.dumps({'source_commit':'2be412ccea62bdc4bd96deb082c46d7a792076ea','hashes':dict(sorted(hashes.items())),'historical_sources':[],'checks':checks,'source_unchanged':unchanged},indent=2)+'\n');print(json.dumps({k:z for k,z in result.items() if k!='preimage_resolution'},indent=2))
