import subprocess,json
from pathlib import Path
s=Path('/private/tmp/runtime-execution-20260906/supply');original=(s/'network-deny.sb').read_text()
variants={'original':original,'without_keychain_deny':'\n'.join(l for l in original.splitlines() if 'mach-lookup' not in l),'without_home_read_deny':'\n'.join(l for l in original.splitlines() if 'deny file-read' not in l),'without_write_deny':'\n'.join(l for l in original.splitlines() if 'deny file-write' not in l)}
res=[]
for name,profile in variants.items():
 p=s/('nested-'+name+'.sb');p.write_text(profile+'\n')
 c=['/usr/bin/sandbox-exec','-f',str(p),'/usr/bin/sandbox-exec','-f',str(s/'nested-control.sb'),'/usr/bin/true']
 r=subprocess.run(c,capture_output=True,text=True,timeout=5);res.append({'variant':name,'argv':c,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
(s/'nested-matrix.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
