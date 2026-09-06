import csv,json,hashlib,re
from pathlib import Path
P=Path(__file__).resolve().parent
R=next(x for x in P.parents if (x/'AGENTS.md').exists() and (x/'agents').is_dir())
C="ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes".split(',')
S="ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes".split(',')
errors=[]; results=[]
for d in ['DEL-05-01','DEL-05-02']:
 w=P/'WORKERS'/d
 ledgers=[]
 for name,header in [('CLAIMS.csv',C),('RESIDUALS.csv',S)]:
  f=w/name; b=f.read_bytes(); rows=list(csv.DictReader(b.decode().splitlines())); actual=next(csv.reader(b.decode().splitlines()))
  if actual!=header:errors.append(f'{d} {name} schema')
  if b'\r' in b:errors.append(f'{d} {name} CR')
  ledgers.append(rows)
 claims,res=ledgers; ids=[x['ClaimID'] for x in claims]; rid=[x['ResidualID'] for x in res]
 if len(set(ids))!=len(ids): errors.append(f'{d} duplicate claims')
 if rid!=[f'{d}-REM-{i:03d}' for i in range(1,len(rid)+1)]:errors.append(f'{d} residual numbering')
 for row in claims+res:
  if row['DeliverableID']!=d:errors.append(f'{d} owner mismatch')
  if not row['Depends']: errors.append(f'{d} empty Depends')
  if not any(x in row['ExactGate'] for x in ['(gated:','(stage-gated:','NOT_SELECTABLE_UNTIL:']):errors.append(f'{d} gate marker')
  if row['Selectability']!='NON_SELECTABLE_PENDING_OWNER_APPLICATION':errors.append(f'{d} selectability')
 for row in claims:
  if row['SourceCommit']!='2be412ccea62bdc4bd96deb082c46d7a792076ea':errors.append(f'{d} commit')
  links=re.findall(r'DEL-\d{2}-\d{2}-REM-\d{3}',row['ProposedResidualID'])
  for link in links:
   rr=next((r for r in res if r['ResidualID']==link),None)
   if rr is None or row['ClaimID'] not in rr['ClaimIDs']:errors.append(f'{d} backlink {row["ClaimID"]}')
 for row in res:
  linked=[c for c in claims if c['ClaimID'] in row['ClaimIDs'].split(';')]
  if not linked or any(row['ResidualID'] not in c['ProposedResidualID'] for c in linked):errors.append(f'{d} reciprocal {row["ResidualID"]}')
 m=json.loads((w/'READ_MANIFEST.json').read_text())
 if set(m)!=set(['source_commit','hashes','historical_sources','checks','source_unchanged']):errors.append(f'{d} manifest schema')
 for path,h in m['hashes'].items():
  f=R/path
  if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=h:errors.append(f'{d} source hash {path}')
 results.append({'DeliverableID':d,'claims':len(claims),'residuals':len(res),'unknowns':sum(x['Disposition']=='UNKNOWN' for x in claims),'source_hashes':len(m['hashes'])})
print(json.dumps({'pass':not errors,'errors':errors,'members':results},indent=2))
raise SystemExit(bool(errors))
