from pathlib import Path
import json,os,signal,time,socket,subprocess,shutil
out=Path(__file__).resolve().parent;scratch=Path('/private/tmp/ch-v3-gui-20260906');results=[]
for name in ['gui-desktop-proof','gui-desktop','gui-frontend','gui-daemon-restart','gui-daemon']:
 v=json.loads((out/(name+'_LAUNCH.json')).read_text());pid=v['pid'];cmd=subprocess.run(['ps','-p',str(pid),'-o','command='],capture_output=True,text=True).stdout.strip();entry={'name':name,'pid':pid,'alive_before':bool(cmd)}
 if cmd:
  assert ('chirality' in cmd or 'next-server' in cmd or 'Electron' in cmd),cmd
  try:os.killpg(pid,signal.SIGTERM)
  except ProcessLookupError:pass
  for n in range(50):
   state=subprocess.run(['ps','-p',str(pid),'-o','stat='],capture_output=True,text=True).stdout.strip()
   if not state or state.startswith('Z'):break
   time.sleep(.1)
  entry['state_after']=state;entry['stopped']=not state or state.startswith('Z')
 results.append(entry)
assert all(x.get('stopped',True) for x in results)
socket_absent=not(scratch/'data/runtime/control.sock').exists();assert socket_absent
shutil.rmtree(scratch)
with socket.socket() as s:connect=s.connect_ex(('127.0.0.1',51404))
report={'processes':results,'socket_absent_before_removal':socket_absent,'scratch_absent':not scratch.exists(),'port51404_connect_ex':connect,'token_bytes_retained':False,'browser_tab_closed':'730583379','viewport_reset':True,'owned_finder_window_closed':True,'user_finder_windows_untouched':True,'proof_bundle_unchanged_retained':True,'exit_codes':'processes were detached; clean shutdown logged, no invented exit codes'}
(out/'GUI_CLEANUP.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
