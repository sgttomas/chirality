"""RV123 addendum 02: J0a's B2-P re-pins. For every dumped witness successor, compare J0a (new) with
72b3e5d9ea (old) structurally: every row by id (kind, entity, unit, metadata, value bits), every other
field of the publication, and the receipt body with its two hashes removed. A moved row must be a
magnitude row whose new value is RN64 of the exact 3-norm of the same row block's three component
rows (decided exactly) and whose old value is not."""
import json, sys, struct, math, glob, os
from fractions import Fraction as F
OLD, NEW = sys.argv[1], sys.argv[2]
def bits(x): return struct.pack('>d', x).hex()
def rn_sqrt(S):
    if S == 0: return 0.0
    y = math.sqrt(float(S))
    for c in sorted({math.nextafter(math.nextafter(y, 0), 0), math.nextafter(y, 0), y, math.nextafter(y, math.inf), math.nextafter(math.nextafter(y, math.inf), math.inf)}):
        if c <= 0: continue
        lo = (F(c) + F(math.nextafter(c, 0))) / 2; hi = (F(c) + F(math.nextafter(c, math.inf))) / 2
        if lo * lo < S < hi * hi: return c
        if (lo * lo == S or hi * hi == S) and struct.unpack('>Q', struct.pack('>d', c))[0] % 2 == 0: return c
    raise AssertionError
def norm(vs): return rn_sqrt(sum(F(v) * F(v) for v in vs))
def components(rows, row):
    ent, basis = row['entity_ref'], (row['basis_ref']['ref_type'], row['basis_ref']['ref_id'])
    same = [r for r in rows if r['entity_ref'] == ent and (r['basis_ref']['ref_type'], r['basis_ref']['ref_id']) == basis]
    if row['kind'] == 'displacement_magnitude':
        want = ['global_nodal_displacement_x', 'global_nodal_displacement_y', 'global_nodal_displacement_z']
        return [next(r['value'] for r in same if r['kind'] == k) for k in want]
    comps = ['Fx', 'Fy', 'Fz'] if 'force' in row['kind'] else ['Mx', 'My', 'Mz']
    return [next(r['value'] for r in same if r['kind'] == 'support_reaction_component_v2' and (r.get('metadata') or {}).get('component') == c) for c in comps]
total_moved, problems = 0, []
for path in sorted(glob.glob(f'{NEW}/*.successor.json')):
    name = os.path.basename(path).replace('.successor.json', '')
    old_path = f'{OLD}/{os.path.basename(path)}'
    if not os.path.exists(old_path): print(name, 'no old dump'); continue
    o, n = json.load(open(old_path))['source'], json.load(open(path))['source']
    orow = {r['id']: r for r in o['results']}; nrow = {r['id']: r for r in n['results']}
    if [r['id'] for r in o['results']] != [r['id'] for r in n['results']]: problems.append(f'{name}: row ids/order differ')
    moved = []
    for rid, r in nrow.items():
        a = orow.get(rid)
        if a is None: continue
        ka = {k: v for k, v in a.items() if k != 'value'}; kn = {k: v for k, v in r.items() if k != 'value'}
        if ka != kn: problems.append(f'{name}: {rid} non-value fields differ')
        if bits(a['value']) != bits(r['value']):
            comps = components(n['results'], r); cr = norm(comps)
            ok = bits(r['value']) == bits(cr) and bits(a['value']) != bits(cr)
            ulps = abs(struct.unpack('>q', struct.pack('>d', r['value']))[0] - struct.unpack('>q', struct.pack('>d', a['value']))[0])
            same_comps = components(o['results'], a) == comps
            moved.append(f"{rid} [{r['kind']}, {r['basis_ref']['ref_id']}, recovery_method={'recovery_method' in r}] {a['value'].hex()} -> {r['value'].hex()} ({ulps} ulp) new==CR norm:{bits(r['value']) == bits(cr)} old==CR:{bits(a['value']) == bits(cr)} components unchanged:{same_comps}")
            if not (ok and same_comps and ulps == 1 and 'recovery_method' not in r): problems.append(f'{name}: {rid} move not the norm move')
    po = {k: v for k, v in o.items() if k not in ('results', 'retained_precision')}; pn = {k: v for k, v in n.items() if k not in ('results', 'retained_precision')}
    if po != pn: problems.append(f'{name}: publication fields other than results differ: {sorted(k for k in set(po) | set(pn) if po.get(k) != pn.get(k))}')
    ro, rn = json.loads(json.dumps(o['retained_precision'])), json.loads(json.dumps(n['retained_precision']))
    for r in (ro, rn): r.pop('receipt_sha256', None); r['body'].pop('publication_sha256', None)
    body_same = ro == rn
    if not body_same: problems.append(f'{name}: receipt differs beyond its two hashes')
    total_moved += len(moved)
    print(f"{name}: moved {len(moved)}; receipt beyond hashes identical: {body_same}; publication hash changed: {o['retained_precision']['body']['publication_sha256'] != n['retained_precision']['body']['publication_sha256']}")
    for m in moved: print('   ', m)
print('TOTAL moved rows', total_moved); print('PROBLEMS', len(problems)); [print('  ', p) for p in problems]
