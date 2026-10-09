"""RV127 addendum 02: the sample at main (ba500defa4) and the PR code (8a12de28db).
Same labels as REVIEW.md's sample, plus every source-block request (T2 radius), the contract-corpus
case 67 (V1), result_export producer case 1 (T1), and the numerical-sensitive torsion model.
Only labels whose payload is identical in both trees are compared. Usage: select2.py enum_main enum_pr out"""
import json, sys
m = {r['label']: r for r in json.load(open(sys.argv[1]))}
p = {r['label']: r for r in json.load(open(sys.argv[2]))}
old = [json.loads(json.dumps(x)) for x in json.load(open('inputs.json'))]
labels = [(x['set'], x['label']) for x in old if x['set'] in ('E', 'F', 'B1', 'P')]
extra = [l for l in p if '/source_blocks/' in l and 'rejected_stress_range' not in l]
extra += [l for l in p if 'case_67_accept_set_field_component_expansion_joint_stiffness' in l]
extra += [l for l in p if l.startswith('fixtures/results/invented/result_export_v0_2.json#/producer_cases/1/')]
extra += [l for l in p if l.startswith('fixtures/product_preview/numerical_sensitive_torsion_model.json')]
seen = {l for _, l in labels}
for l in sorted(set(extra)):
    if l not in seen:
        labels.append((p[l]['set'], l)); seen.add(l)
items, skipped = [], []
for s, l in labels:
    if l not in m or l not in p:
        skipped.append((l, 'missing')); continue
    if m[l]['payload'] != p[l]['payload']:
        skipped.append((l, 'payload differs')); continue
    items.append({'set': s, 'label': l, 'payload': p[l]['payload']})
# the refusal probes from REVIEW.md (constructed inputs), unchanged
items += [x for x in old if x['set'] == 'R']
json.dump(items, open(sys.argv[3], 'w'))
c = {}
for i in items: c[i['set']] = c.get(i['set'], 0) + 1
print(c, 'skipped:', skipped)
print('only at PR:', sorted(set(p) - set(m)))
