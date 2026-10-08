"""Parse cargo test logs into {target: {test: outcome}} and diff runs. Usage: parse_outcomes.py out.json label=log [label=log ...]"""
import json, re, sys
out = {}
for arg in sys.argv[2:]:
    label, path = arg.split('=', 1)
    res = {}; target = None
    for line in open(path, errors='replace'):
        m = re.match(r'\s*Running (unittests )?(\S+)', line)
        if m: target = m.group(2); continue
        m = re.match(r'test (\S+) \.\.\. (ok|FAILED|ignored)', line)
        if m and target: res[f'{target}::{m.group(1)}'] = m.group(2)
    out[label] = res
    c = {}
    for v in res.values(): c[v] = c.get(v, 0) + 1
    print(label, len(res), c)
labels = list(out)
base = out[labels[0]]
for l in labels[1:]:
    changed = {k: (base.get(k), out[l].get(k)) for k in set(base) | set(out[l]) if base.get(k) != out[l].get(k)}
    print(f'{labels[0]} -> {l}: {len(changed)} changed')
    for k, v in sorted(changed.items()): print('  ', v, k)
json.dump(out, open(sys.argv[1], 'w'), indent=1, sort_keys=True)
