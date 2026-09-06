"""Read-only member fan-in checks; writes only caller-named package report."""
import csv,hashlib,json,pathlib,re,sys,subprocess
P=pathlib.Path(__file__).resolve().parent
R=pathlib.Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],cwd=P,text=True).strip())
BASE='2be412ccea62bdc4bd96deb082c46d7a792076ea'
CF='ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'.split(',')
RF='ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'.split(',')
DIS=set('ALIGNED IMPLEMENTED_UNDOCUMENTED DOCUMENTED_UNIMPLEMENTED PARTIALLY_IMPLEMENTED IMPLEMENTED_DIFFERENTLY ACCEPTED_DIVERGENCE LIFECYCLE_REASSESSMENT_REQUIRED DEFERRED_AGENT_WORKFLOW AUTHORITY_CONFLICT UNKNOWN STALE_INPUT'.split())
expected=json.loads((P/'EXPECTED_CLAIM_IDS.json').read_text()); members={};errors=[];allc=[];allr=[]
def err(d,s):errors.append(d+': '+s)
def csvread(f,fields,d):
 b=f.read_bytes()
 if b'\r' in b:err(d,'CSV is not LF '+f.name)
 rd=csv.DictReader(b.decode().splitlines()); rows=list(rd)
 if rd.fieldnames!=fields:err(d,'schema '+f.name)
 return rows
for d in expected:
 root=P/'WORKERS'/d
 if (root/'CORRECTION_S001'/'RETURN.md').exists():root=root/'CORRECTION_S001'
 if not (root/'RETURN.md').exists():continue
 c=csvread(root/'CLAIMS.csv',CF,d);rr=csvread(root/'RESIDUALS.csv',RF,d); ids={x['ClaimID'] for x in c};rids={x['ResidualID'] for x in rr}
 if len(ids)!=len(c):err(d,'duplicate claim IDs')
 if len(rids)!=len(rr):err(d,'duplicate residual IDs')
 missing={d+'::'+x for x in expected[d]['local_ids']}-ids
 if missing:err(d,'missing defined IDs '+str(sorted(missing)))
 for x in c:
  if x['DeliverableID']!=d or not x['ClaimID'].startswith(d+'::'):err(d,'claim identity')
  if x['Disposition'] not in DIS:err(d,'disposition '+x['Disposition'])
  if x['SourceCommit']!=BASE:err(d,'source commit '+x['ClaimID'])
  if not x['SourceHashes']:err(d,'missing source hashes '+x['ClaimID'])
  links={v.strip() for v in x['ProposedResidualID'].split(';') if v.strip() not in {'','NONE','N/A'}}
  for rid in links:
   if rid not in rids:err(d,'claim missing residual '+rid)
   elif x['ClaimID'] not in next(y for y in rr if y['ResidualID']==rid)['ClaimIDs']:err(d,'claim inverse link '+x['ClaimID'])
 for x in rr:
  if x['Selectability']!='NON_SELECTABLE_PENDING_OWNER_APPLICATION':err(d,'selectable residual '+x['ResidualID'])
  if not re.fullmatch(re.escape(d)+r'-REM-\d{3}',x['ResidualID']):err(d,'residual ID shape '+x['ResidualID'])
  if not x['Depends'].strip():err(d,'blank Depends '+x['ResidualID'])
  if not any(v in x['ExactGate']+' '+x['ProposedText'] for v in ['NOT_SELECTABLE_UNTIL:','(gated:','(stage-gated:']):err(d,'gate marker '+x['ResidualID'])
  for cid in x['ClaimIDs'].split(';'):
   if cid not in ids:err(d,'residual missing claim '+cid)
   elif x['ResidualID'] not in next(y for y in c if y['ClaimID']==cid)['ProposedResidualID']:err(d,'residual inverse link '+cid)
 m=json.loads((root/'READ_MANIFEST.json').read_text())
 if m.get('source_commit')!=BASE:err(d,'manifest base')
 for key in ['hashes','historical_sources','checks','source_unchanged']:
  if key not in m:err(d,'missing manifest field '+key)
 for path,h in m.get('hashes',{}).items():
  fp=R/path
  if pathlib.Path(path).is_absolute() or '..' in pathlib.Path(path).parts:err(d,'nonportable source path '+path)
  elif not fp.is_file():err(d,'source missing '+path)
  elif hashlib.sha256(fp.read_bytes()).hexdigest()!=h:err(d,'source drift '+path)
 if not m.get('source_unchanged'):err(d,'source unchanged not proven')
 members[d]={'claims':len(c),'residuals':len(rr),'unknown':sum(x['Disposition']=='UNKNOWN' for x in c),'nonaligned':sum(x['Disposition']!='ALIGNED' for x in c),'read_hashes':len(m.get('hashes',{})),'selected_root':str(root.relative_to(R))}
 allc+=c;allr+=rr
report={'base':BASE,'member_count':len(members),'members':members,'claims':len(allc),'residuals':len(allr),'errors':errors,'structural_pass':not errors}
if len(sys.argv)>1:(P/sys.argv[1]).write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
sys.exit(bool(errors))
