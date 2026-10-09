"""I105 J0a: test by test, the merged head (h) against b2's start head (b) and main (m), and the census.
Suites: cargo logs S/logs/<t>_{pp,runner,re}.log; vitest JSON and pytest junit in S/out/suites; tsc's exit code.
Census: S/out/census/<t>_<corpus>_<reader>.jsonl, whole records compared entry by entry, h against b and m, and
against I101's repair-03 census at the readers' heads where one exists (07m and 07n; given as gz files).
Usage: compare_j0a.py <S> <I101 repair_03 census dir> <out dir>"""
import gzip, json, pathlib, re, sys
import xml.etree.ElementTree as ET
S, I101, OUT = map(pathlib.Path, sys.argv[1:4])
HEADS = ('h', 'b', 'm')


def cargo(path):
    out, binary = {}, '?'
    for line in path.read_text(errors='replace').splitlines():
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
            k = f'{binary}::{m.group(1)}'
            assert k not in out, k
            out[k] = m.group(2)
    return out


def vitest(path):
    out = {}
    for f in json.loads(path.read_text())['testResults']:
        name = f['name'].split('/apps/desktop/', 1)[-1]
        seen = {}
        for a in f['assertionResults']:
            k = f'{name}::{a["fullName"]}'
            seen[k] = seen.get(k, 0) + 1
            if seen[k] > 1:  # a repeated name (vitest allows it): numbered by occurrence in its file
                k = f'{k} #{seen[k]}'
            out[k] = a['status']
    return out


def junit(path):
    out = {}
    for tc in ET.parse(path).getroot().iter('testcase'):
        k = f'{tc.get("classname")}::{tc.get("name")}'
        st = 'passed'
        for c in tc:
            if c.tag in ('failure', 'error'):
                st = 'failed'
            elif c.tag == 'skipped':
                st = 'skipped'
        n, base = 1, k
        while k in out:
            n += 1; k = f'{base} #{n}'
        out[k] = st
    return out


def rc(label):
    m = re.search(r'^# end \S+ rc=(\d+)$', (S / 'logs' / f'{label}.log').read_text(), re.M)
    return int(m.group(1)) if m else None


def pair(x, y):
    return {'changed': {k: [x[k], y[k]] for k in sorted(x.keys() & y.keys()) if x[k] != y[k]},
            'added': {k: y[k] for k in sorted(y.keys() - x.keys())},
            'removed': {k: x[k] for k in sorted(x.keys() - y.keys())}}


def counts(d):
    c = {}
    for v in d.values():
        c[v] = c.get(v, 0) + 1
    return dict(sorted(c.items()))


suites = {}
readers = {'pp': lambda t: cargo(S / 'logs' / f'{t}_pp.log'), 'runner': lambda t: cargo(S / 'logs' / f'{t}_runner.log'),
           're': lambda t: cargo(S / 'logs' / f'{t}_re.log'), 'vitest': lambda t: vitest(S / 'out/suites' / f'{t}_vitest.json'),
           'py': lambda t: junit(S / 'out/suites' / f'{t}_py.junit.xml')}
for name, read in readers.items():
    d = {t: read(t) for t in HEADS}
    suites[name] = {'rc': {t: rc(f'{t}_{name}') for t in HEADS}, 'counts': {t: counts(d[t]) for t in HEADS},
                    'h_vs_b': pair(d['b'], d['h']), 'h_vs_m': pair(d['m'], d['h'])}
suites['tsc'] = {'rc': {t: rc(f'{t}_tsc') for t in HEADS}}
(OUT / 'SUITES_CMP.json').write_text(json.dumps(suites, indent=1) + '\n')
for name, r in suites.items():
    print(name, 'rc', r['rc'], *(('counts', r['counts']) if 'counts' in r else ()))
    for p in ('h_vs_b', 'h_vs_m'):
        if p in r:
            print(' ', p, {k: len(v) for k, v in r[p].items()})


def load(p):
    op = gzip.open if str(p).endswith('.gz') else open
    with op(p, 'rt') as f:
        return [json.loads(l) for l in f if l.strip()]


def cmp_census(a, b):
    ka = [(x['set'], x['i'], x['id']) for x in a]
    kb = [(x['set'], x['i'], x['id']) for x in b]
    if ka != kb:
        return {'entries_equal': False, 'a': len(a), 'b': len(b)}
    ch = [x['id'] + ':' + k for x, y in zip(a, b) for k in sorted(set(x) | set(y)) if x.get(k) != y.get(k)]
    return {'entries_equal': True, 'entries': len(a), 'changes': ch}


I101F = {('07m', 'rs'): 'final5_rs_census.jsonl.gz', ('07m', 'ts'): 'final5_ts_census.jsonl.gz', ('07m', 'py'): 'py_final5_07m.jsonl.gz',
         ('07n', 'rs'): 'c07n_final5_rs_census.jsonl.gz', ('07n', 'ts'): 'c07n_final5_ts_census.jsonl.gz', ('07n', 'py'): 'py_final5_07n.jsonl.gz'}
census = {}
for k in ('07m', '07n', '07nN'):
    for r in ('rs', 'ts', 'py'):
        d = {t: load(S / 'out/census' / f'{t}_{k}_{r}.jsonl') for t in HEADS}
        e = {'entries': {t: len(d[t]) for t in HEADS}, 'sets': {s: sum(1 for x in d['h'] if x['set'] == s) for s in ('base', 'mutation', 'must_pass')},
             'h_vs_b': cmp_census(d['b'], d['h']), 'h_vs_m': cmp_census(d['m'], d['h'])}
        if (k, r) in I101F:
            e['h_vs_I101_repair03'] = cmp_census(load(I101 / I101F[(k, r)]), d['h'])
        census[f'{k}_{r}'] = e
        print(k, r, e['entries'], e['sets'], {p: (len(v['changes']) if v.get('entries_equal') else 'ENTRIES DIFFER') for p, v in e.items() if p.startswith('h_vs')})
(OUT / 'CENSUS_CMP.json').write_text(json.dumps(census, indent=1) + '\n')
