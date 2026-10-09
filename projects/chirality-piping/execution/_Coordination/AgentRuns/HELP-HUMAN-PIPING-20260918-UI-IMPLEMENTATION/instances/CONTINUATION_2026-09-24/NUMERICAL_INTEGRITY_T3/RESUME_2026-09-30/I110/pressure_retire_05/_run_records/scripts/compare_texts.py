"""I110 round 4: byte comparison against B with declared text changes. For each row and output, equal to B
(raw sha), or differs only in declared strings (normalized sha equals B's sha), or differs otherwise.
Usage: compare_texts.py <hb.jsonl> <hc.jsonl>"""
import json, sys, collections
def load(p): return {(r['label'], r['mode']): r for r in map(json.loads, open(p))}
hb, hc = load(sys.argv[1]), load(sys.argv[2])
c = collections.Counter(); other = []; declared = []
def outputs(r):
    out = {'ordinary': r['ordinary'].get('sha') or r['ordinary'].get('error'),
           'mechanics': r['runner'].get('mechanics'), 'document': r['runner'].get('document'),
           'unavailability': json.dumps(r['runner'].get('unavailability'), sort_keys=True),
           'runner_error': r['runner'].get('error'),
           'retained': r['retained'].get('sha') or r['retained'].get('error'), 'retained_kind': r['retained'].get('kind')}
    return out
for k in sorted(set(hb) | set(hc)):
    b, h = hb.get(k), hc.get(k)
    if b is None or h is None: c['missing'] += 1; other.append(k); continue
    ob, oh = outputs(b), outputs(h)
    row_state = 'equal'
    for name in ob:
        if ob[name] == oh[name]: continue
        norm = h.get('texts', {}).get(name, {}).get('norm')
        if norm is not None and norm == ob[name]:
            row_state = 'declared' if row_state == 'equal' else row_state
            declared.append((k, name))
        else:
            row_state = 'other'; other.append((k, name))
    c[(b['set'], row_state)] += 1
print(dict(sorted(c.items())))
print('declared-only outputs:', len(declared), sorted(set(x[0][0] for x in declared))[:20])
print('other differences:', other[:20])
