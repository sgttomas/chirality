"""RV123: compare the exact successor (m3x) with the preview milestone successor, row by row.
m3x is the milestone authored exact with E = 2e11, nu = 0.25 (G = 8e10 exactly, the milestone's G),
same OD and wall, so the prepared sections and the K law coincide; shared rows should agree."""
import json, struct, sys
R = sys.argv[1]
h = lambda x: struct.pack('>d', x).hex()
for mode in ['sparse_interactive', 'dense_scrutiny']:
    x = json.load(open(f'{R}/retained_precision_exact_successor_{mode}.json'))['source']
    p = json.load(open(f'{R}/retained_precision_milestone_successor_{mode}.json'))['source']
    xr = {r['id']: r for r in x['results']}
    pr = {r['id']: r for r in p['results']}
    shared = sorted(set(xr) & set(pr))
    only_x = sorted(set(xr) - set(pr)); only_p = sorted(set(pr) - set(xr))
    diff = [i for i in shared if h(xr[i]['value']) != h(pr[i]['value']) or xr[i]['kind'] != pr[i]['kind']]
    print(mode, 'exact rows', len(xr), 'preview rows', len(pr), 'shared', len(shared), 'value/kind differs', len(diff))
    print('  only exact:', only_x)
    print('  only preview:', [(i, pr[i]['kind']) for i in only_p])
    for i in diff[:20]:
        print('  DIFF', i, xr[i]['kind'], xr[i]['value'], pr[i]['value'])
    xb = {a['result_id']: a['bound'] for a in x['retained_precision']['body']['cases'][0]['selection']['absolute_verified']}
    pb = {a['result_id']: a['bound'] for a in p['retained_precision']['body']['cases'][0]['selection']['absolute_verified']}
    bd = [i for i in set(xb) & set(pb) if xb[i] != pb[i]]
    print('  bounds: exact', len(xb), 'preview', len(pb), 'shared differing', len(bd), bd[:5])
    # evidence: the exact maxima vs preview maxima
    xe = x['contract_evidence']['exact_cases'][0]['pipe_stress_extrema']
    pe = p['contract_evidence']['preview_cases'][0]['pipe_stress_extrema']
    keys = ["station_fraction","span_index","local_fraction","value_lower_pa","value_upper_pa","global_upper_bound_pa","certified_gap_pa","subdivisions"]
    for a, b in zip(xe, pe):
        print('  extrema', a.get('pipe_id'), [(k, a[k] == b[k]) for k in keys if a[k] != b[k]] or 'equal on the eight fields')
    print('  summary exact', x['summary'].get('max_open_formula_stress'), '\n  summary prev ', p['summary'].get('max_open_formula_stress'))
    print('  disp exact', x['summary'].get('max_displacement'), '\n  disp prev ', p['summary'].get('max_displacement'))
