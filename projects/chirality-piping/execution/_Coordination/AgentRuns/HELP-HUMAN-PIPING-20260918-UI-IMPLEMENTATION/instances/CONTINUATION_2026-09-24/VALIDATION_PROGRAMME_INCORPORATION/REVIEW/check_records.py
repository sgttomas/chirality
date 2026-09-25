"""Read-only custody, local-link and planning-graph checks; no validation run."""
from pathlib import Path
import csv, hashlib, json, re, subprocess
from urllib.parse import unquote

HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'projects/chirality-piping/AGENTS.md').is_file())
P=ROOT/'projects/chirality-piping'
GRAPH=P/'execution/_Coordination/WorkGraphs/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/WORK_GRAPH.md'
REF=P/'docs/references/validation-programme'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=json.loads((REF/'REFERENCE_MANIFEST.json').read_text())
copies=[]
for item in manifest['references']:
    original=Path('/Users/ryan/Downloads')/item['original_filename'];copied=ROOT/item['repository_path']
    assert original.read_bytes()==copied.read_bytes()
    assert sha(copied)==item['sha256'] and copied.stat().st_size==item['bytes']
    copies.append({**item,'actual_original_path':str(original),'original_sha256':sha(original),'copy_sha256':sha(copied),'byte_identical':True})

basis=json.loads((HERE.parent/'SOURCE_BASIS.json').read_text())
checked_basis=[]
for item in basis['instruction_and_method_origins']+basis['deliverable_mapping_basis']:
    path=ROOT/item['path'];assert sha(path)==item['sha256'],item['path']
    lines=path.read_text().splitlines()
    for excerpt in item.get('excerpts',[]):assert lines[excerpt['line']-1]==excerpt['text'],(item['path'],excerpt['line'])
    checked_basis.append({'path':item['path'],'sha256':sha(path),'excerpts_match':True})
dag=list(csv.DictReader((P/'execution/_DAG/DAG-011/DeliverableNodes.csv').open()))
dag_ids={row['DeliverableID'] for row in dag}
assert all(item['deliverable_id'] in dag_ids for item in basis['deliverable_mapping_basis'])

rows={}
for line in GRAPH.read_text().splitlines():
    if not line.startswith('| '):continue
    cells=[part.strip() for part in line.split('|')[1:-1]]
    match=re.match(r'([A-Z][A-Z0-9-]*) — ',cells[0]) if cells else None
    if match:
        assert len(cells)==5,(match.group(1),len(cells))
        assert match.group(1) not in rows
        rows[match.group(1)]=cells
future={key:value for key,value in rows.items() if key.startswith('VP-')}
assert len(future)==17,len(future)
edges={key:[] for key in rows}
conditional=[]
informational=[]
for key,cells in rows.items():
    for dependency in rows:
        if not re.search(r'(?<![A-Z0-9-])'+re.escape(dependency)+r'(?![A-Z0-9-])',cells[2]):continue
        if key==dependency:
            assert key=='G-11' and 'authorized recorded G-11 direction' in cells[2]
            informational.append([key,'reference to its recorded owner direction, not a work prerequisite'])
            continue
        if key=='VP-LICENSED' and dependency=='VP-INTERCHANGE':
            assert 'not completion of VP-INTERCHANGE' in cells[2]
            continue
        edges[key].append(dependency)
        if key in {'VP-LICENSED','VP-WORKFLOW'} and dependency=='LIVE-FINAL':conditional.append([key,dependency,'actual agent-control witness/campaign only'])
    if key.startswith('VP-') and key!='VP-REF':assert 'ON HOLD' in cells[4]
    if key.startswith('VP-'):assert all(cells[1:]),key
done=set();active=set()
def visit(node):
    assert node not in active,('dependency cycle',node)
    if node in done:return
    active.add(node)
    for dependency in edges[node]:visit(dependency)
    active.remove(node);done.add(node)
for node in edges:visit(node)

links=[]
for source in [GRAPH,REF/'README.md',HERE.parent/'BRIEF.md']:
    text=source.read_text()
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',text):
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target):continue
        path,_,fragment=target.partition('#');resolved=(source.parent/unquote(path)).resolve() if path else source
        assert resolved.exists(),(str(source),target,str(resolved))
        if fragment=='validation-programme-successor-route':assert '## Validation programme successor route' in resolved.read_text()
        links.append({'source':str(source.relative_to(ROOT)),'target':target,'resolved':str(resolved),'exists':True})

git=lambda *args:subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()
refs={name:git('rev-parse','refs/remotes/origin/'+name) for name in ['codex/piping-source-recovery-20260924','codex/piping-scientific-json-20260925','codex/piping-engine-integration-20260925']}
expected={'codex/piping-source-recovery-20260924':'45d412e5d10e52e80d14a88d5cbea82e2bee005a','codex/piping-scientific-json-20260925':'05a9baa3342e8a322536ce2286f4189553d43eec','codex/piping-engine-integration-20260925':'22452ecd148e86486fe36a36e34a184c9a5a5943'}
assert refs==expected
changed=git('diff','--name-only','ed688b13f633ce8aa6aeede784c3562511c20966','45d412e5d10e52e80d14a88d5cbea82e2bee005a').splitlines()
assert all('/FRONTEND_READERS/INDEPENDENT_REVIEW/' in path for path in changed)
assert len(git('show','--format=','--name-only','22452ecd148e86486fe36a36e34a184c9a5a5943').splitlines())==510
output={'scope':'Records/custody/structural checks only; no benchmark/reference generator/product/native execution or network.',
        'copies':copies,'source_basis_checks':checked_basis,'dag_node_count':len(dag),'vp_nodes':list(future),
        'explicit_dependency_edges':edges,'acyclic':True,'conditional_edges':conditional,'informational_mentions':informational,'planning_interpretation':'VP-ASSESS selected-profile fan-in is conditional, not every optional branch; owner VP-GO holds apply to all future work.',
        'local_links':links,'remote_tracking_refs':refs,'remote_limit':'Read existing local tracking refs; no network fetch or new remote verification.',
        'source_review_checkpoint_only':changed,'checked_files':[{'path':str(p.relative_to(ROOT)),'sha256':sha(p)} for p in [GRAPH,REF/'README.md',REF/'REFERENCE_MANIFEST.json',HERE.parent/'BRIEF.md',HERE.parent/'SOURCE_BASIS.json']]}
(HERE/'CHECKS.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'byte_identical_copies':len(copies),'source_basis_hashes_and_excerpts':len(checked_basis),'future_nodes':len(future),'acyclic':True,'local_links_checked':len(links),'checkpoint_refs':refs},indent=2))
