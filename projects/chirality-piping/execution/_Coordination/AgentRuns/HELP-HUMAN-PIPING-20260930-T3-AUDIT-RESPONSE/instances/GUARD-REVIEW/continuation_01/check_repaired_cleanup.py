"""Same finalizer-path witness against v3, including injected wait failure."""
import ast,hashlib,json
from pathlib import Path
from types import SimpleNamespace
from subprocess import TimeoutExpired
HERE=Path(__file__).resolve().parent;source=HERE.parents[2]/'instances/ROOT-GUARD-QUALIFICATION/continuation_01/qualify_case_v3.py';tree=ast.parse(source.read_text());main=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main');outer=next(n for n in main.body if isinstance(n,ast.Try) and n.finalbody);helper=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='cleanup_owned_children');cases=[]
for inject_error in (False,True):
 actions=[]
 class Monitor:
  alive=True
  def poll(self):actions.append('monitor.poll');return None if self.alive else -9
  def kill(self):actions.append('monitor.kill');self.alive=False
  def terminate(self):actions.append('monitor.terminate(TERM-pending-while-stopped)')
  def wait(self,timeout):
   actions.append('monitor.wait')
   if inject_error or self.alive:raise TimeoutExpired('fake-monitor',timeout)
   return -9
 class Sentinel:
  alive=True
  def poll(self):actions.append('sentinel.poll');return None if self.alive else 0
  def terminate(self):actions.append('sentinel.terminate');self.alive=False
  def kill(self):actions.append('sentinel.kill');self.alive=False
  def wait(self,timeout):actions.append('sentinel.wait');return 0
 class Storage:
  def __truediv__(self,name):return self
  def write_text(self,text):actions.append('controller-result.persisted')
 state={'errors':['simulated provider failure after SIGSTOP']}
 ns={'monitor':Monitor(),'sentinel':Sentinel(),'result':state,'folder':Storage(),'time':SimpleNamespace(monotonic=lambda:1),'json':json}
 exec(compile(ast.Module(body=[helper],type_ignores=[]),str(source),'exec'),ns)
 exec(compile(ast.Module(body=outer.finalbody,type_ignores=[]),str(source),'exec'),ns)
 cases.append({'persistent_wait_error':inject_error,'actions':actions,'errors':state['errors'],'sentinel_cleanup_attempted':'sentinel.terminate' in actions,'result_persisted':'controller-result.persisted' in actions})
print(json.dumps({'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'fake_objects_only':True,'live_operations':False,'cases':cases},indent=2))
assert all(x['sentinel_cleanup_attempted'] and x['result_persisted'] for x in cases)
assert any('unconfirmed' in e for e in cases[1]['errors'])
