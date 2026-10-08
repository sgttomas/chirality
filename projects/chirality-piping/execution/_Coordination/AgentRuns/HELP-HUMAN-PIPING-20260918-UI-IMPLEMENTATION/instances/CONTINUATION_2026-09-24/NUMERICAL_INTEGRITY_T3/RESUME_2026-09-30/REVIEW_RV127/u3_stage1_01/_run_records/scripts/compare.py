"""RV127: compare the harness rows at B and at the candidate. Usage: compare.py <base.jsonl> <cand.jsonl> <out.json>"""
import json, sys
def load(p):
    return {(r['set'], r['label'], r['mode']): r for r in map(json.loads, open(p))}
b, c = load(sys.argv[1]), load(sys.argv[2])
assert set(b) == set(c), 'row sets differ'
fields = [('ordinary', 'sha'), ('retained_direct', 'kind'), ('retained_direct', 'sha'), ('runner', 'output'),
          ('runner', 'mechanics'), ('runner', 'document'), ('runner', 'unavailability'),
          ('runner_retained_headless', 'output'), ('runner_retained_headless', 'document')]
out = {'by_set': {}, 'differences': [], 'probe_changes': []}
for key in sorted(b):
    s, label, mode = key
    rb, rc = b[key], c[key]
    st = out['by_set'].setdefault(s, {'rows': 0, 'all_equal': 0, 'solved': 0, 'w1_successor': 0, 'w1_ordinary': 0, 'export_documents': 0})
    st['rows'] += 1
    diffs = [f'{a}.{f}' for a, f in fields if rb[a].get(f) != rc[a].get(f)]
    for a in ('ordinary', 'retained_direct', 'runner', 'runner_retained_headless'):
        if 'error' in rb[a] or 'error' in rc[a]:
            diffs.append(f'{a}.error')
    st['all_equal'] += not diffs
    st['solved'] += rc['ordinary'].get('status') == 'MECHANICS_SOLVED'
    st['w1_successor'] += rc['retained_direct'].get('kind') == 'successor'
    st['w1_ordinary'] += rc['retained_direct'].get('kind') == 'ordinary'
    st['export_documents'] += rc['runner'].get('document') is not None
    if diffs:
        row = {'set': s, 'label': label, 'mode': mode, 'fields': diffs,
               'base': {'status': rb['ordinary'].get('status'), 'blocking': sorted({d[0] for d in rb['ordinary'].get('blocking') or []}), 'w1': rb['retained_direct'].get('kind')},
               'cand': {'status': rc['ordinary'].get('status'), 'blocking': sorted({d[0] for d in rc['ordinary'].get('blocking') or []}), 'w1': rc['retained_direct'].get('kind')}}
        (out['probe_changes'] if s in ('R',) else out['differences']).append(row)
json.dump(out, open(sys.argv[3], 'w'), indent=1)
print(json.dumps(out['by_set'], indent=1))
print('differences outside the probes:', len(out['differences']))
for d in out['differences']: print('  DIFF', d)
for d in out['probe_changes']: print('  probe', d['label'], d['mode'][:6], d['base']['status'], d['base']['blocking'], '->', d['cand']['status'], d['cand']['blocking'])
