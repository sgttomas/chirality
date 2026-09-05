#!/usr/bin/env python3
"""Read-only structural checks over the six authorized R0 sample outputs."""
from pathlib import Path
import csv, hashlib, json, re, sys, subprocess
root=Path(__file__).resolve().parent
repo=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],cwd=root,text=True).strip())
samples=['DEL-00-02','DEL-00-03','DEL-01-05','DEL-01-06','DEL-02-07','DEL-08-02']
fields='ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'.split(',')
resfields='ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'.split(',')
dispositions=set('ALIGNED IMPLEMENTED_UNDOCUMENTED DOCUMENTED_UNIMPLEMENTED PARTIALLY_IMPLEMENTED IMPLEMENTED_DIFFERENTLY ACCEPTED_DIVERGENCE LIFECYCLE_REASSESSMENT_REQUIRED DEFERRED_AGENT_WORKFLOW AUTHORITY_CONFLICT UNKNOWN STALE_INPUT'.split())
errors=[]; summary=[]
manifest=json.loads((root/'SOURCE_MANIFEST.json').read_text())
for name,h in manifest['hashes'].items():
 p=repo/name
 if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=h:errors.append('SOURCE_DRIFT:'+name)
for did in samples:
 d=root/'R0_CALIBRATION'/did
 for name in ['CLAIMS.csv','RESIDUALS.csv','COVERAGE.md','READ_MANIFEST.json','RETURN.md']:
  if not (d/name).is_file():errors.append('MISSING:'+did+'/'+name)
 if not (d/'CLAIMS.csv').is_file() or not (d/'RESIDUALS.csv').is_file():continue
 ledgers={}
 for name,expected in [('CLAIMS.csv',fields),('RESIDUALS.csv',resfields)]:
  p=d/name
  if b'\r' in p.read_bytes():errors.append('NON_LF:'+str(p.relative_to(root)))
  with p.open(newline='') as f:
   reader=csv.DictReader(f);rows=list(reader)
   if reader.fieldnames!=expected:errors.append('SCHEMA:'+did+'/'+name)
   if any(None in row for row in rows):errors.append('ROW_WIDTH:'+did+'/'+name)
   ledgers[name]=rows
 claims=ledgers['CLAIMS.csv'];residuals=ledgers['RESIDUALS.csv'];ids=[row.get('ClaimID','') for row in claims]
 if len(set(ids))!=len(ids):errors.append('DUPLICATE_CLAIM:'+did)
 rids=[row.get('ResidualID','') for row in residuals]
 if len(set(rids))!=len(rids):errors.append('DUPLICATE_RESIDUAL:'+did)
 for row in claims:
  cid=row.get('ClaimID','')
  if not cid.startswith(did+'::'):errors.append('CLAIM_ID:'+cid)
  if row.get('DeliverableID')!=did:errors.append('WRONG_OWNER:'+cid)
  if row.get('Disposition') not in dispositions:errors.append('DISPOSITION:'+cid)
  for f in ['NormativeSource','DeclaredSource','SourceCommit','SourceHashes','EvidenceReferences']:
   if not row.get(f,'').strip():errors.append('MISSING_FIELD:'+cid+':'+f)
  if row.get('SourceCommit')!=manifest['base']:errors.append('WRONG_BASE:'+cid)
 for row in residuals:
  if row.get('DeliverableID')!=did:errors.append('RESIDUAL_OWNER:'+did)
  if row.get('Selectability')!='NON_SELECTABLE_PENDING_OWNER_APPLICATION':errors.append('RESIDUAL_SELECTABILITY:'+row.get('ResidualID',''))
  for f in ['ProposedText','Depends','ExactGate','ClosureEvidence','AuthorityNeeded']:
   if not row.get(f,'').strip():errors.append('RESIDUAL_MISSING:'+did+':'+f)
 sow=repo/manifest['sample'][did]/'ScopeOfWork.md'
 # Require every unique existing contract ID to appear as claim or explained handling.
 if sow.is_file():
  sourceids=set(re.findall(r'\b(?:REQ|AC|VER)-\d{3}\b',sow.read_text()))
  covered=set(cid.split('::',1)[-1] for cid in ids)
  handling=(d/'COVERAGE.md').read_text() if (d/'COVERAGE.md').is_file() else ''
  missing=[x for x in sourceids-covered if x not in handling]
  if missing:errors.append('UNCOVERED_IDS:'+did+':'+','.join(sorted(missing)))
 summary.append({'deliverable':did,'claims':len(claims),'residuals':len(residuals),'dispositions':{x:sum(c.get('Disposition')==x for c in claims) for x in sorted(dispositions) if any(c.get('Disposition')==x for c in claims)}})
print(json.dumps({'status':'PASS' if not errors else 'FAIL','kind':'structural_only_not_semantic_acceptance','summary':summary,'errors':errors},indent=2))
sys.exit(bool(errors))
