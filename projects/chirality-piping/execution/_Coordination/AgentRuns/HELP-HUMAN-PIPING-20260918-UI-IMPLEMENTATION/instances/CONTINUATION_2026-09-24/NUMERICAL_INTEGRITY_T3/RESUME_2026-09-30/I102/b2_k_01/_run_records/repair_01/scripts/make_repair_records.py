#!/usr/bin/env python3
"""Repair 01 records: copy the repair's evidence into R/I102/b2_k_01/_run_records/repair_01
with machine paths replaced by placeholders (WT, NUM), large logs gzipped (mtime 0); update
SHA256SUMS's line for the corrected _run_records/MUTANTS.md; write SHA256SUMS.repair_01 over
REPAIR_01.md, _run_records/MUTANTS.md and _run_records/repair_01/. No symlink, no folder named build."""
import gzip, hashlib, os, pathlib, re, shutil

WT = str(pathlib.Path(__file__).resolve().parents[2])  # this script lives in WT/scratch/i102_b2_k
S = pathlib.Path(WT) / 'scratch/i102_b2_k'
R = pathlib.Path(WT) / ('numerics/projects/chirality-piping/execution/_Coordination/AgentRuns/'
    'HELP-HUMAN-PIPING-20260918-UI-IMPLEMENTATION/instances/CONTINUATION_2026-09-24/'
    'NUMERICAL_INTEGRITY_T3/RESUME_2026-09-30/I102/b2_k_01')
OUT = R / '_run_records' / 'repair_01'
USERS, PRIVATE, TILDE = '/' + 'Users' + '/', '/' + 'private' + '/', '~' + '/'
SUBS = [(WT + '/numerics', 'NUM'), (WT, 'WT'), (PRIVATE + 'tmp/', '<tmp>/'), (os.path.expanduser('~'), '<home>')]
PATTERN = re.compile('|'.join(re.escape(x) for x in (USERS, PRIVATE, TILDE)))
L = 'logs'
FILES = [  # (source under S, destination under OUT, gzip)
    ('run_r1_mutants.sh', 'scripts/run_r1_mutants.sh', False),
    ('mutate.py', 'scripts/mutate.py', False),
    ('make_repair_records.py', 'scripts/make_repair_records.py', False),
    (f'{L}/r1/mutants_run.log', 'mutants/mutants_run.log', False),
    (f'{L}/r1/gen_write.txt', 'oracle/generator_write.txt', False),
    (f'{L}/r1/gen_verify_head.txt', 'oracle/generator_verify_e22fd799bc.txt', False),
    (f'{L}/r1_b2k.log', 'suites/b2k_e22fd799bc.log', False),
    (f'{L}/r1_fk_full.log', 'suites/fk_full_e22fd799bc.log', True),
    (f'{L}/r1_k09_rows.log', 'suites/k09_rows_e22fd799bc.log', True),
    (f'{L}/r1/compare.txt', 'compare.txt', False),
    (f'{L}/r1/screens.txt', 'screens.txt', False),
]
for mid in ('p2m29', 'm36', 'm18', 'mrk4'):
    FILES += [(f'mut_defs_r1/{mid}.old', f'scripts/mut_defs_r1/{mid}.old', False),
              (f'mut_defs_r1/{mid}.new', f'scripts/mut_defs_r1/{mid}.new', False),
              (f'{L}/mutant_r1_head_{mid}.log', f'mutants/r1_head_{mid}.log', False),
              (f'{L}/mutant_r1_head_{mid}_b2k.txt', f'mutants/r1_head_{mid}_b2k.txt', True)]
FILES += [(f'{L}/mutant_r1_ef51_mrk4.log', 'mutants/r1_ef51_mrk4.log', False),
          (f'{L}/mutant_r1_ef51_mrk4_.txt', 'mutants/r1_ef51_mrk4_whole_lib.txt', True)]


def clean(text):
    for a, b in SUBS:
        text = text.replace(a, b)
    assert not PATTERN.search(text), 'unreplaced machine path'
    return text


def put(src, dst, gz):
    text = clean((S / src).read_text(errors='replace'))
    target = OUT / dst
    target.parent.mkdir(parents=True, exist_ok=True)
    if gz:
        with open(str(target) + '.gz', 'wb') as raw:
            with gzip.GzipFile(fileobj=raw, mode='wb', mtime=0, filename='') as g:
                g.write(text.encode())
    else:
        target.write_text(text)


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir(parents=True)
for src, dst, gz in FILES:
    put(src, dst, gz)
for p in R.rglob('*'):
    assert not p.is_symlink() and p.name != 'build', p
# The original manifest: only MUTANTS.md's line changes.
sums = R / 'SHA256SUMS'
lines = sums.read_text().splitlines()
mut = '_run_records/MUTANTS.md'
hit = [i for i, x in enumerate(lines) if x.endswith('  ' + mut)]
assert len(hit) == 1
lines[hit[0]] = f'{sha(R / mut)}  {mut}'
sums.write_text('\n'.join(lines) + '\n')
# The repair's own manifest.
covered = [R / 'REPAIR_01.md', R / mut] + sorted(x for x in OUT.rglob('*') if x.is_file())
(R / 'SHA256SUMS.repair_01').write_text(''.join(f'{sha(p)}  {p.relative_to(R).as_posix()}\n' for p in covered))
print(f'{len(covered)} files in SHA256SUMS.repair_01; SHA256SUMS {sha(sums)}')
