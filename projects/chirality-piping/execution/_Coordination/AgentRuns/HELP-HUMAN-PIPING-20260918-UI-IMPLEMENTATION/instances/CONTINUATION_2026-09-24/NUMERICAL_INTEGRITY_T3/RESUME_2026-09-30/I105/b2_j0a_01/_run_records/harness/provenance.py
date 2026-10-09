"""I105 J0a: where each h-vs-b and h-vs-m difference comes from. A test added at h relative to b should exist at m
(main brought it), and one added relative to m should exist at b (b2's own); removed and changed are listed in full.
Usage: provenance.py <SUITES_CMP.json> <out json>"""
import json, sys
d = json.load(open(sys.argv[1]))
out = {}
for name, r in d.items():
    if 'h_vs_b' not in r:
        continue
    hb, hm = r['h_vs_b'], r['h_vs_m']
    added_b_not_from_main = [k for k in hb['added'] if k in hm['added']]  # also absent at m: neither side's
    added_m_not_from_b2 = [k for k in hm['added'] if k in hb['added']]
    out[name] = {
        'h_vs_b': {'added': len(hb['added']), 'added_absent_at_m_too': added_b_not_from_main,
                   'removed': hb['removed'], 'changed': hb['changed']},
        'h_vs_m': {'added': len(hm['added']), 'added_absent_at_b_too': added_m_not_from_b2,
                   'removed': hm['removed'], 'changed': hm['changed']}}
    print(name, json.dumps(out[name], indent=1)[:3000])
json.dump(out, open(sys.argv[2], 'w'), indent=1)
