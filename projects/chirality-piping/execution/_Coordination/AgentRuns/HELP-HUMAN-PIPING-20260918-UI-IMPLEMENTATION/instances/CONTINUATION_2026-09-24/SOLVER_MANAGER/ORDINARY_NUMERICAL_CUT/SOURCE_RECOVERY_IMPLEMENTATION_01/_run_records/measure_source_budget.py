"""Bounded temporary work-reservation measurement; restores candidate source."""
from pathlib import Path
import hashlib
import json
import os
import resource
import subprocess
import sys
import time

out = Path(__file__).resolve().parent
root = next(p for p in out.parents if (p / '.git').exists())
project = root / 'projects/chirality-piping'
attempt, limit = sys.argv[1], int(sys.argv[2])
source = project / 'core/product_physics/src/lib.rs'
before = source.read_bytes()
old = b'const SOURCE_BLOCKS_WORK_LIMIT: usize = 2_000_000;'
assert before.count(old) == 1
trial = before.replace(old, f'const SOURCE_BLOCKS_WORK_LIMIT: usize = {limit};'.encode())
sha = lambda b: hashlib.sha256(b).hexdigest()
record = {'purpose': 'Temporary work-reservation measurement, not candidate qualification',
          'temporary_limit': limit, 'before_source_sha256': sha(before), 'trial_source_sha256': sha(trial)}
source.write_bytes(trial)
try:
    env = dict(os.environ, CARGO_TARGET_DIR='/private/tmp/piping-source-recovery-product-target',
               CARGO_BUILD_JOBS='2', OPS_SOURCE_BLOCK_BUDGET_OBSERVATION='1')
    command = ['cargo', 'test', '--offline', '--locked', '-j2', '--manifest-path',
               'core/product_physics/Cargo.toml', '--test', 'source_block_recovery', '--no-run', '--message-format=json']
    built = subprocess.run(command, cwd=project, env=env, capture_output=True)
    (out / f'budget_probe_{attempt}_build.stderr').write_bytes(built.stderr)
    (out / f'budget_probe_{attempt}_build.jsonl').write_bytes(built.stdout)
    record['build_exit_code'] = built.returncode
    if built.returncode == 0:
        items = [json.loads(line) for line in built.stdout.decode().splitlines() if line.startswith('{')]
        executable = next(x['executable'] for x in items if x.get('reason') == 'compiler-artifact'
                          and x.get('target', {}).get('name') == 'source_block_recovery' and x.get('executable'))
        record['executable_sha256'] = sha(Path(executable).read_bytes())
        start = time.perf_counter()
        # resource.getrusage in a separate supervisor excludes compilation RSS.
        supervisor = '''import os,resource,subprocess,sys,time,json
start=time.perf_counter()
p=subprocess.run([sys.argv[1],"--nocapture","--test-threads=1"],env=os.environ)
r=resource.getrusage(resource.RUSAGE_CHILDREN)
print("RUNTIME_RESOURCE "+json.dumps({"exit_code":p.returncode,"wall_seconds":time.perf_counter()-start,"user_seconds":r.ru_utime,"system_seconds":r.ru_stime,"max_rss_host_units":r.ru_maxrss}),flush=True)
sys.exit(p.returncode)
'''
        with (out / f'budget_probe_{attempt}_runtime.log').open('w') as log:
            run = subprocess.run([sys.executable, '-c', supervisor, executable], cwd=project, env=env, stdout=log, stderr=subprocess.STDOUT)
        raw = (out / f'budget_probe_{attempt}_runtime.log').read_text()
        record.update(runtime_exit_code=run.returncode, supervisor_wall_seconds=time.perf_counter()-start,
                      runtime_log_sha256=sha(raw.encode()))
        for line in raw.splitlines():
            if 'SOURCE_BLOCK_BUDGET_OBSERVATION ' in line or line.startswith('RUNTIME_RESOURCE ') or 'test result:' in line:
                print(line)
        if run.returncode:
            print(raw[-2200:])
    else:
        for line in built.stdout.decode().splitlines():
            item = json.loads(line)
            if item.get('reason') == 'compiler-message':
                print(item['message']['rendered'])
finally:
    assert source.read_bytes() == trial, 'source changed concurrently; do not overwrite'
    source.write_bytes(before)
    record['source_restored'] = sha(source.read_bytes()) == record['before_source_sha256']
    (out / f'budget_probe_{attempt}.json').write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps(record))
