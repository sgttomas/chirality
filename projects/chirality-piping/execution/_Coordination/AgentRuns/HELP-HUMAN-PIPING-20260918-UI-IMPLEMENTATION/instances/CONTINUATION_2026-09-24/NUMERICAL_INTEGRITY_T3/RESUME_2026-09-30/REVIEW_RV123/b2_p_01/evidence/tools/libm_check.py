"""RV123 round 2 (platform note): for every published magnitude in the combination successor
fixtures, compare the published bits with (a) this host's nested f64 hypot of the published
components, (b) the correctly rounded nested hypot (each hypot rounded once from its exact value)
and (c) RN64 of the exact 3-norm; and measure each hypot step's distance from a rounding midpoint."""
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
    s = doc['source']; rows = s['results']
    by = {}
    for r in rows: by.setdefault((r['basis_ref']['ref_type'], r['basis_ref']['ref_id'], r['entity_ref']), []).append(r)
    stats = {'combination_displacement_magnitudes': 0, 'magnitudes': 0, 'libm_ne_cr': 0, 'min_midpoint_margin': 1.0, 'exact_norm_ne_published': 0}
    for (t, ref, ent), rs in by.items():
        kinds = {}
        for r in rs:
            comp = (r.get('metadata') or {}).get('component')
            kinds.setdefault(r['kind'], {})[comp] = r
        for mag_kind, comp_kind, comps in [('support_reaction_force_magnitude_v2', 'support_reaction_component_v2', ['Fx', 'Fy', 'Fz']),
                                           ('support_reaction_moment_magnitude_v2', 'support_reaction_component_v2', ['Mx', 'My', 'Mz'])]:
            if mag_kind not in kinds: continue
            p = list(kinds[mag_kind].values())[0]['value']
            v = [kinds[comp_kind][c]['value'] for c in comps]
            host = math.hypot(math.hypot(v[0], v[1]), v[2])
            xy, m1 = cr_hypot(v[0], v[1]); cr, m2 = cr_hypot(xy, v[2])
            stats['magnitudes'] += 1
            if bits(p) != bits(cr): stats['libm_ne_cr'] += 1; print(f'  {label} {t}:{ref} {ent} {mag_kind}: published {bits(p)} cr_nested {bits(cr)} host {bits(host)}')
            for m in (m1, m2):
                if m is not None: stats['min_midpoint_margin'] = min(stats['min_midpoint_margin'], m)
        if 'displacement_magnitude' in kinds and t == 'combination':
            p = list(kinds['displacement_magnitude'].values())[0]['value']
            xyz = [list(kinds[k].values())[0]['value'] for k in ['global_nodal_displacement_x', 'global_nodal_displacement_y', 'global_nodal_displacement_z']]
            ex, _ = rn_sqrt(sum(F(x) * F(x) for x in xyz)); stats['combination_displacement_magnitudes'] += 1
            if bits(ex) != bits(p): stats['exact_norm_ne_published'] += 1; print(f'  {label} combination {ent} displacement_magnitude published {bits(p)} exact-norm {bits(ex)}')
    print(label, stats)
for path in sys.argv[1:]:
    analyse(json.load(open(path)), path.rsplit('/', 1)[-1])
