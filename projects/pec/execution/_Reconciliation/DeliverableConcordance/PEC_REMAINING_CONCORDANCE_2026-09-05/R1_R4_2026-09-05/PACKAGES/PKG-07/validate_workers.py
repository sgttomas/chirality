import pathlib,csv,json,hashlib,re,sys
ROOT=pathlib.Path.cwd()
PKG=pathlib.Path(__file__).parent
C="ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes".split(',')
R="ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes".split(',')
BASE="2be412ccea62bdc4bd96deb082c46d7a792076ea"
def validate(d):
 errors=[]; tables=[]
 for name,fields in [("CLAIMS.csv",C),("RESIDUALS.csv",R)]:
  p=d/name
  if not p.exists(): return {"member":d.name,"errors":["missing "+name]}
  data=p.read_bytes(); reader=csv.DictReader(data.decode().splitlines()); rows=list(reader);tables.append(rows)
  if reader.fieldnames!=fields:errors.append(name+" schema")
  if b'\r' in data:errors.append(name+" non-LF")
  for row in rows:
   if not row['Depends']:errors.append(name+" blank Depends")
   if not any(m in row['ExactGate'] for m in ['(gated:', '(stage-gated:', 'NOT_SELECTABLE_UNTIL:']):errors.append(name+" gate marker")
   if row['Selectability']!='NON_SELECTABLE_PENDING_OWNER_APPLICATION':errors.append(name+" selectability")
 claims,res=tables; ci={x['ClaimID']:x for x in claims};ri={x['ResidualID']:x for x in res}
 if len(ci)!=len(claims) or len(ri)!=len(res):errors.append('duplicate IDs')
 if sorted(ri)!=[f'{d.name}-REM-{n:03}' for n in range(1,len(res)+1)]:errors.append('residual sequence')
 for c in claims:
  if not c['ClaimID'].startswith(d.name+'::'):errors.append('claim owner')
  if c['SourceCommit']!=BASE:errors.append('source commit')
  for rid in filter(None,(x.strip() for x in re.split(r'[;|]',c['ProposedResidualID']))):
   if rid=='NONE':continue
   if rid not in ri or c['ClaimID'] not in ri[rid]['ClaimIDs']:errors.append('claim reciprocity '+rid)
 for rr in res:
  for cid in filter(None,(x.strip() for x in re.split(r'[;|]',rr['ClaimIDs']))):
   if cid not in ci or rr['ResidualID'] not in ci[cid]['ProposedResidualID']:errors.append('residual reciprocity '+cid)
 m=json.loads((d/'READ_MANIFEST.json').read_text())
 if m.get('source_commit')!=BASE or not m.get('source_unchanged'):errors.append('manifest basis')
 for path,h in m['hashes'].items():
  q=ROOT/path
  if not q.is_file() or hashlib.sha256(q.read_bytes()).hexdigest()!=h:errors.append('hash '+path)
 return {'member':d.name,'claims':len(claims),'residuals':len(res),'unknown':sum(c['Disposition']=='UNKNOWN' for c in claims),'dispositions':{v:sum(c['Disposition']==v for c in claims) for v in sorted(set(c['Disposition'] for c in claims))},'sources':len(m['hashes']),'errors':errors}
if __name__=='__main__':
 dirs=[PKG/'WORKERS'/x for x in sys.argv[1:]] if len(sys.argv)>1 else sorted((PKG/'WORKERS').iterdir())
 result=[validate(d) for d in dirs];print(json.dumps(result,indent=2));sys.exit(int(any(x['errors'] for x in result)))
