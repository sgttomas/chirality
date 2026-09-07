"""Exact isolated Stage2 composition and negative checks; no live writes."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys,tempfile
root=Path(__file__).resolve().parents[4];out=Path(__file__).resolve().parent
runtime=Path(sys.argv[1]).resolve();fixture=Path(tempfile.mkdtemp(prefix='chirality-root-stage2-check-')).resolve()
paths=subprocess.check_output(['git','-C',str(root),'ls-files','execution','docs','tools','plans/steers','projects/chirality-runtime','AGENTS.md','CLAUDE.md'],text=True).splitlines()
for name in paths:
    src=root/name
    if src.is_file():
        dest=fixture/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest)
for src in [root/'docs/governance_harness/_DECISIONS/D-GOV-38_runtime_stage2_successor_adoption.md',*out.glob('*')]:
    if src.is_file():
        dest=fixture/src.relative_to(root);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dest)
gitdir=subprocess.check_output(['git','-C',str(root),'rev-parse','--absolute-git-dir'],text=True).strip();(fixture/'.git').write_text('gitdir: '+gitdir+'\n')
assert Path(subprocess.check_output(['git','-C',str(fixture),'rev-parse','--show-toplevel'],text=True).strip()).resolve()==fixture
sys.path.insert(0,str(fixture/'tools/validation'))
import yaml
import root_governance_state as g
config=yaml.safe_load((fixture/'execution/_harness/root_guards.yaml').read_text())
baseline=g.load_governance_state(fixture,config,require_effective=True)['runtime_successor_recognition']
assert baseline['adoptions']==['D36_STAGE1'] and baseline['published'] and not baseline['execution_authority']
policy=json.loads((out/'SUCCESSOR_ADOPTIONS.json').read_text());entry=policy['adoptions'][1];subject=runtime/entry['subject']['path'];assert hashlib.sha256(subject.read_bytes()).hexdigest()==entry['subject']['sha256'];members=json.loads(subject.read_text())['files']
inputs=[]
for item in [entry['subject'],entry['acceptance'],*members]:
    raw=(runtime/item['path']).read_bytes();assert hashlib.sha256(raw).hexdigest()==item['sha256'];dest=fixture/item['path'];dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(raw);inputs.append(item)
index=json.loads((fixture/entry['postimage_index']['path']).read_text())
for row in index:
    dest=fixture/row['target'];assert hashlib.sha256(dest.read_bytes()).hexdigest()==row['preimageSha256'];raw=(runtime/row['target']).read_bytes();assert raw==(runtime/row['candidatePath']).read_bytes();assert hashlib.sha256(raw).hexdigest()==row['postimageSha256'];dest.write_bytes(raw)
state=g.load_governance_state(fixture,config,require_effective=True);observed=state['runtime_successor_recognition'];assert observed['adoptions']==['D36_STAGE1','D36_STAGE2'] and not observed['published'] and not observed['execution_authority'];assert [len(state[k]) for k in ['source_ids','governance_ids','runtime_ids','held_capabilities']]==[53,46,7,9]
results=[]
for name in ['root_materialization_fence','root_harness_adapter','root_surface_ownership','root_work_graph_dispatch']:
    p=subprocess.run([sys.executable,str(fixture/'tools/validation'/('validate_'+name+'.py'))],cwd=fixture,capture_output=True,text=True);results.append({'check':name,'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr});assert p.returncode==0
negative=[]
third=next(x['path'] for x in state['successors'] if x['target'].startswith('chirality-runtime::DEL-02-07'))
member=next(x['path'] for x in members if x['path']!=entry['postimage_index']['path'])
cases=[('missing subject member',member,None),('tampered subject member',member,b'tampered full-subject evidence'),('missing acceptance',entry['acceptance']['path'],None),('tampered acceptance',entry['acceptance']['path'],b'not an owner act'),('tampered index',entry['postimage_index']['path'],b'[]'),('mixed SOW',index[0]['target'],subprocess.check_output(['git','-C',str(root),'show','origin/main:'+index[0]['target']])),('unapproved third SOW',third,b'unapproved SOW'),('tampered Root act',policy['root_owner_act']['path'],b'not the ruled act')]
for label,name,replacement in cases:
    path=fixture/name;before=path.read_bytes()
    try:
        path.unlink() if replacement is None else path.write_bytes(replacement)
        try:g.load_governance_state(fixture,config)
        except g.GovernanceError as exc:negative.append({'case':label,'result':'REJECTED','error':str(exc)})
        else:raise AssertionError('Unaccepted case passed: '+label)
    finally:path.write_bytes(before)
result={'status':'PASS','fixture':str(fixture),'runtime_input_root':str(runtime),'inputs':inputs,'baseline':baseline,'stage2':observed,'guards':results,'negative':negative,'preserved_counts':[53,46,7,9],'scope':'disposable fixture only; Runtime live checkout untouched'}
(out/'STAGE2_COMPOSITION.json').write_text(json.dumps(result,indent=2)+'\n');print('PASS: baseline Stage1, exact Stage2 four guards, eight rejection cases;53/46/7/9 intact')
