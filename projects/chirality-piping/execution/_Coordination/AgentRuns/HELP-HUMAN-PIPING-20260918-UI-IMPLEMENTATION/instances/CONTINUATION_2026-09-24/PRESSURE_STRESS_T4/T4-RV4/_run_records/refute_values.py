"""T4-RV4: independent refutation of T4-I8's rebuilt straight references.

Standard library only. No product module is imported; no product output is read.
Inputs: T4-I8's rebuilt_reference_cases.json (the object under test) and, for the
twin, the frozen fixture SOURCE_ODWALL_EXPECTATIONS.json (passed by path).

Methods differ from T4-I8's wherever one exists:
- radial/hoop/axial: a generalized-plane-strain 3D elasticity solve in Lame
  constants (u_r = A r + B/r, uniform eps_z), boundary conditions solved as a
  linear system, instead of Hooke's compliance with C = P/As;
- section: I = pi (ro^4 - ri^4)/4 directly, As = pi (ro^2 - ri^2);
- transverse: virtual work (unit-load integrals of M m / EI) for deflections
  and rotations, and load integration for V, M, instead of closed-form double
  integration or a stiffness solve;
- axial reactions from nodal free bodies with the cap ledger.
Every row of every T4-I8 load case is then recomputed from (kind, entity,
component, location) and compared EXACTLY (rational * pi^k) with T4-I8's value.

Usage: python -I refute_values.py <rebuilt_reference_cases.json> <SOURCE_ODWALL_EXPECTATIONS.json>
"""
import json
import sys
from decimal import Decimal, getcontext
from fractions import Fraction as F

getcontext().prec = 60
FAILS = []
NCHK = [0]


def chk(label, ok):
    NCHK[0] += 1
    if not ok:
        FAILS.append(label)
        print("FAIL", label)


# ---------- exact values: (rational, power of pi) ----------
class X:
    __slots__ = ("r", "k")

    def __init__(self, r, k=0):
        self.r = F(r)
        self.k = k if self.r != 0 else 0

    def __add__(self, o):
        o = o if isinstance(o, X) else X(o)
        if self.r == 0:
            return o
        if o.r == 0:
            return self
        assert self.k == o.k, (self, o)
        return X(self.r + o.r, self.k)

    def __neg__(self):
        return X(-self.r, self.k)

    def __sub__(self, o):
        return self + (-(o if isinstance(o, X) else X(o)))

    def __mul__(self, o):
        o = o if isinstance(o, X) else X(o)
        return X(self.r * o.r, self.k + o.k)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = o if isinstance(o, X) else X(o)
        return X(self.r / o.r, self.k - o.k)

    def __eq__(self, o):
        o = o if isinstance(o, X) else X(o)
        return self.r == o.r and (self.k == o.k or self.r == 0)

    def __repr__(self):
        return f"{self.r}*pi^{self.k}"

    def f(self):
        pi = Decimal("3.14159265358979323846264338327950288419716939937510582097494459")
        return float(Decimal(self.r.numerator) / Decimal(self.r.denominator) * pi ** self.k)


def from_json(q):
    e = q["exact"]
    k = {"rational": 0, "rational_times_pi": 1, "rational_over_pi": -1}.get(e["kind"])
    if k is None:
        return None
    return X(F(e["rational"]), k)


PI = X(1, 1)


# ---------- generalized plane strain (Lame constants) ----------
def gps(od, t, E, nu, p, alpha_dT, axial):
    """axial = ('restrained',) -> eps_z = 0; ('free_transfer',) -> int sigma_z dA = p pi ri^2.
    Returns dict of exact stresses (rational, Pa) and eps_z."""
    ro = F(od) / 2
    ri = ro - F(t)
    E, nu, p, th = F(E), F(nu), F(p), F(alpha_dT)
    lam = E * nu / ((1 + nu) * (1 - 2 * nu))
    mu = E / (2 * (1 + nu))
    beta = (3 * lam + 2 * mu) * th           # thermal stress modulus * strain
    # unknowns A, B, ez ; sigma_r(r) = 2(l+m)A - 2m B/r^2 + l ez - beta
    def sr_row(r):
        return [2 * (lam + mu), -2 * mu / (r * r), lam]
    rows = [sr_row(ri), sr_row(ro)]
    rhs = [-p + beta, F(0) + beta]
    if axial == "restrained":
        rows.append([F(0), F(0), F(1)])
        rhs.append(F(0))
    else:
        # sigma_z = 2 l A + (l+2m) ez - beta ; sigma_z (ro^2 - ri^2) = p ri^2
        rows.append([2 * lam, F(0), lam + 2 * mu])
        rhs.append(p * ri * ri / (ro * ro - ri * ri) + beta)
    # Cramer
    def det(m):
        return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
    D = det(rows)
    sol = []
    for c in range(3):
        m = [row[:] for row in rows]
        for i in range(3):
            m[i][c] = rhs[i]
        sol.append(det(m) / D)
    A, B, ez = sol
    sr = lambda r: 2 * (lam + mu) * A - 2 * mu * B / (r * r) + lam * ez - beta
    sh = lambda r: 2 * (lam + mu) * A + 2 * mu * B / (r * r) + lam * ez - beta
    sz = 2 * lam * A + (lam + 2 * mu) * ez - beta
    return {"ro": ro, "ri": ri, "sr_i": sr(ri), "sr_o": sr(ro), "sh_i": sh(ri), "sh_o": sh(ro), "sz": sz, "ez": ez}


def section(od, t):
    ro = F(od) / 2
    ri = ro - F(t)
    return {"As": X(ro ** 2 - ri ** 2, 1), "Ai": X(ri ** 2, 1), "I": X((ro ** 4 - ri ** 4) / 4, 1), "ro": ro, "ri": ri}


# ---------- piecewise-polynomial exact integration ----------
def poly_int(coeffs, a, b):
    """integral_a^b sum c_n x^n dx"""
    return sum(F(c) * (F(b) ** (n + 1) - F(a) ** (n + 1)) / (n + 1) for n, c in enumerate(coeffs))


def pmul(p1, p2):
    out = [F(0)] * (len(p1) + len(p2) - 1)
    for i, a in enumerate(p1):
        for j, b in enumerate(p2):
            out[i + j] += F(a) * F(b)
    return out


# ---------- model-specific references ----------
def axial_rows_member(st, P, As):
    """Wall/effective/membrane, Lame; endpoint actions."""
    Nw = X(st["sz"]) * As
    return Nw, Nw - P, X(st["sz"])


def compare_case(label, lc, mine):
    """mine: dict key (kind, entity, component, location) -> X. Compare every row exactly, both ways."""
    exp = lc["expected"]
    seen = set()
    for r in lc["rows"]:
        key = (r["kind"], r["entity_ref"], r["component"], r["location"])
        seen.add(key)
        if key not in mine:
            chk(f"{label}: row {key} not in independent model", False)
            continue
        theirs = from_json(exp[r["expected"]])
        ok = theirs == mine[key]
        if not ok:
            print("   theirs", theirs, "mine", mine[key])
        chk(f"{label}: {key}", ok)
        # zero rows: scale positive; nonzero: relative criterion
        if mine[key].r == 0:
            chk(f"{label}: zero criterion {key}", r["criterion"]["kind"] == "zero_scale" and r["criterion"]["absolute_tolerance"] > 0)
        else:
            chk(f"{label}: relative criterion {key}", r["criterion"]["kind"] == "relative" and r["criterion"]["relative_tolerance"] == 1e-9)
    for key in mine:
        chk(f"{label}: independent row {key} present in T4-I8 rows", key in seen)
    return len(seen)


STN = [("end_i", F(0)), ("quarter_1", F(1, 4)), ("midspan", F(1, 2)), ("quarter_3", F(3, 4)), ("end_j", F(1))]
TK = [("element_local_shear_force_y", "shear_force_y"), ("element_local_shear_force_z", "shear_force_z"),
      ("element_local_torsional_moment", "torsional_moment"), ("element_local_bending_moment_y", "bending_moment_y"),
      ("element_local_bending_moment_z", "bending_moment_z")]


def pressure_block(mine, pipe, Nw, S, sz, st):
    for loc, _ in STN:
        mine[("pipe_wall_axial_force_v2", pipe, "wall_axial_force", loc)] = Nw
        mine[("pipe_effective_axial_force_v2", pipe, "effective_axial_force", loc)] = S
        mine[("pipe_axial_membrane_stress_v2", pipe, "axial_membrane_stress", loc)] = sz
        mine[("pipe_lame_radial_stress_v2", pipe, "lame_inner_radial_stress", loc)] = X(st["sr_i"])
        mine[("pipe_lame_radial_stress_v2", pipe, "lame_outer_radial_stress", loc)] = X(st["sr_o"])
        mine[("pipe_lame_hoop_stress_v2", pipe, "lame_inner_hoop_stress", loc)] = X(st["sh_i"])
        mine[("pipe_lame_hoop_stress_v2", pipe, "lame_outer_hoop_stress", loc)] = X(st["sh_o"])
    # node-on-element wall action: tension pulls end i toward -x, end j toward +x
    mine[("pipe_wall_endpoint_action_v2", pipe, "wall_axial_end_action", "end_i")] = -Nw
    mine[("pipe_wall_endpoint_action_v2", pipe, "wall_axial_end_action", "end_j")] = Nw


def transverse_block(mine, pipe, values):
    for loc, _ in STN:
        vy, mz = values.get(loc, (X(0), X(0)))
        for kind, comp in TK:
            mine[(kind, pipe, comp, loc)] = vy if comp == "shear_force_y" else (mz if comp == "bending_moment_z" else X(0))


def node_block(mine, node, ux=X(0), uy=X(0), rz=X(0)):
    for ax, v in (("x", ux), ("y", uy), ("z", X(0))):
        mine[(f"global_nodal_displacement_{ax}", node, f"nodal_displacement_{ax}", "node")] = v  # metres (JSON stores m)
    for ax, v in (("x", X(0)), ("y", X(0)), ("z", rz)):
        mine[(f"global_nodal_rotation_{ax}", node, f"nodal_rotation_{ax}", "node")] = v


def support_block(mine, sup, comps):
    for c, v in zip(["Fx", "Fy", "Fz", "Mx", "My", "Mz"], comps):
        mine[("support_reaction_component_v2", sup, c, "node")] = v


def case1(doc):
    c = doc["cases"]["milltol_lame_membrane"]
    od, t_nom, ca, mill = F(1, 5), F(1, 100), F(1, 500), F(1, 800)
    # fold: retired t_eff = t_nom - ca - mill with OD fixed (retired id = OD - 2 t_eff)
    t_eff = t_nom - ca - mill
    authored = F(c["variants"]["free_transferring"]["documents"]["v2_model_0.3.0"]["model"]["pipe_segments"][0]["section"]["wall_thickness"]["value"]).limit_denominator(10 ** 9)
    mill_doc = F(c["variants"]["free_transferring"]["documents"]["v2_model_0.3.0"]["model"]["pipe_segments"][0]["section"]["mill_tolerance"]["value"]).limit_denominator(10 ** 9)
    chk("case1 document wall 0.008 and mill 0.00125 reproduce the retired t_eff", authored - mill_doc == t_eff and authored == F(1, 125))
    sec = section(od, t_eff)
    E, nu, p, L = 200 * 10 ** 9, F(3, 10), 2000, F(2)
    P = X(p) * sec["Ai"]
    out = {}
    for key, axial in (("free_transferring", "free"), ("axially_restrained_transferring", "restrained")):
        st = gps(od, t_eff, E, nu, p, 0, axial)
        Nw, S, sz = axial_rows_member(st, P, sec["As"])
        mine = {}
        pressure_block(mine, "pipe:A-B", Nw, S, sz, st)
        transverse_block(mine, "pipe:A-B", {})
        node_block(mine, "node:A")
        node_block(mine, "node:B", ux=X(st["ez"] * L))
        # node free bodies on the x axis: cap -P at A (outward), +P at B; wall tension pulls A +x, B -x
        RA = P - Nw          # -P + Nw + R = 0
        support_block(mine, "support:A", [RA] + [X(0)] * 5)
        if axial == "restrained":
            RB = Nw - P      # +P - Nw + R = 0
            support_block(mine, "support:B", [RB] + [X(0)] * 5)
            chk("case1 restrained global x balance", RA + RB == 0)
        lc = list(c["variants"][key]["load_cases"].values())[0]
        n = compare_case(f"case1/{key}", lc, mine)
        out[key] = {"rows": n, "Nw": Nw, "sz": sz, "hoop_i": st["sh_i"], "ux_B": st["ez"] * L}
    # realistic wrong product the discriminator list lacks: Ai from the authored (un-reduced) bore 0.1-0.008
    ri_auth = od / 2 - authored
    wrong_sz = X(p) * X(ri_auth ** 2, 1) / sec["As"]
    out["wrong_Ai_authored_bore_sigma_z_free"] = wrong_sz
    listed = [from_json(dd["wrong"]) for dd in c["wrong_result_discriminators"]]
    out["listed_contains_authored_bore"] = any(w == wrong_sz for w in listed)
    return out


def case2(doc):
    c = doc["cases"]["tp_phys_pressure_halves"]
    od, t = F(1, 5), F(1, 100)
    E, nu, alpha, dT, p = 200 * 10 ** 9, F(3, 10), F(12, 10 ** 6), F(5), 2 * 10 ** 6
    xs = [F(0), F(3, 2), F(9, 2), F(6)]
    L = xs[-1]
    q, a, b = F(-300), F(3, 2), F(9, 2)
    sec = section(od, t)
    EI = X(E) * sec["I"]
    P = X(p) * sec["Ai"]
    nodes = ["node:A", "node:B", "node:C", "node:D"]
    pipes = ["pipe:A-B", "pipe:B-C", "pipe:C-D"]

    # statics by load integration: action of the right part on the left part at x
    def V(x):
        lo, hi = max(F(x), a), b
        return q * (hi - lo) if hi > lo else F(0)

    def M(x):
        lo, hi = max(F(x), a), b
        if hi <= lo:
            return F(0)
        return q * poly_int([-F(x), 1], lo, hi)    # int (s - x) q ds

    # unit-load (virtual work) deflection and rotation at x0
    def M_poly_pieces():
        # M(x) as polynomials on [0,a], [a,b], [b,L]
        p1 = [q * (b - a) * (a + b) / 2, -q * (b - a)]                   # q(b-a)(a+b-2x)/2
        p2 = [q * b * b / 2, -q * b, q / 2]                              # q(b-x)^2/2
        return [(F(0), a, p1), (a, b, p2), (b, L, [F(0)])]

    pieces = M_poly_pieces()
    for (lo, hi, pp) in pieces:
        for x in (lo, (lo + hi) / 2, hi):
            val = sum(cc * x ** n for n, cc in enumerate(pp))
            chk(f"case2 M polynomial == load-integrated M at {x}", val == M(x))

    def defl(x0):
        tot = F(0)
        for lo, hi, pp in pieces:
            hi2 = min(hi, x0)
            if hi2 > lo:
                tot += poly_int(pmul(pp, [x0, -1]), lo, hi2)   # m(x) = x0 - x
        return X(tot) / EI

    def rot(x0):
        tot = F(0)
        for lo, hi, pp in pieces:
            hi2 = min(hi, x0)
            if hi2 > lo:
                tot += poly_int(pp, lo, hi2)                  # m(x) = 1
        return X(tot) / EI

    out = {}
    for cid, th in (("case:pressure-half", False), ("case:combined", True)):
        st = gps(od, t, E, nu, p, alpha * dT if th else 0, "restrained")
        Nw, S, sz = axial_rows_member(st, P, sec["As"])
        mine = {}
        for m, pipe in enumerate(pipes):
            pressure_block(mine, pipe, Nw, S, sz, st)
            vals = {}
            if th:
                x0, x1 = xs[m], xs[m + 1]
                for loc, s in STN:
                    x = x0 + s * (x1 - x0)
                    if loc == "end_i":
                        vals[loc] = (X(-V(x)), X(-M(x)))     # node-on-element at i = -(right-on-left)
                    else:
                        vals[loc] = (X(V(x)), X(M(x)))       # j-side cut and node-on-element at j
            transverse_block(mine, pipe, vals)
        for nid, x in zip(nodes, xs):
            node_block(mine, nid, ux=X(0), uy=defl(x) if th else X(0), rz=rot(x) if th else X(0))
        # anchor A: Fy, Mz from whole-pipe equilibrium; Fx from node-A free body with cap -P
        W = q * (b - a)
        Mq = q * poly_int([0, 1], a, b)       # moment of the load about A
        RAx, RDx = P - Nw, Nw - P
        support_block(mine, "support:A", [RAx, X(-W) if th else X(0), X(0), X(0), X(0), X(-Mq) if th else X(0)])
        support_block(mine, "support:D", [RDx] + [X(0)] * 5)
        chk(f"{cid}: global x balance (caps -P at A, +P at D)", RAx + RDx + (-P) + P == 0)
        lc = c["load_cases"][cid]
        n = compare_case(f"case2/{cid}", lc, mine)
        out[cid] = {"rows": n, "Nw": Nw, "S": S, "sz": sz, "uyD": defl(L) if th else None, "rzD": rot(L) if th else None}
        # magnitudes block
        mag = lc["support_magnitudes"]
        fa = (RAx.f() ** 2 + (float(-W) if th else 0.0) ** 2) ** 0.5
        chk(f"{cid}: support:A force magnitude", abs(mag["support:A"]["force_magnitude"]["value"] - fa) <= 1e-15 * fa)
        chk(f"{cid}: support:D force magnitude", abs(mag["support:D"]["force_magnitude"]["value"] - abs(RDx.f())) <= 1e-15 * abs(RDx.f()))
    # retired 009 transverse half at q=-2, EI=2000 (convention witness)
    s = F(-2) / q
    chk("009 tip uy -0.070875 via unit load", (defl(L) * EI).r * s / 2000 == F(-70875, 10 ** 6))
    chk("009 tip rz -0.014625 via unit load", (rot(L) * EI).r * s / 2000 == F(-14625, 10 ** 6))
    out["EI"] = EI
    return out


def case3(doc):
    c = doc["cases"]["pressure_membrane_thin_wall_limit"]
    p, rm, t = 100, F(3), F(1, 2)
    od = 2 * rm + t
    E, nu, L = 200 * 10 ** 9, F(3, 10), F(65)
    sec = section(od, t)
    P = X(p) * sec["Ai"]
    st = gps(od, t, E, nu, p, 0, "free")
    Nw, S, sz = axial_rows_member(st, P, sec["As"])
    mine = {}
    pressure_block(mine, "pipe:A-B", Nw, S, sz, st)
    transverse_block(mine, "pipe:A-B", {})
    node_block(mine, "node:A")
    node_block(mine, "node:B", ux=X(st["ez"] * L))
    support_block(mine, "support:A", [P - Nw] + [X(0)] * 5)
    n = compare_case("case3", c["load_cases"]["case:membrane-free"], mine)
    thin_h, thin_l, mean_h = F(p) * rm / t, F(p) * rm / (2 * t), F(p) * (rm - t / 2) / t
    rel = {"inner": (thin_h - st["sh_i"]) / st["sh_i"], "outer": (thin_h - st["sh_o"]) / st["sh_o"],
           "mean": (thin_h - mean_h) / mean_h, "sz": (thin_l - st["sz"]) / st["sz"]}
    comp = c["thin_wall_comparison"]
    chk("case3 rel inner", from_json(comp["relative_difference_thin_hoop_vs_lame_inner"]) == X(rel["inner"]))
    chk("case3 rel outer", from_json(comp["relative_difference_thin_hoop_vs_lame_outer"]) == X(rel["outer"]))
    chk("case3 rel mean", from_json(comp["relative_difference_thin_hoop_vs_mean_hoop_p_ri_over_t"]) == X(rel["mean"]))
    chk("case3 rel sz", from_json(comp["relative_difference_thin_longitudinal_vs_sigma_z_free"]) == X(rel["sz"]))
    # through-thickness mean hoop from the Lame field (integral of sigma_h dr / t) equals p ri / t
    ro, ri = sec["ro"], sec["ri"]
    Cc = F(p) * ri * ri / (ro * ro - ri * ri)
    Dd = Cc * ro * ro
    mean_from_field = (Cc * (ro - ri) + Dd * (1 / ri - 1 / ro)) / t
    chk("case3 mean hoop from field == p ri/t", mean_from_field == mean_h)
    return {"rows": n, "rel": rel, "sh_i": st["sh_i"], "sh_o": st["sh_o"], "sz": st["sz"]}


def twin(path):
    fx = json.load(open(path))
    c0 = fx["cases"][0]
    inp = c0["inputs"]
    od, t, p, E, nu, L, Fy, Mx = (F(inp[k]) for k in ("OD_m", "wall_m", "p_Pa", "E_Pa", "nu", "L_m", "tip_Fy_N", "tip_Mx_Nm"))
    sec = section(od, t)
    G = E / (2 * (1 + nu))
    J = sec["I"] * 2
    st = gps(od, t, E, nu, p, 0, "free")
    P = X(p) * sec["Ai"]
    vals = {"A_m2": sec["As"], "Ai_m2": sec["Ai"], "I_m4": sec["I"], "J_m4": J, "Z_m3": sec["I"] / X(sec["ro"]), "P_N": P,
            "free_pressure_extension_m": X(st["ez"] * L), "axial_membrane_Pa": X(st["sz"]),
            "lame_inner_hoop_Pa": X(st["sh_i"]), "lame_outer_hoop_Pa": X(st["sh_o"]), "lame_inner_radial_Pa": X(st["sr_i"]),
            "lame_outer_radial_Pa": X(st["sr_o"]),
            # unit-load cantilever: v(L) = int_0^L (Fy (L-x)) (L-x) dx / EI ; theta = int Fy (L-x) dx / EI
            "tip_bending_y_m": X(Fy * poly_int(pmul([L, -1], [L, -1]), 0, L)) / (X(E) * sec["I"]),
            "tip_rotation_z_rad": X(Fy * poly_int([L, -1], 0, L)) / (X(E) * sec["I"]),
            "tip_rotation_x_rad": X(Mx * L) / (X(G) * J),
            "torsional_surface_shear_Pa": X(Mx * sec["ro"]) / J,
            "root_force_Fy_N": X(-Fy), "root_moment_Mz_Nm": X(-Fy * L), "root_moment_Mx_Nm": X(-Mx)}
    worst = 0.0
    for k, v in vals.items():
        ref = c0[k]["f64"]
        mine = v.f()
        rel = 0.0 if ref == mine == 0 else abs(mine - ref) / abs(ref)
        worst = max(worst, rel)
        chk(f"twin {k} binary64-identical to fixture", mine == ref)
    # maximum |normal| at the root fibre: sigma_z + |M(0)|/Z, with Z = I/ro (pi kept exact: (rational + rational/pi))
    pi = Decimal("3.14159265358979323846264338327950288419716939937510582097494459")
    Zr = (sec["I"] / X(sec["ro"])).r
    mx = Decimal(st["sz"].numerator) / Decimal(st["sz"].denominator) + Decimal((Fy * L / Zr).numerator) / Decimal((Fy * L / Zr).denominator) / pi
    chk("twin maximum_absolute_normal_stress binary64-identical", float(mx) == c0["maximum_absolute_normal_stress_Pa"]["f64"])
    return {"n": len(vals) + 1, "worst": worst}


def discriminators(doc):
    """Separation of each wrong value from its correct value, in units of the 1e-9 criterion."""
    rows = []
    cs = doc["cases"]
    m = cs["milltol_lame_membrane"]
    mf = list(m["variants"]["free_transferring"]["load_cases"].values())[0]["expected"]
    mr = list(m["variants"]["axially_restrained_transferring"]["load_cases"].values())[0]["expected"]
    tgt = {"lame_inner_hoop": mf["lame_inner_hoop"], "sigma_z (free)": mf["sigma_z"], "sigma_z (restrained)": mr["sigma_z"], "Nw (restrained)": mr["Nw"]}
    for dd in m["wrong_result_discriminators"]:
        rows.append(("case1", dd["id"], tgt[dd["quantity"]]["value"], dd["wrong"]["value"]))
    t = cs["tp_phys_pressure_halves"]
    nm = {"Nw": "Nw", "S": "S", "support:A Fx": "A_Fx", "pipe:A-B midspan bending_moment_z": "A-B_midspan_bending_moment_z", "node:D uy": "D_uy"}
    for dd in t["wrong_result_discriminators"]:
        rows.append(("case2", dd["id"], t["load_cases"][dd["case"]]["expected"][nm[dd["quantity"]]]["value"], dd["wrong"]["value"]))
    c3 = cs["pressure_membrane_thin_wall_limit"]["load_cases"]["case:membrane-free"]["expected"]
    for dd in cs["pressure_membrane_thin_wall_limit"]["wrong_result_discriminators"]:
        names = ["lame_inner_hoop", "lame_outer_hoop"] if "outer" in dd["quantity"] else (["sigma_z"] if dd["quantity"] == "sigma_z" else ["lame_inner_hoop"])
        for n in names:
            rows.append(("case3", dd["id"] + "/" + n, c3[n]["value"], dd["wrong"]["value"]))
    out = []
    for case, ident, good, bad in rows:
        sep = abs(good - bad) / (1e-9 * max(abs(good), abs(bad)))
        out.append((case, ident, good, bad, sep))
    return out


def zero_floor_audit(doc):
    """For each zero row: tolerance / (eps * largest same-unit magnitude in the load case)."""
    eps = 2.0 ** -52
    res = []
    for ck, c in doc["cases"].items():
        holders = [c] + list(c.get("variants", {}).values())
        for h in holders:
            for cid, lc in h.get("load_cases", {}).items():
                exp = lc["expected"]
                big = {}
                for r in lc["rows"]:
                    v = abs(exp[r["expected"]]["value"])
                    u = exp[r["expected"]]["unit"]
                    big[u] = max(big.get(u, 0.0), v)
                worst = None
                for r in lc["rows"]:
                    if exp[r["expected"]]["value"] != 0:
                        continue
                    u = exp[r["expected"]]["unit"]
                    tol = r["criterion"]["absolute_tolerance"]
                    ref = big.get(u, 0.0)
                    ratio = tol / (eps * ref) if ref else float("inf")
                    if worst is None or ratio < worst[0]:
                        worst = (ratio, r["kind"], r["entity_ref"], r["component"], r["location"], tol, ref)
                res.append((ck, cid, worst))
    return res


def main():
    doc = json.load(open(sys.argv[1]))
    r1 = case1(doc)
    r2 = case2(doc)
    r3 = case3(doc)
    tw = twin(sys.argv[2])
    print("case1 rows compared:", r1["free_transferring"]["rows"], r1["axially_restrained_transferring"]["rows"])
    print("case1 free: Nw", r1["free_transferring"]["Nw"], "sigma_z", r1["free_transferring"]["sz"], "hoop_i", r1["free_transferring"]["hoop_i"], "uB", r1["free_transferring"]["ux_B"])
    print("case1 restrained: Nw", r1["axially_restrained_transferring"]["Nw"], "sigma_z", r1["axially_restrained_transferring"]["sz"])
    print("case1 wrong (Ai from authored bore 0.092, As reduced) sigma_z free =", r1["wrong_Ai_authored_bore_sigma_z_free"], "=", repr(r1["wrong_Ai_authored_bore_sigma_z_free"].f()),
          "; in T4-I8 discriminator list:", r1["listed_contains_authored_bore"])
    for cid in ("case:pressure-half", "case:combined"):
        v = r2[cid]
        print(f"case2 {cid} rows compared: {v['rows']}; Nw {v['Nw']} S {v['S']} sigma_z {v['sz']}")
    print("case2 EI", r2["EI"], "uy(D)", r2["case:combined"]["uyD"], "rz(D)", r2["case:combined"]["rzD"])
    print("case3 rows compared:", r3["rows"], "; sh_i", r3["sh_i"], "sh_o", r3["sh_o"], "sz", r3["sz"], "; rel", {k: str(v) for k, v in r3["rel"].items()})
    print(f"twin: {tw['n']} fixture values re-derived by a second route; worst relative difference {tw['worst']:.1e}")
    print("discriminators (separation in units of the 1e-9 criterion; minimum shown first):")
    ds = sorted(discriminators(doc), key=lambda x: x[4])
    for case, ident, good, bad, sep in ds:
        print(f"  {case} {ident}: correct {good!r} wrong {bad!r} separation {sep:.3e}")
        chk(f"discriminator {case}/{ident} separated by > 1e3 criteria", sep > 1e3)
    print("zero-floor audit (tolerance / (eps * largest same-unit value in the case); smallest per load case):")
    for ck, cid, w in zero_floor_audit(doc):
        if w:
            print(f"  {ck}/{cid}: ratio {w[0]:.3e} at {w[1]} {w[2]} {w[3]} {w[4]}; tol {w[5]:.3e}; largest same-unit {w[6]:.3e}")
    print(f"checks: {NCHK[0]}, failures: {len(FAILS)}")
    print("RESULT:", "PASS" if not FAILS else "FAIL")
    return 0 if not FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
