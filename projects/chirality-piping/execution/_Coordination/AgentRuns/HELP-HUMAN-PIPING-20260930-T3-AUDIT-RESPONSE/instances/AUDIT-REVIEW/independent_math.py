#!/usr/bin/env python3
"""Exact local proof probes; no audit, solver, generator or runner imports.

Run from any directory with Python 3, -B. Prints JSON only. This models scale
and publication algebra, not a generated PrimitiveSource or accepted solve.
"""
import json
import math
from fractions import Fraction as Q


def p2(e):
    return Q(2**e) if e >= 0 else Q(1, 2**-e)


def nearest_integer(x):
    n, rem = divmod(x.numerator, x.denominator)
    return n + (2*rem > x.denominator or (2*rem == x.denominator and n % 2))


def binary64(x):
    """Independent integer rounding to nearest/even, for bounded nonnegative x."""
    assert x >= 0
    if x == 0:
        return x
    e = x.numerator.bit_length() - x.denominator.bit_length()
    if x < p2(e):
        e -= 1
    quantum = p2(max(-1074, e - 52))
    return nearest_integer(x / quantum) * quantum


def upward(x):
    y = binary64(x)
    if y >= x:
        return y
    return Q.from_float(math.nextafter(float(y), math.inf))


def bound(value, scale):
    b = upward(scale * p2(-64))
    if scale == 0 or scale >= p2(-988):
        return b
    return upward(b + upward(abs(value) * p2(-53)) + p2(-1074))


def main():
    h, r, u = p2(-1074), 5*p2(-1076), p2(-64)
    assert binary64(r) == h == Q.from_float(float(r))
    rows = []
    for direction, extent in [('rotation_to_translation', p2(100)),
                              ('translation_to_rotation', p2(-100))]:
        gain = extent if direction.startswith('rotation') else 1/extent
        sv = gain*r
        sp = binary64(gain*binary64(r))
        q_true = Q(9, 8)*u*sp
        b = bound(Q(0), sp)
        # Same power-of-two body extent is returned by binary64 bbox arithmetic.
        assert math.sqrt(float(extent)**2) == float(extent)
        assert sv == 5*p2(-976) and sp == p2(-974)
        assert sv-sp > (p2(-64)+p2(-52))*sv + h/2
        assert sp >= p2(-988) and Q(0) < binary64(p2(-34)*sp)
        assert q_true < u*sv and q_true > b*(1+p2(-22))
        assert q_true < sv and q_true/gain < r
        # A single nonzero vector component has the same magnitude. The actual
        # rule additionally charges 2^(1-P)|q_2p| to displacement magnitudes.
        for precision in [256, 512, 1024]:
            assert q_true*(1+p2(1-precision)) < u*sv
            assert r*p2(1-precision) < u*r
        rows.append({'direction': direction, 'extent_hex': float(extent).hex(),
                     'verification_over_published': str(sv/sp),
                     'relative_scale_loss': str((sv-sp)/sv),
                     'abstract_truth_over_bound': str(q_true/b),
                     'magnitude_charge_alone_excludes': False,
                     'branch': 'plain bound, published scale >= 2^-988'})
    zero_sv = p2(-100)*r
    zero_sp = binary64(p2(-100)*binary64(r))
    assert zero_sv > 0 and zero_sp == 0 and bound(Q(0), zero_sp) == 0
    thresholds = []
    for e in [85, 86, 87, 100]:
        sv = p2(e)*r
        sp = binary64(p2(e)*h)
        thresholds.append({'extent_exponent': e,
                           'published_scale_hex': float(sp).hex(),
                           'small_branch': 0 < sp < p2(-988),
                           'bound_hex_for_zero_row': float(bound(Q(0), sp)).hex(),
                           'scale_loss': str((sv-sp)/sv)})
    # At L=2^86, the ordinary branch begins; below it, h does not universally
    # cover u*(Sv-Sp), either. At 2^85 that transfer gap is 2^19 h.
    assert u*(p2(85)*r-p2(85)*h)/h == 2**19
    # Scalar candidates are exact dyadics of <=4 significant bits; they fit all
    # candidate/verification widths and the retained +/-2^62 exponent range.
    print(json.dumps({'coupling_cases': rows, 'thresholds': thresholds,
                      'zero_scale': {'verification_positive': True,
                                     'publication_zero': True, 'row_bound_zero': True},
                      'limits': ['No source model or Rust execution.',
                                 'Zero W_plus is stipulated; source-derived verification, force/moment and theta/g constraints are not demonstrated.',
                                 'Vector magnitude charges checked algebraically with one nonzero component; no full source layout is asserted.',
                                 'Large extent may be excluded by product capture; small extent has no analogous large-coordinate issue.']},
                     indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
