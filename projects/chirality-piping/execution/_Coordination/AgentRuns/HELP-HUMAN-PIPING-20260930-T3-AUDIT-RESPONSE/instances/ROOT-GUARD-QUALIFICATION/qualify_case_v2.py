"""ROOT-only bounded fixture controller for the independently reviewed plan.

Signals only its own unreaped direct monitor/sentinel child handles. Group
termination belongs exclusively to the reviewed guard. Never clears ACTIVE.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import time


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for part in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(part)
    return h.hexdigest()


def read_events(path):
    if not path.exists():
        return []
    result = []
    for line in path.read_text().splitlines():
        try:
            result.append(json.loads(line))
        except json.JSONDecodeError:
            pass  # a live final line may be incomplete; final raw bytes remain
    return result


def main():
    guard_path, runtime, fixture = (Path(p).resolve() for p in sys.argv[1:4])
    candidate, mode, job_id = sys.argv[4:7]
    assert mode in ('clean', 'alloc16', 'sleepers', 'ignore', 'cap64', 'monitorloss', 'monitorstall', 'escape')
    spec = importlib.util.spec_from_file_location('qualified_guard_candidate', guard_path)
    guard = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = guard
    spec.loader.exec_module(guard)
    provider = guard.MacProvider(runtime / 'logs')
    assert not (runtime / 'guard/ACTIVE.json').exists()
    folder = runtime / 'scratch/guard-qualification' / job_id
    folder.mkdir(mode=0o700, parents=True, exist_ok=False)
    python = str(Path(sys.executable).resolve())
    fixture_mode = 'sleepers' if mode in ('monitorloss','monitorstall') else mode
    job = {
        'job_id': job_id, 'run_id': guard.RUN_ID, 'candidate_sha': candidate,
        'input_hashes': {python: digest(python), str(fixture): digest(fixture)},
        'kind': 'qualification', 'containment': 'inherited-group',
        'cwd': str(folder), 'command': [python, '-B', str(fixture), fixture_mode],
        'env': {'PYTHONDONTWRITEBYTECODE': '1'},
        'limits': {'cap_bytes': (64 if mode == 'cap64' else 128) * guard.MIB,
                   'allowance_bytes': 64 * guard.MIB,
                   'disk_write_budget_bytes': 64 * guard.MIB,
                   'disk_reserve_bytes': guard.GIB, 'max_seconds': 8},
    }
    job_path = folder / 'job.json'
    job_path.write_text(json.dumps(job, indent=2) + '\n')
    log_dir = runtime / 'logs' / job_id
    result = {'job_id': job_id, 'mode': mode, 'guard_sha256': digest(guard_path),
              'controller_sha256': digest(__file__), 'job_sha256': digest(job_path),
              'started': time.monotonic(), 'monitor_killed': False, 'errors': []}
    sentinel = monitor = None
    try:
        sentinel = subprocess.Popen(['/bin/sleep', '45'])
        sentinel_identity, zombie = provider.identity(sentinel.pid)
        assert not zombie
        result['sentinel_before'] = guard.asdict(sentinel_identity)
        with (folder/'monitor.stdout').open('wb') as out, (folder/'monitor.stderr').open('wb') as err:
            monitor = subprocess.Popen([python, '-B', str(guard_path), 'run', '--runtime-dir', str(runtime), '--job-spec', str(job_path)], stdout=out, stderr=err, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'})
            deadline = time.monotonic() + 22
            lock_probe = False
            while monitor.poll() is None and time.monotonic() < deadline:
                events = read_events(log_dir/'monitor.jsonl')
                started = any(e['kind']=='control-received' and e['data'].get('control_kind')=='STARTED' for e in events)
                samples = [e for e in events if e['kind']=='sample']
                if mode == 'clean' and started and not lock_probe:
                    probe = dict(job); probe['job_id'] = job_id+'-lock'
                    probe_path = folder/'lock-probe.json'; probe_path.write_text(json.dumps(probe))
                    p = subprocess.run([python,'-B',str(guard_path),'run','--runtime-dir',str(runtime),'--job-spec',str(probe_path)], capture_output=True, text=True, timeout=4)
                    result['lock_probe'] = {'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
                    lock_probe = True
                if mode in ('monitorloss','monitorstall') and started and samples and len(samples[-1]['data']['members']) >= 3:
                    if mode == 'monitorstall':
                        result['monitor_stopped_at'] = time.monotonic()
                        monitor.send_signal(signal.SIGSTOP)  # owned direct unreaped handle
                        time.sleep(5.5)
                        stalled_members = samples[-1]['data']['members']
                        stalled_table = provider.table(time.monotonic()+1.5)
                        result['post_stall_observation_at'] = time.monotonic()
                        result['post_stall_members'] = [{'pid':member['pid'], 'state':'absent' if member['pid'] not in stalled_table else ('zombie' if stalled_table[member['pid']].zombie else 'live')} for member in stalled_members]
                    result['monitor_kill_at'] = time.monotonic()
                    result['last_complete_sample_before_kill'] = samples[-1]
                    monitor.kill()  # unreaped direct child handle, never log PID
                    result['monitor_killed'] = True
                    break
                time.sleep(.05)
            if monitor.poll() is None and not result['monitor_killed']:
                result['errors'].append('controller-deadline')
                monitor.terminate()  # retained unreaped direct handle only
            result['monitor_returncode'] = monitor.wait(timeout=8)
        if mode in ('monitorloss', 'monitorstall', 'escape'):
            time.sleep(7)  # heartbeat/escalation or bounded escaped self-expiry
        result['sentinel_survived'] = sentinel.poll() is None
        actual, zombie = provider.identity(sentinel.pid)
        result['sentinel_after'] = guard.asdict(actual)
        result['sentinel_unchanged'] = actual == sentinel_identity and not zombie
        events = read_events(log_dir/'monitor.jsonl')
        result['monitor_events'] = events
        result['supervisor_events'] = read_events(log_dir/'supervisor.jsonl')
        known = {}
        registry = log_dir/'registry.json'
        if registry.exists():
            result['registry'] = json.loads(registry.read_text())
            for key in ('monitor','supervisor'):
                entry=result['registry'][key];known[entry['pid']]=entry
        for event in events:
            if event['kind']=='sample':
                for entry in event['data']['members']:
                    known[entry['pid']]=entry
        output = (log_dir/'workload.log').read_text() if (log_dir/'workload.log').exists() else ''
        result['workload_output'] = output
        for pid in re.findall(r'(?:READY|CHILD)\s+(\d+)',output):
            known.setdefault(int(pid),None)
        table=provider.table(time.monotonic()+1.5)
        observations=[]
        for pid, original in sorted(known.items()):
            item={'pid':pid,'original':original}
            if pid not in table:
                item['state']='absent'
            else:
                try:
                    ident,zombie=provider.identity(pid)
                    item.update(state='zombie' if zombie else 'live', current=guard.asdict(ident))
                except Exception as exc:
                    item.update(state='unknown',error=str(exc))
            observations.append(item)
        result['owned_exit_observations']=observations
        result['active_latch_remains']=(runtime/'guard/ACTIVE.json').exists()
        if result['active_latch_remains']:
            probe=dict(job);probe['job_id']=job_id+'-latch'
            probe_path=folder/'latch-probe.json';probe_path.write_text(json.dumps(probe))
            p=subprocess.run([python,'-B',str(guard_path),'run','--runtime-dir',str(runtime),'--job-spec',str(probe_path)],capture_output=True,text=True,timeout=4)
            result['latch_probe']={'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
    except BaseException as exc:
        result['errors'].append(type(exc).__name__+':'+str(exc))
    finally:
        if monitor is not None and monitor.poll() is None:
            monitor.terminate();monitor.wait(timeout=8)
        if sentinel is not None and sentinel.poll() is None:
            sentinel.terminate();sentinel.wait(timeout=3)
        result['finished']=time.monotonic()
        (folder/'controller-result.json').write_text(json.dumps(result,indent=2)+'\n')
    summary={k:result.get(k) for k in ('job_id','mode','monitor_returncode','monitor_killed','sentinel_survived','sentinel_unchanged','owned_exit_observations','active_latch_remains','lock_probe','latch_probe','errors')}
    summary['guard_results']=[e for e in result.get('monitor_events',[]) if e['kind'] in ('result','refusal-or-failure','stop-request')]
    print(json.dumps(summary,indent=2))
    return bool(result['errors'])


if __name__=='__main__':
    raise SystemExit(main())
