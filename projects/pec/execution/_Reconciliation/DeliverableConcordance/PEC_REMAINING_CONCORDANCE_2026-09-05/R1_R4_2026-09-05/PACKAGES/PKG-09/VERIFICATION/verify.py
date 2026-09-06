from pathlib import Path
import csv,json,hashlib,re,subprocess,os
P=Path(__file__).resolve().parent.parent.relative_to(Path.cwd()); V=P/'VERIFICATION'; COMMON=P.parent.parent/'COMMON';BASE='2be412ccea62bdc4bd96deb082c46d7a792076ea'
H={};checks=[];errors=[];maps=[]
def read(p):
 p=Path(p);b=p.read_bytes();H[str(p)]=hashlib.sha256(b).hexdigest();return b.decode()
def js(p):return json.loads(read(p))
def rows(p):return list(csv.DictReader(read(p).splitlines()))
def check(ok,msg):
 if not ok:errors.append(msg)
def writej(name,o):(V/name).write_text(json.dumps(o,indent=2)+'\n')
def csvout(name,rs,fields=None):
 with (V/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields or list(rs[0]),lineterminator='\n');w.writeheader();w.writerows(rs)
for m in [COMMON/'SOURCE_MANIFEST.json',COMMON/'COMMON_FROZEN_MANIFEST.json',P/'SOURCE_MANIFEST.json']:
 d=js(m)
 for p,h in d.get('hashes',{}).items():read(p);check(H[p]==h,'frozen drift '+p)
claims=[];res=[]
C='ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'
R='ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'
for w in sorted((P/'WORKERS').iterdir()):
 for p in w.iterdir():
  if p.is_file():read(p)
 c=rows(w/'CLAIMS.csv');r=rows(w/'RESIDUALS.csv');claims+=c;res+=r
 for name,header in [('CLAIMS.csv',C),('RESIDUALS.csv',R)]:
  s=read(w/name);check(s.splitlines()[0]==header,'schema '+str(w/name));check('\r' not in s,'LF '+str(w/name))
 m=js(w/'READ_MANIFEST.json');check(m['source_unchanged'],'source unchanged flag')
 for p,h in m['hashes'].items():read(p);check(H[p]==h,'worker source drift '+p)
 for p in w.glob('*MAP*'):
  d=rows(p) if p.suffix=='.csv' else js(p)
  def visit(o):
   if isinstance(o,list):
    for x in o:visit(x)
   elif isinstance(o,dict):
    q=o.get('quote',o.get('ExactQuote',o.get('Quote')));h=o.get('quote_sha256',o.get('QuoteSHA256'));src=o.get('source',o.get('SourcePath',o.get('Source',o.get('source_path'))))
    if q and h:
     check(hashlib.sha256(q.encode()).hexdigest()==h,'quote hash '+str(p));check(bool(src),'quote source '+str(p))
     if src:
      source_text=read(src); representation='literal source excerpt';match=q in source_text
      if not match and q.startswith('{') and src.endswith('.csv'):
       parsed=json.loads(q);match=parsed in list(csv.DictReader(source_text.splitlines()));representation='JSON serialization of complete parsed CSV row; independently compared all fields'
      check(match,'quote occurrence '+str(p));maps.append({'mapping':str(p),'source':src,'locus':o.get('locus',o.get('SourceLocus',o.get('Locus',''))),'quote_sha256':h,'representation':representation})
    for x in o.values():
     if isinstance(x,(dict,list)):visit(x)
  visit(d)
ci={x['ClaimID']:x for x in claims};ri={x['ResidualID']:x for x in res}
check(len(ci)==len(claims)==110,'claim count uniqueness');check(len(ri)==len(res)==9,'residual count uniqueness')
for c in claims:
 check(c['ClaimID'].startswith(c['DeliverableID']+'::'),'claim prefix');check(c['SourceCommit']==BASE,'base');check(bool(c['Depends']),'depends');check(any(x in c['ExactGate'] for x in ['NOT_SELECTABLE_UNTIL:','(gated:','(stage-gated:']),'gate')
 for rid in filter(lambda x:x and x!='NONE',c['ProposedResidualID'].split(';')):check(rid in ri and c['ClaimID'] in ri[rid]['ClaimIDs'].split(';'),'claim reciprocity')
 try:
  for p,h in json.loads(c['SourceHashes']).items():read(p);check(H[p]==h,'claim hash '+p)
 except (json.JSONDecodeError,AttributeError):
  for p,h in re.findall(r'([^;=]+)=([0-9a-f]{64})',c['SourceHashes']):read(p.strip());check(H[p.strip()]==h,'claim hash '+p)
for d in sorted({c['DeliverableID'] for c in claims}):
 rr=[r for r in res if r['DeliverableID']==d];check([r['ResidualID'] for r in rr]==[f'{d}-REM-{n:03}' for n in range(1,len(rr)+1)],'residual sequence')
for r in res:
 check(r['Depends']=='NONE' and r['Selectability']=='NON_SELECTABLE_PENDING_OWNER_APPLICATION','residual gate')
 for cid in r['ClaimIDs'].split(';'):check(cid in ci and r['ResidualID'] in ci[cid]['ProposedResidualID'].split(';'),'residual reciprocity')
check(rows(P/'PACKAGE_CLAIMS.csv')==claims,'aggregate claim exact equality');check(rows(P/'PACKAGE_RESIDUALS.csv')==res,'aggregate residual exact equality')
# Independently inventory local contracts and preflight every exact project source and absent SOW.
local=list(Path('projects/pec/execution/PKG-09_Dashboards/1_Working').iterdir()); absent=[];stable=[]
for d in local:
 s=d/'ScopeOfWork.md';check(not s.exists(),'new contract '+str(s));absent.append(str(s))
 for p in d.rglob('*'):
  if p.is_file():
   txt=read(p);stable+=re.findall(r'\b(?:REQ|AC|VER)-[A-Za-z0-9-]+',txt)
check(not stable,'uncovered defined IDs '+str(stable))
targets=sorted({p[len('projects/pec/'):] for p in H if p.startswith('projects/pec/') and '/R1_R4_2026-09-05/' not in p}|{p[len('projects/pec/'):] for p in absent})
for t in targets:
 cmd=['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register','projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv','--target',t,'--operation','candidate-validation'];r=subprocess.run(cmd,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'});check(r.returncode==0,'hold '+t);checks.append({'command':cmd,'cwd':str(Path.cwd()),'environment':{'PYTHONDONTWRITEBYTECODE':'1'},'exit_code':r.returncode,'result':r.stdout.strip()})
writej('PREFLIGHT.json',checks)
writej('MAPPING_CHECKS.json',maps)
writej('MECHANICAL_VALIDATION.json',{'status':'PASS' if not errors else 'FAIL','errors':errors,'claims':len(claims),'residuals':len(res),'unique_sources_rehashed':len(H),'mapping_quotes':len(maps),'exact_hold_targets':len(targets),'missing_contracts':absent,'defined_local_requirement_ids':stable})
writej('READ_MANIFEST.json',{'source_commit':BASE,'hashes':H,'historical_sources':[],'checks':checks,'source_unchanged':not errors,'read_scope_note':'Full frozen manifests independently rehashed; semantic inspection limited to scoped sources and exact checks in CHECKED_CLAIMS, not every byte in common corpus.'})
print(json.dumps({'errors':errors,'hashes':len(H),'maps':len(maps),'targets':len(targets)}))
