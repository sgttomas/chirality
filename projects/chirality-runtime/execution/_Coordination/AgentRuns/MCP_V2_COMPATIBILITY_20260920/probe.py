import os,sys,json,subprocess,threading,queue,datetime,hashlib,signal
from pathlib import Path
root=Path(__file__).resolve().parent
binary=Path('/Applications/ChatGPT.app/Contents/Resources/codex')
wire=root/'mcp-wire.jsonl';frames=[];events=queue.Queue();stderr=[]
profile=root/'isolation.sb'
profile.write_text('(version 1)\n(allow default)\n(deny network*)\n(deny file-read* file-write* (subpath "/Users/ryan/.codex"))\n(deny file-read* file-write* (subpath "/Users/ryan/Library/Keychains"))\n(deny file-read* file-write* (subpath "/Users/ryan/Library/Application Support"))\n')
config='mcp_servers={chirality_v2_probe={command="/usr/bin/python3",args=['+json.dumps(str(root/'server.py'))+','+json.dumps(str(wire))+'],startup_timeout_sec=5,tool_timeout_sec=5,required=true}}'
cmd=['/usr/bin/sandbox-exec','-f',str(profile),str(binary),'-c',config,'app-server','--listen','stdio://']
env={'PATH':'/usr/bin:/bin:/usr/sbin:/sbin','HOME':str(root/'home'),'CODEX_HOME':str(root/'codex-home'),'TMPDIR':str(root),'LANG':'en_US.UTF-8'}
start=datetime.datetime.now(datetime.timezone.utc).isoformat()
p=subprocess.Popen(cmd,env=env,cwd=root/'cwd',stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,start_new_session=True)
def reader():
 for line in p.stdout:
  try:v=json.loads(line)
  except Exception:v={'unparsed':line.rstrip()}
  frames.append({'direction':'app-server-to-driver','frame':v});events.put(v)
def err_reader():
 for line in p.stderr:
  if '@' not in line:stderr.append(line)
threading.Thread(target=reader,daemon=True).start();threading.Thread(target=err_reader,daemon=True).start()
def send(frame):
 frames.append({'direction':'driver-to-app-server','frame':frame});p.stdin.write(json.dumps(frame)+'\n');p.stdin.flush()
def request(i,method,params,timeout=15):
 send({'id':i,'method':method,'params':params})
 import time
 end=time.monotonic()+timeout
 while time.monotonic()<end:
  try:v=events.get(timeout=max(.01,end-time.monotonic()))
  except queue.Empty:break
  if v.get('id')==i:return v
 raise RuntimeError('Timed out on '+method)
report={'started':start,'binary':str(binary),'version':subprocess.check_output([str(binary),'--version'],env=env,text=True).strip(),'network':'denied by sandbox','home':'fresh scratch','targetProtocol':'2026-07-28','modelTurns':0}
try:
 report['initialize']=request(1,'initialize',{'clientInfo':{'name':'chirality_mcp_v2_compatibility','version':'0.0.0'},'capabilities':{'experimentalApi':True}})
 send({'method':'initialized','params':{}})
 report['threadStart']=request(2,'thread/start',{'cwd':str(root/'cwd'),'ephemeral':True,'approvalPolicy':'never','sandbox':'read-only'},20)
 # Readiness inventory triggers the actual configured MCP client, without inference.
 thread=(report['threadStart'].get('result',{}).get('thread') or {}).get('id')
 if thread:
  report['inventory']=request(3,'mcpServerStatus/list',{'threadId':thread},12)
 raw=[json.loads(line) for line in wire.read_text().splitlines()] if wire.exists() else []
 inbound=[v['frame'] for v in raw if v['direction']=='client-to-server']
 report['mcpMethods']=[v.get('method') for v in inbound]
 report['legacyInitializeObserved']=any(v.get('method')=='initialize' for v in inbound)
 modern=[v for v in inbound if v.get('params',{}).get('_meta',{}).get('io.modelcontextprotocol/protocolVersion')=='2026-07-28']
 report['modernRequests']=len(modern)
 if report['legacyInitializeObserved']:
  report['result']='INCOMPATIBLE_LEGACY_HANDSHAKE';report['remaining']='Tool call, reconnect, isolation and cancellation not reached. No legacy success or downgrade accepted.'
 elif modern and thread:
  report['callA']=request(4,'mcpServer/tool/call',{'threadId':thread,'server':'chirality_v2_probe','tool':'inspect_fixture','arguments':{'workspace':'invented-A','basis':'A-1'}})
  report['callB']=request(5,'mcpServer/tool/call',{'threadId':thread,'server':'chirality_v2_probe','tool':'inspect_fixture','arguments':{'workspace':'invented-B','basis':'B-1'}})
  report['result']='MODERN_EXCHANGE_REQUIRES_INSPECTION'
 else:report['result']='INCONCLUSIVE_NO_MODERN_REQUEST'
except Exception as e:report['error']=str(e);report['result']='PROBE_ERROR'
finally:
 try:p.stdin.close();p.wait(timeout=5)
 except subprocess.TimeoutExpired:
  os.killpg(p.pid,signal.SIGTERM)
  try:p.wait(timeout=3)
  except subprocess.TimeoutExpired:os.killpg(p.pid,signal.SIGKILL);p.wait()
 # Process group belongs solely to this scratch invocation and its fixture.
 try:os.killpg(p.pid,signal.SIGTERM)
 except ProcessLookupError:pass
 report['exitCode']=p.returncode;report['ended']=datetime.datetime.now(datetime.timezone.utc).isoformat()
 h=hashlib.sha256()
 with binary.open('rb') as f:
  for block in iter(lambda:f.read(1048576),b''):h.update(block)
 report['binarySha256']=h.hexdigest()
 (root/'app-server-wire.json').write_text(json.dumps(frames,indent=2)+'\n');(root/'stderr.log').write_text(''.join(stderr));(root/'result.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:report.get(k) for k in ['result','version','mcpMethods','legacyInitializeObserved','modernRequests','error','exitCode','ended','binarySha256']},indent=2))
 print('Evidence: '+str(root))
