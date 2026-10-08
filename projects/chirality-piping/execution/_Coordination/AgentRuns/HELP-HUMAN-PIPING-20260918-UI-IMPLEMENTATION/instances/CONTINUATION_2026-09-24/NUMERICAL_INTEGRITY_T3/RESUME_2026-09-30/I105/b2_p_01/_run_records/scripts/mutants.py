"""I105 (lane P): one mutant per new check, on a scratch archive of the candidate commit.

Usage: mutants.py <mutants.json> <archive root (holds projects/chirality-piping)> <out dir> [ids...]
Each mutant is one or more exact edits {file, old, new} (each `old` must occur exactly once). For each:
apply, run PP `--lib` tests matching the filters through WT/tools/t3_cargo.sh (one job at a time),
restore the file bytes and check the restore by sha256. Killed = some test failed (named) after a
successful compile; survived = all ran and passed; compile = the build failed (not a kill).
"""
import hashlib, json, os, pathlib, re, subprocess, sys, time

WT = pathlib.Path('WT')
S = WT / 'scratch/i105_b2_p'
spec = json.loads(pathlib.Path(sys.argv[1]).read_text())
root = pathlib.Path(sys.argv[2]) / 'projects/chirality-piping/core/product_physics'
out = pathlib.Path(sys.argv[3]); out.mkdir(parents=True, exist_ok=True)
only = set(sys.argv[4:])
env = dict(os.environ, TMPDIR=str(S / 'tmp'), RUSTUP_TOOLCHAIN='1.97.1', RUSTUP_AUTO_INSTALL='0', CARGO_INCREMENTAL='1',
           CARGO_BUILD_JOBS='8', RUST_TEST_THREADS='4', CARGO_TARGET_DIR=str(WT / 'targets/i105-b2-p-mut'))
env.pop('RUSTFLAGS', None); env.pop('CARGO_ENCODED_RUSTFLAGS', None)
results = []
for m in spec['mutants']:
    if only and m['id'] not in only:
        continue
    saved = {}
    for e in m['edits']:
        f = root / e['file']
        text = saved.setdefault(e['file'], f.read_bytes()).decode()
        cur = f.read_text()
        assert cur.count(e['old']) == 1, (m['id'], e['file'], cur.count(e['old']))
        f.write_text(cur.replace(e['old'], e['new']))
    cmd = [str(WT / 'tools/t3_cargo.sh'), 'test', '--locked', '--offline', '--lib', '--no-fail-fast', '--'] + m.get('filters', spec['filters']) + \
          [x for s in spec.get('skip', []) for x in ('--skip', s)]
    t0 = time.time()
    p = subprocess.run(cmd, cwd=root, env=env, capture_output=True, text=True)
    log = p.stdout + p.stderr
    for name, data in saved.items():
        (root / name).write_bytes(data)
        assert hashlib.sha256((root / name).read_bytes()).hexdigest() == hashlib.sha256(data).hexdigest()
    failed = sorted(set(re.findall(r'^test (\S+) \.\.\. FAILED', log, re.M)))
    passed = len(re.findall(r'^test \S+ \.\.\. ok', log, re.M))
    compiled = 'error[E' not in log and 'could not compile' not in log
    verdict = 'compile' if not compiled else ('killed' if failed else ('survived' if passed else 'no-tests'))
    (out / f"{m['id']}.log").write_text('\n'.join(l for l in log.splitlines() if l.startswith(('test ', 'test result', 'error', 'thread ', '  left', ' right', 'assertion'))))
    r = {'id': m['id'], 'check': m['check'], 'verdict': verdict, 'failed': failed, 'passed': passed, 'seconds': round(time.time() - t0)}
    results.append(r)
    print(json.dumps(r), flush=True)
(out / 'results.json').write_text(json.dumps(results, indent=1))
