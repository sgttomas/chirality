"""I110 round 2: per-test outcome diffs (base vs candidate) and byte equality. Usage: compare_evidence.py <ev dir> <out.json>"""
import json, os, re, sys, collections
ev, out = sys.argv[1], sys.argv[2]

def cargo_outcomes(path, prefix):
    res = {}; target = None
    for line in open(path, errors='replace'):
        m = re.match(r'\s*Running (unittests )?(\S+)', line)
        if m: target = m.group(2); continue
        m = re.match(r'\s*Doc-tests (\S+)', line)
        if m: target = 'doctests:' + m.group(1); continue
        m = re.match(r'test (.+?) \.\.\. (ok|FAILED|ignored)', line)
        if m and target: res[f'{prefix}|{target}|{m.group(1)}'] = m.group(2)
    return res

def suites(d):
    res = {}
    for f in sorted(os.listdir(d)):
        if f.endswith('.log'):
            res.update(cargo_outcomes(os.path.join(d, f), f[4:-4]))
    return res

def pytest(path):
    res = {}
    for line in open(path, errors='replace'):
        m = re.match(r'(PASSED|FAILED|SKIPPED|XFAIL|XPASS|ERROR) (\[\d+\] )?(\S+)', line)
        if m: res[m.group(3)] = m.group(1)
    return res

def vitest(path, root):
    res = {}
    d = json.load(open(path))
    for f in d['testResults']:
        name = f['name']
        i = name.find('apps/desktop/')
        rel = name[i:] if i >= 0 else name
        for a in f['assertionResults']:
            res[f"{rel}|{a['fullName']}"] = a['status']
    return res

def diff(base, cand):
    keys = sorted(set(base) | set(cand))
    changed = [(k, base.get(k), cand.get(k)) for k in keys if base.get(k) != cand.get(k)]
    return dict(base=dict(collections.Counter(base.values())), cand=dict(collections.Counter(cand.values())),
                changed=[dict(test=k, base=b, cand=c) for k, b, c in changed])

report = {}
pairs = {
    'manifests_40': lambda: (suites(f'{ev}/suites_base'), suites(f'{ev}/suites_cand')),
    'src_tauri': lambda: (cargo_outcomes(f'{ev}/tauri_base.log', 'src-tauri'), cargo_outcomes(f'{ev}/tauri_cand.log', 'src-tauri')),
    'pytest': lambda: (pytest(f'{ev}/pytest_base.log'), pytest(f'{ev}/pytest_cand.log')),
    'vitest': lambda: (vitest(f'{ev}/vitest_base.json', 'base'), vitest(f'{ev}/vitest_cand.json', 'cand')),
}
for name, get in pairs.items():
    try:
        b, c = get()
        report[name] = diff(b, c)
    except FileNotFoundError as e:
        report[name] = {'missing': str(e).split(':')[0]}

# byte equality, per pass (release: E, F, B1 ordinary + runner; w1: B1 with the retained entry, debug)
def load(p):
    rows = {}
    for line in open(p):
        r = json.loads(line); rows[(r['label'], r['mode'])] = r
    return rows
for pass_name in ('release', 'w1'):
    try:
        hb, hc = load(f'{ev}/bytes_hb_{pass_name}.jsonl'), load(f'{ev}/bytes_hc_{pass_name}.jsonl')
    except FileNotFoundError as e:
        report[f'bytes_{pass_name}'] = {'missing': str(e)}; continue
    sets = collections.defaultdict(collections.Counter)
    diffs = []
    for k in sorted(set(hb) | set(hc)):
        b, c = hb.get(k), hc.get(k)
        s = (b or c)['set']
        same = b is not None and c is not None and all(b[f] == c[f] for f in ('ordinary', 'retained', 'runner'))
        sets[s]['rows'] += 1
        sets[s]['equal' if same else 'differ'] += 1
        if b:
            if b['retained'].get('kind') == 'successor': sets[s]['w1_successor_published'] += 1
            if b['retained'].get('kind') == 'ordinary': sets[s]['w1_ordinary_published'] += 1
            if b['runner'].get('document'): sets[s]['runner_export_document'] += 1
            if b['ordinary'].get('status') == 'MECHANICS_SOLVED': sets[s]['ordinary_solved'] += 1
        if not same: diffs.append(dict(label=k[0], mode=k[1], base=b, cand=c))
    report[f'bytes_{pass_name}'] = dict(by_set={k: dict(v) for k, v in sets.items()}, differences=diffs)
json.dump(report, open(out, 'w'), indent=1)
for k, v in report.items():
    if 'changed' in v: print(k, 'base', v['base'], 'cand', v['cand'], 'changed', len(v['changed']))
    else: print(k, json.dumps(v)[:400])
