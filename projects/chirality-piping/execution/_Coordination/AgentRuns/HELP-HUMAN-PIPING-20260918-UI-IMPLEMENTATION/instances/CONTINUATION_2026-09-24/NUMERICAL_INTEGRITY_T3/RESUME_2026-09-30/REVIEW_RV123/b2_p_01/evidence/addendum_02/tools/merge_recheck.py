"""RV123 addendum 02: independent re-check of the J0a merge (6094636871 = 7cc786285c + ec5d397359).
For every path that differs between the parents: outside P, the merge must equal main; inside P,
classify the merge's bytes as ours / theirs / the clean 3-way merge on base 8d46b045e2 (git merge-file)
/ other (hand-resolved), and list the conflicted 3-way paths."""
import subprocess, sys, os, json, tempfile
REPO, TMP = sys.argv[1], sys.argv[2]
OURS, THEIRS, MERGE, BASE = '7cc786285c', 'ec5d397359', '6094636871', '8d46b045e2'
def git(*a, check=True):
    return subprocess.run(['git', '-C', REPO, *a], capture_output=True, check=check)
def blob(rev, path):
    r = git('cat-file', '-p', f'{rev}:{path}', check=False)
    return r.stdout if r.returncode == 0 else None
paths = git('diff', '--name-only', '--no-renames', OURS, THEIRS).stdout.decode().split('\n')
paths = [p for p in paths if p]
P = 'projects/chirality-piping/'
out = {'outside_P': {'total': 0, 'merge_eq_main': 0, 'other': []}, 'inside_P': {}}
classes = {}
for p in paths:
    m, o, t = blob(MERGE, p), blob(OURS, p), blob(THEIRS, p)
    if not p.startswith(P):
        out['outside_P']['total'] += 1
        if m == t: out['outside_P']['merge_eq_main'] += 1
        else: out['outside_P']['other'].append(p)
        continue
    if m == o and m == t: c = 'both'
    elif m == o: c = 'ours'
    elif m == t: c = 'theirs'
    else:
        b = blob(BASE, p)
        if None in (o, t):
            c = 'other(one side absent)'
        else:
            fs = []
            for name, data in (('o', o), ('b', b if b is not None else b''), ('t', t)):
                f = os.path.join(TMP, name); open(f, 'wb').write(data); fs.append(f)
            r = subprocess.run(['git', 'merge-file', '-p', fs[0], fs[1], fs[2]], capture_output=True)
            clean = r.returncode == 0
            if clean and r.stdout == m: c = 'clean_3way'
            elif not clean: c = f'hand(conflicts={r.returncode})'
            else: c = 'other(clean 3way differs)'
    classes.setdefault(c, []).append(p)
out['inside_P'] = {k: (len(v), v if not k.startswith(('ours', 'theirs', 'both')) else None) for k, v in sorted(classes.items())}
print(json.dumps(out, indent=1))
