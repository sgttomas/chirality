from pathlib import Path
import subprocess,os,json,time,socket,urllib.request,urllib.parse
repo=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip());out=Path(__file__).resolve().parent;front=repo/'projects/chirality-app-dev/frontend';scratch=Path('/private/tmp/ch-v3-gui-20260906');assert not scratch.exists();scratch.mkdir(mode=0o700)
env=os.environ.copy()
for k in list(env):
 if k.startswith('CHIRALITY_') or k.endswith('_API_KEY') or k in ['ANTHROPIC_AUTH_TOKEN','ELECTRON_RUN_AS_NODE']:env.pop(k,None)
env.update({'CHIRALITY_INSTRUCTION_ROOT':str(repo),'CHIRALITY_HARNESS_PROVIDER':'stub','NEXT_TELEMETRY_DISABLED':'1','CHIRALITY_RUNTIME_USER_DATA':str(scratch/'data'),'CHIRALITY_USER_DATA':str(scratch/'data'),'CHIRALITY_RUNTIME_SOCKET_PATH':str(scratch/'control.sock'),'CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE':str(scratch/'data/runtime/auth/tokens/operator.token')})
def save(n,v):(out/n).write_text(json.dumps(v,indent=2)+'\n')
procs=[]
def launch(name,args,e):
 log=(out/(name+'.log')).open('w');p=subprocess.Popen(args,cwd=front,env=e,stdout=log,stderr=subprocess.STDOUT,start_new_session=True);log.close();procs.append(p);save(name+'_LAUNCH.json',{'pid':p.pid,'command':args,'cwd':str(front),'environment_overrides':{k:v for k,v in e.items() if k.startswith('CHIRALITY_') or k in ['ELECTRON_RENDERER_URL','NEXT_TELEMETRY_DISABLED']}});return p
try:
 daemon=launch('gui-daemon',[str(front/'node_modules/.bin/electron'),'--user-data-dir='+str(scratch/'data'),str(front/'dist-electron/main.js'),'--runtime-daemon'],env)
 for i in range(180):
  if Path(env['CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE']).is_file() and Path(env['CHIRALITY_RUNTIME_SOCKET_PATH']).exists():break
  assert daemon.poll() is None,'daemon exited';time.sleep(.5)
 else:raise RuntimeError('daemon timeout')
 regs=[]
 for label in ['alpha','beta']:
  root=scratch/label;root.mkdir();(root/'execution').mkdir();(root/'notes.md').write_text('# Owned App v3 GUI fixture\nThis disposable document contains no user data.\n')
  manifest={'schemaVersion':'chirality.project/v2','projectId':'app-v3-gui-'+label,'displayName':'App v3 GUI '+label,'workingRoot':'.','instructionRoot':{'mode':'runtime'},'defaultExecutionRoot':'execution','profiles':{'domain':[],'capability':[],'dataBoundary':[]},'enabledAdapterIds':['stub'],'embeddedUi':{'declared':False}}
  file=root/'chirality.project.json';file.write_text(json.dumps(manifest,indent=2)+'\n');save('fixture-'+label+'.json',manifest)
  re=env.copy();re['CHIRALITY_RUNTIME_TOKEN_FILE']=env['CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE'];args=['node',str(front/'dist-runtime/chirality-cli.mjs'),'project','register','--manifest',str(file),'--approved-by','owner-authorized-app-v3-gui-fixtures','--approval-reference','APP_V3_INTEGRATION_2026-09-06','--json'];p=subprocess.run(args,cwd=front,env=re,capture_output=True,text=True);(out/('registration-'+label+'.stderr')).write_text(p.stderr);assert p.returncode==0,p.stderr
  raw=json.loads(p.stdout);reg={k:v for k,v in raw.items() if k in ['projectId','tokenFile','manifestPath','workingRoot','instructionRoot','registeredAt']};regs.append(reg);save('registration-'+label+'.json',{'command':args,'exit_code':0,'result':reg})
 env.update({'CHIRALITY_RUNTIME_TOKEN_FILE':regs[0]['tokenFile'],'CHIRALITY_RUNTIME_PROJECT_ID':'app-v3-gui-alpha','CHIRALITY_RUNTIME_PROJECT_ROOT':str(scratch/'alpha')})
 with socket.socket() as s:s.bind(('127.0.0.1',0));port=s.getsockname()[1]
 url='http://127.0.0.1:'+str(port);server=launch('gui-frontend',['node',str(front/'node_modules/next/dist/bin/next'),'start','--hostname','127.0.0.1','--port',str(port)],env)
 for i in range(90):
  try:
   with urllib.request.urlopen(url+'/api/harness/session/list?'+urllib.parse.urlencode({'projectRoot':str(scratch/'alpha')}),timeout=2) as r:
    if r.status==200:break
  except Exception:pass
  assert server.poll() is None,'server exited';time.sleep(1)
 else:raise RuntimeError('server timeout')
 ui_env=env.copy();ui_env['ELECTRON_RENDERER_URL']=url
 ui=launch('gui-desktop',[str(front/'node_modules/.bin/electron'),'--user-data-dir='+str(scratch/'data'),str(front/'dist-electron/main.js')],ui_env)
 save('GUI_READY.json',{'url':url,'scratch':str(scratch),'roots':[str(scratch/x) for x in ['alpha','beta']],'process_ids':[p.pid for p in procs],'source_unchanged':True,'provider':'stub','api_list_status':200,'token_bytes_retained':False});print(url,flush=True)
except Exception:
 import signal
 for p in reversed(procs):
  if p.poll() is None:os.killpg(p.pid,signal.SIGTERM)
 raise
