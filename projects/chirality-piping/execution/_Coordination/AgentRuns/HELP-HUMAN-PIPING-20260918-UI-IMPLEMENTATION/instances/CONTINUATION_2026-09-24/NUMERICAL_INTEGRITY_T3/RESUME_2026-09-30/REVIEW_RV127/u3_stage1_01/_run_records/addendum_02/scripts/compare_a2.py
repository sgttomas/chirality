"""RV127 addendum 02: classify main-vs-PR output differences.
For every row whose 9 harness fields are not all equal, the dumped JSON outputs are compared leaf by leaf.
A differing leaf is 'declared' when the main string with every declared replacement applied equals the PR
string; 'digest' when its key names a digest (sha256/digest/hash/checksum) and both values are digest-like
strings; otherwise 'other'. Usage: compare_a2.py <main.jsonl> <pr.jsonl> <dump_main> <dump_pr> <out.json>"""
import json, os, re, sys
PAIRS = [
    ("pressure_thrust_treatment=arc_end_cap_tangent_pair_plus_consistent_radial_wall_load",
     "pressure_thrust_treatment=none_pressure_refused_outside_the_exact_straight_contract"),
    ("pressure_thrust_generation=load_side_user_effective_area;pressure_thrust=",
     "pressure_thrust_generation=none_pressure_refused_outside_the_exact_straight_contract;user_pressure_thrust_reference="),
    ("; pressure-thrust generation is load-side effective-area evidence and no compliance claim is made",
     "; no joint pressure thrust is generated and no compliance claim is made"),
    ("Pressure thrust and pressure stress retain the existing preview formulation and capability qualifications; pressure formulation qualification remains open.",
     "Pressure is not solved on this profile: legacy pressure inputs are refused, and pressure is solved only on the exact straight-pressure profile, under that profile's own qualifications."),
    ("expansion joint components require solver_consumption=mechanics_geometry_and_user_flexibility under DEC-045; pressure thrust remains load-side input evidence",
     "expansion joint components require solver_consumption=mechanics_geometry_and_user_flexibility under DEC-045; no joint pressure thrust is generated"),
    ("expansion joint effective pressure area and movement limit must be finite positive user-entered values before load-side pressure-thrust evidence can be generated",
     "expansion joint effective pressure area and movement limit must be finite positive user-entered values; they are recorded as input evidence only, and no joint pressure thrust is generated"),
]
DIGEST_KEY = re.compile(r'sha256|digest|hash|checksum', re.I)
DIGEST_VAL = re.compile(r'^(sha256:)?[0-9a-f]{64}$')
def apply(s):
    for a, b in PAIRS: s = s.replace(a, b)
    return s
def leaves(a, b, path, out):
    if type(a) != type(b):
        out.append(('other', path, a, b)); return
    if isinstance(a, dict):
        if set(a) != set(b):
            out.append(('other', path + '{keys}', sorted(set(a) ^ set(b)), None))
        for k in a:
            if k in b: leaves(a[k], b[k], path + '/' + k, out)
    elif isinstance(a, list):
        if len(a) != len(b): out.append(('other', path + '[len]', len(a), len(b))); return
        for i, (x, y) in enumerate(zip(a, b)): leaves(x, y, f'{path}/{i}', out)
    elif a != b:
        key = path.rsplit('/', 1)[-1]
        if isinstance(a, str) and apply(a) == b and a != b:
            out.append(('declared', path, None, None))
        elif isinstance(a, str) and isinstance(b, str) and (DIGEST_KEY.search(key) or DIGEST_KEY.search(path)) and DIGEST_VAL.match(a) and DIGEST_VAL.match(b):
            out.append(('digest', path, None, None))
        else:
            out.append(('other', path, a if not isinstance(a, str) else a[:160], b if not isinstance(b, str) else b[:160]))
def load(p): return [json.loads(l) for l in open(p)]
mrows, prows = load(sys.argv[1]), load(sys.argv[2])
assert len(mrows) == len(prows)
FIELDS = [('ordinary', 'sha'), ('retained_direct', 'kind'), ('retained_direct', 'sha'), ('runner', 'output'),
          ('runner', 'mechanics'), ('runner', 'document'), ('runner', 'unavailability'),
          ('runner_retained_headless', 'output'), ('runner_retained_headless', 'document')]
report = {'by_set': {}, 'rows': []}
for idx2, (m, p) in enumerate(zip(mrows, prows)):
    assert (m['set'], m['label'], m['mode']) == (p['set'], p['label'], p['mode'])
    idx = idx2 // 2
    st = report['by_set'].setdefault(m['set'], {'rows': 0, 'equal': 0, 'declared_or_digest_only': 0, 'other': 0})
    st['rows'] += 1
    diff = [f'{a}.{f}' for a, f in FIELDS if m[a].get(f) != p[a].get(f)]
    if not diff:
        st['equal'] += 1; continue
    classes, detail = {}, []
    for kind in ('ordinary', 'mechanics', 'document', 'successor', 'output'):
        fm = os.path.join(sys.argv[3], f"{idx}_{m['mode']}_{kind}.json"); fp = os.path.join(sys.argv[4], f"{idx}_{p['mode']}_{kind}.json")
        if not (os.path.exists(fm) or os.path.exists(fp)): continue
        if os.path.exists(fm) != os.path.exists(fp):
            classes.setdefault(kind, {})['other'] = 1; detail.append((kind, 'presence differs')); continue
        bm, bp = open(fm, 'rb').read(), open(fp, 'rb').read()
        if bm == bp: continue
        out = []
        leaves(json.loads(bm), json.loads(bp), '', out)
        c = {}
        for cls, path, a, b in out:
            c[cls] = c.get(cls, 0) + 1
            if cls == 'other': detail.append((kind, path, a, b))
        classes[kind] = c
    worst = 'other' if any('other' in c for c in classes.values()) else 'declared_or_digest_only'
    st[worst] += 1
    report['rows'].append({'set': m['set'], 'label': m['label'], 'mode': m['mode'], 'fields': diff, 'classes': classes, 'other': detail[:20]})
json.dump(report, open(sys.argv[5], 'w'), indent=1)
print(json.dumps(report['by_set'], indent=1))
for r in report['rows']:
    print(r['set'], r['mode'][:6], r['label'][-80:], json.dumps(r['classes']), ('OTHER ' + json.dumps(r['other'])[:400]) if r['other'] else '')
