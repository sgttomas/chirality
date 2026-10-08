"""I103 repair 01: the repairs' mutants, each one exact edit in a scratch archive, run with a test filter
through WT/tools/t3_cargo.sh. Usage: repair_mutants.py <old-head tree> <new-head tree> <out dir>"""
import json, os, pathlib, re, subprocess, sys

WT = pathlib.Path('WT')
OLD, NEW, OUT = (pathlib.Path(a) for a in sys.argv[1:4]); OUT.mkdir(parents=True, exist_ok=True)
PPL = 'projects/chirality-piping/core/product_physics/src/lib.rs'
PPM = 'projects/chirality-piping/core/product_physics/src/retained_memory.rs'
RSR = 'projects/chirality-piping/core/reporting/result_export/src/retained_precision.rs'
# (id, repair, what the mutant does, file, old, new, filter, trees)
MUTANTS = [
    ('R1-SF1-a', 'SF-1', 'the precommit fallback publishes without its notice', PPL,
     '            ordinary.diagnostics.push(notice);\n', '            drop(notice);\n', 'b3a_direct_entry_oracles', ['old', 'new']),
    ('R1-SF1-b', 'SF-1', "RS's G8 admits the L3 contract (m3l's successor passes precommit)", RSR,
     '            && model["pressure_contract"].is_null()\n',
     '            && (model["pressure_contract"].is_null() || model["pressure_contract"]["mode"] == "legacy_pressure_v1")\n',
     'b3a_direct_entry_oracles', ['old', 'new']),
    ('R1-SF2', 'SF-2', "the exact D1.5 clause no longer reads the empty list's capacity", PPM,
     '.filter(|regions| regions.capacity() != 0)', '.filter(|regions| regions.capacity() != 0 && false)',
     'b3b_exact_regions_capacity_is_read', ['new']),
]

def run(tree, tag, mid, filt):
    env = dict(os.environ)
    env.update({'RUSTUP_TOOLCHAIN': '1.97.1', 'RUSTUP_AUTO_INSTALL': '0', 'CARGO_INCREMENTAL': '0', 'CARGO_BUILD_JOBS': '8',
                'RUST_TEST_THREADS': '4', 'CARGO_TARGET_DIR': str(WT / f'targets/i103-b2-a-r1-mut-{tag}'), 'TMPDIR': str(WT / 'scratch/i103_b2_a/tmp')})
    env.pop('RUSTFLAGS', None); env.pop('CARGO_ENCODED_RUSTFLAGS', None)
    pp = tree / 'projects/chirality-piping/core/product_physics'
    args = [str(WT / 'tools/t3_cargo.sh'), 'test', '--locked', '--offline', '--manifest-path', str(pp / 'Cargo.toml'), '--lib', '--', filt]
    log = OUT / f'{mid}_{tag}.log'
    with open(log, 'w') as f:
        rc = subprocess.run(args, cwd=pp, env=env, stdout=f, stderr=subprocess.STDOUT).returncode
    text = log.read_text()
    return rc, re.findall(r'^test (\S+) \.\.\. FAILED$', text, re.M), len(re.findall(r'^test \S+ \.\.\. ok$', text, re.M)), 'error[E' in text

results = []
for mid, repair, what, rel, old, new, filt, trees in MUTANTS:
    for tag in trees:
        src = (OLD if tag == 'old' else NEW) / rel
        original = src.read_text()
        assert original.count(old) == 1, (mid, tag, original.count(old))
        src.write_text(original.replace(old, new))
        try:
            rc, failed, passed, compile_error = run(OLD if tag == 'old' else NEW, tag, mid, filt)
        finally:
            src.write_text(original)
        r = {'id': mid, 'repair': repair, 'mutant': what, 'tree': {'old': 'e96355ef8f', 'new': 'ea5625ad04'}[tag], 'filter': filt, 'rc': rc,
             'killed': rc != 0 and bool(failed) and not compile_error, 'compile_error': compile_error, 'passed': passed,
             'killed_by': [f.split('::')[-1] for f in failed]}
        results.append(r); print(json.dumps(r), flush=True)
(OUT / 'repair_mutants.json').write_text(json.dumps(results, indent=1) + '\n')
