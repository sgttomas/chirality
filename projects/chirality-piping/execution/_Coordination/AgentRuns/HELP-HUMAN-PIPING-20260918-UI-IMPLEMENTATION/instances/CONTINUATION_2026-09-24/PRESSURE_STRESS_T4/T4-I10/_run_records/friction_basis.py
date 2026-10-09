"""T4-I10, read-only arithmetic (fractions). Item 6: what NI's four friction tests
actually pin, so that the replacement coupling keeps the same structure.

Fixture `coupled_normal_friction_problem` (NI/src/lib.rs:3580@ed012c7ccf): node 0 fixed;
node 1 restrained in Uy, Uz, Rx, Ry, Rz; only Ux free, with a friction support on Ux
(mu = 0.30) whose normal is the Uy reaction. The old element joins (0,0,0)-(1,1,0) with
axial 100 and lateral 200 (angular/torsional springs do not touch the translations).
Its node-1 translational block is k_a e e^T + k_l (I - e e^T), e = (1,1,0)/sqrt2:
Kxx = (k_a + k_l)/2, Kxy = (k_a - k_l)/2.

Sliding solution (friction opposes the applied Ux): reaction Ry = Kxy*u - Fy,
N = |Ry|, friction reaction Rx = -sign(Fx)*mu*N, Kxx*u = Fx + Rx.
This reproduces the four expectations at NI/src/lib.rs:3761-3762@ed012c7ccf exactly.

Any coupling whose node-1 translational block on the free Ux and the reacting Uy has the
same form gives the same algebra. An ordinary FrameElement on an off-axis chord, with
node-1 rotations restrained (they already are), has the block
(EA/L) e e^T + (12 E Iz / L^3)(I - e e^T) in plane. The illustrative choice below is
not a frozen reference: the reference TASK derives and freezes its own values.
"""
from fractions import Fraction as F


def sliding(kxx, kxy, fx, fy, mu):
    # Solve for u with Rx = -s*mu*|kxy*u - fy|, s = sign(fx); check the branch.
    s = 1 if fx > 0 else -1
    for sign_ry in (1, -1):
        # |Ry| = sign_ry*(kxy*u - fy); kxx*u = fx - s*mu*sign_ry*(kxy*u - fy)
        u = (fx + s * mu * sign_ry * fy) / (kxx + s * mu * sign_ry * kxy)
        ry = kxy * u - fy
        if (ry >= 0) == (sign_ry == 1):
            n = abs(ry)
            return u, n, -s * mu * n
    raise ValueError("no consistent branch")


mu = F(3, 10)
ka, kl = F(100), F(200)
kxx, kxy = (ka + kl) / 2, (ka - kl) / 2
expected = {
    (10, -10): (F(7, 135), F(200, 27), F(-20, 9)),
    (-10, -10): (F(-7, 165), F(400, 33), F(40, 11)),
}
print(f"old element block: Kxx={kxx}, Kxy={kxy}")
for (fx, fy), exp in expected.items():
    got = sliding(kxx, kxy, F(fx), F(fy), mu)
    print(f"  Fx={fx}, Fy={fy}: u={got[0]}, N={got[1]}, friction={got[2]}; matches pinned values: {got == exp}")

# Illustrative replacement: FrameElement (0,0,0)-(3,4,0), L=5, E=125, A=4, Iz=25.
L, E, A, Iz = F(5), F(125), F(4), F(25)
c, s = F(3, 5), F(4, 5)
ea_l, b = E * A / L, 12 * E * Iz / L**3
kxx2 = ea_l * c * c + b * s * s
kxy2 = (ea_l - b) * c * s
print(f"illustrative frame block: EA/L={ea_l}, 12EIz/L^3={b}, Kxx={kxx2}, Kxy={kxy2}")
for fx, fy in expected:
    print(f"  Fx={fx}, Fy={fy}: (u, N, friction) = {sliding(kxx2, kxy2, F(fx), F(fy), mu)}")
