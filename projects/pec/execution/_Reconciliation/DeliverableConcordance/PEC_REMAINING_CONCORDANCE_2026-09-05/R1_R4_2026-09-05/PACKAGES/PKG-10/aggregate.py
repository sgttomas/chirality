import pathlib,csv,json,hashlib,re,collections
P=pathlib.Path(__file__).parent
inv=json.loads((P/'MANAGER_INVENTORY.json').read_text())
claims=[];res=[];summary=[];errors=[];sources={};selection={}
def sha(q):return hashlib.sha256(q.read_bytes()).hexdigest()
def read(q):
 with q.open() as f:return list(csv.DictReader(f))
def write(q,rs,fields=None):
 with q.open('w') as f:
  w=csv.DictWriter(f,fieldnames=fields or list(rs[0]),lineterminator='\n');w.writeheader();w.writerows(rs)
for x in inv:
 d=x['DeliverableID'];w=P/'WORKERS'/d
 if (w/'REVISION_M001/CLAIMS.csv').exists():w=w/'REVISION_M001'
 selection[d]=str(w);cr=read(w/'CLAIMS.csv');rr=read(w/'RESIDUALS.csv');claims+=cr;res+=rr
 ids={a['ClaimID'] for a in cr};rids={a['ResidualID'] for a in rr}
 for z in x['required_definitions']:
  if d+'::'+z['id'] not in ids:errors.append(d+' missing '+z['id'])
 if rids!={d+f'-REM-{n:03}' for n in range(1,len(rr)+1)}:errors.append(d+' bad residual sequence')
 for y in cr+rr:
  if not y['Depends']:errors.append(d+' empty Depends')
  if not any(t in y['ExactGate'] for t in ['NOT_SELECTABLE_UNTIL:','(gated:','(stage-gated:']):errors.append(d+' gate marker missing')
 for y in rr:
  if y['Selectability']!='NON_SELECTABLE_PENDING_OWNER_APPLICATION':errors.append('selectability '+y['ResidualID'])
  for cid in re.split(r'[;,|]\s*',y['ClaimIDs']):
   if cid not in ids:errors.append('bad claim ref '+cid)
   elif y['ResidualID'] not in next(a['ProposedResidualID'] for a in cr if a['ClaimID']==cid):errors.append('nonreciprocal '+cid)
 for y in cr:
  if y['SourceCommit']!='2be412ccea62bdc4bd96deb082c46d7a792076ea':errors.append('wrong source commit')
  for rid in re.split(r'[;,|]\s*',y['ProposedResidualID']):
   if rid and rid not in ['NONE','N/A'] and rid not in rids:errors.append('bad residual ref '+rid)
 m=json.loads((w/'READ_MANIFEST.json').read_text())
 if not m['source_unchanged']:errors.append(d+' source changed')
 for s,h in m['hashes'].items():
  if not pathlib.Path(s).is_file() or sha(pathlib.Path(s))!=h:errors.append('hash mismatch '+s)
  if s in sources and sources[s]!=h:errors.append('cross-worker hash mismatch '+s)
  sources[s]=h
 unknown=sum(a['Disposition']=='UNKNOWN' for a in cr);stale=sum(a['Disposition']=='STALE_INPUT' for a in cr)
 summary.append({'DeliverableID':d,'Claims':len(cr),'RawResidualProposals':len(rr),'UnknownClaims':unknown,'StaleClaims':stale,'NonAlignedClaims':sum(a['Disposition']!='ALIGNED' for a in cr),'CandidateAssessment':'ASSESSED_UNKNOWN' if unknown else ('ASSESSED_WITH_RESIDUALS' if rr or stale else 'NONE'),'SelectedClaims':str(w/'CLAIMS.csv'),'SelectedClaimsSHA256':sha(w/'CLAIMS.csv'),'SelectedResiduals':str(w/'RESIDUALS.csv'),'SelectedResidualsSHA256':sha(w/'RESIDUALS.csv')})
if len({a['ClaimID'] for a in claims})!=len(claims):errors.append('duplicate aggregate claims')
if len({a['ResidualID'] for a in res})!=len(res):errors.append('duplicate aggregate residuals')
for name,rs in [('PACKAGE_CLAIMS.csv',claims),('PACKAGE_RESIDUALS.csv',res),('PACKAGE_SUMMARY.csv',summary)]:write(P/name,rs)
(P/'SELECTED_DERIVATIVES.json').write_text(json.dumps(selection,indent=2)+'\n')
result={'source_commit':'2be412ccea62bdc4bd96deb082c46d7a792076ea','deliverables':len(summary),'claims':len(claims),'residuals':len(res),'unknowns':sum(a['Disposition']=='UNKNOWN' for a in claims),'stale':sum(a['Disposition']=='STALE_INPUT' for a in claims),'warranted_none':[a['DeliverableID'] for a in summary if a['CandidateAssessment']=='NONE'],'dispositions':dict(collections.Counter(a['Disposition'] for a in claims)),'source_hashes_reproduced':len(sources),'errors':errors,'result':'PASS' if not errors else 'FAIL','independent_verification':'PENDING until separately sealed verifier reviewed'}
(P/'VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));assert not errors,errors
