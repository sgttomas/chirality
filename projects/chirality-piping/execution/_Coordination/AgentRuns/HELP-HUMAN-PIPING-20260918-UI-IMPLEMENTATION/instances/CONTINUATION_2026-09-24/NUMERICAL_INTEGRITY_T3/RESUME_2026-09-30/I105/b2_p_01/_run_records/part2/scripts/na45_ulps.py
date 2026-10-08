"""I105 (B2-P, NA4-5): on each successor document, every selected combination's displacement_magnitude rows
against its own translation rows: the retained magnitude vs RN64 of the exact 3-norm (expected equal), and
vs the ordinary route's formula, nested binary64 hypot (Python math.hypot on two arguments), in ulps.
Usage: na45_ulps.py <document.json>..."""
import json, math, sys
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec = 80
def rn64_sqrt(q):
    # RN64 of sqrt(q) for a nonnegative Fraction q: candidate by Decimal, then fix by exact comparison.
    if q == 0: return 0.0
    x = float(Decimal(q.numerator).sqrt() / Decimal(q.denominator).sqrt())
    for _ in range(4):
        lo, hi = math.nextafter(x, 0), math.nextafter(x, math.inf)
        # choose among lo, x, hi the one whose midpoint bracket contains sqrt(q)
        def below_mid(a, b):  # sqrt(q) < (a+b)/2 ?
            m = (Fraction(a) + Fraction(b)) / 2
            return q < m * m
        if not below_mid(lo, x) and below_mid(x, hi): return x
        x = lo if below_mid(lo, x) else hi
    return x
def ulps(a, b):
    if a == b: return 0
    n = 0; lo, hi = sorted((a, b))
    while lo < hi and n < 1000: lo = math.nextafter(lo, math.inf); n += 1
    return n
for path in sys.argv[1:]:
    doc = json.load(open(path)); s = doc.get('source', doc)
    body = s['retained_precision']['body']
    rows = {r['id']: r for r in s['results']}
    for c in body['combinations']:
        if c['disposition'] != 'retained_selected': continue
        cid = c['basis_ref']['ref_id']
        block = [rows[i] for i in c['result_ids']]
        by = {}
        for r in block: by.setdefault(r['entity_ref'], {})[r['kind']] = r['value']
        exact_eq = n = 0; worst = 0
        for node, k in by.items():
            if 'displacement_magnitude' not in k: continue
            x, y, z = (k[f'global_nodal_displacement_{a}'] for a in 'xyz')
            p = k['displacement_magnitude']
            q = Fraction(x) ** 2 + Fraction(y) ** 2 + Fraction(z) ** 2
            exact_eq += p == rn64_sqrt(q); n += 1
            worst = max(worst, ulps(p, math.hypot(math.hypot(x, y), z)))
        print(f"NA45 {path.rsplit('/',1)[-1]} {cid}: nodes={n} retained==RN64(exact)={exact_eq} max_ulps_vs_nested_hypot={worst}")
