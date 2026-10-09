"""T4-RV2 self-checks of rv2_lib (independent of T4-I6)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decimal import Decimal as D, getcontext
import math
import rv2_lib as L
getcontext().prec = 60
# trig and pi
pi = L.pi_agm()
print("pi digits ok:", str(pi)[:52] == "3.141592653589793238462643383279502884197169399375105"[:52])
s, c = L.sincos(D(1))
print("sin1 cos1", str(s)[:30], str(c)[:30], "s^2+c^2-1 =", f"{float(s*s+c*c-1):.1e}")
t = L.angle_newton(D(1), D(1)); print("atan(1)*4 - pi =", f"{float(4*t-pi):.1e}")
# quarter circle, in-plane bending only: delta_x = (3pi/4-2) P R^3/EI, delta_y = pi/4 P R^3/EI
R, E, I = D(2), D(100), D(5)
huge = D(10) ** 40
g = L.arc_geometry([2, 0, 0], [0, 2, 0], 2, [1, 1, 0])
F = L.tip_flexibility_global(g, E, E, huge, I, huge, 1, 1, n=40)
ex = (3 * pi / 4 - 2) * R ** 3 / (E * I)
ey = pi / 4 * R ** 3 / (E * I)
print("quarter circle F_xx rel err %.1e  F_yy rel err %.1e  phi-pi/2 %.1e" % (float(F[0][0] / ex - 1), float(F[1][1] / ey - 1), float(g["phi"] - pi / 2)))
# out-of-plane: load P_z at free end, bending + torsion. Known (Roark): delta_z = P R^3 [pi/4 /EI*kout + (3pi/4 - 2)/GJ]
G, J = D(40), D(7)
F2 = L.tip_flexibility_global(g, E, G, huge, I, J, 1, 1, n=40)
ez = R ** 3 * (pi / 4 / (E * I) + (3 * pi / 4 - 2) / (G * J))
print("quarter circle out-of-plane F_zz rel err %.1e" % float(F2[2][2] / ez - 1))
# straight limit: phi = 1e-6, |d| = 1, k=1 -> frame K
getcontext().prec = 60
d = [D(1), D(0), D(0)]
Rr = D(1) / (2 * L.sincos(D("5e-7"))[0])
K = L.curved_K([0, 0, 0], [1, 0, 0], Rr, [0, 1, 0], 2e11, 8e10, 0.006, 2.7e-5, 5.4e-5, 1, 1, n=24)["K"]
Kf = L.frame_K([0, 0, 0], [1, 0, 0], 2e11, 8e10, 0.006, 2.7e-5, 5.4e-5)
print("straight limit phi=1e-6: max|K-Kframe|/max|K| = %.2e" % float(max(abs(K[i][j] - Kf[i][j]) for i in range(12) for j in range(12)) / L.maxabs(Kf)))
# rigid null space of the curved element
KK = L.curved_K([0.1, 0.2, 0.3], [0.5, -0.1, 0.9], 1.3, [1, 2, -1], 2e11, 8e10, 0.006, 2.7e-5, 5.4e-5, 2.5, 1.75)["K"]
dd = [D(0.5) - D(0.1), D(-0.1) - D(0.2), D(0.9) - D(0.3)]
worst = max(abs(sum(KK[r][c] * m[c] for c in range(12))) / sum(abs(KK[r][c] * m[c]) for c in range(12)) for m in L.rigid_modes(dd) for r in range(12))
print("curved element rigid null residual (row-relative): %.1e" % float(worst))
sym = max(abs(KK[i][j] - KK[j][i]) for i in range(12) for j in range(12)) / L.maxabs(KK)
print("symmetry %.1e" % float(sym))
