"""List #[test] fn names per file at a git revision (or the working tree with REV='WT'). Usage: test_names.py <repo> <rev|WT>"""
import re, subprocess, sys, os, json
repo, rev = sys.argv[1], sys.argv[2]
env = {**os.environ, 'GIT_OPTIONAL_LOCKS': '0'}
if rev == 'WT':
    files = subprocess.run(['git', '-C', repo, 'ls-files', '-co', '--exclude-standard', '*.rs'], capture_output=True, text=True, env=env).stdout.split()
    read = lambda f: open(os.path.join(repo, f), errors='replace').read() if os.path.exists(os.path.join(repo, f)) else ''
else:
    files = subprocess.run(['git', '-C', repo, 'ls-tree', '-r', '--name-only', rev], capture_output=True, text=True, env=env).stdout.split()
    files = [f for f in files if f.endswith('.rs')]
    read = lambda f: subprocess.run(['git', '-C', repo, 'show', f'{rev}:{f}'], capture_output=True, text=True, env=env, errors='replace').stdout
out = {}
for f in files:
    if '/execution/' in f: continue
    s = read(f)
    names = re.findall(r'#\[test\][^\n]*\n(?:\s*#\[[^\n]*\n)*\s*(?:pub\s+)?(?:async\s+)?fn\s+(\w+)', s)
    if names: out[f] = sorted(names)
json.dump(out, sys.stdout, indent=0, sort_keys=True)
