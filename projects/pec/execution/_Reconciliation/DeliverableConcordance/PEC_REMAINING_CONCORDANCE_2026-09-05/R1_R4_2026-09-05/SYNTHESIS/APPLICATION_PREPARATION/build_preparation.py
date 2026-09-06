from pathlib import Path
import json,csv,re,hashlib,subprocess,collections
R=Path('projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05/R1_R4_2026-09-05'); O=R/'SYNTHESIS/APPLICATION_PREPARATION'; BASE='2be412ccea62bdc4bd96deb082c46d7a792076ea'
sha=lambda b:hashlib.sha256(b).hexdigest()
def dump(name,value):(O/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n')
def csvwrite(name,rows,fields=None):
 with (O/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields or list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
res=json.loads((O/'ORIGINAL_RESIDUALS.json').read_text()); claims=json.loads((O/'ORIGINAL_LINKED_CLAIMS.json').read_text());routes=list(csv.DictReader((R/'SYNTHESIS/PREPARATION/ROUTING_TEN_PACKAGE_DRAFT.csv').open()));car=json.loads((R/'SYNTHESIS/PREPARATION/TEN_PACKAGE_CARRIER_PRECHECK.json').read_text())['carriers']; cm={x['DeliverableID']:x for x in car}
# This curated subject map states only evidence inspection objects; original imperative production wording remains in the immutable source map.
subjects={
'00-02-001':'SOW-034 event-schema/versioned daemon, hooks CLI and adapter types, local schema and pinned mirrors, additive evolution, contract tests and versioning note; distinguish the capability API schema and historical PEC code from this event-contract obligation',
'00-02-002':'the PKG-00 versioned event-contract publication and dependency handoff evidence ahead of P3 DEL-07-01 and DEL-07-03 consumers',
'01-01-001':'the accepted record-tier schema, fourteen entity types and linked model requirements/criteria; preserve exact accepted obligation and D75 O-A selection of DEL-01-06 only',
'01-01-002':'VER-001 through VER-012 execution records for the selected record model and their AC mapping; distinguish contract-format checks from model tests',
'01-02-001':'the accepted presence entity model, expected loss on rebuild and model-test evidence; preserve operational, TTL and never-citable boundaries',
'01-03-001':'OUT-001 and REQ-001/002/007/008 store lifecycle/interface evidence and criteria; distinguish store-local delete/recreate from DEL-10-02 system kill testing',
'01-03-002':'single-boundary content-minimal guard behavior, admitted field classes, located rejection, no silent loss and uniform ingest',
'01-03-003':'each declared store/guard VER method and existing executing-test evidence; distinguish SOW format checks and system kill-test evidence',
'01-04-001':'SOW-057 logging module, inspection command and tests, content minimality, append-only behavior and graceful absence',
'01-05-003':'VER-004 records for a sequence of service-core changes and at least one release candidate at each exact evaluated state; registration or one passing run cannot establish this sequence and this inquiry creates no release candidate',
'02-01-001':'SOW-011 parser, declared lifecycle dialect and admission-rule obligations; locate an accepted existing dialect and parser without authoring either',
'02-01-002':'existing VER-001 through VER-012 fixture execution records against the exact lifecycle parser/dialect, their criteria and finite limits; retain AC-013 human REVIEW as a separate acceptance act',
'02-02-001':'SOW-012 decision-register/packet parser, its REQ/AC/VER fixture contract, identity/status-only output, grammar, explicit limitations and both-paths OI-001 posture',
'02-03-001':'SOW-013 receipts parser, per-loop grammar table and fixture suite against OUT-001..003, REQ-001..013 and AC-001..013',
'02-04-001':'the accepted run-evidence parser, declared grammar, upstream RunRecord typing and fixture obligations',
'02-05-001':'both dependency feeds under accepted SOW-015 and their claim-specific verification',
'02-06-001':'SOW-016 parser and fixtures, declared grammar, upstream typing, gate transcription, provenance, explicit limitations, content minimality, determinism, read-only behavior and boundaries; map each AC/VER',
'03-01-001':'OUT-001 and REQ-001..015 one-command full rebuild, declared write boundary and unresolved contract choices',
'03-01-002':'OUT-002 rebuild suite and existing results for its sixteen methods; distinguish VER-012 stand-in/live-facility evidence and VER-015 later enforcement boundary',
'03-03-001':'drift-classifier implementation and REQ-001..014, retaining unresolved upstream schema/snapshot questions for their owners',
'03-03-002':'existing VER-001..014 and AC-001..014 claim-mapped execution records, finite fixture limits and live upstream integration versus stand-ins',
'03-04-001':'SOW-020 parity comparison tool, findings, source boundaries, limitations, declared equivalence, standing registration and VER-001..015; upstream harness tests are not downstream parity proof',
'03-05-001':'SOW-038 recovery by reconciliation, no stream-only record facts, bounded gap-recovery method and limits; preserve PKG-07 ingest and DEL-10-08 demonstration ownership',
'03-06-001':'performance suite and recorded bound against REQ-001..014, AC-001..013 and VER-001..013, real upstream invocation, corpus/conditions/coverage/baseline/delta/fallback, own writes, content minimality, repeatability and method mapping; stand-in timings cannot establish real performance',
'04-02-001':'delta-service OUT-001/002, REQ-001..015, existing VER-001..015 execution and AC-001..016 acceptance records; preserve CON-001..005/TBD-002..004, delta composition, caller anchor, record-tier and ownership boundaries',
'04-03-001':'SOW-006/SOW-007 citation and freshness implementation, tests and acceptance evidence against the accepted linked contract requirements',
'04-05-001':'SOW-009 limitation renderer, derivation record and executing tests against OUT-001/002, REQ-001..014, AC-001..014 and VER-001..014',
'05-01-001':'SOW-022 gate predicates and SOW-023 Explain/advisory facets and their claim-relevant verification',
'05-02-001':'SOW-024 cross-loop AWAITING_RULING completeness, parked owner-act lanes and link-only authored-file references; identify any accepted local contract and preserve the presently missing contract boundary',
'06-01-001':'SOW-026 harness-reported session records, every required field and daemon-owned identity/lifecycle with corresponding verification',
'06-02-001':'SOW-027 worktrees, branches, HEAD, ahead/behind, dirty path names/counts and read-only Git scanning tests; never capture file/diff content',
'06-03-001':'SOW-028 correlation implementation, claim-relevant tests and contract/acceptance records, retaining the missing local contract boundary',
'06-04-001':'SOW-029 live parent-child hierarchy edges from daemon/hook feeds and anticipated hierarchy-maintenance tests',
'06-05-001':'accepted TTL, heartbeat-age, liveness-honesty, presence-store citation exclusion and anticipated tests, preserving runtime ownership',
'06-06-001':'SOW-031 overlap detection for write scopes, shared branches, same merge targets and never-blocking advisory behavior',
'07-01-001':'SOW-033/SOW-039 event-id keying, append-only/idempotent ingest, durable queryable attributable messages and no ephemeral relay',
'07-02-001':'SOW-035 owner-authorized bridge artifact, declaration/attribution contract, event-contract mapping and claim-relevant tests',
'07-03-001':'SOW-036 session start/stop/status/scope-declaration hooks and declared attributable use, with exact verification/acceptance records',
'07-04-001':'SOW-037 optional cmux adapter, any accepted activation/contract and claim-relevant verification, declaration, attribution and graceful absence; optionality remains unchanged',
'07-05-001':'SOW-087 shared-runtime client seam, v2 entity integration, PKG-00 event-contract consumption and claim-relevant tests; retain root runtime ownership',
'08-01-001':'the DEL-08-01 socket, token access, internal seam and declared service tests; record exact implementation roots or explicit unknowns',
'08-03-001':'the DEL-08-03 format specification, serializer and tests, each production requirement and finite verification method; a generic upstream schema is not this evidence',
'08-04-001':'the declared latency suite and budget record, p95 ≤100 ms with corpus, boundary/vantage, composition, conditions and sample; retain the proven absence of outputs in the enumerated local surfaces separately from unobserved wider implementation and real-surface versus stand-in evidence',
'08-05-001':'accepted SOW-044 SSE delta/presence endpoint verification/acceptance evidence; preserve missing local contract and P4 production staging',
'10-02-001':'the accepted kill-test workflow/deletion/failure/reporting/boundary contract, harness artifacts and existing finite VER results',
'10-02-002':'owned kill-test gate wiring, an accepted release path and exact-candidate verdict records; explicitly report an unarmed gate if the path is unestablished, without creating a release process',
'10-03-001':'SOW-025 negative-surface suite, operative definition, schema-plus-listener enumeration, all-class refusal/non-persistence, fail-closed faults, repeatability, binding and observation-only checks; additive schema acceptance alone cannot discharge these methods',
'10-04-001':'SOW-059 spot-check method, conditional instrumentation need and existing applicable measurement evidence; retain missing contract/owner interpretation for later decision',
'10-05-001':'SOW-085 owner use or non-use of orientation/dashboard, P2-B uptake/falsification evaluation, existing logs and accepted local contract; preserve manual Step 0 and no PEC read/write duty',
'10-06-001':'SOW-061 accepted seeded-conflict test contract and existing warning results, fixture coverage and separately identified P3 acceptance evidence',
'10-07-001':'SOW-062 kill/crash TTL-honesty test contract, applicable implementation and source-bound verification/acceptance; retain explicit local contract/evidence unknowns',
'10-08-001':'SOW-063 P4 stream-loss recovery demonstration, declared method, observed reconciliation recovery and separate owner exit acceptance',
'10-09-001':'SOW-084 accepted metric definition and measurement evidence for write-scope/branch conflicts first discovered at Git time rather than surfaced in advance, per week of concurrent operation, incident metric and weekly report; do not fabricate data',
'10-10-001':'any existing standing progression record and maintenance declaration, accepted DAG ingestion, per-cutover predecessor capability/acceptance, attributed friction, proposed/rejected/unnecessary functions, occasion-level fallback, human-gated routes, upstream limits and explicitly unmet/met structurally different-loop generality; no terminal completion',
'10-10-002':'any existing standing check method, check-to-VER-001..013 map and exact-state execution records, including explicit verdicts for absent required progression evidence or failed assertions; distinguish produced verdict from release-blocking authority',
'10-11-001':'OUT-001 and REQ-001..013 parity metric report and verification records, counting rules, state binding, coverage limits and measurement/non-authority boundaries',
'10-12-001':'SOW-060 current enablement metric, enabled-consumer orientation-use metric, consumer-owned contact-opportunity basis and evaluation notes; preserve optional consumer-owned use and do not infer zero uptake or receiving-loop nonconformance'
}
for i in range(1,15):
 id=f'DEL-03-02-REM-{i:03}';subjects[f'03-02-{i:03}']=res[id]['ProposedText'].split('verification for ',1)[1].split(';',1)[0]+' under the accepted DEL-03-02 incremental reconcile contract'
known={'EVIDENCE','DOCUMENTARY','PRODUCT_OBLIGATION','CONFIRMED_SCANNER_REPAIR'}
items=[];mapping=[];gates=[];depmapping=[]
for route in routes:
 id=route['ResidualID']; x=res[id];d=x['DeliverableID']; kind=route['ProposedRoute']; links=[v.strip() for v in x['ClaimIDs'].split(';') if v.strip()];linked=[claims[k] for k in links];assert all(c['DeliverableID']==d for c in linked)
 folder=Path(cm[d]['CarrierPath']).parent; depfile=folder/'Dependencies.csv'; deps=list(csv.DictReader(depfile.open())) if depfile.exists() else []
 production_rows=[q for q in deps if q['DependencyClass']=='EXECUTION'];orig_targets=[v.strip() for v in x['Depends'].split(';') if v.strip() and v.strip()!='NONE']; blocking=[q['DependencyID'] for q in deps if q['Status']=='ACTIVE' and q['DependencyType']=='PREREQUISITE' and q['SatisfactionStatus'] in ['TBD','PENDING','IN_PROGRESS'] and q['TargetDeliverableID'] in orig_targets]
 pending=d.startswith('DEL-00-'); frozen=cm[d]['CurrentLifecycle']=='CHECKING'; text='';gate='';depends=x['Depends']; clarification='No application proposed; original route/wording/gates preserved.'
 if kind=='EVIDENCE':
  key=id[4:].replace('-REM-','-');assert key in subjects,id
  text='Inspect and map existing source-state-bound evidence for '+subjects[key]+'. Cover the exact linked claims; distinguish observed implementation, bounded local absence, missing/unmapped evidence, finite method execution and historical acceptance. Retain UNKNOWN where evidence is unavailable and return exact unresolved obligations for owner disposition. This item is read-only inquiry and a derivative evidence report; any new contract, implementation, test, measurement run, acceptance or production act requires a separate ruling.'
  gate='(gated: owner authorizes the exact evidence-only read scope and derivative report-output write paths/acts in a bounded brief; current exact-target reliance preflight)'
  depends='NONE';clarification='Scope of act narrowed to inspection/mapping of existing evidence. Any raw imperative production/test/measurement/contract tail is retained below as a prospective obligation, not selected by this item. Production Depends removed from this evidence-only item; original targets and every current production row/gate remain separately recorded.'
 elif kind=='PRODUCT_OBLIGATION':
  text=x['ProposedText']
  gate=f'(gated: separate exact owner-ruled {d} production packet on origin/main opening the named source/test paths, acts, verification and rollback under F-PEC-1; WORKING_ITEMS activation; current reliance preflight)'
  if id=='DEL-02-07-REM-002':gate+=' (gated: accepted CON-002 loop-to-project relation derivation or owner-ruled SCOPE_CHANGE if not derivable)'
  clarification='Accepted future-production obligation retained because positive current REVIEW declaration of IMPLEMENTATION NOT PRODUCED corroborates the bounded inventory; no UNKNOWN-to-implementation inference. Application prerequisite is packet-level; original current production Depends and source/scope gates retained.'
 elif kind=='CONFIRMED_SCANNER_REPAIR':
  if id.endswith('001'):text='Repair the demonstrated importlib.import_module callable-alias detector false negative using exact R0 dynamic_import_alias bytes; retain static stdlib/workspace exceptions and the current conservative BLOCK policy for recognized dynamic imports, with failing-before/passing-after regression and exact-byte acceptance.'
  else:text='Repair the demonstrated socket.sendto external-UDP detector false negative using exact R0 external_udp bytes; correctly locate bound/unbound overload destinations, retain local/unknown classification controls and open OI-009, with failing-before/passing-after regression and exact-byte acceptance.'
  gate='(gated: separately accepted exact owner PEC source/test fence-opening packet and owning REVIEW/CHECKING change path before any mutation; fresh independent verification and exact artifact acceptance remain separate acts)'
  clarification='Confirmed detector gaps only; finite VER-001/VER-003 methods and historical acceptance remain valid for their exact bytes. Frozen carrier preview is conditional and requires separate lawful reversal/change then fresh carrier rebinding before application.'
 elif kind=='DOCUMENTARY':
  text=x['ProposedText'];sow=str(folder/'ScopeOfWork.md')
  gate=f'(gated: owner accepts exact bounded documentary wording and authorizes only the named current-source paraphrase loci in {sow}; preserve lifecycle, accepted history, completed ordinary currency and current dependency topology/status)'
  clarification='Narrow exact named present-source documentary correction; no blanket SOW rewrite, lifecycle change, dependency repair or completed currency reopening. Current source/control hashes and dependency evidence are bound; actual canonical SOW edit still requires separate exact wording/path ruling.'
 if kind in known:
  items.append({'ResidualID':id,'DeliverableID':d,'Route':kind,'ClaimIDs':';'.join(links),'ProposedText':text,'Depends':depends,'ItemGate':gate,'PacketApplicationGate':'NOT_SELECTABLE_UNTIL: owner separately approves and applies the exact status application manifest; this preparation is not authority','PreparationState':'BLOCKED_PKG00_CORRECTION' if pending else 'CONDITIONAL_FROZEN_PREVIEW' if frozen else 'CANDIDATE_PENDING_APPLICATION','ClosureEvidence':('Dated derivative map covers every linked claim with exact source/hash, evidence strength and unresolved-owner routes; no manufactured production result.' if kind=='EVIDENCE' else x['ClosureEvidence'])})
 mapping.append({'ResidualID':id,'DeliverableID':d,'ProposedRoute':kind,'OriginalResidual':x,'OriginalManagerDraftRoute':route,'OriginalLinkedClaims':linked,'ProposedItem':items[-1] if kind in known else None,'ActScopeClarification':clarification,'ProductionBoundary':{'original_depends':x['Depends'],'original_exact_gate':x['ExactGate'],'current_dependency_path':str(depfile),'current_dependency_rows':production_rows,'matching_original_target_blockers':blocking,'limitations':'Original source/Root/runtime owner, REVIEW/lifecycle, P4/C-01/C16 and interpretation conditions remain prospective for actual production. D81/D82 discharge calibration/reporting only. Report-output write authority is separately prospective. No actual target or dependency register is changed.'},'PackageFanInState':'BLOCKED_PENDING_PKG00_EXACT_CORRECTION' if pending else 'CLEARED_FOR_TEN_PACKAGE_PREPARATION','EvidenceStrengths':dict(collections.Counter(c['Disposition'] for c in linked))})
 gates.append({'ResidualID':id,'OriginalExactGate':x['ExactGate'],'D81Calibration':'DISCHARGED by D-PEC-81_CALIBRATION_ACCEPTANCE_2026-09-05.md','D82Reporting':'DISCHARGED by D-PEC-82_remaining_corpus_reporting_2026-09-05.md at '+BASE,'ExactApplication':'PROSPECTIVE_PACKET_LEVEL; no source application','ProposedItemGate':gate or 'NO_ITEM: held/conditional outside Remaining','OriginalProductionDepends':x['Depends'],'ProposedDepends':depends if kind in known else 'NO_ITEM','CurrentMatchingProductionBlockerIDs':';'.join(blocking) or 'NONE','ScopeChangeReason':clarification})
 depmapping.append({'ResidualID':id,'DeliverableID':d,'Route':kind,'OriginalDepends':x['Depends'],'ProposedDepends':depends if kind in known else 'NO_ITEM','CurrentDependenciesPath':str(depfile),'CurrentDependencySHA256':sha(depfile.read_bytes()) if depfile.exists() else None,'OriginalMatchingBlockingIDs':blocking,'CurrentProductionRows':production_rows})
assert len(mapping)==156 and len(car)==57 and len(items)==85
assert all(i['Depends']=='NONE' for i in items if i['Route']=='EVIDENCE')
csvwrite('PROPOSED_ITEMS.csv',items);dump('CLAIM_TO_PROPOSAL_MAP.json',mapping);csvwrite('GATE_CURRENTNESS.csv',gates);dump('PRODUCTION_DEPENDENCY_MAP.json',depmapping)
application=[];rollback=[];dispositions=[];sims=[]
for c in car:
 d=c['DeliverableID'];p=Path(c['CarrierPath']);b=p.read_bytes();assert sha(b)==c['PreimageSHA256'];assert b'## Remaining' not in b
 historical=subprocess.check_output(['git','show',f'{BASE}:{p}']);assert historical==b
 pre=O/'PREIMAGES'/d/'_STATUS.md';pre.parent.mkdir(parents=True,exist_ok=True);pre.write_bytes(b)
 selected=[i for i in items if i['DeliverableID']==d];rs=[m for m in mapping if m['DeliverableID']==d]
 if selected:
  suffix=b'\n## Remaining\n\n'+('\n\n'.join('- [ ] '+i['ResidualID']+' — '+i['ProposedText']+'\n  Depends: '+i['Depends']+'\n  '+i['ItemGate'] for i in selected)+'\n').encode()
  after=b+suffix;post=O/'CANDIDATES'/d/'_STATUS.md';post.parent.mkdir(parents=True,exist_ok=True);post.write_bytes(after)
  state='BLOCKED_PKG00_CORRECTION' if d.startswith('DEL-00-') else 'CONDITIONAL_FROZEN_PREVIEW' if c['CurrentLifecycle']=='CHECKING' else 'CANDIDATE_PENDING_OWNER_APPLICATION'
  rec={'DeliverableID':d,'TargetPath':str(p),'Operation':'APPEND_REMAINING_ONLY','SourceCommit':BASE,'OriginalBaseSHA256':sha(historical),'CurrentPreimageSHA256':sha(b),'ProposedPostimageSHA256':sha(after),'PreimageCopy':str(pre),'CandidateCopy':str(post),'ResidualIDs':[i['ResidualID'] for i in selected],'CurrentLifecycle':c['CurrentLifecycle'],'PreparationState':state,'ApplyAuthority':'NONE; future exact owner application ruling required','FrozenRebindRequired':c['CurrentLifecycle']=='CHECKING','ExpectedAppendBytes':len(suffix)};application.append(rec)
  rollback.append({'DeliverableID':d,'TargetPath':str(p),'ExpectedAppliedPostimageSHA256':sha(after),'RestorePreimageSHA256':sha(b),'RestoreCopy':str(pre),'InverseOperation':'Remove exact appended Remaining bytes only when complete current bytes equal authorized postimage; stop on drift; frozen preview requires new manifest after separate lawful change','RollbackAuthority':'Future owning packet must name lawful rollback; no automatic target action'})
  assert after[:len(b)]==b and after[len(b):]==suffix and after[:-len(suffix)]==b
  sims.append({'DeliverableID':d,'ApplyInMemory':True,'InverseInMemory':True,'NonRemainingBytePreservation':True,'LifecycleAndLastUpdatedPreserved':True,'OriginalCurrentBaseEquality':True,'TargetUntouched':p.read_bytes()==b})
  reason='Exact draft Remaining additions only; source, approval and report-output gates remain prospective.'
 else:
  state='NO_APPLICATION_BLOCKED_PKG00_CORRECTION' if d.startswith('DEL-00-') else 'NO_APPLICATION_HELD_OR_CONDITIONAL' if rs else 'NO_APPLICATION_BOUNDED_NONE' if d=='DEL-10-01' else 'NO_APPLICATION_UNRESOLVED'
  reason='All source proposals for this carrier are held/conditional outside automatic Remaining; no warranted NONE inferred.' if rs else 'Accepted DEL-10-01 before-leg baseline scope only; no after-leg, continuing parity or wider release completion implied.' if d=='DEL-10-01' else 'No candidate item selected; unresolved claim/evidence conditions remain; no warranted NONE asserted.'
 dispositions.append({'DeliverableID':d,'CarrierPath':str(p),'CurrentLifecycle':c['CurrentLifecycle'],'PreimageSHA256':sha(b),'PreimageCopy':str(pre),'Disposition':state,'ProposedItemCount':len(selected),'ProposedResidualIDs':';'.join(i['ResidualID'] for i in selected),'HeldOrConditionalResidualIDs':';'.join(m['ResidualID'] for m in rs if m['ProposedRoute'] not in known),'Reason':reason,'SourceUnchanged':p.read_bytes()==b})
dump('APPLICATION_MANIFEST.json',{'status':'TEN_PACKAGE_PARTIAL_PREPARATION_NOT_APPLICATION','source_commit':BASE,'author_native_identity':'/root/pec_corpus_synthesis/scanner_proposal','carrier_population':57,'candidate_carriers':len(application),'proposed_items':len(items),'apply_prerequisites':['PKG00 corrected fan-in','PKG09 explicit release and additive full-scope preparation','fresh independent final R4 review','exact owner Remaining application approval','each frozen carrier separate lawful reversal/change then rebind/reissue before application'],'entries':application})
dump('ROLLBACK_MANIFEST.json',{'status':'PROSPECTIVE_INVERSE_ONLY','entries':rollback});csvwrite('CARRIER_DISPOSITIONS.csv',dispositions)
dump('SIMULATION.json',{'status':'PASS_FOR_DRAFT_BYTE_TRANSFORMS_ONLY','candidate_count':len(sims),'all57_carriers_preimage_bound':True,'target_writes':0,'checks':sims,'all_checks_pass':all(all(x[k] for k in ['ApplyInMemory','InverseInMemory','NonRemainingBytePreservation','LifecycleAndLastUpdatedPreserved','OriginalCurrentBaseEquality','TargetUntouched']) for x in sims)})
print('Prepared',len(items),'items across',len(application),'candidate carriers; accounted',len(dispositions),'carriers; non-Remaining bytes preserved.')
