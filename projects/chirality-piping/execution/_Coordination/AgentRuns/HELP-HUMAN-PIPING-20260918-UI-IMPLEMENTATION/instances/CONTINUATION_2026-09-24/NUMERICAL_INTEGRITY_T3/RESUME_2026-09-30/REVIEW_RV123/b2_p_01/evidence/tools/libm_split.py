"""RV123 round 2: libm_check split into retained rows (recovery_method present) and ordinary non-range rows."""

import json, math, sys, struct
from fractions import Fraction as F
def bits(x): return struct.pack('>d', x).hex()
def rn_sqrt(S):
    """RN64 (ties to even) of sqrt(S) for a non-negative Fraction S, decided exactly."""
    if S == 0: return 0.0, None
    y = math.sqrt(float(S)) if float(S) not in (0.0, math.inf) else float(F(math.isqrt(int(S * 2**2200)), 2**1100))
    best = None
    for c in {math.nextafter(math.nextafter(y, 0), 0), math.nextafter(y, 0), y, math.nextafter(y, math.inf), math.nextafter(math.nextafter(y, math.inf), math.inf)}:
        if c <= 0 or not math.isfinite(c): continue
        lo = (F(c) + F(math.nextafter(c, 0))) / 2; hi = (F(c) + F(math.nextafter(c, math.inf))) / 2
        if lo * lo <= S <= hi * hi:
            if lo * lo == S or hi * hi == S:
                if struct.unpack('>Q', struct.pack('>d', c))[0] % 2: continue
            best = c
    assert best is not None
    # distance of sqrt(S) from the nearest midpoint, in ulps of best (0.5 means far from any midpoint)
    from decimal import Decimal, getcontext
    getcontext().prec = 120
    exact = (Decimal(S.numerator) / Decimal(S.denominator)).sqrt()
    ulp = Decimal(math.nextafter(best, math.inf)) - Decimal(best)
    d = abs((exact - Decimal(best)) / ulp)
    return best, float(abs(Decimal('0.5') - d))
def cr_hypot(a, b):
    v, m = rn_sqrt(F(a) * F(a) + F(b) * F(b)); return v, m

def analyse(doc, label):
    rows = doc['source']['results']
    by = {}
    for r in rows: by.setdefault((r['basis_ref']['ref_type'], r['basis_ref']['ref_id'], r['entity_ref']), []).append(r)
    st = {True: [0, 0, 1.0], False: [0, 0, 1.0]}  # retained?: [magnitudes, ne_cr, min margin]
    for (t, ref, ent), rs in by.items():
        kinds = {}
        for r in rs: kinds.setdefault(r['kind'], {})[(r.get('metadata') or {}).get('component')] = r
        for mag_kind, comps in [('support_reaction_force_magnitude_v2', ['Fx', 'Fy', 'Fz']), ('support_reaction_moment_magnitude_v2', ['Mx', 'My', 'Mz'])]:
            if mag_kind not in kinds: continue
            if t == 'combination' and 'range' in ref: continue
            row = list(kinds[mag_kind].values())[0]; p = row['value']
            retained = 'recovery_method' in row
            v = [kinds['support_reaction_component_v2'][c]['value'] for c in comps]
            xy, m1 = cr_hypot(v[0], v[1]); cr, m2 = cr_hypot(xy, v[2])
            s = st[retained]; s[0] += 1
            if bits(p) != bits(cr): s[1] += 1
            for m in (m1, m2):
                if m is not None: s[2] = min(s[2], m)
    print(label, 'retained', st[True], 'ordinary(non-range)', st[False])
for path in sys.argv[1:]:
    analyse(json.load(open(path)), path.rsplit('/', 1)[-1])
