import hashlib,json,shutil,subprocess,sys
from pathlib import Path
r=Path('/private/tmp/runtime-execution-20260906/supplier-candidate')
phase=sys.argv[1]
assert phase in ('baseline','patched')
assert json.loads((r/'builds'/f'{phase}.json').read_text())['exit']==0
out=r/'builds'/f'{phase}-artifacts'
out.mkdir(exist_ok=False)
records=[]
for name in ['codex-app-server','codex-code-mode-host']:
 src=r/'builds/target/aarch64-apple-darwin/release'/name
 dest=out/name
 shutil.copy2(src,dest)
 records.append({'name':name,'path':str(dest),'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'file':subprocess.check_output(['/usr/bin/file',str(dest)],text=True).strip()})
(out/'MANIFEST.json').write_text(json.dumps({'phase':phase,'artifacts':records},indent=2)+'\n')
print(json.dumps(records,indent=2))
