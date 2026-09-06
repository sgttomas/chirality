from pathlib import Path
import json,csv,re,hashlib,subprocess,collections
ROOT=Path.cwd();P=Path('projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05/PACKAGES/PKG-03');V=P/'VERIFICATION';base='2be412ccea62bdc4bd96deb082c46d7a792076ea'
claims_header='ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'.split(',')
res_header='ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'.split(',')
errors=[]; hashes={};historical=[];checks=[];stats={};allclaims=[];allres=[];coverage={}
def h(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def verifyhash(path,sha,context):
 pp=Path(path)
 if pp.is_absolute() or '..' in pp.parts:errors.append([context,'unsafe path',path]);return
 if not pp.is_file():errors.append([context,'missing path',path]);return
 digest=h(pp);hashes[str(pp)]=digest
 if digest!=sha:errors.append([context,'hash mismatch',path])
for act in json.loads((P/'SOURCE_MANIFEST.json').read_text())['checks']:
 r=subprocess.run(act['command'],text=True,capture_output=True);checks.append(dict(command=act['command'],cwd=str(ROOT),environment={'PYTHONDONTWRITEBYTECODE':'1'},exit_code=r.returncode,result=r.stdout));
 if r.returncode:errors.append(['hold',r.stdout,r.stderr])
for d,wstr in json.loads((P/'SELECTED_WORKERS.json').read_text())['selected'].items():
 w=Path(wstr);cr=list(csv.DictReader((w/'CLAIMS.csv').open()));rr=list(csv.DictReader((w/'RESIDUALS.csv').open()));allclaims+=cr;allres+=rr
 for name,header in [('CLAIMS.csv',claims_header),('RESIDUALS.csv',res_header)]:
  raw=(w/name).read_bytes();
  if b'\r' in raw:errors.append([d,name,'CR'])
  if raw.decode().splitlines()[0].split(',')!=header:errors.append([d,name,'schema'])
 cs={r['ClaimID']:r for r in cr};rs={r['ResidualID']:r for r in rr}
 if len(cs)!=len(cr) or len(rs)!=len(rr):errors.append([d,'duplicate IDs'])
 if list(rs)!=[d+'-REM-'+str(i).zfill(3) for i in range(1,len(rr)+1)]:errors.append([d,'residual sequence'])
 for r in cr+rr:
  if r['DeliverableID']!=d:errors.append([d,'owner mismatch'])
  if not r['Depends'] or not any(x in r['ExactGate'] for x in ['(gated:','(stage-gated:','NOT_SELECTABLE_UNTIL:']):errors.append([d,'Depends/gate',r.get('ClaimID',r.get('ResidualID'))])
  if r['Selectability']!='NON_SELECTABLE_PENDING_OWNER_APPLICATION':errors.append([d,'selectable',r.get('ClaimID',r.get('ResidualID'))])
 for r in cr:
  cid=r['ClaimID']
  if not cid.startswith(d+'::'):errors.append([d,'claim prefix',cid])
  if r['SourceCommit']!=base:errors.append([d,'commit',cid])
  sh=r['SourceHashes']
  hm=json.loads(sh) if sh.startswith('{') else dict(x.strip().rsplit('=',1) for x in sh.split(';') if x.strip())
  for path,sha in hm.items():verifyhash(path,sha,cid)
  links=re.findall(r'DEL-\d\d-\d\d-REM-\d{3}',r['ProposedResidualID'])
  for rid in links:
   if rid not in rs or cid not in rs[rid]['ClaimIDs'].split(';'):errors.append([cid,'broken residual backlink',rid])
 for r in rr:
  for cid in r['ClaimIDs'].split(';'):
   if cid not in cs or r['ResidualID'] not in cs[cid]['ProposedResidualID']:errors.append([r['ResidualID'],'broken claim backlink',cid])
 m=json.loads((w/'READ_MANIFEST.json').read_text())
 if set(m)!=set(['source_commit','hashes','historical_sources','checks','source_unchanged']):errors.append([d,'read manifest schema'])
 if m['source_commit']!=base or not m['source_unchanged']:errors.append([d,'manifest basis'])
 for path,sha in m['hashes'].items():verifyhash(path,sha,d+' manifest')
 historical+=m['historical_sources']
 for f in w.glob('*'):
  if f.is_file():hashes[str(f)]=h(f)
 sow=list(Path('projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working').glob(d+'*/ScopeOfWork.md'))
 definitions=set(re.findall(r'^- \*\*([A-Z]+-\d{3})\*\*',sow[0].read_text(),re.M)) if sow else set()
 locals={x.split('::',1)[1] for x in cs};missing=definitions-locals
 if missing:errors.append([d,'uncovered definitions',sorted(missing)])
 coverage[d]={'defined':len(definitions),'covered':len(definitions & locals),'extra':sorted(locals-definitions)}
 stats[d]={'claims':len(cr),'residuals':len(rr),'dispositions':dict(collections.Counter(r['Disposition'] for r in cr))}
 if (w/'OUTPUT_MANIFEST.json').exists():
  om=json.loads((w/'OUTPUT_MANIFEST.json').read_text());om=om.get('files',om)
  for path,sha in om.items():
   if isinstance(sha,str) and re.fullmatch('[a-f0-9]{64}',sha):verifyhash(str(w/path),sha,d+' output')
for item in json.loads((P/'WORKERS/DEL-03-05/FALLBACK_MAP.json').read_text()):
 q=item['quote'];path=item['path']
 if hashlib.sha256(q.encode()).hexdigest()!=item['quote_sha256'] or q not in Path(path).read_text():errors.append(['fallback quote',item['ClaimID']])
# Frozen originals are separate manager evidence; inspect exact formats before seal validation.
(V/'STRUCTURAL_CHECK.json').write_text(json.dumps(dict(verdict='FAIL' if errors else 'PASS',errors=errors,stats=stats,coverage=coverage,source_hashes_checked=len(hashes),claims=len(allclaims),residuals=len(allres)),indent=2)+'\n')
(V/'READ_MANIFEST.json').write_text(json.dumps(dict(source_commit=base,hashes=hashes,historical_sources=historical,checks=checks,source_unchanged=not any('hash mismatch' in e for e in errors)),indent=2)+'\n')
print(json.dumps(dict(errors=errors,stats=stats,coverage=coverage,hashes=len(hashes)),indent=2))
