"""I103: test-by-test comparison of two suite runs (run_suites.sh logs).
Usage: compare.py <base run dir> <candidate run dir> <out json>
Prints, per suite, the counts and every test whose outcome differs or that exists on one side only."""
import json, pathlib, re, sys

def cargo(text):
    out, binary = {}, '?'
    for line in text.splitlines():
        m = re.match(r'\s*Running (?:unittests )?(\S+)', line)
        if m:
            binary = m.group(1)
            continue
        m = re.match(r'\s*Doc-tests (\S+)', line)
        if m:
            binary = 'doc:' + m.group(1)
            continue
        m = re.match(r'^test (.+?) \.\.\. (ok|FAILED|ignored)(?:, .*)?$', line)
        if m:
            out[f'{binary}::{m.group(1)}'] = m.group(2)
    return out

def pytest(text):
    out = {}
    for line in text.splitlines():
        m = re.match(r'^(tests/\S+::.+?) (PASSED|FAILED|SKIPPED|ERROR|XFAIL|XPASS)\b', line)
        if m:
            out[m.group(1)] = m.group(2)
    return out

def vitest(text):
    out = {}
    for line in text.splitlines():
        m = re.match(r'^\s*([✓×↓])\s+(src/\S+)\s+>\s+(.+?)(?:\s+\d+ms)?$', line)
        if m:
            status = {'✓': 'passed', '×': 'failed', '↓': 'skipped'}[m.group(1)]
            out[f'{m.group(2)} > {m.group(3)}'] = status
    return out

PARSERS = {'re': cargo, 'pp': cargo, 'runner': cargo, 'py': pytest, 'ts': vitest}
base, cand = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
report = {}
for suite, parse in PARSERS.items():
    b = parse((base / f'{suite}.log').read_text()) if (base / f'{suite}.log').exists() else {}
    c = parse((cand / f'{suite}.log').read_text()) if (cand / f'{suite}.log').exists() else {}
    count = lambda d: {k: sum(1 for v in d.values() if v == k) for k in sorted(set(d.values()))}
    changed = {k: [b[k], c[k]] for k in sorted(set(b) & set(c)) if b[k] != c[k]}
    report[suite] = {'base': count(b), 'candidate': count(c), 'changed': changed,
                     'only_base': {k: b[k] for k in sorted(set(b) - set(c))},
                     'only_candidate': {k: c[k] for k in sorted(set(c) - set(b))}}
    r = report[suite]
    print(f"{suite}: base {r['base']} candidate {r['candidate']} changed {len(changed)} only-base {len(r['only_base'])} only-candidate {len(r['only_candidate'])}")
    for k, v in changed.items():
        print(f'  changed {k}: {v[0]} -> {v[1]}')
    for k, v in r['only_base'].items():
        print(f'  only base {k}: {v}')
    for k, v in r['only_candidate'].items():
        print(f'  only candidate {k}: {v}')
pathlib.Path(sys.argv[3]).write_text(json.dumps(report, indent=1, ensure_ascii=False) + '\n')
