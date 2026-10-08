"""I110 round 2: the byte-equality input list. Usage: make_inputs.py <P root> <out.json>
Sets: E = committed exact model documents (0.3.0/0.4.0 + 2.0.0/exact_straight_pressure_v2);
F = committed 0.1.0/0.2.0 documents without any pressure primitive; B1 = the retained corpus
(fixtures/results/retained_precision_*.json), a subset of F. Execution records excluded."""
import json, os, sys
root, out = sys.argv[1], sys.argv[2]
items = []
def is_model(d):
    return isinstance(d, dict) and all(k in d for k in ('pipe_segments', 'nodes', 'load_cases', 'schema_version'))
def has_pressure(m):
    return any(isinstance(l, dict) and (l.get('category') == 'pressure' or l.get('dimension') == 'pressure')
               for c in m.get('load_cases') or [] for l in (c.get('primitive_loads') or []))
def walk(o, path, parent, rel):
    if is_model(o):
        pc = o.get('pressure_contract')
        if o['schema_version'] in ('0.3.0', '0.4.0') and pc == {'version': '2.0.0', 'mode': 'exact_straight_pressure_v2'}:
            s = 'E'
        elif o['schema_version'] in ('0.1.0', '0.2.0') and pc is None and not has_pressure(o):
            s = 'B1' if rel.startswith('fixtures/results/retained_precision') else 'F'
        else:
            return
        if isinstance(parent, dict) and 'model' in parent and set(parent) <= {'model', 'materials'}:
            payload = parent
        else:
            payload = {'model': o, 'materials': []}
        items.append({'set': s, 'label': f'{rel}#{path or "/"}', 'payload': payload})
        return
    if isinstance(o, dict):
        for k, v in o.items(): walk(v, f'{path}/{k}', o, rel)
    elif isinstance(o, list):
        for i, v in enumerate(o): walk(v, f'{path}/{i}', o, rel)
for dp, dn, fn in os.walk(root):
    dn[:] = sorted(x for x in dn if x not in ('node_modules', 'target', '.git', 'execution', '_run_records'))
    for f in sorted(fn):
        if not f.endswith('.json'): continue
        p = os.path.join(dp, f)
        try: d = json.load(open(p))
        except Exception: continue
        walk(d, '', None, os.path.relpath(p, root))
json.dump(items, open(out, 'w'))
c = {}
for i in items: c[i['set']] = c.get(i['set'], 0) + 1
print(c, len(items))
