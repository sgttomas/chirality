"""RV126: self-test of check.py's two oracles against a third, decimal-based rounding, and a
mutation test of oracle B (it must reject both binary64 neighbours of the correct result).

Usage: selftest.py TRIPLES SAMPLE_SIZE SEED
"""
import decimal
import random
import struct
import sys

import check

decimal.getcontext().prec = 1600
D = decimal.Decimal


def dec_of_bits(bits):
    m, e = check.decomp_bits(bits)
    return D(m) * (D(2) ** e)


def oracle_c(bit_list):
    """RN via decimal: sqrt to 1600 digits, then compare with exact decimal midpoints."""
    kinds = [check.classify(x) for x in bit_list]
    if 'inf' in kinds:
        return 'bits', check.INF_BITS
    if 'nan' in kinds:
        return 'nan', None
    s = sum(dec_of_bits(x) ** 2 for x in bit_list if check.classify(x) == 'fin')
    if s == 0:
        return 'bits', 0
    r = s.sqrt()
    # walk candidates: start from the float nearest r (via a coarse conversion), then fix by midpoints
    try:
        approx = float(r)
    except OverflowError:
        approx = float('inf')
    if approx == float('inf'):
        cand = 0x7FEFFFFFFFFFFFFF
    else:
        cand = struct.unpack('<Q', struct.pack('<d', approx))[0]
    for _ in range(8):
        val = dec_of_bits(cand)
        m, q = check.decomp_bits(cand)
        up_mid = val + (D(2) ** (q - 1))
        ef = cand >> 52
        down_gap = (D(2) ** (q - 2)) if (ef > 1 and (cand & check.MANT) == 0) else (D(2) ** (q - 1))
        down_mid = val - down_gap
        even = m & 1 == 0
        if r > up_mid or (r == up_mid and not even):
            if cand == 0x7FEFFFFFFFFFFFFF:
                return 'bits', check.INF_BITS
            cand += 1
            continue
        if r < down_mid or (r == down_mid and not even):
            cand -= 1
            continue
        return 'bits', cand
    raise RuntimeError('no convergence')


def main():
    path, size, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    data = open(path, 'rb').read()
    cats = open(path + '.cat', 'rb').read()
    n = len(cats)
    rng = random.Random(seed)
    idx = sorted(set(rng.randrange(n) for _ in range(size)))
    bad_ac = bad_b_true = bad_b_mut = ties = 0
    checked = 0
    for i in idx:
        a, b, c = struct.unpack_from('<QQQ', data, 24 * i)
        for comps in ([a, b, c], [a, b]):
            ka, va = check.oracle_a(comps)
            kc, vc = oracle_c(comps)
            checked += 1
            if ka != kc or (ka == 'bits' and va != vc):
                bad_ac += 1
                print('A!=C', i, [hex(x) for x in comps], ka, va and hex(va), kc, vc and hex(vc))
                continue
            if ka == 'nan':
                continue
            if not check.oracle_b(comps, va):
                bad_b_true += 1
                print('B rejects RN', i, [hex(x) for x in comps], hex(va))
            # mutation: neighbours must be rejected (for a finite nonzero, non-special result)
            kinds = [check.classify(x) for x in comps]
            if 'inf' in kinds or va == 0:
                continue
            for nb in (va - 1, va + 1):
                if nb < 0 or nb > check.INF_BITS:
                    continue
                if check.oracle_b(comps, nb):
                    bad_b_mut += 1
                    print('B accepts neighbour', i, [hex(x) for x in comps], hex(va), hex(nb))
            if check.closeness(comps) == float('-inf'):
                ties += 1
    print({'sampled_triples': len(idx), 'results_checked': checked, 'A_vs_C_disagree': bad_ac,
           'B_rejects_RN': bad_b_true, 'B_accepts_a_neighbour': bad_b_mut, 'exact_ties_in_sample': ties})


if __name__ == '__main__':
    main()
