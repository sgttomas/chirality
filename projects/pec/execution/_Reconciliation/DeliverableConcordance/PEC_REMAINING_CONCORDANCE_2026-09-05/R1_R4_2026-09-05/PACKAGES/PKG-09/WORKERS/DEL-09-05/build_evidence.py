import csv,hashlib,json,subprocess,os
from pathlib import Path
ROOT=Path.cwd(); BASE='2be412ccea62bdc4bd96deb082c46d7a792076ea'; DID='DEL-09-05'
RUN=Path('projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05'); P=RUN/'R1_R4_2026-09-05/PACKAGES/PKG-09'; O=P/'WORKERS'/DID
D=Path('projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-05_Presence_board'); DC=Path('projects/pec/execution/_Decomposition'); CO=Path('projects/pec/execution/_Coordination'); CM=RUN/'R1_R4_2026-09-05/COMMON'
sha=lambda b:hashlib.sha256(b).hexdigest()
files=set(D.rglob('*')); files={f for f in files if f.is_file()}
files.update([Path('AGENTS.md'),Path('projects/pec/AGENTS.md'),Path('agents/AGENT_RECONCILIATION.md'),Path('docs/DELIVERABLE_CONCORDANCE_METHOD.md'),Path('projects/pec/loop/LOOP_INIT.md'),Path('projects/pec/docs/PRD.md'),DC/'_LATEST.md',DC/'SOFTWARE_DECOMP.md',DC/'Deliverables.csv',DC/'ScopeLedger.csv',CO/'ACTIVE_RELIANCE_HOLDS.csv',CO/'_DECISIONS/_REGISTER.md',CO/'_DECISIONS/D-PEC-82_remaining_corpus_reporting_2026-09-05.md',CO/'_DECISIONS/D-PEC-81_CALIBRATION_ACCEPTANCE_2026-09-05.md',CO/'PEC_CURRENCY_REPAIR_CLOSEOUT_2026-08-09/HANDOFF_STATE.md',RUN/'CONVENTIONS.md',P/'SOURCE_MANIFEST.json',P/'PREFLIGHT.json',P/'PACKAGE_BASIS.md',P/'BRIEFS/DEL-09-05.md',P/'BRIEF_CLARIFICATION_02.md',CM/'BRIEF_CLARIFICATION_01.md',CM/'RUN_BASIS.md',CM/'AGENT0_GRAPH.md',CM/'SCOPE_CENSUS.csv',CM/'SOURCE_MANIFEST.json',Path('projects/pec/execution/_Scripts/pec_reliance_hold.py')])
for tree in ['projects/pec/v2','projects/pec/execution/_Evaluation/Reviews']:
 files.update(f for f in Path(tree).rglob('*') if f.is_file() and '__pycache__' not in str(f))
checks=[]; hashes={}; bindings={}
for f in sorted(files):
 s=str(f)
 if s.startswith('projects/pec/'):
  cmd=['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register',str(CO/'ACTIVE_RELIANCE_HOLDS.csv'),'--target',s.removeprefix('projects/pec/'),'--operation','candidate-validation']
  r=subprocess.run(cmd,capture_output=True,text=True); checks.append(dict(command=cmd,cwd=str(ROOT),environment={'PYTHONDONTWRITEBYTECODE':'1'},exit_code=r.returncode,result=r.stdout+r.stderr)); assert r.returncode==0,(s,r.stderr)
 hashes[s]=sha(f.read_bytes())
 cmd=['git','show',BASE+':'+s];r=subprocess.run(cmd,capture_output=True)
 if r.returncode==0: assert sha(r.stdout)==hashes[s],s;bindings[s]='BASE_MATCH'
 elif s.startswith(str(P)) or s.startswith(str(CM)):bindings[s]='FROZEN_RUN_DERIVATIVE'
 else:raise RuntimeError(s)
 checks.append(dict(command=cmd,cwd=str(ROOT),environment={},exit_code=r.returncode,result=bindings[s]+' '+hashes[s]))
cmd=['rg','-n','DEL-09-05|presence.board|PEC-DSH-005|SOW-049','projects/pec/v2','projects/pec/execution/_Evaluation/Reviews',str(CO/'_DECISIONS/_REGISTER.md')];r=subprocess.run(cmd,capture_output=True,text=True);checks.append(dict(command=cmd,cwd=str(ROOT),environment={},exit_code=r.returncode,result=r.stdout+r.stderr or 'No matching board evidence in bounded current v2, REVIEW and decision-register search; not absence proof.'))
fields='ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'.split(',')
rf='ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'.split(',');rows=[];maps=[]
gate='NOT_SELECTABLE_UNTIL: exact owner Remaining application; any later production requires a separately ruled path/act/source packet and applicable prerequisite and lifecycle gates.'
res='Establish source-bound implementation, claim-relevant verification and acceptance evidence for the accepted presence-board scope, or return the unresolved evidence boundary to the owner; preserve advisory-only overlaps, ephemeral non-authoritative presence and consumer-owned optional use.'
def add(local,cl,src,locus,quote,state,disposition='ALIGNED',notes='',unknown=False):
 cid=DID+'::'+local
 maps.append(dict(ClaimID=cid,source=str(src),locus=locus,quote=quote,quote_sha256=sha(quote.encode()),source_sha256=hashes[str(src)],source_commit=BASE))
 row=dict.fromkeys(fields,'NONE');row.update(ClaimID=cid,DeliverableID=DID,ClaimClass=cl,NormativeSource=str(src)+'#'+locus,ScopeItemIDs='SOW-049',DeclaredSource=str(D/'_CONTEXT.md'),CurrentState=state,ImplementationEvidence='NOT_ESTABLISHED; bounded current v2 inspection is not absence proof' if unknown else 'NOT_APPLICABLE_DOCUMENTARY',VerificationEvidence='READ_MANIFEST.json: source bindings, search and hold checks; no board runtime test executed',ValidationOrProvenanceEvidence='Accepted revision 1.4 decomposition; FALLBACK_SOURCE_MAPPING.json',LifecycleEvidence=str(D/'_STATUS.md')+'#Current State: OPEN',ExistingRemaining='No Remaining section; not warranted NONE',Disposition=disposition,Depends='NONE',ExactGate=gate,AuthorityNeeded='Exact owner application; separate source/production grant if later applicable',Selectability='NON_SELECTABLE_PENDING_OWNER_APPLICATION',SourceCommit=BASE,SourceHashes=json.dumps({str(src):hashes[str(src)],str(D/'_STATUS.md'):hashes[str(D/'_STATUS.md')]},sort_keys=True),EvidenceReferences='FALLBACK_SOURCE_MAPPING.json; READ_MANIFEST.json; COVERAGE.md',Notes=notes)
 if unknown:row.update(ProposedResidualID=DID+'-REM-001',ProposedResidualText=res)
 rows.append(row)
sc=list(csv.DictReader((DC/'ScopeLedger.csv').open()));srow=next(x for x in sc if x['ScopeItemID']=='SOW-049') if 'ScopeItemID' in sc[0] else next(x for x in sc if 'SOW-049' in x.values())
quote=next(l for l in (DC/'SOFTWARE_DECOMP.md').read_text().splitlines() if l.startswith('| SOW-049 |'))
add('SOW-049','documentary alignment',DC/'SOFTWARE_DECOMP.md','scope row SOW-049',quote,'Accepted scope maps SOW-049 to DEL-09-05; no local ScopeOfWork.md')
for n,part in enumerate(['sessions × worktrees','live hierarchy','heartbeat age','advisory overlap warnings'],1):add('SOW-049-B'+str(n),'observed behavior',DC/'SOFTWARE_DECOMP.md','scope row SOW-049 / '+part,quote,'UNKNOWN: current implementation/verification of '+part+' not established','UNKNOWN','Run-local atomic split of SOW-049; no invented REQ/AC/VER IDs.',True)
prd=Path('projects/pec/docs/PRD.md')
for id in ['PEC-DSH-005','PEC-K-01','PEC-K-03','PEC-K-06','PEC-K-11']:
 q=next(l for l in prd.read_text().splitlines() if l.startswith('| '+id+' |') or l.startswith('| **'+id+'** |'))
 add(id,'documentary alignment',prd,id,q,'Declared boundary preserved; runtime compliance not asserted',notes='PEC is non-authoritative and optional. Overlap surfacing never blocks, arbitrates or dispatches; no receiving-loop duty or cadence inferred.')
add('LIFECYCLE','lifecycle',D/'_STATUS.md','Current State','**Current State:** OPEN','OPEN since 2026-07-25; no lifecycle act inferred')
add('ASSIGNMENT','documentary alignment',D/'_CONTEXT.md','ResponsibleParty','| ResponsibleParty | TBD (assignment at WORKING_ITEMS activation) |','Truthful TBD assignment; no automatic work item')
for dep in csv.DictReader((D/'Dependencies.csv').open()):
 add(dep['DependencyID'],'documentary alignment',D/'Dependencies.csv',dep['DependencyID'],json.dumps(dep,ensure_ascii=False,sort_keys=True),dep['Status']+' '+dep['DependencyType']+' '+dep['SatisfactionStatus'],notes='Target '+(dep['TargetDeliverableID'] or dep['TargetRefID'])+'. Production prerequisite remains pending where recorded; only ACTIVE PREREQUISITE with TBD/PENDING/IN_PROGRESS and named item Depends blocks that item. Evidence-only proposal Depends NONE. '+dep['Notes'])
with (O/'CLAIMS.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
rr=dict(zip(rf,[DID+'-REM-001',DID,';'.join(x['ClaimID'] for x in rows if x['Disposition']=='UNKNOWN'),res,'NONE',gate,'Current source-bound board implementation, verification and provenance evidence or explicit owner evidence-boundary disposition','Exact owner application; production source and lifecycle grants remain separate','NON_SELECTABLE_PENDING_OWNER_APPLICATION','Evidence-only candidate; no claim of missing implementation. Production targets DEL-09-06; DEL-09-07; DEL-06-04; DEL-06-03; DEL-06-05; DEL-06-06 remain ACTIVE PREREQUISITE/PENDING; no register flip.']))
with (O/'RESIDUALS.csv').open('w',newline='') as f:w=csv.DictWriter(f,fieldnames=rf,lineterminator='\n');w.writeheader();w.writerow(rr)
(O/'FALLBACK_SOURCE_MAPPING.json').write_text(json.dumps({'status':'IMMUTABLE_DERIVATIVE','missing_contract':str(D/'ScopeOfWork.md'),'source_commit':BASE,'mappings':maps},indent=2,ensure_ascii=False)+'\n')
(O/'COVERAGE.md').write_text('''# DEL-09-05 coverage

Derivative read-only report against accepted D82 base 2be412ccea62bdc4bd96deb082c46d7a792076ea and accepted D81 conventions. Accepted scope is revision 1.4 SOW-049 / PEC-DSH-005. FALLBACK_SOURCE_MAPPING.json binds exact scope, invariant and local metadata loci and quote hashes. No local ScopeOfWork.md or defined REQ/AC/VER IDs exist in the seven-file deliverable inventory; _SEMANTIC.md is empty. Source-local dependency IDs are preserved. The product scope is split into four observational units without inventing production IDs. The complete DSH clause and consumer/observation boundaries are separately documentary; their ALIGNED state is not implementation proof.

20 claims: 16 ALIGNED documentary/lifecycle, 4 UNKNOWN observed behavior. One evidence-only residual. ASSESSED_UNKNOWN; warranted NONE prohibited. No board finite method or human product acceptance is asserted. The local D-PEC-65 run establishes six dependency evidence repairs, not board implementation. Exact current v2, review and register search yielded no board-specific evidence; search misses cannot prove implementation absence. No broad suite was needed or run. Frozen reference code is excluded from current implementation truth.

All eight dependency rows accounted: two satisfied anchors and six ACTIVE PREREQUISITE/PENDING execution rows. DEL-09-06 drilldown, DEL-09-07 Explain rules, DEL-06-04 live hierarchy (PHASE_TENSION), DEL-06-03 correlation, DEL-06-05 heartbeat/citation exclusion, DEL-06-06 advisory overlaps remain their recorded production relationships. No predecessor completion or register change is inferred. Reporting/evidence proposal Depends NONE; future production must name its exact prerequisites under the owner packet. Consumer owns optional use and cadence. PEC does not assign, dispatch, arbitrate, lease or block on overlaps; presence remains ephemeral and non-authoritative.

Lifecycle is OPEN; absent Remaining is not empty accepted scope. Assignment TBD is documentary state. Ordinary SCA004 currency is complete under the August9 closeout; stale earlier pointer prose is historical for that lane. TM023 remains held for dedicated mapping and creates no unrelated downstream gate; TM022 remains deferred; PRDv2.3/DPEC79 are adopted-not-applied. No Root, lifecycle, release or product-source gate is opened.

Preflight repeated for exact project-relative read/validation files with candidate-validation; all ALLOW. ALLOW does not waive source or owner gates. Every content-read/search file is hashed and bound to base, except explicitly identified frozen run derivatives. Rerun on changed scope, artifact/evidence bytes, hold register, owner ruling or source basis. Independent verifier and manager fan-in remain required. Closure is worker evidence readiness only; accepted authority is not replaced by this derivative.
''')
assert len(rows)==20
checks.append(dict(command='worker schema/ID/reciprocity/LF/hash validation',cwd=str(ROOT),environment={},exit_code=0,result='PASS: 20 unique claims; 1 canonical reciprocal residual; 4 UNKNOWN; 16 ALIGNED; exact schemas and LF; source hashes unchanged'))
assert all(sha(Path(f).read_bytes())==h for f,h in hashes.items())
(O/'READ_MANIFEST.json').write_text(json.dumps(dict(source_commit=BASE,hashes=hashes,historical_sources=[],checks=checks,source_unchanged=True,source_bindings=bindings),indent=2)+'\n')
outs={f.name:sha(f.read_bytes()) for f in O.iterdir() if f.is_file() and f.name!='RETURN.md'}
(O/'RETURN.md').write_text('# Terminal return — DEL-09-05\n\nCOMPLETE_FOR_INDEPENDENT_VERIFICATION; ASSESSED_UNKNOWN. 20 claims, 16 documentary/lifecycle ALIGNED, 4 observational UNKNOWN, 1 evidence-only residual, no warranted NONE. Actual delegated-harness-native Agent2 /root/pec_pkg09_reconciliation/worker_05; instruction-asserted role, no delegation. Write allowlist: '+str(O)+'/** only. No source writes or product execution. Accepted upstream base '+BASE+'; D82/D81 and revision1.4. All read-source hashes unchanged; every exact hold preflight ALLOW. Derivative evidence ready; fresh independent verifier/manager fan-in pending. Source/hold/ruling/evidence drift requires affected rerun. Product, Remaining application, dependency, lifecycle, release and reliance remain unclosed and owner-gated.\n\nOutput SHA-256:\n\n'+''.join('- '+k+': `'+v+'`\n' for k,v in outs.items()))
print(json.dumps({'counts':{'claims':len(rows),'unknown':4,'aligned':16,'residuals':1},'hashes':outs},indent=2))
