"""T4-RV5: independent re-solve of T4-I12's system case U3-SYS-DEMO-CONNECTOR-001.

Different method from T4-I12 (exact rationals, Machin pi): Decimal arithmetic at 70
digits, pi by the Gauss-Legendre AGM, a textbook 12x12 Euler-Bernoulli element with
Hermite-consistent uniform loads, the connector by the natural-mode chain
N(L) . blockdiag(Q^T) (offsets zero here), partial-pivot Gaussian elimination.
Inputs are read from the JSON document itself (nodes, pipes, supports, loads, connector
record), so the transport is exercised. Also solves the two discriminator variants
(raw-difference element; P-130 retained in parallel) and reports the margins.

Usage: python -I rv5_system.py <json>
"""
import json
import sys
from decimal import Decimal as D, getcontext

getcontext().prec = 70
FAILS = []
NCHK = [0]


def chk(name, ok):
    NCHK[0] += 1
    if not ok:
        FAILS.append(name)
        print("FAIL", name)


def agm_pi():
    a, b, t, p = D(1), D(1) / D(2).sqrt(), D(1) / D(4), D(1)
    for _ in range(12):
        an = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - an) ** 2
        a = an
        p *= 2
    return (a + b) ** 2 / (4 * t)


PI = agm_pi()

doc = json.load(open(sys.argv[1]))
case = doc["cases"]["U3-SYS-DEMO-CONNECTOR-001"]
model = case["inputs"]["document_v3_0.3.0"]["model"]
conn = case["inputs"]["connector_record"]
chk("connector record in the document equals the separate connector_record", model["components"][0]["objective_connector"] == conn)
chk("pressure_regions empty in every case; no combinations", all(c["pressure_regions"] == [] for c in model["load_cases"]) and model["combinations"] == [])

nodes = {n["id"]: [D(repr(n["position"][k])) for k in "xyz"] for n in model["nodes"]}
order = [n["id"] for n in model["nodes"]]
idx = {nid: i for i, nid in enumerate(order)}
NDOF = 6 * len(order)
mat = model["materials"][0]
E = D(repr(mat["elastic_modulus"]["value"]))
nu = D(repr(mat["poisson_ratio"]["value"]))
alpha = D(repr(mat["thermal_expansion_coefficient"]["value"]))
G = E / (2 * (1 + nu))


def section(p):
    od = D(repr(p["section"]["outside_diameter"]["value"]))
    t = D(repr(p["section"]["wall_thickness"]["value"]))
    ro = od / 2
    ri = ro - t
    A = PI * (ro * ro - ri * ri)          # = pi t (OD - t), written as ro^2 - ri^2
    I = PI * (ro ** 4 - ri ** 4) / 4      # direct annulus formula (not As(ro^2+ri^2)/4)
    J = 2 * I
    return A, I, J


def zeros(n, m):
    return [[D(0)] * m for _ in range(n)]


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def tr(A):
    return [list(r) for r in zip(*A)]


def mv(A, x):
    return [sum(a * b for a, b in zip(row, x)) for row in A]


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def unit(v):
    n = sum(x * x for x in v).sqrt()
    return [x / n for x in v], n


def beam_local(E, G, A, Iy, Iz, J, L):
    k = zeros(12, 12)

    def s(i, j, v):
        k[i][j] = v
        k[j][i] = v
    a, t = E * A / L, G * J / L
    s(0, 0, a); s(6, 6, a); s(0, 6, -a)
    s(3, 3, t); s(9, 9, t); s(3, 9, -t)
    c12, c6, c4, c2 = 12 * E * Iz / L**3, 6 * E * Iz / L**2, 4 * E * Iz / L, 2 * E * Iz / L
    s(1, 1, c12); s(7, 7, c12); s(1, 7, -c12); s(1, 5, c6); s(1, 11, c6); s(5, 7, -c6); s(7, 11, -c6)
    s(5, 5, c4); s(11, 11, c4); s(5, 11, c2)
    c12, c6, c4, c2 = 12 * E * Iy / L**3, 6 * E * Iy / L**2, 4 * E * Iy / L, 2 * E * Iy / L
    s(2, 2, c12); s(8, 8, c12); s(2, 8, -c12); s(2, 4, -c6); s(2, 10, -c6); s(4, 8, c6); s(8, 10, c6)
    s(4, 4, c4); s(10, 10, c4); s(4, 10, c2)
    return k


def rot12(lam):
    R = zeros(12, 12)
    for b in range(4):
        for i in range(3):
            for j in range(3):
                R[3 * b + i][3 * b + j] = lam[i][j]
    return R


pipes = {}
for p in model["pipe_segments"]:
    xi, xj = nodes[p["from"]], nodes[p["to"]]
    ex, L = unit([xj[k] - xi[k] for k in range(3)])
    yr = [D(repr(p["y_reference"][k])) for k in "xyz"]
    pr = sum(a * b for a, b in zip(yr, ex))
    ey, _ = unit([yr[k] - pr * ex[k] for k in range(3)])
    ez = cross(ex, ey)
    lam = [ex, ey, ez]  # rows: local axes in global
    A, I, J = section(p)
    R = rot12(lam)
    Kg = mm(tr(R), mm(beam_local(E, G, A, I, I, J, L), R))
    pipes[p["id"]] = dict(i=idx[p["from"]], j=idx[p["to"]], L=L, lam=lam, R=R, Kg=Kg, A=A)

# reference section identity used by T4-I12: As = pi t (OD - t), I = As (ro^2 + ri^2)/4
A0, I0, _ = section(model["pipe_segments"][0])
chk("section: pi(ro^2-ri^2) == pi t (OD-t) == 0.001127 pi", abs(A0 - PI * D("0.001127")) < D(10) ** -60)
chk("section: pi(ro^4-ri^4)/4 == As(ro^2+ri^2)/4 == 0.001127 pi 0.012985/4", abs(I0 - PI * D("0.001127") * D("0.012985") / 4) < D(10) ** -60)


def natural_modes(L):
    N = zeros(6, 12)
    N[0][0], N[0][6] = D(-1), D(1)
    N[1][1], N[1][7], N[1][5], N[1][11] = D(-1), D(1), -L / 2, -L / 2
    N[2][2], N[2][8], N[2][4], N[2][10] = D(-1), D(1), L / 2, L / 2
    for k in range(3):
        N[3 + k][3 + k], N[3 + k][9 + k] = D(-1), D(1)
    return N


# connector from the record (columns of the row-major matrix are the axes)
Qrm = [[D(x) for x in row] for row in conn["connector_axes_global"]]
Q = Qrm
ni, nj = idx[conn["end_i"]["node_ref"]], idx[conn["end_j"]["node_ref"]]
for end in ("end_i", "end_j"):
    o = conn[end]["offset_local"]
    chk("connector %s offset zero" % end, o["x"] == 0 and o["y"] == 0 and o["z"] == 0)
r = [nodes[order[nj]][k] - nodes[order[ni]][k] for k in range(3)]
xc, Lc = unit(r)
chk("connector: Q proper orthonormal, Q.x = r/|r|", mm(tr(Q), Q) == [[D(int(i == j)) for j in range(3)] for i in range(3)]
    and [Q[k][0] for k in range(3)] == xc)
Ls = D(repr(conn["stiffness"]["translation_scale"]["value"]))
H21 = [D(repr(x)) for x in conn["stiffness"]["upper_triangle"]]
H = zeros(6, 6)
c = 0
for i in range(6):
    for j in range(i, 6):
        H[i][j] = H[j][i] = H21[c]
        c += 1
Dg = [Ls] * 3 + [D(1)] * 3
K = [[H[i][j] / (Dg[i] * Dg[j]) for j in range(6)] for i in range(6)]
chk("connector K = diag(3.2e6, 9e5, 9e5, 6.2e5, 4.8e5, 4.8e5)", [K[i][i] for i in range(6)] == [D("3.2e6"), D("9e5"), D("9e5"), D("6.2e5"), D("4.8e5"), D("4.8e5")])
Qt4 = rot12(tr(Q))
B_obj = mm(natural_modes(Lc), Qt4)
B_raw = zeros(6, 12)
for i in range(3):
    for j in range(3):
        B_raw[i][j] = -Q[j][i]
        B_raw[i][6 + j] = Q[j][i]
        B_raw[3 + i][3 + j] = -Q[j][i]
        B_raw[3 + i][9 + j] = Q[j][i]


def dofmap(a, b):
    return list(range(6 * a, 6 * a + 6)) + list(range(6 * b, 6 * b + 6))


support_dofs = {}
springs = []
for s in model["supports"]:
    n = idx[s["node"]]
    names = ["UX", "UY", "UZ", "RX", "RY", "RZ"]
    support_dofs[s["id"]] = [6 * n + names.index(x) for x in s["restraints"]]
    if s.get("hanger"):
        h = s["hanger"]["stiffness"]
        springs.append((s["id"], 6 * n + names.index(h["dof"]), D(repr(h["value"]["value"]))))
restrained = sorted(d for v in support_dofs.values() for d in v)


def solve_model(case_id, variant):
    Kt = zeros(NDOF, NDOF)
    for pid, p in pipes.items():
        if pid == conn["topology"]["span_ref"] and variant != "parallel":
            continue
        dm = dofmap(p["i"], p["j"])
        for a in range(12):
            for b in range(12):
                Kt[dm[a]][dm[b]] += p["Kg"][a][b]
    Bc = B_raw if variant == "raw" else B_obj
    Kc = mm(tr(Bc), mm(K, Bc))
    dm = dofmap(ni, nj)
    for a in range(12):
        for b in range(12):
            Kt[dm[a]][dm[b]] += Kc[a][b]
    for _, dof, k in springs:
        Kt[dof][dof] += k
    Fv = [D(0)] * NDOF
    lc = next(x for x in model["load_cases"] if x["id"] == case_id)
    for ld in lc["primitive_loads"]:
        val = D(repr(ld["magnitude"]["value"]))
        tgt = ld["target"]
        if tgt["type"] == "node":
            n = idx[tgt["node"]]
            comp = {"global_x": 0, "global_y": 1, "global_z": 2, "rotation_x": 3, "rotation_y": 4, "rotation_z": 5}[ld["direction"]]
            Fv[6 * n + comp] += val
        elif ld["category"] == "thermal":
            p = pipes[tgt["pipe"]]
            P = E * p["A"] * alpha * val
            for k in range(3):
                Fv[6 * p["i"] + k] -= P * p["lam"][0][k]
                Fv[6 * p["j"] + k] += P * p["lam"][0][k]
        else:  # uniform global force per length, Hermite-consistent
            p = pipes[tgt["pipe"]]
            gdir = {"global_x": 0, "global_y": 1, "global_z": 2}[ld["direction"]]
            qg = [D(0)] * 3
            qg[gdir] = val
            ql = mv(p["lam"], qg)
            L = p["L"]
            fl = [D(0)] * 12
            fl[0] = fl[6] = ql[0] * L / 2
            fl[1] = fl[7] = ql[1] * L / 2
            fl[5], fl[11] = ql[1] * L * L / 12, -ql[1] * L * L / 12
            fl[2] = fl[8] = ql[2] * L / 2
            fl[4], fl[10] = -ql[2] * L * L / 12, ql[2] * L * L / 12
            fg = mv(tr(p["R"]), fl)
            dm2 = dofmap(p["i"], p["j"])
            for a in range(12):
                Fv[dm2[a]] += fg[a]
    free = [i for i in range(NDOF) if i not in restrained]
    n = len(free)
    M = [[Kt[a][b] for b in free] + [Fv[a]] for a in free]
    for col in range(n):
        piv = max(range(col, n), key=lambda i: abs(M[i][col]))
        M[col], M[piv] = M[piv], M[col]
        for i in range(col + 1, n):
            f = M[i][col] / M[col][col]
            if f != 0:
                M[i] = [x - f * y for x, y in zip(M[i], M[col])]
    x = [D(0)] * n
    for i in reversed(range(n)):
        x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    u = [D(0)] * NDOF
    for k, i in enumerate(free):
        u[i] = x[k]
    Ku = mv(Kt, u)
    R = [Ku[i] - Fv[i] for i in range(NDOF)]
    reac = {}
    for sid, dofs in support_dofs.items():
        v = [D(0)] * 6
        for d in dofs:
            v[d % 6] = R[d]
        reac[sid] = v
    for sid, dof, k in springs:
        v = reac[sid]
        v[dof % 6] = -k * u[dof]
    dc = [u[i] for i in dofmap(ni, nj)]
    q = mv(Bc, dc)
    g = mv(K, q)
    U = sum(q[i] * K[i][j] * q[j] for i in range(6) for j in range(6)) / 2
    f = mv(tr(Bc), g)
    # balance: applied loads plus reactions, force and moment about the origin
    tot = [D(0)] * 6
    for nid in order:
        n6 = 6 * idx[nid]
        x0 = nodes[nid]
        Fn = [Fv[n6 + k] for k in range(3)]
        Mn = [Fv[n6 + 3 + k] for k in range(3)]
        for k in range(3):
            tot[k] += Fn[k]
        cr = cross(x0, Fn)
        for k in range(3):
            tot[3 + k] += Mn[k] + cr[k]
    for sid, v in reac.items():
        s = next(ss for ss in model["supports"] if ss["id"] == sid)
        x0 = nodes[s["node"]]
        cr = cross(x0, v[0:3])
        for k in range(3):
            tot[k] += v[k]
            tot[3 + k] += v[3 + k] + cr[k]
    return dict(u=u, reac=reac, q=q, g=g, U=U, f=f, tot=tot, F=mv(Q, g[0:3]), M=mv(Q, g[3:6]))


def rel(a, b, floor):
    return abs(D(a) - D(b)) / max(abs(D(b)), D(floor))


exp = case["expected"]
worst = D(0)
for lc in ["load:L-100", "load:L-200", "load:L-300"]:
    sol = solve_model(lc, "connector")
    e = exp[lc]
    fl = e["zero_scale_floors"]
    w = D(0)
    for nid in order:
        n6 = 6 * idx[nid]
        for k in range(3):
            w = max(w, rel(sol["u"][n6 + k], e["displacements"][nid]["u_m"][k], fl["translation_m"]))
            w = max(w, rel(sol["u"][n6 + 3 + k], e["displacements"][nid]["theta_rad"][k], fl["rotation_rad"]))
    key = "reactions_support_on_pipe_global_Fx_Fy_Fz_Mx_My_Mz"
    for sid, v in sol["reac"].items():
        for k in range(6):
            w = max(w, rel(v[k], e[key][sid][k], fl["force_N"] if k < 3 else fl["moment_N_m"]))
    ce = e["connector"]
    for k in range(6):
        w = max(w, rel(sol["q"][k], ce["q_local"][k], fl["q_translation_m"] if k < 3 else fl["q_rotation_rad"]))
        w = max(w, rel(sol["g"][k], ce["g_local"][k], fl["g_force_N"] if k < 3 else fl["g_moment_N_m"]))
    w = max(w, rel(sol["U"], ce["energy_J"], "1e-30"))
    ea = ce["end_actions_node_on_element"]
    blocks = [ea["Fi_at_N-130"], ea["Mi_at_N-130"], ea["Fj_at_N-140"], ea["Mj_at_N-140"]]
    for b in range(4):
        for k in range(3):
            w = max(w, rel(sol["f"][3 * b + k], blocks[b][k], fl["force_N"] if b in (0, 2) else fl["moment_N_m"]))
    for k in range(3):
        w = max(w, rel(sol["F"][k], ce["F_global"][k], fl["force_N"]))
        w = max(w, rel(sol["M"][k], ce["M_global"][k], fl["moment_N_m"]))
    bal = max(abs(x) for x in sol["tot"])
    print("%s: worst normalized difference vs JSON over u, theta, reactions, q, g, U, F, M, end actions = %.2E; |balance| = %.2E"
          % (lc, w, bal))
    chk(lc + " connector solve agrees with JSON to 1e-25 (normalized)", w < D("1e-25"))
    chk(lc + " balance exact to 1e-50", bal < D("1e-50"))
    worst = max(worst, w)
    # discriminators
    dis = case["wrong_result_discriminators"][lc]
    for variant, keyd in (("raw", "raw_difference_element_solve"), ("parallel", "retained_span_in_parallel_solve")):
        sv = solve_model(lc, variant)
        dd = dis[keyd]
        wv = D(0)
        for sid, v in sv["reac"].items():
            for k in range(6):
                wv = max(wv, rel(v[k], dd["reactions"][sid][k], fl["force_N"] if k < 3 else fl["moment_N_m"]))
        if variant == "parallel":
            for k in range(6):
                wv = max(wv, rel(sv["g"][k], dd["connector_g_local"][k], fl["g_force_N"] if k < 3 else fl["g_moment_N_m"]))
        chk("%s %s variant reactions agree with JSON to 1e-17 (20-digit strings)" % (lc, variant), wv < D("1e-17"))
        margins = []
        for comp in dd["discriminating_components"]:
            sid, name = comp.rsplit(".", 1)
            k = ["Fx", "Fy", "Fz", "Mx", "My", "Mz"].index(name)
            m = rel(sv["reac"][sid][k], e[key][sid][k], fl["force_N"] if k < 3 else fl["moment_N_m"])
            margins.append(m)
        mn = min(margins)
        print("   %s variant: min normalized gap on its discriminating components = %.3E (criterion 1e-9; ratio %.1E)"
              % (variant, mn, mn / D("1e-9")))
        chk("%s %s discriminates by > 1e-6 normalized" % (lc, variant), mn > D("1e-6"))
        if variant == "raw":
            imb = sv["tot"]
            print("   raw variant: global imbalance (applied + reactions) F = (%s), M about origin = (%s)" % (
                ", ".join("%.6f" % x for x in imb[:3]), ", ".join("%.6f" % x for x in imb[3:])))
            chk("%s raw imbalance equals JSON statement" % lc, all(abs(imb[3 + k] - D(dd["global_moment_imbalance_about_origin_N_m"][k])) < D("1e-40") for k in range(3))
                and all(abs(imb[k]) < D("1e-40") for k in range(3)))
            # the criterion's moment allowance
            allow = D("1e-9") * D(fl["force_N"]) * D("8.27")
            print("   raw imbalance / balance allowance = %.2E" % (max(abs(x) for x in imb[3:]) / allow))
        # a statically determined component must be the same in the wrong solve (justifies 'listed components only')
    # thermal: P-120 free expansion moves N-130 by alpha dT L in x
    if lc == "load:L-100":
        chk("L-100: N-130 u_x = alpha dT L = 0.00066 exactly (free expansion)", abs(sol["u"][6 * idx["node:N-130"]] - D("0.00066")) < D("1e-60"))

print("worst normalized difference over all three cases: %.2E" % worst)
print("system checks: %d run, %d fail" % (NCHK[0], len(FAILS)))
print("PASS" if not FAILS else "FAIL")
