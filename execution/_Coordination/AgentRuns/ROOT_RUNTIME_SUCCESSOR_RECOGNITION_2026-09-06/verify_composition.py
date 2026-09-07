"""Build a disposable exact-source composition; no live checkout edits."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile

root=Path(__file__).resolve().parents[4]
out=Path(__file__).resolve().parent
base='e1dee34315ff4ca448b0fbc14e5542b6bad9fac2'
head='04a110a4443a532fcf7f31124e5c857f88c27949'
fixture=Path(tempfile.mkdtemp(prefix='chirality-root-runtime-composition-'))
# Preserve evidence, not a duplicate checkout or credentials.
paths=subprocess.check_output(['git','-C',str(root),'ls-files','execution','docs','tools','plans/steers','projects/chirality-runtime','AGENTS.md','CLAUDE.md'],text=True).splitlines()
for path in paths:
    source=root/path
    if source.is_file():
        dest=fixture/path;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,dest)
# New Root adoption/helper/notice evidence is necessary but never imports other
# untracked projects or Runtime private state.
for source in [root/'tools/validation/root_runtime_successors.py', *out.glob('*')]:
    if source.is_file():
        dest=fixture/source.relative_to(root);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(source,dest)
changes=subprocess.check_output(['git','-C',str(root),'diff','--name-only',base+'...'+head],text=True).splitlines()
assert all(path.startswith('projects/chirality-runtime/') for path in changes)
for path in changes:
    data=subprocess.check_output(['git','-C',str(root),'show',head+':'+path]);dest=fixture/path;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
gitdir=subprocess.check_output(['git','-C',str(root),'rev-parse','--absolute-git-dir'],text=True).strip()
(fixture/'.git').write_text('gitdir: '+gitdir+'\n')
# Validators run from copied code with fixture cwd; Git metadata is read-only.
results=[]
for guard in ['root_materialization_fence','root_harness_adapter','root_surface_ownership','root_work_graph_dispatch']:
    cmd=[sys.executable,str(fixture/'tools/validation'/('validate_'+guard+'.py'))]
    run=subprocess.run(cmd,cwd=fixture,capture_output=True,text=True)
    results.append({'guard':guard,'exit':run.returncode,'stdout':run.stdout,'stderr':run.stderr})
# Direct semantic observation separates accepted branch bytes from publication.
sys.path.insert(0,str(fixture/'tools/validation'))
import yaml
import root_governance_state as g
try:
    state=g.load_governance_state(fixture,yaml.safe_load((fixture/'execution/_harness/root_guards.yaml').read_text()),require_effective=True)
    observation=state['runtime_successor_recognition']
    assert observation['state']=='accepted-pending-publication' and not observation['published'] and not observation['execution_authority']
    assert len(state['source_ids'])==53 and len(state['governance_ids'])==46 and len(state['runtime_ids'])==7 and len(state['held_capabilities'])==9
except Exception as exc:
    observation={'error':repr(exc)}
    results.append({'guard':'direct_observation','exit':1,'stdout':'','stderr':repr(exc)})
result={'base':base,'runtime_head':head,'fixture':str(fixture),'input_runtime_paths':changes,'results':results,'observation':observation,'status':'PASS' if all(x['exit']==0 for x in results) else 'FAIL','method':'Tracked baseline copy plus exact Runtime commit files and current bounded Root candidate; no live edits'}
(out/'COMPOSITION_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(result['status']);print([(x['guard'],x['exit'],x['stdout'].strip()) for x in results]);print(observation.get('state',observation))
# Deliberately retain disposable fixture location for independent recheck during
# this run; no fixture is part of publication inventory.
