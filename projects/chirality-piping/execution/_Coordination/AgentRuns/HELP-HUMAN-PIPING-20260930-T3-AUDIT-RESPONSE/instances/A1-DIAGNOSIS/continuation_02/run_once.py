"""One guard invocation only. No retry, repair, latch cleanup or numerical case."""
from pathlib import Path
import hashlib,json,os,subprocess,sys,tempfile,time

here=Path(__file__).resolve().parent
root=Path(subprocess.check_output(['git','rev-parse','--show-toplevel'],text=True).strip()).resolve()
run=here.parents[2]
binding=json.loads((run/'RUNTIME_BINDING.json').read_text())
local=json.loads((here/'RAW_BINDING.json').read_text())
runtime=(Path(tempfile.gettempdir())/binding['runtime_directory_name']).resolve()
raw=runtime/local['scratch_relative_path']; spec=raw/'job.json'
assert hashlib.sha256(spec.read_bytes()).hexdigest()==local['raw_spec_sha256']
job=json.loads(spec.read_text()); guard=run/'tools/host_guard_v2.py'
assert hashlib.sha256(guard.read_bytes()).hexdigest()=='533a6f7506da4e031d8a824a27b4e9c496f374a3af8b7e98c72da55e8bbc26b5'
# Exclusive marker prevents even accidental repeated invocation of this script.
with open(raw/'INVOCATION_STARTED.json','x') as f:
    json.dump(dict(wall_ns=time.time_ns(),pid=os.getpid(),guard_sha256=hashlib.sha256(guard.read_bytes()).hexdigest()),f)
command=[sys.executable,str(guard),'run','--runtime-dir',str(runtime),'--job-spec',str(spec)]
started=time.monotonic(); wall=time.time_ns()
with open(raw/'guard.stdout','xb') as stdout,open(raw/'guard.stderr','xb') as stderr:
    process=subprocess.Popen(command,env=job['env'],cwd=root,stdout=stdout,stderr=stderr)
    code=process.wait()
result=dict(guard_returncode=code,elapsed_seconds=time.monotonic()-started,wall_start_ns=wall,
            wall_end_ns=time.time_ns(),command=command,job_spec_sha256=local['raw_spec_sha256'],
            active_latch_after=(runtime/'guard/ACTIVE.json').exists(),retry=False,model_run=False)
(raw/'CONTROLLER_RESULT.raw.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
sys.exit(code)
