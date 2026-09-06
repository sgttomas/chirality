import subprocess,json
from pathlib import Path
s=Path('/private/tmp/runtime-execution-20260906/supply')
p=str(s/'nested-control.sb')
commands=[['/usr/bin/sandbox-exec','-f',p,'/usr/bin/true'],['/usr/bin/sandbox-exec','-f',p,'/usr/bin/sandbox-exec','-f',p,'/usr/bin/true']]
res=[]
for c in commands:
 r=subprocess.run(c,capture_output=True,text=True,timeout=5);res.append({'argv':c,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
(s/'nested-control.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res))
