#!/usr/bin/env python3
"""I112 T9 cross-check (new): every differing T9 output through normdiff2 (the structure walker used for the gate), which must
give the same moves as t9_compare.py's normdiff, and which also compares each base value with this host's libm hypot chain of
the same components. Usage: python3 -B t9_libm_check.py <t9-dir> <normdiff-dir>"""
import json, os, sys
t9, nd = sys.argv[1:3]
sys.path.insert(0, nd)
import normdiff2 as N2
r = json.load(open(os.path.join(t9, 't9_compare.json')))
n = same = libm = cr = 0
for d in r['differing']:
    sub = {'main': ('out_base', 'out_cand'), 'extra': ('extra_base', 'extra_cand')}[d['set']]
    v, items = N2.compare(open(os.path.join(t9, sub[0], d['output']), 'rb').read(), open(os.path.join(t9, sub[1], d['output']), 'rb').read())
    a = [(i['id'], i['base'], i['cand'], i['norm_ok'], i['cr_norm']) for i in items]
    b = [(i['id'], i['base'], i['cand'], i['norm_ok'], i['cr_norm']) for i in d['items']]
    same += (a == b and v == d['verdict'])
    for i in items:
        n += 1; libm += bool(i['base_is_libm_chain']); cr += bool(i['norm_ok'])
    print('%s %s: %s; same moves as normdiff: %s; base values = libm hypot chain: %s' % (d['set'], d['output'], v, a == b,
          [i['base_is_libm_chain'] for i in items]))
print('outputs %d, agreeing %d; moved values %d, candidate CR %d, base = libm hypot chain %d' % (len(r['differing']), same, n, cr, libm))
