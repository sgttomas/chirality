import csv,json,pathlib,re,hashlib,collections,sys
root=pathlib.Path.cwd(); pkg=root/'projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05/PACKAGES/PKG-04'
CF='ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'.split(',')
RF='ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'.split(',')
errors=[]; members=[]
for n in range(1,6):
 d=f'DEL-04-{n:02}'; w=pkg/'WORKERS'/d
 if '--selected' in sys.argv and n in [3,5]: w=pkg/'CORRECTIONS'/d/'C01'
 if not (w/'RETURN.md').exists(): print(d,'pending'); continue
 c=list(csv.DictReader((w/'CLAIMS.csv').open())); rr=list(csv.DictReader((w/'RESIDUALS.csv').open()))
 for file,fields in [('CLAIMS.csv',CF),('RESIDUALS.csv',RF)]:
  f=w/file
  if next(csv.reader(f.open()))!=fields:errors.append(d+' schema '+file)
  if b'\r' in f.read_bytes():errors.append(d+' CR '+file)
 for rows,key in [(c,'ClaimID'),(rr,'ResidualID')]:
  ids=[x[key] for x in rows]
  if len(set(ids))!=len(ids):errors.append(d+' duplicate '+key)
 for x in c+rr:
  if not x['Depends']:errors.append(d+' empty Depends')
  if not any(t in x['ExactGate'] for t in ['(gated:','(stage-gated:','NOT_SELECTABLE_UNTIL:']):errors.append(d+' gate marker '+str(x.get('ClaimID',x.get('ResidualID'))))
  if x['Selectability']!='NON_SELECTABLE_PENDING_OWNER_APPLICATION':errors.append(d+' selectability')
 for i,x in enumerate(rr,1):
  if x['ResidualID']!=f'{d}-REM-{i:03}':errors.append(d+' residual numbering '+x['ResidualID'])
  linked=[v for v in re.split('[;|]',x['ClaimIDs']) if v]
  for v in linked:
   found=[q for q in c if q['ClaimID']==v]
   if len(found)!=1 or x['ResidualID'] not in found[0]['ProposedResidualID']:errors.append(d+' reciprocal residual '+v)
 for x in c:
  if x['SourceCommit']!='2be412ccea62bdc4bd96deb082c46d7a792076ea':errors.append(d+' commit '+x['ClaimID'])
  for v in re.split('[;|]',x['ProposedResidualID']):
   if v and v!='NONE' and not any(q['ResidualID']==v and x['ClaimID'] in q['ClaimIDs'] for q in rr):errors.append(d+' reciprocal claim '+x['ClaimID'])
 m=json.loads((w/'READ_MANIFEST.json').read_text())
 for p,h in m['hashes'].items():
  path=root/p
  if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest()!=h:errors.append(d+' source hash '+p)
 sows=list((root/'projects/pec/execution/PKG-04_Orientation_Services/1_Working').glob(d+'*/ScopeOfWork.md'))
 if sows:
  local=set(re.findall(r'^- \*\*([A-Z]+-[0-9]+)\*\*',sows[0].read_text(),re.M)); covered={x['ClaimID'].split('::',1)[1] for x in c}; missing=local-covered
  if missing:errors.append(d+' missing local IDs '+','.join(sorted(missing)))
 members.append({'DeliverableID':d,'ClaimCount':len(c),'ResidualCount':len(rr),'UnknownCount':sum(x['Disposition']=='UNKNOWN' for x in c),'dispositions':dict(collections.Counter(x['Disposition'] for x in c))})
print(json.dumps({'members':members,'errors':errors},indent=2))
