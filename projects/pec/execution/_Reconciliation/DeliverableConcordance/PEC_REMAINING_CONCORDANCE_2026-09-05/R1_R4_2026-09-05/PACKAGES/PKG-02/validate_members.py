from pathlib import Path
import csv,json,hashlib,re,sys
ROOT=Path(__file__).resolve().parent
REPO=Path.cwd()
C='ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'.split(',')
R='ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'.split(',')
BASE='2be412ccea62bdc4bd96deb082c46d7a792076ea'
def refs(s): return [x.strip() for x in re.split('[;|]',s) if x.strip() and x.strip()!='NONE']
def validate(p):
 p=p.resolve(); e=[]; ds=p.name; ds=next((x for x in p.parts if re.fullmatch('DEL-02-[0-9]{2}',x)),ds)
 rows=[]
 for name,cols in [('CLAIMS.csv',C),('RESIDUALS.csv',R)]:
  f=p/name
  if not f.exists(): e.append('missing '+name); rows.append([]); continue
  b=f.read_bytes(); rd=csv.DictReader(b.decode().splitlines()); rr=list(rd); rows.append(rr)
  if rd.fieldnames!=cols:e.append(name+' schema')
  if b'\r' in b:e.append(name+' not LF')
  if len({x[cols[0]] for x in rr})!=len(rr):e.append(name+' duplicate IDs')
  for x in rr:
   if x['DeliverableID']!=ds:e.append(name+' wrong deliverable')
   if not x['Depends']:e.append(name+' empty Depends')
   if not any(y in x['ExactGate'] for y in ('(gated:','(stage-gated:','NOT_SELECTABLE_UNTIL:')):e.append(name+' invalid gate '+x[cols[0]])
   if x['Selectability']!='NON_SELECTABLE_PENDING_OWNER_APPLICATION':e.append(name+' selectability '+x[cols[0]])
 cc,rr=rows; cm={x['ClaimID']:x for x in cc}; rm={x['ResidualID']:x for x in rr}
 if set(rm)!={ds+'-REM-'+str(i).zfill(3) for i in range(1,len(rr)+1)}:e.append('residual sequence')
 for c in cc:
  if not c['ClaimID'].startswith(ds+'::'):e.append('claim prefix '+c['ClaimID'])
  if c['SourceCommit']!=BASE:e.append('base mismatch')
  if not c['SourceHashes']:e.append('empty hashes')
  for rid in refs(c['ProposedResidualID']):
   if rid not in rm or c['ClaimID'] not in refs(rm[rid]['ClaimIDs']):e.append('backlink '+c['ClaimID']+' '+rid)
 for r in rr:
  for cid in refs(r['ClaimIDs']):
   if cid not in cm or r['ResidualID'] not in refs(cm[cid]['ProposedResidualID']):e.append('inverse backlink '+r['ResidualID']+' '+cid)
 mf=p/'READ_MANIFEST.json'
 if mf.exists():
  m=json.loads(mf.read_text())
  for k in ('source_commit','hashes','historical_sources','checks','source_unchanged'):
   if k not in m:e.append('manifest missing '+k)
  if m.get('source_commit')!=BASE:e.append('manifest base')
  for path,h in m.get('hashes',{}).items():
   f=REPO/path
   if Path(path).is_absolute() or '..' in Path(path).parts:e.append('nonportable '+path)
   elif not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=h:e.append('hash mismatch '+path)
 else:e.append('missing manifest')
 return {'path':str(p.relative_to(REPO)),'claims':len(cc),'residuals':len(rr),'unknowns':sum(c['Disposition']=='UNKNOWN' for c in cc),'errors':sorted(set(e)),'pass':not e}
if __name__=='__main__':
 paths=[Path(x) for x in sys.argv[1:]] or sorted((ROOT/'WORKERS').glob('DEL-*'))
 results=[validate(p) for p in paths]; print(json.dumps(results,indent=2)); sys.exit(0 if all(x['pass'] for x in results) else 1)
