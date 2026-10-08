#!/usr/bin/env python3
"""Apply one mutant to a fresh scratch copy of FK and run filtered lib tests.
usage: mutate.py <id> <rel-file> <old-file> <new-file> <test-filter> [<test-filter> ...]
old/new are files holding the exact text to replace (must occur exactly once).
"""
import os, shutil, subprocess, sys, pathlib, re
WT = pathlib.Path('WT')
SRC = pathlib.Path(os.environ.get('MUT_SRC', str(WT / 'b2-k/projects/chirality-piping/core/solver/frame_kernel')))
DST = WT / 'scratch/i102_b2_k/mut/frame_kernel'
LOG = WT / 'scratch/i102_b2_k/logs'
mid, rel, oldf, newf, filters = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5:]
old, new = pathlib.Path(oldf).read_text(), pathlib.Path(newf).read_text()
if DST.exists(): shutil.rmtree(DST)
DST.mkdir(parents=True)
for part in ('src', 'tests', 'Cargo.toml', 'Cargo.lock'):
    s = SRC / part
    (shutil.copytree if s.is_dir() else shutil.copy2)(s, DST / part)
target = DST / rel
text = target.read_text()
out = LOG / f'mutant_{mid}.log'
SEP = '\n=====MUT=====\n'
for o, nw in zip(old.split(SEP), new.split(SEP)):
    n = text.count(o)
    if n != 1:
        out.write_text(f'MUTANT {mid} NOT_APPLIED occurrences={n}\n'); print(f'MUTANT {mid} NOT_APPLIED occurrences={n}'); sys.exit(2)
    text = text.replace(o, nw)
target.write_text(text)
env = dict(os.environ, TMPDIR=str(WT / 'scratch/i102_b2_k/tmp'), CARGO_TARGET_DIR=str(WT / 'targets/i102-b2-k/mut'))
lines = [f'MUTANT {mid} file={rel}']
failed, passed, compile_error = [], 0, False
for flt in filters:
    p = subprocess.run([str(WT / 'tools/t3_cargo.sh'), 'test', '--locked', '--offline', '--lib', flt],
                       cwd=DST, env=env, capture_output=True, text=True)
    body = p.stdout + p.stderr
    (LOG / f'mutant_{mid}_{re.sub("[^A-Za-z0-9]", "_", flt)}.txt').write_text(body)
    if 'error[E' in body or 'could not compile' in body:
        compile_error = True
    failed += re.findall(r'^test (\S+) \.\.\. FAILED', body, re.M)
    passed += len(re.findall(r'^test (\S+) \.\.\. ok', body, re.M))
    lines.append(f'  filter={flt} rc={p.returncode}')
verdict = 'COMPILE_ERROR' if compile_error else ('KILLED' if failed else 'SURVIVED')
lines.append(f'  verdict={verdict} failed={len(failed)} passed={passed}')
lines += [f'  FAILED {t}' for t in sorted(set(failed))]
out.write_text('\n'.join(lines) + '\n'); print('\n'.join(lines))
