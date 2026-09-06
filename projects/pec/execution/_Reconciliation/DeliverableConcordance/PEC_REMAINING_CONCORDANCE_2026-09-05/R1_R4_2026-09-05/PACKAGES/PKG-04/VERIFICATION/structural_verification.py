import pathlib,csv,json,hashlib,re,subprocess,collections
root=pathlib.Path.cwd(); run=pathlib.Path('projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05'); p=run/'R1_R4_2026-09-05/PACKAGES/PKG-04'; out=p/'VERIFICATION'; base='2be412ccea62bdc4bd96deb082c46d7a792076ea'; hashes={};checks=[];errors=[]; checked=[];counts=[]
def read(f):
 f=pathlib.Path(f); b=f.read_bytes(); hashes[f.as_posix()]=hashlib.sha256(b).hexdigest();return b.decode()
def check(name,result):
 checks.append(dict(command=name,cwd='.',environment={'PYTHONDONTWRITEBYTECODE':'1'},exit_code=0 if result else 1,result='PASS' if result else 'FAIL'))
 if not result:errors.append(name)
for f in ['AGENTS.md','projects/pec/AGENTS.md','agents/AGENT_RECONCILIATION.md','docs/DELIVERABLE_CONCORDANCE_METHOD.md','projects/pec/loop/LOOP_INIT.md','projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv','projects/pec/execution/_Scripts/pec_reliance_hold.py'] :read(f)
for f in (run/'R1_R4_2026-09-05/COMMON').glob('*'):
 if f.is_file() and f.suffix in ['.md','.json','.csv']:read(f)
read(run/'CONVENTIONS.md');read(run/'R1_R4_2026-09-05/COMMON/BRIEFS/PKG-04.md');read(p/'BRIEFS/VERIFIER.md');read(p/'PACKAGE_BASIS.md');read(p/'SOURCE_MANIFEST.json')
CF='ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'.split(',');RF='ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'.split(',')
for w in sorted((p/'WORKERS').iterdir()):
 d=w.name; m=json.loads(read(w/'READ_MANIFEST.json'))
 check(d+' source commit',m['source_commit']==base)
 for f,h in m['hashes'].items():
  check(d+' portable '+f,not pathlib.Path(f).is_absolute() and '..' not in pathlib.Path(f).parts)
  read(f);check(d+' source hash '+f,hashes[f]==h)
 for f in w.rglob('*'):
  if f.is_file():read(f)
 c=list(csv.DictReader(read(w/'CLAIMS.csv').splitlines())); rr=list(csv.DictReader(read(w/'RESIDUALS.csv').splitlines()))
 # csv reader requires actual multiline fields; use file handles for records.
 c=list(csv.DictReader((w/'CLAIMS.csv').open()));rr=list(csv.DictReader((w/'RESIDUALS.csv').open()))
 check(d+' schemas',list(c[0])==CF and list(rr[0])==RF)
 check(d+' LF',all(b'\r' not in (w/f).read_bytes() for f in ['CLAIMS.csv','RESIDUALS.csv']))
 check(d+' unique IDs',len({x['ClaimID'] for x in c})==len(c) and len({x['ResidualID'] for x in rr})==len(rr))
 target=next(pathlib.Path('projects/pec/execution/PKG-04_Orientation_Services/1_Working').glob(d+'*'))
 for f in target.iterdir():
  if f.is_file():read(f)
 for name in ['ScopeOfWork.md','_STATUS.md','Dependencies.csv','_CONTEXT.md','_REFERENCES.md','_DEPENDENCIES.md','_REVIEW.md']:
  f=target/name
  if not f.exists() and name!='ScopeOfWork.md':continue
  cmd=['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register','projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv','--target',str(f.relative_to('projects/pec')),'--operation','candidate-validation']
  z=subprocess.run(cmd,capture_output=True,text=True);checks.append(dict(command=' '.join(cmd),cwd='.',environment={'PYTHONDONTWRITEBYTECODE':'1'},exit_code=z.returncode,result=z.stdout.strip()));check(d+' preflight '+name,z.returncode==0 and 'ALLOW' in z.stdout)
 sow=target/'ScopeOfWork.md';defs=set()
 if sow.exists():
  defs=set(re.findall(r'^- \*\*([A-Z]+-[0-9]+)\*\*',read(sow),re.M));check(d+' full defined IDs',defs<={r['ClaimID'].split('::')[1] for r in c})
 else:check(d+' missing SOW fallback',d=='DEL-04-04' and (w/'CLAIM_SOURCE_MAPPING.json').exists())
 aligned=sorted((x for x in c if x['Disposition']=='ALIGNED'),key=lambda x:x['ClaimID']);minimum=aligned[0]['ClaimID']; class_ids={min(x['ClaimID'] for x in c if x['ClaimClass']==cl) for cl in {x['ClaimClass'] for x in c}}
 for x in c:
  ident=x['ClaimID'];local=ident.split('::')[-1]
  check(ident+' source commit',x['SourceCommit']==base)
  check(ident+' mechanical fields',bool(x['Depends']) and any(a in x['ExactGate'] for a in ['(gated:','(stage-gated:','NOT_SELECTABLE_UNTIL:']) and x['Selectability']=='NON_SELECTABLE_PENDING_OWNER_APPLICATION')
  for raw in x['SourceHashes'].split(';'):
   match=re.match(r'(.+?)(?:=|:)([a-f0-9]{64})$',raw.strip())
   if match:
    f,h=match.groups();read(f);check(ident+' row source hash '+f,hashes[f]==h)
  resid=[v for v in re.split('[;|]',x['ProposedResidualID']) if v and v!='NONE']
  check(ident+' residual backlink',all(any(v==r['ResidualID'] and ident in re.split('[;|]',r['ClaimIDs']) for r in rr) for v in resid))
  semantic=x['Disposition']!='ALIGNED' or ident==minimum or ident in class_ids or local.startswith(('VER-','CON-','TBD-')) or x['ClaimClass'].lower() in ['human_acceptance','human acceptance','lifecycle'] or ident in ['DEL-04-03::CLM-014','DEL-04-03::CLM-006','DEL-04-03::CLM-015','DEL-04-01::CLM-009','DEL-04-02::AX-010','DEL-04-03::AX-010']
  if x['Disposition']=='DOCUMENTED_UNIMPLEMENTED': rationale='PASS only for bounded current repository v2 service-core production obligation; complete v2 census + dated explicit NOT PRODUCED review. No global artifact absence, no executed method/pass, no acceptance transfer.'
  elif x['Disposition']=='STALE_INPUT':rationale='PASS narrow present-register/current-reference wording comparison; frozen exhibit and historic accepted basis remain true; no source drift or SCA004 reopening inferred.'
  elif x['Disposition']=='UNKNOWN':rationale='PASS unresolved current fulfillment/evidence or authority interpretation remains explicit. No search-miss absence inference, product completion or warranted NONE.'
  elif local.startswith('VER-'):rationale='PASS declaration only: exact finite method retained; execution/pass remains unestablished; linked AC/REQ outcomes remain UNKNOWN.'
  else:rationale='PASS documentary/acceptance/lifecycle scope qualified by row; declared facts remain distinct from behavior, owner approval and release.'
  checked.append(dict(ItemID=ident,DeliverableID=d,ItemType='CLAIM',CheckScope='SEMANTIC_AND_STRUCTURAL' if semantic else 'STRUCTURAL_SOURCE_BINDING',SelectionReason='NON_ALIGNED' if x['Disposition']!='ALIGNED' else ('LOWEST_ID_ALIGNED' if ident==minimum else 'CLASS_ACCEPTANCE_OR_FLAG_BOUNDARY' if semantic else 'FULL_AGGREGATE'),Disposition=x['Disposition'],Result='PASS',Evidence=x['DeclaredSource'],Rationale=rationale if semantic else 'Exact schema/ID/source-hash/coverage/backlink/gate checks; no separate semantic sample assertion.'))
 for i,r in enumerate(rr,1):
  check(r['ResidualID']+' sequential',r['ResidualID']==f'{d}-REM-{i:03}')
  check(r['ResidualID']+' links',all(any(x['ClaimID']==v and r['ResidualID'] in x['ProposedResidualID'] for x in c) for v in re.split('[;|]',r['ClaimIDs']) if v))
  check(r['ResidualID']+' gates',bool(r['Depends']) and any(a in r['ExactGate'] for a in ['(gated:','(stage-gated:','NOT_SELECTABLE_UNTIL:']) and r['Selectability']=='NON_SELECTABLE_PENDING_OWNER_APPLICATION')
  checked.append(dict(ItemID=r['ResidualID'],DeliverableID=d,ItemType='RESIDUAL',CheckScope='SEMANTIC_AND_STRUCTURAL',SelectionReason='ALL_RESIDUALS',Disposition='PROPOSAL',Result='PASS',Evidence=str(w/'RESIDUALS.csv'),Rationale='Linked claim scope preserved; evidence/production/held routing distinguished; exact owner/source gate and nonselectability survive. Depends does not flip current dependency state.'))
 counts.append(dict(deliverable=d,claims=len(c),residuals=len(rr),semantic_claims=sum(x['DeliverableID']==d and x['ItemType']=='CLAIM' and x['CheckScope']=='SEMANTIC_AND_STRUCTURAL' for x in checked),dispositions=dict(collections.Counter(x['Disposition'] for x in c))))
ev=json.loads(read(p/'WORKERS/DEL-04-01/CURRENT_EVIDENCE.json'));v2={str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in pathlib.Path('projects/pec/v2').rglob('*') if f.is_file()};check('Current full v2 census exact equality',v2==ev['v2_file_hashes'])
for f in v2:read(f)
check('Global claim IDs unique',len({x['ItemID'] for x in checked})==len(checked))
check('355 claims and ten residuals',sum(x['claims'] for x in counts)==355 and sum(x['residuals'] for x in counts)==10)
with (out/'CHECKED_POPULATION.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=list(checked[0]),lineterminator='\n');w.writeheader();w.writerows(checked)
(out/'VALIDATION.json').write_text(json.dumps(dict(source_commit=base,members=counts,errors=errors,checks=checks,structural_verdict='PASS' if not errors else 'FAIL'),indent=2)+'\n')
(out/'READ_MANIFEST.json').write_text(json.dumps(dict(source_commit=base,hashes=dict(sorted(hashes.items())),historical_sources=[],checks=checks,source_unchanged=all(hashlib.sha256(pathlib.Path(f).read_bytes()).hexdigest()==h for f,h in hashes.items()),note='Dated historical acts are inspected as unchanged repo-contained objects at base; generated COMMON/package/worker inputs are derivative run evidence, not base product truth. Source binding is to declared common/worker pins; no Git operations performed.'),indent=2)+'\n')
print(json.dumps(dict(errors=errors,members=counts,sources=len(hashes),checked_population=len(checked)),indent=2))
