from pathlib import Path
import subprocess,os,json,time,socket,urllib.request,urllib.error,hashlib,signal,shutil,datetime
repo=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip());out=Path(__file__).resolve().parent;app=repo/'projects/chirality-app-dev';front=app/'frontend'
scratch=Path('/private/tmp/ch-v3-28a8-20260906')
assert not scratch.exists(),'scratch must be absent'
env=os.environ.copy()
for k in list(env):
 if k.startswith('CHIRALITY_') or k.endswith('_API_KEY') or k in ['ANTHROPIC_AUTH_TOKEN','OPENAI_API_KEY']:env.pop(k,None)
env.update({'CHIRALITY_INSTRUCTION_ROOT':str(repo),'CHIRALITY_HARNESS_PROVIDER':'stub','NEXT_TELEMETRY_DISABLED':'1','CHIRALITY_RUNTIME_USER_DATA':str(scratch),'CHIRALITY_USER_DATA':str(scratch),'CHIRALITY_RUNTIME_SOCKET_PATH':str(scratch/'runtime/control.sock'),'CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE':str(scratch/'runtime/auth/tokens/operator.token')})
assert len(env['CHIRALITY_RUNTIME_SOCKET_PATH'].encode())<=103
def save(name,v):(out/name).write_text(json.dumps(v,indent=2)+'\n')
def run(name,args,cwd,envrun=env):
 start=datetime.datetime.now(datetime.timezone.utc).isoformat()
 p=subprocess.run(args,cwd=cwd,env=envrun,capture_output=True,text=True)
 (out/(name+'.stdout')).write_text(p.stdout);(out/(name+'.stderr')).write_text(p.stderr)
 save(name+'.json',{'command':args,'cwd':str(cwd),'started':start,'exit_code':p.returncode,'environment_overrides':{k:v for k,v in envrun.items() if k.startswith('CHIRALITY_') or k in ['HARNESS_BASE_URL','HARNESS_PROJECT_ROOT','NEXT_TELEMETRY_DISABLED']}})
 print(name,p.returncode,flush=True);return p
assert run('native-freshness',['git','fetch','origin','main'],repo).returncode==0
assert run('native-ancestor',['git','merge-base','--is-ancestor','origin/main','HEAD'],repo).returncode==0
scratch.mkdir(mode=0o700);(front/'.chirality/sessions').mkdir(parents=True,exist_ok=True)
save('FIXTURE_SCOPE.json',{'head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=repo,text=True).strip(),'scratch':str(scratch),'socket':env['CHIRALITY_RUNTIME_SOCKET_PATH'],'socket_bytes':len(env['CHIRALITY_RUNTIME_SOCKET_PATH'].encode()),'token_contents_retained':False,'provider':'stub','native_sandbox_disabled':False})
daemon=None;server=None;handles=[];results={}
try:
 args=[str(front/'node_modules/.bin/electron'),'--user-data-dir='+str(scratch),str(front/'dist-electron/main.js'),'--runtime-daemon']
 log=(out/'daemon.log').open('w');handles.append(log);daemon=subprocess.Popen(args,cwd=front,env=env,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
 save('DAEMON_LAUNCH.json',{'command':args,'cwd':str(front),'pid':daemon.pid,'environment_overrides':{k:v for k,v in env.items() if k.startswith('CHIRALITY_')},'started':datetime.datetime.now(datetime.timezone.utc).isoformat()})
 ready=False
 for attempt in range(180):
  if daemon.poll() is not None:break
  if Path(env['CHIRALITY_RUNTIME_SOCKET_PATH']).exists() and Path(env['CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE']).is_file():ready=True;break
  time.sleep(.5)
 results['daemon_ready']=ready;results['daemon_exit']=daemon.poll();save('NATIVE_PROGRESS.json',results);print('daemon_ready',ready,flush=True)
 if not ready:raise RuntimeError('daemon readiness failed')
 regenv=env.copy();regenv['CHIRALITY_RUNTIME_TOKEN_FILE']=env['CHIRALITY_RUNTIME_OPERATOR_TOKEN_FILE']
 args=['node',str(front/'dist-runtime/chirality-cli.mjs'),'project','register','--manifest',str(app/'chirality.project.json'),'--approved-by','owner-authorized-app-v3-integration','--approval-reference','APP_V3_INTEGRATION_2026-09-06-owner-staged-execution','--json']
 p=subprocess.run(args,cwd=repo,env=regenv,capture_output=True,text=True)
 # Registration returns public token-file path, never persist arbitrary secret fields.
 (out/'registration.stderr').write_text(p.stderr)
 if p.returncode:save('REGISTRATION.json',{'exit_code':p.returncode,'command':args,'stdout_redacted':True});raise RuntimeError('registration failed')
 registration=json.loads(p.stdout);token=registration.get('tokenFile');assert token and Path(token).resolve().is_relative_to(scratch.resolve())
 save('REGISTRATION.json',{'exit_code':p.returncode,'command':args,'public_result':{k:v for k,v in registration.items() if k in ['projectId','tokenFile','manifestPath','workingRoot','instructionRoot','registeredAt']},'other_fields_omitted':True})
 env.update({'CHIRALITY_RUNTIME_TOKEN_FILE':token,'CHIRALITY_RUNTIME_PROJECT_ID':'chirality-app-dev','CHIRALITY_RUNTIME_PROJECT_ROOT':str(app),'HARNESS_PROJECT_ROOT':str(app)})
 with socket.socket() as s:s.bind(('127.0.0.1',0));port=s.getsockname()[1]
 env['HARNESS_BASE_URL']='http://127.0.0.1:'+str(port)
 args=['node',str(front/'node_modules/next/dist/bin/next'),'dev','--hostname','127.0.0.1','--port',str(port)]
 log=(out/'frontend.log').open('w');handles.append(log);server=subprocess.Popen(args,cwd=front,env=env,stdout=log,stderr=subprocess.STDOUT,start_new_session=True)
 save('FRONTEND_LAUNCH.json',{'command':args,'pid':server.pid,'cwd':str(front),'environment_overrides':{k:v for k,v in env.items() if k.startswith('CHIRALITY_') or k.startswith('HARNESS_')}})
 from urllib.parse import urlencode
 url=env['HARNESS_BASE_URL']+'/api/harness/session/list?'+urlencode({'projectRoot':str(app)})
 statuses=[]
 for attempt in range(90):
  if server.poll() is not None:break
  try:
   with urllib.request.urlopen(url,timeout=2) as response:
    statuses.append(response.status)
    if response.status==200:break
  except urllib.error.HTTPError as e:statuses.append(e.code)
  except Exception as e:statuses.append(type(e).__name__)
  time.sleep(1)
 results['api_ready']=bool(statuses and statuses[-1]==200);save('API_READINESS.json',{'url':url,'observations':statuses,'ready':results['api_ready']})
 if not results['api_ready']:raise RuntimeError('API readiness failed')
 p=run('configured-premerge',['npm','run','harness:validate:premerge'],front,env);results['premerge_exit']=p.returncode
 for rel in ['artifacts/harness/section8/latest/summary.json']:
  f=front/rel
  if f.is_file():shutil.copyfile(f,out/'CONFIGURED_PREMERGE_SUMMARY.json')
except Exception as e:
 results['error']=str(e);print('native error',str(e),flush=True)
finally:
 cleanup={}
 for name,p in [('frontend',server),('daemon',daemon)]:
  if p is None:continue
  if p.poll() is None:
   os.killpg(p.pid,signal.SIGTERM)
   try:p.wait(timeout=15)
   except subprocess.TimeoutExpired:os.killpg(p.pid,signal.SIGKILL);p.wait(timeout=5);cleanup[name+'_forced']=True
  cleanup[name]={'pid':p.pid,'exit_code':p.returncode}
 for h in handles:h.close()
 cleanup['socket_exists_before_scratch_removal']=Path(env['CHIRALITY_RUNTIME_SOCKET_PATH']).exists()
 if scratch.is_dir():shutil.rmtree(scratch)
 cleanup['scratch_absent']=not scratch.exists()
 if server is not None:
  with socket.socket() as s:cleanup['frontend_connect_ex']=s.connect_ex(('127.0.0.1',port))
 save('NATIVE_CLEANUP.json',cleanup);save('NATIVE_RESULT.json',results)
 print('native result',results,flush=True)
