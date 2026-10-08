"""RV126: an independent exact oracle for PR-N's correctly rounded norm.

Two independent exact checks per result (Python integers only, no floating-point arithmetic in
the decision):
  A. compute:  RN(sqrt(S)) to binary64 (ties to even, subnormal grid, overflow at 2^1024 - 2^970)
               from an integer square root, and compare its bits with the implementation's;
  B. verify:   the implementation's r satisfies D^2 <= S <= U^2 at its own lower and upper
               midpoints D and U, with the tie rule (an exact tie keeps r only if r is even;
               a tie at U for r = MAX goes to +inf).
Special values follow C Annex F's hypot (independently re-stated here): any infinity gives +inf
(even with a NaN); otherwise any NaN gives NaN; zeros give +0.

Also reports the closeness of each finite exact norm to the nearest rounding midpoint (in ulps,
from an integer square root with 96 guard bits), and, for information only, how often the
platform's libm hypot (and its chain) differs from the correctly rounded value.

Usage: check.py TRIPLES DRIVER_OUT [WORKERS]   (TRIPLES.cat holds one category byte per triple)
"""
import json
import math
import struct
import sys
from multiprocessing import Pool

MANT = (1 << 52) - 1
INF_BITS = 0x7FF0000000000000
TH_NUM = (1 << 54) - 1  # overflow threshold = TH_NUM * 2^970
CATS = ['special', 'rbits', 'compar', 'thresh', 'tie2d', 'tie3d', 'near2d', 'near3d', 'subnorm', 'overflow', 'smallint']
G = 96  # guard bits for the closeness measure


def decomp_bits(bits):
    """(M, E) with value = M * 2^E for a finite nonnegative binary64 with these bits (sign ignored)."""
    bits &= 0x7FFFFFFFFFFFFFFF
    ef = bits >> 52
    fr = bits & MANT
    if ef == 0:
        return fr, -1074
    return fr | (1 << 52), ef - 1075


def classify(bits):
    a = bits & 0x7FFFFFFFFFFFFFFF
    if a == INF_BITS:
        return 'inf'
    if a > INF_BITS:
        return 'nan'
    if a == 0:
        return 'zero'
    return 'fin'


def sum_squares(bit_list):
    """(N, E0) with S = N * 4^E0, over the finite nonzero components; (0, 0) when all are zero."""
    comps = [decomp_bits(x) for x in bit_list if classify(x) == 'fin']
    if not comps:
        return 0, 0
    e0 = min(e for _, e in comps)
    return sum((m << (e - e0)) ** 2 for m, e in comps), e0


def oracle_a(bit_list):
    """('nan', None) | ('bits', u64) for RN(sqrt(sum of squares))."""
    kinds = [classify(x) for x in bit_list]
    if 'inf' in kinds:
        return 'bits', INF_BITS
    if 'nan' in kinds:
        return 'nan', None
    n, e0 = sum_squares(bit_list)
    if n == 0:
        return 'bits', 0
    er = (n.bit_length() - 1) // 2 + e0  # floor(log2 sqrt(S))
    q = max(er - 52, -1074)  # quantum exponent of the destination
    k = q - e0
    # t = floor(2 * sqrt(S) / 2^q) = floor(sqrt(N * 4^(1-k)))
    if 1 - k >= 0:
        x = n << (2 * (1 - k))
        t = math.isqrt(x)
        is_exact = t * t == x
    else:
        sh = 2 * (k - 1)
        t = math.isqrt(n >> sh)
        is_exact = (t * t) << sh == n
    base = t >> 1
    if t & 1 == 0:
        rn = base
    elif is_exact:
        rn = base + (base & 1)
    else:
        rn = base + 1
    # value = rn * 2^q
    if rn.bit_length() - 1 + q >= 1024:
        return 'bits', INF_BITS
    # encode rn * 2^q as binary64 bits (exact): normalize
    if rn == 0:
        return 'bits', 0
    if rn.bit_length() == 54:  # rn = 2^53 after a carry
        assert rn == 1 << 53
        rn, q = 1 << 52, q + 1
    if q == -1074 and rn < (1 << 52):
        return 'bits', rn  # subnormal
    # normal: rn in [2^52, 2^53)
    assert (1 << 52) <= rn < (1 << 53), (rn, q)
    ef = q + 1075
    assert 1 <= ef <= 2046
    return 'bits', (ef << 52) | (rn & MANT)


def oracle_b(bit_list, r_bits):
    """True when r_bits is the correctly rounded norm, verified without computing RN."""
    kinds = [classify(x) for x in bit_list]
    if 'inf' in kinds:
        return r_bits == INF_BITS
    if 'nan' in kinds:
        return classify(r_bits) == 'nan'
    if r_bits >> 63:
        return False  # never negative (nor -0)
    n, e0 = sum_squares(bit_list)
    kr = classify(r_bits)
    if n == 0:
        return r_bits == 0
    if kr == 'zero' or kr == 'nan':
        return False
    if kr == 'inf':
        # S >= TH^2: N * 4^e0 >= TH_NUM^2 * 4^970
        f = min(e0, 970)
        return n << (2 * (e0 - f)) >= (TH_NUM << (970 - f)) ** 2
    rm, qr = decomp_bits(r_bits)
    ef = r_bits >> 52
    even = rm & 1 == 0
    f = min(e0, qr - 2)
    s = n << (2 * (e0 - f))
    up = ((2 * rm + 1) << (qr - 1 - f)) ** 2
    if ef > 1 and (r_bits & MANT) == 0:
        down = ((4 * rm - 1) << (qr - 2 - f)) ** 2
    else:
        down = ((2 * rm - 1) << (qr - 1 - f)) ** 2
    ok_up = s < up or (s == up and even)
    ok_down = s > down or (s == down and even)
    return ok_up and ok_down


def closeness(bit_list):
    """log2 of the distance (in ulps of the destination) from the exact norm to the nearest midpoint;
    -inf for an exact tie; None for specials/zero/overflow."""
    kinds = [classify(x) for x in bit_list]
    if 'inf' in kinds or 'nan' in kinds:
        return None
    n, e0 = sum_squares(bit_list)
    if n == 0:
        return None
    er = (n.bit_length() - 1) // 2 + e0
    q = max(er - 52, -1074)
    k = q - e0
    # W = floor(2 * sqrt(S)/2^q * 2^G); midpoints are at odd values of 2*sqrt(S)/2^q
    p = 1 - k + G
    if p >= 0:
        x = n << (2 * p)
        w = math.isqrt(x)
        ex = w * w == x
    else:
        sh = -2 * p
        w = math.isqrt(n >> sh)
        ex = (w * w) << sh == n
    period = 1 << (G + 1)
    rem = w % period
    d = abs(rem - (1 << G))  # distance to the odd point, in units 2^-G of (2*sqrt(S)/2^q)
    if d == 0 and ex:
        return float('-inf')
    # one ulp = 2 units of 2*sqrt(S)/2^q  -> distance in ulps = d / 2^(G+1)
    return math.log2(max(d, 1)) - (G + 1)


def work(args):
    trip_bytes, out_bytes, cat_bytes, start = args
    n = len(cat_bytes)
    res = {
        'a3_bad': [], 'a2_bad': [], 'b3_bad': [], 'b2_bad': [], 'ab_disagree': 0,
        'libm2_diff': 0, 'chain3_diff': 0, 'finite_cases': 0,
        'close3': {}, 'close2': {}, 'by_cat': {},
    }
    for i in range(n):
        a, b, c = struct.unpack_from('<QQQ', trip_bytes, 24 * i)
        n3, n2, h2, h3 = struct.unpack_from('<QQQQ', out_bytes, 32 * i)
        cat = CATS[cat_bytes[i]]
        bc = res['by_cat'].setdefault(cat, [0, 0, 0])
        bc[0] += 1
        for tag, comps, got, libm, close_key in (('3', [a, b, c], n3, h3, 'close3'), ('2', [a, b], n2, h2, 'close2')):
            kind, want = oracle_a(comps)
            okb = oracle_b(comps, got)
            if kind == 'nan':
                oka = classify(got) == 'nan'
                libm_ok = classify(libm) == 'nan'
            else:
                oka = got == want
                libm_ok = libm == want
            if not oka:
                res['a' + tag + '_bad'].append([start + i, cat, hex(a), hex(b), hex(c), hex(got), hex(want or 0)])
                bc[1] += 1
            if not okb:
                res['b' + tag + '_bad'].append([start + i, cat, hex(a), hex(b), hex(c), hex(got)])
                bc[2] += 1
            if oka != okb:
                res['ab_disagree'] += 1
            if not libm_ok:
                res['libm2_diff' if tag == '2' else 'chain3_diff'] += 1
            cl = closeness(comps)
            if cl is not None:
                if tag == '3':
                    res['finite_cases'] += 1
                if cl == float('-inf'):
                    key = 'tie'
                else:
                    key = '<2^-%d' % (10 * int(-cl // 10)) if cl < -10 else '>=2^-10'
                res[close_key][key] = res[close_key].get(key, 0) + 1
    return res


def merge(parts):
    out = None
    for p in parts:
        if out is None:
            out = p
            continue
        for k in ('a3_bad', 'a2_bad', 'b3_bad', 'b2_bad'):
            out[k] += p[k]
        for k in ('ab_disagree', 'libm2_diff', 'chain3_diff', 'finite_cases'):
            out[k] += p[k]
        for k in ('close3', 'close2'):
            for kk, v in p[k].items():
                out[k][kk] = out[k].get(kk, 0) + v
        for cat, v in p['by_cat'].items():
            o = out['by_cat'].setdefault(cat, [0, 0, 0])
            for j in range(3):
                o[j] += v[j]
    return out


def main():
    trip_path, out_path = sys.argv[1], sys.argv[2]
    workers = int(sys.argv[3]) if len(sys.argv) > 3 else 4
    trips = open(trip_path, 'rb').read()
    outs = open(out_path, 'rb').read()
    cats = open(trip_path + '.cat', 'rb').read()
    n = len(cats)
    assert len(trips) == 24 * n and len(outs) == 32 * n, (len(trips), len(outs), n)
    chunk = 20000
    jobs = [(trips[24 * s:24 * min(n, s + chunk)], outs[32 * s:32 * min(n, s + chunk)], cats[s:min(n, s + chunk)], s)
            for s in range(0, n, chunk)]
    with Pool(workers) as pool:
        parts = pool.map(work, jobs)
    res = merge(parts)
    summary = {
        'triples': n,
        'results_checked': 2 * n,
        'norm3_misrounded_oracle_A': len(res['a3_bad']),
        'norm2_misrounded_oracle_A': len(res['a2_bad']),
        'norm3_rejected_oracle_B': len(res['b3_bad']),
        'norm2_rejected_oracle_B': len(res['b2_bad']),
        'oracle_A_B_disagreements': res['ab_disagree'],
        'by_category_[cases,A_bad,B_bad]': res['by_cat'],
        'closeness_norm3_ulps_to_midpoint': dict(sorted(res['close3'].items())),
        'closeness_norm2_ulps_to_midpoint': dict(sorted(res['close2'].items())),
        'info_libm_hypot2_not_RN': res['libm2_diff'],
        'info_libm_chain3_not_RN3': res['chain3_diff'],
        'first_failures': (res['a3_bad'] + res['a2_bad'] + res['b3_bad'] + res['b2_bad'])[:50],
    }
    print(json.dumps(summary, indent=1))


if __name__ == '__main__':
    main()
