"""T4-I12 consumer-side check of u3_reference_cases.json (standard library only).

It re-derives the frozen connector values from the inputs recorded in the JSON with a
different formulation than the generator: q from rigid arms to a common midpoint,
q = blockdiag(Q,Q)^T (Gamma_j d_j - Gamma_i d_i), Gamma_k = [[I, -S(b_k)], [0, I]],
b_i = a_i + r/2, b_j = a_j - r/2; end actions from the transposed arms,
f_i = -Gamma_i^T G, f_j = Gamma_j^T G, G = blockdiag(Q,Q) g. It also checks the system
case's statics from the recorded document and the frozen 30-digit values, and the NI
expectations against equilibrium and the friction law.

Usage: python -I check_reference_json.py <u3_reference_cases.json>
"""
import json
import sys
from decimal import Decimal, getcontext
from fractions import Fraction as Fr

getcontext().prec = 80
doc = json.load(open(sys.argv[1]))
N_OK, FAILS = 0, []


def ok(name, cond):
    global N_OK
    print(("ok   " if cond else "FAIL ") + name)
    if cond:
        N_OK += 1
    else:
        FAILS.append(name)


def P(s):
    return Fr(s) if isinstance(s, str) else Fr(s)


def Pv(v):
    return [P(x) for x in v]


def Pm(m):
    return [[P(x) for x in r] for r in m]


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def sub(a, b):
    return [x - y for x, y in zip(a, b)]


def sc(s, a):
    return [s * x for x in a]


def mv(m, v):
    return [sum(x * y for x, y in zip(r, v)) for r in m]


def tr(m):
    return [list(r) for r in zip(*m)]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def arm_q(d, ai, aj, r, Q):
    bi, bj = add(ai, sc(Fr(1, 2), r)), sub(aj, sc(Fr(1, 2), r))
    ui, ti, uj, tj = d[0:3], d[3:6], d[6:9], d[9:12]
    mi = add(ui, cross(ti, bi))  # u + theta x b = u - S(b) theta
    mj = add(uj, cross(tj, bj))
    QT = tr(Q)
    return mv(QT, sub(mj, mi)) + mv(QT, sub(tj, ti))


def arm_f(g, ai, aj, r, Q):
    bi, bj = add(ai, sc(Fr(1, 2), r)), sub(aj, sc(Fr(1, 2), r))
    Fv, Mv = mv(Q, g[0:3]), mv(Q, g[3:6])
    fi = sc(-1, Fv) + sc(-1, add(cross(bi, Fv), Mv))
    fj = Fv + add(cross(bj, Fv), Mv)
    return fi + fj


def K_from(inp):
    Ls = P(inp["translation_scale_Ls_m"])
    u = Pv(inp["H_upper_triangle_21_N_m"])
    H = [[Fr(0)] * 6 for _ in range(6)]
    k = 0
    for i in range(6):
        for j in range(i, 6):
            H[i][j] = H[j][i] = u[k]
            k += 1
    D = [Ls] * 3 + [Fr(1)] * 3
    return [[H[i][j] / (D[i] * D[j]) for j in range(6)] for i in range(6)]


def check_connector(cid, inp, exp):
    xi, xj = Pv(inp["x_i"]), Pv(inp["x_j"])
    ai, aj = Pv(inp["a_i_global"]), Pv(inp["a_j_global"])
    Q = Pm(inp["Q_row_major_columns_are_axes"])
    K = K_from(inp)
    ok(f"{cid}: H with Ls decodes to the recorded physical K", K == Pm(inp["K_physical"]))
    if inp.get("attachment_local"):
        al = inp["attachment_local"]
        ok(f"{cid}: a_i = Q_i offset_i", mv(Pm(al["initial_node_axes_global_i"]), Pv(al["offset_local_i"])) == ai)
        ok(f"{cid}: a_j = Q_j offset_j", mv(Pm(al["initial_node_axes_global_j"]), Pv(al["offset_local_j"])) == aj)
    r = sub(add(xj, aj), add(xi, ai))
    ok(f"{cid}: r", r == Pv(exp["r"]))
    # B column by column from the arm form
    B = Pm(exp["B"])
    for k in range(12):
        e = [Fr(0)] * 12
        e[k] = Fr(1)
        ok(f"{cid}: B column {k} (arm form)", arm_q(e, ai, aj, r, Q) == [B[i][k] for i in range(6)])
    Ke = Pm(exp["Ke"])
    BtKB = [[sum(B[a][i] * K[a][b] * B[b][j] for a in range(6) for b in range(6)) for j in range(12)] for i in range(12)]
    ok(f"{cid}: Ke = B^T K B", Ke == BtKB)
    qref = Pv(inp["q_ref"])
    ok(f"{cid}: installed RHS = B^T K q_ref", Pv(exp["installed_rhs_BT_K_qref"]) == mv(tr(B), mv(K, qref)))
    if "d" in exp:
        d = Pv(exp["d"])
        q = arm_q(d, ai, aj, r, Q)
        ok(f"{cid}: q", q == Pv(exp["q"]["exact"]))
        g = mv(K, sub(q, qref))
        ok(f"{cid}: g", g == Pv(exp["g"]["exact"]))
        ok(f"{cid}: energy", dot(sub(q, qref), g) / 2 == P(exp["energy"]["exact"]))
        f = arm_f(g, ai, aj, r, Q)
        ea = exp["end_actions_node_on_element"]
        ok(f"{cid}: end actions (arm transpose)", f == Pv(ea["Fi"]["exact"]) + Pv(ea["Mi"]["exact"]) + Pv(ea["Fj"]["exact"]) + Pv(ea["Mj"]["exact"]))
        for k_, s in enumerate(exp["q"]["decimal"]):
            ok(f"{cid}: decimal q[{k_}] matches exact to 30 digits", abs(Decimal(s) - Decimal(q[k_].numerator) / Decimal(q[k_].denominator)) <= Decimal("1e-30") * max(Decimal(1), abs(Decimal(s))))


cases = doc["cases"]
for cid in ("U3-J1-LATERAL", "U3-J1-COMMON-ROTATION", "U3-J2-ROTATION", "U3-J2-ROTATION-HELD", "U3-REF-ENDMOMENT",
            "U3-GENERIC-SKEW-OFFSET-PRESTRESS", "U3-OFFSETS", "U3-REVERSAL"):
    check_connector(cid, cases[cid]["inputs"], cases[cid]["expected"])
fc = cases["U3-FRAME-COVARIANCE"]
check_connector("U3-FRAME-COVARIANCE", fc["inputs"], fc["expected"])
cc = cases["U3-COUPLED-H-SCALE-PRELOAD"]
check_connector("U3-COUPLED-H", cc["inputs"]["coupled"], cc["expected"]["coupled"])
pr = dict(cc["inputs"]["coupled"])
pr["q_ref"] = cc["inputs"]["preload_q_ref"]
check_connector("U3-PRELOAD-INSTALLED", pr, cc["expected"]["preload_installed_d0"])
six = cases["U3-SIX-COMPONENTS"]
for k, v in six["expected"].items():
    check_connector(f"U3-SIX-{k}", six["inputs"], v)
# reversal relations between the generic case and its reversal
G, Rv = cases["U3-GENERIC-SKEW-OFFSET-PRESTRESS"]["expected"], cases["U3-REVERSAL"]["expected"]
T = Pm(cases["U3-REVERSAL"]["inputs"]["T"])
ok("reversal: q' = T q", Pv(Rv["q"]["exact"]) == mv(T, Pv(G["q"]["exact"])))
ok("reversal: energy equal", Rv["energy"] == G["energy"])
for a, b in (("Fi", "Fj"), ("Mi", "Mj"), ("Fj", "Fi"), ("Mj", "Mi")):
    ok(f"reversal: {a}' = {b}", Rv["end_actions_node_on_element"][a] == G["end_actions_node_on_element"][b])
# B oracle
bo = cases["U3-B-ORACLE"]
inp = bo["inputs"]
xi, xj, ai, aj, Q = Pv(inp["x_i"]), Pv(inp["x_j"]), Pv(inp["a_i_global"]), Pv(inp["a_j_global"]), Pm(inp["Q_row_major_columns_are_axes"])
r = sub(add(xj, aj), add(xi, ai))
ok("B oracle: r = (2,0,0)", r == [2, 0, 0])
f = arm_f(Pv(inp["g_given"]), ai, aj, r, Q)
ea = bo["expected"]["end_actions_node_on_element"]
ok("B oracle: end blocks (arm transpose)", f == Pv(ea["Fi"]) + Pv(ea["Mi"]) + Pv(ea["Fj"]) + Pv(ea["Mj"]))
q = arm_q(Pv(inp["d_given"]), ai, aj, r, Q)
ok("B oracle: q for d_given", q == Pv(bo["expected"]["q_for_d_given"]))
ok("B oracle: virtual work", dot(Pv(inp["g_given"]), q) == P(bo["expected"]["virtual_work"]) == dot(f, Pv(inp["d_given"])))

# system case: statics from the recorded document and the 30-digit values
sysc = cases["U3-SYS-DEMO-CONNECTOR-001"]
model = sysc["inputs"]["document_v3_0.3.0"]["model"]
nodes = {n["id"]: [Decimal(repr(n["position"][c])) for c in "xyz"] for n in model["nodes"]}
pipes = {p["id"]: (p["from"], p["to"]) for p in model["pipe_segments"]}
sup_node = {s["id"]: s["node"] for s in model["supports"]}
axis = {"global_x": 0, "global_y": 1, "global_z": 2, "rotation_x": 3, "rotation_y": 4, "rotation_z": 5}
for case in model["load_cases"]:
    cid = case["id"]
    e = sysc["expected"][cid]
    Ft, Mt = [Decimal(0)] * 3, [Decimal(0)] * 3

    def addF(x, fv):
        global Ft, Mt
        Ft = [a + b for a, b in zip(Ft, fv)]
        Mt = [a + b for a, b in zip(Mt, [x[1] * fv[2] - x[2] * fv[1], x[2] * fv[0] - x[0] * fv[2], x[0] * fv[1] - x[1] * fv[0]])]
    for ld in case["primitive_loads"]:
        val = Decimal(repr(ld["magnitude"]["value"]))
        ax = axis[ld["direction"]]
        if ld["category"] == "thermal":
            continue  # self-equilibrated pair
        if ld["target"]["type"] == "element":
            a, b = pipes[ld["target"]["pipe"]]
            xa, xb = nodes[a], nodes[b]
            L = sum((p - q_) ** 2 for p, q_ in zip(xa, xb)).sqrt()
            mid = [(p + q_) / 2 for p, q_ in zip(xa, xb)]
            fv = [Decimal(0)] * 3
            fv[ax] = val * L
            addF(mid, fv)
        elif ax < 3:
            fv = [Decimal(0)] * 3
            fv[ax] = val
            addF(nodes[ld["target"]["node"]], fv)
        else:
            Mt[ax - 3] += val
    for sid, rv in e["reactions_support_on_pipe_global_Fx_Fy_Fz_Mx_My_Mz"].items():
        rv = [Decimal(s) for s in rv]
        addF(nodes[sup_node[sid]], rv[0:3])
        Mt = [a + b for a, b in zip(Mt, rv[3:6])]
    fl = e["zero_scale_floors"]
    ok(f"system {cid}: sum of applied loads and frozen reactions = 0 (force, to 1e-25 of the floor)", max(abs(x) for x in Ft) <= Decimal("1e-25") * Decimal(fl["force_N"]))
    ok(f"system {cid}: moment balance about the origin from frozen values (to 1e-25 of floor x 10 m)", max(abs(x) for x in Mt) <= Decimal("1e-24") * Decimal(fl["force_N"]))
    # spring reaction = -k u_z
    uz = Decimal(e["displacements"]["node:N-140"]["u_m"][2])
    ok(f"system {cid}: spring reaction = -42000 u_z", abs(Decimal(e["reactions_support_on_pipe_global_Fx_Fy_Fz_Mx_My_Mz"]["support:SH-140"][2]) + 42000 * uz) < Decimal("1e-22"))
    # connector q from the frozen displacements, g = K q, actions from g (arm form), with decimal inputs
    c = sysc["inputs"]["connector_record"]
    Q = [[Fr(x) for x in row] for row in c["connector_axes_global"]]
    xi, xj = [Fr(str(v)) for v in nodes["node:N-130"]], [Fr(str(v)) for v in nodes["node:N-140"]]
    dd = []
    for nid in ("node:N-130", "node:N-140"):
        dd += [Fr(s) for s in e["displacements"][nid]["u_m"]] + [Fr(s) for s in e["displacements"][nid]["theta_rad"]]
    qv = arm_q(dd, [Fr(0)] * 3, [Fr(0)] * 3, sub(xj, xi), Q)
    Ls = Fr(str(c["stiffness"]["translation_scale"]["value"]))
    Kd = [Fr(x) for i, x in enumerate(c["stiffness"]["upper_triangle"]) if i in (0, 6, 11, 15, 18, 20)]
    Kd = [Kd[k] / (Ls * Ls if k < 3 else 1) for k in range(6)]
    ok(f"system {cid}: connector K diagonal decodes to (3.2e6, 9e5, 9e5, 6.2e5, 4.8e5, 4.8e5)", Kd == [3200000, 900000, 900000, 620000, 480000, 480000])
    qf = [Fr(s) for s in e["connector"]["q_local"]]
    qs, ss = Fr(fl["q_translation_m"]), Fr(fl["q_rotation_rad"])
    ok(f"system {cid}: q from frozen displacements matches frozen q (1e-25 of floor)", all(abs(a - b) <= Fr(1, 10 ** 25) * (qs if k < 3 else ss) for k, (a, b) in enumerate(zip(qv, qf))))
    gf = [Fr(s) for s in e["connector"]["g_local"]]
    ok(f"system {cid}: g = K q (frozen values, 1e-22 relative to floor)", all(abs(Kd[k] * qf[k] - gf[k]) <= Fr(1, 10 ** 22) * Fr(fl["g_force_N"] if k < 3 else fl["g_moment_N_m"]) for k in range(6)))
    fz = arm_f(gf, [Fr(0)] * 3, [Fr(0)] * 3, sub(xj, xi), Q)
    ea = e["connector"]["end_actions_node_on_element"]
    fr = [Fr(s) for s in ea["Fi_at_N-130"] + ea["Mi_at_N-130"] + ea["Fj_at_N-140"] + ea["Mj_at_N-140"]]
    ok(f"system {cid}: end actions from frozen g (arm transpose)", all(abs(a - b) <= Fr(1, 10 ** 25) * 1000 for a, b in zip(fz, fr)))
    # discriminators are distinct from the reference at the criterion
    disc = sysc["wrong_result_discriminators"][cid]
    for name, block in (("raw", disc["raw_difference_element_solve"]["reactions"]), ("parallel", disc["retained_span_in_parallel_solve"]["reactions"])):
        diff = max(abs(Decimal(a) - Decimal(b)) for sid in block for a, b in zip(block[sid], e["reactions_support_on_pipe_global_Fx_Fy_Fz_Mx_My_Mz"][sid]))
        ok(f"system {cid}: {name} discriminator differs by more than 1e-6 x force floor", diff > Decimal("1e-6") * Decimal(fl["force_N"]))

# NI expectations
ni = cases["U3-NI-FRICTION-FRAME"]
blk = ni["inputs"]["frame_block_node1"]
Kxx, Kxy = P(blk["Kxx"]), P(blk["Kxy"])
ok("NI: Kxx = 20 (9/25) + (48/5)(16/25)", Kxx == Fr(20) * Fr(9, 25) + Fr(48, 5) * Fr(16, 25))
ok("NI: Kxy = (20 - 48/5)(3/5)(-4/5)", Kxy == (Fr(20) - Fr(48, 5)) * Fr(3, 5) * Fr(-4, 5))
A = ni["expected"]["assertions"]
mu = Fr(3, 10)
for key, (Fx, Fy) in (("test1_10_-10", (10, -10)), ("test1_-10_-10", (-10, -10))):
    u, n, fr_ = (P(A[key][k]["exact"]) for k in ("u", "normal", "friction"))
    ok(f"NI {key}: Kxx u = Fx + friction", Kxx * u == Fx + fr_)
    ok(f"NI {key}: normal = Kxy u - Fy", n == Kxy * u - Fy)
    ok(f"NI {key}: |friction| = 0.3 |normal|, opposing motion", abs(fr_) == mu * abs(n) and fr_ * u < 0)
    ok(f"NI {key}: binary64 string is the nearest double", repr(float(u)) == A[key]["u"]["binary64"])
for key, (Fx, Fy) in (("test2_10_-1", (10, -1)), ("test2_-10_1", (-10, 1))):
    a = {k: P(v["exact"]) for k, v in A[key].items() if isinstance(v, dict)}
    ok(f"NI {key}: retry iterate equilibrium", Kxx * a["branch_retry_u"] == Fx + a["branch_retry_applied"] and a["branch_retry_Ry"] == Kxy * a["branch_retry_u"] - Fy)
    ok(f"NI {key}: retry normal changed sign against the sticking trial (-Fy)", a["branch_retry_Ry"] * (-Fy) < 0)
    ok(f"NI {key}: retry force built on the assumed branch: f = -s mu sigma Ry with sigma = sign(-Fy)",
       a["branch_retry_applied"] == -(1 if Fx > 0 else -1) * mu * (1 if -Fy > 0 else -1) * a["branch_retry_Ry"])
    ok(f"NI {key}: final equilibrium and friction law", Kxx * a["final_u"] == Fx + a["final_friction"] and a["final_normal"] == Kxy * a["final_u"] - Fy
       and abs(a["final_friction"]) == mu * abs(a["final_normal"]) and a["final_friction"] * a["final_u"] < 0)
    ok(f"NI {key}: final normal keeps the retry's sign", a["final_normal"] * a["branch_retry_Ry"] > 0)
t4 = A["test4"]
ok("NI test4: u = Fx/Kxx with no friction", P(t4["u"]["exact"]) == Fr(10) / Kxx)

# finite rotation: recompute with an independent series at 50 digits
from decimal import Decimal as D
getcontext().prec = 60
for row in cases["U3-FINITE-ROTATION-NEGATIVE"]["expected"]["rows"]:
    L, ph = D(row["L_m"]), D(row["phi_rad"])
    c, s, term, k = D(0), D(0), D(1), 0
    while k < 60:
        c += term if k % 4 == 0 else (-term if k % 4 == 2 else 0)
        s += term if k % 4 == 1 else (-term if k % 4 == 3 else 0)
        k += 1
        term = term * ph / k
    ok(f"finite rotation L={row['L_m']} phi={row['phi_rad']}: qt_x", abs(D(row["qt"][0]) - L * (c - 1)) <= D("1e-38") * abs(L * (c - 1)))
    ok(f"finite rotation L={row['L_m']} phi={row['phi_rad']}: qt_y", abs(D(row["qt"][1]) - L * (s - ph)) <= D("1e-38") * abs(L * (s - ph)))

print(f"consumer checks: {N_OK} pass, {len(FAILS)} fail")
for f_ in FAILS:
    print("FAIL:", f_)
print("PASS" if not FAILS else "FAIL")
sys.exit(1 if FAILS else 0)
