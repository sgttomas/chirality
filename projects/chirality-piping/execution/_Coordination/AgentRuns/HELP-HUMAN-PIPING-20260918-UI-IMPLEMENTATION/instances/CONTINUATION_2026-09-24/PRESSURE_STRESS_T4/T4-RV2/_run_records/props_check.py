"""T4-RV2: P1, P2 (exact permutation), P4 floors against labelled binary64 emulations:
  * the stable element (emu64 'GL' and 'CR') on every B2 case and every UTM control;
  * today's absolute-centre path (PP centre + CB geometry, closed-form F, formula chord),
    emulated in binary64 in source order, at X = 0, 5e5, 2e6, 5e6, 7.3e6 (discrimination).
usage: python -I props_check.py U1_REFERENCE_CASES_JSON"""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decimal import Decimal as D, getcontext
from fractions import Fraction as Fr
import rv2_lib as L
import emu64 as M

getcontext().prec = 60
doc = json.load(open(sys.argv[1]))


def p1(Kb, d):
    """max over rigid modes (exact, from binary64 d) and rows of |K r| / sum|K_rc r_c|, exact sums."""
    worst = Fr(0)
    dd = [Fr(v) for v in d]
    modes = []
    for k in range(3):
        m = [Fr(0)] * 12
        m[k] = m[6 + k] = Fr(1)
        modes.append(m)
    for k in range(3):
        w = [Fr(0)] * 3
        w[k] = Fr(1)
        s = [w[1] * dd[2] - w[2] * dd[1], w[2] * dd[0] - w[0] * dd[2], w[0] * dd[1] - w[1] * dd[0]]
        m = [Fr(0)] * 12
        for c in range(3):
            m[3 + c] = m[9 + c] = w[c]
            m[6 + c] = s[c]
        modes.append(m)
    zero_rows_bad = 0
    for m in modes:
        for r in range(12):
            terms = [Fr(Kb[r][c]) * m[c] for c in range(12)]
            den = sum(abs(t) for t in terms)
            num = abs(sum(terms))
            if den == 0:
                if num != 0:
                    zero_rows_bad += 1
                continue
            worst = max(worst, num / den)
    return float(worst), zero_rows_bad


def p4(Kb, Kref):
    sc = max(abs(v) for row in Kref for v in row)
    ms = max(abs(D(Kb[i][j]) - Kref[i][j]) for i in range(12) for j in range(12)) / sc
    dg = max(abs(D(Kb[i][j]) - Kref[i][j]) / (Kref[i][i] * Kref[j][j]).sqrt() for i in range(12) for j in range(12))
    return float(ms), float(dg)


def perm_dev(case, Fm, Kb):
    inp = case["inputs"]
    d, y = inp["d"], inp["y_reference"]
    dp, yp = [d[2], d[0], d[1]], [y[2], y[0], y[1]]
    KbP, _, _ = M.element_b64(dp, inp["R"], yp, inp["E"], inp["G"], inp["A"], inp["I"], inp["J"], case["k_in"], case["k_out"], F_mode=Fm)
    # P K P^T with P (x,y,z) -> (z,x,y) per 3-block: new index of old component c is (c+1)%3
    PK = [[0.0] * 12 for _ in range(12)]
    for i in range(12):
        for j in range(12):
            ni = 3 * (i // 3) + (i % 3 + 1) % 3
            nj = 3 * (j // 3) + (j % 3 + 1) % 3
            PK[ni][nj] = Kb[i][j]
    sc = max(abs(v) for row in Kb for v in row)
    return max(abs(KbP[i][j] - PK[i][j]) for i in range(12) for j in range(12)) / sc


print("Stable-element emulation on the 48 B2 cases (CB toy separately): P1 (<=1e-11), P4 ms (<=1e-9), P4 diag, P2-perm (<=1e-12)")
agg = {"GL": [0, 0, 0, 0], "CR": [0, 0, 0, 0]}
for c in doc["cases"]:
    inp = c["inputs"]
    Kref = [[D(v) for v in row] for row in c["K_global"]]
    line = "%-28s" % c["id"]
    for Fm in ("GL", "CR"):
        if c["id"].startswith("CB_"):
            nd = c["nodes_by_X"]["origin"]
            dd = [nd["x_j"][k] - nd["x_i"][k] for k in range(3)]
        else:
            dd = inp["d"]
        Kb, g, _ = M.element_b64(dd, inp["R"], inp["y_reference"], inp["E"], inp["G"], inp["A"], inp["I"], inp["J"], c["k_in"], c["k_out"], F_mode=Fm)
        r1, zb = p1(Kb, dd)
        ms, dg = p4(Kb, Kref)
        pdv = perm_dev(c, Fm, Kb) if not c["id"].startswith("CB_") else 0.0
        a = agg[Fm]
        a[0] = max(a[0], r1); a[1] = max(a[1], ms); a[2] = max(a[2], dg); a[3] = max(a[3], pdv)
        line += "  %s: P1 %.1e%s P4 %.1e/%.1e P2 %.1e" % (Fm, r1, "" if zb == 0 else "(!%d zero-rows)" % zb, ms, dg, pdv)
    print(line)
for Fm in agg:
    print("WORST %s: P1 %.2e  P4 %.2e (diag %.2e)  P2 %.2e" % (Fm, *agg[Fm]))
print()
print("UTM controls (stable GL element): P1, P4")
for c in doc["utm_controls_refused_today"]["cases"]:
    s = c["section"]
    dd = [c["x_j"][k] - c["x_i"][k] for k in range(3)]
    Kref = [[D(v) for v in row] for row in c["K_global"]]
    Kb, g, _ = M.element_b64(dd, c["R"], c["y_reference"], s["e"], s["g"], s["a"], s["i"], s["j"], 1.0, 1.0, F_mode="GL")
    r1, zb = p1(Kb, dd)
    ms, dg = p4(Kb, Kref)
    print("  X %-9s phi %.4f  P1 %.1e P4 %.1e/%.1e" % (c["X"], g["phi"], r1, ms, dg))


# ------------------------------------------------------------------ today's path (labelled emulation)
def legacy_K(xi, xj, R, y, E, G, A, I, J, k):
    chord = [xj[0] - xi[0], xj[1] - xi[1], xj[2] - xi[2]]
    Lc = math.sqrt(chord[0] * chord[0] + chord[1] * chord[1] + chord[2] * chord[2])
    h = 0.5 * Lc
    if R <= h:
        return None, "R<=L/2"
    cu = [chord[0] / Lc, chord[1] / Lc, chord[2] / Lc]
    ax = y[0] * cu[0] + y[1] * cu[1] + y[2] * cu[2]
    pn = [y[0] - ax * cu[0], y[1] - ax * cu[1], y[2] - ax * cu[2]]
    pm = math.sqrt(pn[0] * pn[0] + pn[1] * pn[1] + pn[2] * pn[2])
    so = math.sqrt(R * R - h * h)
    C = [0.5 * (xi[k] + xj[k]) - so * pn[k] / pm for k in range(3)]
    ri = [xi[k] - C[k] for k in range(3)]
    rj = [xj[k] - C[k] for k in range(3)]
    ni, nj = math.sqrt(sum(v * v for v in ri)), math.sqrt(sum(v * v for v in rj))
    if abs(ni - nj) > 1e-9 * max(ni, nj):
        return None, "radius mismatch %.2e" % (abs(ni - nj) / max(ni, nj))
    Rm = 0.5 * (ni + nj)
    nrm = [ri[1] * rj[2] - ri[2] * rj[1], ri[2] * rj[0] - ri[0] * rj[2], ri[0] * rj[1] - ri[1] * rj[0]]
    phi = math.atan2(math.sqrt(sum(v * v for v in nrm)), sum(ri[k] * rj[k] for k in range(3)))
    sp, cp = math.sin(phi), math.cos(phi)
    Gm = [[phi, sp, 1 - cp], [sp, phi / 2 + math.sin(2 * phi) / 4, sp * sp / 2], [1 - cp, sp * sp / 2, phi / 2 - math.sin(2 * phi) / 4]]
    z3 = (0.0, 0.0, 0.0)
    acts = [((0, 0, -1), (-Rm * sp, 0, Rm), z3, z3), ((0, 1, 0), (Rm * cp, -Rm, 0), z3, z3),
            (z3, z3, (0, Rm * sp, -Rm * cp), (Rm, -Rm * cp, -Rm * sp)), (z3, z3, (0, 1, 0), (0, 0, -1)),
            (z3, z3, (0, 0, 1), (0, 1, 0)), (z3, (1, 0, 0), z3, z3)]
    q = lambda u, v: sum(u[i] * Gm[i][j] * v[j] for i in range(3) for j in range(3))
    F = [[Rm * (k * q(acts[a][1], acts[b][1]) / (E * I) + k * q(acts[a][2], acts[b][2]) / (E * I) + q(acts[a][3], acts[b][3]) / (G * J) + q(acts[a][0], acts[b][0]) / (E * A)) for b in range(6)] for a in range(6)]
    Kt = M.inv6(F)
    c = [Rm * (cp - 1.0), Rm * sp, 0.0]
    ex = [v / ni for v in ri]
    nn = math.sqrt(sum(v * v for v in nrm))
    ez = [v / nn for v in nrm]
    ey = [ez[1] * ex[2] - ez[2] * ex[1], ez[2] * ex[0] - ez[0] * ex[2], ez[0] * ex[1] - ez[1] * ex[0]]
    H = [[1.0 if i == j else 0.0 for j in range(6)] for i in range(6)]
    H[3][1], H[3][2], H[4][0], H[4][2], H[5][0], H[5][1] = -c[2], c[1], c[2], -c[0], -c[1], c[0]
    HK = M.mm(H, Kt)
    HKHt = M.mm(HK, [list(r) for r in zip(*H)])
    Kl = [[0.0] * 12 for _ in range(12)]
    for i in range(6):
        for j in range(6):
            Kl[i][j] = HKHt[i][j]; Kl[i][j + 6] = -HK[i][j]; Kl[i + 6][j] = -HK[j][i]; Kl[i + 6][j + 6] = Kt[i][j]
    Ax = [ex, ey, ez]
    K = [[0.0] * 12 for _ in range(12)]
    for bi in range(4):
        for bj in range(4):
            for r in range(3):
                for cc in range(3):
                    K[3 * bi + r][3 * bj + cc] = sum(Ax[p][r] * sum(Kl[3 * bi + p][3 * bj + qq] * Ax[qq][cc] for qq in range(3)) for p in range(3))
    return K, "formed"


print()
print("Today's path (labelled emulation): P1 row-relative residual and P4, by X (refusals named)")
for cid in ("B90-IP-k1.0-base", "B90-SK-k1.0-base", "B45-SK-k1.0-base", "B5-IP-k1.0-base", "B5-SK-k2.5-rotated", "B90-SK-k2.5-rotated"):
    c = next(x for x in doc["cases"] if x["id"] == cid)
    inp = c["inputs"]
    Kref = [[D(v) for v in row] for row in c["K_global"]]
    out = "%-22s" % cid
    for X, nd in c["nodes_by_X"].items():
        K, st = legacy_K(nd["x_i"], nd["x_j"], inp["R"], inp["y_reference"], inp["E"], inp["G"], inp["A"], inp["I"], inp["J"], c["k_in"])
        if K is None:
            out += "  X=%s: refused (%s)" % (X, st)
        else:
            r1, _ = p1(K, inp["d"])
            ms, _ = p4(K, Kref)
            out += "  X=%s: P1 %.1e P4 %.1e" % (X, r1, ms)
    print(out)
