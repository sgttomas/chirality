#!/usr/bin/env python3
"""Independent bounded replay of the 36 preserved W1 admission decisions.

No audit/runner imports; reproduces only the exercised W1 admitted branch,
asserting its preconditions. Does not certify policy, E_max, or another host.
"""
import json
from check_records import ROOT, T3, A, load

H = 'projects/chirality-piping/core/solver/performance_harness'


def lines(path):
    return [json.loads(s) for s in (ROOT/path).read_text().splitlines() if s.strip()]


def policy(run, estimate, previous):
    assert run['mode'] == 'w1a' and estimate <= run['heap_cap_bytes']//2
    if run['members'] > 100:
        predecessor = run['model'].replace('-n%05d-' % run['members'], '-n%05d-' % (run['members']//10))
        assert any(x['model'] == predecessor and x['mode'] == 'w1a' and x.get('classification') not in (None, 'not_run') for x in previous)
    usable = [x for x in previous if x['family'] == run['family'] and x['mode'] == 'w1a'
              and (100 if run['members'] >= 1000 else 0) <= x['members'] < run['members']
              and x.get('classification') == 'ok']
    rss_ratios, footprint_ratios, rf_ratios = [], [], []
    for rec in usable:
        fp = rec['rss']['time_peak_footprint_bytes']
        rss = rec['peak_rss_bytes']
        heap = rec['repeats_heap_peak_move'] or 0
        rss_ratios.append(max(max(0,rss-run['baseline_rss_bytes']),heap)/rec['estimate_adm_bytes'])
        footprint_ratios.append(max(max(0,fp-run['baseline_footprint_bytes']),heap)/rec['estimate_adm_bytes'])
        rf_ratios.append(rss/fp)
    rho = max(footprint_ratios) if footprint_ratios else 2.0
    rho_rss = max(rss_ratios) if rss_ratios else 2.0
    rf = max(rf_ratios) if rf_ratios else 1.45
    half = run['rss_cap_bytes']//2
    assert estimate*rho <= half
    footprint = int(estimate*rho)
    projected, limit = int(footprint*rf), int(.8*run['rss_cap_bytes'])
    assert projected <= limit
    return {'decision':'admitted','reason':'estimate %d B x rho %.3f <= C/2; projected RSS %d B <= 0.8C' % (estimate,rho,projected),
            'estimate_adm_bytes':estimate,'rho':rho,'rho_rss':rho_rss,'half_cap_bytes':half,
            'footprint_estimate_bytes':footprint,'rss_to_footprint':rf,'projected_rss_bytes':projected,
            'projected_rss_limit_bytes':limit}


def main():
    h = {r['model']:r for r in lines(ROOT/H/'observations/k6b/counts.jsonl')}
    audit = {r['slice']:r for r in load(A/'_run_records/admissions.json')['results']}
    summaries = []
    for name in ['VK','KF3']:
        folder = T3/'IMPLEMENTATION'/name/'_run_records/b'
        counts = {r['model']:r for r in lines(folder/('setup/counts.jsonl' if name == 'VK' else 'counts.json'))}
        records = lines(folder/'runs/records.jsonl')
        historical, sensitive, results = [], [], []
        audit_runs = {r['run_id']:r for r in audit[name]['runs']}
        for rec in records:
            hc, vc = h[rec['model']], counts[rec['model']]
            for key in ['free_dofs','rows','profile_entries','pattern_entries']:
                assert hc['w1_'+key] == vc[key]
            delta = 288*hc['w1_free_dofs'] - 8*(3*hc['w1_rows']+hc['w1_free_dofs'])
            estimate = hc['estimate_adm_bytes_w1a']-hc['estimate_w1_fixed_bytes']+vc['estimate_fixed_bytes']+max(0,delta)
            old_result = policy(rec,vc['estimate_max_bytes'],historical)
            new_result = policy(rec,estimate,sensitive)
            assert old_result == rec['admission'], rec['run_id']
            assert new_result == audit_runs[rec['run_id']]['sensitivity'], rec['run_id']
            historical.append(rec)
            sensitive.append(dict(rec,estimate_adm_bytes=estimate))
            results.append({'run_id':rec['run_id'],'all_original_fields_match':True,
                            'all_sensitivity_fields_match':True,'decision_changed':False,
                            'sensitivity_rho':new_result['rho']})
        summaries.append({'slice':name,'rows':results})
    figures = load(A/'_run_records/figures.json')
    vr = {r['model']:r for r in lines(T3/'IMPLEMENTATION/KF3/_run_records/b/counts.json')}
    memory = []
    for row in figures['memory']:
        hc, vc = h[row['model']], vr[row['model']]
        pattern = '*_'+row['model']+'_w1a.jsonl'
        files = list((ROOT/T3/'IMPLEMENTATION/KF3/_run_records/b/runs').glob(pattern))
        assert len(files) == 1
        peak = next(r['repeats_heap_peak'] for r in lines(files[0]) if r['kind'] == 'summary')
        margin = hc['estimate_adm_bytes_w1a']-hc['estimate_w1_fixed_bytes']+vc['estimate_fixed_bytes']-peak
        omission = (288-8)*hc['w1_free_dofs']-24*hc['w1_rows']
        assert margin == row['like_for_like_margin'] and omission == row['known_shift_undercount']
        memory.append({'model':row['model'],'margin_bytes':margin,'shift_delta_bytes':omission})
    # Recompute the other figures by parsing the underlying preserved text/JSON;
    # do not copy the audit probe's results into the oracle.
    import re
    probe = (ROOT/T3/'IMPLEMENTATION/KF3/_run_records/d/b1_probe.txt').read_text()
    sizes, coeffs = None, []
    for line in probe.splitlines():
        if line.startswith('MODEL KF3-TREE-n'):
            sizes = int(re.search(r'-n(\d+)-',line)[1])
        m = re.match(r'PAIR (\d+) vs (\d+):.*worst \(b\) ratio Some\(([^)]+)\)',line)
        if m:
            coeffs.append(dict(members=sizes,candidate_p=int(m[1]),verification_P=int(m[2]),ratio=float(m[3]),c=float(m[3])*64))
    assert coeffs == figures['b1_coefficients']
    for row in figures['scale_10000']:
        records = lines(T3/'IMPLEMENTATION'/row['slice']/'_run_records/b/runs/records.jsonl')
        rec = next(r for r in records if r['model'] == row['model'])
        assert all(rec[k] == v for k,v in row.items() if k != 'slice')
    for row in figures['suite_deltas']:
        def suites(name):
            text = (ROOT/T3/'IMPLEMENTATION'/(name+'_MERGE')/'dec025/suites.log').read_text()
            return {m[4]:list(map(int,m[:4])) for m in re.findall(r'^(\d+) passed=(\d+) failed=(\d+) ignored=(\d+) (\S+)',text,re.M)}
        before,after = suites(row['baseline']),suites(row['slice'])
        delta = {k:{'before_exit_pass_fail_ignore':before.get(k),'after_exit_pass_fail_ignore':after.get(k)} for k in set(before)|set(after) if before.get(k) != after.get(k)}
        assert delta == row['delta']
    print(json.dumps({'admissions':summaries,'memory':memory,'coefficient_rows_verified':len(coeffs),
                      'scale_10000_rows_verified':len(figures['scale_10000']),
                      'suite_deltas_verified':len(figures['suite_deltas']),
                      'limits':['Only the exercised admitted W1 branch checked; other policy branches are not certified.',
                                'Historical measurements retained unchanged under the sensitivity substitution; no final phase bound or M3 admission established.']},indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
