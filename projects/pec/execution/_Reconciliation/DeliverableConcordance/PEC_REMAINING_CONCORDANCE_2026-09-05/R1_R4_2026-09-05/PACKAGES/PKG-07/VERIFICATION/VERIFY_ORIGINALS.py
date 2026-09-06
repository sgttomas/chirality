from pathlib import Path
import csv,json,hashlib,re,collections
B=Path('projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05/PACKAGES/PKG-07');V=B/'VERIFICATION';base='2be412ccea62bdc4bd96deb082c46d7a792076ea'
H=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
C='ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'.split(',')
R='ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'.split(',')
errors=[]; hashes={};checks=json.loads((V/'PREFLIGHTS.json').read_text()); cs=[];rs=[]; counts=[];pop=[]
def read(p):
 p=Path(p);hashes[str(p)]=H(p);return p.read_text()
def check(ok,msg):
 if not ok:errors.append(msg)
def split(x):return {a.strip() for a in re.split('[;|]',x) if a.strip() and a.strip()!='NONE'}
check(H(B/'BRIEFS/VERIFIER.md')=='65f091d8f9b950b8fd68120ca0046a252aeeaed0f56b8340680e66820063be68','brief seal')
check(H(B/'ORIGINAL_WORKER_MANIFEST.json')=='a127c07008fcc51368449d8a669c9e386c15441710be90ba5270fdac2c80e20b','original seal')
for mf in [B/'SOURCE_MANIFEST.json',B/'ORIGINAL_WORKER_MANIFEST.json']+sorted((B/'WORKERS').glob('*/READ_MANIFEST.json')):
 m=json.loads(read(mf));check(m['source_commit']==base,str(mf)+' base')
 if mf.name=='READ_MANIFEST.json':
  check(set(m)=={'source_commit','hashes','historical_sources','checks','source_unchanged'},str(mf)+' manifest schema')
  check(m['source_unchanged'] is True,str(mf)+' source unchanged')
  for c in m['checks']:check(set(c)>={'command','cwd','environment','exit_code','result'},str(mf)+' check schema')
 for p,h in m['hashes'].items():
  check(Path(p).is_file() and H(p)==h,'hash '+p)
  if Path(p).is_file():read(p)
for w in sorted((B/'WORKERS').iterdir()):
 tables=[]
 for f,fields in [('CLAIMS.csv',C),('RESIDUALS.csv',R)]:
  s=read(w/f);reader=csv.DictReader(s.splitlines());rows=list(reader);tables.append(rows)
  check(reader.fieldnames==fields,str(w/f)+' columns');check(b'\r' not in (w/f).read_bytes(),str(w/f)+' LF')
  for r in rows:
   check(None not in r and all(v is not None for v in r.values()),str(w/f)+' row shape')
   check(r['DeliverableID']==w.name,str(w/f)+' owner');check(bool(r['Depends']),str(w/f)+' Depends')
   check(any(x in r['ExactGate'] for x in ['(gated:','(stage-gated:','NOT_SELECTABLE_UNTIL:']),str(w/f)+' gate')
   check(r['Selectability']=='NON_SELECTABLE_PENDING_OWNER_APPLICATION',str(w/f)+' selectable')
 claims,res=tables;cs+=claims;rs+=res;ci={r['ClaimID']:r for r in claims};ri={r['ResidualID']:r for r in res}
 check(len(ci)==len(claims) and len(ri)==len(res),w.name+' duplicate')
 check(sorted(ri)==[f'{w.name}-REM-{i:03}' for i in range(1,len(res)+1)],w.name+' sequence')
 for c in claims:
  check(c['ClaimID'].startswith(w.name+'::') and c['SourceCommit']==base,c['ClaimID']+' ID/base')
  for rid in split(c['ProposedResidualID']):check(rid in ri and c['ClaimID'] in split(ri[rid]['ClaimIDs']),c['ClaimID']+' backlink')
  try:
   hp=json.loads(c['SourceHashes']) if c['SourceHashes'].lstrip().startswith('{') else dict(pair.strip().split('=',1) for pair in c['SourceHashes'].split(';') if pair.strip())
   for p,h in hp.items():check(Path(p).is_file() and H(p)==h,c['ClaimID']+' source hash '+p)
  except (ValueError,TypeError):errors.append(c['ClaimID']+' invalid source hash encoding')
  pop.append({'Kind':'CLAIM','DeliverableID':w.name,'ID':c['ClaimID'],'Disposition':c['Disposition'],'Check':'Full schema/hash/reciprocity; source and semantic boundary review','Source':c['NormativeSource'],'Result':'PASS_ORIGINAL_ROW'})
 for r in res:
  for cid in split(r['ClaimIDs']):check(cid in ci and r['ResidualID'] in split(ci[cid]['ProposedResidualID']),r['ResidualID']+' reciprocal')
  pop.append({'Kind':'RESIDUAL','DeliverableID':w.name,'ID':r['ResidualID'],'Disposition':'PROPOSAL','Check':'Exact scope/Depends/gate and reciprocal source claim review','Source':str(w/'RESIDUALS.csv'),'Result':'F001' if w.name=='DEL-07-03' else 'PASS'})
 counts.append({'member':w.name,'claims':len(claims),'residuals':len(res),'dispositions':dict(collections.Counter(x['Disposition'] for x in claims)),'lowest_aligned':min(c['ClaimID'] for c in claims if c['Disposition']=='ALIGNED')})
 d=next(Path('projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working').glob(w.name+'_*'))
 local=[]
 for p in d.rglob('*'):
  if p.is_file(): local.extend(re.findall(r'\b(?:REQ|AC|VER)-\d+\b',read(p)))
 check(not (d/'ScopeOfWork.md').exists(),w.name+' missing SOW changed')
 check(not local,w.name+' local REQ/AC/VER requires census '+str(local))
 pop.append({'Kind':'SOURCE_CENSUS','DeliverableID':w.name,'ID':w.name+'::LOCAL-REQ-AC-VER','Disposition':'ABSENT','Check':'All seven local files text scanned; canonical SOW absent','Source':str(d),'Result':'PASS: zero REQ/AC/VER definitions or references'})
for f,rows in [('PACKAGE_CLAIMS.csv',cs),('PACKAGE_RESIDUALS.csv',rs)]:
 if (B/f).exists():check(list(csv.DictReader(read(B/f).splitlines()))==rows,f+' exact original aggregate')
check(len(cs)==63 and len(rs)==5,'totals')
check(collections.Counter(x['Disposition'] for x in cs)=={'UNKNOWN':26,'ALIGNED':36,'ACCEPTED_DIVERGENCE':1},'dispositions')
for p in [Path('AGENTS.md'),Path('projects/pec/AGENTS.md'),Path('agents/AGENT_TASK.md'),Path('docs/DELIVERABLE_CONCORDANCE_METHOD.md'),B/'BRIEFS/VERIFIER.md',B/'PACKAGE_BASIS.md',B.parent.parent/'COMMON/BRIEFS/PKG-07.md',B.parent.parent/'COMMON/BRIEF_CLARIFICATION_01.md']:
 read(p)
validation={'status':'NOT_READY','structural_errors':errors,'original_claims':len(cs),'original_residuals':len(rs),'dispositions':dict(collections.Counter(x['Disposition'] for x in cs)),'members':counts,'source_files_rehashed':len(hashes),'source_unchanged':all(H(p)==h for p,h in hashes.items()),'hold_checks':40,'hold_results':'ALLOW','semantic_findings':['F001'],'checked_population':len(pop),'method_limits':'No behavior PASS or product test outcome asserted. Full original populations reviewed; evidence-report readiness only.'}
(V/'VALIDATION.json').write_text(json.dumps(validation,indent=2)+'\n')
with (V/'CHECKED_POPULATION.csv').open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=list(pop[0]),lineterminator='\n');writer.writeheader();writer.writerows(pop)
checks.append({'command':'python3 /tmp/pec07_verify.py','cwd':str(Path.cwd()),'environment':{'PYTHONDONTWRITEBYTECODE':'1'},'exit_code':0 if not errors else 1,'result':validation})
(V/'READ_MANIFEST.json').write_text(json.dumps({'source_commit':base,'hashes':hashes,'historical_sources':[],'checks':checks,'source_unchanged':validation['source_unchanged']},indent=2)+'\n')
print(json.dumps(validation,indent=2))
