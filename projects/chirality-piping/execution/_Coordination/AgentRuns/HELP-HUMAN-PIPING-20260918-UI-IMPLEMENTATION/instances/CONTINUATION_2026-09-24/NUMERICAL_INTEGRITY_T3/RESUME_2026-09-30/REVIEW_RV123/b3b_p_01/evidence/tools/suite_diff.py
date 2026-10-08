"""RV123: test-by-test comparison of two cargo test logs (per test binary)."""
import re, sys
def parse(path):
    out, binary = {}, None
    for line in open(path, errors='replace'):
        m = re.match(r'\s*Running (?:unittests )?(\S+)', line)
        if m: binary = m.group(1); continue
        m = re.match(r'test (\S+) \.\.\. (ok|FAILED|ignored)', line)
        if m: out[(binary, m.group(1))] = m.group(2)
    return out
a, b = parse(sys.argv[1]), parse(sys.argv[2])
def counts(d):
    from collections import Counter
    return dict(Counter(d.values()))
print('base', len(a), counts(a)); print('cand', len(b), counts(b))
for k in sorted(set(a) | set(b), key=str):
    x, y = a.get(k), b.get(k)
    if x != y:
        print(f'{x or "-":8} -> {y or "-":8} {k[0]} {k[1]}')
