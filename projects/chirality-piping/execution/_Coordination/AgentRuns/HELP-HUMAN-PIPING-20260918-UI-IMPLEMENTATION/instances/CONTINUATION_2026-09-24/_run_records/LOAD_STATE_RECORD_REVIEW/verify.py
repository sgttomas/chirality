"""Bounded records/custody inspection; does not execute either analytical script."""
from pathlib import Path
import ast, datetime, hashlib, json, re, subprocess

R=Path('/Users/ryan/.codex/worktrees/6614/chirality')
OUT=Path(__file__).resolve().parent
BASE='7cf85889062b5629001204e248cfe4e09c9d0739'
C='projects/chirality-piping/execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/'
PACKET=C+'CORRECTNESS_DESIGN/LOAD_REFERENCE_STATES'
P=R/PACKET
G='projects/chirality-piping/execution/_Coordination/WorkGraphs/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/WORK_GRAPH.md'
git=lambda *a:subprocess.check_output(['git','-C',str(R),*a])
sha=lambda b:hashlib.sha256(b).hexdigest()
fsha=lambda p:sha(p.read_bytes())
load=lambda p:json.loads(p.read_text())
assert git('rev-parse','HEAD').decode().strip()==BASE
files=sorted(x for x in P.rglob('*') if x.is_file())
assert len(files)==21
manifest=load(P/'PACKET_MANIFEST.json')
manifest_paths={x['path'] for x in manifest['files']}
assert manifest_paths|{'PACKET_MANIFEST.json'}=={str(x.relative_to(P)) for x in files}
assert len(manifest['files'])==len(manifest_paths)==20
manifest_bad=[x['path'] for x in manifest['files'] if fsha(P/x['path'])!=x['sha256'] or (P/x['path']).stat().st_size!=x['bytes']]
assert not manifest_bad
review=load(P/'_run_records/INDEPENDENT_REVIEW/FINAL_HASHES.json')
reviewed=[]
for row in review['files']:
    path=row['path'].removeprefix('LOAD_REFERENCE_STATES/')
    assert fsha(P/path)==row['sha256'] and (P/path).stat().st_size==row['bytes']
    reviewed.append(path)
assert len(reviewed)==7 and review['status']=='CLEAR_AFTER_THREE_REPAIRS'
local=load(P/'_run_records/LOCAL_CHECKS.json')
for path,row in local['files'].items():assert fsha(P/path)==row['sha256'] and (P/path).stat().st_size==row['bytes']
assert local['local_links']=='PASS' and local['missing']==[]
final=load(P/'_run_records/FINAL_BACKCHECK.json')
assert final['status']=='PASS' and final['analytical_groups']==11 and all(x['matches'] for x in final['independent_final_hashes_match'])

links=[];missing=[]
for path in files:
    if path.suffix!='.md':continue
    for link in re.findall(r'\]\(([^)]+)\)',path.read_text()):
        if re.match(r'https?://',link) or link.startswith('#'):continue
        target=path.parent/link.split('#',1)[0]
        links.append({'from':str(path.relative_to(P)),'link':link,'exists':target.exists()})
        if not target.exists():missing.append(links[-1])
assert not missing
author=load(P/'_run_records/analytical_examples.json')
independent=load(P/'_run_records/INDEPENDENT_REVIEW/NUMERICAL_REVIEW.json')
run=load(P/'_run_records/INDEPENDENT_REVIEW/CHECK_RUN.json')
assert author['status']==independent['status']=='PASS' and author['groups']==independent['groups']==11
assert len(author['examples'])==len(independent['results'])==11
assert independent['product_execution'] is False and run['exit_status']==0
assert json.loads(run['stdout'])=={'status':'PASS','groups':11,'product_execution':False}
assert independent['script_sha256']==fsha(P/'_run_records/INDEPENDENT_REVIEW/independent_check.py')
imports={}
for path in ['verify_reference_states.py','_run_records/INDEPENDENT_REVIEW/independent_check.py']:
    tree=ast.parse((P/path).read_text());names=[]
    for node in ast.walk(tree):
        if isinstance(node,ast.Import):names.extend(x.name for x in node.names)
        elif isinstance(node,ast.ImportFrom):names.append(node.module)
    assert set(names)<= {'json','fractions','decimal','pathlib','hashlib'}
    imports[path]=names
delegation=load(P/'_run_records/DELEGATION.json');basis=load(P/'BASIS.json')
review_basis=load(P/'_run_records/INDEPENDENT_REVIEW/BASIS_START.json')
assert basis['agent']=='/root/load_state_design' and basis['actual_parent']=='/root'
assert delegation['child']==review_basis['agent']=='/root/load_state_design/reference_review'
assert delegation['actual_parent']==review_basis['parent']=='/root/load_state_design'
assert delegation['launch_result']=='created successfully' and delegation['refusals']==[]
review_return=(P/'_run_records/INDEPENDENT_REVIEW/RETURN.md').read_text()
assert 'supplied by ROOT during review' in review_return and 'Independently confirmed the root-supplied counterexample' in review_return
assert 'derived rather than taken from vendor output' in review_return
assert 'not a vendor benchmark' in (P/'HYDROSTATIC_CONTROL.md').read_text()
assert 'No product finding is closed' in (P/'RETURN.md').read_text()

graph_before=git('show',BASE+':'+G).decode();graph_after=(R/G).read_text();patch=git('diff',BASE,'--',G)
(OUT/'WORK_GRAPH.reviewed.patch').write_bytes(patch)
def table(s):
    rows={}
    for line in s.splitlines():
        m=re.match(r'^\| (M\d{2}) \| (.*?) \| (.*?) \|$',line)
        if m:rows[m[1]]=m[3]
    return rows
old,new=table(graph_before),table(graph_after)
assert len(old)==len(new)==38
changed=[k for k in old if old[k]!=new[k]]
assert changed==['M10','M16','M21','M29']
closed=lambda t:sorted(k for k,v in t.items() if v.startswith('COMPLETE'))
assert closed(old)==closed(new)==['M04','M09','M24','M35']
assert all('DESIGN READY' in new[k] and 'open' in new[k] for k in ['M10','M16','M29'])
assert new['M21'].startswith('PARTIAL') and 'full implementation and native authoring remain open' in new['M21']
assert 'not new product capability or finding closure' in graph_after
assert 'Public identities will be allocated before the implementing source freeze' in graph_after
graph_link='../../AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/CORRECTNESS_DESIGN/LOAD_REFERENCE_STATES/RETURN.md'
assert graph_link in graph_after and ((R/G).parent/graph_link).resolve()==P/'RETURN.md'

full_models=[]
def scan(v,path):
    if isinstance(v,dict):
        if 'nodes' in v and 'pipe_segments' in v:full_models.append(path)
        for x in v.values():scan(x,path)
    elif isinstance(v,list):
        for x in v:scan(x,path)
    elif isinstance(v,str) and v.startswith('{'):
        try:x=json.loads(v)
        except ValueError:return
        scan(x,path)
for path in files:
    if path.suffix=='.json':scan(load(path),str(path.relative_to(P)))
assert not full_models
assert 'All engineering numbers below are invented test inputs, not library records.' in (P/'VERIFICATION.md').read_text()
scope=[str(x.relative_to(R)) for x in files]+[G]
command=['python3',str(R/'tools/software_workflow/validate_change_scope.py'),str(R),'--allowed',PACKET,'--allowed',G]
for path in scope:command.extend(['--path',path])
checked=subprocess.run(command,text=True,capture_output=True)
assert checked.returncode==0
(OUT/'SCOPE_CHECK.json').write_text(checked.stdout)
coverage=[]
for path in files:
    rel=str(path.relative_to(P))
    coverage.append({'path':str(path.relative_to(R)),'sha256':fsha(path),'bytes':path.stat().st_size,
      'coverage':'Exact final-seven technical review carried; source/status/provenance/limit sections and local links inspected for records review.' if rel in reviewed
      else 'Records/content/provenance inspected; hash/link/count/execution-claim checks as applicable. Independent script imports and custody inspected without rerunning its arithmetic.'})
coverage.append({'path':G,'sha256':fsha(R/G),'coverage':'Complete frozen diff and all changed state/count/link claims reviewed.'})
report={'reviewer':'/root/m35_integration_review','parent':'/root','role':'TASK','time_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'base':BASE,'scope_count':len(scope),'packet_files':len(files),'packet_manifest_entries':len(manifest['files']),
 'manifest_sha256':fsha(P/'PACKET_MANIFEST.json'),'manifest_mismatches':manifest_bad,'final_review_files':reviewed,
 'local_links_checked':links,'missing_local_links':missing,'author_analytical_groups_recorded':author['groups'],
 'reviewer_analytical_groups_recorded':independent['groups'],'analytical_scripts_rerun_by_this_reviewer':False,
 'script_imports':imports,'delegation_record_sha256':fsha(P/'_run_records/DELEGATION.json'),
 'hydrostatic_attribution':'ROOT contributed the counterexample; independent TASK reference_review checked it. Neither is vendor benchmark/runtime output.',
 'changed_finding_states':changed,'closed_groups_unchanged':closed(new),'original_open_count':38-len(closed(new)),
 'graph_before_sha256':sha(graph_before.encode()),'graph_after_sha256':fsha(R/G),'graph_diff_sha256':sha(patch),
 'no_full_model_json_matches':full_models,'privacy_scope':'Packet contains invented analytical scalars/interfaces/reference discussion, not complete native/user models or populated material/component/code-rule datasets.',
 'candidate_coverage':coverage,'scope_validator_exit':checked.returncode,
 'current_origin_hashes':[{'path':path,'sha256':fsha(R/path)} for path in ['AGENTS.md','agents/AGENT_TASK.md',
    'projects/chirality-piping/AGENTS.md','projects/chirality-piping/loop/LOOP_INIT.md','.agents/skills/software-code-review/SKILL.md']],
 'unrelated_working_state_excluded':git('status','--porcelain').decode(),
 'limits':'Recoverable records checkpoint only. Prior technical review carried, no new literature review/analytical execution/source qualification. No source, graph, Git, native, runtime or heavy checks; no delegation. ROOT selection is existing authority, not a new human gate.'}
(OUT/'HASHES.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'packet_files':len(files),'candidate_paths':len(scope),'reviewed_technical_files':len(reviewed),
 'scope':'PASS','local_links':len(links),'changed_states':changed,'closed_groups_unchanged':closed(new)},indent=2))
