from pathlib import Path
import sys,subprocess,json,datetime
p=Path(__file__).resolve().parent
name=sys.argv[1];c=['/usr/bin/swift','-module-cache-path','/private/tmp/app-loop-t3-native-ac3dexfs/swift-cache',str(p/'window_inventory.swift')]
a=subprocess.run(c,capture_output=True,text=True,timeout=15);d={'command':c,'exit':a.returncode,'stdout':a.stdout,'stderr':a.stderr,'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat()};(p/(name+'-inventory.json')).write_text(json.dumps(d,indent=2)+'\n')
w=json.loads(a.stdout);print(json.dumps([{'id':x['kCGWindowNumber'],'app':x['kCGWindowOwnerName'],'pid':x['kCGWindowOwnerPID'],'title':x.get('kCGWindowName'),'bounds':x['kCGWindowBounds'],'onscreen':x.get('kCGWindowIsOnscreen',False)} for x in w if x['kCGWindowBounds']['Height']>100 and x.get('kCGWindowLayer')==0],indent=2))
for arg in sys.argv[2:]:
 ident=int(arg);match=next(x for x in w if x['kCGWindowNumber']==ident);baseline=json.loads(json.loads((p/'NATIVE_INVENTORY_HOST_01.json').read_text())['stdout']);assert ident not in {x['kCGWindowNumber'] for x in baseline},'do not capture preexistingwindow'
 target=p/(name+'-'+str(ident)+'.png');cmd=['/usr/sbin/screencapture','-x','-o','-l',str(ident),str(target)];r=subprocess.run(cmd,capture_output=True,text=True,timeout=10);(p/(name+'-'+str(ident)+'-capture.json')).write_text(json.dumps({'command':cmd,'window':match,'exit':r.returncode,'stdout':r.stdout,'stderr':r.stderr},indent=2)+'\n');print('capture',ident,r.returncode)
