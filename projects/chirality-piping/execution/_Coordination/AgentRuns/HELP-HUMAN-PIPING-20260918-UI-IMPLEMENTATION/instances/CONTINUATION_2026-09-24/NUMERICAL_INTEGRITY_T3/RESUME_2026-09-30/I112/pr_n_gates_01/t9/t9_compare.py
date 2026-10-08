#!/usr/bin/env python3
"""I112 PR-N T9 comparison (new; I61 compared by hand). Base B 7eae707bb7 against candidate C 8dd64c1835.

1. Output sets: sha_base.txt vs sha_cand.txt (core, fixtures, validation) and extra_sha_*.txt (F1b's extra corpus).
2. Every differing output is put through normdiff.compare (the brief's acceptance rule: byte-exact lexeme accounting, each
   difference a <= 1-ulp published magnitude whose candidate value is the exactly computed correctly rounded norm of the same
   output's own components; any other difference is OTHER, a stop).
3. Committed raw fixtures: for every request <stem>.request.json in the tree with a committed <stem>-<mode>.raw.json beside it,
   the base and candidate outputs are compared byte for byte with the committed file (as I109's compare_regen.py did). The
   committed file is the pretty envelope followed by one newline; the harness writes no final newline, so the comparison is
   output + b'\\n' == committed bytes.
Usage: python3 -B t9_compare.py <t9-dir> <tree_base> <tree_cand> <out.json>
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import normdiff as N  # noqa: E402

t9, tree_b, tree_c, out_path = sys.argv[1:5]


def shas(p):
    d = {}
    for line in open(p):
        h, name = line.rstrip('\n').split('  ', 1)
        d[name] = h
    return d


report = dict(sets={}, differing=[], raw_fixtures=[])
verdict_ok = True
for label, lb, lc, db, dc in (('main', 'sha_base.txt', 'sha_cand.txt', 'out_base', 'out_cand'),
                               ('extra', 'extra_sha_base.txt', 'extra_sha_cand.txt', 'extra_base', 'extra_cand')):
    b, c = shas(os.path.join(t9, lb)), shas(os.path.join(t9, lc))
    common = sorted(set(b) & set(c))
    same = [n for n in common if b[n] == c[n]]
    diff = [n for n in common if b[n] != c[n]]
    report['sets'][label] = dict(base=len(b), cand=len(c), common=len(common), identical=len(same), differing=len(diff),
                                 only_base=sorted(set(b) - set(c)), only_cand=sorted(set(c) - set(b)))
    if set(b) != set(c):
        verdict_ok = False
    for n in diff:
        tb = open(os.path.join(t9, db, n), encoding='utf-8').read()
        tc = open(os.path.join(t9, dc, n), encoding='utf-8').read()
        v, items = N.compare(tb, tc)
        report['differing'].append(dict(set=label, output=n.lstrip('./'), verdict=v, items=items,
                                        base_sha256=b[n], cand_sha256=c[n]))
        if v != 'norm_only' or any(it.get('hash_field') for it in items):
            verdict_ok = False  # hash fields would need their own verification; none expected in T9's pretty envelopes

# committed raw fixtures beside requests
for root in ('core', 'fixtures', 'validation'):
    base_root = os.path.join(tree_c, 'projects/chirality-piping', root)
    for dp, dn, fn in os.walk(base_root):
        for f in sorted(fn):
            if not f.endswith('.request.json'):
                continue
            rel = os.path.relpath(os.path.join(dp, f), base_root)
            stem = os.path.join(dp, f[:-len('.request.json')])
            for mode in ('sparse_interactive', 'dense_scrutiny'):
                raw_c = stem + '-%s.raw.json' % mode
                if not os.path.exists(raw_c):
                    continue
                raw_b = raw_c.replace(tree_c, tree_b, 1)
                outname = '%s.%s.out' % (rel.replace('/', '__'), mode)
                ob = open(os.path.join(t9, 'out_base', root, outname), 'rb').read()
                oc = open(os.path.join(t9, 'out_cand', root, outname), 'rb').read()
                rb = open(raw_b, 'rb').read() if os.path.exists(raw_b) else None
                rc = open(raw_c, 'rb').read()
                # the committed raw fixture is the pretty envelope plus one final newline (the harness writes none)
                report['raw_fixtures'].append(dict(fixture=os.path.relpath(raw_c, os.path.join(tree_c, 'projects/chirality-piping')),
                                                   raw_same_in_both_trees=(rb == rc),
                                                   base_output_equals_raw=(ob + b'\n' == rb), cand_output_equals_raw=(oc + b'\n' == rc),
                                                   raw_ends_with_one_newline=(rc.endswith(b'}\n'))))
rf = report['raw_fixtures']
report['raw_summary'] = dict(fixtures=len(rf), cand_reproduces=sum(r['cand_output_equals_raw'] for r in rf),
                             base_reproduces=sum(r['base_output_equals_raw'] for r in rf),
                             base_misses=[r['fixture'] for r in rf if not r['base_output_equals_raw']],
                             cand_misses=[r['fixture'] for r in rf if not r['cand_output_equals_raw']])
if report['raw_summary']['cand_misses']:
    verdict_ok = False
report['RESULT'] = 'PASS' if verdict_ok else 'STOP'
json.dump(report, open(out_path, 'w'), indent=1, ensure_ascii=False)

# text summary
for label, s in report['sets'].items():
    print(f"{label}: base {s['base']} cand {s['cand']} common {s['common']} identical {s['identical']} differing {s['differing']} "
          f"only_base {len(s['only_base'])} only_cand {len(s['only_cand'])}")
print('differing outputs:')
for d in report['differing']:
    print(f"  [{d['set']}] {d['output']}: {d['verdict']}")
    for it in d['items']:
        if it.get('hash_field'):
            print(f"      HASH {it['path']}")
        elif it.get('OTHER'):
            print(f"      OTHER {it}")
        else:
            print(f"      {it['kind']} {it['id']} ({it['unit']}): {it['base']} -> {it['cand']}, {it['ulps']} ulp; "
                  f"CR norm of {it['components']} = {it['cr_norm']}: cand {'equals' if it['norm_ok'] else 'DIFFERS'}; base is CR: {it['base_is_cr']}")
r = report['raw_summary']
print(f"committed raw fixtures beside requests: {r['fixtures']}; candidate reproduces {r['cand_reproduces']}; base reproduces {r['base_reproduces']}")
print('  base misses:', r['base_misses'])
print('  candidate misses:', r['cand_misses'])
print('RESULT', report['RESULT'])
