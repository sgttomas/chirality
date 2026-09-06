import csv,json,hashlib,pathlib,re,sys
import subprocess
ROOT=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],cwd=pathlib.Path(__file__).resolve().parent,text=True).strip())
P=pathlib.Path(__file__).resolve().parent
C='ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'.split(',')
R='ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'.split(',')
DISP=set('ALIGNED IMPLEMENTED_UNDOCUMENTED DOCUMENTED_UNIMPLEMENTED PARTIALLY_IMPLEMENTED IMPLEMENTED_DIFFERENTLY ACCEPTED_DIVERGENCE LIFECYCLE_REASSESSMENT_REQUIRED DEFERRED_AGENT_WORKFLOW AUTHORITY_CONFLICT UNKNOWN STALE_INPUT'.split())
BASE='2be412ccea62bdc4bd96deb082c46d7a792076ea'
def validate(paths):
 errors=[];counts=[];allc=[];allr=[]
 for path in paths:
  d=path.name if path.name.startswith('DEL-') else path.parent.name
  def fail(msg):errors.append(d+': '+msg)
  def rows(name,header):
   b=(path/name).read_bytes()
   if b'\r' in b:fail(name+' non-LF')
   with (path/name).open(newline='') as f:
    reader=csv.DictReader(f)
    if reader.fieldnames!=header:fail(name+' schema')
    return list(reader)
  try:c=rows('CLAIMS.csv',C);r=rows('RESIDUALS.csv',R);m=json.loads((path/'READ_MANIFEST.json').read_text())
  except Exception as e:fail(str(e));continue
  ids=[x['ClaimID'] for x in c];rids=[x['ResidualID'] for x in r]
  if len(ids)!=len(set(ids)):fail('duplicate claims')
  if rids!=[f'{d}-REM-{i:03}' for i in range(1,len(r)+1)]:fail('residual sequence')
  for x in c:
   if x['DeliverableID']!=d or not x['ClaimID'].startswith(d+'::'):fail('claim owner')
   if x['Disposition'] not in DISP:fail('controlled disposition')
   if x['SourceCommit']!=BASE or not x['SourceHashes']:fail('source binding')
   if not x['Depends']:fail('empty Depends')
   linked=re.findall(r'DEL-\d{2}-\d{2}-REM-\d{3}',x['ProposedResidualID'])
   for ri in linked:
    matches=[z for z in r if z['ResidualID']==ri]
    if len(matches)!=1 or x['ClaimID'] not in matches[0]['ClaimIDs']:fail('claim backlink '+x['ClaimID'])
   if linked and not any(t in x['ExactGate'] for t in ['(gated:','(stage-gated:','NOT_SELECTABLE_UNTIL:']):fail('claim gate')
  for x in r:
   if x['DeliverableID']!=d:fail('residual owner')
   if not x['Depends']:fail('empty residual Depends')
   if not any(t in x['ExactGate'] for t in ['(gated:','(stage-gated:','NOT_SELECTABLE_UNTIL:']):fail('residual gate')
   if x['Selectability']!='NON_SELECTABLE_PENDING_OWNER_APPLICATION':fail('selectability')
   linked=re.findall(r'DEL-\d{2}-\d{2}::[A-Za-z0-9_.-]+',x['ClaimIDs'])
   if not linked:fail('empty residual claims')
   for ci in linked:
    matches=[z for z in c if z['ClaimID']==ci]
    if len(matches)!=1 or x['ResidualID'] not in matches[0]['ProposedResidualID']:fail('residual backlink '+ci)
  if m.get('source_commit')!=BASE or m.get('source_unchanged') is not True:fail('manifest binding')
  if not all(k in m for k in ['hashes','historical_sources','checks']):fail('manifest schema')
  for source,h in m.get('hashes',{}).items():
   s=pathlib.Path(source)
   if s.is_absolute() or '..' in s.parts:fail('nonportable source '+source);continue
   if not (ROOT/s).is_file():fail('source absent '+source);continue
   if hashlib.sha256((ROOT/s).read_bytes()).hexdigest()!=h:fail('source drift '+source)
  counts.append({'DeliverableID':d,'Claims':len(c),'Residuals':len(r),'Unknown':sum(x['Disposition']=='UNKNOWN' for x in c),'DispositionCounts':dict((z,sum(x['Disposition']==z for x in c)) for z in sorted(set(x['Disposition'] for x in c)))})
  allc+=c;allr+=r
 return {'passed':not errors,'errors':errors,'members':counts},allc,allr
if __name__=='__main__':
 paths=[pathlib.Path(x) for x in sys.argv[1:]] or sorted((P/'WORKERS').glob('DEL-*'))
 result,_,_=validate(paths); print(json.dumps(result,indent=2));sys.exit(0 if result['passed'] else 1)
