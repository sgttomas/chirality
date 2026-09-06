from pathlib import Path
import subprocess,json,os,hashlib
s=Path('/private/tmp/runtime-execution-20260906/supply')
for n in ['home','work','tmp']: (s/n).mkdir(exist_ok=True)
profile='''(version 1)
(allow default)
(deny network*)
(deny file-write*)
(allow file-write* (subpath "/private/tmp/runtime-execution-20260906/supply"))
(deny file-read* (subpath "/Users/ryan"))
(deny mach-lookup (global-name "com.apple.securityd"))
'''
(s/'network-deny.sb').write_text(profile)
config='''approval_policy = "never"
sandbox_mode = "workspace-write"
allow_login_shell = false
cli_auth_credentials_store = "file"
check_for_update_on_startup = false
web_search = "disabled"
[sandbox_workspace_write]
network_access = false
exclude_slash_tmp = true
exclude_tmpdir_env_var = true
[features]
plugins = false
[analytics]
enabled = false
[feedback]
enabled = false
'''
(s/'home/config.toml').write_text(config)
env={'PATH':'/usr/bin:/bin:/usr/sbin:/sbin','HOME':str(s/'home'),'CODEX_HOME':str(s/'home'),'TMPDIR':str(s/'tmp')}
base=['/usr/bin/sandbox-exec','-f',str(s/'network-deny.sb')]
def run(name,args,inp=None):
 try:
  r=subprocess.run(args,input=inp,text=True,capture_output=True,env=env,cwd=s/'work',timeout=12)
  out={'exit':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
 except subprocess.TimeoutExpired as e:out={'exit':'TIMEOUT','stdout':str(e.stdout),'stderr':str(e.stderr)}
 (s/(name+'.json')).write_text(json.dumps(out,indent=2)+'\n');return out
r=run('containment-preflight',base+['/bin/sh','-c','/usr/bin/curl --max-time 1 http://127.0.0.1:9; /bin/cat /Users/ryan/.codex/config.toml; /usr/bin/touch /private/tmp/runtime-supply-forbidden-canary'])
print(r)
assert 'sandbox_apply' not in r['stderr'] and 'curl:' in r['stderr'] and 'cat:' in r['stderr'] and 'touch:' in r['stderr'] and r['exit']!=0, 'Containment not proven'
r=run('signature',['/usr/bin/codesign','--verify','--deep','--strict',str(s/'app-server')]); print('signature',r)
r=run('version',base+[str(s/'app-server'),'--version']);print('version',r)
if r['exit']!=0:raise SystemExit('Exact original executable unavailable; no transformed artifact executed')
msgs=[{'method':'initialize','id':1,'params':{'clientInfo':{'name':'chirality_runtime_offline_probe','version':'0.0.0'},'capabilities':{'experimentalApi':True}}},{'method':'initialized'}, {'method':'config/read','id':2,'params':{'includeLayers':True,'cwd':str(s/'work')}},{'method':'configRequirements/read','id':3,'params':{}},{'method':'experimentalFeature/list','id':4,'params':{'limit':100}}]
(s/'input.jsonl').write_text('\n'.join(json.dumps(m) for m in msgs)+'\n')
r=run('protocol',base+[str(s/'app-server'),'-c','features.plugins=false'],(s/'input.jsonl').read_text()); print('protocol',r['exit'],len(r['stdout']))
