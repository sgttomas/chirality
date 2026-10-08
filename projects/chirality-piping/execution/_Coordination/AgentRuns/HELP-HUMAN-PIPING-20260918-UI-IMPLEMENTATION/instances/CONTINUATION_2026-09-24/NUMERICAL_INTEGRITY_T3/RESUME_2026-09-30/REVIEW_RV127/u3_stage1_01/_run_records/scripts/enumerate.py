"""RV127: enumerate committed model documents in an archive tree and classify them.
E = schema 0.3.0/0.4.0 with exact contract 2.0.0/exact_straight_pressure_v2;
F = schema 0.1.0/0.2.0, no pressure_contract, no pressure-category/-dimension primitive;
B1 = F documents under fixtures/results/retained_precision*; P = 0.1.0/0.2.0 with a pressure primitive;
L = any document naming legacy_pressure_v1. Usage: enumerate.py <P root> <out.json>"""
import json, os, sys
root, out = sys.argv[1], sys.argv[2]
rows = []
def is_model(d):
    return isinstance(d, dict) and {'pipe_segments', 'nodes', 'load_cases', 'schema_version'} <= set(d)
def prims(m):
    for c in m.get('load_cases') or []:
        for l in c.get('primitive_loads') or []:
            if isinstance(l, dict):
                yield l
def walk(o, ptr, parent, rel):
    if is_model(o):
        pc = o.get('pressure_contract'); sv = o.get('schema_version')
        press = [l for l in prims(o) if l.get('category') == 'pressure' or l.get('dimension') == 'pressure']
        if sv in ('0.3.0', '0.4.0') and pc == {'version': '2.0.0', 'mode': 'exact_straight_pressure_v2'}:
            s = 'E'
        elif sv in ('0.1.0', '0.2.0') and pc is None:
            s = 'P' if press else ('B1' if rel.startswith('fixtures/results/retained_precision') else 'F')
        else:
            s = 'X:%s:%s' % (sv, json.dumps(pc, sort_keys=True))
        payload = parent if isinstance(parent, dict) and 'model' in parent and set(parent) <= {'model', 'materials'} else {'model': o, 'materials': []}
        rows.append({'set': s, 'label': '%s#%s' % (rel, ptr or '/'), 'nodes': len(o.get('nodes') or []),
                     'cases': len(o.get('load_cases') or []), 'payload': payload})
        return
    if isinstance(o, dict):
        for k, v in o.items(): walk(v, ptr + '/' + k, o, rel)
    elif isinstance(o, list):
        for i, v in enumerate(o): walk(v, ptr + '/' + str(i), o, rel)
for dp, dn, fn in os.walk(root):
    dn[:] = sorted(x for x in dn if x not in ('node_modules', 'target', '.git', 'execution', '_run_records'))
    for f in sorted(fn):
        if f.endswith('.json'):
            p = os.path.join(dp, f)
            try:
                d = json.load(open(p))
            except Exception:
                continue
            walk(d, '', None, os.path.relpath(p, root))
json.dump(rows, open(out, 'w'))
c = {}
for r in rows: c[r['set']] = c.get(r['set'], 0) + 1
print(json.dumps(c, indent=1), len(rows))
