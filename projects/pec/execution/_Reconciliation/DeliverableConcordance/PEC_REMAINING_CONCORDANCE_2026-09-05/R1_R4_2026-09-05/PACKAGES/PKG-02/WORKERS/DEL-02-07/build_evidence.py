from pathlib import Path
import csv,json,hashlib,re,subprocess,os,collections
ROOT=Path.cwd(); RUN=Path('projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05'); OLD=RUN/'R0_CALIBRATION/DEL-02-07'; PKG=RUN/'R1_R4_2026-09-05/PACKAGES/PKG-02'; OUT=PKG/'WORKERS/DEL-02-07'; COMMON=RUN/'R1_R4_2026-09-05/COMMON'; BASE='2be412ccea62bdc4bd96deb082c46d7a792076ea'; DS=Path('projects/pec/execution/PKG-02_File_Truth_Parsers/1_Working/DEL-02-07_adapter_yaml_feed_manifest_consumer')
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dump(n,x): (OUT/n).write_text(json.dumps(x,indent=2)+'\n')
def csvwrite(n,fields,rows):
 with (OUT/n).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,lineterminator='\n');w.writeheader();w.writerows(rows)
oldm=json.loads((OLD/'READ_MANIFEST.json').read_text()); hashes={p:sha(p) for p in oldm['hashes']}; deltas=[{'path':p,'old_sha256':h,'current_sha256':hashes[p]} for p,h in oldm['hashes'].items() if hashes[p]!=h]
assert [x['path'] for x in deltas]==['projects/pec/execution/_Coordination/_DECISIONS/_REGISTER.md']
extras=[RUN/'CONVENTIONS.md',RUN/'SAMPLE_SUMMARY.csv',RUN/'RESIDUAL_RECOMMENDATIONS.csv',RUN/'CALIBRATION_REPORT.md',PKG/'PACKAGE_BASIS.md',PKG/'SOURCE_MANIFEST.json',PKG/'BRIEFS/DEL-02-07.md',PKG/'validate_members.py']
extras+=list(COMMON.glob('*.md'))+[COMMON/'SOURCE_MANIFEST.json',COMMON/'SCOPE_CENSUS.csv']+list(OLD.glob('*'))
extras+=list(Path('projects/pec/execution/_Coordination/_DECISIONS').glob('*82*.md'))+[Path('projects/pec/execution/_Coordination/_DECISIONS/D-PEC-81_CALIBRATION_ACCEPTANCE_2026-09-05.md')]
for p in extras:
 if p.is_file():hashes[str(p)]=sha(p)
cm=json.loads((COMMON/'SOURCE_MANIFEST.json').read_text())['hashes']; overlap={p:h for p,h in hashes.items() if p in cm}; assert all(cm[p]==h for p,h in overlap.items())
sample=next(x for x in csv.DictReader((RUN/'SAMPLE_SUMMARY.csv').open()) if x['DeliverableID']=='DEL-02-07');assert sha(OLD/'CLAIMS.csv')==sample['SelectedClaimsSHA256']=='90e330c034a9a7a89accf737fc926632106693a9c55490722b55dbb4ad669931'
checks=[]
for name in ['ScopeOfWork.md','_STATUS.md','Dependencies.csv']:
 command=['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register','projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv','--target',str((DS/name).relative_to('projects/pec')),'--operation','candidate-validation']
 p=subprocess.run(command,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'});assert p.returncode==0 and json.loads(p.stdout)['status']=='ALLOW'
 checks.append({'command':' '.join(command),'cwd':'.','environment':{'PYTHONDONTWRITEBYTECODE':'1'},'exit_code':p.returncode,'result':p.stdout.strip()})
checks.append({'command':'R0 selected-source SHA-256 rehash and COMMON overlap comparison','cwd':'.','environment':{},'exit_code':0,'result':f'{len(oldm["hashes"])} R0 inputs rehashed; one expected D82 decision-register successor; {len(overlap)} COMMON overlapping hashes match.'})
# Inspect the complete current declared v2 implementation boundary, not filename search inference.
source_inventory=[]
for p in sorted(Path('projects/pec/v2/src').rglob('*')):
 if p.is_file():
  hashes[str(p)]=sha(p);text=p.read_text();source_inventory.append({'path':str(p),'sha256':sha(p),'lines':len(text.splitlines()),'semantic_role':'LoopRegistry JSON adapter' if p.name=='loop_registry.py' and 'adapters' in p.parts else 'LoopRegistry typed port' if p.name=='loop_registry.py' else 'package initializer'})
# Every source module is one of five initializers and two fully inspected registry modules.
assert len(source_inventory)==7
checks.append({'command':'bounded complete v2/src file census + source inspection + accepted _REVIEW.md anticipated-artifact and software-workflow checks','cwd':'.','environment':{},'exit_code':0,'result':'Seven source modules: five initializers, typed registry port, JSON registry adapter. Accepted current review explicitly records reader/fixture suite not produced and AC-001..007 future production. Workflow registers no manifest reader method. No search miss alone supports disposition.'})
rows=list(csv.DictReader((OLD/'CLAIMS.csv').open()));res=list(csv.DictReader((OLD/'RESIDUALS.csv').open())); fields=list(rows[0]);rfields=list(res[0]);rec={x['ResidualID']:x for x in csv.DictReader((RUN/'RESIDUAL_RECOMMENDATIONS.csv').open()) if x['DeliverableID']=='DEL-02-07'}
maprows=[]
for r in res:
 oldgate=r['ExactGate'];r['ExactGate']=oldgate.replace('owner accepts calibration and separately authorizes exact Remaining application on origin/main','owner separately authorizes exact Remaining application on origin/main (D81 calibration acceptance effective through D82)')
 r['Notes']=rec[r['ResidualID']]['Recommendation']+'. '+rec[r['ResidualID']]['Reason']+' '+r['Notes']+' Raw proposal retained for provenance/reciprocity; not an applied Remaining item.'
 if r['ResidualID'].endswith('005'):r['ProposedText']='HELD ROUTING ONLY: truthful ResponsibleParty=TBD is documentary alignment; assignment remains at separately authorized WORKING_ITEMS activation. Do not mirror this concern into product Remaining.'
 if r['ResidualID'].endswith('006'):r['ProposedText']='HELD ROUTING ONLY: retain CLM-007 as accepted historical/future-contract phrasing; current upstream source existence is observable, but current-wording intent remains owner-held. No automatic SOW correction or reopening of ordinary currency.'
 if r['ResidualID'].endswith('007'):r['ProposedText']='HELD ROUTING ONLY: preserve CLM-011 as a dated foreign-corpus observation. Current reliance requires a separately scoped evidence refresh; no schema adoption or foreign production duty is inferred.'
 maprows.append({'ObjectID':r['ResidualID'],'OldID':r['ResidualID'],'NewID':r['ResidualID'],'OldDisposition':'RAW_PROPOSAL','NewDisposition':rec[r['ResidualID']]['Recommendation'],'Changes':'IDs and Depends preserved. Calibration prerequisite discharged by effective D82; exact application/source/scope conditions preserved. Held text made explicit.'})
rm={x['ResidualID']:x for x in res}
for row in rows:
 olddisp=row['Disposition'];local=row['ClaimID'].split('::')[1];row['SourceCommit']=BASE
 row['EvidenceReferences']+=';'+str(OUT/'REUSE_AUDIT.json')+';'+str(RUN/'RESIDUAL_RECOMMENDATIONS.csv')
 row['Notes']=row['Notes'].replace('R0 candidate convention.','D82 accepted conventions; R0 source identity revalidated.')+' Selected original R0 row preserved by identical ClaimID; read REUSE_MAP.csv for calibration changes. Current class qualification is not runtime acceptance.'
 if row['ProposedResidualID']:
  rr=rm[row['ProposedResidualID']];row['ExactGate']=rr['ExactGate'];row['ProposedResidualText']=rr['ProposedText'];row['Notes']+=' '+rec[row['ProposedResidualID']]['Recommendation']+'.'
 else:row['ExactGate']='NOT_SELECTABLE_UNTIL: separate owner authority for any future application or production; evidence classification only'
 if local=='TBD-001':
  row['ClaimClass']='DOCUMENTARY_PROVENANCE';row['Disposition']='ALIGNED';row['ImplementationEvidence']='Not applicable to truthful assignment statement; current Deliverables.csv retains ResponsibleParty=TBD.';row['VerificationEvidence']='Current SOW TBD-001 and Deliverables.csv agree: assignment is deferred to activation. No product implementation obligation follows from an unassigned field.'
 if local=='CLM-007':
  row['VerificationEvidence']='Reused R0 finite registry suite: 12 PASS at faf22452528b5ba895e88ba0ad3770855100de08; all source/default/schema/test/fixture inputs rehashed identical at effective D82 base. Not rerun here. This proves finite upstream behavior only, not manifest-reader behavior or source acceptance.'
  row['Notes']+=' Accepted phrase is retained as dated future-contract framing. UNKNOWN is current-reliance/wording qualification only; no automatic stale-text repair or reversal of acceptance.'
 if local=='CLM-011':row['Notes']+=' Two foreign paths remain outside this worker scope. UNKNOWN only for current census reliance; historical observation preserved.'
 if row['Disposition']=='DOCUMENTED_UNIMPLEMENTED':
  row['ImplementationEvidence']='Accepted current _REVIEW.md Gate 1 explicitly records Manifest reader + fixture tests NOT PRODUCED; SOW CLM-010 is a future-production contract. Complete current seven-module v2/src inspection confirms only registry port/JSON adapter and initializers; registered workflow has no reader suite. This conclusion uses positive documentary evidence plus complete bounded source inventory, not a search miss.'
  row['VerificationEvidence']='No DEL-02-07 execution evidence supplied: accepted _REVIEW.md AC-001..007 are addressed as future production contract, not PASS. VER obligations remain future finite methods; upstream 12-test registry result cannot satisfy them.'
 if row['ClaimClass']=='DOCUMENTARY_PROVENANCE' and local!='TBD-001':row['ImplementationEvidence']='Documentary boundary/traceability claim; accepted SOW and current cited decomposition/control hashes reproduce. Runtime production is separately assessed by REQ/AC/VER rows.'
 row['SourceHashes']=';'.join(p+'='+hashes[p] for p in [s.split('=',1)[0] for s in row['SourceHashes'].split(';')])
 maprows.append({'ObjectID':row['ClaimID'],'OldID':row['ClaimID'],'NewID':row['ClaimID'],'OldDisposition':olddisp,'NewDisposition':row['Disposition'],'Changes':'Exact local definition preserved; current source base and evidence reuse qualified; gates made literal. '+('Truthful assignment reclassified documentary ALIGNED; REM-005 held only.' if local=='TBD-001' else 'No disposition change.')})
# Independently derive local definitions; quoted upstream REQ IDs are excluded by anchored bullet syntax.
defs=re.findall(r'^- \*\*([A-Z]+-\d{3})\*\*', (DS/'ScopeOfWork.md').read_text(),re.M)
assert len(defs)==51 and len(set(defs))==51 and {'DEL-02-07::'+x for x in defs}=={r['ClaimID'] for r in rows}
assert sum(x.startswith(('REQ-','AC-','VER-')) for x in defs)==23
checks.append({'command':'anchored local SOW definition census / exact claim-set comparison','cwd':'.','environment':{},'exit_code':0,'result':'51/51 definitions covered; 23/23 REQ/AC/VER. Upstream quoted definitions and matrix references are nonlocal/nonduplicate.'})
csvwrite('CLAIMS.csv',fields,rows);csvwrite('RESIDUALS.csv',rfields,res);csvwrite('REUSE_MAP.csv',list(maprows[0]),maprows)
csvwrite('RESIDUAL_ROUTING.csv',['ResidualID','Recommendation','Reason','Selectability'],[{k:rec[x['ResidualID']][k] for k in ['ResidualID','Recommendation','Reason','Selectability']} for x in res])
dump('REUSE_AUDIT.json',{'selected_original_claims':sample['SelectedClaims'],'selected_original_sha256':sha(OLD/'CLAIMS.csv'),'original_claims':51,'original_residuals':7,'original_unknowns':4,'current_base':BASE,'original_manifest_base':oldm['base'],'rehashed_original_inputs':len(oldm['hashes']),'hash_deltas':deltas,'delta_routing':'Only decision-register successor D82; D81 calibration acceptance and D82 read afresh. All product/claim/method evidence identical. R0 decision register is historical, not current authority.','common_matching_inputs':len(overlap),'source_inventory':source_inventory,'finite_evidence_reuse':oldm['tests'],'finite_evidence_limit':'Historical finite registry run at R0 base, current compatible inputs proven; not rerun, no DEL-02-07 implementation verification and no all-input/normalization/containment guarantee.','lexical_containment_boundary':'PurePosixPath validation of the upstream locator is lexical; no filesystem containment or project resolution follows. Lexical normalization issue belongs to DEL-01-06 conditional reporting, not a new DEL-02-07 obligation.','source_unchanged':all(sha(p)==h for p,h in hashes.items())})
historical=[{'path':str(p),'commit':oldm['base'],'sha256':sha(p)} for p in OLD.glob('*') if p.is_file()]
historical += [{'path':x['path'],'commit':oldm['base'],'sha256':x['old_sha256']} for x in deltas]
# Existing evidence objects carry R0 source basis; their publication occurred at report commit, stated separately.
for h in historical:
 if h['path'].startswith(str(OLD)):h['commit']='bfbe4d356dcc322c36fcccff008df441f3c66331'
manifest={'source_commit':BASE,'hashes':dict(sorted(hashes.items())),'historical_sources':historical,'checks':checks,'source_unchanged':True}
dump('READ_MANIFEST.json',manifest)
counts=dict(collections.Counter(x['Disposition'] for x in rows)); census=dict(collections.Counter(x.split('-')[0] for x in defs))
(OUT/'COVERAGE.md').write_text(f'''# DEL-02-07 R1–R4 evidence coverage

Derivative audit under effective D82 base `{BASE}`, accepted decomposition revision 1.4 and exact Aug9 SOW `d044499ab5ace12305434ab3c7b5e17e21f730f8d77b45ff64c055d1edce2559`. Accepted R0 conventions apply through the append-only D81 calibration acceptance; historical candidate labels do not alter that act.

51/51 local definitions covered: {json.dumps(census)}. REQ/AC/VER coverage 23/23. Quoted upstream REQ-004/REQ-005 inside CLM-007 are source context; matrix references are links, not new claims. SOW-017 and objective/purpose scope are covered by CLM-001..003 and AC-008, with no fallback IDs needed. Dispositions: {json.dumps(counts)}. Seven raw residuals remain: four eligible for later exact application proposal, three held routing only. Four UNKNOWNs require ASSESSED_UNKNOWN; NONE is not warranted. Missing Remaining stays MISSING_SECTION / NOT_ASSESSED at entry.

## Current evidence and reuse

R0 selected original CLAIMS SHA `90e330c034a9a7a89accf737fc926632106693a9c55490722b55dbb4ad669931` reproduced. All {len(oldm['hashes'])} original read sources rehashed. Only the decision register changed, adding effective D82; new D81 acceptance and D82 ruling are read as current authority. {len(overlap)} COMMON-overlapping inputs match. REUSE_AUDIT.json records complete source inventory, exact delta and finite-test reuse; REUSE_MAP.csv maps all 51 old/new claim IDs and seven residual IDs without renumbering.

Positive accepted _REVIEW anticipated-artifact nonproduction, SOW CLM-010 future-contract statement, complete seven-module source inspection and registered workflow are concordant. DOCUMENTED_UNIMPLEMENTED uses this combined evidence, not a failed source search. No old frozen PEC code counts as current implementation. The 12-test upstream registry result is reused with unchanged source/schema/default/test/fixture hashes and remains finite upstream evidence only; no DEL-02-07 VER was executed or passed. Lexical path checking is distinct from normalization policy, filesystem containment and loop/project resolution.

AC-008 remains ALIGNED human-review provenance: exact accepted SOW bytes, reviewed scope traceability and resolved RF-001/RF-002 reproduce. Acceptance covers the same SOW semantics, not source implementation or Gate 5. Twenty-one ALIGNED rows are documentary/human provenance, never product completion. TBD-001 is now documentary ALIGNED under accepted convention; its original raw assignment concern remains REM-005 HELD_ROUTING_ONLY, not a recommended product item.

CLM-007 remains UNKNOWN only for current-reliance qualification: existing typed port/loader/default do not force accepted future-production phrasing to be edited or reverse acceptance. REM-006 is held. CLM-011 is a dated foreign-corpus observation, not a fresh census; REM-007 remains held and no foreign discovery or schema adoption is inferred. TBD-003 and CON-002 preserve the unknown loop-to-project relation. REM-002 product proposal remains conditional on accepted resolution or scope change; the LoopRegistry locator is not an accepted derivation by itself.

## Dependency, authority and handoff

Only REM-002 names Depends DEL-01-06. DEP-02-07-003 is ACTIVE PREREQUISITE PENDING, so it blocks that named candidate under LOOP_INIT; observed predecessor files never flip its register. All other Depends are NONE. Calibration acceptance is now effective but exact Remaining application, source/test paths, administrative activation, contract wording, scope, lifecycle and reliance each retain their own owner gate. Owner acts require origin/main evidence; branch-observable predecessor checks cannot replace acceptance. Three exact project-relative file candidate-validation preflights returned ALLOW; header-only active holds do not grant production.

Ordinary SCA-004/Aug9 currency is complete. Frozen CHECKING/ISSUED elsewhere remains intact; this deliverable stays INITIALIZED/GATE_5_UNENTERED. TM023 dedicated mapping stays held without unrelated gates, TM022 deferred, PRDv2.3/DPEC79 adopted-not-applied, no retired plan resurrection. No TM/assignment mirror, source or target file was written.

Worker audit complete for fresh independent package verification; authoritative truth unchanged, required worker derivative current, package aggregation/verification pending parent. Closure means report readiness only. Rerun affected evidence on source, scope, hold, acceptance or convention drift, newly authorized foreign census or accepted loop/project resolution. Write allowlist: `{OUT}/**`. Actual role /root/pec_pkg02_reconciliation/del0207 is delegated-harness-native Agent2, instruction-asserted, no delegation.
''')
(OUT/'RETURN.md').write_text(f'''# DEL-02-07 worker return

COMPLETE_FOR_INDEPENDENT_PACKAGE_VERIFICATION / ASSESSED_UNKNOWN. 51 claims, 23 REQ/AC/VER, seven raw residuals (four eligible later exact application proposals / three held), four UNKNOWNs. Dispositions {json.dumps(counts)}. Exact IDs and reciprocal links preserved; TBD-001 calibrated to documentary ALIGNED and held assignment routing.

Accepted upstream: D82 effective `{BASE}`, D81 calibration acceptance, revision1.4 and exact Aug9 SOW. Selected R0 source SHA revalidated; all {len(oldm['hashes'])} original read hashes checked, only expected decision-register successor. Current product/test sources identical; historical 12-test registry evidence reused, no gratuitous suite run. Source unchanged. REUSE_AUDIT.json and REUSE_MAP.csv provide traceable selection and changes.

CLAIMS.csv / RESIDUALS.csv / COVERAGE.md / READ_MANIFEST.json are the worker contract; RESIDUAL_ROUTING.csv, REUSE_AUDIT.json and REUSE_MAP.csv retain four eligible versus three held distinction. VALIDATION.json records deterministic validation. OUTPUT_MANIFEST.json hashes final outputs, excluding itself. Parent must dispatch independent verification and perform fan-in; no repair/application or product closure claimed.

Blocking questions: loop-to-project accepted resolution; current reliance interpretation of CLM-007 and foreign-census CLM-011. Exact owner/application/source/lifecycle/reliance gates persist; REM-002 additionally names ACTIVE PREREQUISITE PENDING DEL-01-06. No unknown disappears into NONE. Rehash and repeat actual hold act on source/authority/hold drift.

Write allowlist `{OUT}/**`; no target/control/foreign/source/Git/network/service mutations. Runtime identity /root/pec_pkg02_reconciliation/del0207; native Agent2 instruction-asserted, no children. This is a current derivative pending independent package verification, not decomposition authority.
''')
assert all(sha(p)==h for p,h in hashes.items())
print(json.dumps({'claims':len(rows),'residuals':len(res),'counts':counts,'read_hashes':len(hashes),'original_rehash':len(oldm['hashes']),'common_match':len(overlap)}))
