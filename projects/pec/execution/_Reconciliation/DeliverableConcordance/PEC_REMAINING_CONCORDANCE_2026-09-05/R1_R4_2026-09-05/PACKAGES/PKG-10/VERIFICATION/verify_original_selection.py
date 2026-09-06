from pathlib import Path
import json,csv,hashlib,re,subprocess,collections,io
root=Path.cwd();p=root/'projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05/PACKAGES/PKG-10';v=p/'VERIFICATION';base='2be412ccea62bdc4bd96deb082c46d7a792076ea';reads={};errs=[];checks={}
def read(f):
 f=Path(f);f=f if f.is_absolute() else root/f;b=f.read_bytes();reads[str(f.relative_to(root))]=hashlib.sha256(b).hexdigest();return b.decode()
def rows(f):return list(csv.DictReader(io.StringIO(read(f))))
def j(f):return json.loads(read(f))
def check(ok,s):
 if not ok:errs.append(s)
sel=j(p/'SELECTED_DERIVATIVES.json');cs=rows(p/'PACKAGE_CLAIMS.csv');rs=rows(p/'PACKAGE_RESIDUALS.csv');ss=rows(p/'PACKAGE_SUMMARY.csv')
cf='ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'.split(',');rf='ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'.split(',')
check(list(cs[0])==cf,'claim schema');check(list(rs[0])==rf,'residual schema');check(len({r['ClaimID'] for r in cs})==len(cs),'claim duplicate');check(len({r['ResidualID'] for r in rs})==len(rs),'residual duplicate')
allc=[];allr=[];sourcepins={};required=[];allids=[];changes=0
for d,path in sel.items():
 w=Path(path);a=rows(w/'CLAIMS.csv');b=rows(w/'RESIDUALS.csv');allc+=a;allr+=b
 for f in ['COVERAGE.md','RETURN.md']:read(w/f)
 m=j(w/'READ_MANIFEST.json');sourcepins.update(m['hashes'])
 for f in ['CLAIMS.csv','RESIDUALS.csv']:check('\r' not in read(w/f),d+' LF')
 check([r['ResidualID'] for r in b]==[f'{d}-REM-{i:03}' for i in range(1,len(b)+1)],d+' sequence')
 if w.name=='REVISION_M001':
  mp=j(w/'CHANGE_MAP.json')
  for f,h in mp['original_hashes'].items():check(hashlib.sha256(read(f).encode()).hexdigest()==h,'preserved '+f)
  actual=[]
  for name in ['CLAIMS.csv','RESIDUALS.csv']:
   bef=rows(w.parent/name);aft=rows(w/name);check(len(bef)==len(aft),'correction count')
   for i,(x,y) in enumerate(zip(bef,aft),1):
    for k in x:
     if x[k]!=y[k]:
      actual.append((name,i,k,x[k],y[k]));check(k in ['ResidualID','ProposedResidualID','ClaimIDs','Depends','ExactGate'],'correction illegal column '+k)
      if k=='Depends':check(x[k]=='' and y[k]=='NONE','Depends semantic change')
      elif k=='ExactGate':check(y[k]=='NOT_SELECTABLE_UNTIL: '+x[k],'gate semantic change')
      else:
       want=x[k]
       for old,new in mp['residual_id_map'].items():want=want.replace(old,new)
       check(want==y[k],'ID map semantics')
  mapped=[(z['file'],z['data_row_1based'],z['column'],z['old'],z['new']) for z in mp['changes']]
  check(collections.Counter(actual)==collections.Counter(mapped),'complete cell map '+d);changes+=len(actual)
  sourcepins.update(j(w.parent/'READ_MANIFEST.json')['hashes'])
 for local in (root/'projects/pec/execution/PKG-10_Validation_Measurement/1_Working').glob(d+'*/**/*'):
  if local.is_file():
   tx=read(local)
   if local.name=='ScopeOfWork.md':
    ids=re.findall(r'^\s*- \*\*((?:REQ|AC|VER|CLM|AX|OUT|TBD|CON)-\d{3})\*\*',tx,re.M)
    allids.extend(d+'::'+x for x in ids);required.extend(d+'::'+x for x in ids if x.startswith(('REQ-','AC-','VER-')))
    check(all(d+'::'+x in {z['ClaimID'] for z in a} for x in ids),d+' missing IDs')
check(collections.Counter(json.dumps(x,sort_keys=True) for x in allc)==collections.Counter(json.dumps(x,sort_keys=True) for x in cs),'aggregate claims equality');check(collections.Counter(json.dumps(x,sort_keys=True) for x in allr)==collections.Counter(json.dumps(x,sort_keys=True) for x in rs),'aggregate residual equality')
for c in cs:
 check(c['SourceCommit']==base,'base '+c['ClaimID']);sourcepins.update(json.loads(c['SourceHashes']) if c['SourceHashes'].startswith('{') else dict(x.rsplit('=',1) for x in c['SourceHashes'].split(';') if x))
for x in cs+rs:
 check(bool(x['Depends']),'empty Depends');check(any(t in x['ExactGate'] for t in ['(gated:','(stage-gated:','NOT_SELECTABLE_UNTIL:']),'gate marker');check(x['Selectability']=='NON_SELECTABLE_PENDING_OWNER_APPLICATION','selectability')
for r in rs:
 links=set(re.findall(r'DEL-\d\d-\d\d::[^;,\s]+',r['ClaimIDs']));back={c['ClaimID'] for c in cs if r['ResidualID'] in re.split(r'[;,]\s*',c['ProposedResidualID'])};check(links==back,'reciprocity '+r['ResidualID'])
for s in ss:
 cc=[c for c in cs if c['DeliverableID']==s['DeliverableID']];rr=[r for r in rs if r['DeliverableID']==s['DeliverableID']]
 for key,val in [('Claims',len(cc)),('RawResidualProposals',len(rr)),('UnknownClaims',sum(x['Disposition']=='UNKNOWN' for x in cc)),('StaleClaims',sum(x['Disposition']=='STALE_INPUT' for x in cc)),('NonAlignedClaims',sum(x['Disposition']!='ALIGNED' for x in cc))]:check(int(s[key])==val,'summary '+key)
 check(not any(x['Disposition']=='UNKNOWN' for x in cc) or s['CandidateAssessment']=='ASSESSED_UNKNOWN','unknown summary')
 for key in ['SelectedClaims','SelectedResiduals']:check(hashlib.sha256(read(s[key]).encode()).hexdigest()==s[key+'SHA256'],'selected hash')
basepins=0;uncommitted=[]
for f,h in sourcepins.items():
 try:b=read(f).encode();check(hashlib.sha256(b).hexdigest()==h,'source hash '+f)
 except FileNotFoundError:errs.append('missing source '+f);continue
 q=subprocess.run(['git','show',base+':'+f],capture_output=True)
 if q.returncode==0:check(hashlib.sha256(q.stdout).hexdigest()==h,'base mismatch '+f);basepins+=1
 else:uncommitted.append(f)
# Read exact governance and selected evidence sources; sourcepins include full bounded inventories.
for f in ['AGENTS.md','projects/pec/AGENTS.md','agents/AGENT_RECONCILIATION.md','docs/DELIVERABLE_CONCORDANCE_METHOD.md'] :read(f)
for f in p.parent.parent.joinpath('COMMON').glob('*.md'):read(f)
read(p.parent.parent/'COMMON/SCOPE_CENSUS.csv');read(p.parent.parent/'COMMON/SOURCE_MANIFEST.json');read(p.parent.parent.parent/'CONVENTIONS.md')
for f in p.glob('*.md'):read(f)
for f in p.glob('*MANIFEST*.json'):read(f)
# Every declared evidence path backed by worker source maps is materialized and hashed above.
checks={'claims':len(cs),'residuals':len(rs),'members':len(sel),'defined_local_ids':len(allids),'required_ids':len(required),'required_unique':len(set(required)),'source_hashes':len(sourcepins),'source_equal_base':basepins,'run_derivative_sources':uncommitted,'mechanical_changed_cells':changes,'errors':errs,'dispositions':dict(collections.Counter(c['Disposition'] for c in cs))}
(v/'STRUCTURAL_CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n');(v/'READ_MANIFEST_WORKING.json').write_text(json.dumps({'source_commit':base,'hashes':reads,'historical_sources':[],'checks':[],'source_unchanged':True},indent=2)+'\n');print(json.dumps(checks,indent=2))
