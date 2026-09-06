#!/usr/bin/env python3
"""Reproduce raw registered analyzer and registry-bound independent audit. No input writes."""
from pathlib import Path
import csv,json,hashlib,subprocess,collections
REPO=Path(__file__).resolve().parents[6]
OUT=Path(__file__).resolve().parent
EXEC=REPO/'projects/chirality-runtime/execution'
def rows(p):return list(csv.DictReader(p.open()))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(cmd):
 r=subprocess.run(cmd,cwd=REPO,text=True,capture_output=True);return {'argv':cmd,'exit':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
commands=[run(['python3','tools/coordination/analyze_dep_closure.py',str(EXEC),'--output-dir',str(OUT/'Evidence')])]
binding=REPO/'execution/_ScopeChange/SCA-005_2026-09-06_GATE4_PLAN/RUNTIME_METADATA_BINDINGS.csv'
plan=REPO/'execution/_ScopeChange/SCA-005_2026-09-06_GATE4_PLAN/DEPENDENCY_DISTRIBUTION.csv'
gov=REPO/'execution/_Coordination/GovernanceControls/_DEPENDENCIES.csv'
regs=rows(binding); ids={r['DeliverableID'] for r in regs};paths={r['DeliverableID']:REPO/r['Folder'] for r in regs}
pins={};errors=[];edge_rows=collections.defaultdict(list);all_rows=[];aliases=[]
def pin(p):pins[str(p.relative_to(REPO))]=sha(p)
for p in [binding,plan,gov,REPO/'tools/coordination/analyze_dep_closure.py',REPO/'tools/validation/validate_dependencies_schema.py',REPO/'agents/AGENT_AUDIT_DEP_CLOSURE.md',EXEC/'_Decomposition/RUNTIME_DELIVERABLE_REGISTER.csv',EXEC/'_Decomposition/RUNTIME_SCOPE_LEDGER.csv',EXEC/'_Decomposition/RUNTIME_OBJECTIVE_REGISTER.csv',EXEC/'_Decomposition/HOLD_SUCCESSOR_MAP.csv',EXEC/'_Decomposition/OWNERSHIP_OVERLAY.md',EXEC/'_Decomposition/_AUTHORITY.md',EXEC/'_Coordination/MIGRATION_APPLICATION.md']:pin(p)
for r in regs:
 ident=r['DeliverableID'];folder=paths[ident];p=folder/'Dependencies.csv';data=rows(p);all_rows+=data
 aliases.append({'discovery_short_id':ident.split('_')[0],'accepted_id':ident,'folder':r['Folder']})
 for name in ['Dependencies.csv','_DEPENDENCIES.md','_CONTEXT.md','_STATUS.md','ScopeOfWork.md','_run_records/SCA005_INIT/Independent_Review.md']:
  f=folder/name;pin(f)
  if name=='_STATUS.md':
   f.read_text()
   for memory in [folder/'_MEMORY.md',folder/'MEMORY.md']:
    if memory.is_file():memory.read_text();pin(memory)
 commands.append(run(['python3','tools/validation/validate_dependencies_schema.py',str(p)]))
 anchors=[x for x in data if x['DependencyClass']=='ANCHOR'];executions=[x for x in data if x['DependencyClass']=='EXECUTION'];notes=(folder/'_DEPENDENCIES.md').read_text()
 expected_anchors={'PKG-02_Runtime_Product','SOW-104','OBJ-001','OBJ-002','OBJ-004','OBJ-007'}
 if len(anchors)!=6 or {x['TargetRefID'] for x in anchors}!=expected_anchors:errors.append([ident,'anchor set'])
 if sum(x['AnchorType']=='IMPLEMENTS_NODE' for x in anchors)!=1:errors.append([ident,'parent anchor count'])
 for x in data:
  if x['FromDeliverableID']!=ident or x['RegisterSchemaVersion']!='v3.1':errors.append([x['DependencyID'],'source ID/schema'])
  if not (REPO/x['TargetLocation']).exists() or not (REPO/x['EvidenceFile']).is_file():errors.append([x['DependencyID'],'unresolved path'])
  if x['TargetType']!='DELIVERABLE' and x['TargetDeliverableID']:errors.append([x['DependencyID'],'misplaced target'])
  if x['DependencyID'] not in notes:errors.append([x['DependencyID'],'not in local extracted view'])
  if x['Status']!='ACTIVE':errors.append([x['DependencyID'],'unexpected status'])
 for x in anchors:
  if x['SatisfactionStatus']!='NOT_APPLICABLE':errors.append([x['DependencyID'],'anchor treated as gate'])
 for x in executions:
  target=x['TargetDeliverableID']
  if target not in ids or Path(x['TargetLocation'])!=Path(str(paths.get(target,'')).removeprefix(str(REPO)+'/')):errors.append([x['DependencyID'],'target identity/path'])
  if any(x[k]!='TBD' for k in ['RequiredMaturity','ProposedMaturity','SatisfactionStatus']):errors.append([x['DependencyID'],'inferred evidence maturity/satisfaction'])
  pair=(target,ident) if x['Direction']=='UPSTREAM' else (ident,target)
  edge_rows[pair].append({'id':x['DependencyID'],'direction':x['Direction'],'file':str(p.relative_to(REPO))})
  if 'chirality-runtime::'+target not in notes:errors.append([x['DependencyID'],'missing declared local relationship'])
expected={(x['Predecessor'].split('::')[1],x['Consumer'].split('::')[1]) for x in rows(plan) if x['Predecessor'].startswith('chirality-runtime::')}
if set(edge_rows)!=expected:errors.append(['graph','approved edge mismatch'])
for pair,values in edge_rows.items():
 if len(values)!=2 or {x['direction'] for x in values}!={'UPSTREAM','DOWNSTREAM'}:errors.append([pair,'mirror mismatch'])
connected={x for pair in edge_rows for x in pair};isolates=sorted(ids-connected)
# Directed prerequisite->consumer graph, unlike registered analyzer's consumer->prerequisite orientation.
adj={i:set() for i in ids}
for a,b in edge_rows:adj[a].add(b)
visited=set();stack=set();cycles=[]
def visit(n):
 if n in stack:cycles.append(n);return
 if n in visited:return
 stack.add(n)
 for t in sorted(adj[n]):visit(t)
 stack.remove(n);visited.add(n)
for n in sorted(ids):visit(n)
expectedgov=[x for x in rows(plan) if x['Predecessor'].startswith('root::')]
if rows(gov)!=expectedgov:errors.append(['Root governance','two edge mismatch'])
for x in expectedgov:
 for key in ['Predecessor','Consumer']:
  p=REPO/'execution/_Coordination/GovernanceControls'/(x[key].split('::')[1]+'.md');pin(p)
summary={'registers':len(regs),'rows':len(all_rows),'anchors':sum(x['DependencyClass']=='ANCHOR' for x in all_rows),'execution_mirror_rows':sum(x['DependencyClass']=='EXECUTION' for x in all_rows),'unique_runtime_edges':len(edge_rows),'root_governance_edges':len(expectedgov),'missing_targets':[],'actual_isolated_deliverables':isolates,'cycles':cycles,'errors':errors,'aliases':aliases,'edges':[{'predecessor':a,'consumer':b,'mirrors':v} for (a,b),v in sorted(edge_rows.items())],'closure_topology_verdict':'PASS' if not errors and not isolates and not cycles else 'BLOCKER','audit_verdict':'WARNING_TOOL_DIALECT' if not errors and not isolates and not cycles else 'BLOCKER','tool_warning':'Registered analyzer discovery strips full-ID suffix while normalize_id leaves graph IDs full; seven reported orphans are false-positive isolates. No source IDs rewritten. Its orphans function does not detect missing target references; this supplement performs that check explicitly.'}
(OUT/'Registry_Backcheck.json').write_text(json.dumps(summary,indent=2)+'\n');(OUT/'Commands.json').write_text(json.dumps(commands,indent=2)+'\n');(OUT/'Input_Hashes.json').write_text(json.dumps(pins,indent=2)+'\n')
assert all(v['exit']==0 for v in commands)
assert not errors and not isolates and not cycles
for p,h in pins.items():assert sha(REPO/p)==h,p
print(json.dumps({k:v for k,v in summary.items() if k not in ['edges','aliases']},indent=2))
