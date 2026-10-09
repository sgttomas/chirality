"""I105: test-by-test comparison of two suite runs (run_suites.sh logs).
Usage: compare.py <base run dir> <candidate run dir> <out json>
Per suite: counts per outcome on each side, and every test whose outcome differs or that exists on one side only."""
import json, pathlib, re, sys


def cargo(text):
    out, binary = {}, '?'
    for line in text.splitlines():
        m = re.match(r'\s*Running (?:unittests )?(\S+)', line)
        if m:
            binary = re.sub(r'-[0-9a-f]{16}\)?$', '', m.group(1).split('/')[-1].rstrip(')'))
            continue
        m = re.match(r'\s*Doc-tests (\S+)', line)
        if m:
            binary = 'doc:' + m.group(1)
            continue
        m = re.match(r'^test (.+?) \.\.\. (ok|FAILED|ignored)(?:, .*)?$', line)
        if m:
            out[f'{binary}::{m.group(1)}'] = m.group(2)
    return out


base, cand = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
report = {}
for log in sorted(cand.glob('*.log')):
    b = base / log.name
    if not b.exists():
        continue
    x, y = cargo(b.read_text(errors='replace')), cargo(log.read_text(errors='replace'))
    count = lambda d: {k: sum(1 for v in d.values() if v == k) for k in ('ok', 'FAILED', 'ignored')}
    report[log.stem] = {
        'base': count(x), 'candidate': count(y),
        'changed': {k: [x[k], y[k]] for k in sorted(x.keys() & y.keys()) if x[k] != y[k]},
        'added': {k: y[k] for k in sorted(y.keys() - x.keys())},
        'removed': {k: x[k] for k in sorted(x.keys() - y.keys())},
    }
pathlib.Path(sys.argv[3]).write_text(json.dumps(report, indent=1))
for suite, r in report.items():
    print(suite, 'base', r['base'], 'candidate', r['candidate'], 'changed', len(r['changed']), 'added', len(r['added']), 'removed', len(r['removed']))
    for k, v in r['changed'].items():
        print('  changed', k, v)
