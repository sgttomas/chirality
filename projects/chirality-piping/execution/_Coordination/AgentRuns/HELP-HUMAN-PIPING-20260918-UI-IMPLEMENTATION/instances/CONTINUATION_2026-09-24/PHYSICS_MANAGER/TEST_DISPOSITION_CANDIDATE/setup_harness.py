from pathlib import Path
import re,json,hashlib,shutil
root=Path('/private/tmp/piping-pressure-stress-20260924');P=root/'projects/chirality-piping';M=P/'execution/_Coordination/AgentRuns/HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/PHYSICS_MANAGER';C=M/'TEST_DISPOSITION_CANDIDATE';D=C/'source/projects/chirality-piping/core/product_physics/src';H=C/'harness';(H/'src').mkdir(parents=True,exist_ok=True)
base=P/'core/product_physics';s=(D/'lib.rs').read_text()
def module(m):
 n=m[2];path=D/(n+'.rs') if (D/(n+'.rs')).exists() else base/'src'/(n+'.rs')
 return '#[path = '+json.dumps(str(path))+']\n'+m[0]
s=re.sub(r'^(pub )?mod (\w+);$',module,s,flags=re.M)
s=re.sub(r'(include_(?:str|bytes)!\(\s*)"([^"]+)"',lambda m:m[1]+json.dumps(str((base/'src'/m[2]).resolve())),s)
(H/'src/lib.rs').write_text(s)
t=(base/'Cargo.toml').read_text();t=re.sub(r'path = "(\.\./[^"]+)"',lambda m:'path = '+json.dumps(str((base/m[1]).resolve())),t)
(H/'Cargo.toml').write_text(t);shutil.copyfile(base/'Cargo.lock',H/'Cargo.lock')
shutil.copyfile('/private/tmp/prepare_physics_test_candidate.py',C/'prepare_candidate.py');shutil.copyfile('/private/tmp/setup_physics_candidate_harness.py',C/'setup_harness.py')
files=[*D.glob('*.rs'),H/'src/lib.rs',H/'Cargo.toml',H/'Cargo.lock',C/'prepare_candidate.py',C/'setup_harness.py']
(C/'PREPARED_INPUTS.json').write_text(json.dumps({'status':'NOT_EXECUTED','base':'FREEZE_03','files':{str(p.relative_to(C)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}},indent=2)+'\n')
print(str(H))
