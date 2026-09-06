import pathlib,csv,json,hashlib,sys,re
P=pathlib.Path(__file__).parent
claim='ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'.split(',')
res='ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'.split(',')
inv=json.loads((P/'MANAGER_INVENTORY.json').read_text()); result=[]
for x in inv:
 d=x['DeliverableID'];w=P/'WORKERS'/d
 if len(sys.argv)>1 and d not in sys.argv[1:]:continue
 errors=[]; rows=[];rr=[]
 for file,cols in [('CLAIMS.csv',claim),('RESIDUALS.csv',res)]:
  q=w/file
  if not q.exists():errors.append('missing '+file);continue
  assert b'\r\n' not in q.read_bytes(),str(q)
  rd=csv.DictReader(q.open());v=list(rd)
  if rd.fieldnames!=cols:errors.append('schema '+file)
  if file=='CLAIMS.csv': rows=v
  else:rr=v
 ids=[y['ClaimID'] for y in rows];rids=[y['ResidualID'] for y in rr]
 if len(ids)!=len(set(ids)):errors.append('duplicate claim IDs')
 if len(rids)!=len(set(rids)):errors.append('duplicate residual IDs')
 for z in x['required_definitions']:
  if d+'::'+z['id'] not in ids:errors.append('missing definition '+z['id'])
 for y in rows:
  if y['DeliverableID']!=d:errors.append('wrong deliverable')
  if y['SourceCommit']!='2be412ccea62bdc4bd96deb082c46d7a792076ea':errors.append('wrong commit '+y['ClaimID'])
  for rid in re.split(r'[;,|]\s*',y['ProposedResidualID']):
   if rid and rid not in ('NONE','N/A','none') and rid not in rids:errors.append('missing residual '+rid)
 for y in rr:
  if y['Selectability']!='NON_SELECTABLE_PENDING_OWNER_APPLICATION':errors.append('selectability '+y['ResidualID'])
  for cid in re.split(r'[;,|]\s*',y['ClaimIDs']):
   if cid not in ids:errors.append('missing reciprocal claim '+cid)
   elif y['ResidualID'] not in next(z['ProposedResidualID'] for z in rows if z['ClaimID']==cid):errors.append('nonreciprocal '+cid)
 mp=w/'READ_MANIFEST.json'
 if mp.exists():
  m=json.loads(mp.read_text())
  if not m.get('source_unchanged'):errors.append('source changed')
  for f,h in m.get('hashes',{}).items():
   q=pathlib.Path(f)
   if not q.is_file() or hashlib.sha256(q.read_bytes()).hexdigest()!=h:errors.append('hash mismatch '+f)
 else:errors.append('missing read manifest')
 result.append({'deliverable':d,'claims':len(rows),'residuals':len(rr),'unknowns':sum(y['Disposition']=='UNKNOWN' for y in rows),'errors':errors})
print(json.dumps(result,indent=2));sys.exit(any(x['errors'] for x in result))
