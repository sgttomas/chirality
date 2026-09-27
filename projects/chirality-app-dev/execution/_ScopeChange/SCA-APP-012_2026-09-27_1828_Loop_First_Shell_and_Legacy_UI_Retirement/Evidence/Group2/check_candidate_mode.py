#!/usr/bin/env python3
"""Exercise build_amendment_preview.py --candidate and --finalize in scratch copies.

Run from the repository root. It copies the 12 edited files (never `.git`)
into a temporary root outside every git work tree and checks:

- the candidate is refused, and nothing is written, for this checkout (the
  default root, `--root` naming it, another spelling of it, and a directory
  inside it), for another git checkout without the group-2 pointer, and for a
  root that does not exist;
- another git checkout that holds the group-2 pointer is written, and its
  files match the recorded candidate hashes;
- the scratch copy is written, keeps E26 unapplied and carries DEC-027; a rerun
  is refused on preimage drift;
- the finalize refusals (draft heading, date mismatch, wrong path, rerun) and
  one finalize with a test decision that fills E26 only;
- this checkout is unchanged at the end.

Exit 1 on any FAIL.
"""
import csv, hashlib, os, shutil, subprocess, sys, tempfile
REPO = os.getcwd()
SNAP = 'projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-012_2026-09-27_1828_Loop_First_Shell_and_Legacy_UI_Retirement'
B = os.path.join(REPO, SNAP, 'Evidence/Group2/build_amendment_preview.py')
CSVP = os.path.join(REPO, SNAP, 'Evidence/Group2/PREIMAGE_POSTIMAGE.csv')
POINTER = 'projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-012_GROUP-2_AUTHORIZED.md'
DECOMP = 'projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md'
rows = list(csv.DictReader(open(CSVP)))
base = tempfile.mkdtemp(prefix='sca-app-012-candidate-')


def copy_tree(dst_root):
    for r in rows:
        dst = os.path.join(dst_root, r['File'])
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copy(os.path.join(REPO, r['File']), dst)


def run(*a):
    p = subprocess.run([sys.executable, B, *a], cwd=REPO, capture_output=True, text=True)
    print('$', ' '.join(a), '-> rc', p.returncode)
    print((p.stdout + p.stderr).strip()[-1500:])
    return p.returncode


def shas(root):
    return {r['File']: hashlib.sha256(open(os.path.join(root, r['File']), 'rb').read()).hexdigest() for r in rows}


def in_work_tree(path):
    p = subprocess.run(['git', '-C', path, 'rev-parse', '--is-inside-work-tree'], capture_output=True, text=True)
    return p.returncode == 0 and p.stdout.strip() == 'true'


results = {}
try:
    root = os.path.join(base, 'scratch')
    other = os.path.join(base, 'other-checkout')
    copy_tree(root)
    copy_tree(other)
    subprocess.run(['git', 'init', '-q', other], check=True)
    results['scratch root is outside every git work tree'] = not in_work_tree(root)
    results['other checkout is a git work tree'] = in_work_tree(other)

    before = shas(REPO)
    results['this checkout refused (default root)'] = run('--candidate') == 3
    results['this checkout refused (--root naming it)'] = run('--candidate', '--root', REPO) == 3
    results['this checkout refused (--root REPO/.)'] = run('--candidate', '--root', os.path.join(REPO, '.')) == 3
    results['this checkout refused (--root inside it)'] = run('--candidate', '--root', os.path.join(REPO, 'projects')) == 3
    results['this checkout unchanged'] = shas(REPO) == before

    other_before = shas(other)
    results['other git checkout refused without the pointer'] = run('--candidate', '--root', other) == 3
    results['other git checkout unchanged'] = shas(other) == other_before
    results['missing root refused'] = run('--candidate', '--root', os.path.join(base, 'absent')) == 3

    os.makedirs(os.path.dirname(os.path.join(other, POINTER)), exist_ok=True)
    open(os.path.join(other, POINTER), 'w').write('# SCA-APP-012 group-2 authority pointer (test fixture)\n')
    rec = {r['File']: r['CandidateSHA256'] for r in rows}
    results['other git checkout with the pointer is written'] = (
        run('--candidate', '--root', other) == 0 and shas(other) == rec)

    results['scratch candidate'] = run('--candidate', '--root', root) == 0
    results['scratch candidate matches the recorded hashes'] = shas(root) == rec
    slot = open(os.path.join(root, DECOMP)).read()
    results['candidate keeps E26 unapplied'] = ('{APPLICATION_DATE}' not in slot
                                                and 'amended by SCA-APP-011 |\n| Date | 2026-09-27 |' in slot
                                                and '| DEC-027 | 2026-09-27 |' in slot)
    results['candidate rerun refused (preimage drift)'] = run('--candidate', '--root', root) == 1

    dec_rel = 'projects/chirality-app-dev/execution/_ScopeChange/checkpoint_snapshots/SCA-APP-012_GROUP-3_2099-01-02/DECISION.md'
    dec_abs = os.path.join(root, dec_rel)
    os.makedirs(os.path.dirname(dec_abs), exist_ok=True)
    open(dec_abs, 'w').write('# SCA-APP-012 checkpoint group 3 — draft\n')
    results['finalize refused: heading not accepted'] = run('--finalize', '--date', '2099-01-02', '--group3-decision', dec_rel, '--root', root) == 3
    open(dec_abs, 'w').write('# SCA-APP-012 checkpoint group 3 — accepted (test)\n')
    results['finalize refused: date mismatch'] = run('--finalize', '--date', '2099-01-03', '--group3-decision', dec_rel, '--root', root) == 3
    results['finalize refused: wrong path'] = run('--finalize', '--date', '2099-01-02', '--group3-decision', 'x/DECISION.md', '--root', root) == 3
    results['finalize ok'] = run('--finalize', '--date', '2099-01-02', '--group3-decision', dec_rel, '--root', root) == 0
    slot = open(os.path.join(root, DECOMP)).read()
    results['E26 filled'] = '| Date | 2099-01-02 |' in slot and 'amended by SCA-APP-012 |' in slot
    results['finalize rerun refused'] = run('--finalize', '--date', '2099-01-02', '--group3-decision', dec_rel, '--root', root) == 1
    results['this checkout still unchanged'] = shas(REPO) == before
finally:
    shutil.rmtree(base, ignore_errors=True)

for k, v in results.items():
    print('PASS' if v else 'FAIL', k)
print(f"{sum(results.values())}/{len(results)} PASS")
sys.exit(0 if all(results.values()) else 1)
