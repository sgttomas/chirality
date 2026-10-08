#!/usr/bin/env python3
"""I112: the full list behind compare_gate_kf2.py's differences (its log prints only the first 40): per run key, the index
columns that differ (from the index_base.tsv and index_cand.tsv it wrote), and the gate_check rows (outcome, quality, standing,
trusted, breaches) compared run by run. Usage: python3 -B gate_rows_compare.py <base-dir> <cand-dir>"""
import json, os, sys
b, c = sys.argv[1:3]
def idx(p):
    lines = open(p).read().splitlines(); head = lines[0].split('\t')
    return {tuple(l.split('\t')[:3]): dict(zip(head, l.split('\t'))) for l in lines[1:]}
ib, ic = idx(os.path.join(b, 'index_base.tsv')), idx(os.path.join(c, 'index_cand.tsv'))
assert ib.keys() == ic.keys()
cols = {}
for k in sorted(ib):
    d = [h for h in ib[k] if ib[k][h] != ic[k][h]]
    if d: cols.setdefault(','.join(d), []).append('__'.join(k))
for d, ks in cols.items():
    print('index columns differing [%s]: %d runs' % (d, len(ks)))
    for k in ks: print('   ', k)
rows = lambda p: {(r['case'], r['mode'], r['entry']): r for r in json.load(open(p))['runs']}
rb, rc = rows(os.path.join(b, 'result_part1_base.json')), rows(os.path.join(c, 'result_part1_cand.json'))
assert rb.keys() == rc.keys()
nd = [k for k in rb if any(rb[k].get(x) != rc[k].get(x) for x in ('outcome', 'quality', 'standing', 'trusted', 'breaches'))]
print('gate_check rows: %d per side; rows differing in outcome, quality, standing, trusted or breaches: %d' % (len(rb), len(nd)))
