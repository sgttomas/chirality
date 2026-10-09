#!/usr/bin/env python3
"""I112 round 2: U3 T9 comparison under the U3 brief's rule (new). Base B ba500defa4 against candidate C 8a12de28db.

1. Output sets (core, fixtures, validation; F1b's extra corpus): common, removed (base only), added (candidate only).
2. Every differing common output is classified by u3diff.classify with its input model (read from the candidate tree; the
   input's bytes are compared with the base tree's): declared / declared_t2 / refusal / OTHER. A refusal also lists which
   leaves differ (normdiff's lexeme accounting, when both sides are JSON of the same shape).
3. Removed outputs: the input is checked against the base and candidate trees and CHANGE_RECORD §4.
4. Added outputs: the input is new in C; its outcome and its relation to the committed demo results are reported.
5. Committed raw fixtures beside requests (<stem>-<mode>.raw.json, or <name>-<mode>.raw.json beside <name>-<mode>.request.json
   for that mode): base output vs the base tree's file, candidate output vs the candidate tree's file (pretty envelope plus one
   final newline).
Usage: python3 -B t9_u3_compare.py <t9-dir> <tree_base> <tree_cand> <out.json>
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
import normdiff as N  # noqa: E402
import u3diff as U  # noqa: E402

t9, tree_b, tree_c, out_path = sys.argv[1:5]
P = 'projects/chirality-piping'


def shas(p):
    d = {}
    for line in open(p):
        h, name = line.rstrip('\n').split('  ', 1)
        d[name.lstrip('./')] = h
    return d


def input_of(name, label):
    """(relative input path, mode) of an output name; inputs live under core/, fixtures/, validation/ or the extra corpus."""
    stem, mode, _ = name.rsplit('.', 2)
    if label == 'extra':
        return 'EXTRA/' + stem, mode
    root, rest = name.split('/', 1)
    return root + '/' + rest.rsplit('.', 2)[0].replace('__', '/'), mode


def read_input(rel, tree):
    if rel.startswith('EXTRA/'):
        p = os.path.join(t9, '..', 'extra_corpus', rel[6:])
    else:
        p = os.path.join(tree, P, rel)
    return open(p, 'rb').read() if os.path.exists(p) else None


def model_of(raw):
    v = json.loads(raw)
    return v['model'] if isinstance(v.get('model'), dict) else v


def leaf_diff(tb, tc):
    try:
        lb, lc = N.lex(tb), N.lex(tc)
    except Exception:
        return 'not JSON'
    if len(lb) != len(lc):
        return 'different shape (%d vs %d lexemes)' % (len(lb), len(lc))
    lv = list(N.leaves(N.parse(tb)))
    out, vi = [], 0
    for xb, xc in zip(lb, lc):
        isv = xb[0] in ('s', 'n', 'l')
        if xb != xc:
            out.append('/'.join(map(str, lv[vi][0])) if isv else 'non-value lexeme')
        if isv:
            vi += 1
    return out


def same(out, raw):
    """'bytes' when the committed file is the output with or without one final newline; 'parsed' when it is the same JSON
    document (string-exact numbers) in another key order (I110: 10 of the 12 source-block raws are sorted-key serializations);
    False otherwise."""
    if raw in (out, out + b'\n'):
        return 'bytes'
    try:
        if json.loads(raw, parse_float=str, parse_int=str) == json.loads(out, parse_float=str, parse_int=str):
            return 'parsed'
    except Exception:
        pass
    return False


report = dict(sets={}, differing=[], removed=[], added=[], raw_fixtures=[])
ok = True
work = os.path.join(t9, 'tmp')
os.makedirs(work, exist_ok=True)
for label, lb, lc, db, dc in (('main', 'sha_base.txt', 'sha_cand.txt', 'out_base', 'out_cand'),
                               ('extra', 'extra_sha_base.txt', 'extra_sha_cand.txt', 'extra_base', 'extra_cand')):
    b, c = shas(os.path.join(t9, lb)), shas(os.path.join(t9, lc))
    common = sorted(set(b) & set(c))
    diff = [n for n in common if b[n] != c[n]]
    report['sets'][label] = dict(base=len(b), cand=len(c), identical=len(common) - len(diff), differing=len(diff),
                                 removed=sorted(set(b) - set(c)), added=sorted(set(c) - set(b)))
    for n in diff:
        rel, mode = input_of(n, label)
        ib, ic = read_input(rel, tree_b), read_input(rel, tree_c)
        tb = open(os.path.join(t9, db, n), encoding='utf-8').read()
        tc = open(os.path.join(t9, dc, n), encoding='utf-8').read()
        cls, info = U.classify(tb, tc, model_of(ic) if ic else None, work)
        row = dict(set=label, output=n, input=rel, mode=mode, input_same_in_both_trees=(ib == ic), cls=cls, info=info)
        if cls == 'refusal':
            row['leaves_differing'] = leaf_diff(tb, tc)
        report['differing'].append(row)
        ok &= cls in ('declared', 'declared_t2', 'refusal') and ib == ic
    for n in sorted(set(b) - set(c)):
        rel, mode = input_of(n, label)
        report['removed'].append(dict(set=label, output=n, input=rel, in_base_tree=read_input(rel, tree_b) is not None,
                                      in_cand_tree=read_input(rel, tree_c) is not None))
        ok = False  # decided against CHANGE_RECORD §4 by hand in the RETURN
    for n in sorted(set(c) - set(b)):
        rel, mode = input_of(n, label)
        tc = open(os.path.join(t9, dc, n), encoding='utf-8').read()
        try:
            d = json.loads(tc)
            outcome = dict(status=(d.get('status') or {}).get('mechanics'), quality=(d.get('numerical_quality') or {}).get('status'),
                           results=len(d.get('results') or []),
                           blocking=sorted({x['code'] for x in d.get('diagnostics', []) if x.get('severity') == 'blocking'}))
        except Exception:
            outcome = dict(text=tc[:120])
        tie = None
        if rel == 'fixtures/product_preview/invented_demo_model.json':
            # the committed demo results (I114's generator record demo_fixture_generation.json names this model)
            short = {'sparse_interactive': 'sparse', 'dense_scrutiny': 'dense'}[mode]
            committed = os.path.join(tree_c, P, 'fixtures/product_preview/invented_demo_result_preview_physics_1_%s.json' % short)
            tie = dict(committed='fixtures/product_preview/invented_demo_result_preview_physics_1_%s.json' % short,
                       output_plus_newline_equals_committed=(tc.encode() + b'\n' == open(committed, 'rb').read()))
        report['added'].append(dict(set=label, output=n, input=rel, in_base_tree=read_input(rel, tree_b) is not None,
                                    in_cand_tree=read_input(rel, tree_c) is not None, outcome=outcome, tie=tie))
for root in ('core', 'fixtures', 'validation'):
    for dp, dn, fn in os.walk(os.path.join(tree_c, P, root)):
        for f in sorted(fn):
            if not f.endswith('.request.json'):
                continue
            rel = os.path.relpath(os.path.join(dp, f), os.path.join(tree_c, P, root))
            for mode in ('sparse_interactive', 'dense_scrutiny'):
                stem = f[:-len('.request.json')]
                raw_c = os.path.join(dp, stem + '-%s.raw.json' % mode)
                if not os.path.exists(raw_c):
                    # the source-block convention: <name>-<mode>.request.json beside <name>-<mode>.raw.json, for that mode
                    raw_c = os.path.join(dp, stem + '.raw.json')
                    if not (stem.endswith('-' + mode) and os.path.exists(raw_c)):
                        continue
                raw_b = raw_c.replace(tree_c, tree_b, 1)
                outname = '%s.%s.out' % (rel.replace('/', '__'), mode)
                ob = open(os.path.join(t9, 'out_base', root, outname), 'rb').read()
                oc = open(os.path.join(t9, 'out_cand', root, outname), 'rb').read()
                rb = open(raw_b, 'rb').read()
                rc = open(raw_c, 'rb').read()
                report['raw_fixtures'].append(dict(fixture=os.path.relpath(raw_c, os.path.join(tree_c, P)), raw_changed_by_c=(rb != rc),
                                                   base_reproduces_base_tree=same(ob, rb), cand_reproduces_cand_tree=same(oc, rc)))
rf = report['raw_fixtures']
report['raw_summary'] = dict(fixtures=len(rf), changed_by_c=sum(r['raw_changed_by_c'] for r in rf),
                             base_reproduces=sum(bool(r['base_reproduces_base_tree']) for r in rf),
                             cand_reproduces=sum(bool(r['cand_reproduces_cand_tree']) for r in rf),
                             by_form={'%s/%s' % k: sum(1 for r in rf if (r['base_reproduces_base_tree'], r['cand_reproduces_cand_tree']) == k)
                                      for k in {(r['base_reproduces_base_tree'], r['cand_reproduces_cand_tree']) for r in rf}})
report['RESULT_DIFFERING'] = 'PASS' if ok else 'SEE REMOVED/ADDED OR STOP'
json.dump(report, open(out_path, 'w'), indent=1, ensure_ascii=False)
for label, s in report['sets'].items():
    print('%s: base %d cand %d identical %d differing %d removed %d added %d' % (label, s['base'], s['cand'], s['identical'],
          s['differing'], len(s['removed']), len(s['added'])))
for r in report['differing']:
    i = r['info']
    extra = ''
    if r['cls'] == 'refusal':
        extra = '; refusal %s; base %s %s results %s; leaves differing %s' % (
            [(c, t) for c, _, t in i['refusal']], i.get('base_status'), i.get('base_blocking_codes'), i.get('base_results'),
            r['leaves_differing'] if isinstance(r['leaves_differing'], str) else sorted(set(r['leaves_differing'])))
    elif r['cls'] == 'declared_t2':
        extra = '; digests %s -> %s (rule on candidate equal: yes; rule on normalized = base)' % (
            [x[:12] for x in i['rule_on_normalized']], [x[:12] for x in i['cand_digests']])
    print('  [%s] %s: %s %s%s%s' % (r['set'], r['output'], r['cls'], i.get('declared', ''), extra,
          '' if r['input_same_in_both_trees'] else ' INPUT CHANGED'))
for r in report['removed']:
    print('  removed:', r)
for r in report['added']:
    print('  added:', r)
s = report['raw_summary']
print('committed raw fixtures beside requests: %d (%d changed by C); base reproduces its tree %d; candidate reproduces its tree %d; '
      '(base, candidate) forms %s' % (s['fixtures'], s['changed_by_c'], s['base_reproduces'], s['cand_reproduces'],
                                      s['by_form']))
print('RESULT (differing common outputs all designed or declared, inputs unchanged):', report['RESULT_DIFFERING'])
