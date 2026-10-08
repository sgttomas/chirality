#!/usr/bin/env python3
"""I112 PR-N part 1: what the moved numbers in diagnostic text are (new). Reads part1_norm_compare.json's DIAG items and checks
each moved number exactly against the norm it prints:

* NUMERICAL_INTEGRITY_SENSITIVE "<member>.<end>: q=<x> N*m": q is the formation guard's end bending magnitude,
  norm2(My, Mz) of the corrected local end forces (PP lib.rs, solve_load_case_observed). The components are the same
  envelope's published element_local_bending_moment_y and _z rows of that member end.
* NUMERICAL_INTEGRITY_PHYSICAL_MECHANISM "Mechanism { direction: [...] }; global_dof_map=[...]": for a free body the
  direction's translation entries are characteristic_length x the rigid translation (FK rigid_body.rs, assess_rigid_body),
  and characteristic_length = max over the body's nodes of norm3(p - p_first). The components are the run's request
  coordinates of the body's nodes (they are not echoed in the envelope).
For each: the candidate's number must equal the exactly computed correctly rounded norm (normdiff.cr_norm, Fractions), and the
base's number is compared with this host's libm hypot (chain) of the same components.
Usage: python3 -B diag_norm_check.py <part1_norm_compare.json> <base-dir> <cand-dir> <gen_out> <normdiff-dir> <out.json>
"""
import json
import os
import re
import sys

rep_path, base_dir, cand_dir, gen, nd_dir, out_path = sys.argv[1:7]
sys.path.insert(0, nd_dir)
import normdiff as N  # noqa: E402
import normdiff2 as N2  # noqa: E402

rep = json.load(open(rep_path))
cases = {c['id']: c for c in json.load(open(os.path.join(gen, 'cases.json')))}
NUM = r'-?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?'
out, ok_all = [], True
for d in rep['differing_runs']:
    for src in ('full', 'summary'):
        for it in d[src + '_items']:
            if not it.get('DIAG'):
                continue
            sub = 'full' if src == 'full' else 'envelopes'
            envc = json.load(open(os.path.join(cand_dir, sub, d['run'] + '.json')))
            envb = json.load(open(os.path.join(base_dir, sub, d['run'] + '.json')))
            idx = int(it['path'].rsplit('/', 1)[1])
            mc, mb = envc['diagnostics'][idx]['message'], envb['diagnostics'][idx]['message']
            checks = []
            if it['code'] == 'NUMERICAL_INTEGRITY_SENSITIVE':
                full = json.load(open(os.path.join(cand_dir, 'full', d['run'] + '.json')))
                rows = {r['id']: r for r in full['results']}
                for m_c, m_b in zip(re.finditer(r'([A-Za-z0-9_\-]+)\.([ij]): q=(' + NUM + ') N\\*m', mc),
                                    re.finditer(r'([A-Za-z0-9_\-]+)\.([ij]): q=(' + NUM + ') N\\*m', mb)):
                    if m_c.group(3) == m_b.group(3):
                        continue
                    member, end = m_c.group(1), m_c.group(2)
                    suf = ':end-j' if end == 'j' else ''
                    ids = ['result:moment:%s:bending-y%s' % (member, suf), 'result:moment:%s:bending-z%s' % (member, suf)]
                    comps = [float(rows[i]['value']) for i in ids]
                    cr = N.cr_norm(comps)
                    lc = N2.libm_chain(comps)
                    c = dict(what='%s.%s q (formation guard end bending magnitude)' % (member, end), components=dict(zip(ids, comps)),
                             base=m_b.group(3), cand=m_c.group(3), ulps=N.ulps(float(m_b.group(3)), float(m_c.group(3))),
                             cr_norm=repr(cr), cand_is_cr=(cr == float(m_c.group(3))),
                             base_is_libm_hypot=(lc == float(m_b.group(3))))
                    checks.append(c)
            elif it['code'] == 'NUMERICAL_INTEGRITY_PHYSICAL_MECHANISM':
                dm = re.search(r'direction: \[([^\]]*)\]', mc).group(1).split(', ')
                db = re.search(r'direction: \[([^\]]*)\]', mb).group(1).split(', ')
                dof = json.loads('[' + re.search(r'global_dof_map=\[([^\]]*)\]', mc).group(1) + ']')
                assert len(dm) == len(db) == len(dof)
                case = d['run'].split('__')[0]
                req = json.load(open(os.path.join(gen, cases[case]['request_file'])))
                pos = {n['id']: n['position'] for n in req['model']['nodes']}
                moved = [(dof[i], db[i], dm[i]) for i in range(len(dm)) if dm[i] != db[i]]
                body = [lab.split(':')[0] for lab, _, _ in moved]
                # every node of the body carries the same translation entry; the body is the set of nodes with a nonzero entry
                nonzero = sorted({dof[i].split(':')[0] for i in range(len(dm)) if float(dm[i]) != 0.0},
                                 key=lambda n: [x['id'] for x in req['model']['nodes']].index(n))
                p0 = pos[nonzero[0]]
                rel = [[pos[n][a] - p0[a] for a in 'xyz'] for n in nonzero]
                crs = [N.cr_norm(r) for r in rel]
                libs = [N2.libm_chain(r) for r in rel]
                length_cr, length_libm = max(crs), max(libs)
                for lab, b, c in moved:
                    checks.append(dict(what='%s direction entry (characteristic length x rigid translation 1)' % lab,
                                       body_nodes=nonzero, origin=nonzero[0],
                                       components=dict(zip(nonzero, rel)), base=b, cand=c,
                                       ulps=N.ulps(float(b), float(c)), cr_norm=repr(length_cr),
                                       cand_is_cr=(length_cr == float(c)), base_is_libm_hypot=(length_libm == float(b))))
                assert sorted(body) == sorted(nonzero), (body, nonzero)
            ok = bool(checks) and len(checks) == len(it['numbers']) and all(c['cand_is_cr'] and c['base_is_libm_hypot'] for c in checks)
            ok_all &= ok
            out.append(dict(run=d['run'], source=src, path=it['path'], code=it['code'], severity=it['severity'], explained=ok,
                            checks=checks))
json.dump(dict(items=out, all_explained=ok_all), open(out_path, 'w'), indent=1)
for o in out:
    print('%s [%s] %s %s: %s' % (o['run'], o['source'], o['code'], 'explained' if o['explained'] else 'NOT EXPLAINED',
          '; '.join('%s: %s -> %s (%d ulp), CR %s, cand CR %s, base libm %s' % (c['what'], c['base'], c['cand'], c['ulps'],
                    c['cr_norm'], c['cand_is_cr'], c['base_is_libm_hypot']) for c in o['checks'][:1])
          + (' (+%d more, same)' % (len(o['checks']) - 1) if len(o['checks']) > 1 else '')))
print('all diagnostic moves are the exact correctly rounded norm of their components, and every base value this host\'s libm hypot:',
      ok_all)
