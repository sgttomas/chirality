"""Independent fake-native backcheck. No author Scenario helper or live provider."""
from contextlib import ExitStack
import ctypes as C
import errno
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
from types import SimpleNamespace
from unittest.mock import patch
HERE=Path(__file__).resolve().parent;RUN=HERE.parents[2]
BLOCK=('os.kill','os.killpg','os.fork','os.execvpe','os.execve','os.setsid','os.setpgid','os._exit','fcntl.flock','subprocess.Popen','ctypes.CDLL','socket.socketpair','signal.signal','time.sleep','os.getsid','os.getpgid','os.getpgrp','os.getpid','os.getuid','os.geteuid')
def forbidden(*a,**k):raise AssertionError('LIVE CAPABILITY FORBIDDEN')
with ExitStack() as fence:
 for x in BLOCK:fence.enter_context(patch(x,side_effect=forbidden))
 spec=importlib.util.spec_from_file_location('independent_guard_v3',RUN/'tools/host_guard_v3.py');g=importlib.util.module_from_spec(spec);sys.modules[spec.name]=g;spec.loader.exec_module(g)
L=4000;A=4100;B=4200;D=4300;S=5000
leader=g.Identity(L,10000,0,502,502,L,L)
def ident(pid):return g.Identity(pid,10000,pid-L,502,502,L,L)
class World:
 def __init__(self,frames,*,fail=None,partial=None,global_extra=None,native=False,advance=0):
  self.frames=frames;self.index=-1;self.clock=100.;self.fail=fail or {};self.partial=partial or {};self.global_extra=global_extra;self.native=native;self.advance=advance;self.calls=[];self.count={};self.records=[];self.memory={L:(100,80),A:(300,200),B:(900,700),D:(500,450)}
  self.p=object.__new__(g.MacProvider);self.p.known={};self.p.seen={};self.p.departed={};self.p.trace=lambda event,**data:self.records.append((event,data));self.p.table=self.table;self.p.lib=SimpleNamespace(proc_pidinfo=self.info,proc_pid_rusage=self.usage,proc_listpids=self.listpids)
 def frame(self):return self.frames[min(self.index,len(self.frames)-1)]
 def rows(self):
  return {pid:g.Row(pid,L if pid not in (L,S) else 1,L if pid!=S else S,502,False) for pid in self.frame()}
 def table(self,deadline):self.index+=1;self.clock+=self.advance;self.calls.append(('table',self.index));return self.rows()
 def hit(self,kind,pid):
  self.count[kind,pid]=self.count.get((kind,pid),0)+1;k=(kind,pid,self.count[kind,pid]);self.calls.append(k);return k
 def info(self,pid,flavor,arg,ptr,size):
  k=self.hit('info',pid)
  if k in self.fail:C.set_errno(self.fail[k][0]);return self.fail[k][1]
  assert pid!=S and pid!=0
  out=C.cast(ptr,C.POINTER(g.BSDInfo)).contents
  out.pid=pid;out.uid=out.ruid=502;out.pgid=L;out.start_sec=10000;out.start_usec=pid-L;out.status=2
  for name,value in self.partial.get(k,{}).items():setattr(out,name,value)
  return size
 def sid(self,pid):
  k=self.hit('sid',pid)
  if k in self.fail:raise OSError(self.fail[k][0],'fake')
  return L
 def usage(self,pid,flavor,ptr):
  k=self.hit('usage',pid)
  if k in self.fail:C.set_errno(self.fail[k][0]);return self.fail[k][1]
  out=C.cast(ptr,C.POINTER(g.RUsageV0)).contents;out.proc_start_abstime=1;out.resident_size,out.phys_footprint=self.memory[pid];return 0
 def listpids(self,flavor,value,buffer,size):
  if flavor==2:self.index+=1;pids=[p for p in self.frame() if p!=S]
  else:
   assert (flavor,value)==(1,0);self.clock+=self.advance
   pids=[0,*self.frame()] if self.global_extra is None else self.global_extra
  self.calls.append(('list',flavor,list(pids)))
  for i,pid in enumerate(pids):buffer[i]=pid
  return len(pids)*C.sizeof(C.c_int)
 def collect(self):return self.p.live_group(leader) if self.native else self.p.group(leader,101.5)

def exercise(name,world,expected,check=None):
 with ExitStack() as f:
  for x in BLOCK:f.enter_context(patch(x,side_effect=forbidden))
  f.enter_context(patch('os.getsid',side_effect=world.sid));f.enter_context(patch('time.monotonic',side_effect=lambda:world.clock))
  try:value=world.collect();outcome='accepted';reason=None
  except g.Refusal as exc:value=None;outcome='refused';reason=str(exc)
  assert outcome==expected,(name,outcome,reason)
  if check:check(world,value,reason)
  return {'name':name,'outcome':outcome,'reason':reason,'value':([value[0],value[1],value[2],sorted(value[3])] if value is not None and not world.native else value),'calls':world.calls,'exit_records':getattr(world.p,'group_exits',[]),'seen':sorted(world.p.seen),'departed':sorted(world.p.departed)}
def require(condition):assert condition
results=[]
results.append(exercise('fresh global absence; new member included',World([[L,A,S],[L,B,S]],fail={('info',A,1):(errno.ESRCH,0)}),'accepted',lambda w,v,r:require(v[:3]==(1000,780,[B]) and w.p.group_exits[0]['resource_observation'] is None)))
results.append(exercise('two bounded retries retain late added member',World([[L,A,S],[L,B,S],[L,B,D,S]],fail={('info',A,1):(errno.ESRCH,0)}),'accepted',lambda w,v,r:require(set(v[2])=={B,D} and v[0]==1500)))
results.append(exercise('native global PID zero is not an owned worker',World([[L,A,S],[L,S]],fail={('info',A,1):(errno.ESRCH,0)},native=True),'accepted',lambda w,v,r:require(v==[] and not any(c[0]=='info' and c[1] in (0,S) for c in w.calls))))
results.append(exercise('native global presence defeats group absence',World([[L,A,S],[L,S]],fail={('info',A,1):(errno.ESRCH,0)},native=True,global_extra=[0,L,A,S]),'refused'))
for code in (errno.EPERM,errno.EIO,0):
 results.append(exercise('non-ESRCH native error '+str(code),World([[L,A,S],[L,S]],fail={('info',A,1):(code,0)}),'refused',lambda w,v,r:require(w.index==0)))
results.append(exercise('short return with ESRCH is not absence',World([[L,A,S],[L,S]],fail={('info',A,1):(errno.ESRCH,135)}),'refused'))
for field,value in [('uid',503),('ruid',503),('pgid',S),('pid',9999),('start_usec',1000000)]:
 results.append(exercise('partial contradiction '+field,World([[L,A,S],[L,S]],fail={('sid',A,1):(errno.ESRCH,None)},partial={('info',A,1):{field:value}}),'refused',lambda w,v,r:require(w.index==0)))
results.append(exercise('leader ESRCH never recovers',World([[L,A,S],[A,S]],fail={('info',L,1):(errno.ESRCH,0)}),'refused',lambda w,v,r:require(w.index==0)))
results.append(exercise('still-present ESRCH refuses',World([[L,A,S]],fail={('usage',A,1):(errno.ESRCH,-1)}),'refused'))
w=World([[L,A,B,S],[L,S]],fail={('info',B,1):(errno.ESRCH,0)});w.memory[A]=(200*g.MIB,180*g.MIB)
results.append(exercise('partial observed cap crossing survives two exits',w,'accepted',lambda w,v,r:require(v[0]>128*g.MIB and v[1]>128*g.MIB and len(w.p.group_exits)==2)))
results.append(exercise('native completion deadline shared with global query',World([[L,A,S],[L,S]],fail={('info',A,1):(errno.ESRCH,0)},native=True,advance=.51),'refused',lambda w,v,r:require('timeout' in r)))
for listing,label in [([0,0,L,S],'duplicate zero'),([0,-1,L,S],'negative PID')]:
 results.append(exercise('unknown global shape '+label,World([[L,A,S],[L,S]],fail={('info',A,1):(errno.ESRCH,0)},native=True,global_extra=listing),'refused'))
w=World([[L,A,S],[L,S]],fail={('info',A,1):(errno.ESRCH,0)})
results.append(exercise('retire first observed worker',w,'accepted'))
w.frames=[[L,A,S]];w.index=-1;before=len(w.calls)
results.append(exercise('job history prevents later PID reappearance',w,'refused',lambda w,v,r:require(not any(c[0]=='info' for c in w.calls[before:]))))
print(json.dumps({'source_sha256':hashlib.sha256((RUN/'tools/host_guard_v3.py').read_bytes()).hexdigest(),'fake_native_only':True,'live_capabilities':'blocked','case_count':len(results),'results':results},indent=2))
