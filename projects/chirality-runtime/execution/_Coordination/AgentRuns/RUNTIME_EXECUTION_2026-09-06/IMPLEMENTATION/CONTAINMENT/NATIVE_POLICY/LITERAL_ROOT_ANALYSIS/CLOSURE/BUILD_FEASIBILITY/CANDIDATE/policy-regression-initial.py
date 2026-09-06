import os,json,subprocess,hashlib
from pathlib import Path
r=Path('/private/tmp/runtime-execution-20260906/supplier-candidate')
t=r/'tmp/policy-regression'; t.mkdir(mode=0o700,exist_ok=False)
root=t/'project';root.mkdir(mode=0o700)
foreign=t/'foreign';foreign.mkdir(mode=0o700)
canary=foreign/'canary';canary.write_text('PRIVATE_CANARY\n')
source='codex-rs/sandboxing/src/seatbelt_base_policy.sbpl'
baseline=subprocess.check_output(['git','show','HEAD:'+source],cwd=r/'source/codex',text=True)
patched=(r/'source/codex'/source).read_text()
extra='\n(allow file-read-metadata)\n(allow file-read* (subpath "/bin") (subpath "/usr/lib") (literal "/usr/bin/nc"))\n(allow file-read* file-write* (subpath '+json.dumps(str(root))+'))\n'
script='printf STARTED; printf allowed > '+str(root/'allowed')+'; if /bin/cat '+str(canary)+' >/dev/null 2>&1; then printf READ_BREACH; else printf READ_DENIED; fi; if (printf forbidden > '+str(foreign/'forbidden')+') 2>/dev/null; then printf WRITE_BREACH; else printf WRITE_DENIED; fi; /usr/bin/nc -z -w 1 127.0.0.1 9; printf DONE'
env={'PATH':'/usr/bin:/bin','TMPDIR':str(root),'LANG':'C','LC_ALL':'C'}
results=[]
for name,base in [('baseline',baseline),('patched',patched)]:
 policy=t/(name+'.sb');policy.write_text(base+extra)
 p=subprocess.run(['/usr/bin/sandbox-exec','-f',str(policy),'/bin/sh','-c',script],cwd=root,env=env,capture_output=True,text=True,timeout=10)
 results.append({'variant':name,'profile_sha256':hashlib.sha256(policy.read_bytes()).hexdigest(),'exit':p.returncode,'stdout':p.stdout,'stderr':p.stderr,'allowed_write_exists':(root/'allowed').exists(),'outside_write_exists':(foreign/'forbidden').exists()})
(r/'builds/policy-regression.json').write_text(json.dumps({'scope':'Direct exact-source base-policy diagnostic; not App Server turn or descendant conformance','results':results},indent=2)+'\n')
print(json.dumps(results,indent=2))
assert results[0]['exit']!=0 and 'STARTED' not in results[0]['stdout']
assert results[1]['exit']==0 and results[1]['stdout']=='STARTEDREAD_DENIEDWRITE_DENIEDDONE' and results[1]['allowed_write_exists'] and not results[1]['outside_write_exists']
assert 'Operation not permitted' in results[1]['stderr']
