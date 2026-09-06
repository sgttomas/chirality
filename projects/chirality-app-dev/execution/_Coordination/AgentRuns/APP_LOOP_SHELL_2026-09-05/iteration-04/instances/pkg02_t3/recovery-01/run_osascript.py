from pathlib import Path
import sys,subprocess,json,os,datetime
p=Path(__file__).resolve().parent;name=sys.argv[1];cmd=['/usr/bin/osascript',str(p/sys.argv[2])];env={k:os.environ[k] for k in ['PATH','HOME','TMPDIR','LANG','LC_CTYPE','__CF_USER_TEXT_ENCODING'] if k in os.environ}
try:
 r=subprocess.run(cmd,capture_output=True,text=True,timeout=10,env=env);d={'command':cmd,'exit':r.returncode,'stdout':r.stdout,'stderr':r.stderr,'effective_environment':env}
except subprocess.TimeoutExpired as e:d={'command':cmd,'status':'TIMEOUT_10S','stdout':str(e.stdout),'stderr':str(e.stderr),'effective_environment':env}
d['timestamp']=datetime.datetime.now(datetime.timezone.utc).isoformat();(p/(name+'.json')).write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d))
