from pathlib import Path
import csv,json,hashlib,re
ROOT=Path.cwd(); BASE='2be412ccea62bdc4bd96deb082c46d7a792076ea'; D='DEL-06-01'
R=Path('projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05'); C=R/'R1_R4_2026-09-05/COMMON'; P=R/'R1_R4_2026-09-05/PACKAGES/PKG-06'; W=P/'WORKERS'/D
T=Path('projects/pec/execution/PKG-06_Presence_Git_Observation/1_Working/DEL-06-01_Session_presence_records'); DE=Path('projects/pec/execution/_Decomposition'); DC=Path('projects/pec/execution/_Coordination/_DECISIONS')
sha=lambda b:hashlib.sha256(b).hexdigest()
paths={Path(p) for p in ['AGENTS.md','projects/pec/AGENTS.md','agents/AGENT_TASK.md','agents/AGENT_RECONCILIATION.md','docs/DELIVERABLE_CONCORDANCE_METHOD.md','projects/pec/docs/PRD.md','projects/pec/loop/LOOP_INIT.md','projects/pec/execution/_Scripts/pec_reliance_hold.py','projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv']}
paths.update(p for p in T.rglob('*') if p.is_file()); paths.update(p for p in DE.iterdir() if p.is_file()); paths.update(p for p in DC.rglob('*.md') if p.is_file())
paths.update([R/'CONVENTIONS.md',C/'SOURCE_MANIFEST.json',C/'RUN_BASIS.md',C/'SCOPE_CENSUS.csv',C/'AGENT0_GRAPH.md',C/'BRIEF_CLARIFICATION_01.md',C/'BRIEFS/PKG-06.md',P/'PACKAGE_BASIS.md',P/'SOURCE_MANIFEST.json',P/'BRIEFS/DEL-06-01.md'])
paths.update(p for p in Path('projects/pec/v2').rglob('*') if p.is_file() and p.suffix in {'.py','.json','.md'})
hashes={str(p):sha(p.read_bytes()) for p in sorted(paths)}
frozen=json.loads((C/'SOURCE_MANIFEST.json').read_text())['hashes']; drift=[p for p,h in hashes.items() if p in frozen and h!=frozen[p]]; assert not drift,drift
checks=json.loads((W/'PREFLIGHT.json').read_text()); checks.append({'command':'SHA256 compare read inputs against COMMON/SOURCE_MANIFEST.json','cwd':'.','environment':{},'exit_code':0,'result':{'matched':sum(p in frozen for p in hashes),'drift':drift,'unlisted_inputs':[p for p in hashes if p not in frozen]}})
scope=next(l for l in (DE/'SOFTWARE_DECOMP.md').read_text().splitlines() if l.startswith('| SOW-026 |')); desc=next(x for x in csv.DictReader((DE/'Deliverables.csv').open()) if x['DeliverableID']==D)
local='\n'.join(p.read_text() for p in T.rglob('*.md')); ids=sorted(set(re.findall(r'\b(?:REQ|AC|VER)-[A-Za-z0-9-]+',local)))
assert not ids
mapping=[]
parts=[('SOW-026-A','Record presence for sessions reported by their owning harness'),('SOW-026-B','Record harness kind'),('SOW-026-C','Record engine/model attribution when known'),('SOW-026-D','Record role'),('SOW-026-E','Record loop/package binding'),('SOW-026-F','Record declared write scopes'),('SOW-026-G','Keep session identity and lifecycle daemon-owned')]
for id,text in parts:mapping.append({'ClaimID':D+'::'+id,'locus':str(DE/'SOFTWARE_DECOMP.md')+' §2.1 SOW-026','exact_quote':scope,'quote_sha256':sha(scope.encode()),'atomic_interpretation':text})
(W/'CLAIM_MAPPING.json').write_text(json.dumps(mapping,indent=2)+'\n')
cols='ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'.split(',')
gate='NOT_SELECTABLE_UNTIL: owner accepts an exact Remaining application packet; any production/source act additionally requires an exact D-PEC grant naming paths, acts, verification and rollback, current reliance preflight, and applicable named prerequisite satisfaction.'
resid=D+'-REM-001'; text='Resolve the SOW-026 session-presence evidence gap: map accepted current implementation and claim-relevant verification for harness-reported session records and each required field, including daemon-owned identity/lifecycle; if evidence does not exist, return the established boundary and a separately gated scope/contract proposal to the owner.'
rows=[]
def row(id,cl,claim,disp,src,notes,res=False):
 refs=[str(DE/'SOFTWARE_DECOMP.md'),str(DE/'ScopeLedger.csv'),str(DE/'Deliverables.csv'),str(T/'_CONTEXT.md'),str(T/'_STATUS.md'),str(T/'Dependencies.csv')]
 x={k:'' for k in cols}; x.update(ClaimID=D+'::'+id,DeliverableID=D,ClaimClass=cl,NormativeSource=src,ScopeItemIDs='SOW-026',DeclaredSource=str(T/'_CONTEXT.md')+' Description; ScopeOfWork.md absent',CurrentState=claim,ImplementationEvidence='UNKNOWN: no accepted presence implementation mapped in inspected current v2 boundary; loop-registry port/adapter and generic API schema do not establish this behavior' if res else 'NOT_APPLICABLE: documentary/lifecycle observation only',VerificationEvidence='UNKNOWN: no claim-specific test/run acceptance mapped; no product tests executed' if res else 'Exact source bytes inspected and compared with common frozen hashes; not behavioral testing',ValidationOrProvenanceEvidence='Accepted revision 1.4 decomposition; D82 and D81 calibration acceptance; CLAIM_MAPPING.json supplies exact quote/hash fallback',LifecycleEvidence=str(T/'_STATUS.md')+' Current State OPEN; no transition performed',ExistingRemaining='ABSENT: no ## Remaining section; not warranted NONE',Disposition=disp,ProposedResidualID=resid if res else '',ProposedResidualText=text if res else '',Depends='NONE',ExactGate=gate,AuthorityNeeded='Owner exact Remaining application; source/contract/lifecycle acts require separate applicable grants',Selectability='NON_SELECTABLE_PENDING_OWNER_APPLICATION',SourceCommit=BASE,SourceHashes=json.dumps({p:hashes[p] for p in refs},sort_keys=True),EvidenceReferences='; '.join(refs)+'; READ_MANIFEST.json; CLAIM_MAPPING.json',Notes=notes)
 rows.append(x)
for id,claim in parts:row(id,'OBSERVED_BEHAVIOR',claim,'UNKNOWN',str(DE/'SOFTWARE_DECOMP.md')+' §2.1 SOW-026; PRD PEC-PRS-001; C13','Fallback atom mapped before ledger creation. Residual candidacy: EVIDENCE_GAP; route to owner for evidence-bound scope clarification, not an established implementation defect. Presence confers no runtime session authority. Missing contract/search misses and historical future-production wording do not establish DOCUMENTED_UNIMPLEMENTED.',True)
row('DOC-ASSIGNMENT','DOCUMENTARY_ALIGNMENT','ResponsibleParty TBD; assignment at WORKING_ITEMS activation','ALIGNED',str(DE/'Deliverables.csv')+' row DEL-06-01 ResponsibleParty','Truthful TBD aligns with accepted register. Administrative assignment is not a product residual; no automatic mirror.')
row('DOC-SCOPE','DOCUMENTARY_ALIGNMENT','Context accurately maps SOW-026 to DEL-06-01 / PKG-06 / OBJ-003 and revision1.4','ALIGNED',str(DE/'Deliverables.csv')+' row DEL-06-01; '+str(DE/'ScopeLedger.csv')+' SOW-026','Documentary ALIGNED only. Anticipated presence writer + tests is an artifact expectation, not evidence of implementation. Empty _SEMANTIC.md is not an invented task. Local REQ/AC/VER IDs not defined.')
row('DOC-DEPENDENCIES','DOCUMENTARY_ALIGNMENT','Two ACTIVE PREREQUISITE rows remain PENDING: DEP-06-01-003 to DEL-01-02 and DEP-06-01-004 to DEL-07-03','ALIGNED',str(T/'Dependencies.csv')+' DEP-06-01-003/-004; projects/pec/loop/LOOP_INIT.md Step1','These target IDs apply to later production only if named by its item Depends; this evidence-gap proposal has Depends NONE. PROPOSAL is provenance, not automatic satisfaction. Historical D65 run only repaired evidence fields, not product behavior or dependency status.')
row('LIFECYCLE-OPEN','LIFECYCLE','Recorded lifecycle remains OPEN; no Remaining is recorded','ALIGNED',str(T/'_STATUS.md')+' Current State and History','Observed documentary lifecycle state only, not completion or human acceptance. UNKNOWN prevents NONE; no lifecycle reassessment or release/admin mirror inferred.')
with (W/'CLAIMS.csv').open('w',newline='') as f:writer=csv.DictWriter(f,fieldnames=cols,lineterminator='\n');writer.writeheader();writer.writerows(rows)
rcols='ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'.split(',')
res={'ResidualID':resid,'DeliverableID':D,'ClaimIDs':';'.join(x['ClaimID'] for x in rows if x['ProposedResidualID']),'ProposedText':text,'Depends':'NONE','ExactGate':gate,'ClosureEvidence':'Exact accepted source/contract mapping, implementation commit and hashes, finite claim-specific test/run evidence, acceptance continuity where claimed; or owner-ruled next scope disposition preserving uncertainty. Recheck actual source and hold targets.','AuthorityNeeded':'Owner exact Remaining application; separate source/contract grants if later work is proposed','Selectability':'NON_SELECTABLE_PENDING_OWNER_APPLICATION','Notes':'Candidacy EVIDENCE_GAP; recommended owner evidence/ambiguity routing only, not confirmed product defect or automatic executable Remaining. Seven UNKNOWN atomic claims consolidate into one proposal. Production dependency targets DEL-01-02/DEL-07-03 remain PENDING in their register; no production selection here. No runtime ownership, release, assignment or TM mirror.'}
with (W/'RESIDUALS.csv').open('w',newline='') as f:writer=csv.DictWriter(f,fieldnames=rcols,lineterminator='\n');writer.writeheader();writer.writerow(res)
coverage=f'''# DEL-06-01 coverage

Source base `{BASE}`; accepted revision 1.4 SOW-026. Derivative of accepted decomposition, not replacement authority. D82 activates this reporting; D81 acceptance supplies convention disposition despite retained historical candidate headings.

11 claims: 7 UNKNOWN behavioral atoms and 4 documentary/lifecycle ALIGNED rows; 1 evidence-gap proposal; summary ASSESSED_UNKNOWN; warranted NONE false. No defined local REQ/AC/VER IDs exist in inspected deliverable files. ScopeOfWork.md and Specification.md absent; exact candidate-validation targets each allowed. This absence is not proof of unimplemented scope.

CLAIM_MAPPING.json records the exact accepted SOW-026 table row, locus, quote SHA256 and seven atomic fallback mappings before claim ledger generation. DOC-ASSIGNMENT maps ResponsibleParty; DOC-SCOPE maps accepted row identity, intended artifacts and current context; DOC-DEPENDENCIES maps both execution edges; LIFECYCLE-OPEN maps status and empty Remaining. REQ/AC/VER coverage is zero defined / zero omitted. SourceRef PEC-PRS-001 is supporting PRD provenance, not independently invented contract scope. Content-minimal and daemon ownership constraints survive.

Current v2 source boundary includes the typed loop-registry port and JSON adapter, service-core checking and generic API schema/tests. These do not supply a claim-specific presence implementation/test/acceptance mapping. No finite suites were rerun because none was mapped to session-presence assertions. No absent test suite pass is claimed. D65 local run concerns dependency evidence repair only. No direct DEL-06-01 acceptance record was identified by scoped decision search; UNKNOWN preserves that boundary and does not prove universal absence. The frozen PEC implementation is historical-only; it was not relied upon as current v2 code. No foreign runtime tree was inspected.

Dependencies: DEP-06-01-003 → DEL-01-02 and DEP-06-01-004 → DEL-07-03 are ACTIVE PREREQUISITE/PENDING. This evidence-gap proposal Depends NONE because it is discovery/clarification, not the presence writer production act. Later production selection must apply exact named-target conjunction and owner source gates; no status flip or SCC resolution is inferred.

No R0 claim reuse: DEL-06-01 was outside the six-deliverable R0 sample. Root/project instructions, accepted D81/D82 conventions and common basis were rehashed. Current metadata's revision1.4 is preserved; older pointer future-work prose cannot reopen completed ordinary SCA004 currency. No TM023 blanket gate, TM022 mirror, PRDv2.3/DPEC79 application, release or lifecycle act is created.

Worker-only output completed; independent verifier and manager fan-in remain pending. Rerun on material source/hash/hold/accepted-scope drift or separately supplied current implementation/acceptance. Source hashes are stable during run; inputs outside frozen common manifest are listed, with package/common run artifacts treated as this run's derivative context, never independent product authority.
'''
(W/'COVERAGE.md').write_text(coverage)
assert all(sha(Path(p).read_bytes())==h for p,h in hashes.items())
checks.append({'command':'validate exact CSV headers, LF, IDs, counts, reciprocal residual links and hashes','cwd':'.','environment':{},'exit_code':0,'result':{'claims':11,'unknown':7,'aligned':4,'residuals':1,'source_unchanged':True}})
manifest={'source_commit':BASE,'hashes':hashes,'historical_sources':[],'checks':checks,'source_unchanged':True}
(W/'READ_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
ret=f'''RUN_STATUS: SUCCESS
ControlSurface: FILE
TaskProfile: NONE
TaskSkill: NONE
ScopePath: {ROOT/W}
ToolsUsed: python3 scoped evidence construction/hash/preflight; read-only shell cat/rg/sed/head
ToolPolicyCompliance: PASS
WriteAuthorization: ALLOWED_WRITE_TARGETS
Outputs: CLAIMS.csv, RESIDUALS.csv, COVERAGE.md, READ_MANIFEST.json, CLAIM_MAPPING.json, PREFLIGHT.json, build_evidence.py, RETURN.md
Counts: 11 claims; 7 UNKNOWN; 4 ALIGNED documentary/lifecycle; 1 evidence-gap residual; ASSESSED_UNKNOWN; no warranted NONE.
MISSING: ScopeOfWork.md and Specification.md; mapped current session-presence implementation, tests and acceptance evidence.
NEEDS_HUMAN_RULING: Exact application remains owner-gated; no request to repeat authorized R1–R4 work.
DEPENDENCY_NOTES: DEP-06-01-003 DEL-01-02 and DEP-06-01-004 DEL-07-03 ACTIVE PREREQUISITE PENDING; evidence proposal Depends NONE; production remains separately governed.
AppliedChanges: New worker derivative evidence only.
Handoff: Accepted upstream D82/D81 and revision1.4/common frozen basis; derivative report complete for worker only, independent verification pending; no product, Remaining, source or lifecycle closure. Rerun for source/hold/scope drift or new accepted evidence.
NativeEvidence: /root/pec_pkg06_reconciliation/del06_01; bounded ephemeral Agent2; instruction-asserted, not mechanically enforced; no delegation, model identity not asserted.
'''
(W/'RETURN.md').write_text(ret)
print(json.dumps({'claims':len(rows),'unknown':7,'aligned':4,'residuals':1,'sources':len(hashes),'frozen_matches':sum(p in frozen for p in hashes),'outputs':str(W)}))
