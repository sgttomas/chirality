from pathlib import Path
import subprocess,selectors,time,json,hashlib
s=Path('/private/tmp/runtime-execution-20260906/supply');env={'PATH':'/usr/bin:/bin:/usr/sbin:/sbin','HOME':str(s/'home'),'CODEX_HOME':str(s/'home'),'TMPDIR':str(s/'tmp')}
assert hashlib.sha256((s/'app-server').read_bytes()).hexdigest()=='b1d1a8c3146b16a01c057e9ecc2213b969a775ba76c424d812714a2911708de2'
args=['/usr/bin/sandbox-exec','-f',str(s/'network-deny.sb'),str(s/'app-server'),'-c','features.plugins=false']
msgs=[json.loads(l) for l in (s/'login-negative-input.jsonl').read_text().splitlines()]
p=subprocess.Popen(args,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,env=env,cwd=s/'work',bufsize=1)
sel=selectors.DefaultSelector();sel.register(p.stdout,selectors.EVENT_READ,'stdout');sel.register(p.stderr,selectors.EVENT_READ,'stderr');events=[]
for m in msgs:
 p.stdin.write(json.dumps(m)+'\n');p.stdin.flush()
 if 'id' not in m:continue
 deadline=time.monotonic()+8
 done=False
 while time.monotonic()<deadline and not done:
  for k,_ in sel.select(.2):
   line=k.fileobj.readline()
   if not line:continue
   events.append({'stream':k.data,'line':line.rstrip()})
   if k.data=='stdout':
    try: done=json.loads(line).get('id')==m['id']
    except ValueError:pass
 if not done:events.append({'missing_response':m['id']})
p.stdin.close()
try:p.wait(timeout=3)
except subprocess.TimeoutExpired:p.terminate();p.wait(timeout=3)
(s/'login-negative.json').write_text(json.dumps({'events':events,'exit':p.returncode},indent=2)+'\n')
print(json.dumps({'response_ids':[json.loads(x['line']).get('id') for x in events if x.get('stream')=='stdout'],'missing':[x for x in events if 'missing_response' in x],'exit':p.returncode}))
