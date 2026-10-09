"""T4-I6 Part B items 4-5: T3's curved models re-derived under the T4-U1 element,
the formula-chord mutant and M31b kill models, and the large-coordinate controls.

usage: python -I t3_models.py KD5_MODELS_RS RV5_MODELS_RS PART1_JSON OUT_JSON
  KD5_MODELS_RS : git show ed012c7ccf:P/core/solver/nonlinear_integration/src/structural_adapter/kd5_models.rs
  RV5_MODELS_RS : git show <NUM>:I/NUMERICAL_INTEGRITY_T3/REVIEW/_run_records/kd5_review/m31b/exact_inputs/rv5_models.rs.txt
  PART1_JSON    : freeze_u1.py output (element cases)
Standard library only. Imports curved_ref.py from this script's directory.
"""
import sys, os, re, ast, json, math, platform, time, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decimal import Decimal as D, getcontext, localcontext
import curved_ref as C

getcontext().prec = 80
R03 = 0.3
SECTION = dict(e=200000000000.0, g=80000000000.0, a=0.005969026041820614, i=2.700984283923829e-05, j=5.401968567847658e-05)


# ------------------------------------------------------------------ parsing
MEMBER_RE = re.compile(r"MemberData \{ i: (\d+), j: (\d+), y_reference: (\[[^\]]*\]), bend: (None|Some\(\((\[[^\]]*\]), ([^)]*)\)\)) \}")


def parse_models(path):
    text = open(path).read()
    models = {}
    for block in re.findall(r"pub\(super\) const (\w+): ModelData = ModelData \{(.*?)\n\};", text, re.S):
        name, body = block
        m = {"name": name}
        for line in body.strip().splitlines():
            line = line.strip().rstrip(",")
            key, _, val = line.partition(": ")
            if key == "name":
                continue
            if key == "section":
                inner = re.findall(r"(\w+): ([-0-9.e+]+)", val)
                m["section"] = {k: float(v) for k, v in inner}
            elif key == "members":
                mem = []
                for mm in MEMBER_RE.finditer(val):
                    bend = None
                    if mm.group(4) != "None":
                        bend = (ast.literal_eval(mm.group(5)), float(mm.group(6)))
                    mem.append({"i": int(mm.group(1)), "j": int(mm.group(2)),
                                "y_reference": ast.literal_eval(mm.group(3)), "bend": bend})
                m["members"] = mem
            else:
                m[key] = ast.literal_eval(val.replace("&[", "["))
        models[name] = m
    return models


# ------------------------------------------------------------------ assembly and solve
def element_matrix(mem, nodes, sec, bend_mode, chord=None):
    xi, xj = nodes[mem["i"]], nodes[mem["j"]]
    if mem["bend"] is None:
        return C.frame_element(xi, xj, mem["y_reference"], sec["e"], sec["g"], sec["a"], sec["i"], sec["i"], sec["j"])
    R, yref, k = bend_mode(mem, nodes)
    return C.curved_element(xi, xj, R, yref, sec["e"], sec["g"], sec["a"], sec["i"], sec["j"], k, k, chord=chord)["K"]


def solve_model(m, mats):
    n = 6 * len(m["nodes"])
    K = [[D(0)] * n for _ in range(n)]
    for mem, Ke in zip(m["members"], mats):
        dof = [6 * mem["i"] + r for r in range(6)] + [6 * mem["j"] + r for r in range(6)]
        for a in range(12):
            for b in range(12):
                K[dof[a]][dof[b]] += C.dec(Ke[a][b])
    for d_, v in m["springs"]:
        K[d_][d_] += C.dec(v)
    f = [D(0)] * n
    for d_, v in m["loads"]:
        f[d_] += C.dec(v)
    free = [d_ for d_ in range(n) if d_ not in m["rigid"]]
    Kf = [[K[a][b] for b in free] for a in free]
    u = C.solve(Kf, [f[a] for a in free])
    return dict(zip(free, u)), (Kf, free)


def actual_ratio(m, uref, u):
    """kd5_tests.rs:204 actual_ratio (S* per D1 4.1.6.1): max |u - u_ref| / (1e-9 max(|u_ref|, S*))."""
    st = max((abs(v) for d_, v in uref.items() if d_ % 6 < 3), default=D(0))
    sr = max((abs(v) for d_, v in uref.items() if d_ % 6 >= 3), default=D(0))
    ext = []
    for k in range(3):
        vals = [C.dec(p[k]) for p in m["nodes"]]
        ext.append(max(vals) - min(vals))
    lb = C.norm(ext)
    tr, ro = max(st, lb * sr), max(sr, st / lb)
    worst, at = D(0), None
    for d_, v in uref.items():
        sc = max(abs(v), tr if d_ % 6 < 3 else ro)
        r = abs(C.dec(u[d_]) - v) / (D("1e-9") * sc)
        if r > worst:
            worst, at = r, d_
    return worst, at


def bow_vector(mem, nodes):
    xi = [C.dec(v) for v in nodes[mem["i"]]]
    xj = [C.dec(v) for v in nodes[mem["j"]]]
    c = [C.dec(v) for v in mem["bend"][0]]
    mid = [(xi[k] + xj[k]) / 2 for k in range(3)]
    b = C.sub(mid, c)
    return b


def consistent(yref, mem, nodes):
    """y_ref projected normal to d must point along the old arc's bow (same plane, same side)."""
    xi = [C.dec(v) for v in nodes[mem["i"]]]
    xj = [C.dec(v) for v in nodes[mem["j"]]]
    d = C.sub(xj, xi)
    dh = C.scale(1 / C.norm(d), d)
    y = [C.dec(v) for v in yref]
    yp = C.sub(y, C.scale(C.dot(y, dh), dh))
    b = bow_vector(mem, nodes)
    bp = C.sub(b, C.scale(C.dot(b, dh), dh))
    cosang = C.dot(yp, bp) / (C.norm(yp) * C.norm(bp))
    return cosang > 1 - D("1e-12")


def new_mode_factory(overrides):
    def mode(mem, nodes):
        key = (mem["i"], mem["j"])
        if key in overrides:
            return overrides[key]
        return R03, mem["y_reference"], mem["bend"][1]
    return mode


def regenerate_inputs(m):
    """R = 0.3 (the generators' radius), y_ref = member y_reference if it bows to
    the old centre's side, else the binary64 bow vector (mid - centre)/|.|."""
    out = {}
    notes = []
    for mem in m["members"]:
        if mem["bend"] is None:
            continue
        xi = [C.dec(v) for v in m["nodes"][mem["i"]]]
        xj = [C.dec(v) for v in m["nodes"][mem["j"]]]
        c = [C.dec(v) for v in mem["bend"][0]]
        ri, rj = C.norm(C.sub(xi, c)), C.norm(C.sub(xj, c))
        if consistent(mem["y_reference"], mem, m["nodes"]):
            y = list(mem["y_reference"])
            src = "member y_reference (in the old arc's plane, on its bow side)"
        else:
            b = bow_vector(mem, m["nodes"])
            nb = C.norm(b)
            y = [float(v / nb) for v in b]
            src = "binary64 (mid - centre)/|mid - centre|: the member y_reference is unused by today's element and does not lie along the old arc's bow"
        out[(mem["i"], mem["j"])] = (R03, y, mem["bend"][1])
        notes.append({"member": [mem["i"], mem["j"]], "R": R03, "y_reference": y, "y_reference_source": src,
                      "old_centre": list(mem["bend"][0]), "old_radii_rel_mismatch": C.sci((ri - rj) / max(ri, rj), 3),
                      "old_mean_radius_minus_0.3": C.sci((ri + rj) / 2 - C.dec(R03), 3), "k": mem["bend"][1]})
    return out, notes


def b64_round_matrix(M):
    return [[float(v) for v in row] for row in M]


# ------------------------------------------------------------------ binary64 formula chord (the mutant)
def formula_chord_b64(xi, xj, R, correctly_rounded_trig=False):
    d = [xj[k] - xi[k] for k in range(3)]
    L = math.sqrt(d[0] * d[0] + d[1] * d[1] + d[2] * d[2])
    phi = 2.0 * math.asin(L / (2.0 * R))
    if correctly_rounded_trig:
        with localcontext() as c:
            c.prec = 60
            cphi = float(C.cos(C.dec(phi)))
            sphi = float(C.sin(C.dec(phi)))
    else:
        cphi, sphi = math.cos(phi), math.sin(phi)
    return [R * (cphi - 1.0), R * sphi, 0.0], phi, cphi, sphi


def cantilever(name, xi, xj, R, yref, k=1.0, springs=1.0e6):
    return {"name": name, "section": SECTION, "nodes": [list(xi), list(xj)],
            "members": [{"i": 0, "j": 1, "y_reference": list(yref), "bend": ((0.0, 0.0, 0.0), k)}],
            "rigid": [0, 1, 2], "springs": [(3, springs), (4, springs), (5, springs)],
            "loads": [(9, 1.0), (10, 1.0), (11, 1.0)]}


def run_cantilever(m, R, yref, k=1.0, mutant_variants=True):
    sec = m["section"]
    mode = lambda mem, nodes: (R, yref, k)
    Kc = element_matrix(m["members"][0], m["nodes"], sec, mode)
    u_int, (Kf, free) = solve_model(m, [Kc])
    res = {"u_int": u_int}
    if mutant_variants:
        for tag, cr in (("libm", False), ("correctly_rounded", True)):
            chord, phi_b, cphi, sphi = formula_chord_b64(m["nodes"][0], m["nodes"][1], R, cr)
            Km = element_matrix(m["members"][0], m["nodes"], sec, mode, chord=chord)
            u_mut, _ = solve_model(m, [Km])
            ratio, at = actual_ratio(m, u_int, u_mut)
            el = C.curved_element(m["nodes"][0], m["nodes"][1], R, yref, sec["e"], sec["g"], sec["a"], sec["i"], sec["j"], k, k)
            dc = [C.dec(chord[q]) - el["c_act"][q] for q in range(3)]
            res["mutant_" + tag] = {"ratio": ratio, "at": at, "phi_b": phi_b, "cos_phi_b": cphi, "sin_phi_b": sphi,
                                    "chord_b64": chord, "dc_over_L": C.norm(dc) / el["geo"]["L"],
                                    "dc": dc, "u_mut": u_mut}
    # correctly rounded binary64 element matrix, exact solve (formation representation estimate)
    u_cr, _ = solve_model(m, [b64_round_matrix(Kc)])
    res["cr_ratio"] = actual_ratio(m, u_int, u_cr)
    # equilibrated 1-norm condition of the reduced matrix (exact)
    dsc = [abs(Kf[i][i]).sqrt() for i in range(len(Kf))]
    Ks = [[Kf[i][j] / (dsc[i] * dsc[j]) for j in range(len(Kf))] for i in range(len(Kf))]
    Ki = C.inverse(Ks)
    n1 = max(sum(abs(Ks[i][j]) for i in range(len(Ks))) for j in range(len(Ks)))
    n1i = max(sum(abs(Ki[i][j]) for i in range(len(Ki))) for j in range(len(Ki)))
    res["cond1_equilibrated"] = n1 * n1i
    # M31b0: the formula chord evaluated exactly at the definition's phi equals the actual chord
    el = C.curved_element(m["nodes"][0], m["nodes"][1], R, yref, sec["e"], sec["g"], sec["a"], sec["i"], sec["j"], k, k)
    g = el["geo"]
    fc = [g["R"] * (g["cosp"] - 1), g["R"] * g["sinp"], D(0)]
    res["m31b0_formula_minus_actual_over_L"] = C.norm([fc[q] - el["c_act"][q] for q in range(3)]) / g["L"]
    res["phi"] = g["phi"]
    return res


def fmt_u(u):
    return {str(k): C.sci(v, 20) for k, v in sorted(u.items())}


# ------------------------------------------------------------------ legacy radius check emulation (cross-check only)
def legacy_pp_centre_and_cb_check(xi, xj, R, yref):
    """Today's PP centre (lib.rs:7766-7846@ed012c7ccf, source order) and CB's radius
    check (curved_bend/src/lib.rs:150-163). Binary64, a labelled emulation."""
    chord = [xj[0] - xi[0], xj[1] - xi[1], xj[2] - xi[2]]
    L = math.sqrt(chord[0] * chord[0] + chord[1] * chord[1] + chord[2] * chord[2])
    h = 0.5 * L
    cu = [chord[0] / L, chord[1] / L, chord[2] / L]
    ax = yref[0] * cu[0] + yref[1] * cu[1] + yref[2] * cu[2]
    pn = [yref[0] - ax * cu[0], yref[1] - ax * cu[1], yref[2] - ax * cu[2]]
    pm = math.sqrt(pn[0] * pn[0] + pn[1] * pn[1] + pn[2] * pn[2])
    s = math.sqrt(R * R - h * h)
    c = [0.5 * (xi[k] + xj[k]) - s * pn[k] / pm for k in range(3)]
    ri_v = [xi[k] - c[k] for k in range(3)]
    rj_v = [xj[k] - c[k] for k in range(3)]
    ri = math.sqrt(ri_v[0] * ri_v[0] + ri_v[1] * ri_v[1] + ri_v[2] * ri_v[2])
    rj = math.sqrt(rj_v[0] * rj_v[0] + rj_v[1] * rj_v[1] + rj_v[2] * rj_v[2])
    mism = abs(ri - rj) / max(ri, rj)
    return c, mism, mism > 1e-9


def main(kd5_path, rv5_path, part1, out):
    t0 = time.time()
    doc = json.load(open(part1))
    kd5 = parse_models(kd5_path)
    rv5 = parse_models(rv5_path)
    report = []
    models_out = []

    # ---------------------------------------------- B4: T3's models
    curved_kd5 = ["E1", "E6", "CSKEW_8_5", "CSKEW_30_RADIUS_MISMATCH", "CPLANAR_60", "CSKEW_30_N122", "PP_UTM_2"]
    curved_rv5 = ["RV5_CANT90_PLANAR", "RV5_CANT60_PLANAR", "RV5_CANT30_SKEW", "RV5_CANT10_SKEW", "RV5_PP_UTM",
                  "RV5_CSKEW30_K30"]
    extra = []
    # R5_4's soft-spring skew elbow at k_X = 10 and 9 (constructed like CSKEW_8_5: load k_X*1e-6 at node 1 rx)
    for kx in (10.0, 9.0):
        m = json.loads(json.dumps(kd5["CSKEW_8_5"]))
        m["name"] = "CSKEW_%g" % kx
        m["springs"] = [(3, kx), (4, 1000000.0), (5, 1000000.0)]
        m["loads"] = [(9, kx * 1e-06)]
        m["u_int"] = []
        m["members"][0]["bend"] = (tuple(m["members"][0]["bend"][0]), m["members"][0]["bend"][1])
        extra.append(m)
    # PP-route (formation_check_runtime.rs PP_UTM_5E5 / PP_UTM_5E6) and the review's UTM elbows
    pp_route = [
        ("PP_UTM_5E5 (formation_check_runtime.rs:358)", [500000.0, 350000.0, 0.0], [500000.010469849, 350000.0001827519, 0.0],
         [(3, 1e-06), (4, 1e-06), (5, 1e-06), (6, -1.8287001134315171e-10), (7, 1.0479998171669618e-08), (8, -1.0297158446337196e-08), (9, 1.0024314433163164e-06), (10, 1.0019471998915866e-06), (11, 1.0019385480234911e-06)]),
        ("PP_UTM_5E6 (formation_check_runtime.rs:379)", [5000000.0, 3500000.0, 0.0], [5000000.026146723, 3500000.0011415905, 0.0],
         [(3, 1e-06), (4, 1e-06), (5, 1e-06), (6, -1.1434351901457734e-09), (7, 2.6210121544675173e-08), (8, -2.5067176622443854e-08), (9, 1.0061076233272944e-06), (10, 1.004902172644534e-06), (11, 1.0048463700931492e-06)]),
        ("review PP-UTM-5e6-phi2", [5000000.0, 3500000.0, 0.0], [5000000.010469849, 3500000.000182752, 0.0], None),
        ("review PP-UTM-7.3e6-phi10", [7300000.0, 5110000.0, 0.0], [7300000.052094453, 5110000.004557674, 0.0], None),
    ]
    all_models = [kd5[n] for n in curved_kd5] + [rv5[n] for n in curved_rv5] + extra
    for m in all_models:
        overrides, notes = regenerate_inputs(m)
        mode = new_mode_factory(overrides)
        mats = [element_matrix(mem, m["nodes"], m["section"], mode) for mem in m["members"]]
        u_new, _ = solve_model(m, mats)
        entry = {"model": m["name"], "source": "kd5_models.rs@ed012c7ccf" if m["name"] in kd5 else ("rv5_models.rs.txt (T3 REVIEW)" if m["name"] in rv5 else "constructed like CSKEW_8_5 (R5_4 table)"),
                 "regenerated_bend_inputs": notes, "u_int_new": fmt_u(u_new)}
        if m.get("u_int"):
            old = {d_: C.dec(v) for d_, v in m["u_int"]}
            r_old, at = actual_ratio(m, u_new, old)
            entry["old_u_int_vs_new_ratio"] = C.sci(r_old, 4)
            entry["old_u_int_vs_new_at_dof"] = at
        # formation-representation estimate: correctly rounded binary64 element matrices, exact solve
        u_cr, _ = solve_model(m, [b64_round_matrix(M) for M in mats])
        r_cr, at_cr = actual_ratio(m, u_new, u_cr)
        entry["estimate_correctly_rounded_K_ratio"] = C.sci(r_cr, 4)
        models_out.append(entry)
        report.append((m["name"], entry.get("old_u_int_vs_new_ratio", "-"), entry["estimate_correctly_rounded_K_ratio"]))
    for label, xi, xj, old in pp_route:
        m = cantilever(label, xi, xj, R03, [0.0, 1.0, 0.0])
        mats = [element_matrix(m["members"][0], m["nodes"], SECTION, lambda mem, nodes: (R03, [0.0, 1.0, 0.0], 1.0))]
        u_new, _ = solve_model(m, mats)
        entry = {"model": label, "source": "PP request (bend_radius 0.3 m, y_reference +y, OD 0.2 m, t 0.01 m, E 2e11, G 8e10)",
                 "nodes": [xi, xj], "u_int_new": fmt_u(u_new)}
        if old:
            r_old, at = actual_ratio(m, u_new, {d_: C.dec(v) for d_, v in old})
            entry["old_u_int_vs_new_ratio"] = C.sci(r_old, 4)
            entry["old_u_int_vs_new_at_dof"] = at
        c, mism, refused = legacy_pp_centre_and_cb_check(xi, xj, R03, [0.0, 1.0, 0.0])
        entry["legacy_centre_emulation"] = {"centre": c, "radius_mismatch_rel": mism, "refused_today": refused}
        u_cr, _ = solve_model(m, [b64_round_matrix(mats[0])])
        entry["estimate_correctly_rounded_K_ratio"] = C.sci(actual_ratio(m, u_new, u_cr)[0], 4)
        models_out.append(entry)
        report.append((label, entry.get("old_u_int_vs_new_ratio", "-"), entry["estimate_correctly_rounded_K_ratio"]))

    # ---------------------------------------------- B5(a): the formula-chord mutant and M31b kill
    G30 = 2.0 ** -30

    def g(v):
        return round(v / G30) * G30
    kill = []
    specs = []
    for plane, dhat, yref in (("IP", [math.cos(math.pi / 6), math.sin(math.pi / 6), 0.0], [0.0, 1.0, 0.0]),
                              ("SK", [1.0 / 3.0, 2.0 / 3.0, 2.0 / 3.0], [1.0, -1.0, 0.5])):
        d = [g(0.3 * c) for c in dhat]
        for label, phi_nom in (("1E-8", 1e-8), ("2E-8", 2e-8), ("5E-8", 5e-8), ("1E-6", 1e-6), ("1E-4", 1e-4), ("5DEG", math.pi / 36), ("90DEG", math.pi / 2)):
            with localcontext() as c:
                c.prec = 60
                Ld = C.norm([C.dec(v) for v in d])
                R = float(Ld / (2 * C.sin(C.dec(phi_nom) / 2)))
            specs.append((f"K1-{plane}-{label}", d, R, yref))
    # near pi, mutant with the naive binary64 phi (R fixed by |d| and the nominal angle)
    for plane, dhat, yref in (("IP", [math.cos(math.pi / 6), math.sin(math.pi / 6), 0.0], [0.0, 1.0, 0.0]),):
        d = [g(0.6 * c) for c in dhat]
        for label, eps in (("PI-1E-6", 1e-6), ("PI-1E-7", 1e-7)):
            with localcontext() as c:
                c.prec = 60
                Ld = C.norm([C.dec(v) for v in d])
                R = float(Ld / (2 * C.sin((C.pi() - C.dec(eps)) / 2)))
            specs.append((f"K1-{plane}-{label}", d, R, yref))
    for name, d, R, yref in specs:
        for X, tag in ((0.0, "X0"), (5.0e6, "X5e6")):
            xi = [X, X * 0.7, 0.0]
            xj = [xi[k] + d[k] for k in range(3)]
            assert all(xj[k] - xi[k] == d[k] for k in range(3))
            m = cantilever(name, xi, xj, R, yref)
            res = run_cantilever(m, R, yref)
            kill.append({
                "model": name + "-" + tag, "nodes": [xi, xj], "R": R, "y_reference": yref,
                "phi": C.sci(res["phi"], 20),
                "supports": "N0 UX,UY,UZ rigid; N0 RX,RY,RZ springs 1e6 N*m/rad; tip moment (1,1,1) N*m at N1",
                "u_int": fmt_u(res["u_int"]),
                "mutant_libm": {"ratio": C.sci(res["mutant_libm"]["ratio"], 4), "at_dof": res["mutant_libm"]["at"],
                                "phi_b": res["mutant_libm"]["phi_b"], "cos_phi_b": res["mutant_libm"]["cos_phi_b"],
                                "sin_phi_b": res["mutant_libm"]["sin_phi_b"], "chord_b64": res["mutant_libm"]["chord_b64"],
                                "dc_over_L": C.sci(res["mutant_libm"]["dc_over_L"], 4),
                                "u_mut": fmt_u(res["mutant_libm"]["u_mut"])},
                "mutant_correctly_rounded_trig": {"ratio": C.sci(res["mutant_correctly_rounded"]["ratio"], 4),
                                                  "cos_phi_b": res["mutant_correctly_rounded"]["cos_phi_b"],
                                                  "dc_over_L": C.sci(res["mutant_correctly_rounded"]["dc_over_L"], 4)},
                "estimate_correctly_rounded_K_ratio": C.sci(res["cr_ratio"][0], 4),
                "cond1_equilibrated_exact": C.sci(res["cond1_equilibrated"], 4),
                "m31b0_formula_at_p_minus_actual_over_L": C.sci(res["m31b0_formula_minus_actual_over_L"], 3),
            })
    # ---------------------------------------------- B5(b) / B3: UTM elbows refused today (legacy emulation), frozen K
    rng = random.Random(20261009)
    found = []
    tried = {}
    for X in (5.0e6, 7.3e6):
        tried[X] = [0, 0]
        while sum(1 for f in found if f["X"] == X) < 4 and tried[X][0] < 5000:
            tried[X][0] += 1
            phi = math.radians(rng.uniform(5.0, 175.0))
            # random chord direction and plane; ordinary decimal coordinates (mm resolution)
            u = [rng.gauss(0, 1) for _ in range(3)]
            nu = math.sqrt(sum(v * v for v in u))
            u = [v / nu for v in u]
            w = [rng.gauss(0, 1) for _ in range(3)]
            L = 2 * R03 * math.sin(phi / 2)
            xi = [round(X + rng.uniform(0, 1000), 3), round(0.7 * X + rng.uniform(0, 1000), 3), round(rng.uniform(0, 100), 3)]
            xj = [xi[k] + L * u[k] for k in range(3)]
            xj = [float("%.9f" % v) for v in xj]
            c, mism, refused = legacy_pp_centre_and_cb_check(xi, xj, R03, w)
            if refused:
                tried[X][1] += 1
                if mism > 2e-9:
                    found.append({"X": X, "x_i": xi, "x_j": xj, "y_reference": w, "legacy_mismatch": mism})
    controls = []
    for f in found:
        el = C.curved_element(f["x_i"], f["x_j"], R03, f["y_reference"], SECTION["e"], SECTION["g"], SECTION["a"], SECTION["i"], SECTION["j"], 1.0, 1.0)
        nres = D(0)
        for _, mvec in C.rigid_modes(f["x_i"], f["x_j"]):
            for r in range(12):
                s = sum((el["K"][r][cc] * mvec[cc] for cc in range(12)), D(0))
                den = sum((abs(el["K"][r][cc] * mvec[cc]) for cc in range(12)), D(0))
                nres = max(nres, abs(s) / den)
        controls.append({"X": f["X"], "x_i": f["x_i"], "x_j": f["x_j"], "R": R03, "y_reference": f["y_reference"], "k": 1.0,
                         "section": SECTION, "phi": C.sci(el["geo"]["phi"], 20),
                         "legacy_emulation_radius_mismatch_rel": f["legacy_mismatch"], "legacy_emulation_refused": True,
                         "K_global": [[C.sci(v, 20) for v in row] for row in el["K"]],
                         "rigid_null_residual_row_relative": C.sci(nres, 3)})
    # ---------------------------------------------- the mutant at element level on the frozen base cases
    mut_el = []
    for cse in doc["cases"]:
        if cse["variant"] != "base" or cse["id"].startswith("CB_"):
            continue
        inp = cse["inputs"]
        chord, phi_b, _, _ = formula_chord_b64([0.0, 0.0, 0.0], inp["d"], inp["R"])
        el = C.curved_element([0.0, 0.0, 0.0], inp["d"], inp["R"], inp["y_reference"], inp["E"], inp["G"], inp["A"], inp["I"], inp["J"], cse["k_in"], cse["k_out"], chord=chord)
        ref = [[D(v) for v in row] for row in cse["K_global"]]
        sc = C.max_abs(ref)
        ms = max(abs(el["K"][i][j] - ref[i][j]) for i in range(12) for j in range(12)) / sc
        dg = max(abs(el["K"][i][j] - ref[i][j]) / (ref[i][i] * ref[j][j]).sqrt() for i in range(12) for j in range(12))
        nres = D(0)
        for _, mvec in C.rigid_modes([0.0, 0.0, 0.0], inp["d"]):
            for r in range(12):
                s = sum((el["K"][r][cc] * mvec[cc] for cc in range(12)), D(0))
                den = sum((abs(el["K"][r][cc] * mvec[cc]) for cc in range(12)), D(0))
                if den > 0:
                    nres = max(nres, abs(s) / den)
        mut_el.append({"case": cse["id"], "agreement_matrix_scale": C.sci(ms, 3), "agreement_diag_scaled": C.sci(dg, 3),
                       "null_residual_row_relative": C.sci(nres, 3)})
    doc["mutant_element_level"] = mut_el
    doc["t3_models"] = models_out
    doc["m31b_kill_and_mutant"] = kill
    doc["utm_controls_refused_today"] = {"generator": "random.Random(20261009); phi ~ U(5,175) deg; R 0.3 m; decimal coordinates (mm at node i, 1e-9 m at node j)",
                                         "tried_refused": {repr(k): v for k, v in tried.items()}, "cases": controls}
    doc["run_t3_models"] = {"python": platform.python_version()}
    with open(out, "w") as fh:
        json.dump(doc, fh, indent=1)
        fh.write("\n")
    print("T4-I6 t3_models: python", platform.python_version())
    print("%-46s %-14s %-14s" % ("model", "old_vs_new", "cr_K_estimate"))
    for r in report:
        print("%-46s %-14s %-14s" % r)
    print()
    print("%-22s %-11s %-10s %-10s %-10s %-10s %-9s %-9s" % ("kill model", "phi", "mut libm", "mut CR", "dc/L", "crK est", "cond1", "M31b0"))
    for k_ in kill:
        print("%-22s %-11s %-10s %-10s %-10s %-10s %-9s %-9s" % (k_["model"], k_["phi"][:10], k_["mutant_libm"]["ratio"], k_["mutant_correctly_rounded_trig"]["ratio"],
              k_["mutant_libm"]["dc_over_L"], k_["estimate_correctly_rounded_K_ratio"], k_["cond1_equilibrated_exact"][:9], k_["m31b0_formula_at_p_minus_actual_over_L"]))
    print()
    print("UTM controls (legacy emulation refuses):", {repr(k): v for k, v in tried.items()})
    for c_ in controls:
        print("  X", c_["X"], "phi", c_["phi"][:10], "legacy mismatch %.3e" % c_["legacy_emulation_radius_mismatch_rel"], "null", c_["rigid_null_residual_row_relative"])
    print()
    print("formula-chord mutant at element level (frozen base cases): agreement ms / diag / null residual")
    for r_ in mut_el:
        print("  %-24s %s / %s / %s" % (r_["case"], r_["agreement_matrix_scale"], r_["agreement_diag_scaled"], r_["null_residual_row_relative"]))


if __name__ == "__main__":
    main(*sys.argv[1:5])
