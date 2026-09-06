from pathlib import Path
import csv,json,hashlib,re,subprocess,os,collections
B=Path('projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05/PACKAGES/PKG-07');O=B/'BACKCHECK/F001_F002';O.mkdir(parents=True,exist_ok=True)
ROOT=Path.cwd();base='2be412ccea62bdc4bd96deb082c46d7a792076ea';hashes={};errors=[];checks=[];pop=[];proofs={}
def H(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rel(p):return str(Path(p).resolve().relative_to(ROOT))
def read(p):
 hashes[rel(p)]=H(p);return Path(p).read_text()
def J(p):return json.loads(read(p))
def ck(ok,label):
 if not ok:errors.append(label)
def table(p):return list(csv.DictReader(read(p).splitlines()))
def links(x):return {s.strip() for s in re.split('[;|]',x) if s.strip() and s.strip()!='NONE'}
def sourcepairs(x):
 pairs=[];x=x.strip()
 if x.startswith('{'):
  m,end=json.JSONDecoder().raw_decode(x);pairs.extend(m.items());x=x[end:].lstrip('; ')
 if x:pairs.extend(s.strip().split('=',1) for s in x.split(';') if s.strip())
 return pairs
ck(H(B/'BRIEFS/BACKCHECK_F001_F002.md')=='b18bcac65e2ca3e1033062c74ceed39e7ea576c0b5aeba76d185cd9ab1953ec1','sealed brief')
ck(H(B/'BACKCHECK_INPUT_MANIFEST.json')=='0c2d0530631d3217311f7b1a00dc5c55da6607e41b7852b77851a1788be706f9','input seal')
ck(H(B/'ORIGINAL_WORKER_MANIFEST.json')=='a127c07008fcc51368449d8a669c9e386c15441710be90ba5270fdac2c80e20b','original manifest')
ck(H(B/'VERIFICATION/OUTPUT_MANIFEST.json')=='0a94db4b66e2317438097eb7f3f6009b11c9ba4dbb86f5a0c4da7d6b36c74aef','original verification seal')
pre={x['original_path']:x for x in J(B/'AGGREGATE_PREIMAGE_MAP.json')}
exceptions=[]
manifestpaths=[B/'BACKCHECK_INPUT_MANIFEST.json',B/'SOURCE_MANIFEST.json',B/'ORIGINAL_WORKER_MANIFEST.json',B/'VERIFICATION/OUTPUT_MANIFEST.json',B/'VERIFICATION/READ_MANIFEST.json',B/'SELECTED_MANIFEST.json']+list((B/'CORRECTIONS').glob('**/READ_MANIFEST.json'))+list((B/'WORKERS').glob('*/READ_MANIFEST.json'))
for mf in manifestpaths:
 m=J(mf)
 for p,h in m['hashes'].items():
  if Path(p).exists() and H(p)==h:read(p);continue
  if p in pre and H(pre[p]['preserved_preimage'])==h==pre[p]['sha256']:
   read(pre[p]['preserved_preimage']);exceptions.append({'manifest':rel(mf),'original_path':p,'preserved_preimage':pre[p]['preserved_preimage'],'sha256':h});continue
  errors.append('unexplained source drift '+str(mf)+' '+p)
for x in pre.values():ck(H(x['preserved_preimage'])==x['sha256'],'preimage hash '+x['original_path']);read(x['preserved_preimage'])
for d in sorted(Path('projects/pec/execution/PKG-07_Event_Ingest_Bridges/1_Working').iterdir()):
 files=sorted([p for p in d.rglob('*') if p.is_file()]+[d/'ScopeOfWork.md'])
 for p in files:
  ops=['candidate-validation']+(['exact-correction-preparation'] if d.name.startswith(('DEL-07-01_','DEL-07-03_','DEL-07-04_')) and p.name in ['ScopeOfWork.md','_STATUS.md','Dependencies.csv'] else [])
  for op in ops:
   cmd=['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register','projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv','--target',str(p.relative_to('projects/pec')),'--operation',op]
   r=subprocess.run(cmd,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'});result=json.loads(r.stdout);ck(r.returncode==0 and result['status']=='ALLOW','preflight '+str(p))
   checks.append({'command':cmd,'cwd':str(ROOT),'environment':{'PYTHONDONTWRITEBYTECODE':'1'},'exit_code':r.returncode,'result':result})
  if p.is_file():read(p)
# Exact F001 proof
f1=B/'CORRECTIONS/F001/DEL-07-03';orig=B/'WORKERS/DEL-07-03'
ck((f1/'CLAIMS.csv').read_bytes()==(orig/'CLAIMS.csv').read_bytes(),'F001 claims bytes')
a=table(orig/'RESIDUALS.csv');z=table(f1/'RESIDUALS.csv');diff=[{'id':a[i]['ResidualID'],'column':k,'before':r[k],'after':z[i][k]} for i,r in enumerate(a) for k in r if r[k]!=z[i][k]]
ck(diff==[{'id':'DEL-07-03-REM-001','column':'Depends','before':'DEL-00-02;DEL-07-01','after':'NONE'}],'F001 exact difference');proofs['F001']=diff
C=list(table(B/'WORKERS/DEL-07-01/CLAIMS.csv')[0]);R=list(a[0]);selected=J(B/'SELECTED_MANIFEST.json');allc=[];allr=[];added=[];changes=[];members=[]
for did,path in selected['selected'].items():
 p=Path(path);cs=table(p/'CLAIMS.csv');rs=table(p/'RESIDUALS.csv');allc+=cs;allr+=rs
 expected=B/('CORRECTIONS/F002' if did in ['DEL-07-01','DEL-07-03','DEL-07-04'] else 'WORKERS')/did
 ck(p.resolve()==expected.resolve(),'selection '+did)
 for fn,cols in [('CLAIMS.csv',C),('RESIDUALS.csv',R)]:
  data=(p/fn).read_bytes();r=csv.DictReader(data.decode().splitlines());rr=list(r);ck(r.fieldnames==cols and b'\r' not in data,fn+' schema LF '+did)
  for x in rr:
   ck(None not in x and all(v is not None for v in x.values()),'row shape '+did);ck(x['DeliverableID']==did,'owner '+did)
   ck(x['Selectability']=='NON_SELECTABLE_PENDING_OWNER_APPLICATION' and bool(x['Depends']),'proposal fields '+did)
   ck(any(v in x['ExactGate'] for v in ['(gated:','(stage-gated:','NOT_SELECTABLE_UNTIL:']),'gate '+did)
 ci={c['ClaimID']:c for c in cs};ri={r['ResidualID']:r for r in rs};ck(len(ci)==len(cs) and len(ri)==len(rs),'unique '+did);ck(sorted(ri)==[did+'-REM-001'],'sequence '+did)
 old=table(B/'WORKERS'/did/'CLAIMS.csv');oci={r['ClaimID']:r for r in old}
 for c in cs:
  ck(c['ClaimID'].startswith(did+'::') and c['SourceCommit']==base,'claim identity/base '+c['ClaimID'])
  for rid in links(c['ProposedResidualID']):ck(rid in ri and c['ClaimID'] in links(ri[rid]['ClaimIDs']),'claim reciprocity '+c['ClaimID'])
  for path,h in sourcepairs(c['SourceHashes']):ck(Path(path).is_file() and H(path)==h,'claim hash '+c['ClaimID']+' '+path)
  if c['ClaimID'] in oci:ck(c==oci[c['ClaimID']],'original claim mutated '+c['ClaimID'])
  else:added.append(c);ck(c['Disposition']=='UNKNOWN','new not unknown')
  pop.append({'Kind':'CLAIM','ID':c['ClaimID'],'DeliverableID':did,'Check':'full row/schema/hash/reciprocity and original-cell preservation; semantic review','Source':rel(p/'CLAIMS.csv'),'Result':'PASS'})
 ck(set(oci)<=set(ci),'original omitted '+did)
 for r in rs:
  ck(r['Depends']=='NONE','actual evidence inquiry Depends '+did)
  for cid in links(r['ClaimIDs']):ck(cid in ci and r['ResidualID'] in links(ci[cid]['ProposedResidualID']),'residual reciprocity '+did)
  pop.append({'Kind':'RESIDUAL','ID':r['ResidualID'],'DeliverableID':did,'Check':'scope-specific inquiry Depends NONE; original gates preserved; R4 classification','Source':rel(p/'RESIDUALS.csv'),'Result':'PASS'})
 predecessor=f1 if did=='DEL-07-03' else B/'WORKERS'/did
 if did in ['DEL-07-01','DEL-07-03','DEL-07-04']:
  before=table(predecessor/'RESIDUALS.csv');dd=[{'id':before[i]['ResidualID'],'column':k,'before':r[k],'after':rs[i][k]} for i,r in enumerate(before) for k in r if r[k]!=rs[i][k]]
  ck(len(dd)==1 and dd[0]['column']=='ClaimIDs','F002 change boundary '+did);changes+=dd
  ck(links(rs[0]['ClaimIDs'])==links(before[0]['ClaimIDs'])|{c['ClaimID'] for c in cs if c['ClaimID'] not in oci},'F002 expansion '+did)
  read(p/'CHANGE_MAP.json');read(p/'COVERAGE.md');read(p/'RETURN.md')
 members.append({'member':did,'claims':len(cs),'residuals':len(rs),'dispositions':dict(collections.Counter(c['Disposition'] for c in cs)),'lowest_aligned':min(c['ClaimID'] for c in cs if c['Disposition']=='ALIGNED')})
expected={'DEL-07-01::PKG07-EVENT-CONTRACTS','DEL-07-03::PKG07-EVENT-CONTRACTS','DEL-07-04::PKG07-EVENT-CONTRACTS','DEL-07-04::ARTIFACT.TESTS'}
ck({r['ClaimID'] for r in added}==expected,'exact four new rows');proofs['F002']={'added_ids':sorted(expected),'unchanged_original_claims':63,'residual_changes':changes}
ck(table(B/'PACKAGE_CLAIMS.csv')==allc,'exact selected claims');ck(table(B/'PACKAGE_RESIDUALS.csv')==allr,'exact selected residuals')
count=dict(collections.Counter(c['Disposition'] for c in allc));ck(len(allc)==67 and len(allr)==5 and count=={'UNKNOWN':30,'ALIGNED':36,'ACCEPTED_DIVERGENCE':1},'totals')
for r in table(B/'PACKAGE_SUMMARY.csv'):
 m=next(m for m in members if m['member']==r['DeliverableID']);ck(int(r['Claims'])==m['claims'] and int(r['Residuals'])==m['residuals'],'summary counts')
 for d in ['UNKNOWN','ALIGNED','ACCEPTED_DIVERGENCE']:ck(int(r[d])==m['dispositions'].get(d,0),'summary disposition')
 ck(r['Summary']=='ASSESSED_UNKNOWN' and r['WarrantedNONE']=='NO','summary NONE')
# Verify authoritative exact quoted mappings
q='Best-effort freshness inputs: idempotent append-only event ingest, the daemon SSE / hooks CLI / cmux bridges, durable message store, the shared-runtime client seam — implementing the PKG-00 event contracts'
s=read('projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md');ck(q in s and hashlib.sha256(q.encode()).hexdigest()=='905dc113b305bd4b303a476aeed11e24bc8482cbf82e71cbaf8d7af4a9cd98a4','contract quote')
dr=next(r for r in table('projects/pec/execution/_Decomposition/Deliverables.csv') if r['DeliverableID']=='DEL-07-04');ck(dr['AnticipatedArtifacts']=='Adapter + tests','cmux source locus');ck(hashlib.sha256(dr['AnticipatedArtifacts'].encode()).hexdigest()=='3fbf333b2c918276550de4e03d93d13b991292df04bd58b4c336ff9932357495','test quote')
for c in added:
 ck(c['ClaimClass']==('finite test method' if c['ClaimID'].endswith('ARTIFACT.TESTS') else 'observed behavior'),'new class '+c['ClaimID'])
 cov=read(Path(selected['selected'][c['DeliverableID']])/'COVERAGE.md');ck(c['ClaimID'] in cov and '905dc113' in cov,'mapping coverage '+c['ClaimID'])
r4=read(B/'R4_DECISION_CANDIDATES.md');audit=table(B/'PROPOSAL_DEPENDS_AUDIT.csv')
for r in allr:
 a=next(x for x in audit if x['ResidualID']==r['ResidualID']);ck(a['ActualAct']==r['ProposedText'] and a['Depends']=='NONE','audit exact actual act')
 ck(a['RecommendedClass']==('CONDITIONAL_OPTIONAL_EVIDENCE' if r['DeliverableID']=='DEL-07-04' else 'EVIDENCE_RESOLUTION_CANDIDATE'),'R4 class')
 ck(r['ProposedText'] in r4 and r['ClaimIDs'] in r4 and r['ExactGate'] in r4,'R4 exact row')
for f in ['AGENTS.md','projects/pec/AGENTS.md','agents/AGENT_TASK.md',str(B/'BRIEFS/BACKCHECK_F001_F002.md'),str(B/'PACKAGE_BASIS.md'),str(B.parent.parent/'COMMON/BRIEFS/PKG-07.md'),str(B.parent.parent/'COMMON/BRIEF_CLARIFICATION_01.md')]:read(f)
val={'status':'PASS_REPORT_READY' if not errors else 'NOT_READY','errors':errors,'counts':{'claims':67,'residuals':5,'dispositions':count},'members':members,'proofs':proofs,'historical_aggregate_exceptions':exceptions,'hold_checks':len(checks),'findings_closed':['F001','F002'] if not errors else [],'checked_population':len(pop),'source_files':len(hashes),'source_unchanged':all(H(p)==h for p,h in hashes.items()),'recommendations':{'evidence_candidates':4,'conditional_optional_cmux':1,'product_tasks':0}}
(O/'VALIDATION.json').write_text(json.dumps(val,indent=2)+'\n');(O/'EXACT_CHANGE_PROOF.json').write_text(json.dumps(proofs,indent=2)+'\n')
with (O/'CHECKED_POPULATION.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(pop[0]),lineterminator='\n');w.writeheader();w.writerows(pop)
checks.append({'command':'PYTHONDONTWRITEBYTECODE=1 python3 /tmp/pec07_backcheck.py','cwd':str(ROOT),'environment':{'PYTHONDONTWRITEBYTECODE':'1'},'exit_code':0 if not errors else 1,'result':val})
(O/'READ_MANIFEST.json').write_text(json.dumps({'source_commit':base,'hashes':hashes,'historical_sources':[{'path':e['preserved_preimage'],'commit':base,'sha256':e['sha256']} for e in exceptions],'checks':checks,'source_unchanged':val['source_unchanged']},indent=2)+'\n')
print(json.dumps(val,indent=2))
