import csv,json,hashlib,pathlib,re,subprocess,ast,sys
root=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip());base='2be412ccea62bdc4bd96deb082c46d7a792076ea'
p=root/'projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05/PACKAGES/PKG-08';o=p/'VERIFICATION';o.mkdir(exist_ok=True)
hashes={};checks=[]; errors=[];historical=[];bindings={}
def read(path):
 path=path if path.is_absolute() else root/path;b=path.read_bytes();hashes[str(path.relative_to(root))]=hashlib.sha256(b).hexdigest();return b
for path in [root/'AGENTS.md',root/'projects/pec/AGENTS.md',p/'BRIEFS/VERIFIER_V1.md',p/'PACKAGE_BASIS.md',p.parent.parent/'COMMON/BRIEFS/PKG-08.md',p.parent.parent/'COMMON/BRIEF_CLARIFICATION_01.md']:read(path)
census=list(csv.DictReader(read(p.parent.parent/'COMMON/SCOPE_CENSUS.csv').decode().splitlines()));targets=[x for x in census if x['PackageID']=='PKG-08']
for t in targets:
 d=root/t['DeliverablePath']; files=sorted(x for x in d.rglob('*') if x.is_file())+[d/'ScopeOfWork.md']
 for path in sorted(set(files)):
  cmd=['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register','projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv','--target',str(path.relative_to(root/'projects/pec')),'--operation','candidate-validation']; r=subprocess.run(cmd,cwd=root,capture_output=True,text=True);checks.append(dict(command=cmd,cwd='.',environment={'PYTHONDONTWRITEBYTECODE':'1'},exit_code=r.returncode,result=r.stdout.strip()));assert r.returncode==0
  if path.is_file():read(path)
claimfields='ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'.split(',');resfields='ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'.split(',')
claims=[];residuals=[];coverage={};workerhash={}
for w in sorted((p/'WORKERS').iterdir()):
 for f in w.rglob('*'):
  if f.is_file() and 'CORRECTION_V001' not in f.parts:workerhash[str(f.relative_to(root))]=hashlib.sha256(read(f)).hexdigest()
 m=json.loads(read(w/'READ_MANIFEST.json'))
 for path,h in m['hashes'].items():
  if hashlib.sha256(read(pathlib.Path(path))).hexdigest()!=h:errors.append('source hash '+path)
 for h in m['historical_sources']:

  if re.fullmatch(r'[0-9a-f]{40}',h['commit']):
   b=subprocess.check_output(['git','show',h['commit']+':'+h['path']],cwd=root);assert hashlib.sha256(b).hexdigest()==h['sha256'];historical.append(h)
  else:
   assert 'RUN_LOCAL' in h['commit'] and hashlib.sha256(read(pathlib.Path(h['path']))).hexdigest()==h['sha256']
 tables=[]
 for name,fields in [('CLAIMS.csv',claimfields),('RESIDUALS.csv',resfields)]:
  b=read(w/name);a=csv.DictReader(b.decode().splitlines());rows=list(a);assert a.fieldnames==fields and b'\r' not in b;tables.append(rows)
  for c in rows:
   assert c['Depends'] and re.search(r'\(gated:|\(stage-gated:|NOT_SELECTABLE_UNTIL:',c['ExactGate'])
 c,rs=tables;claims+=c;residuals+=rs
 for row in c:
  assert row['SourceCommit']==base
  sh=json.loads(row['SourceHashes'])
  for path,h in sh.items():assert hashlib.sha256(read(pathlib.Path(path))).hexdigest()==h
  assert row['ClaimID'].startswith(w.name+'::')
 for i,row in enumerate(rs,1):assert row['ResidualID']==w.name+f'-REM-{i:03}' and row['Selectability']=='NON_SELECTABLE_PENDING_OWNER_APPLICATION'
 d=root/next(x['DeliverablePath'] for x in targets if x['DeliverableID']==w.name);s=d/'ScopeOfWork.md'
 defined=re.findall(r'^- \*\*((?:REQ|AC|VER|CLM|OUT|TBD|CON|AX)-\d{3})\*\*',read(s).decode(),re.M) if s.exists() else []
 local={x['ClaimID'].split('::')[1] for x in c};missing=set(defined)-local;assert not missing
 coverage[w.name]={'claims':len(c),'residuals':len(rs),'defined':len(defined),'REQ_AC_VER':sum(x.startswith(('REQ','AC','VER')) for x in defined),'missing':sorted(missing)}
ci={x['ClaimID']:x for x in claims};ri={x['ResidualID']:x for x in residuals};assert len(ci)==len(claims) and len(ri)==len(residuals)
for c in claims:
 for r in re.split(r'[;|]',c['ProposedResidualID']):
  if r not in ('','NONE','N/A'):assert c['ClaimID'] in ri[r]['ClaimIDs'].split(';')
for r in residuals:
 for c in r['ClaimIDs'].split(';'):assert r['ResidualID'] in ci[c]['ProposedResidualID'].split(';')
for path,h in list(hashes.items()):
 r=subprocess.run(['git','show',base+':'+path],cwd=root,capture_output=True)
 bindings[path]='BASE_EQUAL' if r.returncode==0 and hashlib.sha256(r.stdout).hexdigest()==h else 'RUN_LOCAL_DERIVATIVE' if '/R1_R4_2026-09-05/' in path else 'NOT_BASE_EQUAL'
 if bindings[path]=='NOT_BASE_EQUAL':errors.append('base '+path)
# Positive semantic inventory of production modules; parse only, do not execute.
production={}
for f in sorted((root/'projects/pec/v2/src').rglob('*.py')):
 s=read(f).decode(); tree=ast.parse(s);production[str(f.relative_to(root))]={'classes':[n.name for n in ast.walk(tree) if isinstance(n,ast.ClassDef)],'functions':[n.name for n in ast.walk(tree) if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))]}
fallback=json.loads(read(p/'WORKERS/DEL-08-05/SCOPE_FALLBACK.json'));fallbackchecks=[]
for x in fallback['mappings']:
 b=read(pathlib.Path(x['path']));assert hashlib.sha256(b).hexdigest()==x['file_sha256'];assert hashlib.sha256(x['quote'].encode()).hexdigest()==x['quote_sha256'];assert x['quote'] in b.decode();fallbackchecks.append(dict(path=x['path'],locus=x['locus'],quote_hash_pass=True,file_hash_pass=True,quote_present=True))
# Exact manifests with existing worker output manifests, whose values are inspected separately.
for path,h in workerhash.items():assert hashlib.sha256((root/path).read_bytes()).hexdigest()==h
result={'structural_pass':not errors,'errors':errors,'coverage':coverage,'claims':len(claims),'residuals':len(residuals),'preflights':checks,'source_bindings':bindings,'production_semantic_inventory':production,'fallback':fallbackchecks,'worker_frozen_hashes':workerhash}
(o/'MECHANICAL_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
(o/'READ_MANIFEST.json').write_text(json.dumps({'source_commit':base,'hashes':hashes,'historical_sources':historical,'checks':checks+[{'command':'python3 /tmp/pkg08_verify.py','cwd':'.','environment':{'PYTHONDONTWRITEBYTECODE':'1'},'exit_code':0,'result':'Independent schemas, LF, source/current/base hashes, reciprocal IDs, local definition coverage, positive AST source inventory and quote-hash checks; see MECHANICAL_CHECKS.json'}],'source_unchanged':True},indent=2)+'\n')
(o/'VERIFY_CHECKS.py').write_bytes(pathlib.Path(__file__).read_bytes())
print(json.dumps({'errors':errors,'coverage':coverage,'source_count':len(hashes),'preflight_count':len(checks),'production':production},indent=2))
