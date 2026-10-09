"""T4-RV5: does the FK unit criterion ("relative 1e-12", no stated floor) accept a correct
binary64 product? A plain binary64 formation of JR section 2 (B = Q^T[...] blocks, Ke = B^T K B,
q = B d, g, U, f = B^T g, RHS = B^T K q_ref) is compared with every exact JSON value: once with
a bare relative test (zero expected values must then be reproduced exactly) and once with a
per-array floor (max |entry| of the same array). Informational; not product evidence.
Usage: python -I rv5_unit_criteria_probe.py <json>
"""
import json
import sys
from fractions import Fraction as Fr

doc = json.load(open(sys.argv[1]))
C = doc["cases"]


def f(s):
    return float(Fr(s))


def S(v):
    return [[0.0, -v[2], v[1]], [v[2], 0.0, -v[0]], [-v[1], v[0], 0.0]]


def form(inp):
    xi, xj = [f(x) for x in inp["x_i"]], [f(x) for x in inp["x_j"]]
    ai, aj = [f(x) for x in inp["a_i_global"]], [f(x) for x in inp["a_j_global"]]
    Q = [[f(x) for x in r] for r in inp["Q_row_major_columns_are_axes"]]
    Ls = f(inp["translation_scale_Ls_m"])
    H21 = [f(x) for x in inp["H_upper_triangle_21_N_m"]]
    H = [[0.0] * 6 for _ in range(6)]
    c = 0
    for i in range(6):
        for j in range(i, 6):
            H[i][j] = H[j][i] = H21[c]
            c += 1
    Dg = [Ls] * 3 + [1.0] * 3
    K = [[H[i][j] / Dg[i] / Dg[j] for j in range(6)] for i in range(6)]
    r = [(xj[k] + aj[k]) - (xi[k] + ai[k]) for k in range(3)]
    Qt = [[Q[j][i] for j in range(3)] for i in range(3)]
    I3 = [[float(i == j) for j in range(3)] for i in range(3)]
    Z3 = [[0.0] * 3 for _ in range(3)]
    bt = [[-x for x in row] for row in I3], [[S(ai)[a][b] + S(r)[a][b] / 2 for b in range(3)] for a in range(3)], I3, [[-S(aj)[a][b] + S(r)[a][b] / 2 for b in range(3)] for a in range(3)]
    br = Z3, [[-x for x in row] for row in I3], Z3, I3
    B = []
    for blocks in (bt, br):
        for a in range(3):
            B.append(sum(([sum(Qt[a][k] * blk[k][b] for k in range(3)) for b in range(3)] for blk in blocks), []))
    Ke = [[sum(B[m][i] * sum(K[m][n] * B[n][j] for n in range(6)) for m in range(6)) for j in range(12)] for i in range(12)]
    qref = [f(x) for x in inp["q_ref"]]
    rhs = [sum(B[m][i] * sum(K[m][n] * qref[n] for n in range(6)) for m in range(6)) for i in range(12)]
    return B, K, Ke, qref, rhs


def compare(label, arrays):
    bare_fail, floor_fail, worst = 0, 0, 0.0
    for name, obs, exp in arrays:
        scale = max(abs(float(e)) for e in exp) or 1.0
        for o, e in zip(obs, exp):
            e = float(e)
            err = abs(o - e)
            if err > 1e-12 * abs(e):
                bare_fail += 1
                if e == 0.0:
                    print("   %s %s: exact 0, binary64 %.3e (bare relative test fails)" % (label, name, o))
            if err > 1e-12 * max(abs(e), scale):
                floor_fail += 1
            worst = max(worst, err / max(abs(e), scale))
    print("%s: bare relative-1e-12 failures %d; with a per-array floor %d (worst %.2e)" % (label, bare_fail, floor_fail, worst))


def ex(v):
    return [Fr(x) for x in (v["exact"] if isinstance(v, dict) else v)]


for cid in ["U3-J1-LATERAL", "U3-J1-COMMON-ROTATION", "U3-J2-ROTATION", "U3-J2-ROTATION-HELD", "U3-OFFSETS",
            "U3-GENERIC-SKEW-OFFSET-PRESTRESS", "U3-FRAME-COVARIANCE", "U3-REVERSAL"]:
    inp, e = C[cid]["inputs"], C[cid]["expected"]
    B, K, Ke, qref, rhs = form(inp)
    d = [f(x) for x in e["d"]]
    q = [sum(B[i][j] * d[j] for j in range(12)) for i in range(6)]
    g = [sum(K[i][j] * (q[j] - qref[j]) for j in range(6)) for i in range(6)]
    U = sum((q[i] - qref[i]) * g[i] for i in range(6)) / 2
    fi = [sum(B[m][i] * g[m] for m in range(6)) for i in range(12)]
    ea = e["end_actions_node_on_element"]
    fe = ex(ea["Fi"]) + ex(ea["Mi"]) + ex(ea["Fj"]) + ex(ea["Mj"])
    compare(cid, [("B", sum(B, []), [Fr(x) for row in e["B"] for x in row]),
                  ("Ke", sum(Ke, []), [Fr(x) for row in e["Ke"] for x in row]),
                  ("RHS", rhs, [Fr(x) for x in e["installed_rhs_BT_K_qref"]]),
                  ("q", q, ex(e["q"])), ("g", g, ex(e["g"])), ("U", [U], [Fr(e["energy"]["exact"])]),
                  ("f", fi, fe)])

# preload relief, node j free: solve the 6x6 node-j block in binary64
pr = C["U3-PRELOAD-RELIEF"]
B, K, Ke, qref, rhs = form(pr["inputs"])
import copy
A = [[Ke[6 + i][6 + j] for j in range(6)] for i in range(6)]
bb = [rhs[6 + i] for i in range(6)]
M = [row[:] + [v] for row, v in zip(A, bb)]
for col in range(6):
    p = max(range(col, 6), key=lambda i: abs(M[i][col]))
    M[col], M[p] = M[p], M[col]
    for i in range(col + 1, 6):
        fac = M[i][col] / M[col][col]
        M[i] = [x - fac * y for x, y in zip(M[i], M[col])]
x = [0.0] * 6
for i in reversed(range(6)):
    x[i] = (M[i][6] - sum(M[i][j] * x[j] for j in range(i + 1, 6))) / M[i][i]
d = [0.0] * 6 + x
q = [sum(B[i][j] * d[j] for j in range(12)) for i in range(6)]
g = [sum(K[i][j] * (q[j] - qref[j]) for j in range(6)) for i in range(6)]
print("U3-PRELOAD-RELIEF node j free: binary64 g =", ["%.3e" % v for v in g], "(exact 0)")
