from pathlib import Path
import json, hashlib, subprocess, difflib
r=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
b=r/'projects/chirality-app-dev/execution/_Coordination/AgentRuns/APP_LOOP_SHELL_2026-09-05/iteration-04/instances/pkg02_t3'
m=b/'recovery-author-v10/SOURCE_MANIFEST_v10.json';d=b/'recovery-author-v10/SOURCE_DIFF_v10.json'
assert hashlib.sha256(m.read_bytes()).hexdigest()=='c88cce09a9ad4ea9c9f822d5f410b26e1f04e7c02067ff1398ecf6bcacc807e4'
assert hashlib.sha256(d.read_bytes()).hexdigest()=='d9e0d2e8ba11f47ddeab5ca236bc612a519a3840a5ceab0bf07c30cd7a226772'
manifest=json.loads(m.read_text());diffs={x['path']:x['diff'] for x in json.loads(d.read_text())}
for f in manifest['files']:
 p=f['path'];data=(r/p).read_bytes();assert hashlib.sha256(data).hexdigest()==f['sha256'] and len(data)==f['bytes']
 result=subprocess.run(['git','show',manifest['repo_head']+':'+p],cwd=r,text=True,capture_output=True)
 before=result.stdout if result.returncode==0 else ''
 actual=''.join(difflib.unified_diff(before.splitlines(keepends=True),data.decode().splitlines(keepends=True),fromfile='a/'+p,tofile='b/'+p))
 assert actual==diffs[p],p
print(json.dumps({'status':'PASS','source_identities':18,'full_diff_entries':18,'nonempty_diffs':sum(bool(x) for x in diffs.values())}))
