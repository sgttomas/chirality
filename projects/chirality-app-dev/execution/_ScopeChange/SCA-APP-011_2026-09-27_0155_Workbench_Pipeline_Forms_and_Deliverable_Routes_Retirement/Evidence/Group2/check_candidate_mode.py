#!/usr/bin/env python3
"""Exercise build_amendment_preview.py --candidate and --finalize in a scratch copy.

Run from the repository root. It copies the 16 edited files into a temporary
root, checks that the repository-tree candidate is refused without the group-2
pointer, writes the candidate in the scratch root, checks the finalize refusals
(draft heading, date mismatch, wrong path, rerun) and one finalize with a
test decision, and confirms the repository tree is unchanged. Exit 1 on any FAIL.
"""
import csv, hashlib, os, shutil, subprocess, sys, tempfile
REPO = os.getcwd()
SNAP = 'projects/chirality-app-dev/execution/_ScopeChange/SCA-APP-011_2026-09-27_0155_Workbench_Pipeline_Forms_and_Deliverable_Routes_Retirement'
B = os.path.join(REPO, SNAP, 'Evidence/Group2/build_amendment_preview.py')
CSVP = os.path.join(REPO, SNAP, 'Evidence/Group2/PREIMAGE_POSTIMAGE.csv')
root = tempfile.mkdtemp(prefix='sca-app-011-candidate-')
shutil.rmtree(root, ignore_errors=True)
rows = list(csv.DictReader(open(CSVP)))
for r in rows:
    dst = os.path.join(root, r['File'])
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy(os.path.join(REPO, r['File']), dst)


def run(*a):
    p = subprocess.run([sys.executable, B, *a], cwd=REPO, capture_output=True, text=True)
    print('$', ' '.join(a), '-> rc', p.returncode)
    print((p.stdout + p.stderr).strip()[-1500:])
    return p.returncode


def tree_sha():
    return {r['File']: hashlib.sha256(open(os.path.join(REPO, r['File']), 'rb').read()).hexdigest() for r in rows}


before = tree_sha()
results = {}
results['repo candidate refused (no group-2 pointer)'] = run('--candidate') == 3
results['repo tree unchanged'] = tree_sha() == before
results['scratch candidate'] = run('--candidate', '--root', root) == 0
slot = open(os.path.join(root, 'projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md')).read()
results['candidate keeps E47 unapplied'] = '{APPLICATION_DATE}' not in slot and 'amended by SCA-APP-010 |\n| Date | 2026-09-04 |' in slot
results['candidate rerun refused (preimage drift)'] = run('--candidate', '--root', root) == 1
dec_dir = os.path.join(root, 'projects/chirality-app-dev/execution/_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-3_2099-01-02')
os.makedirs(dec_dir, exist_ok=True)
decp = 'projects/chirality-app-dev/execution/_ScopeChange/checkpoint_snapshots/SCA-APP-011_GROUP-3_2099-01-02/DECISION.md'
open(os.path.join(dec_dir, 'DECISION.md'), 'w').write('# SCA-APP-011 checkpoint group 3 — draft\n')
results['finalize refused: heading not accepted'] = run('--finalize', '--date', '2099-01-02', '--group3-decision', decp, '--root', root) == 3
open(os.path.join(dec_dir, 'DECISION.md'), 'w').write('# SCA-APP-011 checkpoint group 3 — accepted (test)\n')
results['finalize refused: date mismatch'] = run('--finalize', '--date', '2099-01-03', '--group3-decision', decp, '--root', root) == 3
results['finalize refused: wrong path'] = run('--finalize', '--date', '2099-01-02', '--group3-decision', 'x/DECISION.md', '--root', root) == 3
results['finalize ok'] = run('--finalize', '--date', '2099-01-02', '--group3-decision', decp, '--root', root) == 0
slot = open(os.path.join(root, 'projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md')).read()
results['E47 filled'] = '| Date | 2099-01-02 |' in slot and 'amended by SCA-APP-011 |' in slot
results['finalize rerun refused'] = run('--finalize', '--date', '2099-01-02', '--group3-decision', decp, '--root', root) == 1
results['repo tree still unchanged'] = tree_sha() == before
for k, v in results.items():
    print('PASS' if v else 'FAIL', k)
shutil.rmtree(root)
sys.exit(0 if all(results.values()) else 1)
