from pathlib import Path
import csv,json,re,hashlib,sys,collections,datetime
R=Path('/Users/ryan/.codex/worktrees/341e/chirality'); P=R/'projects/chirality-runtime'; E=P/'execution'; D=E/'_Decomposition'; G=R/'execution/_ScopeChange/SCA-005_2026-09-06_GATE4_PLAN'; RUN=R/'execution/_Coordination/AgentRuns/ROOT_RUNTIME_MIGRATION_GATE5_2026-09-06'; O=E/'_Evaluation/DecompCoverage/SCA005_MIGRATION_POST'
sys.path.insert(0,str(R/'tools/scope_of_work'));import common
rows=lambda p:list(csv.DictReader(p.open()))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
rel=lambda p:str(p.relative_to(R))
register=rows(D/'RUNTIME_DELIVERABLE_REGISTER.csv');ledger=rows(D/'RUNTIME_SCOPE_LEDGER.csv');objectives=rows(D/'RUNTIME_OBJECTIVE_REGISTER.csv');reqs=rows(D/'INHERITED_REQUIREMENT_TRACE.csv'); inputs={};checks=[];matrix=[];formats=[];reqout=[]
def take(p):
 if p.is_file():inputs[rel(p)]=sha(p)
def ck(name,condition,evidence):checks.append(dict(Check=name,Status='PASS' if condition else 'FAIL',Evidence=evidence))
for p in D.rglob('*'):
 if p.is_file():take(p)
for p in [G/'Propagation_Plan.md',G/'DERIVATIVE_RECONCILIATION.csv',G/'EVIDENCE_OUTPUT_SCOPES.csv',G/'SCOPE_104_SUCCESSOR_MAP.csv',R/'plans/steers/root_runtime_migration_gate3_approval_2026-09-05.md',R/'plans/steers/root_runtime_migration_gate4_approval_2026-09-05.md',P/'docs/PRD_AUTHORITY.md',D/'_AUTHORITY.md',R/'tools/scope_of_work/common.py']:take(p)
publication=json.loads((RUN/'SETUP/PUBLICATION.json').read_text())
for row in publication['copied']:
 p=R/row['Target'];ck('approved payload '+row['Target'],sha(p)==row['ApprovedSHA256'],row['ApprovedSource'])
expected={r['DeliverableID'] for r in register};discovered={p.name for p in E.glob('PKG-*/1_Working/DEL-*') if p.is_dir()}
ck('seven exact destination carriers',expected==discovered and len(expected)==7,sorted(discovered));ck('one package',{p.name for p in E.glob('PKG-*') if p.is_dir()}=={'PKG-02_Runtime_Product'},rel(E));ck('one inherited scope',len(ledger)==1 and ledger[0]['ScopeItemID']=='SOW-104',rel(D/'RUNTIME_SCOPE_LEDGER.csv'));ck('four objectives',len(objectives)==4 and {o['ObjectiveID'] for o in objectives}=={'OBJ-001','OBJ-002','OBJ-004','OBJ-007'},rel(D/'RUNTIME_OBJECTIVE_REGISTER.csv'))
for r in register:
 eid=r['DeliverableID'];p=E/r['ParentPackageID']/'1_Working'/eid;ctx=(p/'_CONTEXT.md').read_text();sow=p/'ScopeOfWork.md';doc=common.parse_sow(sow);res=common.resolve_production_format(p);state=common.read_lifecycle_state(p);formats.append([eid,res.state,res.valid,'; '.join(res.issues)])
 for f in ['_CONTEXT.md','_STATUS.md','_REFERENCES.md','_SEMANTIC.md','_DEPENDENCIES.md','ScopeOfWork.md']:
  ck(eid+' minimum '+f,(p/f).is_file(),rel(p/f));take(p/f)
 if(p/'_MEMORY.md').exists():take(p/'_MEMORY.md')
 ck(eid+' initialized',state=='INITIALIZED',rel(p/'_STATUS.md'));ck(eid+' valid SOW',res.valid and res.state=='SOW_V1',list(res.issues))
 def field(key):
  m=re.search(r'\*\*'+re.escape(key)+r':\*\*\s*([^\n]+)',ctx);return m[1] if m else ''
 ck(eid+' context identity',all(field(k)==v for k,v in [('Name',r['Name']),('Type',r['Type']),('Responsible',r['ResponsibleParty']),('Context Envelope',r['ContextEnvelope'])]) and field('Package').startswith(r['ParentPackageID']) and r['Description'] in ctx,rel(p/'_CONTEXT.md'))
 local=[x for x in doc.definitions if x.startswith('REQ-')];traced=[x for x in reqs if x['DeliverableID']==eid];tracedids=[x['QualifiedSuccessorRequirement'].split('::')[-1] for x in traced]
 ck(eid+' numbered requirement conservation',len(local)==len(set(local)) and set(local)==set(tracedids),{'local':local,'trace':tracedids})
 for q in traced:
  src=R/q['SourceFile'];take(src);copy=D/'SOURCE_SCOPE_REQUIREMENTS'/f'{eid}.md';ck(q['QualifiedSourceRequirement']+' source bytes',sha(src)==q['SourceSHA256']==sha(copy),rel(src));reqout.append([q['QualifiedSourceRequirement'],q['QualifiedSuccessorRequirement'],q['SourceSHA256'],q['QualifiedSuccessorRequirement'].split('::')[-1] in local])
 ck(eid+' qualified owner',r['QualifiedIdentity']=='chirality-runtime::'+eid and r['SourceIdentity']=='root::'+eid,r['QualifiedIdentity'])
 ck(eid+' objectives/scope',set(doc.frontmatter['package_objective_refs'])==set(r['SupportsObjectives'].split(';')) and doc.frontmatter['project_scope_refs']==['SOW-104'],doc.frontmatter)
 matrix.append(dict(ProductionUnitID=eid,PartitionID=r['ParentPackageID'],ConcreteProductionUnitLabel='Deliverable',ConcretePartitionLabel='Package',FolderExists=True,ContextPresent=True,ContextMatch='MATCH',ArtifactCoverage='NOT_PRODUCTION_AUDITED',ObjectivesMapped='4/4',LifecycleState=state,IssueCount=0,QualifiedIdentity=r['QualifiedIdentity'],NumberedRequirements=len(local)))
ck('66 inherited requirement trace rows',len(reqs)==66 and len({q['QualifiedSuccessorRequirement'] for q in reqs})==66,len(reqs))
for o in objectives:ck(o['ObjectiveID']+' support',set(o['MappedDeliverables'].split(';'))==expected,o['MappedDeliverables'])
ck('scope ledger coverage',set(ledger[0]['DeliverableIDs'].split(';'))==expected and set(ledger[0]['ObjectiveIDs'].split(';'))=={o['ObjectiveID'] for o in objectives},rel(D/'RUNTIME_SCOPE_LEDGER.csv'))
sm=rows(G/'SCOPE_104_SUCCESSOR_MAP.csv');ck('all104 source scope accounted in approved map',len(sm)==104 and len({x['SourceScopeID'] for x in sm})==104 and all(x['Successors'] or x['SourceInOut']=='OUT' for x in sm),rel(G/'SCOPE_104_SUCCESSOR_MAP.csv'))
# Detail evidence stays outside final snapshot until parent verifies dependency run is complete.
result={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'matrix':matrix,'formats':formats,'requirements':reqout,'inputs':inputs,'failures':[c for c in checks if c['Status']=='FAIL'],'topology':{'packages':1,'deliverables':7,'objectives':4,'scope_items':1,'ledger_rows':1,'inherited_requirements':66,'mapped_root_source_rows':104}}
(RUN/'AUDIT/runtime_measured.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'checks':len(checks),'failures':result['failures'],'topology':result['topology']},indent=2))
