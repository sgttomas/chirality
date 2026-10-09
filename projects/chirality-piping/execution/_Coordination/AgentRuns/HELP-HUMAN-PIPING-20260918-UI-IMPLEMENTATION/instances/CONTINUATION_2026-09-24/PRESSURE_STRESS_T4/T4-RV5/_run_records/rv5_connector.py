"""T4-RV5: independent refutation of T4-I12's FK unit-level connector references.

Standard library only (fractions, decimal). Method, deliberately different from
T4-I12's closed-form/kinematic B:

  * B is built as a chain  N(L) . blockdiag(Q^T x4) . T_link(a_i, a_j), where N(L) is
    the Euler-Bernoulli natural-mode matrix of a straight member along local x
    (axial, two antisymmetric chord modes, torsion, two symmetric bending modes).
    N(L) is anchored independently: N^T diag(EA/L, 12EIz/L^3, 12EIy/L^3, GJ/L,
    EIy/L, EIz/L) N must equal the textbook 12x12 beam stiffness for several
    rational sections and lengths. T_link is the standard rigid end-offset map
    u_att = u + theta x a.
  * End actions come from virtual work: f_a = dU/dd_a by exact central differences
    of the quadratic energy U(d) (q(d) evaluated by the chain on vectors, not by a
    stored B), and separately from a midpoint-cut free body.
  * Definiteness by Sylvester leading minors (determinants by exact elimination),
    rank and null space by exact row reduction.
  * Finite rotation values from Decimal Taylor series at 60 digits.

Every value is compared with T4-I12's JSON. Usage: python -I rv5_connector.py <json>
"""
import json
import sys
from decimal import Decimal, getcontext
from fractions import Fraction as Fr

getcontext().prec = 80
FAILS = []
NCHK = [0]


def chk(name, ok):
    NCHK[0] += 1
    if not ok:
        FAILS.append(name)
        print("FAIL", name)


def F(s):
    return Fr(s)


def vec(xs):
    return [F(x) for x in xs]


def mat(rows):
    return [[F(x) for x in row] for row in rows]


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def mv(A, x):
    return [sum(a * b for a, b in zip(row, x)) for row in A]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def tr(A):
    return [list(r) for r in zip(*A)]


def zeros(n, m):
    return [[Fr(0)] * m for _ in range(n)]


def rank(A):
    A = [row[:] for row in A]
    r = 0
    rows, cols = len(A), len(A[0])
    for c in range(cols):
        p = next((i for i in range(r, rows) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                f = A[i][c] / A[r][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        r += 1
    return r


def det(A):
    A = [row[:] for row in A]
    n = len(A)
    d = Fr(1)
    for c in range(n):
        p = next((i for i in range(c, n) if A[i][c] != 0), None)
        if p is None:
            return Fr(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            d = -d
        d *= A[c][c]
        for i in range(c + 1, n):
            f = A[i][c] / A[c][c]
            A[i] = [x - f * y for x, y in zip(A[i], A[c])]
    return d


def solve(A, b):
    n = len(A)
    M = [row[:] + [bb] for row, bb in zip(A, b)]
    for c in range(n):
        p = next(i for i in range(c, n) if M[i][c] != 0)
        M[c], M[p] = M[p], M[c]
        for i in range(n):
            if i != c and M[i][c] != 0:
                f = M[i][c] / M[c][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[c])]
    return [M[i][n] / M[i][i] for i in range(n)]


# --------------------------------------------------------- independent anchor of N(L)
def natural_modes(L):
    """Rows: axial e, chord-antisymmetric y (= L*(chord rotation about z - mean end
    rotation about z)), chord-antisymmetric z, torsion, symmetric bending y, z."""
    N = zeros(6, 12)
    N[0][0], N[0][6] = -1, 1
    N[1][1], N[1][7], N[1][5], N[1][11] = -1, 1, -L / 2, -L / 2
    N[2][2], N[2][8], N[2][4], N[2][10] = -1, 1, L / 2, L / 2
    for k in range(3):
        N[3 + k][3 + k], N[3 + k][9 + k] = -1, 1
    return N


def textbook_beam(E, G, A, Iy, Iz, J, L):
    """Standard 12x12 Euler-Bernoulli space-frame stiffness (Przemieniecki ordering
    u, v, w, thx, thy, thz at each end)."""
    k = zeros(12, 12)

    def s(i, j, v):
        k[i][j] = v
        k[j][i] = v
    a = E * A / L
    t = G * J / L
    s(0, 0, a); s(6, 6, a); s(0, 6, -a)
    s(3, 3, t); s(9, 9, t); s(3, 9, -t)
    # bending in x-y plane (v, thz) uses Iz
    c12, c6, c4, c2 = 12 * E * Iz / L**3, 6 * E * Iz / L**2, 4 * E * Iz / L, 2 * E * Iz / L
    s(1, 1, c12); s(7, 7, c12); s(1, 7, -c12)
    s(1, 5, c6); s(1, 11, c6); s(5, 7, -c6); s(7, 11, -c6)
    s(5, 5, c4); s(11, 11, c4); s(5, 11, c2)
    # bending in x-z plane (w, thy) uses Iy
    c12, c6, c4, c2 = 12 * E * Iy / L**3, 6 * E * Iy / L**2, 4 * E * Iy / L, 2 * E * Iy / L
    s(2, 2, c12); s(8, 8, c12); s(2, 8, -c12)
    s(2, 4, -c6); s(2, 10, -c6); s(4, 8, c6); s(8, 10, c6)
    s(4, 4, c4); s(10, 10, c4); s(4, 10, c2)
    return k


for (E, G, A, Iy, Iz, J, L) in [(7, 3, 2, 5, 11, 13, Fr(3, 10)), (Fr(200000), Fr(77000), Fr(1, 100), Fr(3, 7), Fr(2, 9), Fr(5, 3), Fr(22, 10)),
                               (1, 1, 1, 1, 1, 1, 2)]:
    E, G, A, Iy, Iz, J, L = map(Fr, (E, G, A, Iy, Iz, J, L))
    N = natural_modes(L)
    kd = [E * A / L, 12 * E * Iz / L**3, 12 * E * Iy / L**3, G * J / L, E * Iy / L, E * Iz / L]
    Kn = mm(tr(N), mm([[kd[i] if i == j else Fr(0) for j in range(6)] for i in range(6)], N))
    chk("N(L) anchored: N^T diag(EA/L,12EIz/L3,12EIy/L3,GJ/L,EIy/L,EIz/L) N == textbook beam, L=%s" % L,
        Kn == textbook_beam(E, G, A, Iy, Iz, J, L))


# --------------------------------------------------------- connector by the chain
def skew(a):
    return [[0, -a[2], a[1]], [a[2], 0, -a[0]], [-a[1], a[0], 0]]


def link(ai, aj):
    T = zeros(12, 12)
    for blk, a in ((0, ai), (6, aj)):
        S = skew(a)
        for i in range(3):
            T[blk + i][blk + i] = Fr(1)
            T[blk + 3 + i][blk + 3 + i] = Fr(1)
            for j in range(3):
                T[blk + i][blk + 3 + j] = -S[i][j]  # u + theta x a = u - a x theta
    return T


def rot4(Q):
    Qt = tr(Q)
    R = zeros(12, 12)
    for b in range(4):
        for i in range(3):
            for j in range(3):
                R[3 * b + i][3 * b + j] = Qt[i][j]
    return R


def isqrt_frac(x):
    # exact rational square root if one exists
    from math import isqrt
    n, d = x.numerator, x.denominator
    rn, rd = isqrt(n), isqrt(d)
    if rn * rn == n and rd * rd == d:
        return Fr(rn, rd)
    return None


class Conn:
    def __init__(self, xi, xj, ai, aj, Q, K, qref):
        self.xi, self.xj, self.ai, self.aj, self.Q, self.K, self.qref = xi, xj, ai, aj, Q, K, qref
        self.r = [xj[k] + aj[k] - xi[k] - ai[k] for k in range(3)]
        L = isqrt_frac(sum(c * c for c in self.r))
        assert L is not None and L > 0, "rational length expected"
        self.L = L
        qx = [Q[k][0] for k in range(3)]
        self.x_aligned = all(qx[k] * L == self.r[k] for k in range(3))
        self.B = mm(natural_modes(L), mm(rot4(Q), link(ai, aj)))

    def q_of(self, d):
        # vector route: attachment motions, rotate, natural modes (no stored B)
        ui, ti, uj, tj = d[0:3], d[3:6], d[6:9], d[9:12]
        vi = [ui[k] + cross(ti, self.ai)[k] for k in range(3)]
        vj = [uj[k] + cross(tj, self.aj)[k] for k in range(3)]
        Qt = tr(self.Q)
        loc = mv(Qt, vi) + mv(Qt, ti) + mv(Qt, vj) + mv(Qt, tj)
        return mv(natural_modes(self.L), loc)

    def energy(self, d):
        e = [a - b for a, b in zip(self.q_of(d), self.qref)]
        return sum(e[i] * self.K[i][j] * e[j] for i in range(6) for j in range(6)) / 2

    def f_virtual_work(self, d):
        f = []
        for a in range(12):
            dp = d[:]
            dm = d[:]
            dp[a] += 1
            dm[a] -= 1
            f.append((self.energy(dp) - self.energy(dm)) / 2)
        return f

    def f_free_body(self, g):
        Fg = mv(self.Q, g[0:3])
        Mg = mv(self.Q, g[3:6])
        m = [(self.xi[k] + self.ai[k] + self.xj[k] + self.aj[k]) / 2 for k in range(3)]
        ci = cross([m[k] - self.xi[k] for k in range(3)], Fg)
        cj = cross([m[k] - self.xj[k] for k in range(3)], Fg)
        Fi = [-x for x in Fg]
        Mi = [-ci[k] - Mg[k] for k in range(3)]
        Fj = Fg[:]
        Mj = [cj[k] + Mg[k] for k in range(3)]
        return Fi + Mi + Fj + Mj

    def rigid(self, t, w, o):
        ui = [t[k] + cross(w, [self.xi[i] - o[i] for i in range(3)])[k] for k in range(3)]
        uj = [t[k] + cross(w, [self.xj[i] - o[i] for i in range(3)])[k] for k in range(3)]
        return ui + w + uj + w


def K_from_H(H21, Ls):
    H = zeros(6, 6)
    idx = 0
    for i in range(6):
        for j in range(i, 6):
            H[i][j] = H[j][i] = F(H21[idx])
            idx += 1
    D = [F(Ls)] * 3 + [Fr(1)] * 3
    return [[H[i][j] / (D[i] * D[j]) for j in range(6)] for i in range(6)], H


def ex(v):
    return F(v["exact"]) if isinstance(v, dict) else F(v)


def exl(v):
    return [F(x) for x in (v["exact"] if isinstance(v, dict) else v)]


def check_unit(label, inp, exp, origin=None):
    xi, xj = vec(inp["x_i"]), vec(inp["x_j"])
    ai, aj = vec(inp["a_i_global"]), vec(inp["a_j_global"])
    Q = mat(inp["Q_row_major_columns_are_axes"])
    K, H = K_from_H(inp["H_upper_triangle_21_N_m"], inp["translation_scale_Ls_m"])
    chk(label + ": K = D^-1 H D^-1 equals K_physical", K == mat(inp["K_physical"]))
    chk(label + ": Q proper orthogonal", mm(tr(Q), Q) == [[Fr(int(i == j)) for j in range(3)] for i in range(3)] and det(Q) == 1)
    qref = vec(inp["q_ref"])
    c = Conn(xi, xj, ai, aj, Q, K, qref)
    chk(label + ": Q.x aligned with r (chain route admissible)", c.x_aligned)
    chk(label + ": r", c.r == vec(exp["r"]))
    chk(label + ": B (chain) == JSON B", c.B == mat(exp["B"]))
    Ke = mm(tr(c.B), mm(K, c.B))
    chk(label + ": Ke == JSON Ke", Ke == mat(exp["Ke"]))
    chk(label + ": rank B = 6", rank(c.B) == 6 == exp["rank_B"])
    rk = rank(Ke)
    chk(label + ": rank Ke", rk == exp["rank_Ke"])
    o = vec(exp.get("rigid_modes_origin", ["0", "0", "0"]))
    modes = []
    for k in range(6):
        t = [Fr(int(k == 0)), Fr(int(k == 1)), Fr(int(k == 2))]
        w = [Fr(int(k == 3)), Fr(int(k == 4)), Fr(int(k == 5))]
        modes.append(c.rigid(t, w, o))
    chk(label + ": six rigid modes give q = 0 (vector route)", all(all(x == 0 for x in c.q_of(m)) for m in modes))
    chk(label + ": rigid modes independent", rank(modes) == 6)
    if rk == 6:
        chk(label + ": PD -> null(Ke) is exactly span(rigid modes) (12 - rank = 6)", 12 - rk == 6)
    # Sylvester minors for PD; LDL pivots from minors
    minors = [det([row[:k] for row in K[:k]]) for k in range(1, 7)]
    pd = all(mnr > 0 for mnr in minors)
    chk(label + ": PD decision (Sylvester) == K_pd_exact", pd == exp["K_pd_exact"])
    if pd:
        piv = [minors[0]] + [minors[k] / minors[k - 1] for k in range(1, 6)]
        chk(label + ": LDL pivots == minor ratios", piv == vec(exp["K_ldl_pivots"]))
    rhs = mv(tr(c.B), mv(K, qref))
    chk(label + ": installed RHS +B^T K q_ref", rhs == vec(exp["installed_rhs_BT_K_qref"]))
    chk(label + ": K q_ref", mv(K, qref) == vec(exp["K_qref"]))
    sf = all(x == 0 for x in mv(K, qref))
    chk(label + ": stress_free flag", sf == exp["stress_free"])
    # B^T K q_ref is self-equilibrated (force and moment about two origins)
    for oo in ([Fr(0)] * 3, [Fr(7), Fr(-3), Fr(5)]):
        Fs = [rhs[k] + rhs[6 + k] for k in range(3)]
        Ms = [rhs[3 + k] + rhs[9 + k] + cross([xi[i] - oo[i] for i in range(3)], rhs[0:3])[k]
              + cross([xj[i] - oo[i] for i in range(3)], rhs[6:9])[k] for k in range(3)]
        chk(label + ": B^T K q_ref self-equilibrated about %s" % oo, all(x == 0 for x in Fs + Ms))
    d = vec(exp["d"])
    q = c.q_of(d)
    chk(label + ": q (vector route) == JSON q", q == exl(exp["q"]))
    chk(label + ": q == B d", q == mv(c.B, d))
    g = mv(K, [a - b for a, b in zip(q, qref)])
    chk(label + ": g", g == exl(exp["g"]))
    U = c.energy(d)
    chk(label + ": energy", U == ex(exp["energy"]))
    fvw = c.f_virtual_work(d)
    ffb = c.f_free_body(g)
    chk(label + ": end actions by virtual work == midpoint free body", fvw == ffb)
    ea = exp["end_actions_node_on_element"]
    jf = exl(ea["Fi"]) + exl(ea["Mi"]) + exl(ea["Fj"]) + exl(ea["Mj"])
    chk(label + ": end actions (virtual work) == JSON Fi Mi Fj Mj", fvw == jf)
    chk(label + ": Ke d - B^T K q_ref == f", [a - b for a, b in zip(mv(Ke, d), rhs)] == fvw)
    chk(label + ": F_global, M_global", mv(Q, g[0:3]) == exl(exp["F_global"]) and mv(Q, g[3:6]) == exl(exp["M_global"]))
    return c, K, d, q, g, U, fvw


doc = json.load(open(sys.argv[1]))
cases = doc["cases"]

# ---- item 1
for cid in ["U3-J1-LATERAL", "U3-J1-COMMON-ROTATION", "U3-J2-ROTATION", "U3-J2-ROTATION-HELD", "U3-REF-ENDMOMENT"]:
    check_unit(cid, cases[cid]["inputs"], cases[cid]["expected"])
check_unit("U3-REF-ENDMOMENT companion", cases["U3-REF-ENDMOMENT"]["inputs"], cases["U3-REF-ENDMOMENT"]["companion_pure_qrz"])
for comp, e in cases["U3-SIX-COMPONENTS"]["expected"].items():
    check_unit("U3-SIX-COMPONENTS " + comp, cases["U3-SIX-COMPONENTS"]["inputs"], e)

# JR statements, typed from JR CONTRACT.md section 6 and INDEPENDENT_REFUTATION.md sections 1 and 6
def endact(cid, e=None):
    e = e or cases[cid]["expected"]
    ea = e["end_actions_node_on_element"]
    return exl(ea["Fi"]), exl(ea["Mi"]), exl(ea["Fj"]), exl(ea["Mj"])


Fi, Mi, Fj, Mj = endact("U3-J1-LATERAL")
e = cases["U3-J1-LATERAL"]["expected"]
chk("JR J1: q_y=.001 g_y=80 U=.04 Fi_y=-80 Fj_y=80 Mi_z=Mj_z=-12",
    exl(e["q"])[1] == Fr(1, 1000) and exl(e["g"])[1] == 80 and ex(e["energy"]) == Fr(4, 100)
    and Fi[1] == -80 and Fj[1] == 80 and Mi[2] == -12 and Mj[2] == -12)
e = cases["U3-J1-COMMON-ROTATION"]["expected"]
chk("JR J1 common rotation: q, U, actions 0", all(x == 0 for x in exl(e["q"])) and ex(e["energy"]) == 0)
# raw difference: Q^T(uj - ui) with the same K
d = vec(e["d"])
raw_qy = d[7] - d[1]
chk("JR raw difference .003 m, 240 N, .36 J", raw_qy == Fr(3, 1000) and 80000 * raw_qy == 240 and 80000 * raw_qy**2 / 2 == Fr(36, 100))
e = cases["U3-J2-ROTATION"]["expected"]
chk("JR J2: qt=0, qr_z=.01, g_mz=12, U=.06", exl(e["q"])[:3] == [0, 0, 0] and exl(e["q"])[5] == Fr(1, 100)
    and exl(e["g"])[5] == 12 and ex(e["energy"]) == Fr(6, 100))
e = cases["U3-J2-ROTATION-HELD"]["expected"]
chk("JR J2 held: qt_y=-.0015, g_y=-120, g_mz=12", exl(e["q"])[1] == Fr(-15, 10000) and exl(e["g"])[1] == -120 and exl(e["g"])[5] == 12)
Fi, Mi, Fj, Mj = endact("U3-J2-ROTATION-HELD")
L, ky, krz, phi = Fr(3, 10), 80000, 1200, Fr(1, 100)
chk("refutation sec 1 closed form at J2 held: Mj=(krz+ky L^2/4)phi=30, Mi=(ky L^2/4-krz)phi=6, Fjy=-ky L phi/2",
    Mj[2] == (krz + ky * L * L / 4) * phi == 30 and Mi[2] == (ky * L * L / 4 - krz) * phi and Fj[1] == -ky * L * phi / 2)
Fi, Mi, Fj, Mj = endact("U3-REF-ENDMOMENT")
e = cases["U3-REF-ENDMOMENT"]["expected"]
chk("refutation sec 1 (L=2, ky=20, krz=60): Fjy=-.2 Miz=-.4 Mjz=.8 U=.004",
    Fj[1] == Fr(-2, 10) and Mi[2] == Fr(-4, 10) and Mj[2] == Fr(8, 10) and ex(e["energy"]) == Fr(4, 1000))
e = cases["U3-REF-ENDMOMENT"]["companion_pure_qrz"]
chk("refutation pure qrz: .6 N m, .003 J", exl(e["g"])[5] == Fr(6, 10) and ex(e["energy"]) == Fr(3, 1000))
# Euler-Bernoulli cross-check of the measurement control: ky=12EI/L^3, krz=EI/L gives Mj/phi = 4EI/L
EI, L = Fr(7), Fr(2)
chk("refutation EB cross-check: krz + ky L^2/4 = 4EI/L", EI / L + 12 * EI / L**3 * L * L / 4 == 4 * EI / L)

# ---- item 2: B oracle (no K in this case; g given)
c_in = cases["U3-B-ORACLE"]["inputs"]
c_ex = cases["U3-B-ORACLE"]["expected"]
xi, xj, ai, aj = vec(c_in["x_i"]), vec(c_in["x_j"]), vec(c_in["a_i_global"]), vec(c_in["a_j_global"])
Q = mat(c_in["Q_row_major_columns_are_axes"])
# refutation: xi=(1,2,3), r=(2,0,0), xj = xi + ai + r - aj
chk("B oracle geometry as refutation sec 6", xi == [1, 2, 3] and xj == [xi[k] + ai[k] + [2, 0, 0][k] - aj[k] for k in range(3)])
K6 = [[Fr(int(i == j)) for j in range(6)] for i in range(6)]
c = Conn(xi, xj, ai, aj, Q, K6, [Fr(0)] * 6)
chk("B oracle: chain B == JSON B", c.B == mat(c_ex["B"]))
gg = vec(c_in["g_given"])
fb = c.f_free_body(gg)
ftb = mv(tr(c.B), gg)
ea = c_ex["end_actions_node_on_element"]
jf = vec(ea["Fi"]) + vec(ea["Mi"]) + vec(ea["Fj"]) + vec(ea["Mj"])
chk("B oracle: B^T g == free body == JSON blocks", fb == ftb == jf)
chk("B oracle: refutation's stated blocks", jf == [Fr(-2), Fr(3), Fr(-5), Fr(-42, 5), Fr(87, 5), Fr(-43, 5), Fr(2), Fr(-3), Fr(5), Fr(10), Fr(-9, 2), Fr(157, 10)])
dd = [Fr(k - 4, 17) for k in range(12)]
chk("B oracle: d_k = (k-4)/17", dd == vec(c_in["d_given"]))
qq = c.q_of(dd)
chk("B oracle: q == JSON == refutation", qq == vec(c_ex["q_for_d_given"]) == [Fr(73, 170), Fr(-26, 85), Fr(29, 34), Fr(6, 17), Fr(6, 17), Fr(6, 17)])
chk("B oracle: virtual work g.q == f.d == 1567/170", sum(a * b for a, b in zip(gg, qq)) == sum(a * b for a, b in zip(ftb, dd)) == Fr(1567, 170) == F(c_ex["virtual_work"]))
o = vec(c_in["origin_for_rigid_modes"])
chk("B oracle: rigid modes about (7,-3,5) give q = 0", all(all(x == 0 for x in c.q_of(c.rigid([Fr(int(k == 0)), Fr(int(k == 1)), Fr(int(k == 2))], [Fr(int(k == 3)), Fr(int(k == 4)), Fr(int(k == 5))], o))) for k in range(6)))
Fs = [jf[k] + jf[6 + k] for k in range(3)]
Ms = [jf[3 + k] + jf[9 + k] + cross([xi[i] - o[i] for i in range(3)], jf[0:3])[k] + cross([xj[i] - o[i] for i in range(3)], jf[6:9])[k] for k in range(3)]
chk("B oracle: force and arbitrary-origin moment sums zero", all(x == 0 for x in Fs + Ms))

# ---- items 3, 4: generic, covariance, offsets, reversal
gen = check_unit("U3-GENERIC", cases["U3-GENERIC-SKEW-OFFSET-PRESTRESS"]["inputs"], cases["U3-GENERIC-SKEW-OFFSET-PRESTRESS"]["expected"])
cG, KG, dG, qG, gG, UG, fG = gen
# discriminators of the generic case
gi = cases["U3-GENERIC-SKEW-OFFSET-PRESTRESS"]["inputs"]
disc = {x["what"]: x for x in cases["U3-GENERIC-SKEW-OFFSET-PRESTRESS"]["wrong_result_discriminators"]}
xi, xj = vec(gi["x_i"]), vec(gi["x_j"])
r0 = [xj[k] - xi[k] for k in range(3)]
# offsets ignored: a = 0, r = xj - xi; JR formula on global vectors directly (Q kept)
def q_formula(xi, xj, ai, aj, Q, d):
    r = [xj[k] + aj[k] - xi[k] - ai[k] for k in range(3)]
    ui, ti, uj, tj = d[0:3], d[3:6], d[6:9], d[9:12]
    vi = [ui[k] + cross(ti, ai)[k] for k in range(3)]
    vj = [uj[k] + cross(tj, aj)[k] for k in range(3)]
    tc = [(ti[k] + tj[k]) / 2 for k in range(3)]
    rel = [vj[k] - vi[k] - cross(tc, r)[k] for k in range(3)]
    Qt = tr(Q)
    return mv(Qt, rel) + mv(Qt, [tj[k] - ti[k] for k in range(3)])
Qg = mat(gi["Q_row_major_columns_are_axes"])
q_noff = q_formula(xi, xj, [Fr(0)] * 3, [Fr(0)] * 3, Qg, dG)
k_off = [k for k in disc if k.startswith("offsets ignored")][0]
chk("generic discriminator: offsets ignored q", q_noff == exl(disc[k_off]["q"]))
q_qt = q_formula(xi, xj, vec(gi["a_i_global"]), vec(gi["a_j_global"]), tr(Qg), dG)
k_qt = [k for k in disc if k.startswith("Q transposed")][0]
chk("generic discriminator: Q transposed q", q_qt == exl(disc[k_qt]["q"]))
KeG = mm(tr(cG.B), mm(KG, cG.B))
k_res = [k for k in disc if k.startswith("initial residual omitted")][0]
chk("generic discriminator: residual omitted f = Ke d", mv(KeG, dG) == exl(disc[k_res]["f"]))
# S8 exact force scaling
b = 20
Ks = [[x * 2**b for x in row] for row in KG]
chk("S8: Ke(2^b K) = 2^b Ke and B^T(2^b K)q_ref = 2^b B^T K q_ref", mm(tr(cG.B), mm(Ks, cG.B)) == [[x * 2**b for x in row] for row in KeG])
# the PD check of the generic K by minors
chk("generic K is PD (minors)", all(det([row[:k] for row in KG[:k]]) > 0 for k in range(1, 7)))

# covariance: R about z by 90 deg, t = (7,-3,5)
ci_ = cases["U3-FRAME-COVARIANCE"]["inputs"]
R = mat(ci_["R_row_major"])
t = vec(ci_["t"])
chk("covariance: R is +90 deg about z", R == [[0, -1, 0], [1, 0, 0], [0, 0, 1]])
chk("covariance inputs are R x + t, R a, R Q", vec(ci_["x_i"]) == [mv(R, vec(gi["x_i"]))[k] + t[k] for k in range(3)]
    and vec(ci_["x_j"]) == [mv(R, vec(gi["x_j"]))[k] + t[k] for k in range(3)]
    and vec(ci_["a_i_global"]) == mv(R, vec(gi["a_i_global"])) and vec(ci_["a_j_global"]) == mv(R, vec(gi["a_j_global"]))
    and mat(ci_["Q_row_major_columns_are_axes"]) == mm(R, Qg))
cov = check_unit("U3-FRAME-COVARIANCE", ci_, cases["U3-FRAME-COVARIANCE"]["expected"])
dC = vec(cases["U3-FRAME-COVARIANCE"]["expected"]["d"])
chk("covariance: d is R-rotated generic d", dC == sum((mv(R, dG[3 * k:3 * k + 3]) for k in range(4)), []))
chk("covariance: q, g, U unchanged", cov[3] == qG and cov[4] == gG and cov[5] == UG)
chk("covariance: global actions rotate", cov[6] == sum((mv(R, fG[3 * k:3 * k + 3]) for k in range(4)), []))

off = check_unit("U3-OFFSETS", cases["U3-OFFSETS"]["inputs"], cases["U3-OFFSETS"]["expected"])
oi = cases["U3-OFFSETS"]["inputs"]
al = oi["attachment_local"]
chk("offsets: a = Q_node offset_local", vec(oi["a_i_global"]) == mv(mat(al["initial_node_axes_global_i"]), vec(al["offset_local_i"]))
    and vec(oi["a_j_global"]) == mv(mat(al["initial_node_axes_global_j"]), vec(al["offset_local_j"])))
q_noff = q_formula(vec(oi["x_i"]), vec(oi["x_j"]), [Fr(0)] * 3, [Fr(0)] * 3, mat(oi["Q_row_major_columns_are_axes"]), off[2])
chk("offsets discriminator q", q_noff == exl(cases["U3-OFFSETS"]["wrong_result_discriminators"][0]["q"]))

# reversal
rv = cases["U3-REVERSAL"]["inputs"]
J = [[-1, 0, 0], [0, 1, 0], [0, 0, -1]]
J = mat(J)
T6 = [[Fr(0)] * 6 for _ in range(6)]
for k in range(3):
    T6[k][k] = -J[k][k]
    T6[3 + k][3 + k] = -J[k][k]
chk("reversal: T = blockdiag(-J,-J)", T6 == mat(rv["T"]))
chk("reversal: inputs are the canonical transform of generic",
    vec(rv["x_i"]) == vec(gi["x_j"]) and vec(rv["x_j"]) == vec(gi["x_i"])
    and vec(rv["a_i_global"]) == vec(gi["a_j_global"]) and vec(rv["a_j_global"]) == vec(gi["a_i_global"])
    and mat(rv["Q_row_major_columns_are_axes"]) == mm(Qg, J)
    and mat(rv["K_physical"]) == mm(T6, mm(KG, tr(T6)))
    and vec(rv["q_ref"]) == mv(T6, vec(gi["q_ref"])))
Hg = K_from_H(gi["H_upper_triangle_21_N_m"], gi["translation_scale_Ls_m"])[1]
Hr = K_from_H(rv["H_upper_triangle_21_N_m"], rv["translation_scale_Ls_m"])[1]
chk("reversal: H' = T H T^T at unchanged Ls", Hr == mm(T6, mm(Hg, tr(T6))) and rv["translation_scale_Ls_m"] == gi["translation_scale_Ls_m"])
rev = check_unit("U3-REVERSAL", rv, cases["U3-REVERSAL"]["expected"])
dR = vec(cases["U3-REVERSAL"]["expected"]["d"])
chk("reversal: d is the generic d with node blocks exchanged", dR == dG[6:12] + dG[0:6])
chk("reversal: q' = T q, g' = T g, U' = U", rev[3] == mv(T6, qG) and rev[4] == mv(T6, gG) and rev[5] == UG)
chk("reversal: end-action blocks exchanged", rev[6] == fG[6:12] + fG[0:6])
# wrong reversal: ids swapped with Q' = QJ but K and q_ref untransformed
cw = Conn(vec(rv["x_i"]), vec(rv["x_j"]), vec(rv["a_i_global"]), vec(rv["a_j_global"]), mat(rv["Q_row_major_columns_are_axes"]), KG, vec(gi["q_ref"]))
wd = cases["U3-REVERSAL"]["wrong_result_discriminators"][0]
chk("reversal discriminator energy and Fj", cw.energy(dR) == ex(wd["energy"]) and cw.f_virtual_work(dR)[6:9] == exl(wd["Fj"]))
chk("reversal discriminator differs from the correct values", cw.energy(dR) != UG)

# W4 link rule
w4 = cases["U3-W4-LINK-RULE"]
Kp, Hp = K_from_H(w4["inputs"]["psd_H_upper_triangle_21_Ls_2m"], "2")
cp = Conn(vec(gi["x_i"]), vec(gi["x_j"]), vec(gi["a_i_global"]), vec(gi["a_j_global"]), Qg, Kp, [Fr(0)] * 6)
Kep = mm(tr(cp.B), mm(Kp, cp.B))
chk("W4 PSD: rank K = 2, rank Ke = 2, null dim 10", rank(Kp) == 2 and rank(Kep) == 2 == w4["expected"]["psd_case"]["rank_Ke"] and 12 - rank(Kep) == 10)
# PSD (not PD): the only nonzero block (coords 0, 3) is PD; all other rows zero
blk = [[Kp[0][0], Kp[0][3]], [Kp[3][0], Kp[3][3]]]
chk("W4 PSD: K is PSD (2x2 block PD, rest zero) and not PD", det(blk) > 0 and blk[0][0] > 0 and not all(det([row[:k] for row in Kp[:k]]) > 0 for k in range(1, 7)))
nv = vec(w4["expected"]["psd_case"]["non_rigid_null_vector_d"])
chk("W4 PSD: stated non-rigid null vector in null(Ke), q = e_y, not rigid", all(x == 0 for x in mv(Kep, nv)) and cp.q_of(nv) == vec(w4["expected"]["psd_case"]["its_q"])
    and rank([cp.rigid([Fr(int(k == 0)), Fr(int(k == 1)), Fr(int(k == 2))], [Fr(int(k == 3)), Fr(int(k == 4)), Fr(int(k == 5))], [Fr(0)] * 3) for k in range(6)] + [nv]) == 7)
nq = vec(w4["expected"]["psd_case"]["null_coordinate_q_ref"]["q_ref"])
chk("W4 PSD: null-coordinate q_ref has K q_ref = 0", all(x == 0 for x in mv(Kp, nq)))
Ki, Hi = K_from_H(w4["inputs"]["indefinite_H_upper_triangle_21_Ls_2m"], "2")
mi = [det([row[:k] for row in Hi[:k]]) for k in range(1, 7)]
chk("W4 indefinite: leading minors of H 4,4,4,-9,...: pivot 4 = -9/4 (negative eigenvalue)", mi[:3] == [4, 4, 4] and mi[3] / mi[2] == Fr(-9, 4)
    and [mi[0]] + [mi[k] / mi[k - 1] for k in range(1, 6)] == vec(w4["expected"]["indefinite_case"]["ldl_pivots_H"]))
# H and K have the same inertia (congruence by diagonal D): decision on H == decision on K
mk = [det([row[:k] for row in Ki[:k]]) for k in range(1, 7)]
chk("W4: sign pattern of minors of H equals that of K (D congruence)", [x > 0 for x in mi] == [x > 0 for x in mk])
# PSD pivots stated as K pivots: check they equal LDL with zero-pivot skipping
chk("W4 PSD: stated K pivots 1,0,0,35/4,0,0", vec(w4["expected"]["psd_case"]["ldl_pivots_K"]) == [1, 0, 0, Fr(35, 4), 0, 0]
    and Kp[3][3] - Kp[0][3] ** 2 / Kp[0][0] == Fr(35, 4))

# coupled H, rescale, preload
ch = cases["U3-COUPLED-H-SCALE-PRELOAD"]
cpl = check_unit("U3-COUPLED", ch["inputs"]["coupled"], ch["expected"]["coupled"])
chk("coupled: U = .075, g_tx = .25, g_rx = 1", cpl[5] == Fr(75, 1000) and cpl[4][0] == Fr(1, 4) and cpl[4][3] == 1)
Kc, Hc = K_from_H(ch["inputs"]["coupled"]["H_upper_triangle_21_N_m"], "2")
Rr = [Fr(1, 2)] * 3 + [Fr(1)] * 3  # D' D^-1 for Ls 2 -> 1
H1 = [[Rr[i] * Hc[i][j] * Rr[j] for j in range(6)] for i in range(6)]
K1, _ = K_from_H(ch["inputs"]["rescaled_H_upper_triangle_Ls_1m"], "1")
chk("rescale: H' = R H R equals JSON (1, .5, 9) and K unchanged", H1 == K_from_H(ch["inputs"]["rescaled_H_upper_triangle_Ls_1m"], "1")[1] and K1 == Kc)
chk("rescale: qhat = D^-1 q", vec(ch["expected"]["qhat"]) == [cpl[3][0] / 2, cpl[3][1] / 2, cpl[3][2] / 2] + cpl[3][3:])
c0 = ch["inputs"]["coupled"].copy()
c0["q_ref"] = ch["inputs"]["preload_q_ref"]
pre = check_unit("U3-PRELOAD-d0", c0, ch["expected"]["preload_installed_d0"])
chk("preload d=0: f = [+.25,-.25] N and [+1,-1] N m, U = .075", pre[6][0] == Fr(1, 4) and pre[6][6] == Fr(-1, 4) and pre[6][3] == 1 and pre[6][9] == -1 and pre[5] == Fr(75, 1000))
# wrong: H read as K (fixed 1 m)
Hq = [[Hc[i][j] for j in range(6)] for i in range(6)]
qv = cpl[3]
chk("coupled discriminator: H read as K gives 29/200 J", sum(qv[i] * Hq[i][j] * qv[j] for i in range(6) for j in range(6)) / 2 == F(ch["wrong_result_discriminators"][1]["energy_J"]) == Fr(29, 200))

# preload relief: solve the reduced systems myself
pr = cases["U3-PRELOAD-RELIEF"]
pin = pr["inputs"]
Kr, _ = K_from_H(pin["H_upper_triangle_21_N_m"], pin["translation_scale_Ls_m"])
chk("preload relief K == K_physical and PD", Kr == mat(pin["K_physical"]) and all(det([row[:k] for row in Kr[:k]]) > 0 for k in range(1, 7)))
crl = Conn(vec(pin["x_i"]), vec(pin["x_j"]), vec(pin["a_i_global"]), vec(pin["a_j_global"]), mat(pin["Q_row_major_columns_are_axes"]), Kr, vec(pin["q_ref"]))
Ker = mm(tr(crl.B), mm(Kr, crl.B))
rhs = mv(tr(crl.B), mv(Kr, crl.qref))
chk("preload relief RHS", rhs == vec(pr["expected"]["installed_rhs_BT_K_qref"]))


def held_solve(free):
    A = [[Ker[i][j] for j in free] for i in free]
    x = solve(A, [rhs[i] for i in free])
    d = [Fr(0)] * 12
    for k, i in enumerate(free):
        d[i] = x[k]
    q = crl.q_of(d)
    g = mv(Kr, [a - b for a, b in zip(q, crl.qref)])
    reac = [a - b for a, b in zip(mv(Ker, d), rhs)]  # support-on-element = internal action f at held DOFs
    return d, q, g, crl.energy(d), reac


for key, free in [("node_i_anchored_node_j_free", list(range(6, 12))), ("node_i_anchored_node_j_ux_held", list(range(7, 12)))]:
    d, q, g, U, reac = held_solve(free)
    e = pr["expected"][key]
    chk("preload relief %s: d, q, g, U, reactions" % key, d == vec(e["d"]) and q == vec(e["q"]) and g == vec(e["g_recovered"]) and U == F(e["energy"])
        and reac == vec(e["support_on_element_reactions"]))
e = pr["expected"]["both_nodes_held"]
chk("preload relief both held: g = -K q_ref, reactions = -B^T K q_ref", mv(Kr, [-x for x in crl.qref]) == vec(e["g_recovered"]) and [-x for x in rhs] == vec(e["support_on_element_reactions"]))
chk("preload relief discriminator: RHS omitted gives g = -K q_ref", vec(pr["wrong_result_discriminators"][0]["g"]) == mv(Kr, [-x for x in crl.qref]))

# raw difference historical
rd = cases["U3-RAW-DIFFERENCE-NEGATIVE"]["expected"]
hc = rd["historical_correct"]
chk("raw historical: correct q = 0 for L=2, w=.01, ujy=.02", all(x == 0 for x in exl(hc["q"])) and vec(hc["d"])[7] == Fr(2, 100) and vec(hc["d"])[5] == vec(hc["d"])[11] == Fr(1, 100))
chk("raw historical: raw q_y .02, 20*.02 = .4 N, .004 J", F(rd["historical_raw"]["q_y_m"]) == Fr(2, 100) and F(rd["historical_raw"]["g_y_N"]) == Fr(4, 10) and F(rd["historical_raw"]["energy_J"]) == Fr(4, 1000))

# finite rotation: Decimal Taylor series
def dcos(x):
    s, t, k = Decimal(0), Decimal(1), 0
    while abs(t) > Decimal(10) ** -75:
        s += t
        k += 2
        t = -t * x * x / ((k - 1) * k)
    return s


def dsin(x):
    s, t, k = Decimal(0), x, 1
    while abs(t) > Decimal(10) ** -75:
        s += t
        k += 2
        t = -t * x * x / ((k - 1) * k)
    return s


for row in cases["U3-FINITE-ROTATION-NEGATIVE"]["expected"]["rows"]:
    Ld, ph = Decimal(row["L_m"]), Decimal(row["phi_rad"])
    # true rigid rotation of x_j = L e_x about z: u_j = (R - I) x_j; theta = phi e_z
    uj = [Ld * (dcos(ph) - 1), Ld * dsin(ph), Decimal(0)]
    # linear measure: qt = u_j - u_i - theta_c x r, theta_c x r = phi e_z x L e_x = (0, L phi, 0)
    qt = [uj[0], uj[1] - Ld * ph, Decimal(0)]
    ok = all(abs(Decimal(a) - b) <= Decimal(10) ** -38 * max(Decimal(1), abs(b)) for a, b in zip(row["qt"], qt))
    ok = ok and all(abs(Decimal(a) - b) <= Decimal(10) ** -38 for a, b in zip(row["d"]["u_j"], uj))
    chk("finite rotation L=%s phi=%s: qt and u_j to 38 digits" % (row["L_m"], row["phi_rad"]), ok)
    lb = Decimal("0.99") * Ld * ph * ph / 2 * (1 - ph * ph / 12)
    chk("finite rotation negative-assertion bound holds for the exact value", abs(qt[0]) >= lb and qt[0] != 0)
# refutation's binary64 decimals at L=2, phi=.1
row = cases["U3-FINITE-ROTATION-NEGATIVE"]["expected"]["rows"][0]
chk("refutation finite-rotation decimals agree to 13 digits only (binary64 cancellation)",
    abs(Decimal(row["qt"][0]) - Decimal("-0.00999166944394836")) < Decimal("2e-16") and abs(Decimal(row["qt"][1]) - Decimal("-0.000333166706343702")) < Decimal("1e-17"))

# ---- self-tests: the comparisons above are not vacuous
Nbad = natural_modes(Fr(2))
Nbad[1][5] = -Nbad[1][5]
Nbad[1][11] = -Nbad[1][11]
kd = [Fr(1), Fr(12, 8), Fr(12, 8), Fr(1), Fr(1, 2), Fr(1, 2)]
chk("self-test: a sign-flipped chord mode is NOT the textbook beam", mm(tr(Nbad), mm([[kd[i] if i == j else Fr(0) for j in range(6)] for i in range(6)], Nbad)) != textbook_beam(*map(Fr, (1, 1, 1, 1, 1, 1, 2))))
Tbad = link(vec(gi["a_i_global"]), vec(gi["a_j_global"]))
for i in range(3):
    for j in range(3):
        Tbad[i][3 + j] = -Tbad[i][3 + j]
chk("self-test: offset map with the wrong sign does NOT reproduce the JSON B", mm(natural_modes(cG.L), mm(rot4(Qg), Tbad)) != mat(cases["U3-GENERIC-SKEW-OFFSET-PRESTRESS"]["expected"]["B"]))
chk("self-test: Q^T replaced by Q does NOT reproduce the JSON B", mm(natural_modes(cG.L), mm(rot4(tr(Qg)), link(vec(gi["a_i_global"]), vec(gi["a_j_global"])))) != mat(cases["U3-GENERIC-SKEW-OFFSET-PRESTRESS"]["expected"]["B"]))
print("connector checks: %d run, %d fail" % (NCHK[0], len(FAILS)))
print("PASS" if not FAILS else "FAIL")
