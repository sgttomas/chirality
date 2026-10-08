"""RV123 mutants: one exact textual edit of the mutant copy's PP source each, then the filtered PP
--lib tests (registered), then restore. Usage: mutants.py <mutants.json> [ids...]"""
import json, subprocess, sys, pathlib, hashlib
S = pathlib.Path('S')
PP = pathlib.Path('WT/rv123/mut/projects/chirality-piping/core/product_physics')
SRC = PP / 'src'
J = S / 'tools/runjob.sh'
FILTERS = ['b2p_', 'b3b_', 'b1_sp_', 'u3_permitted_path', 'u3g2_', 'u1_constants', 'i51_c0']
SKIP = ['b2p_w_cb1_', 't13_committed_fallback_uz_is_byte_identical']
ms = json.load(open(sys.argv[1]))
want = set(sys.argv[2:])
results = []
for m in ms:
    if want and m['id'] not in want:
        continue
    p = SRC / m['file']
    pristine = p.read_bytes()
    text = pristine.decode()
    n = text.count(m['old'])
    if n != 1:
        results.append({'id': m['id'], 'status': f'bad-edit (count {n})'}); continue
    p.write_text(text.replace(m['old'], m['new']))
    name = 'mut_' + m['id']
    args = ['test', '--locked', '--offline', '--no-fail-fast', '--lib', '--'] + FILTERS + sum([['--skip', s] for s in SKIP], []) + ['--test-threads=2']
    subprocess.run([str(J), name, str(PP), 'rv123-r2-mut', '0'] + args)
    p.write_bytes(pristine)
    assert hashlib.sha256(p.read_bytes()).hexdigest() == hashlib.sha256(pristine).hexdigest()
    log = (S / 'logs' / f'{name}.log').read_text(errors='replace')
    rc = (S / 'logs' / f'{name}.rc').read_text().strip()
    failed = sorted({l.split()[1] for l in log.splitlines() if l.startswith('test ') and l.rstrip().endswith('FAILED')})
    compiled = 'error[E' not in log
    summary = [l for l in log.splitlines() if l.startswith('test result:')]
    status = 'compile-error' if not compiled else ('killed' if failed else ('survived' if rc == '0' else f'rc={rc}'))
    results.append({'id': m['id'], 'what': m['what'], 'status': status, 'rc': rc, 'failed': failed, 'summary': summary})
    print(json.dumps(results[-1]), flush=True)
json.dump(results, open(S / 'logs/mutant_results.json', 'w'), indent=1)
