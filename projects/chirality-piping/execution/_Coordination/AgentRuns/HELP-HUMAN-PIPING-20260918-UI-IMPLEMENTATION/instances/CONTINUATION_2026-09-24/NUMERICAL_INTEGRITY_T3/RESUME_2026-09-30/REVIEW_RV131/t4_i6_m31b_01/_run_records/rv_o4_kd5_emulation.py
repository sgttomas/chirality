"""RV131: K-D5's own re-formation error at p (O4), and M31b / M31b0 inside K-D5, on the K1 cantilever.
The product is ideal: u = the exact intended solution rounded once to binary64. EF = K^-1 rho with
rho = f - K_int u summed exactly (K-D5's ExactAccumulator), K the exact intended system (K-tilde's
own error is second order). Trigger = 2|w_i| / (1e-9 max(|u_i|, S*_kind)) as formation_check.rs:306-337.
usage: python -I rv_o4_kd5_emulation.py"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from decimal import Decimal as D, getcontext, localcontext
import rv_element as RV
import rv_wide as W
getcontext().prec = 70
S = RV.SECTION
g30 = 2.0 ** -30
def gr(v): return round(v / g30) * g30
PLANES = {"IP": ([math.cos(math.pi / 6), math.sin(math.pi / 6), 0.0], [0.0, 1.0, 0.0]),
          "SK": ([1.0 / 3.0, 2.0 / 3.0, 2.0 / 3.0], [1.0, -1.0, 0.5])}
FREE = [3, 4, 5, 6, 7, 8, 9, 10, 11]
LOAD = {9: 1.0, 10: 1.0, 11: 1.0}

def radius_for(d, phi):
    with localcontext() as c:
        c.prec = 60
        L = RV.v_norm([D(v) for v in d])
        s, _ = RV.d_sincos(D(phi) / 2)
        return float(L / (2 * s))

def scales(u_b64, L_b):
    st = max(abs(u_b64[k]) for k in FREE if k % 6 < 3)
    sr = max(abs(u_b64[k]) for k in FREE if k % 6 >= 3)
    return max(st, L_b * sr), max(sr, st / L_b)

def trigger(Kint_el, u_b64, Kexact_free, L_b):
    # rho_i = f_i - sum_j Kint_ij u_j - spring_i u_i, exact (Fractions)
    rho = []
    for a in FREE:
        acc = Fr(LOAD.get(a, 0.0))
        for b in range(12):
            if u_b64[b] != 0.0:
                acc -= Kint_el[a][b] * Fr(u_b64[b])
        if a in (3, 4, 5):
            acc -= Fr(1.0e6) * Fr(u_b64[a])
        rho.append(acc)
    rhoD = [D(x.numerator) / D(x.denominator) for x in rho]
    w = RV.m_solve(Kexact_free, rhoD)
    tr, ro = scales(u_b64, L_b)
    worst = (0.0, None)
    for idx, a in enumerate(FREE):
        sc = max(abs(u_b64[a]), ro if a % 6 >= 3 else tr)
        t = float(2 * abs(w[idx]) / (D("1e-9") * D(sc)))
        if t > worst[0]:
            worst = (t, a)
    return worst

def run(plane, phi, variants):
    dh, y = PLANES[plane]
    d = [gr(0.3 * c) for c in dh]
    R = radius_for(d, phi)
    xi = [0.0, 0.0, 0.0]
    xj = d[:]
    Kex, geo, _ = RV.element_global(d, R, y, S["E"], S["G"], S["A"], S["I"], S["J"], 1.0, 1.0)
    u_ex, Kf, free = RV.cantilever_solve(Kex)
    u_b64 = [0.0] * 12
    for k, v in u_ex.items():
        u_b64[k] = float(v)
    L_b = float(geo["L"])
    out = []
    sc = max(abs(v) for r in Kex for v in r)
    for name, p, variant, chord_mode, b64_chord in variants:
        ar = W.P(p)
        if b64_chord:
            # M31b: H from the binary64 formula chord (binary64 R, phi, cos, sin), lifted into K-D5
            L64 = math.sqrt(d[0] * d[0] + d[1] * d[1] + d[2] * d[2])
            phib = 2.0 * math.asin(L64 / (2.0 * R))
            Kp, info = kd5_with_chord(ar, xi, xj, R, y, variant, [R * (math.cos(phib) - 1.0), R * math.sin(phib), 0.0])
        else:
            Kp, info = W.kd5_curved_at_p(ar, xi, xj, R, y, S["E"], S["G"], S["A"], S["I"], S["J"], 1.0, 1.0, variant, chord_mode)
        Kd = [[D(v.numerator) / D(v.denominator) for v in row] for row in Kp]
        relK = max(abs(Kd[i][j] - Kex[i][j]) for i in range(12) for j in range(12)) / sc
        t = trigger(Kp, u_b64, Kf, L_b)
        out.append((name, relK, t))
    return float(geo["phi"]), R, out

def kd5_with_chord(ar, xi, xj, R, y, variant, chord_b64):
    # same as W.kd5_curved_at_p but H from a supplied (binary64) local chord
    import rv_wide
    orig = rv_wide.kd5_curved_at_p
    Kp, info = orig(ar, xi, xj, R, y, S["E"], S["G"], S["A"], S["I"], S["J"], 1.0, 1.0, variant, "actual")
    # recompute with the supplied chord: reuse tip and axes from info by re-running the H/rotate part
    r = ar
    F = info["F"]
    tip = rv_wide.invert6(r, F)
    chord = [Fr(v) for v in chord_b64]
    h = [[Fr(int(i == j)) for j in range(6)] for i in range(6)]
    h[3][1] = -chord[2]; h[3][2] = chord[1]; h[4][0] = chord[2]; h[4][2] = -chord[0]; h[5][0] = -chord[1]; h[5][1] = chord[0]
    coupled = rv_wide.mul6(r, h, tip, False)
    anchored = rv_wide.mul6(r, coupled, h, True)
    k = [[Fr(0)] * 12 for _ in range(12)]
    for i in range(6):
        for j in range(6):
            k[i][j] = anchored[i][j]; k[i][j + 6] = -coupled[i][j]; k[i + 6][j] = -coupled[j][i]; k[i + 6][j + 6] = tip[i][j]
    return rv_wide.rotate(r, k, info["axes"]), info

if __name__ == "__main__":
    # sanity of the emulator at p = 53 against hardware binary64
    a53 = W.P(53)
    import random
    rng = random.Random(131)
    for _ in range(2000):
        x, y_ = rng.uniform(-1e3, 1e3), rng.uniform(1e-3, 1e3)
        assert a53.add(x, y_) == Fr(x + y_) and a53.mul(x, y_) == Fr(x * y_) and a53.div(x, y_) == Fr(x / y_) and a53.sqrt(y_) == Fr(math.sqrt(y_))
    print("emulator: p=53 add/mul/div/sqrt bit-equal to hardware binary64 on 2000 random pairs")
    V = [("KD5 p128 closed (1-cos from rounded cos)", 128, "closed", "actual", False),
         ("KD5 p128 stable (1-cos = 2 s^2)", 128, "stable", "actual", False),
         ("KD5 p192 closed", 192, "closed", "actual", False),
         ("M31b0 p128 closed (formula chord at p)", 128, "closed", "formula_p", False),
         ("M31b0 p128 stable", 128, "stable", "formula_p", False),
         ("M31b p128 (binary64 formula chord)", 128, "closed", "actual", True)]
    for plane in ("IP", "SK"):
        for phi in (1e-9, 1.5e-9, 2e-9, 3e-9, 5e-9, 1e-8, 2e-8, 1e-6, 1e-4, math.pi / 36):
            ph, R, out = run(plane, phi, V)
            print("%s phi %.4e R %.6e" % (plane, ph, R))
            for name, relK, (t, at) in out:
                print("   %-44s relK %.2e  trigger %.4e at dof %s  %s" % (name, relK, t, at, "DEMOTES" if t > 1 else ""))
