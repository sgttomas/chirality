from pathlib import Path
import sys,subprocess,json,datetime
p=Path(__file__).resolve().parent;cmd=['/usr/bin/swift','-module-cache-path','/private/tmp/app-loop-t3-native-ac3dexfs/swift-cache',str(p/'ax_owned_windows.swift')]+sys.argv[2:]
try:
 r=subprocess.run(cmd,capture_output=True,text=True,timeout=15);d={'command':cmd,'exit':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
except subprocess.TimeoutExpired as e:d={'command':cmd,'status':'TIMEOUT_15S','stdout':str(e.stdout),'stderr':str(e.stderr)}
d['timestamp']=datetime.datetime.now(datetime.timezone.utc).isoformat();(p/(sys.argv[1]+'.json')).write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(d))
