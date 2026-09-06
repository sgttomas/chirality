"""Capture only after exact admitted Candidate3 build succeeds; never substitute copied outputs."""
from pathlib import Path
import hashlib,json,os,shutil,subprocess,time
E=Path(__file__).resolve().parent
N=Path('/private/tmp/runtime-execution-20260906/supplier-candidate/candidate3')
O=N.parent

def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def save(n,obj):
 with (E/n).open('x') as f:json.dump(obj,f,indent=2);f.write('\n')
receipt=json.loads((N/'builds/candidate3.json').read_text())
pins=json.loads((E/'REVIEW_PINS.json').read_text())
assert receipt['exit']==0
assert receipt['source_sha256']==receipt['source_after_sha256']==pins['source_sha256']
assert receipt['runner_sha256']==pins['runner_sha256']==sha(N/'run.py')
assert receipt['log_sha256']==sha(N/'builds/candidate3.log')
assert sha(N/'source/codex-rs/exec-server/src/fs_sandbox.rs')==pins['source_sha256']
old=json.loads((E/'COPIED_BEFORE.json').read_text())['preexisting_target_outputs']
artifacts=[]
policy='(version 1)(allow default)(deny network*)(deny file-write* (require-not (require-any (subpath '+json.dumps(str(N))+') (literal "/dev/null"))))'
for name in ['codex-app-server','codex-code-mode-host']:
 src=N/'target/aarch64-apple-darwin/release'/name;dst=N/'artifacts'/name
 assert not dst.exists()
 src_stat=src.stat();digest=sha(src)
 if name=='codex-app-server':
  assert digest!=old[name]['sha256'], 'stale copied app-server is not Candidate3'
  assert src_stat.st_mtime_ns>old[name]['mtime_ns']
  assert src_stat.st_mtime_ns>=int(receipt['started']*1e9)
 shutil.copy2(src,dst)
 assert sha(dst)==digest
 version=None
 if name=='codex-app-server':
  r=subprocess.run(['/usr/bin/sandbox-exec','-p',policy,str(dst),'--version'],cwd=N,env={'PATH':'/usr/bin:/bin:/usr/sbin:/sbin','TMPDIR':str(N/'tmp')},text=True,capture_output=True,timeout=10)
  version={'exit':r.returncode,'stdout':r.stdout,'stderr':r.stderr};assert r.returncode==0
 artifacts.append({'name':name,'path':str(dst),'sha256':digest,'bytes':dst.stat().st_size,'source_mtime_ns':src_stat.st_mtime_ns,'capture_mtime_ns':dst.stat().st_mtime_ns,'source_inode':src_stat.st_ino,'capture_inode':dst.stat().st_ino,'version':version,'file':subprocess.check_output(['/usr/bin/file',str(dst)],text=True).strip(),'same_bytes_as_copied_target':digest==old[name]['sha256'],'provenance':'fresh successful Candidate3 build; code-host may be unchanged dependency output' if name=='codex-code-mode-host' else 'new app-server bytes from admitted repaired source'})
for phase in ['helper-tests','protected-glob-tests','candidate3']:
 for ext in ['json','log','pid.json']:
  src=N/'builds'/f'{phase}.{ext}';dst=E/f'{phase}.{ext}';assert not dst.exists();shutil.copy2(src,dst)
policies=[]
for line in (N/'builds/helper-tests.log').read_text().splitlines():
 if 'helper policy writable=' in line:
  start=line.index('helper policy writable='); label,raw=line[start:].split(': ',1);policies.append({'label':label,'command':json.loads(raw)})
assert len(policies)==4
save('GENERATED_HELPER_POLICIES.json',policies)
base=json.loads((E/'ORIGINAL_BEFORE.json').read_text());source={n:sha(O/'source/codex'/n) for n in base['source_files']};assert source==base['source_files']
for a in base['retained_artifacts']:assert sha(Path(a['path']))==a['sha256']
repaired=json.loads((E/'SOURCE_REPAIRED.json').read_text())['source_files'];actual={n:sha(N/'source'/n) for n in repaired};assert actual==repaired
seal=json.loads((E.parents[1]/'SUPPLIER/OUTPUT_MANIFEST.json').read_text());assert all(sha(E.parents[1]/'SUPPLIER'/n)==h for n,h in seal.items())
save('ARTIFACT_MANIFEST.json',{'captured':time.time(),'artifacts':artifacts,'completion_sha256':sha(N/'builds/candidate3.json'),'source_sha256':pins['source_sha256'],'runner_sha256':pins['runner_sha256'],'acceptance':'unaccepted Candidate3 supplier artifact; actual alias backcheck remains parent-owned'})
save('POST_BUILD_VERIFICATION.json',{'source6416_original_unchanged':True,'retained7_artifacts_unchanged':True,'supplier70file_seal_unchanged':True,'candidate3_source_manifest_stable':True,'original_manifest_sha256':sha(E/'ORIGINAL_BEFORE.json'),'repaired_manifest_sha256':sha(E/'SOURCE_REPAIRED.json'),'process_metadata':subprocess.check_output(['ps','-axo','pid,ppid,comm'],text=True),'process_scope':'metadata census; no exhaustive orphan proof','owned_phases':[json.loads((N/'builds'/f'{p}.pid.json').read_text()) for p in ['helper-tests','protected-glob-tests','candidate3']]})
print(json.dumps(artifacts,indent=2))
