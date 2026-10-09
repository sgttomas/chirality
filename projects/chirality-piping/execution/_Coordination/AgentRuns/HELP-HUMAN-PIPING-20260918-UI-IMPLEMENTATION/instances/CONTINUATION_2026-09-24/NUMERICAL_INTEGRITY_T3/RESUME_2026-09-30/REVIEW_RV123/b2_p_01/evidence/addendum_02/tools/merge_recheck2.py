"""RV123 addendum 02: for each P path the merge took wholesale from one side, check that the other
side did not change it since the fork base 8d46b045e2 (so the clean 3-way would give the same bytes),
or else that the clean 3-way merge equals the merge's bytes."""
import subprocess, sys, os
REPO, TMP = sys.argv[1], sys.argv[2]
OURS, THEIRS, MERGE, BASE = '7cc786285c', 'ec5d397359', '6094636871', '8d46b045e2'
def git(*a, check=True): return subprocess.run(['git', '-C', REPO, *a], capture_output=True, check=check)
def blob(rev, path):
    r = git('cat-file', '-p', f'{rev}:{path}', check=False); return r.stdout if r.returncode == 0 else None
P = 'projects/chirality-piping/'
paths = [p for p in git('diff', '--name-only', '--no-renames', OURS, THEIRS).stdout.decode().split('\n') if p.startswith(P)]
stats = {}
for p in paths:
    m, o, t, b = blob(MERGE, p), blob(OURS, p), blob(THEIRS, p), blob(BASE, p)
    if m == o: side, other = 'ours', t
    elif m == t: side, other = 'theirs', o
    else: continue
    if other == b: why = 'other side unchanged since base'
    elif None not in (o, t):
        fs = []
        for name, data in (('o', o), ('b', b or b''), ('t', t)):
            f = os.path.join(TMP, name); open(f, 'wb').write(data); fs.append(f)
        r = subprocess.run(['git', 'merge-file', '-p', *fs], capture_output=True)
        why = 'clean 3-way equals' if r.returncode == 0 and r.stdout == m else f'CHECK (3-way rc={r.returncode})'
    else:
        why = f'CHECK (absent: merge={m is None} ours={o is None} theirs={t is None} base={b is None})'
    stats.setdefault((side, why), []).append(p)
for (side, why), ps in sorted(stats.items()):
    print(side, '|', why, '|', len(ps))
    if why.startswith('CHECK'):
        for p in ps: print('   ', p)
