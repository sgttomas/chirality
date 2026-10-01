"""One ROOT-selected fast-exit qualification job; never retries or clears a latch."""
from pathlib import Path
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import time


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    here = Path(__file__).resolve().parent
    run = here.parents[2]
    mode, job_id, candidate = sys.argv[1:4]
    assert mode in ('true', 'one', 'tail', 'pair')
    runtime = (Path(tempfile.gettempdir()) / json.loads((run/'RUNTIME_BINDING.json').read_text())['runtime_directory_name']).resolve()
    source = run/'tools/host_guard_v3.py'
    assert sha(source) == 'b32050c72d0bbad0f69526fc98d1f28dcb1fa131115227a2169db8100d66848b'
    guard = load_module('fast_exit_guard', source)
    cleanup = load_module('owned_handle_cleanup', run/'instances/ROOT-GUARD-QUALIFICATION/continuation_01/qualify_case_v3.py')
    assert not (runtime/'guard/ACTIVE.json').exists()
    scratch = runtime/'scratch/guard-v3-qualification'/job_id
    scratch.mkdir(mode=0o700, parents=True, exist_ok=False)
    python = str(Path(sys.executable).resolve())
    fixture = here/'fixture.py'
    command = ['/usr/bin/true'] if mode == 'true' else [python, '-B', str(fixture), mode]
    inputs = {str(source):sha(source), str(fixture):sha(fixture), python:sha(python), command[0]:sha(command[0])}
    env = {'PATH':'/usr/bin:/bin:/usr/sbin:/sbin', 'HOME':os.environ['HOME'], 'LC_ALL':'C', 'PYTHONDONTWRITEBYTECODE':'1'}
    job = {'job_id':job_id, 'run_id':guard.RUN_ID, 'candidate_sha':candidate,
           'input_hashes':inputs, 'kind':'qualification', 'containment':'inherited-group',
           'cwd':str(scratch), 'command':command, 'env':env,
           'limits':{'cap_bytes':128*guard.MIB, 'allowance_bytes':64*guard.MIB,
                     'disk_write_budget_bytes':64*guard.MIB, 'disk_reserve_bytes':guard.GIB,
                     'max_seconds':8}}
    job_path = scratch/'job.json';job_path.write_text(json.dumps(job,indent=2)+'\n')
    result = {'job_id':job_id,'mode':mode,'started':time.monotonic(),'controller_sha256':sha(__file__),
              'job_spec_sha256':sha(job_path),'guard_source_sha256':sha(source),'errors':[]}
    sentinel = monitor = None
    try:
        provider = guard.MacProvider(runtime/'logs')
        sentinel = subprocess.Popen(['/bin/sleep','30'])
        identity,zombie = provider.identity(sentinel.pid);assert not zombie
        result['sentinel_before'] = guard.asdict(identity)
        with (scratch/'stdout.log').open('wb') as out, (scratch/'stderr.log').open('wb') as err:
            monitor = subprocess.Popen([python,'-B',str(source),'run','--runtime-dir',str(runtime),'--job-spec',str(job_path)],env=env,stdout=out,stderr=err)
            result['guard_returncode'] = monitor.wait(timeout=20)
        actual,zombie = provider.identity(sentinel.pid)
        result['sentinel_after'] = guard.asdict(actual)
        result['sentinel_unchanged'] = sentinel.poll() is None and not zombie and actual==identity
        events = [json.loads(line) for line in (runtime/'logs'/job_id/'monitor.jsonl').read_text().splitlines()]
        result['result_events'] = [e for e in events if e['kind'] in ('result','refusal-or-failure','stop-request')]
        result['active_latch_after'] = (runtime/'guard/ACTIVE.json').exists()
        result['healthy'] = (result['guard_returncode']==0 and result['sentinel_unchanged']
                             and not result['active_latch_after'] and any(e['kind']=='result' and e['data']['guard_healthy'] and e['data']['workload_returncode']==0 for e in events))
    except BaseException as exc:
        result['errors'].append(type(exc).__name__+':'+str(exc))
    finally:
        cleanup.cleanup_owned_children(monitor,sentinel,result)
        result['finished'] = time.monotonic()
        (scratch/'RESULT.raw.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    return 0 if result.get('healthy') and not result['errors'] else 2


if __name__=='__main__':
    raise SystemExit(main())
