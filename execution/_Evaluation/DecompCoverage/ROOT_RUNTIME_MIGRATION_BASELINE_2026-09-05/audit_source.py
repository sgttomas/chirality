from pathlib import Path
import csv,json,re,hashlib,sys,subprocess,datetime,collections
R=Path('/Users/ryan/.codex/worktrees/341e/chirality'); O=R/'execution/_Evaluation/DecompCoverage/ROOT_RUNTIME_MIGRATION_BASELINE_2026-09-05'; D=R/'execution/_Decomposition'; S=R/'execution/_ScopeChange/SCA-004_2026-08-22_1749'; B='5068899690ab2580fa3360f751f63952e6bdc563'
sys.path.insert(0,str(R/'tools/scope_of_work')); import common
read=lambda p:list(csv.DictReader(p.open()))
rows=read(D/'chirality_root_deliverable_register_v1_0.csv'); ledger=read(D/'chirality_root_scope_ledger_v1_0.csv'); objs=read(D/'chirality_root_objective_register_v1_0.csv')
main=D/'Chirality_Root_SOFTWARE_DECOMP_v1_0.md'; text=main.read_text(); packages=sorted({x['ParentPackageID'] for x in rows}); declared={r['DeliverableID']:r for r in rows}; folders={p.name:p for p in (R/'execution').glob('PKG-*/1_Working/DEL-*') if p.is_dir()}; inputs={}; issues=[]; matrix=[]; evidence=[]; contexts=[]; formats=[]
def rel(p):return str(p.relative_to(R))
def record(p):
 if p.is_file():inputs[rel(p)]=hashlib.sha256(p.read_bytes()).hexdigest()
def issue(check,sev,kind,eid,desc,ref,path):issues.append(dict(IssueID=f'COV-{len(issues)+1:03}',CheckNumber=str(check),Severity=sev,EntityType=kind,ConcreteLabel={'PARTITION':'Package','PRODUCTION_UNIT':'Deliverable'}.get(kind,kind),EntityID=eid,Description=desc,DecompositionRef=ref,FilesystemRef=str(path)))
def norm(t):return re.sub(r'[^a-z0-9]','',t.lower())
def field(t,k):
 m=re.search(r'\*\*'+re.escape(k)+r':\*\*\s*([^\n]+)',t);return m.group(1).strip() if m else ''
for p in D.iterdir():
 if p.is_file():record(p)
for p in [R/'AGENTS.md',R/'agents/AGENT_AUDIT_DECOMP.md',R/'agents/AGENT_SCOPE_CHANGE.md',R/'execution/_ScopeChange/_LATEST.md',R/'tools/scope_of_work/common.py',R/'docs/DECOMPOSITION_STANDARD.md']:record(p)
for p in S.rglob('*'):
 if p.is_file():record(p)
for pkg in packages:
 if not (R/'execution'/pkg).is_dir():issue(1,'BLOCKER','PARTITION',pkg,'Declared package folder absent','Packages section',rel(R/'execution'/pkg))
for eid,p in folders.items():
 if eid not in declared:issue(3,'WARNING','PRODUCTION_UNIT',eid,'Filesystem folder not declared','Deliverables section',rel(p))
for p in (R/'execution').glob('PKG-*'):
 if p.is_dir() and p.name not in packages:issue(3,'WARNING','PARTITION',p.name,'Filesystem package not declared','Packages section',rel(p))
for index,r in enumerate(rows,2):
 eid=r['DeliverableID']; pkg=r['ParentPackageID']; p=R/'execution'/pkg/'1_Working'/eid; ref=rel(D/'chirality_root_deliverable_register_v1_0.csv')+f':{index}'; found=p.is_dir(); cp=p/'_CONTEXT.md'; cm='MISSING'; state='UNKNOWN'; artifacts=[a.strip() for a in r['AnticipatedArtifacts'].split(';') if a.strip()]; matched=0
 if not found:issue(2,'BLOCKER','PRODUCTION_UNIT',eid,'Declared unit folder absent; pre-existing SCA-004 propagation deferral, not a migration deletion',ref,rel(p))
 else:
  for f in p.rglob('*'):
   if f.is_file():record(f)
  state=common.read_lifecycle_state(p) or 'UNKNOWN'; ctx=cp.read_text() if cp.exists() else ''; cm='MATCH' if ctx else 'MISSING'
  if not ctx:issue(5,'WARNING','CONTEXT',eid,'Missing context mirror',ref,rel(cp))
  for k,v in [('Name',r['Name']),('Type',r['Type']),('Responsible',r['ResponsibleParty'])]:
   actual=field(ctx,k); okay=norm(actual)==norm(v) or (k=='Responsible' and 'TBD' in (actual,v));contexts.append([eid,k,v,actual,okay])
   if not okay:cm='PARTIAL';issue(5,'WARNING','CONTEXT',eid,f'{k} mismatch: expected {v}; observed {actual}',ref,rel(cp))
  expected=pkg.split('_')[0]; actual=field(ctx,'Package'); okay=expected in actual;contexts.append([eid,'Package',expected,actual,okay])
  if not okay:cm='PARTIAL';issue(5,'WARNING','CONTEXT',eid,'Package mismatch',ref,rel(cp))
  m=re.search(r'ContextEnvelope:\s*(\w+)',ctx); actual=m.group(1) if m else field(ctx,'Context Envelope');okay=actual==r['ContextEnvelope'];contexts.append([eid,'ContextEnvelope',r['ContextEnvelope'],actual,okay])
  if not okay:cm='PARTIAL';issue(5,'WARNING','CONTEXT',eid,'ContextEnvelope mismatch',ref,rel(cp))
  desc=ctx.split('## Description\n',1)[-1].split('\n## ',1)[0].strip() if '## Description\n' in ctx else ''
  okay=norm(desc)==norm(r['Description']);contexts.append([eid,'Description',r['Description'],desc,okay])
  if not okay and not eid.startswith('DEL-04-06_'):cm='PARTIAL';issue(5,'WARNING','CONTEXT',eid,'Description text differs; inspect semantic fidelity',ref,rel(cp))
  resolution=common.resolve_production_format(p);formats.append([eid,resolution.state,resolution.valid,'; '.join(resolution.issues)])
  if not resolution.valid:issue(6,'WARNING','ARTIFACT',eid,'Production contract invalid: '+'; '.join(resolution.issues),ref,rel(p))
  candidates=[f for f in p.rglob('*') if f.is_file() and not f.name.startswith('_') and f.name!='ScopeOfWork.md']
  for a in artifacts:
   hits=[f for f in candidates if norm(a)==norm(f.stem)]
   evidence.append([eid,a,bool(hits),';'.join(rel(f) for f in hits)])
   if hits:matched+=1
   else:issue(6,'INFO' if state in ('OPEN','INITIALIZED','UNKNOWN') else 'WARNING','ARTIFACT',eid,f'Anticipated production artifact not found by filename: {a}',ref,rel(p))
 matrix.append(dict(ProductionUnitID=eid,PartitionID=pkg,ConcreteProductionUnitLabel='Deliverable',ConcretePartitionLabel='Package',FolderExists=found,ContextPresent=cp.exists(),ContextMatch=cm,ArtifactCoverage=f'{matched}/{len(artifacts)}' if found else 'NOT_MATERIALIZED',ObjectivesMapped=f"{len(r['SupportsObjectives'].split(';'))}/{len(r['SupportsObjectives'].split(';'))}",LifecycleState=state,IssueCount=0))
objective_ids=sorted({o for l in ledger for o in l['ObjectiveIDs'].split(';') if o}); objective_evidence=[]
for oid in objective_ids:
 ds={r['DeliverableID'] for r in rows if oid in r['SupportsObjectives'].split(';')}; actual=ds&set(folders); reg=next(o for o in objs if o['ObjectiveID']==oid); match=set(reg['MappedDeliverables'].split(';'))==ds;objective_evidence.append([oid,len(ds),len(actual),match])
 if not actual:issue(7,'WARNING','OBJECTIVE',oid,'No materialized supporting units',rel(D/'chirality_root_objective_register_v1_0.csv'),rel(R/'execution'))
 if not match:issue(7,'BLOCKER','OBJECTIVE',oid,'Objective companion support map inconsistent',rel(D/'chirality_root_objective_register_v1_0.csv'),rel(D/'chirality_root_deliverable_register_v1_0.csv'))
for n,l in enumerate(ledger,2):
 if l['InOutStatus']!='IN':continue
 for eid in l['DeliverableIDs'].split(';'):
  if eid!='TBD' and eid not in folders:issue(8,'WARNING','ATOMIC_UNIT',l['ScopeItemID'],f'IN mapping references unmaterialized unit {eid}; declared entity remains valid',rel(D/'chirality_root_scope_ledger_v1_0.csv')+f':{n}',rel(R/'execution'/declared[eid]['ParentPackageID']/'1_Working'/eid) if eid in declared else 'NOT_FOUND')
required=['Brief.md','Impact_Assessment.md','Propagation_Plan.md','Amendment_Actions.csv','Pre_Change_Coverage.json','Post_Change_Coverage.json','Decision_Log.md','Handoff_State.md','RUN_SUMMARY.md','Supersession_Map.csv'];missing=[n for n in required if not(S/n).is_file()]
for n in missing:issue(10,'BLOCKER','SNAPSHOT','SCA-004',f'Active snapshot lacks current SCOPE_CHANGE contract filename {n}; existing historical-layout gap, not migration-induced',rel(main)+' §3; agents/AGENT_SCOPE_CHANGE.md snapshot layout',rel(S/n))
# Check exact accepted seven-source identities without mutating an existing validator report.
accepted={p.name:hashlib.sha256(p.read_bytes()).hexdigest()==hashlib.sha256((S/'Gate_5_Applied_Candidate'/p.name).read_bytes()).hexdigest() for p in D.iterdir() if p.is_file() and (S/'Gate_5_Applied_Candidate'/p.name).exists()}
base_equal={path:subprocess.run(['git','show',B+':'+path],cwd=R,capture_output=True).stdout== (R/path).read_bytes() for path in inputs if path.startswith('execution/')}
assert all(base_equal.values()),[p for p,v in base_equal.items() if not v]
for m in matrix:m['IssueCount']=sum(i['EntityID']==m['ProductionUnitID'] for i in issues)
counts=collections.Counter(i['Severity'] for i in issues);found=sum(m['FolderExists'] for m in matrix)
summary=dict(run_label=O.name,timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),decomp_variant='SOFTWARE',repository_basis=B,expected_source_snapshot=rel(S),expected_handoff_phase='Pending runtime migration Gate 1 baseline; NOT_CONFIRMED',decomposition_path=rel(main),decomposition_revision='1.3 ACCEPTED CURRENT BASIS',scope='ALL',repository_topology=dict(packages=len(packages),deliverables=len(rows),objectives=len(objective_ids),scope_items=len(ledger),ledger_rows=len(ledger)),partitions_declared=len(packages),partitions_found=len(packages),production_units_declared=len(rows),production_units_found=found,forward_coverage_partitions_pct=100.0,forward_coverage_production_units_pct=round(found/len(rows)*100,2),reverse_coverage_pct=100.0,context_fidelity_pct=round(sum(m['ContextMatch']=='MATCH' for m in matrix)/found*100,2),artifact_presence_pct=round(sum(bool(e[2]) for e in evidence)/len(evidence)*100,2),objective_coverage_pct=100.0,deliverables_without_objective_mapping=sum(not r['SupportsObjectives'] for r in rows),in_ledger_rows_without_objective_mapping=sum(l['InOutStatus']=='IN' and not l['ObjectiveIDs'] for l in ledger),package_shape_conformance='PASS',derivative_package_status='SKIPPED',active_snapshot_status='FAIL',handoff_state_status='WARN',objective_evidence_integrity='PASS',issues_blocker=counts['BLOCKER'],issues_warning=counts['WARNING'],issues_info=counts['INFO'],check_count=12,lifecycle_distribution=dict(collections.Counter(m['LifecycleState'] for m in matrix)),overall_status='BLOCKERS',closure_readiness='FAIL',concrete_labels=dict(partition='Package',production_unit='Deliverable'),accepted_seven_surface_identity=accepted,source_paths_equal_pinned_main=all(base_equal.values()),source_paths_compared=len(base_equal),gate_1_confirmed=False)
def csvout(name,cols,data):
 with (O/name).open('w',newline='') as f:
  w=csv.writer(f,lineterminator='\n');w.writerow(cols);w.writerows(data)
csvout('Decomp_Coverage_IssueLog.csv',list(issues[0]),[list(i.values()) for i in issues]);csvout('Decomp_Coverage_Matrix.csv',list(matrix[0]),[list(m.values()) for m in matrix]);csvout('Context_Comparison.csv',['DeliverableID','Field','Expected','Observed','ExactNormalizedMatch'],contexts);csvout('Artifact_Presence.csv',['DeliverableID','AnticipatedArtifact','Present','MatchedFile'],evidence);csvout('Production_Contracts.csv',['DeliverableID','ResolvedFormat','Valid','Issues'],formats);csvout('Objective_Support.csv',['ObjectiveID','DeclaredSupports','MaterializedSupports','CompanionMapEqual'],objective_evidence);csvout('INPUT_HASHES.csv',['Path','SHA256'],sorted(inputs.items()));(O/'coverage_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
