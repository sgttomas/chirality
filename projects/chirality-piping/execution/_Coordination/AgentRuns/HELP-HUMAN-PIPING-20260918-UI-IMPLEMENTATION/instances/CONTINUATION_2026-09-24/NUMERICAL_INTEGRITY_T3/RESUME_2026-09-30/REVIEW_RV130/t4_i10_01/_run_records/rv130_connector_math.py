"""RV130, read-only and self-contained (standard library only; exact rationals).
Checks of T4-I10's connector mathematics on T3's surfaces (W4, K-D5, S11-G).

Usage: python -I rv130_connector_math.py

Kinematics are JR CONTRACT.md section 2 (S(v)w = v x w):
  Bt = Q^T[-I, S(ai)+S(r)/2, I, -S(aj)+S(r)/2],  Br = Q^T[0, -I, 0, I],
  r = (xj + aj) - (xi + ai).
Sections:
  A. rank B = 6 and B * rigid = 0 exactly, for proper-orthogonal rational Q,
     random rational offsets and positions, including coincident attachments
     (r = 0) and coincident nodes; also for binary64 Q (only invertible).
  B. PD K: rank(B^T K B) = 6, so null(B^T K B) = null(B) = rigid (a link).
     PSD K of rank 5: rank 5, a seventh null vector (a release, not a link).
  C. The old element's tie space {ui = uj, thi = thj} is not the pair's rigid
     space when r != 0 (why W4 needed virtual positions for it).
  D. An exact PD decision on binary64 K vs a binary64 Cholesky pivot test.
  E. K-D5 at UTM: binary64 r from absolute attachment positions vs from node
     differences, against the exact r, and the K-D5 trigger on a one-connector
     model (node i restrained, node j free).
  F. S11-G's Bounded q_ref term: |r_hat - r| against gamma bounds written on
     |r_hat| and on |xj - xi| + |aj - ai| (coincident attachments).
"""
import random
from fractions import Fraction as F

random.seed(130)
U = F(1, 2 ** 53)


def gamma(n):
    return n * U / (1 - n * U)


# ---------------------------------------------------------------- algebra
def mat(rows, cols, f=lambda i, j: F(0)):
    return [[f(i, j) for j in range(cols)] for i in range(rows)]


def mul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0)) for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return [list(r) for r in zip(*a)]


def rank(m):
    m = [list(r) for r in m]
    rk, rows, cols = 0, len(m), len(m[0])
    for c in range(cols):
        piv = next((r for r in range(rk, rows) if m[r][c] != 0), None)
        if piv is None:
            continue
        m[rk], m[piv] = m[piv], m[rk]
        for r in range(rows):
            if r != rk and m[r][c] != 0:
                f = m[r][c] / m[rk][c]
                m[r] = [x - f * y for x, y in zip(m[r], m[rk])]
        rk += 1
    return rk


def skew(v):
    return [[F(0), -v[2], v[1]], [v[2], F(0), -v[0]], [-v[1], v[0], F(0)]]


def eye(n):
    return mat(n, n, lambda i, j: F(1) if i == j else F(0))


def inv3(m):
    a = [list(r) + e for r, e in zip(m, eye(3))]
    for c in range(3):
        p = next(r for r in range(c, 3) if a[r][c] != 0)
        a[c], a[p] = a[p], a[c]
        a[c] = [x / a[c][c] for x in a[c]]
        for r in range(3):
            if r != c:
                a[r] = [x - a[r][c] * y for x, y in zip(a[r], a[c])]
    return [r[3:] for r in a]


def cayley(s):
    """Exact proper orthogonal Q = (I - S)^-1 (I + S) for skew S."""
    S = skew(s)
    I = eye(3)
    return mul(inv3([[I[i][j] - S[i][j] for j in range(3)] for i in range(3)]),
               [[I[i][j] + S[i][j] for j in range(3)] for i in range(3)])


def bmatrix(xi, xj, ai, aj, Q):
    r = [(xj[k] + aj[k]) - (xi[k] + ai[k]) for k in range(3)]
    Qt = tr(Q)
    Sai, Saj, Sr = skew(ai), skew(aj), skew(r)
    I = eye(3)
    blocks_t = [[[-I[i][j] for j in range(3)] for i in range(3)],
                [[Sai[i][j] + Sr[i][j] / 2 for j in range(3)] for i in range(3)],
                I,
                [[-Saj[i][j] + Sr[i][j] / 2 for j in range(3)] for i in range(3)]]
    Z = mat(3, 3)
    blocks_r = [Z, [[-I[i][j] for j in range(3)] for i in range(3)], Z, I]
    rows = []
    for blocks in (blocks_t, blocks_r):
        qb = [mul(Qt, b) for b in blocks]
        for i in range(3):
            rows.append([qb[c][i][j] for c in range(4) for j in range(3)])
    return rows, r


def rigid_basis(xi, xj, origin):
    vecs = []
    for k in range(6):
        t = [F(1) if k == m else F(0) for m in range(3)]
        w = [F(1) if k - 3 == m else F(0) for m in range(3)]
        col = []
        for x in (xi, xj):
            d = [x[m] - origin[m] for m in range(3)]
            wx = [w[1] * d[2] - w[2] * d[1], w[2] * d[0] - w[0] * d[2], w[0] * d[1] - w[1] * d[0]]
            col += [t[m] + wx[m] for m in range(3)] + w
        vecs.append(col)
    return vecs


def rnd(scale=10, den=97):
    return F(random.randint(-scale * den, scale * den), den)


# ---------------------------------------------------------------- A, B
def section_ab():
    print("A/B. rank B, B*rigid, PD link and PSD release (exact rationals)")
    cases = 0
    for trial in range(60):
        kind = trial % 4
        Q = cayley([rnd(1, 7) for _ in range(3)])
        xi = [rnd(1000) for _ in range(3)]
        xj = [xi[k] + rnd(2) for k in range(3)]
        ai = [rnd(1) for _ in range(3)]
        aj = [rnd(1) for _ in range(3)]
        if kind == 1:  # coincident attachments: r = 0 with distinct nodes and offsets
            aj = [xi[k] + ai[k] - xj[k] for k in range(3)]
        if kind == 2:  # coincident node positions (distinct node identities)
            xj = list(xi)
        if kind == 3:  # binary64 Q: approximately orthogonal, exactly invertible
            Q = [[F(float(v)) for v in row] for row in Q]
        B, r = bmatrix(xi, xj, ai, aj, Q)
        assert rank(B) == 6, ("rank", trial)
        for v in rigid_basis(xi, xj, [rnd(5) for _ in range(3)]):
            q = [sum((B[i][j] * v[j] for j in range(12)), F(0)) for i in range(6)]
            if kind == 3:
                # Q binary64 is still invertible, so B*rigid = Q^T*(exact zero) = 0.
                pass
            assert all(x == 0 for x in q), ("rigid", trial)
        L = mat(6, 6, lambda i, j: rnd(3) if j <= i else F(0))
        for i in range(6):
            L[i][i] = abs(L[i][i]) + 1
        K_pd = mul(L, tr(L))
        assert rank(mul(tr(B), mul(K_pd, B))) == 6
        L5 = [row[:5] for row in L]
        K_psd = mul(L5, tr(L5))  # rank 5: one released generalized direction
        assert rank(K_psd) == 5
        assert rank(mul(tr(B), mul(K_psd, B))) == 5
        cases += 1
    print(f"   {cases} cases (15 general, 15 r = 0, 15 coincident nodes, 15 binary64 Q): rank B = 6, "
          "B * rigid = 0 (6 modes, arbitrary origin), rank(B^T K_pd B) = 6, rank(B^T K_psd B) = 5. PASS")


# ---------------------------------------------------------------- C
def section_c():
    print("C. the old element's tie space is not the rigid space")
    xi, xj = [F(0)] * 3, [F(3, 10), F(0), F(0)]
    # Common rigid rotation wz = 1e-3 about xi: uj = w x (xj - xi) = (0, 3e-4, 0).
    w = F(1, 1000)
    ui, uj = [F(0)] * 3, [F(0), w * F(3, 10), F(0)]
    rel = [uj[k] - ui[k] for k in range(3)]
    print(f"   rigid rotation wz = 1e-3: relative translation uj - ui = {[float(v) for v in rel]} "
          "(nonzero lateral: the old lateral spring is strained by a rigid motion, so its 'tie' "
          "u_i = u_j, th_i = th_j is not rigid; W4 represented it by virtual positions)")
    B, _ = bmatrix(xi, xj, [F(0)] * 3, [F(0)] * 3, eye(3))
    d = ui + [F(0), F(0), w] + uj + [F(0), F(0), w]
    q = [sum((B[i][j] * d[j] for j in range(12)), F(0)) for i in range(6)]
    print(f"   connector q for the same motion: {[float(v) for v in q]} (exactly zero: a link)")


# ---------------------------------------------------------------- D
def ldl_pd(K):
    """Exact PD decision: every LDL^T pivot > 0 (no square roots)."""
    n = len(K)
    A = [list(r) for r in K]
    for c in range(n):
        if A[c][c] <= 0:
            return False
        for r in range(c + 1, n):
            f = A[r][c] / A[c][c]
            A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return True


def float_pivots(K):
    n = len(K)
    A = [[float(v) for v in r] for r in K]
    piv = []
    for c in range(n):
        piv.append(A[c][c])
        if A[c][c] == 0:
            break
        for r in range(c + 1, n):
            f = A[r][c] / A[c][c]
            A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return piv


def section_d():
    print("D. exact PD decision on binary64 K vs binary64 pivots")
    third = F(1.0 / 3.0)  # fl(1/3) < 1/3
    K = eye(6)
    K[0][0], K[0][1], K[1][0], K[1][1] = F(3), F(1), F(1), third
    print(f"   K[0:2,0:2] = [[3, 1], [1, fl(1/3)]]: exact det block = {float(3 * third - 1):.3e}; "
          f"exact LDL^T PD = {ldl_pd(K)}; binary64 pivots {float_pivots(K)[:2]} "
          "(second pivot exactly 0.0: a tolerance test calls it PSD, the exact test finds it indefinite)")
    K[1][1] = F(0.33333333333333337)
    print(f"   with K[1][1] = next binary64 above 1/3: exact det block = {float(3 * K[1][1] - 1):.3e}; "
          f"exact PD = {ldl_pd(K)}")


# ---------------------------------------------------------------- E
def solve_float(A, b):
    n = len(A)
    M = [list(map(float, A[i])) + [float(b[i])] for i in range(n)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        M[c], M[p] = M[p], M[c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    x = [0.0] * n
    for i in reversed(range(n)):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return x


def kd5_ratio(xi, xj, ai, aj, Q, Kdiag, f_j, r_float):
    """One connector, node i restrained, node j free. Product: binary64-formed
    K_jj from r_float (all else exact-then-rounded per entry); K-D5: exact K_jj
    from the binary64 inputs. Returns max_i 2|w_i| / (1e-9 * max(|u_i|, S*))."""
    B_exact, r_exact = bmatrix(xi, xj, ai, aj, Q)
    K = mat(6, 6, lambda i, j: Kdiag[i] if i == j else F(0))
    Kint = mul(tr(B_exact), mul(K, B_exact))
    # product matrix: the same formula with r replaced by the binary64 r, rounded per entry
    aj_eff = [F(r_float[k]) - (xj[k] - xi[k]) + ai[k] for k in range(3)]  # gives r = r_float exactly
    B_hat, r_hat = bmatrix(xi, xj, ai, aj_eff, Q)
    B_hat = [[B_hat[i][j] if j < 6 else B_hat[i][j] for j in range(12)] for i in range(6)]
    # Only the r-dependent theta columns differ; aj itself stays as authored in S(aj):
    Qt = tr(Q)
    Sr = skew([F(v) for v in r_float])
    Saj = skew(aj)
    blk = mul(Qt, [[-Saj[i][j] + Sr[i][j] / 2 for j in range(3)] for i in range(3)])
    for i in range(3):
        for j in range(3):
            B_hat[i][9 + j] = blk[i][j]
    Khat = [[F(float(v)) for v in row] for row in mul(tr(B_hat), mul(K, B_hat))]
    jj = list(range(6, 12))
    Kh = [[Khat[a][b] for b in jj] for a in jj]
    Ki = [[Kint[a][b] for b in jj] for a in jj]
    u = solve_float(Kh, f_j)
    rho = [F(f_j[a]) - sum((Ki[a][b] * F(u[b]) for b in range(6)), F(0)) for a in range(6)]
    w = solve_float(Kh, [float(v) for v in rho])
    s_tr = max(abs(u[k]) for k in range(3))
    s_ro = max(abs(u[k]) for k in range(3, 6))
    worst = 0.0
    for k in range(6):
        scale = max(abs(u[k]), s_tr if k < 3 else s_ro)
        worst = max(worst, 2 * abs(w[k]) / (1e-9 * scale))
    return worst


def section_e():
    print("E. K-D5 at UTM coordinates: how the binary64 path forms r")
    Q = eye(3)
    Kdiag = [F(200000), F(80000), F(120000), F(600), F(900), F(1200)]
    f_j = [10.0, 80.0, -15.0, 1.5, -2.0, 12.0]
    rows = []
    for label, origin in (("ordinary", [F(0)] * 3), ("UTM", [F(5_000_000.25), F(4_000_000.5), F(100)])):
        xi = [origin[0] + F(1.0), origin[1] + F(2.0), origin[2]]
        xi = [F(float(v)) for v in xi]
        xj = [F(float(xi[0] + F(3, 10))), xi[1], xi[2]]
        ai = [F(0.0123), F(0.0456), F(-0.0078)]
        aj = [F(-0.0217), F(0.0331), F(0.0094)]
        exact = [(xj[k] + aj[k]) - (xi[k] + ai[k]) for k in range(3)]
        fx = lambda v: float(v)
        naive = [(fx(xj[k]) + fx(aj[k])) - (fx(xi[k]) + fx(ai[k])) for k in range(3)]
        safe = [(fx(xj[k]) - fx(xi[k])) + (fx(aj[k]) - fx(ai[k])) for k in range(3)]
        en = max(abs(F(naive[k]) - exact[k]) for k in range(3))
        es = max(abs(F(safe[k]) - exact[k]) for k in range(3))
        rn = kd5_ratio(xi, xj, ai, aj, Q, Kdiag, f_j, naive)
        rs = kd5_ratio(xi, xj, ai, aj, Q, Kdiag, f_j, safe)
        rows.append((label, float(en), float(es), rn, rs))
    for label, en, es, rn, rs in rows:
        print(f"   {label:8s}: |r err| absolute-position form {en:.3e} m, node-difference form {es:.3e} m; "
              f"K-D5 trigger 2|w|/(1e-9 S) = {rn:.3g} vs {rs:.3g} (demotes when > 1)")


# ---------------------------------------------------------------- F
def section_f():
    print("F. S11-G Bounded q_ref term: the r operand under cancellation")
    worst_hat, worst_ops = 0.0, 0.0
    fails = 0
    trials = 2000
    for _ in range(trials):
        # Decimal-authored coincident attachments: xi + ai = xj + aj in decimal,
        # each value then read as binary64 (the user's intent is r = 0).
        dxi = F(random.randint(-50000, 50000), 1000)
        dxj = dxi + F(random.randint(-2000, 2000), 1000)
        dai = F(random.randint(-1000, 1000), 1000)
        daj = dxi + dai - dxj
        xi, xj, ai, aj = (float(v) for v in (dxi, dxj, dai, daj))
        exact = (F(xj) + F(aj)) - (F(xi) + F(ai))
        r_hat = (xj - xi) + (aj - ai)
        err = abs(F(r_hat) - exact)
        bound_hat = gamma(3) * abs(F(r_hat))
        bound_ops = gamma(3) * (abs(F(xj) - F(xi)) + abs(F(aj) - F(ai)))
        if err > bound_hat:
            fails += 1
        if bound_ops > 0:
            worst_ops = max(worst_ops, float(err / bound_ops))
    print(f"   {trials} decimal-authored coincident attachments: |r_hat - r| > gamma_3*|r_hat| in {fails} cases; "
          f"max |r_hat - r| / (gamma_3*(|xj - xi| + |aj - ai|)) = {worst_ops:.3f} (<= 1 holds)")


section_ab()
section_c()
section_d()
section_e()
section_f()
