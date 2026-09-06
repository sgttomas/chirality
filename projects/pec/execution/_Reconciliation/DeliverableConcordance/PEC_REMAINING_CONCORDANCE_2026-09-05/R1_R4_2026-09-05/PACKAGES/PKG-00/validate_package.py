import pathlib,csv,json,hashlib,sys
root=pathlib.Path.cwd()
p=pathlib.Path(__file__).resolve().parent
claim_fields="ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes".split(',')
res_fields="ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes".split(',')
claims=[];residuals=[];errors=[];sources={}; members=[]
for d in ['DEL-00-01','DEL-00-02','DEL-00-03']:
 w=p/'WORKERS'/d
 if '--selected' in sys.argv and d in ['DEL-00-01','DEL-00-03']: w=w/'REVISION_V001'
 if not (w/'CLAIMS.csv').exists():
  errors.append(d+': missing worker');continue
 for f,fields,target in [('CLAIMS.csv',claim_fields,claims),('RESIDUALS.csv',res_fields,residuals)]:
  raw=(w/f).read_bytes();reader=csv.DictReader(raw.decode().splitlines());rows=list(reader)
  if reader.fieldnames!=fields:errors.append(d+': schema '+f)
  if b'\r' in raw:errors.append(d+': non-LF '+f)
  if any(x['DeliverableID']!=d for x in rows):errors.append(d+': foreign row')
  target.extend(rows)
 m=json.loads((w/'READ_MANIFEST.json').read_text())
 for name in ['source_commit','hashes','historical_sources','checks','source_unchanged']:
  if name not in m:errors.append(d+': manifest missing '+name)
 for f,h in m.get('hashes',{}).items():
  fp=root/f
  if pathlib.Path(f).is_absolute() or '..' in pathlib.Path(f).parts:errors.append(d+': nonportable '+f)
  elif not fp.is_file() or hashlib.sha256(fp.read_bytes()).hexdigest()!=h:errors.append(d+': source hash '+f)
  elif f in sources and sources[f]!=h:errors.append(d+': inconsistent '+f)
  sources[f]=h
 if m.get('source_commit')!='2be412ccea62bdc4bd96deb082c46d7a792076ea':errors.append(d+': base mismatch')
 if m.get('source_unchanged')!=True:errors.append(d+': source unchanged not true')
 members.append({'deliverable':d,'claim_count':sum(x['DeliverableID']==d for x in claims),'residual_count':sum(x['DeliverableID']==d for x in residuals)})
ids=[x['ClaimID'] for x in claims];rids=[x['ResidualID'] for x in residuals]
if len(ids)!=len(set(ids)):errors.append('duplicate claims')
if len(rids)!=len(set(rids)):errors.append('duplicate residuals')
for c in claims:
 if not c['ClaimID'].startswith(c['DeliverableID']+'::'):errors.append('noncompound '+c['ClaimID'])
 if c['SourceCommit']!='2be412ccea62bdc4bd96deb082c46d7a792076ea':errors.append('row base '+c['ClaimID'])
 if c['ProposedResidualID'] not in ['', 'NONE','N/A']:
  linked=[r for r in residuals if r['ResidualID'] in c['ProposedResidualID']]
  if not linked or any(c['ClaimID'] not in r['ClaimIDs'] for r in linked):errors.append('claim reciprocity '+c['ClaimID'])
for r in residuals:
 linked=[c for c in claims if c['ClaimID'] in r['ClaimIDs']]
 if not linked or any(r['ResidualID'] not in c['ProposedResidualID'] for c in linked):errors.append('residual reciprocity '+r['ResidualID'])
 if not r['ResidualID'].startswith(r['DeliverableID']+'-REM-'):errors.append('residual ID shape '+r['ResidualID'])
 if r['Selectability']!='NON_SELECTABLE_PENDING_OWNER_APPLICATION':errors.append('selectability '+r['ResidualID'])
result={'status':'PASS' if not errors else 'FAIL','errors':errors,'members':members,'claims':len(claims),'residuals':len(residuals),'source_hashes_reproduced':len(sources)}
print(json.dumps(result,indent=2))
if '--write' in sys.argv:
 (p/'AGGREGATE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
 if not errors:
  for name,fields,rows in [('PACKAGE_CLAIMS.csv',claim_fields,claims),('PACKAGE_RESIDUALS.csv',res_fields,residuals)]:
   with (p/name).open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');writer.writeheader();writer.writerows(rows)
sys.exit(bool(errors))
