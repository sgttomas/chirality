import csv,hashlib,json,re,subprocess,os
from pathlib import Path
ROOT=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip());os.chdir(ROOT)
BASE='2be412ccea62bdc4bd96deb082c46d7a792076ea'
RUN=Path('projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05')
PKG=RUN/'R1_R4_2026-09-05/PACKAGES/PKG-03'; W=PKG/'WORKERS/DEL-03-01'
D=Path('projects/pec/execution/PKG-03_Reconciliation_Parity/1_Working/DEL-03-01_Full_rebuild_reconciler_one_command'); S=D/'ScopeOfWork.md'
hashes={}; texts={}; checks=[]
def read(p):
 p=Path(p); b=p.read_bytes(); hashes[str(p)]=hashlib.sha256(b).hexdigest();texts[str(p)]=b.decode();return texts[str(p)]
def check(cmd):
 r=subprocess.run(cmd,text=True,capture_output=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'});checks.append(dict(command=' '.join(cmd),cwd='.',environment={'PYTHONDONTWRITEBYTECODE':'1'},exit_code=r.returncode,result=r.stdout+r.stderr));return r
paths=[Path('AGENTS.md'),Path('projects/pec/AGENTS.md'),Path('agents/AGENT_RECONCILIATION.md'),Path('docs/DELIVERABLE_CONCORDANCE_METHOD.md'),Path('docs/governance_harness/_DECISIONS/D-GOV-01_substrate_authority.md'),Path('tools/REGISTRY.md'),Path('projects/pec/docs/PRD.md'),Path('projects/pec/loop/LOOP_INIT.md'),RUN/'CONVENTIONS.md',PKG/'PACKAGE_BASIS.md',PKG/'SOURCE_MANIFEST.json',PKG/'BRIEFS/DEL-03-01.md',PKG/'validate_worker.py']
paths+=list((RUN/'R1_R4_2026-09-05/COMMON').glob('*.md'))+[RUN/'R1_R4_2026-09-05/COMMON/SOURCE_MANIFEST.json',RUN/'R1_R4_2026-09-05/COMMON/SCOPE_CENSUS.csv',RUN/'R1_R4_2026-09-05/COMMON/BRIEFS/PKG-03.md']
paths+=list(D.rglob('*'))
for pat in ['projects/pec/execution/_Decomposition/*','projects/pec/execution/_ScopeChange/SCA-002_2026-07-25_1042/*','projects/pec/execution/_ScopeChange/SCA-004_2026-08-02_2325/Handoff_State.md','projects/pec/v2/**/*']:
 paths+=list(Path('.').glob(pat))
for prefix in ['D-PEC-81','D-PEC-82','D-PEC-62','D-PEC-64','D-PEC-65','D-PEC-72','D-PEC-78']:
 paths+=list(Path('projects/pec/execution/_Coordination/_DECISIONS').glob(prefix+'*.md'))
paths += [Path('projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md'),Path('projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv'),Path('projects/pec/execution/_Scripts/pec_reliance_hold.py'),Path('projects/pec/execution/_Coordination/PLAN_2026-07-25_project_setup_dag_gate.md')]
upstreams=['DEL-01-01','DEL-01-03','DEL-01-04','DEL-01-06']+[f'DEL-02-{i:02}' for i in range(1,8)]
for did in upstreams+['DEL-00-01']:
 for folder in Path('projects/pec/execution').glob('PKG-*/1_Working/'+did+'_*'):
  paths += [folder/f for f in ['ScopeOfWork.md','_STATUS.md','_REVIEW.md','_CONTEXT.md'] if (folder/f).is_file()]
  if did=='DEL-00-01': paths += list((folder/'artifacts').rglob('*.md'))
for p in sorted(set(paths)):
 if p.is_file() and '__pycache__' not in str(p): read(p)
sow=texts[str(S)]; review=texts[str(D/'_REVIEW.md')]
assert hashes[str(S)]=='564955235aeab60f169e6377dd9d5bb5fbe2a88a8cc66094e17f6f83987792d2'
for filename in ['ScopeOfWork.md','_STATUS.md']:
 r=check(['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register','projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv','--target',str(D/filename).removeprefix('projects/pec/'),'--operation','candidate-validation']);assert r.returncode==0 and 'ALLOW' in r.stdout
source_manifest=json.loads(texts[str(PKG/'SOURCE_MANIFEST.json')]); mismatches=[p for p,h in hashes.items() if p in source_manifest['hashes'] and h!=source_manifest['hashes'][p]]; assert not mismatches
symbols={}
for p,t in texts.items():
 if p.startswith('projects/pec/v2/src/'):
  symbols[p]=re.findall(r'^\s*(?:class|def)\s+(\w+)',t,re.M)
(W/'IMPLEMENTATION_INVENTORY.json').write_text(json.dumps({'source_commit':BASE,'production_symbols':symbols,'v2_files':[p for p in hashes if p.startswith('projects/pec/v2/')],'finding':'Current production code exposes registered-loop configuration and typed registry port; no rebuild operation occurs in the inspected production modules. SOW CLM-022 and accepted REVIEW explicitly describe future implementation. This bounded corpus evidence is not a universal absence proof; all product execution rows remain UNKNOWN. Frozen pre-v2 source was not used as implementation evidence.'},indent=2)+'\n')
# Markdown definitions outside blockquotes; upstream quoted identifiers are not local definitions.
matches=list(re.finditer(r'^- \*\*((?:REQ|AC|VER|CLM|AX|TBD|CON|OUT)-\d{3})\*\* — (.*)',sow,re.M))
assert len(matches)==96 and len({m[1] for m in matches})==96
claims=[]; residuals=[]
HEADER='ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'.split(',')
RHEADER='ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'.split(',')
sel='NON_SELECTABLE_PENDING_OWNER_APPLICATION'
gate='(gated: later owner-approved exact Remaining application and exact PEC source/write/verification/rollback packet; D82 authorizes reporting only; preserve lifecycle and dependency registers)'
deps=';'.join(upstreams)
resdefs=[('Establish the current implementation and evidence for OUT-001 / REQ-001 through REQ-015; if still absent, propose bounded production of the one-command full rebuild and declared write boundary under the accepted SOW, retaining unresolved contract choices for owner routing.',deps,'Current source-bound reconciler entry point, declared-view record, claim-specific AC-001..015 evidence and accepted ambiguity dispositions; no inherited upstream completion.','EVIDENCE_CANDIDATE_CONDITIONAL_PRODUCTION'),('Establish the current OUT-002 rebuild test suite and execute the sixteen declared methods against the exact candidate; preserve VER-012 stand-in then live-facility rerun and VER-015 later enforcement boundary.',deps,'Test-to-VER mapping, complete execution logs and exact source hashes; finite method results only; no release/kill discharge.','EVIDENCE_CANDIDATE'),('Route the still-unresolved loop-to-project feed-manifest resolution in TBD-005 to the owning upstream/PEC decision instrument; do not settle registry serialization or create a downstream duty.', 'DEL-02-07','Accepted resolution and current stable-interface mapping preserving REQ-008; no automatic upstream mutation.','HELD_AMBIGUITY_ROUTING'),('Route CON-004 state-token versus prose admissibility to the owning content-minimality decision instrument; preserve the separate generated-view restriction and do not broaden permitted content.', 'DEL-01-03','Accepted boundary definition and claim-specific content-minimal evidence; scope change if permitted content changes.','HELD_AMBIGUITY_ROUTING'),('Route CON-005 meaning of a rebuild completed with coverage limitations versus SOW-010 in full for an owner interpretation; preserve honest limitation reporting and the narrower receipts-parser contract.', 'NONE','Accepted interpretation bound to SOW-010, REQ-001/009 and upstream limitation placement; no invented full-coverage guarantee.','HELD_AMBIGUITY_ROUTING')]
for i,(text,dep,closure,kind) in enumerate(resdefs,1):
 residuals.append(dict(zip(RHEADER,[f'DEL-03-01-REM-{i:03}','DEL-03-01','',text,dep,gate,closure,'PEC owner under D82 exclusion of application/repair; owning source/scope-change instrument as applicable',sel,kind])))
for m in matches:
 local=m[1];kind=local.split('-')[0];num=int(local[-3:]);line=sow[:m.start()].count('\n')+1
 c={k:'' for k in HEADER};c.update(ClaimID='DEL-03-01::'+local,DeliverableID='DEL-03-01',ClaimClass='DOCUMENTARY_ALIGNMENT',NormativeSource=str(S)+'#'+local,ScopeItemIDs='SOW-010;SOW-021',DeclaredSource=str(S)+':'+str(line),CurrentState=m[2],ImplementationEvidence='Not a product execution assertion. Current v2 inventory does not demonstrate this downstream reconciler.',VerificationEvidence='Accepted contract-level REVIEW with exact unchanged SOW hash; no product test PASS inferred.',ValidationOrProvenanceEvidence=str(D/'_REVIEW.md')+'#Exact-byte acceptance and remaining gates; exact hash reproduced.',LifecycleEvidence=str(D/'_STATUS.md')+'#Current State: INITIALIZED',ExistingRemaining='No ## Remaining section in current _STATUS.md; not warranted NONE.',Disposition='ALIGNED',ProposedResidualID='NONE',ProposedResidualText='NONE',Depends='NONE',ExactGate=gate,AuthorityNeeded='No new documentary act; future application/production requires owning owner ruling.',Selectability=sel,SourceCommit=BASE,SourceHashes=json.dumps({str(S):hashes[str(S)],str(D/'_REVIEW.md'):hashes[str(D/'_REVIEW.md')],str(D/'_STATUS.md'):hashes[str(D/'_STATUS.md')]},sort_keys=True),EvidenceReferences=str(W/'READ_MANIFEST.json')+';'+str(W/'IMPLEMENTATION_INVENTORY.json'),Notes='Assessment is qualified by ClaimClass; accepted future-contract framing is not implementation or release acceptance.')
 rid=None
 if kind in ['REQ','AC','OUT','VER'] and local!='AC-017':
  c['Disposition']='UNKNOWN';c['ClaimClass']={'REQ':'PRODUCT_REQUIREMENT','AC':'PRODUCT_ACCEPTANCE_CRITERION','OUT':'PRODUCT_OUTPUT','VER':'FINITE_TEST_METHOD'}[kind]
  c['ImplementationEvidence']='Inspected complete current v2 production module symbols (IMPLEMENTATION_INVENTORY.json): registry port/configuration only. Accepted SOW CLM-022 and REVIEW frame this as future production; no source-bound reconciler candidate identified. Bounded observation, not universal absence proof.'
  c['VerificationEvidence']=str(S)+'#VER-'+f'{min(num,16):03}'+': method is declared, not executed evidence. No rebuild run is established by current source or local production run records.'
  c['Notes']='UNKNOWN means implementation/execution evidence unresolved; contract wording and exact acceptance remain valid. Source-name absence alone is not DOCUMENTED_UNIMPLEMENTED.'
  rid=2 if kind=='VER' or local in ['REQ-016','AC-016','OUT-002'] else 1
 if local=='AC-017':c['ClaimClass']='HUMAN_ACCEPTANCE';c['Notes']='Exact current SOW hash equals owner accepted hash. Contract traceability only; Gate5 unentered, no implementation/source acceptance.'
 if local=='TBD-005':rid=3;c['Disposition']='UNKNOWN';c['Notes']='Explicit contract unknown survives registry-home resolution; routing only, no new parser obligation.'
 if local=='CON-004':rid=4;c['Disposition']='UNKNOWN';c['Notes']='Unresolved accepted-boundary interpretation; upstream guard cannot alone prove generated-view compliance.'
 if local=='CON-005':rid=5;c['Disposition']='UNKNOWN';c['Notes']='In-full interpretation unresolved. CLM-016 explicitly preserves narrower DEL-02-03 absence reporting; no silent uniformity.'
 if local in ['CLM-011','CLM-022','AX-011','AX-013','CON-003']:
  c['Notes']='Accepted production-contract framing, not a current assertion that all upstream code is absent. Current registry adapter/port exists; INITIALIZED statuses unchanged. OI-012 resolution belongs to DEL-00-01 ADR; no currency repair or reopening inferred.'
 if local in ['TBD-001','TBD-002','TBD-003','TBD-004','CON-001']:c['Notes']='Truthful documented assignment/production choice; no automatic administrative Remaining mirror and no invented product obligation.'
 if rid:
  r=residuals[rid-1];c.update(ProposedResidualID=r['ResidualID'],ProposedResidualText=r['ProposedText'],Depends=r['Depends'],AuthorityNeeded=r['AuthorityNeeded']);r['ClaimIDs']+=(';' if r['ClaimIDs'] else '')+c['ClaimID']
 claims.append(c)
for local,cls,desc in [('LIFECYCLE','LIFECYCLE','INITIALIZED unchanged; Gate5 not entered.'),('EXACT_ACCEPTANCE','HUMAN_ACCEPTANCE','Owner ACCEPT_EXACT_BYTES applies only to current ScopeOfWork.md hash, not implementation.'),('RELEASE_BOUNDARY','RELEASE','DEL-10-02 kill gate, DEL-01-05 enforcement and professional reliance are explicitly not discharged here.')]:
 c=claims[0].copy();c.update(ClaimID='DEL-03-01::'+local,ClaimClass=cls,NormativeSource=str(D/'_REVIEW.md')+'#Exact-byte acceptance and remaining gates',DeclaredSource=str(D/'_REVIEW.md'),CurrentState=desc,Notes='Run-local explicit section mapping; no invented stable production ID.');claims.append(c)
for name,header,rows in [('CLAIMS.csv',HEADER,claims),('RESIDUALS.csv',RHEADER,residuals)]:
 with (W/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=header,lineterminator='\n');w.writeheader();w.writerows(rows)
counts={x:sum(c['Disposition']==x for c in claims) for x in ['ALIGNED','UNKNOWN']}
# Rehash all input bytes and prove tracked current inputs against exact base.
unchanged=all(hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in hashes.items())
checks.append(dict(command='source hash comparison against frozen package SOURCE_MANIFEST and final input reread',cwd='.',environment={},exit_code=0,result={'frozen_mismatches':mismatches,'source_unchanged':unchanged,'accepted_sow_sha256':hashes[str(S)],'local_definitions':len(matches),'counts':counts}))
manifest={'source_commit':BASE,'hashes':hashes,'historical_sources':[],'checks':checks,'source_unchanged':unchanged}
(W/'READ_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
(W/'COVERAGE.md').write_text('# DEL-03-01 claim coverage\n\nASSESSMENT: ASSESSED_UNKNOWN. Derivative reporting against D82 base '+BASE+'.\n\nAll 96 local own-voice definitions are covered exactly once: OUT2, REQ16, AC17, VER16, CLM22, AX13, TBD5, CON5. Three run-local section claims separately preserve lifecycle, exact artifact acceptance and release boundaries. Quoted upstream identifiers, register edge IDs and SOW/OBJ IDs are source context, not duplicated local definitions. Source lines are recorded per row. No missing contract fallback is needed.\n\n'+str(counts)+'; 99 total claims; five residual proposals (two conditional evidence/production candidates, three held ambiguity routes). UNKNOWN prohibits NONE. All proposals remain nonselectable. No status field was changed.\n\nImplementation inspection covers every current v2 production module and enumerates all v2 source/test files. The positive operation surfaces are typed registry and JSON configuration; no downstream rebuild is demonstrated. Future-production SOW and contract-only REVIEW are corroborating but dated statements. Product evidence is therefore UNKNOWN rather than inferred absent from a filename miss. Finite methods are declared and their execution is UNKNOWN; no current finite PASS was claimed or broad suite gratuitously rerun.\n\nDocumentary CLM/AX rows are evaluated as accepted contractual mappings and framing, qualified explicitly where older no-artifact prose would be false as a global present-day assertion. Current upstream INITIALIZED does not mean no upstream code. Exact SOW acceptance persists at unchanged hash; it is not implementation or Gate5 acceptance.\n\nCross-package routing: DEL-02-07 loop-to-project mapping (TBD-005), DEL-01-03 prose/state-token boundary (CON-004), DEL-02-03 narrower absent-feed placement (CLM-016), and PEC owner meaning of in full (CON-005). Do not route TM023 as an unrelated blanket downstream gate. D79/PRDv2.3 are not applied; ordinary SCA004 currency is not reopened.\n\nDependencies: eleven ACTIVE PREREQUISITE rows remain PENDING and require INITIALIZED; exact target IDs are attached only to production/evidence candidates, plus source-grounded upstream ambiguity targets. Documentary rows use NONE. Observed predecessor state never flips the register. C05 chronology does not create a fresh pre-P1 blocker after closure; P1 production remains packet-gated.\n')
print(json.dumps({'claims':len(claims),'residuals':len(residuals),'counts':counts,'sources':len(hashes)},indent=2))
