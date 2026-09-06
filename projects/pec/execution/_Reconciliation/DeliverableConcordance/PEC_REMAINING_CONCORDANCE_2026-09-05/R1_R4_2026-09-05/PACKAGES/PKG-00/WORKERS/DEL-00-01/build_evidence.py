from pathlib import Path
import hashlib,json,csv,re,subprocess,os
root=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip());os.chdir(root)
base='2be412ccea62bdc4bd96deb082c46d7a792076ea'
run=Path('projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05');pkg=run/'R1_R4_2026-09-05/PACKAGES/PKG-00';out=pkg/'WORKERS/DEL-00-01'
d=Path('projects/pec/execution/PKG-00_Architecture_Runway_Contracts/1_Working/DEL-00-01_v2_first_ADRs_core_isolation_carried_postures');co=Path('projects/pec/execution/_Coordination');dec=co/'_DECISIONS';decomp=Path('projects/pec/execution/_Decomposition');a=co/'D-PEC-72_P1_ENTRY_FOUNDATION_2026-08-01'
sha=lambda b:hashlib.sha256(b).hexdigest()
paths=[Path(x) for x in ['AGENTS.md','projects/pec/AGENTS.md','agents/AGENT_RECONCILIATION.md','docs/DELIVERABLE_CONCORDANCE_METHOD.md','projects/pec/loop/LOOP_INIT.md','projects/pec/docs/PRD.md','projects/pec/docs/.archive/adr/ADR.md']]
paths += [run/'CONVENTIONS.md',run/'SAMPLE_SUMMARY.csv',pkg/'PACKAGE_BASIS.md',pkg/'SOURCE_MANIFEST.json',pkg/'BRIEFS/DEL-00-01.md']
paths += [run/'R1_R4_2026-09-05/COMMON'/f for f in ['RUN_BASIS.md','SOURCE_MANIFEST.json','SCOPE_CENSUS.csv','AGENT0_GRAPH.md']]
paths += list(p for p in d.rglob('*') if p.is_file())
paths += [dec/f for f in ['D-PEC-81_CALIBRATION_ACCEPTANCE_2026-09-05.md','D-PEC-82_remaining_corpus_reporting_2026-09-05.md','D-PEC-72_p1_entry_foundation_slice.md','D-PEC-58_prd_v2_adoption.md','_REGISTER.md']]
paths += [decomp/f for f in ['SOFTWARE_DECOMP.md','ScopeLedger.csv','Deliverables.csv','_LATEST.md']]
paths += [a/f for f in ['ARTIFACT_ACCEPTANCE_AND_DEL10_REPAIR_RULING_2026-08-01.md','C05_CLOSURE_RULING_2026-08-01.md','REVIEW_GATE_RULING_2026-08-01.md','FINALIZATION_AUTHORIZATION_2026-08-01.md','HANDOFF.md']]
paths += [co/'ACTIVE_RELIANCE_HOLDS.csv',co/'PLAN_2026-07-25_project_setup_dag_gate.md',co/'PEC_CURRENCY_REPAIR_CLOSEOUT_2026-08-09/HANDOFF_STATE.md',Path('projects/pec/execution/_Scripts/pec_reliance_hold.py')]
paths=sorted(set(paths));texts={str(p):p.read_text() for p in paths};hashes={str(p):sha(p.read_bytes()) for p in paths}
checks=[]
def check(argv):
 r=subprocess.run(argv,text=True,capture_output=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1','PYTHONPYCACHEPREFIX':'/tmp/pec-del0001-pycache'});checks.append(dict(command=' '.join(argv),cwd=str(root),environment={'PYTHONDONTWRITEBYTECODE':'1','PYTHONPYCACHEPREFIX':'/tmp/pec-del0001-pycache'},exit_code=r.returncode,result=r.stdout+r.stderr));return r
for target in ['ScopeOfWork.md','_STATUS.md','artifacts/v2/ADRs.md']:
 r=check(['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register',str(co/'ACTIVE_RELIANCE_HOLDS.csv'),'--target',str(d/target).removeprefix('projects/pec/'),'--operation','candidate-validation']);assert r.returncode==0
assert check(['git','rev-parse','HEAD']).stdout.strip()==base
assert check(['git','rev-parse','origin/main']).stdout.strip()==base
for p in [d/'artifacts/v2/ADRs.md',d/'ScopeOfWork.md',a/'ARTIFACT_ACCEPTANCE_AND_DEL10_REPAIR_RULING_2026-08-01.md']:
 r=check(['git','show',f'origin/main:{p}']);assert r.returncode==0 and sha(r.stdout.encode())==hashes[str(p)]
r=check(['git','show','--format=','--name-only','5942c50333c5cbd1e9b77e72c79c11bf46051040']);assert r.returncode==0 and all(s.startswith('projects/pec/execution/PKG-00_') for s in r.stdout.splitlines() if s)
assert hashes[str(d/'artifacts/v2/ADRs.md')]=='f63ecc2725b26e0e78be993a7902ad5b901cdfbb2e7921a19fc3442c9d785db5'
assert hashes[str(d/'ScopeOfWork.md')]=='4334615044448441780c818ec7badf5ca55a4a6cf30b3ff19d11bf3049b21740'
common=json.loads(texts[str(run/'R1_R4_2026-09-05/COMMON/SOURCE_MANIFEST.json')]); ch=common.get('hashes',{})
drift=[p for p in hashes if p in ch and ch[p]!=hashes[p]];assert not drift
claims=[];contract=texts[str(d/'ScopeOfWork.md')];defs=re.findall(r'^- \*\*([A-Z]+-\d+)\*\* — (.*)$',contract,re.M)
notes={
'REQ-001':'ADR-PEC-V2-001 selects one hexagonal boundary and explicitly Resolves OI-012.',
'REQ-002':'Context derives from accepted invariants and package grain; Decision items cite existing service/schema obligations. This source-from-basis requirement does not itself demand exhaustive reproduction; AC-002 separately does.',
'REQ-003':'ADR-PEC-V2-002 Carried posture item1 names ADR-002, PEC-SVC-001 and SOW-052; archived heading resolves.',
'REQ-004':'ADR-PEC-V2-002 items2–4 explicitly retire old allocation and preserve optional-client/no-second-loop/human-only-act boundary.',
'REQ-005':'ADR-PEC-V2-002 Context and Consequences make archived corpus historical and ADR-002 sole live carried posture.',
'REQ-006':'ADR-PEC-V2-001 Decision item6 supplies entity-domain meaning versus physical persistence classification.',
'REQ-007':'ADR-PEC-V2-001 Non-decisions explicitly preserves OI-001..009 and OI-013; later owner OI-003 decision is not a decision by this ADR.',
'REQ-008':'D-PEC-72 Exact O-A/O-B production fence names current artifact path; it exists.',
'REQ-009':'Published artifact is referenceable in place. E-N18/E-P01 remain PROPOSAL and first LOW_CONFIDENCE; production commit is PKG-00-contained. No consumer duty inferred.',
'REQ-010':'ADR Context graceful absence and file-native authority plus no second loop and owner exact confirmation support documentary absence posture; not a runtime kill-test claim.',
'AC-001':'Exactly one core-isolation decision record (ADR-PEC-V2-001); second record carries postures.',
'AC-002':'Narrow context-reproduction gap: no statement preserves the recorded rationale that nearly all §16 open decisions are adapter-level and isolation keeps them open cheaply. Context supplies package grain, Decision7 leaves contract home unresolved, Alternatives supplies lighter functional core, Non-decisions preserves issues, and Consequences describes adapter replacement. These are related but do not convey the classification of the §16 decision population or its cheap-deferral rationale. See GAP_ANALYSIS.md. Exact AC-007 acceptance remains valid; this assessment is not an owner reversal.',
'AC-003':'ADR-PEC-V2-002 items1–4 and Consequences carry precisely the live/historical boundary.',
'AC-004':'ADR self-resolves OI-012 and decides no other issue; current decomposition disposition still routes OI-012 decision to this ADR. Register correction expressly excluded by AC-004.',
'AC-005':'Decision6 contains operational candidate-change classification rule.',
'AC-006':'Exact packet path exists; git show of production commit5942c50333c5cbd1e9b77e72c79c11bf46051040 confirms PKG-00-only changed paths.',
'AC-007':'Separate owner ruling on origin/main accepts exact current f63ecc... bytes, hexagonal style and graceful absence. Lifecycle/ISSUED/release and acceptance of changed bytes excluded.',
'VER-001':'Document-inspection method executed in current assessment, with AC-002 finding; historical candidate PASS is bound to be300... candidate and final SELF_CHECK to f63ecc... . Method availability/execution is not a blanket pass of every criterion.',
'VER-002':'Current historical headings ADR-002 and ADR-014 resolve; entire ADR inspected for sole-live-posture/historical allocation distinction.',
'VER-003':'Current complete ADR inspected against OI012 and named non-decisions; no register act performed. This is bounded documentary inspection, not all future implementations.',
'VER-004':'Current path existence and exact packet checked; historical production changeset rechecked for containment; downstream PROPOSAL edges require no consumer writes.',
'CLM-001':'Identity/type/envelope/phase and truthful ResponsibleParty TBD match current Deliverables.csv row.',
'CLM-002':'Current accepted row and _CONTEXT description match scope; artifact supplies both outputs.',
'CLM-003':'Packet selects the anticipated ADR markdown artifact class at exact path.',
'CLM-004':'Archived heading and live PRD PEC-SVC-001/SOW052 support carried dependency rule; archived technology allocations not restored.',
'CLM-005':'D58 behavior8 retires adapter allocation; ADR and PRD preserve optional client and human-only boundaries.',
'CLM-006':'Documentary assertion accurately quotes retained OI012 basis; reproducing all that basis in artifact is separate AC002 finding.',
'CLM-007':'Two satisfied anchors and no execution predecessor. E-N18/E-P01 are proposal provenance; no gating authority inferred.',
'CLM-008':'Accepted decomposition DL12 and exact D72 packet preserve disjoint package writes.',
'TBD-001':'Explicitly dated contract unknown resolved by later D72 exact artifact path. Frozen contract not a current missing-path assertion.',
'TBD-002':'ResponsibleParty remains truthfully TBD in activation; owner named no accountable human. Not missing product work.',
'CON-001':'Undecided at contract-writing time; later D72 O-B and AC007 select architecture. Dated statement preserved, no decision reversal.',
'AX-001':'Documentary graceful-absence objective remains unchanged in revision1.4 and exact owner confirmation.',
'AX-002':'Revision1.3 is frozen contract/ADR acceptance provenance; current revision1.4 references and scope checked. SCA004 changes OI003, not SOW088/OBJ005/ADR requirement semantics. No stale-contract repair invented.',
'AX-003':'DL12 governs artifact consumption versus disjoint package writes.',
'AX-004':'Archived source is historical; D58 and ADR carried-posture distinctions match.',
'AX-005':'Contract-time unknowns recorded honestly; architecture/path later ruled, assignment still TBD.',
'AX-006':'Historical lifecycle-neutral production framing at writing; current _STATUS is CHECKING by exact human override. Frozen contract sentence does not reverse later lifecycle.',
'AX-007':'Exhibit E-N18/E-P01 and C10 support proposed/low-confidence, non-gating consumer relation.',
'OUT-001':'Published ADR-PEC-V2-001 decides hexagonal isolation/OI012. AC002 documentary context gap tracked separately.',
'OUT-002':'Published ADR-PEC-V2-002 carries ADR002, historical ADR014 and surviving v2 boundaries.'}
fields='ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'.split(',')
resid='DEL-00-01::R-001';rtext='Owner disposition of the narrow AC-002 context-reproduction gap: determine whether accepted ADR context adequately carries the CLM-006 adapter-level open-decision/cheap-deferral rationale; if clarification is required, authorize exact CHECKING change and corresponding REVIEW rerun against new hashes, preserving existing AC-007 acceptance history.'
for local,quote in defs:
 cl='human_acceptance' if local=='AC-007' else 'finite_test_method' if local.startswith('VER') else 'documentary_alignment'
 disposition='PARTIALLY_IMPLEMENTED' if local=='AC-002' else 'ALIGNED'
 ev=[d/'ScopeOfWork.md',d/'artifacts/v2/ADRs.md',d/'_REVIEW.md',d/'_STATUS.md',decomp/'SOFTWARE_DECOMP.md',decomp/'ScopeLedger.csv',decomp/'Deliverables.csv',dec/'D-PEC-72_p1_entry_foundation_slice.md']
 if local=='AC-007':ev+=[a/'ARTIFACT_ACCEPTANCE_AND_DEL10_REPAIR_RULING_2026-08-01.md']
 if local in ['CLM-007','AX-007','REQ-009','VER-004']:ev+=[d/'Dependencies.csv',co/'PLAN_2026-07-25_project_setup_dag_gate.md']
 row={k:'' for k in fields};row.update(ClaimID='DEL-00-01::'+local,DeliverableID='DEL-00-01',ClaimClass=cl,NormativeSource=str(d/'ScopeOfWork.md')+'#'+local,ScopeItemIDs='SOW-088',DeclaredSource=quote,CurrentState='CHECKING; current artifact owner accepted at exact hash',ImplementationEvidence=str(d/'artifacts/v2/ADRs.md')+'; '+notes[local],VerificationEvidence=str(d/'_REVIEW.md')+'; current bounded inspection; READ_MANIFEST.json checks',ValidationOrProvenanceEvidence=str(a/'ARTIFACT_ACCEPTANCE_AND_DEL10_REPAIR_RULING_2026-08-01.md')+'; D72 O-B; historical production/finalization chain preserved',LifecycleEvidence=str(d/'_STATUS.md')+'; '+str(a/'C05_CLOSURE_RULING_2026-08-01.md'),ExistingRemaining='No ## Remaining section present; not independent evidence of warranted NONE',Disposition=disposition,Selectability='NON_SELECTABLE_PENDING_OWNER_APPLICATION',SourceCommit=base,SourceHashes=';'.join(str(p)+'='+hashes[str(p)] for p in ev),EvidenceReferences=';'.join(map(str,ev)),Notes=notes[local]+' Source quote SHA256='+sha(quote.encode()))
 if local=='AC-002':row.update(ProposedResidualID=resid,ProposedResidualText=rtext,Depends='NONE',ExactGate='Owner interpretation/acceptance disposition; any edit requires exact CHECKING change authorization and REVIEW against resulting hashes',AuthorityNeeded='PEC owner; governing CHECKING change path; no current repair grant')
 claims.append(row)
for local,cl,txt,ev in [('LIFECYCLE','lifecycle','CHECKING is preserved; owner Gate5 override never ISSUED.',d/'_STATUS.md'),('C05','human_acceptance','C05 CLOSED by separate subsequent owner act; earlier D72 candidate/acceptance statements that it remains open are dated chronology. Closure confers no P1/source/release authority.',a/'C05_CLOSURE_RULING_2026-08-01.md')]:
 row={k:'' for k in fields};row.update(ClaimID='DEL-00-01::'+local,DeliverableID='DEL-00-01',ClaimClass=cl,NormativeSource=str(ev),ScopeItemIDs='SOW-088',DeclaredSource=txt,CurrentState=txt,ImplementationEvidence='N/A: human authority/lifecycle claim',VerificationEvidence='Exact current owner/status source read and hashed',ValidationOrProvenanceEvidence=str(ev),LifecycleEvidence=str(d/'_STATUS.md'),ExistingRemaining='No section present',Disposition='ALIGNED',Selectability='NON_SELECTABLE_PENDING_OWNER_APPLICATION',SourceCommit=base,SourceHashes=str(ev)+'='+hashes[str(ev)],EvidenceReferences=str(ev),Notes='Source-grounded additional run-local ID; no missing-contract fallback.');claims.append(row)
with (out/'CLAIMS.csv').open('w',newline='') as f:w=csv.DictWriter(f,fields,lineterminator='\n');w.writeheader();w.writerows(claims)
rf='ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'.split(',')
with (out/'RESIDUALS.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,rf,lineterminator='\n');w.writeheader();w.writerow(dict(ResidualID=resid,DeliverableID='DEL-00-01',ClaimIDs='DEL-00-01::AC-002',ProposedText=rtext,Depends='NONE',ExactGate='Owner interpretation/acceptance disposition; separate exact CHECKING change authorization before any edit',ClosureEvidence='Owner disposition bound to unchanged artifact, or exact authorized new artifact + semantic AC002 backcheck and REVIEW/owner acceptance as applicable',AuthorityNeeded='PEC owner; frozen CHECKING change path',Selectability='NON_SELECTABLE_PENDING_OWNER_APPLICATION',Notes='Held owner interpretation/documentary gap; not selected product implementation; existing exact AC007 acceptance remains valid and no lifecycle reversal is inferred.'))
manifest=dict(source_commit=base,hashes=hashes,historical_sources=[],checks=checks,source_unchanged=all(sha(Path(p).read_bytes())==h for p,h in hashes.items()))
(out/'READ_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'claims':len(claims),'defined_ids':len(defs),'hashes':len(hashes),'partial':1,'unknown':0,'checks':len(checks),'source_unchanged':manifest['source_unchanged']}))
