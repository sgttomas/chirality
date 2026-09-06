from pathlib import Path
import subprocess,selectors,time,json,hashlib,os,shutil
s=Path('/private/tmp/runtime-execution-20260906/supply'); home=s/'failure_home'; work=s/'failure_work';temp=s/'failure_tmp'
for x in [home,work,temp]:x.mkdir(exist_ok=False)
(home/'config.toml').write_bytes((s/'home/config.toml').read_bytes())
env={'PATH':'/usr/bin:/bin:/usr/sbin:/sbin','HOME':str(home),'CODEX_HOME':str(home),'TMPDIR':str(temp)}
base=['/usr/bin/sandbox-exec','-f',str(s/'network-deny.sb')]
pre=subprocess.run(base+['/usr/bin/python3','-c','import socket; socket.socket(socket.AF_INET,socket.SOCK_STREAM).connect(("127.0.0.1",9))'],capture_output=True,text=True,env=env,cwd=work,timeout=5)
(s/'offline-preflight.json').write_text(json.dumps({'exit':pre.returncode,'stdout':pre.stdout,'stderr':pre.stderr},indent=2)+'\n')
assert pre.returncode!=0 and 'Operation not permitted' in pre.stderr and 'sandbox_apply' not in pre.stderr
assert not (home/'auth.json').exists()
assert hashlib.sha256((s/'app-server').read_bytes()).hexdigest()=='b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2'
p=subprocess.Popen(base+[str(s/'app-server'),'-c','features.plugins=false'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,env=env,cwd=work)
sel=selectors.DefaultSelector();sel.register(p.stdout,selectors.EVENT_READ,'stdout');sel.register(p.stderr,selectors.EVENT_READ,'stderr');buffers={'stdout':b'','stderr':b''};events=[];requests=[]
def read_for(seconds,target=None):
 end=time.monotonic()+seconds
 while time.monotonic()<end:
  for key,_ in sel.select(.15):
   data=os.read(key.fileobj.fileno(),65536)
   if not data:sel.unregister(key.fileobj);continue
   kind=key.data;buffers[kind]+=data
   while b'\n' in buffers[kind]:
    line,buffers[kind]=buffers[kind].split(b'\n',1);line=line.decode(errors='replace');events.append({'stream':kind,'line':line})
    if kind=='stdout':
     try:m=json.loads(line)
     except ValueError:continue
     if target is not None and m.get('id')==target:return m
 return None
def send(m):
 requests.append(m);p.stdin.write((json.dumps(m)+'\n').encode());p.stdin.flush()
send({'method':'initialize','id':1,'params':{'clientInfo':{'name':'chirality_runtime_offline_failure_probe','version':'0.0.0'},'capabilities':{'experimentalApi':True}}});assert read_for(5,1).get('result')
send({'method':'initialized'})
send({'method':'account/read','id':2,'params':{'refreshToken':False}});account=read_for(5,2);assert account['result']['account'] is None
send({'method':'thread/start','id':3,'params':{'cwd':str(work),'ephemeral':True,'sandbox':'workspace-write','approvalPolicy':'never','model':'offline-invalid-model'}});tr=read_for(6,3)
if tr and tr.get('result'):
 tid=tr['result']['thread']['id'];assert tr['result']['thread']['ephemeral'] is True
 send({'method':'turn/start','id':4,'params':{'threadId':tid,'model':'offline-invalid-model','input':[{'type':'text','text':'Offline failure-path probe. Do not use tools.'}]}});read_for(12)
p.stdin.close()
try:p.wait(timeout=3)
except subprocess.TimeoutExpired:p.terminate();p.wait(timeout=3)
result={'requests':requests,'events':events,'exit':p.returncode,'auth_file_after':(home/'auth.json').exists(),'payload_sha256_after':hashlib.sha256((s/'app-server').read_bytes()).hexdigest()}
(s/'offline-failure.json').write_text(json.dumps(result,indent=2)+'\n')
for x in [home,work,temp]:shutil.rmtree(x)
print(json.dumps({'exit':p.returncode,'event_count':len(events),'requests':[r['method'] for r in requests]}))
