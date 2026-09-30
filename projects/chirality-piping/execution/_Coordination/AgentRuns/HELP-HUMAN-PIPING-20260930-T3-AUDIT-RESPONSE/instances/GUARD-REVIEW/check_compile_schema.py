"""Pure regression witnesses: fake files and the supplied live-capability fence."""
from contextlib import ExitStack
import importlib.util
import io
import json
from pathlib import Path
import sys
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'GUARD-IMPLEMENTATION' / 'test_host_guard.py'
spec = importlib.util.spec_from_file_location('review_supplied_fakes', SOURCE)
tests = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = tests
spec.loader.exec_module(tests)
guard = tests.guard
binary = b'fake rustup proxy bytes'
base = {
    'job_id': 'fake-schema-review', 'run_id': guard.RUN_ID,
    'candidate_sha': 'a'*40, 'kind': 'compile', 'containment': 'inherited-group',
    'cwd': '/fake/workspace', 'command': [],
    'env': {'RUSTUP_TOOLCHAIN': '1.97.1', 'RUSTUP_AUTO_INSTALL': '0',
            'CARGO_INCREMENTAL': '0', 'CARGO_BUILD_JOBS': '1', 'RUST_TEST_THREADS': '1'},
    'input_hashes': {'/fake/cargo': guard.hashlib.sha256(binary).hexdigest(),
                     '/fake/rustc': guard.hashlib.sha256(binary).hexdigest()},
    'limits': {'cap_bytes':128*guard.MIB, 'allowance_bytes':64*guard.MIB,
               'disk_write_budget_bytes':64*guard.MIB, 'disk_reserve_bytes':guard.GIB,
               'max_seconds':8}}
cases = {
    'proper_cargo_build': ['/fake/cargo','build','--offline','--locked','-j','1'],
    'cargo_flags_in_workload_args': ['/fake/cargo','run','--jobs','8','--','--offline','--locked','-j','1'],
    'cargo_explicit_toolchain': ['/fake/cargo','+stable','build','--offline','--locked','-j','1'],
    'rustc_explicit_toolchain': ['/fake/rustc','+stable','input.rs'],
}
results=[]
with ExitStack() as fence:
    for target in tests.FORBIDDEN:
        fence.enter_context(patch(target,side_effect=tests.blocked))
    fence.enter_context(patch.object(Path,'is_dir',return_value=True))
    for name,argv in cases.items():
        job={**base,'command':argv}
        raw=json.dumps(job).encode()
        def fake_open(path,mode):
            assert mode=='rb'
            return io.BytesIO(raw if str(path)=='/fake/job.json' else binary)
        with patch('builtins.open',side_effect=fake_open):
            try:
                actual,_=guard.read_job(Path('/fake/job.json'))
                results.append({'case':name,'argv':argv,'accepted':True,'env':actual['env']})
            except Exception as exc:
                results.append({'case':name,'argv':argv,'accepted':False,'error':repr(exc)})
print(json.dumps({'live_capabilities':'blocked','fake_files_only':True,'cases':results},indent=2))
assert all(r['accepted'] for r in results), 'Sealed candidate acceptance changed; inspect before updating review.'
