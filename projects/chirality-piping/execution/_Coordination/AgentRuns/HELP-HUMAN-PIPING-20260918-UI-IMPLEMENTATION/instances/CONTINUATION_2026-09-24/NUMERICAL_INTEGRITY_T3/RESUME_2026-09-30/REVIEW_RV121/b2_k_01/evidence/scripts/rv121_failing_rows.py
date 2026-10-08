"""Item 8: why do C1, C4, C5 and C8 lose rows? Reads the kernel's B2K_ROW lines (argv[1]) as data."""
import sys, json, struct
from fractions import Fraction as F
def f64(h): return struct.unpack('>d', struct.pack('>Q', int(h, 16)))[0]
def tokval(t):
    if t == 'Z+': return F(0)
    s = -1 if t[0] == '-' else 1; h, e = t[1:].split('p')
    return s * int(h.ljust(256, '0'), 16) * F(2) ** (int(e) - 1023)
rows = [json.loads(l.split('B2K_ROW ', 1)[1]) for l in open(sys.argv[1]) if 'B2K_ROW ' in l]
out = []
for r in rows:
    if r['pass']: continue
    y = f64(r['raw']); n = F(f64(r['n'])); scale = F(f64(r['scale']))
    c = {'mm': F(1, 1000), 'MPa': F(10 ** 6)}.get(r['unit'], F(1))
    lo = min(tokval(r['k'][0]), tokval(r['g'][0])); hi = max(tokval(r['k'][1]), tokval(r['g'][1]))
    klo, khi, glo, ghi = (tokval(t) for t in r['k'] + r['g'])
    h = max(n - lo, hi - n); w = (hi - lo) / 2; mid = (lo + hi) / 2
    m = max(abs(n), scale)
    a_exact = m * F(2) ** -64 + m * F(2) ** -85 + abs(n) * F(2) ** -53 + F(2) ** -1074
    ulp = lambda x: F(2) ** (int(abs(x)).bit_length() - 53) if abs(x) >= 1 else None
    # what a point publication at the exact midpoint would need, and the publication's own errors
    y_exact_unit = mid / c                 # the midpoint in the row's unit
    rn_unit = F(float(y_exact_unit))       # RN64 in the unit (the projection's last step, from the exact midpoint)
    n_from_rn = F(float(rn_unit * c))      # binary64 normalization y*1e6 (or /1000)
    out.append({'combination': r['combination'], 'key': r['key'], 'unit': r['unit'], 'class': r['class'],
        'predicates': r['predicates'],
        'h_over_allowance': float(h / a_exact),
        'half_width_over_allowance': float(w / a_exact),
        'k_lane_width_rel': float((khi - klo) / abs(mid)) if mid else None,
        'g_lane_width_rel': float((ghi - glo) / abs(mid)) if mid else None,
        'lane_offset_rel': float((max(klo, glo) - min(khi, ghi)) / abs(mid)) if mid else None,
        'publication_error_over_allowance': float(abs(n - mid) / a_exact),
        'n_equals_rn_of_midpoint_then_normalized': n == n_from_rn,
        'scale_over_n': float(scale / abs(n)) if n else None})
print(json.dumps(out, indent=1))
