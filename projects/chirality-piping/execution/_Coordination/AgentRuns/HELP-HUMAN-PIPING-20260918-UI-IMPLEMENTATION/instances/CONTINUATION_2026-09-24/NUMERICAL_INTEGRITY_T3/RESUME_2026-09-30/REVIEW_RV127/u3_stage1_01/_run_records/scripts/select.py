"""RV127: the sample for byte reproduction and the refusal probes. Usage: select.py <enum.json> <out.json>"""
import copy, json, sys
rows = json.load(open(sys.argv[1]))
E = [1, 47, 48, 49, 165, 166, 169, 173, 174, 176, 232, 234, 238, 252, 256, 260]
F = [0, 2, 3, 4, 25, 45, 50, 57, 64, 68, 131, 133, 141, 143, 149, 151, 160, 162, 164, 179, 185, 226, 229, 230, 231]
B1 = [193, 197, 199, 208, 210, 217, 219, 223]
items = []
for s, idx in (('E', E), ('F', F), ('B1', B1)):
    for i in idx:
        assert rows[i]['set'] == s, (i, rows[i]['set'])
        items.append({'set': s, 'label': rows[i]['label'], 'payload': rows[i]['payload']})
for r in rows:
    if r['set'] == 'P':
        items.append({'set': 'P', 'label': r['label'], 'payload': r['payload']})
def model_of(i):
    return copy.deepcopy(rows[i]['payload'])
# Probes: constructed refusal cases (candidate must refuse each by PRESSURE_MODEL_REAUTHOR_REQUIRED unless noted).
p = model_of(175)  # physics_source/n05 exact
p['model']['pressure_contract'] = {'version': '1.0.0', 'mode': 'legacy_pressure_v1'}
for c in p['model']['load_cases']: c.pop('pressure_regions', None)
items.append({'set': 'R', 'label': 'R1 label on n05 (regions removed)', 'payload': p})
p2 = copy.deepcopy(p)
p2['model']['load_cases'][0]['primitive_loads'].append({'id': 'load:rv127-p', 'category': 'pressure', 'target': {'type': 'element', 'pipe': p2['model']['pipe_segments'][0]['id']}, 'direction': 'global_x', 'magnitude': {'value': 2.0e6, 'unit': 'Pa'}, 'dimension': 'pressure', 'provenance': 'rv127_probe'})
items.append({'set': 'R', 'label': 'R2 label plus nonzero legacy primitive', 'payload': p2})
u = copy.deepcopy(p); u['model']['pressure_contract'] = {'version': '1.0.1', 'mode': 'legacy_pressure_v1'}
items.append({'set': 'R', 'label': 'R3 unknown contract 1.0.1/legacy (UNSUPPORTED)', 'payload': u})
for name, cat, dim, val in (('R4 zero pressure primitive', 'pressure', 'pressure', 0.0),
                            ('R5 negative-zero pressure primitive', 'pressure', 'pressure', -0.0),
                            ('R6 category pressure, dimension force, zero', 'pressure', 'force', 0.0),
                            ('R7 hydrotest category, pressure dimension, zero', 'hydrotest', 'pressure', 0.0),
                            ('R8 nonzero pressure primitive', 'pressure', 'pressure', 1.0e5)):
    for base_i, tag in ((193, 'B1#0'), (2, 'F invented')):
        q = model_of(base_i)
        q['model']['load_cases'][0]['primitive_loads'].append({'id': 'load:rv127-p', 'category': cat, 'target': {'type': 'element', 'pipe': q['model']['pipe_segments'][0]['id']}, 'direction': 'global_x', 'magnitude': {'value': val, 'unit': 'Pa'}, 'dimension': dim, 'provenance': 'rv127_probe'})
        items.append({'set': 'R', 'label': '%s on %s' % (name, tag), 'payload': q})
json.dump(items, open(sys.argv[2], 'w'))
c = {}
for i in items: c[i['set']] = c.get(i['set'], 0) + 1
print(c)
