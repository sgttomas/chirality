import subprocess,json
from pathlib import Path
s=Path('/private/tmp/runtime-execution-20260906/supply')
clauses={'network':'(deny network*)','write':'(deny file-write*)\n(allow file-write* (subpath "'+str(s)+'"))','home':'(deny file-read* (subpath "/Users/ryan"))','keychain':'(deny mach-lookup (global-name "com.apple.securityd"))'}
env={'PATH':'/usr/bin:/bin:/usr/sbin:/sbin','HOME':str(s/'home'),'CODEX_HOME':str(s/'home'),'TMPDIR':str(s/'tmp')}
res=[]
for names in [('network',),('write',),('home',),('keychain',),('network','write'),('network','home'),('network','keychain'),tuple(clauses)]:
 name='-'.join(names);profile='(version 1)\n(allow default)\n'+'\n'.join(clauses[n] for n in names)+'\n';p=s/('matrix2-'+name+'.sb');p.write_text(profile)
 for inner in [s/'nested-control.sb',p]:
  c=['/usr/bin/sandbox-exec','-f',str(p),'/usr/bin/sandbox-exec','-f',str(inner),'/usr/bin/true']
  r=subprocess.run(c,capture_output=True,text=True,timeout=5,env=env,cwd=s/'work');res.append({'variant':name,'inner':str(inner),'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
(s/'nested-matrix2.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
