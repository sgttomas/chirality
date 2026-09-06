"""Bounded recovery proof runner. No build/source/provider actions."""
from pathlib import Path
import os,sys,json,subprocess,datetime,hashlib,threading,signal
# Resolve by marker rather than fixed depth, then independently require git root.
REPO=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip())
T3=Path(__file__).resolve().parent.parent
FRONTEND=REPO/'projects/chirality-app-dev/frontend'
mode=sys.argv[1]; name=sys.argv[2]; out=T3/'recovery-01'/name
out.mkdir(exist_ok=False)
env={k:os.environ[k] for k in ['PATH','HOME','TMPDIR','LANG','LC_CTYPE','__CF_USER_TEXT_ENCODING'] if k in os.environ}
env.update(NEXT_TELEMETRY_DISABLED='1',CHIRALITY_HARNESS_PROVIDER='stub',CHIRALITY_RUNTIME_SOCKET_PATH='/private/tmp/app-loop-t3-native-ac3dexfs/user-data/runtime/control.sock',CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE='/private/tmp/app-loop-t3-native-ac3dexfs/user-data/runtime/auth/tokens/operator.token',T3_BASE_URL='http://127.0.0.1:39119',T3_SOURCE_MANIFEST='../recovery-author-v10/SOURCE_MANIFEST_v10.json',T3_ATTEMPT=name,PLAYWRIGHT_MODULE='/Users/ryan/.npm/_npx/e41f203b7505f1fb/node_modules/playwright/index.mjs',T3_CHROMIUM_EXECUTABLE='/Users/ryan/Library/Caches/ms-playwright/chromium_headless_shell-1223/chrome-headless-shell-mac-arm64/chrome-headless-shell',T3_FRONTEND=str(FRONTEND),T3_REPO_ROOT=str(REPO))
if mode=='server': cmd=['node','node_modules/next/dist/bin/next','start','--hostname','127.0.0.1','--port','39119'];cwd=FRONTEND
elif mode in ['browser','native']:
 cmd=['node',str(T3/mode/sys.argv[3])];cwd=REPO
 if len(sys.argv)>4:env['T3_CHROMIUM_EXECUTABLE']=sys.argv[4]
else:raise ValueError(mode)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
record={'started':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':cmd,'cwd':str(cwd),'effective_environment':env,'runner_sha256':sha(Path(__file__)),'versions':{'node':subprocess.check_output(['node','--version'],text=True).strip(),'python':sys.version},'mode':mode,'source_manifest_sha256':sha(T3/'recovery-author-v10/SOURCE_MANIFEST_v10.json')}
(out/'COMMAND.json').write_text(json.dumps(record,indent=2)+'\n')
stdout=open(out/'stdout.log','wb');stderr=open(out/'stderr.log','wb')
p=subprocess.Popen(cmd,cwd=cwd,env=env,stdin=subprocess.PIPE if mode=='native' else subprocess.DEVNULL,stdout=subprocess.PIPE,stderr=stderr)
(out/'PROCESS.json').write_text(json.dumps({'pid':p.pid,'mode':mode,'owned':True},indent=2)+'\n')
def drain():
 for line in p.stdout:
  stdout.write(line);stdout.flush();sys.stdout.buffer.write(line);sys.stdout.buffer.flush()
thread=threading.Thread(target=drain,daemon=True);thread.start()
try:
 if mode=='native':
  with open(out/'stdin.jsonl','w') as inputs:
   for line in sys.stdin:
    inputs.write(line);inputs.flush();p.stdin.write(line.encode());p.stdin.flush()
    if '"finish"' in line:break
 if mode=='server':
  for line in sys.stdin:
   if line.strip()=='STOP':break
  p.terminate()
 code=p.wait(timeout=180)
except BaseException:
 p.terminate()
 try:code=p.wait(timeout=10)
 except subprocess.TimeoutExpired:p.kill();code=p.wait()
 raise
finally:
 thread.join(timeout=5);stdout.close();stderr.close()
 (out/'EXIT.json').write_text(json.dumps({'finished':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit':p.returncode,'process_reaped':p.poll() is not None,'stdout_sha256':sha(out/'stdout.log'),'stderr_sha256':sha(out/'stderr.log')},indent=2)+'\n')
sys.exit(code)
