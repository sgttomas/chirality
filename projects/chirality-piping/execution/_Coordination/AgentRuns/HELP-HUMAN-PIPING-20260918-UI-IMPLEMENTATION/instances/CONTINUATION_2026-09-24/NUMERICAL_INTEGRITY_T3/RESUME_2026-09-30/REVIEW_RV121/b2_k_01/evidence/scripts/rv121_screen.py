"""Screens a records folder for machine data: absolute or home-relative paths, the junit hostname
attribute, the local-domain suffix, and this machine's names (read at run time, never printed). Prints path:line:label."""
import os, re, subprocess, sys, gzip
def sh(*a):
    try: return subprocess.run(a, capture_output=True, text=True).stdout.strip()
    except Exception: return ''
names = {sh('hostname'), sh('scutil', '--get', 'LocalHostName'), sh('scutil', '--get', 'ComputerName')}
GENERIC = {'local', 'home', 'lan', 'domain', 'localdomain', 'pro', 'mac', 'air', 'mini'}
labels = set()
for n in names:
    for x in re.split(r'[^A-Za-z0-9]+', n):
        if len(x) >= 3 and x.lower() not in GENERIC: labels.add(x.lower())
pats = [('abs-users', re.compile('/' + 'Us' + 'ers/')), ('abs-private', re.compile('/' + 'priv' + 'ate/')), ('home', re.compile('~' + '/')),
        ('dot-local', re.compile('\\.' + 'lo' + 'cal\\b', re.I)), ('junit-host', re.compile('host' + 'name=', re.I)),
        ('model-form', re.compile('mac' + 'book', re.I)), ('tmp', re.compile('(^|[^A-Za-z])/t' + 'mp/')),
        ('worktree', re.compile('[.]claude/' + 'worktrees'))]
pats += [('host-name', re.compile(re.escape(l), re.I)) for l in labels]
hits = 0
for dp, dn, fn in os.walk(sys.argv[1]):
    for f in fn:
        p = os.path.join(dp, f)
        if os.path.islink(p): print(f'{p}: SYMLINK'); hits += 1; continue
        data = gzip.open(p).read() if f.endswith('.gz') else open(p, 'rb').read()
        text = data.decode('utf-8', 'replace')
        for i, line in enumerate(text.splitlines(), 1):
            for label, rx in pats:
                if rx.search(line):
                    hits += 1; print(f'{os.path.relpath(p, sys.argv[1])}:{i}: {label}')
    for d in dn:
        if d == 'build': print(f'{dp}/{d}: folder named build'); hits += 1
print(f'screen hits: {hits} (names checked: {len(labels)})')
sys.exit(1 if hits else 0)
