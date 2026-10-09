"""I105 J0a: for each re-pinned successor, every published row whose value moved from the old successor to the new
one, and an exact check that the new value is the correctly rounded norm (RN64 of the exact sqrt of the exact sum of
squares) of its own components in the new successor; the old value's distance from it in ulps is reported (the old
value came from the platform libm's nested hypot, which Python cannot reproduce).
Usage: moved_rows.py <old.json> <new.json> [label]  (documents with a "source" member, or bare successors)."""
import json, math, sys
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec = 120

def rn64_sqrt(q):
    if q == 0:
        return 0.0
    x = float(Decimal(q.numerator).sqrt() / Decimal(q.denominator).sqrt())
    for _ in range(8):
        lo, hi = math.nextafter(x, 0), math.nextafter(x, math.inf)
        below = lambda a, b: q < ((Fraction(a) + Fraction(b)) / 2) ** 2
        if not below(lo, x) and below(x, hi):
            return x
        x = lo if below(lo, x) else hi
    raise SystemExit('no convergence')

def cr_norm(vals):
    return rn64_sqrt(sum(Fraction(v) ** 2 for v in vals))

def nested_hypot(vals):
    r = math.hypot(vals[0], vals[1])
    for v in vals[2:]:
        r = math.hypot(r, v)
    return r

def load(p):
    d = json.load(open(p))
    return d.get('source', d)

old, new = load(sys.argv[1]), load(sys.argv[2])
label = sys.argv[3] if len(sys.argv) > 3 else sys.argv[2].rsplit('/', 1)[-1]
o = {r['id']: r for r in old['results']}
n = {r['id']: r for r in new['results']}
assert set(o) == set(n), f'{label}: row ids differ'

def comps(rows, r):
    basis = json.dumps(r.get('basis_ref'), sort_keys=True)
    same = [x for x in rows if x['entity_ref'] == r['entity_ref'] and json.dumps(x.get('basis_ref'), sort_keys=True) == basis]
    if r['kind'] == 'displacement_magnitude':
        out = []
        for k in ('x', 'y', 'z'):
            c = [x for x in same if x['kind'] == f'global_nodal_displacement_{k}']
            assert len(c) == 1, (label, r['id'], k, len(c))
            out.append(c[0]['value'])
        return out
    if r['kind'] in ('support_reaction_force_magnitude_v2', 'support_reaction_moment_magnitude_v2'):
        names = ['Fx', 'Fy', 'Fz'] if 'force' in r['kind'] else ['Mx', 'My', 'Mz']
        out = []
        for c in names:
            m = [x for x in same if x['kind'] == 'support_reaction_component_v2' and (x.get('metadata') or {}).get('component') == c]
            assert len(m) == 1, (label, r['id'], c, len(m))
            out.append(m[0]['value'])
        return out
    return None

rows = new['results']
moved = [i for i in n if o[i]['value'] != n[i]['value'] or json.dumps(o[i], sort_keys=True) != json.dumps(n[i], sort_keys=True)]
ok = True
for i in sorted(moved):
    a, b = o[i], n[i]
    other = sorted(k for k in set(a) | set(b) if k != 'value' and a.get(k) != b.get(k))
    c = comps(rows, b)
    if c is None or other:
        ok = False
        print(f'MOVED {label} {i} kind={b["kind"]} UNCHECKED other_fields={other}')
        continue
    cr = cr_norm(c)
    good = b['value'] == cr
    import struct
    ulps = abs(struct.unpack('<q', struct.pack('<d', a['value']))[0] - struct.unpack('<q', struct.pack('<d', b['value']))[0])
    ok &= good
    print(f'MOVED {label} {i} kind={b["kind"]} basis={b.get("basis_ref",{}).get("ref_type")}:{b.get("basis_ref",{}).get("ref_id")} '
          f'old={a["value"].hex()} new={b["value"].hex()} cr_norm={cr.hex()} new==cr_norm:{good} old_to_new_ulps={ulps}')
# every magnitude row of the new successor, moved or not: the correctly rounded norm, or a retained value
allmag = [r for r in rows if comps(rows, r) is not None]
bad = [r['id'] for r in allmag if r['value'] != cr_norm(comps(rows, r)) and not r.get('recovery_method')]
print(f'SUMMARY {label} moved={len(moved)} all_checked={ok} magnitude_rows={len(allmag)} ordinary_magnitudes_not_cr={len(bad)} {bad[:5]}')
sys.exit(0 if ok and not bad else 1)
