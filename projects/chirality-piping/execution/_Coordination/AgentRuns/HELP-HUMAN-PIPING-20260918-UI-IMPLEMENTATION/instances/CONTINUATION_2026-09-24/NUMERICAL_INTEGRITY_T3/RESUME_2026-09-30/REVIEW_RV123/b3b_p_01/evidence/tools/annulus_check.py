"""RV123: the correctly rounded annulus (A, I, J, Z) of the m3x section from the exact binary64
OD and effective wall, with pi to 300 digits, against the published prepared bits and the
ordinary SourceAnnulus bits (B3-D 1.3's table)."""
from decimal import Decimal as Dm, getcontext
from fractions import Fraction as F
import struct, sys
getcontext().prec = 320
def pi_dec():
    # Machin: pi = 16 atan(1/5) - 4 atan(1/239)
    def atan_inv(x):
        x = Dm(x); x2 = x * x; term = Dm(1) / x; total = term; n = 1; sign = -1
        while True:
            term /= x2; n += 2; t = term / n
            if t < Dm(10) ** (-315): break
            total += sign * t; sign = -sign
        return total
    return 16 * atan_inv(5) - 4 * atan_inv(239)
PI = pi_dec()
def rn64(d):  # correctly round a Decimal (far from ties) to binary64 via Fraction
    f = F(d)
    x = float(f)  # Python rounds Fraction -> float correctly (round-half-even)
    return x
def bits(x): return struct.pack('>d', x).hex()
D = 0.2; t = 0.01
ro = F(D) / 2; ri = ro - F(t)
A = PI * Dm((ro * ro - ri * ri).numerator) / Dm((ro * ro - ri * ri).denominator)
q4 = ro ** 4 - ri ** 4
I = PI * Dm(q4.numerator) / Dm(q4.denominator) / 4
J = 2 * I
Z = I / (Dm(ro.numerator) / Dm(ro.denominator))
out = {k: bits(rn64(v)) for k, v in [('A', A), ('I', I), ('J', J), ('Z', Z)]}
print('correctly rounded', out)
print('published prepared', dict(A='3f7872fa3a37ac13', I='3efc52664442210a', J='3f0c52664442210a', Z='3f31b37feaa954a6'))
print('ordinary SourceAnnulus', dict(A='3f7872fa3a37ac13', I='3efc52664442210b', J='3f0c52664442210b', Z='3f31b37feaa954a7'))
