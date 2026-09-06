from pathlib import Path
import csv,json,re,hashlib,sys,collections,datetime,subprocess
R=Path('/Users/ryan/.codex/worktrees/341e/chirality');E=R/'execution';D=E/'_Decomposition';G=E/'_ScopeChange/SCA-005_2026-09-06_GATE4_PLAN';RUN=E/'_Coordination/AgentRuns/ROOT_RUNTIME_MIGRATION_GATE5_2026-09-06';B='8209bc54e0d133b19437c93b184cd50ba3d43489'
rows=lambda p:list(csv.DictReader(p.open()));sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();rel=lambda p:str(p.relative_to(R));checks=[];inputs={};matrix=[];memories=[]
def take(p):
 if p.is_file():inputs[rel(p)]=sha(p)
def ck(n,v,e):checks.append(dict(Check=n,Status='PASS' if v else 'FAIL',Evidence=e))
reg=rows(D/'chirality_root_deliverable_register_v1_0.csv');ledger=rows(D/'chirality_root_scope_ledger_v1_0.csv');objs=rows(D/'chirality_root_objective_register_v1_0.csv');bindings=rows(E/'_Coordination/GovernanceControls/_AUTHORITY_BINDINGS.csv');pkgs=rows(G/'ROOT_6_PACKAGE_CLOSURE.csv');maps=rows(G/'SCOPE_104_SUCCESSOR_MAP.csv')
for p in D.glob('*'):
 if p.is_file():take(p)
for p in G.glob('*'):
 if p.is_file():take(p)
for w in rows(G/'WRITE_TARGETS.csv'):
 if w['SurfaceClass'] in ['SOURCE_METADATA','SOURCE_AUTHORITY'] or w['Target'].startswith('execution/_Decomposition/'):
  p=R/w['Target'];take(p);ck('exact approved source postimage '+w['Target'],sha(p)==w['ApprovedSHA256'],w['ApprovedSource'])
ck('53 historical registered',len(reg)==53 and len({r['DeliverableID'] for r in reg})==53,rel(D/'chirality_root_deliverable_register_v1_0.csv'));ck('six historical packages',len(pkgs)==6 and {p.name for p in E.glob('PKG-*') if p.is_dir()}=={p['SourcePackage'] for p in pkgs},rel(G/'ROOT_6_PACKAGE_CLOSURE.csv'))
ck('53 exact historical folders',{p.name for p in E.glob('PKG-*/1_Working/DEL-*') if p.is_dir()}=={r['DeliverableID'] for r in reg},rel(E))
for r in reg:
 eid=r['DeliverableID'];p=E/r['ParentPackageID']/'1_Working'/eid
 for name in ['_MEMORY.md','MEMORY.md']:
  m=p/name
  if m.exists():memories.append({'path':rel(m),'text':m.read_text(),'sha256':sha(m)});take(m)
 status=p/'_STATUS.md';st=status.read_text();take(status);m=re.search(r'\*\*Current State:\*\*\s*([^\n]+)',st);state=m[1].strip() if m else 'UNKNOWN'
 ck(eid+' retired',state=='RETIRED',rel(status));ck(eid+' zero active product authority',r.get('ActiveRootProductAuthority')=='NO' and r.get('RegistrationState','').startswith('RETIRED'),rel(D/'chirality_root_deliverable_register_v1_0.csv'))
 successor=r.get('SuccessorIdentity','');target=r.get('SuccessorAuthorityPath','');ck(eid+' successor exists',bool(target) and (R/target).exists(),target)
 if successor.startswith('chirality-runtime::'):ck(eid+' qualified runtime successor',successor=='chirality-runtime::'+eid and target.startswith('projects/chirality-runtime/'),target)
 else:ck(eid+' governance successor',successor.startswith('GOV-') and target=='execution/_Coordination/GovernanceControls/'+successor+'.md',target)
 # Historical contracts/context remain source evidence, never demanded to impersonate destination authority.
 tracked=subprocess.run(['git','ls-tree','-r','--name-only',B,'--',rel(p)],cwd=R,check=True,capture_output=True,text=True).stdout.splitlines();unchanged=True
 for name in tracked:
  f=R/name
  if f.name=='_STATUS.md':continue
  take(f);old=subprocess.run(['git','show',B+':'+name],cwd=R,check=True,capture_output=True).stdout
  unchanged=unchanged and f.is_file() and f.read_bytes()==old
 ck(eid+' source history untouched',unchanged,rel(p))
 matrix.append(dict(ProductionUnitID=eid,PartitionID=r['ParentPackageID'],ConcreteProductionUnitLabel='HistoricalDeliverable',ConcretePartitionLabel='HistoricalPackage',FolderExists=p.is_dir(),ContextPresent=(p/'_CONTEXT.md').exists(),ContextMatch='PRESERVED_HISTORICAL',ArtifactCoverage='HISTORICAL_NOT_ACTIVE_PRODUCTION',ObjectivesMapped='PRESERVED_HISTORICAL',LifecycleState=state,IssueCount=0,SuccessorIdentity=successor,SuccessorAuthorityPath=target,ActiveRootProductAuthority=r.get('ActiveRootProductAuthority')))
ck('46 distinct governance controls',len(bindings)==46 and len({r['ControlID'] for r in bindings})==46 and {p.stem for p in (E/'_Coordination/GovernanceControls').glob('GOV-*.md')}=={r['ControlID'] for r in bindings},rel(E/'_Coordination/GovernanceControls'))
for b in bindings:
 p=R/b['ProposedControlHome'];take(p);ck(b['ControlID']+' exact control authority',sha(p)==b['ControlSHA256'] and all((R/part).is_file() for part in b['ControllingInstrument'].split(';')) and (R/b['ExactPredicateRegister']).exists(),b['ExactControlSource'])
for pkg in pkgs:
 declared={r['DeliverableID'] for r in reg if r['ParentPackageID']==pkg['SourcePackage']};ck(pkg['SourcePackage']+' child conservation',set(pkg['Children'].split(';'))==declared and int(pkg['ChildCount'])==len(declared),pkg['Children'])
ck('104 source rows conserved',len(ledger)==104 and {r['ScopeItemID'] for r in ledger}=={r['SourceScopeID'] for r in maps},rel(D/'chirality_root_scope_ledger_v1_0.csv'))
oldcsv=subprocess.run(['git','show',B+':'+rel(D/'chirality_root_scope_ledger_v1_0.csv')],cwd=R,check=True,capture_output=True,text=True).stdout
old=list(csv.DictReader(oldcsv.splitlines()));byid={r['ScopeItemID']:r for r in ledger};preserved=all(all(byid[r['ScopeItemID']].get(k)==v for k,v in r.items()) for r in old);ck('104 original ledger field preservation',preserved,rel(D/'chirality_root_scope_ledger_v1_0.csv'))
ck('seven historical objectives preserved',len(objs)==7,rel(D/'chirality_root_objective_register_v1_0.csv'));ck('qualified successor partition',sum(r['SuccessorIdentity'].startswith('chirality-runtime::') for r in reg)==7 and sum(r['SuccessorIdentity'].startswith('GOV-') for r in reg)==46,rel(D/'chirality_root_deliverable_register_v1_0.csv'))
for r in maps:
 for successor in filter(None,r['Successors'].split(';')):
  okay=successor in {b['ControlID'] for b in bindings} or successor in {x['SuccessorIdentity'] for x in reg}
  ck(r['SourceScopeID']+' mapped successor '+successor,okay,rel(G/'SCOPE_104_SUCCESSOR_MAP.csv'))
result={'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'matrix':matrix,'inputs':inputs,'source_memories_read':memories,'failures':[c for c in checks if c['Status']=='FAIL'],'topology':{'historical_packages':6,'historical_deliverables':53,'active_root_product_deliverables':0,'governance_controls':46,'runtime_successors':7,'historical_objectives':7,'source_scope_items':104,'source_ledger_rows':104}}
(RUN/'AUDIT/root_measured.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'checks':len(checks),'failures':result['failures'],'topology':result['topology']},indent=2))
