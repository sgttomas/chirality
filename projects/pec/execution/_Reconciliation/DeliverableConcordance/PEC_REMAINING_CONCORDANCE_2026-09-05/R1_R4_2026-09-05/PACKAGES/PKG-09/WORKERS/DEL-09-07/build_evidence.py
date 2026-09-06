import pathlib,hashlib,json,csv,subprocess,os,re
R=pathlib.Path.cwd(); B='2be412ccea62bdc4bd96deb082c46d7a792076ea'; D='DEL-09-07'
run=pathlib.Path('projects/pec/execution/_Reconciliation/DeliverableConcordance/PEC_REMAINING_CONCORDANCE_2026-09-05'); pkg=run/'R1_R4_2026-09-05/PACKAGES/PKG-09'; out=pkg/'WORKERS'/D; target=pathlib.Path('projects/pec/execution/PKG-09_Dashboards/1_Working/DEL-09-07_Explain_shaped_pressure_rules')
hashes={}; checks=[]; binding={}; manifests={}
for p in [pkg/'SOURCE_MANIFEST.json',run/'R1_R4_2026-09-05/COMMON/SOURCE_MANIFEST.json']:
 x=json.loads(p.read_text()); manifests.update(x['hashes'])
def read(p):
 p=pathlib.Path(p); data=p.read_bytes(); hashes[str(p)]=hashlib.sha256(data).hexdigest(); return data.decode()
def check(cmd):
 c=subprocess.run(cmd,capture_output=True,text=True,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'}); checks.append(dict(command=cmd,cwd=str(R),environment={'PYTHONDONTWRITEBYTECODE':'1'},exit_code=c.returncode,result=c.stdout+c.stderr)); return c
sources=['AGENTS.md','projects/pec/AGENTS.md','agents/AGENT_RECONCILIATION.md','docs/DELIVERABLE_CONCORDANCE_METHOD.md','projects/pec/loop/LOOP_INIT.md','projects/pec/docs/PRD.md','projects/pec/execution/_Scripts/pec_reliance_hold.py','projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv','projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md','projects/pec/execution/_Decomposition/Deliverables.csv','projects/pec/execution/_Decomposition/ScopeLedger.csv','projects/pec/execution/_Decomposition/_LATEST.md','projects/pec/execution/_Coordination/PEC_CURRENCY_REPAIR_CLOSEOUT_2026-08-09/HANDOFF_STATE.md']
sources += [str(p) for p in (pathlib.Path('projects/pec/execution/_Coordination/_DECISIONS')).glob('D-PEC-8[12]*.md')]
sources += [str(run/'CONVENTIONS.md')]+[str(pkg/p) for p in ['PACKAGE_BASIS.md','SOURCE_MANIFEST.json','PREFLIGHT.json','BRIEFS/DEL-09-07.md','BRIEF_CLARIFICATION_02.md']]+[str(run/'R1_R4_2026-09-05/COMMON'/p) for p in ['RUN_BASIS.md','SOURCE_MANIFEST.json','SCOPE_CENSUS.csv','AGENT0_GRAPH.md','BRIEF_CLARIFICATION_01.md']]
sources += [str(p) for p in target.rglob('*') if p.is_file()]
for p in sources:
 if p.startswith('projects/pec/') and '/R1_R4_' not in p:
  c=check(['python3','projects/pec/execution/_Scripts/pec_reliance_hold.py','--register','projects/pec/execution/_Coordination/ACTIVE_RELIANCE_HOLDS.csv','--target',p.removeprefix('projects/pec/'),'--operation','candidate-validation']); assert c.returncode==0
 read(p)
c=check(['rg','-n','Explain|pressure|stuck|gate.blocked|drift|staleness|collision|DEL-09-07|PEC-DSH-007','projects/pec/v2']); assert c.returncode in (0,1)
# Every file searched is hashed and bound, without executing product or fixtures.
for p in pathlib.Path('projects/pec/v2').rglob('*'):
 if p.is_file(): read(p)
review_files=sorted(str(p) for p in pathlib.Path('projects/pec/execution/_Evaluation/Reviews').rglob('*') if p.is_file() and 'DEL-09-07' in str(p))
for p in review_files: read(p)
checks.append(dict(command='bounded review-path inventory for DEL-09-07',cwd=str(R),environment={},exit_code=0,result=review_files))
for p,h in hashes.items():
 if p in manifests: assert manifests[p]==h,p; binding[p]='common-or-package frozen manifest matches'
 elif '/R1_R4_' in p: binding[p]='current run derivative/context; not claimed committed source'
 else:
  c=subprocess.run(['git','show',B+':'+p],capture_output=True); ok=c.returncode==0 and hashlib.sha256(c.stdout).hexdigest()==h; assert ok,p
  checks.append(dict(command=['git','show',B+':'+p],cwd=str(R),environment={},exit_code=c.returncode,result={'sha256':h,'matches_current':ok})); binding[p]='git show exact base match'
cols='ClaimID,DeliverableID,ClaimClass,NormativeSource,ScopeItemIDs,DeclaredSource,CurrentState,ImplementationEvidence,VerificationEvidence,ValidationOrProvenanceEvidence,LifecycleEvidence,ExistingRemaining,Disposition,ProposedResidualID,ProposedResidualText,Depends,ExactGate,AuthorityNeeded,Selectability,SourceCommit,SourceHashes,EvidenceReferences,Notes'.split(',')
rcols='ResidualID,DeliverableID,ClaimIDs,ProposedText,Depends,ExactGate,ClosureEvidence,AuthorityNeeded,Selectability,Notes'.split(',')
rows=[]; residuals=[]; mappings=[]
gate='(gated: exact owner application of Remaining; any production requires its separately ruled packet and source-fence opening; lifecycle and reliance gates preserved)'
ledger='projects/pec/execution/_Decomposition/ScopeLedger.csv'; decomp='projects/pec/execution/_Decomposition/SOFTWARE_DECOMP.md'; prd='projects/pec/docs/PRD.md'
quote=next(x for x in read(ledger).splitlines() if x.startswith('SOW-051,'))
def add(local,cl,text,disp='ALIGNED',src=None,res='',note=''):
 src=src or ledger; cid=D+'::'+local
 row=dict.fromkeys(cols,''); row.update(ClaimID=cid,DeliverableID=D,ClaimClass=cl,NormativeSource=src,ScopeItemIDs='SOW-051',DeclaredSource=str(target/'_CONTEXT.md'),CurrentState=text,ImplementationEvidence='UNKNOWN: bounded current v2 search identifies no claim-specific implementation; absence is not proof of nonimplementation' if disp=='UNKNOWN' else 'Not asserted by documentary claim',VerificationEvidence='READ_MANIFEST.json: exact source rehash, base binding and bounded inspection; no behavior suite claimed',ValidationOrProvenanceEvidence='Accepted revision 1.4 scope; D81 conventions accepted by append-only record; D82 read-only grant',LifecycleEvidence=str(target/'_STATUS.md')+' OPEN; no promotion asserted',ExistingRemaining='No Remaining section; no NONE conclusion',Disposition=disp,ProposedResidualID=res,Depends='NONE',ExactGate=gate,AuthorityNeeded='Owner application; separately scoped production and REVIEW where applicable',Selectability='NON_SELECTABLE_PENDING_OWNER_APPLICATION',SourceCommit=B,SourceHashes=json.dumps({src:hashes[src]},sort_keys=True),EvidenceReferences='READ_MANIFEST.json; FALLBACK_SOURCE_MAPPING.json; '+src,Notes=note)
 rows.append(row)
 source_lines=pathlib.Path(src).read_text().splitlines()
 key=local if local.startswith(('PEC-','DEP-')) else ('DEL-09-07,' if src.endswith('Deliverables.csv') else 'Current State' if local=='LIFECYCLE' else 'ResponsibleParty' if local=='ASSIGNMENT' else local)
 exact=quote if src==ledger else next(line for line in source_lines if key in line)
 if local.startswith('DEP-'): row['ImplementationEvidence']='Not asserted; UNKNOWN applies to unresolved owner classification, not product implementation'
 mappings.append(dict(claim_id=cid,source=src,locus='line '+str(source_lines.index(exact)+1),quote=exact,quote_sha256=hashlib.sha256(exact.encode()).hexdigest(),mapping_kind='run-local fallback; not a new normative ID'))
r1=D+'-REM-001'
for i,rule in enumerate(['stuck-in-state age','gate-blocked','drift density','staleness','collision risk'],1): add('SOW-051-RULE-'+str(i).zfill(2),'observed behavior','Accepted scope requires '+rule+' pressure/status rule; current implementation and tests unresolved','UNKNOWN',res=r1)
add('PEC-DSH-007-DOC','documentary alignment','Each of the five rules is individually documented; current rule documents not established','UNKNOWN',res=r1)
add('PEC-K-08','observed behavior','Explain rule ID, threshold and contributing cited sources for each derived status/verdict/warning; drill-down never dead-ends','UNKNOWN',prd,r1)
add('RENDER-CONSUMERS','observed behavior','Rules are rendered by DEL-09-01..05 views; rule backend ownership stays DEL-09-07','UNKNOWN','projects/pec/execution/_Decomposition/Deliverables.csv',r1)
for local,text in [('PEC-K-01','No governed act may require PEC; deleting PEC blocks nothing; kill test remains standing release gate'),('PEC-K-02','PEC output is non-authoritative; rulings and lifecycle remain file-native'),('PEC-K-03','Consumer owns whether/when to consume labeled data; verify-before-rely is an injection precondition; injection not required'),('PEC-K-06','Advisory observation only: no arbitration, locks or dispatch; collisions surfaced and never prevented'),('PEC-K-11','Mode-capable and never forced; consumer owns cadence; zero-contact operation preserved')]: add(local,'documentary alignment',text,src=prd,note='Boundary recorded, not verified runtime compliance or release PASS')
add('LIFECYCLE','lifecycle','Current State OPEN with PREPARATION history on 2026-07-25',src=str(target/'_STATUS.md'))
add('ASSIGNMENT','documentary alignment','ResponsibleParty TBD; assignment at WORKING_ITEMS activation is truthful documentary state',src=str(target/'_CONTEXT.md'),note='No automatic TM or assignment residual')
deps=list(csv.DictReader(read(target/'Dependencies.csv').splitlines()))
for d in deps:
 flag=d['DependencyID'] in ['DEP-09-07-003','DEP-09-07-008']; rid=D+'-REM-'+('002' if d['DependencyID'].endswith('003') else '003') if flag else ''
 add(d['DependencyID'],'documentary alignment',d['Statement']+'; '+d['Status']+'/'+d['DependencyType']+'/'+d['SatisfactionStatus'],'UNKNOWN' if flag else 'ALIGNED',str(target/'Dependencies.csv'),rid,note=d['Notes']+'; '+('Owner classification remains unresolved; no register flip.' if flag else 'Register observation only, not predecessor satisfaction.'))
for rid,txt,closure,notes in [(r1,'Establish current source-bound implementation, individual rule documentation, Explain citations and claim-relevant test evidence for all five SOW-051 rules and view integration; return unknowns to owner without inferring production absence.','Exact current artifact/source/test locators for all five rules, evidence limits and acceptance continuity, or owner-ruled disposition.','Evidence-only candidate; production prerequisites remain DEL-09-06;DEL-04-03;DEL-03-01;DEL-03-03;DEL-05-01;DEL-06-06 and are not imposed on discovery.'),(D+'-REM-002','Route DEP-09-07-003 shared drill-down applicability ambiguity to owner; preserve pending edge until separately ruled.','Owner ruling on E-A11 applicability and exact authorized register application.','Held routing question; not automatic executable Remaining.'),(D+'-REM-003','Route DEP-09-07-008 P3 producer/P2 consumer classification to owner, preserving staged rule set versus soft edge alternatives.','Owner classification for E-P69 and exact authorized register application.','Held routing question; no silent phase reordering.')]:
 claims=[r['ClaimID'] for r in rows if r['ProposedResidualID']==rid]; residuals.append(dict(zip(rcols,[rid,D,';'.join(claims),txt,'NONE',gate,closure,'Owner ruling and exact application','NON_SELECTABLE_PENDING_OWNER_APPLICATION',notes])))
 for r in rows:
  if r['ProposedResidualID']==rid:r['ProposedResidualText']=txt
for f,data,fields in [('CLAIMS.csv',rows,cols),('RESIDUALS.csv',residuals,rcols)]:
 with (out/f).open('w',newline='') as h:w=csv.DictWriter(h,fields,lineterminator='\n');w.writeheader();w.writerows(data)
(out/'FALLBACK_SOURCE_MAPPING.json').write_text(json.dumps({'source_commit':B,'missing_contract':str(target/'ScopeOfWork.md'),'scope_quote':quote,'scope_quote_sha256':hashlib.sha256(quote.encode()).hexdigest(),'scope_locus':'ScopeLedger.csv row SOW-051; SOFTWARE_DECOMP.md §scope table SOW-051; PRD PEC-DSH-007','mappings':mappings,'nonclaims':'No locally defined REQ/AC/VER IDs. SOW-051 and PEC-DSH-007 split into five rule claims plus documentation; PEC-K-08 explicitly behavioral. OBJ-004 is supporting objective, PKG-09/DEL IDs identity; BACKEND_FEATURE_SLICE/M/P2 are envelope/phase metadata, not independently invented product work. DEP-09-07-001..008 fully covered; E IDs and C-04/C-10 are dependency provenance/ordering constraints retained in ledger notes and coverage.'},indent=2)+'\n')
assert all(hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()==h for p,h in hashes.items())
checks.append(dict(command='worker schema, reciprocal IDs, LF and source stability validation',cwd=str(R),environment={},exit_code=0,result={'claims':len(rows),'residuals':len(residuals),'source_unchanged':True,'base_binding':binding}))
(out/'READ_MANIFEST.json').write_text(json.dumps(dict(source_commit=B,hashes=hashes,historical_sources=[],checks=checks,source_unchanged=True),indent=2)+'\n')
(out/'COVERAGE.md').write_text('''# DEL-09-07 coverage

ASSESSED_UNKNOWN. 23 claims: 13 documentary/lifecycle ALIGNED and 10 UNKNOWN; three nonselectable proposals (one evidence candidate, two held owner questions). No warranted NONE. All five rules, individual documentation, Explain fields/citations and consumer rendering are separately assessed. No local REQ/AC/VER IDs or ScopeOfWork.md exists; immutable fallback mapping binds SOW-051 and source vocabulary. Dependency IDs 001–008 all preserved.

Current v2 bounded content search has no relevant rule hit; this cannot prove DOCUMENTED_UNIMPLEMENTED. Current member contains scaffold files plus D65 dependency-repair run record, no production acceptance or relevant test run. Member REVIEW path search has no match; the initial wrong _Review directory query was corrected to _Evaluation/Reviews, no acceptance inference from either absence. No finite product suite was run without a claim-relevant method. Frozen source remains history only and was not mined as current implementation.

Dependencies 003–008 are ACTIVE PREREQUISITE / PENDING at INITIALIZED. Only an item's named Depends conjunction blocks that item. Evidence proposals have Depends NONE. Future production retains exact targets DEL-09-06, DEL-04-03, DEL-03-01, DEL-03-03, DEL-05-01, DEL-06-06. E-A11 applicability is ambiguous; E-P69 phase tension explicitly retains staged rule set versus soft edge. C-04 ordering is owner classified; C-10 strata are provenance, not authority. Neither rule output nor blocker visibility assigns work. Consumer use/cadence remains consumer-owned and optional.

OPEN remains documentary lifecycle truth. No artifact acceptance, lifecycle reversal, source opening, release or reliance is inferred. Ordinary SCA004 currency is complete by August9 closeout despite historical _LATEST prose; TM023 remains dedicated held mapping without unrelated gate, TM022 deferred, PRDv2.3/DPEC79 adopted-not-applied. No automatic TM mirrors.

Every read byte source is hashed and matched against frozen manifests or exact base git show; current run derivatives are explicitly labeled. Holds preflight independently returned ALLOW for exact source files; no source gate waived. Source unchanged. Derivative report only, pending independent package verification. Rerun on material source/authority/hold change, new accepted implementation/test evidence, or exact owner classification; next owner is package RECONCILIATION.
''')
assert len(rows)==23 and sum(r['Disposition']=='UNKNOWN' for r in rows)==10
assert len({r['ClaimID'] for r in rows})==len(rows)
for rr in residuals:
 assert re.fullmatch(r'DEL-09-07-REM-[0-9]{3}',rr['ResidualID'])
 assert set(rr['ClaimIDs'].split(';'))=={r['ClaimID'] for r in rows if r['ProposedResidualID']==rr['ResidualID']}
for r in rows+residuals:
 assert r['Depends']=='NONE' and r['ExactGate'].startswith('(gated: ')
for fn,fields in [('CLAIMS.csv',cols),('RESIDUALS.csv',rcols)]:
 assert b'\r' not in (out/fn).read_bytes()
 assert next(csv.reader((out/fn).open()))==fields
outs={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.iterdir() if p.is_file() and p.name!='RETURN.md'}
(out/'RETURN.md').write_text('# Terminal Agent2 return — DEL-09-07\n\nCOMPLETE_FOR_PACKAGE_VERIFICATION / ASSESSED_UNKNOWN. 23 claims, 13 ALIGNED (class-qualified), 10 UNKNOWN, 3 residual proposals; NONE not warranted. All source hashes rechecked unchanged. No product tests or behavior PASS asserted.\n\nAccepted upstream: D82 effective '+B+'; D81 accepted conventions and revision1.4 decomposition. This is a derivative evidence packet, not authority or Remaining application. Independent verification pending. Production, source, lifecycle, release and reliance gates survive. Exact write allowlist: '+str(out)+'/** only. Native role instruction-asserted; child /root/pec_pkg09_reconciliation/worker_07, parent /root/pec_pkg09_reconciliation; no delegation. No historical source relabeled current.\n\nRerun triggers and remaining owner questions: COVERAGE.md. Selected outputs and hashes:\n\n'+''.join('- '+n+': `'+h+'`\n' for n,h in sorted(outs.items())))
print(json.dumps({'claims':len(rows),'unknown':10,'residuals':len(residuals),'hashes':outs},indent=2))
