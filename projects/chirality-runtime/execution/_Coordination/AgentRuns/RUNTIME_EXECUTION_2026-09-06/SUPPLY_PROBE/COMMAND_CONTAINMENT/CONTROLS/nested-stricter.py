import subprocess,json
from pathlib import Path
s=Path('/private/tmp/runtime-execution-20260906/supply');res=[]
for inner in ['matrix2-network-home.sb','matrix2-network-write.sb','matrix2-network-keychain.sb']:
 c=['/usr/bin/sandbox-exec','-f',str(s/'nested-control.sb'),'/usr/bin/sandbox-exec','-f',str(s/inner),'/usr/bin/true'];p=subprocess.run(c,capture_output=True,text=True,timeout=5,cwd=s/'work');res.append({'inner':inner,'exit_code':p.returncode,'stderr':p.stderr})
(s/'nested-stricter.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
