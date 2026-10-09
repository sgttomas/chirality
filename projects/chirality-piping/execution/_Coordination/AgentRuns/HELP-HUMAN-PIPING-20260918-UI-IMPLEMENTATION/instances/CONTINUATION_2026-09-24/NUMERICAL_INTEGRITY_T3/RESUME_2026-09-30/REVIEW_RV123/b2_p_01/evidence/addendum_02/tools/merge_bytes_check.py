"""RV123 addendum 02: what J0a's merge did to each Direct publication, against b2's merge parent b
(7cc786285c). Every difference between b's and J0a's Direct output must be inherited from main's
ordinary change to the same input (the same path and the same before/after in the plain outputs),
or be a retained-precision hash. Retained rows (with `recovery_method`) must not change, unless the
new value is the correctly rounded norm of its components (FK's support_hypot -> norm3)."""
import json, struct, sys, os, math
from fractions import Fraction as F
B, J = sys.argv[1], sys.argv[2]
def bits(x): return struct.pack('>d', x).hex()
def flat(v, path, out):
    if isinstance(v, dict):
        if path == '.results' or path.endswith('.results'): pass
        for k, x in v.items(): flat(x, f'{path}.{k}', out)
    elif isinstance(v, list):
        for i, x in enumerate(v): flat(x, f'{path}[{i}]', out)
    elif isinstance(v, float): out[path] = 'f' + bits(v)
    else: out[path] = json.dumps(v)
def rows(doc): return {r['id']: r for r in doc.get('results', [])}
def nonrow(doc):
    d = {k: v for k, v in doc.items() if k not in ('results', 'retained_precision')}; out = {}; flat(d, '', out); return out
def rowflat(r):
    out = {}; flat({k: v for k, v in r.items()}, '', out); return out
names = sorted({f.split('.')[0] for f in os.listdir(J) if f.endswith('.direct.json')})
bad = []
for n in names:
    for mode in ('sparse_interactive', 'dense_scrutiny'):
        ld = lambda side, kind: json.load(open(f'{side}/{n}.{mode}.{kind}.json'))
        bd, jd, bp, jp = ld(B, 'direct'), ld(J, 'direct'), ld(B, 'plain'), ld(J, 'plain')
        if bd == jd: print(f'{n:24} {mode:18} identical'); continue
        notes = []
        # non-row fields
        fb, fj, pb, pj = nonrow(bd), nonrow(jd), nonrow(bp), nonrow(jp)
        for k in sorted(set(fb) | set(fj)):
            if fb.get(k) != fj.get(k):
                if pb.get(k) == fb.get(k) and pj.get(k) == fj.get(k): notes.append('inherited:' + k.split('[')[0])
                else: bad.append(f'{n} {mode} field {k}: {fb.get(k)} -> {fj.get(k)} (plain {pb.get(k)} -> {pj.get(k)})')
        # rows by id
        rb, rj, rpb, rpj = rows(bd), rows(jd), rows(bp), rows(jp)
        if list(rb) != list(rj): bad.append(f'{n} {mode}: row ids/order differ')
        moved_ord = moved_ret = 0
        for rid in rj:
            a, c = rb.get(rid), rj[rid]
            if a == c: continue
            if 'recovery_method' in c or 'recovery_method' in a:
                moved_ret += 1; bad.append(f'{n} {mode} retained row {rid}: {a.get("value")} -> {c.get("value")}')
            elif rpb.get(rid) == a and rpj.get(rid) == c: moved_ord += 1
            else: bad.append(f'{n} {mode} ordinary row {rid} not inherited')
        # receipt
        if ('retained_precision' in bd) != ('retained_precision' in jd): bad.append(f'{n} {mode}: successor presence differs')
        elif 'retained_precision' in bd:
            rb_, rj_ = json.loads(json.dumps(bd['retained_precision'])), json.loads(json.dumps(jd['retained_precision']))
            for r in (rb_, rj_): r.pop('receipt_sha256', None); r['body'].pop('publication_sha256', None)
            ob, oj = {}, {}; flat(rb_, '', ob); flat(rj_, '', oj)
            diffk = sorted(k for k in set(ob) | set(oj) if ob.get(k) != oj.get(k))
            if diffk: notes.append(f'receipt body differs at {len(diffk)} paths: ' + ', '.join(sorted({k.split("[")[0] for k in diffk}))[:300])
        print(f'{n:24} {mode:18} differs: ordinary rows inherited {moved_ord}, retained rows changed {moved_ret}; ' + '; '.join(sorted(set(notes)))[:400])
print('NOT EXPLAINED', len(bad)); [print('  ', x) for x in bad[:40]]
