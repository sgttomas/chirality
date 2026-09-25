"""git diff --check origin/main...HEAD, whole diff and product-only; summary by file.
usage: diffcheck.py <repo> <table.tsv>"""
import collections, subprocess, sys
repo, table = sys.argv[1], sys.argv[2]
product = [l.split('\t')[0] for l in open(table, encoding='utf-8')]
def run(paths):
    r = subprocess.run(['git', '-C', repo, 'diff', '--check', 'origin/main...HEAD', '--'] + paths,
                       capture_output=True, text=True)
    return r.returncode, r.stdout
rc, out = run(product)
print(f"PRODUCT (31 paths): exit={rc} notices={sum(1 for l in out.splitlines() if not l.startswith('+'))}")
print(out, end='')
rc, out = run([])
per = collections.Counter(l.split(':')[0] for l in out.splitlines() if not l.startswith('+'))
kinds = collections.Counter(l.split(': ', 1)[1] for l in out.splitlines() if not l.startswith('+') and ': ' in l)
print(f"WHOLE DIFF: exit={rc} notices={sum(per.values())}")
for f, n in sorted(per.items()):
    print(f"  {n}\t{f}")
print("kinds:", dict(kinds))
