"""Feed ROOT's retained PID arrays through v3's pure fake binding; no live API."""
from contextlib import ExitStack
import ctypes as C
import hashlib,importlib.util,json
from pathlib import Path
import sys
from types import SimpleNamespace
from unittest.mock import patch
HERE=Path(__file__).resolve().parent;RUN=HERE.parents[2]
BLOCK=('ctypes.CDLL','subprocess.Popen','os.fork','os.execve','os.execvpe','os.kill','os.killpg','os.setsid','os.setpgid','socket.socketpair','signal.signal','os._exit','fcntl.flock')
def blocked(*a,**k):raise AssertionError('LIVE CAPABILITY FORBIDDEN')
source=RUN/'tools/host_guard_v3.py';path=RUN/'instances/ROOT-GUARD-V3-QUALIFICATION/provider_01/NATIVE_PID_LIST_WITNESS.json';record=json.loads(path.read_text());result=[]
with ExitStack() as f:
 for t in BLOCK:f.enter_context(patch(t,side_effect=blocked))
 spec=importlib.util.spec_from_file_location('native_witness_backcheck',source);g=importlib.util.module_from_spec(spec);sys.modules[spec.name]=g;spec.loader.exec_module(g)
 for sample in record['samples']:
  pids=sample['pids'];assert sample['returned_bytes']==len(pids)*record['pid_int_bytes'];assert sample['zero_count']==pids.count(0);assert sample['duplicate_count']==len(pids)-len(set(pids));assert sample['negative_count']==sum(p<0 for p in pids);assert sample['errno']==0 and not sample['saturated'];assert 0<sample['returned_bytes']<sample['buffer_bytes'];assert sample['finished']>=sample['started']
  def fake(flavor,value,buffer,size):
   assert (flavor,value)==(sample['flavor'],sample['selector']);assert len(pids)*C.sizeof(C.c_int)<size
   for i,pid in enumerate(pids):buffer[i]=pid
   return sample['returned_bytes']
  p=object.__new__(g.MacProvider);p.trace=None;p.lib=SimpleNamespace(proc_listpids=fake)
  actual=p._pid_list(sample['flavor'],sample['selector'],32768 if sample['flavor']==1 else g.MAX_MEMBERS)
  assert actual==set(pids)
  result.append({'index':sample['index'],'flavor':sample['flavor'],'pid_count':len(pids),'zero_count':pids.count(0),'duplicates':len(pids)-len(actual),'v3_accepts_observed_shape':True,'native_elapsed_seconds':sample['finished']-sample['started']})
print(json.dumps({'witness_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'guard_v3_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'records':result,'live_execution_by':'ROOT; this reviewer only replayed retained arrays through fake binding','limit':'Successful host snapshots support current zero/count representation, not atomic enumeration or all future churn.'},indent=2))
