"""I105 J0a: classify every path of the merge 6094636871 (O = b2's start 7cc786285c, T = main ec5d397359) that
differs between O and T. Result R: equal to O, equal to T, equal to git merge-file's clean 3-way result with the
fork base F = 8d46b045e2 (b2's fork from b1), or equal to that with 601ba408e4 (git's merge base), else HAND.
Usage: merge_check.py <repo> <out json>"""
import json, subprocess, sys, tempfile, os
repo, out = sys.argv[1:3]
O, T, F, B, R = '7cc786285c', 'ec5d397359', '8d46b045e2', '601ba408e4', '6094636871'
g = lambda *a: subprocess.run(['git', '-C', repo, *a], capture_output=True).stdout
def blob(c, p):
    r = subprocess.run(['git', '-C', repo, 'show', f'{c}:{p}'], capture_output=True)
    return r.stdout if r.returncode == 0 else None
def mfile(o, base, t):
    if o is None or t is None:
        return None, None
    with tempfile.TemporaryDirectory() as d:
        fs = []
        for n, b in (('o', o), ('b', base or b''), ('t', t)):
            p = os.path.join(d, n); open(p, 'wb').write(b); fs.append(p)
        r = subprocess.run(['git', 'merge-file', '-p', *fs], capture_output=True)
        return r.stdout, r.returncode
paths = g('diff', '--name-only', O, T).decode().split('\n')
paths = [p for p in paths if p]
res, counts = {}, {}
for p in paths:
    o, t, r = blob(O, p), blob(T, p), blob(R, p)
    if r == o: k = 'ours (b2)'
    elif r == t: k = 'theirs (main)'
    else:
        mf, rc = mfile(o, blob(F, p), t)
        if rc == 0 and r == mf: k = 'clean 3-way, fork base F'
        else:
            mb, rcb = mfile(o, blob(B, p), t)
            k = 'clean 3-way, base 601ba' if rcb == 0 and r == mb else f'HAND (fork-base conflicts: {rc})'
    counts[k] = counts.get(k, 0) + 1
    if not k.startswith('theirs') or p.startswith('projects/chirality-piping/'):
        res[p] = k
json.dump({'paths_differing_O_T': len(paths), 'counts': counts, 'by_path (all but theirs outside P)': res}, open(out, 'w'), indent=1)
print(len(paths), counts)
for p, k in res.items():
    if not k.startswith('theirs'):
        print(k, p)
# Second pass: every path against the fork-base 3-way (deletions on one side count as that side's result).
fb = {}
for p in paths:
    o, t, r, f = blob(O, p), blob(T, p), blob(R, p), blob(F, p)
    if o is None or t is None:
        k = ('R == O' if r == o else 'R == T' if r == t else 'other') + ' (a side lacks the path)'
    else:
        mf, rc = mfile(o, f, t)
        k = 'R == clean fork-base 3-way' if rc == 0 and r == mf else f'fork-base conflicts {rc}, R hand-resolved' if rc else 'R != clean fork-base 3-way'
    fb[k] = fb.setdefault(k, 0) + 1
    if not k.startswith('R == clean'):
        print('FB', k, p)
d = json.load(open(out)); d['against_fork_base_3way'] = fb; json.dump(d, open(out, 'w'), indent=1)
print(fb)
