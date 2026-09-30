"""Execute only the controller's finally AST with fake child handles and storage."""
import ast
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
from subprocess import TimeoutExpired
HERE=Path(__file__).resolve().parent
source=HERE.parents[2]/'instances/ROOT-GUARD-QUALIFICATION/qualify_case_v2.py'
tree=ast.parse(source.read_text());main=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='main')
outer=next(n for n in main.body if isinstance(n,ast.Try) and n.finalbody)
actions=[]
class StoppedMonitor:
 def poll(self): actions.append('monitor.poll');return None
 def terminate(self):actions.append('monitor.terminate(TERM-pending-while-stopped)')
 def wait(self,timeout):actions.append('monitor.wait');raise TimeoutExpired('fake-monitor',timeout)
class Sentinel:
 def poll(self):actions.append('sentinel.poll');return None
 def terminate(self):actions.append('sentinel.terminate')
 def wait(self,timeout):actions.append('sentinel.wait');return 0
class FakeStorage:
 def __truediv__(self,name):return self
 def write_text(self,text):actions.append('controller-result.persisted')
namespace={'monitor':StoppedMonitor(),'sentinel':Sentinel(),'result':{'errors':['simulated provider failure after SIGSTOP']},'folder':FakeStorage(),'time':SimpleNamespace(monotonic=lambda:1),'json':json}
try:
 exec(compile(ast.Module(body=outer.finalbody,type_ignores=[]),str(source),'exec'),namespace)
 error=None
except TimeoutExpired as exc:error=type(exc).__name__
result={'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'executed_lines':[outer.finalbody[0].lineno,outer.finalbody[-1].end_lineno],'fake_objects_only':True,'live_operations':False,'actions':actions,'exception':error,'sentinel_cleanup_attempted':'sentinel.terminate' in actions,'result_persisted':'controller-result.persisted' in actions}
print(json.dumps(result,indent=2));assert error=='TimeoutExpired' and not result['sentinel_cleanup_attempted'] and not result['result_persisted']
