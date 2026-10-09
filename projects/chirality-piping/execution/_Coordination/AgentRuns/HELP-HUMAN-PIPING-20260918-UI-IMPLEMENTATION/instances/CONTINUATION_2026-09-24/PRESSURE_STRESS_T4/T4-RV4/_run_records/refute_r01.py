"""T4-RV4 addendum 01: independent check of T4-I8's repair round 01.

Standard library only; no product module imported, no product output read. Reuses this
directory's refute_values.py (round 00 methods: generalized plane strain, unit-load integrals,
load integration, nodal free bodies), loaded by explicit file path.

Checks:
A. every row of every round-01 load case, both ways, against an independent model that now also
   carries the support norms, the bending/torsion stress rows (j-side section M/Z at all five
   locations, MPa rows over a Pa reference), and the straight elastic maximum per member
   (max over the member of |Nw/As| + |M|/Z, the maximum of |M| found from member ends and
   interior stationary points); symbolic references are compared as decimals;
B. the separate-closures twin: values from a closure-free nodal ledger, and its 0.3.0 document
   rebuilt field for field from PP/tests/pressure_runtime.rs model(true, false, 0.0);
C. T1 transport: every row's reference_origin pointer resolves to its expected quantity, the row
   unit is reached by an exact factor, and zero tolerances equal 1e-9 * scale * factor;
D. nothing else changed: every round-00 quantity, row and document against round 01, with a
   path-level list of every other difference.

Usage: python -I refute_r01.py <round-01 json> <frozen round-00 json> <SOURCE_ODWALL_EXPECTATIONS.json>
"""
import importlib.util
import json
import sys
from decimal import Decimal, getcontext
from fractions import Fraction as F
from pathlib import Path

spec = importlib.util.spec_from_file_location("rv", Path(__file__).resolve().parent / "refute_values.py")
rv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rv)
X, gps, section, poly_int, pmul = rv.X, rv.gps, rv.section, rv.poly_int, rv.pmul
getcontext().prec = 80
PI = Decimal("3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803")
FAILS, NCHK = [], [0]


def chk(label, ok):
    NCHK[0] += 1
    if not ok:
        FAILS.append(label)
        print("FAIL", label)


def xdec(v):
    if isinstance(v, X):
        return Decimal(v.r.numerator) / Decimal(v.r.denominator) * PI ** v.k
    return v


def ref_value(q):
    """I8 quantity -> (X or None, Decimal)."""
    x = rv.from_json(q)
    if x is not None:
        return x, xdec(x)
    return None, Decimal(q["decimal"])


STN = rv.STN
TK = rv.TK
SK = [("element_local_bending_normal_stress_y", "bending_normal_stress_y"),
      ("element_local_bending_normal_stress_z", "bending_normal_stress_z"),
      ("element_local_torsional_shear_stress", "torsional_shear_stress")]


def add_stress_and_max(mine, pipe, sz, Mj, mmax, Z):
    """Mj: loc -> j-side section Mz (X); mmax: max |M| on the member (X); Z exact (X)."""
    for loc, _ in STN:
        mz = Mj.get(loc, X(0))
        for kind, comp in SK:
            mine[(kind, pipe, comp, loc)] = (mz / Z) if comp == "bending_normal_stress_z" else X(0)
    a = X(abs(sz.r), sz.k)
    mine[("pipe_elastic_normal_stress_maximum_v2", pipe, "maximum_absolute_normal_stress", "governing_station")] = (
        a if mmax.r == 0 else xdec(a) + xdec(mmax / Z))


def add_norms(mine, sup, comps):
    for kind, comp, vec in (("support_reaction_force_magnitude_v2", "force_magnitude", comps[:3]),
                            ("support_reaction_moment_magnitude_v2", "moment_magnitude", comps[3:])):
        nz = [v for v in vec if v.r != 0]
        if not nz:
            val = X(0)
        elif len(nz) == 1:
            val = X(abs(nz[0].r), nz[0].k)
        else:
            val = sum((xdec(v) ** 2 for v in nz), Decimal(0)).sqrt()
        mine[(kind, sup, comp, "node")] = val


def compare(label, lc, mine):
    exp, seen = lc["expected"], set()
    for r in lc["rows"]:
        key = (r["kind"], r["entity_ref"], r["component"], r["location"])
        seen.add(key)
        if key not in mine:
            chk(f"{label}: row {key} not in independent model", False)
            continue
        q = exp[r["expected"]]
        x, d = ref_value(q)
        m = mine[key]
        if isinstance(m, X) and x is not None:
            ok = x == m
        else:
            md = xdec(m)
            ok = (md == 0 and d == 0) or (md != 0 and abs(d - md) <= abs(md) * Decimal(10) ** -60)
            ok = ok and float(d) == q["value"]
        if not ok:
            print("   theirs", q["exact"], q["decimal"][:30], "mine", m)
        chk(f"{label}: {key}", ok)
        is_zero = (m.r == 0) if isinstance(m, X) else (m == 0)
        crit = r["criterion"]
        chk(f"{label}: criterion {key}", crit["kind"] == ("zero_scale" if is_zero else "relative"))
    for key in mine:
        chk(f"{label}: independent row {key} present", key in seen)
    return len(seen)


# ---------------------------------------------------------------- case models
def case1(doc):
    c = doc["cases"]["milltol_lame_membrane"]
    od, t_eff = F(1, 5), F(1, 100) - F(1, 500) - F(1, 800)
    sec = section(od, t_eff)
    Z = sec["I"] / X(sec["ro"])
    E, nu, p, L = 200 * 10 ** 9, F(3, 10), 2000, F(2)
    P = X(p) * sec["Ai"]
    n = []
    for key, axial in (("free_transferring", "free"), ("axially_restrained_transferring", "restrained")):
        st = gps(od, t_eff, E, nu, p, 0, axial)
        Nw, S, sz = rv.axial_rows_member(st, P, sec["As"])
        mine = {}
        rv.pressure_block(mine, "pipe:A-B", Nw, S, sz, st)
        rv.transverse_block(mine, "pipe:A-B", {})
        add_stress_and_max(mine, "pipe:A-B", sz, {}, X(0), Z)
        rv.node_block(mine, "node:A")
        rv.node_block(mine, "node:B", ux=X(st["ez"] * L))
        ra = [P - Nw] + [X(0)] * 5
        rv.support_block(mine, "support:A", ra)
        add_norms(mine, "support:A", ra)
        if axial == "restrained":
            rb = [Nw - P] + [X(0)] * 5
            rv.support_block(mine, "support:B", rb)
            add_norms(mine, "support:B", rb)
        lc = list(c["variants"][key]["load_cases"].values())[0]
        n.append(compare(f"case1/{key}", lc, mine))
    # S-3 control
    ri_auth = od / 2 - F(1, 125)
    want = X(2000) * X(ri_auth ** 2, 1) / sec["As"]
    ds = {d["id"]: d for d in c["wrong_result_discriminators"]}
    chk("S-3 cap_area_on_authored_bore == 270848000/20871", rv.from_json(ds["cap_area_on_authored_bore"]["wrong"]) == want
        and want == X(F(270848000, 20871)) and ds["cap_area_on_authored_bore"].get("producible_today") is True)
    chk("S-3 nominal-bore control kept, marked not producible today", ds["cap_area_on_nominal_bore"].get("producible_today") is False
        and ds["cap_area_on_nominal_bore"].get("active_from") == "T4-U6")
    return n, want


def case2(doc):
    c = doc["cases"]["tp_phys_pressure_halves"]
    od, t = F(1, 5), F(1, 100)
    E, nu, alpha, dT, p = 200 * 10 ** 9, F(3, 10), F(12, 10 ** 6), F(5), 2 * 10 ** 6
    xs = [F(0), F(3, 2), F(9, 2), F(6)]
    L, q, a, b = xs[-1], F(-300), F(3, 2), F(9, 2)
    sec = section(od, t)
    EI, Z, P = X(E) * sec["I"], sec["I"] / X(sec["ro"]), X(p) * sec["Ai"]
    nodes, pipes = ["node:A", "node:B", "node:C", "node:D"], ["pipe:A-B", "pipe:B-C", "pipe:C-D"]

    def V(x):
        lo, hi = max(F(x), a), b
        return q * (hi - lo) if hi > lo else F(0)

    def M(x):
        lo, hi = max(F(x), a), b
        return q * poly_int([-F(x), 1], lo, hi) if hi > lo else F(0)

    pieces = [(F(0), a, [q * (b - a) * (a + b) / 2, -q * (b - a)]), (a, b, [q * b * b / 2, -q * b, q / 2]), (b, L, [F(0)])]

    def defl(x0):
        return X(sum(poly_int(pmul(pp, [x0, -1]), lo, min(hi, x0)) for lo, hi, pp in pieces if min(hi, x0) > lo)) / EI

    def rot(x0):
        return X(sum(poly_int(pp, lo, min(hi, x0)) for lo, hi, pp in pieces if min(hi, x0) > lo)) / EI

    def max_abs_M(x0, x1):
        cands = [x0, x1] + [x for x in (b,) if x0 < x < x1]       # V = 0 only for x >= b (M = 0 there)
        return max(abs(M(x)) for x in cands)

    # max |M| check against a dense rational sweep (no stationary point is missed)
    for m in range(3):
        x0, x1 = xs[m], xs[m + 1]
        chk(f"case2 member {m}: max|M| from ends/stationary points == dense sweep",
            max_abs_M(x0, x1) == max(abs(M(x0 + F(k, 240) * (x1 - x0))) for k in range(241)))
    n = {}
    for cid, th in (("case:pressure-half", False), ("case:combined", True)):
        st = gps(od, t, E, nu, p, alpha * dT if th else 0, "restrained")
        Nw, S, sz = rv.axial_rows_member(st, P, sec["As"])
        mine = {}
        for m, pipe in enumerate(pipes):
            rv.pressure_block(mine, pipe, Nw, S, sz, st)
            x0, x1 = xs[m], xs[m + 1]
            vals, Mj = {}, {}
            if th:
                for loc, s in STN:
                    x = x0 + s * (x1 - x0)
                    vals[loc] = (X(-V(x)), X(-M(x))) if loc == "end_i" else (X(V(x)), X(M(x)))
                    Mj[loc] = X(M(x))                         # stresses use the j-side section action, ends included
            rv.transverse_block(mine, pipe, vals)
            add_stress_and_max(mine, pipe, sz, Mj, X(max_abs_M(x0, x1)) if th else X(0), Z)
        for nid, x in zip(nodes, xs):
            rv.node_block(mine, nid, uy=defl(x) if th else X(0), rz=rot(x) if th else X(0))
        W, Mq = q * (b - a), q * poly_int([0, 1], a, b)
        ra = [P - Nw, X(-W) if th else X(0), X(0), X(0), X(0), X(-Mq) if th else X(0)]
        rd = [Nw - P] + [X(0)] * 5
        rv.support_block(mine, "support:A", ra)
        rv.support_block(mine, "support:D", rd)
        add_norms(mine, "support:A", ra)
        add_norms(mine, "support:D", rd)
        lc = c["load_cases"][cid]
        n[cid] = compare(f"case2/{cid}", lc, mine)
        if th:
            ab = xdec(mine[("pipe_elastic_normal_stress_maximum_v2", "pipe:A-B", "maximum_absolute_normal_stress", "governing_station")])
            n["A-B maximum"] = ab
            tagged = sorted(r["entity_ref"] for r in lc["rows"] if r.get("refreeze"))
            chk("S-2: exactly the nonzero uy rows at B, C, D carry the T4-U8 re-freeze tag",
                tagged == ["node:B", "node:C", "node:D"] and all(r["kind"] == "global_nodal_displacement_y" for r in lc["rows"] if r.get("refreeze")))
    chk("S-2: case-2 refreeze block names T4-U8 and the D-6/SP-1 note", c.get("refreeze", {}).get("unit") == "T4-U8" and "sp1_note" in c["refreeze"])
    return n


def case3(doc):
    c = doc["cases"]["pressure_membrane_thin_wall_limit"]
    p, rm, t = 100, F(3), F(1, 2)
    od = 2 * rm + t
    E, nu, L = 200 * 10 ** 9, F(3, 10), F(65)
    sec = section(od, t)
    Z, P = sec["I"] / X(sec["ro"]), X(p) * sec["Ai"]
    st = gps(od, t, E, nu, p, 0, "free")
    Nw, S, sz = rv.axial_rows_member(st, P, sec["As"])
    mine = {}
    rv.pressure_block(mine, "pipe:A-B", Nw, S, sz, st)
    rv.transverse_block(mine, "pipe:A-B", {})
    add_stress_and_max(mine, "pipe:A-B", sz, {}, X(0), Z)
    rv.node_block(mine, "node:A")
    rv.node_block(mine, "node:B", ux=X(st["ez"] * L))
    ra = [P - Nw] + [X(0)] * 5
    rv.support_block(mine, "support:A", ra)
    add_norms(mine, "support:A", ra)
    return compare("case3", c["load_cases"]["case:membrane-free"], mine)


def twin_b(doc):
    c = doc["cases"]["v3_straight_twin_separate_closures"]
    od, t = F(12, 100), F(1, 100)
    E, nu, p, L = 200 * 10 ** 9, F(3, 10), 2 * 10 ** 6, F(6)
    sec = section(od, t)
    Z, P = sec["I"] / X(sec["ro"]), X(p) * sec["Ai"]
    st = gps(od, t, E, nu, p, 0, "restrained")               # both ends held; radial BCs unchanged by the closure type
    Nw, S, sz = rv.axial_rows_member(st, P, sec["As"])
    chk("twin B: Nw = 3000 pi, S = -2000 pi (frozen six-state values)", Nw == X(3000, 1) and S == X(-2000, 1))
    mine = {}
    rv.pressure_block(mine, "pipe:A-B", Nw, S, sz, st)
    rv.transverse_block(mine, "pipe:A-B", {})
    add_stress_and_max(mine, "pipe:A-B", sz, {}, X(0), Z)
    rv.node_block(mine, "node:A")
    rv.node_block(mine, "node:B")
    # closure-free nodal ledger: wall tension pulls A toward +x, B toward -x; no cap load on the pipe
    ra, rb = [-Nw] + [X(0)] * 5, [Nw] + [X(0)] * 5
    rv.support_block(mine, "support:A", ra)
    rv.support_block(mine, "support:B", rb)
    add_norms(mine, "support:A", ra)
    add_norms(mine, "support:B", rb)
    n = compare("twinB", c["load_cases"]["case:pressure-oracle"], mine)
    # document rebuilt from PP/tests/pressure_runtime.rs helpers at ed012c7ccf
    O = "independent_pressure_runtime_oracle"
    term = lambda nid: {"node_ref": nid, "closure_transfer": "separately_supported_or_compensated", "provenance": "explicit_independent_pressure_boundary"}
    anchor = lambda i, nid: {"id": i, "node": nid, "family": "anchor", "restraints": ["UX", "UY", "UZ", "RX", "RY", "RZ"], "provenance": O}
    want = {"model": {
        "schema_version": "0.3.0", "document_kind": "openpipestress.product_preview.model",
        "pressure_contract": {"version": "2.0.0", "mode": "exact_straight_pressure_v2"},
        "project": {"id": "project:pressure-oracle", "units": {"length": "m", "force": "N", "angle": "rad", "pressure": "Pa", "stress": "Pa", "temperature": "degC"}},
        "analysis_status": {"mechanics": "ready_for_preview_diagnostics", "rule_check": "not_performed_user_rule_inputs_missing", "professional_acceptance": "not_provided"},
        "nodes": [{"id": "node:A", "position": {"x": 0.0, "y": 0.0, "z": 0.0}, "provenance": O}, {"id": "node:B", "position": {"x": 6.0, "y": 0.0, "z": 0.0}, "provenance": O}],
        "pipe_segments": [{"id": "pipe:A-B", "from": "node:A", "to": "node:B", "section": {"outside_diameter": {"value": 0.12, "unit": "m"}, "wall_thickness": {"value": 0.01, "unit": "m"}},
                           "material": "material:one", "y_reference": {"x": 0.0, "y": 0.0, "z": 1.0}, "provenance": "synthetic_straight_annulus"}],
        "supports": [anchor("support:A", "node:A"), anchor("support:B", "node:B")], "components": [],
        "materials": [{"id": "material:one", "constitutive_basis": "homogeneous_isotropic_E_nu_v1", "elastic_modulus": {"value": 200e9, "unit": "Pa"},
                       "poisson_ratio": {"value": 0.3, "unit": "1"}, "thermal_expansion_coefficient": {"value": 0.000012, "unit": "1/degC"},
                       "temperature_points": [], "provenance": "synthetic_isotropic_reference_no_catalog"}],
        "load_cases": [{"id": "case:pressure-oracle", "primitive_loads": [], "pressure_regions": [{
            "id": "region:pressure-oracle", "member_pipe_ids": ["pipe:A-B"], "pressure_basis": "internal_differential_zero_external_v1",
            "pressure": {"value": 2e6, "unit": "Pa"}, "terminals": [term("node:A"), term("node:B")], "provenance": "independent_pressure_region"}],
            "provenance": "synthetic_load_case"}], "combinations": []}, "materials": []}
    chk("twin B: 0.3.0 document equals the test's model(true, false, 0.0)", c["documents"]["v2_model_0.3.0"] == want)
    return n


# ---------------------------------------------------------------- transport (S-1)
FACT = {("m", "mm"): Decimal(1000), ("Pa", "MPa"): Decimal(1) / Decimal(10 ** 6)}


def resolve(doc, ptr):
    node = doc
    for raw in ptr[1:].split("/"):
        node = node[raw.replace("~1", "/").replace("~0", "~")]
    return node


def transport(doc):
    nrows = 0
    for ck, c in doc["cases"].items():
        for h in [c] + list(c.get("variants", {}).values()):
            for cid, lc in h.get("load_cases", {}).items():
                for z, zq in lc["zero_scales"].items():
                    chk(f"S-1 {ck}/{cid}: zero scale {z} is a pure maintained quantity", set(zq) == {"unit", "exact", "decimal", "value"})
                    chk(f"S-1 {ck}/{cid}: zero scale {z} has a definition", z in lc.get("zero_scale_definitions", {}))
                for r in lc["rows"]:
                    nrows += 1
                    o = r["reference_origin"]
                    q = resolve(doc, o["pointer"])
                    chk(f"S-1 pointer resolves to the row's expected quantity {ck}/{cid}/{r['kind']}", q is lc["expected"][r["expected"]] or q == lc["expected"][r["expected"]])
                    chk(f"S-1 origin shape {ck}/{cid}/{r['kind']}", o["kind"] == "analytical" and o["transform"] == "identity" and q["unit"] == o["reference_unit"])
                    fac = Decimal(1) if o["reference_unit"] == r["unit"] else FACT[(o["reference_unit"], r["unit"])]
                    if "zero_scale" in o:
                        zs = o["zero_scale"]
                        base = resolve(doc, zs["base"]["pointer"])
                        tol = float(Decimal("1e-9") * abs(Decimal(base["decimal"])) * fac)
                        chk(f"S-1 zero tolerance in row unit {ck}/{cid}/{r['kind']}/{r['entity_ref']}/{r['location']}",
                            r["criterion"]["absolute_tolerance"] == tol and zs["scale_unit"] == base["unit"] == o["reference_unit"])
                    chk(f"S-1 no legacy transform key {ck}/{cid}", "transform" not in r)
    return nrows


# ---------------------------------------------------------------- nothing else changed
def is_q(n):
    return isinstance(n, dict) and "exact" in n and "decimal" in n and "value" in n


def leaves(node, path=""):
    if isinstance(node, dict) and not is_q(node):
        for k, v in node.items():
            yield from leaves(v, f"{path}/{k}")
    elif isinstance(node, list) and not (node and all(isinstance(x, dict) and "kind" in x and "entity_ref" in x for x in node)):
        for i, v in enumerate(node):
            yield from leaves(v, f"{path}/{i}")
    else:
        yield path, node


def unchanged(new, old):
    out = {"quantities_same_path": 0, "zero_scales_def_moved": 0, "moved_magnitudes": 0, "rows_kept": 0}
    oq = {p: v for p, v in leaves(old) if is_q(v)}
    nq = dict(leaves(new))
    missing = []
    for p, v in oq.items():
        if p in nq and nq[p] == v:
            out["quantities_same_path"] += 1
        elif p in nq and is_q(nq[p]) and "definition" in v and {k: x for k, x in v.items() if k != "definition"} == nq[p]:
            out["zero_scales_def_moved"] += 1
            chk(f"definition preserved {p}", resolve(new, p.rsplit("/zero_scales/", 1)[0] + "/zero_scale_definitions")[p.rsplit("/", 1)[1]] == v["definition"])
        else:
            missing.append(p)
    # the side block of round 00 (case 2 support magnitudes) must reappear as rows with equal quantities
    for p in missing:
        ok = False
        if "/support_magnitudes/" in p:
            cid = p.split("/load_cases/")[1].split("/")[0]
            sup = p.split("/support_magnitudes/")[1].split("/")[0]
            comp = p.rsplit("/", 1)[1]
            lc = new["cases"]["tp_phys_pressure_halves"]["load_cases"][cid]
            row = [r for r in lc["rows"] if r["entity_ref"] == sup and r["component"] == comp]
            if len(row) == 1:
                nqv = lc["expected"][row[0]["expected"]]
                ov = oq[p]
                ok = nqv["decimal"] == ov["decimal"] and nqv["value"] == ov["value"] and (
                    nqv["exact"] == ov["exact"] or (ov["exact"]["kind"] == "symbolic" and nqv["exact"]["expression"] == ov["exact"]["expression"]))
                out["moved_magnitudes"] += ok
        chk(f"round-00 quantity kept: {p}", ok)
    # every round-00 row survives with the same selector, value, unit and criterion kind
    def rowmap(d):
        m = {}
        for ck, c in d["cases"].items():
            for hn, h in [("", c)] + list(c.get("variants", {}).items()):
                for cid, lc in h.get("load_cases", {}).items():
                    for r in lc["rows"]:
                        m[(ck, hn, cid, r["kind"], r["entity_ref"], r["component"], r["location"])] = (r, lc["expected"][r["expected"]])
        return m
    om, nm = rowmap(old), rowmap(new)
    for k, (r, q) in om.items():
        if k not in nm:
            chk(f"round-00 row kept {k}", False)
            continue
        r2, q2 = nm[k]
        ok = (q2["exact"] == q["exact"] and q2["value"] == q["value"] and r2["unit"] == r["unit"] and r2["coordinate_system"] == r["coordinate_system"]
              and r2["criterion"]["kind"] == r["criterion"]["kind"])
        if r["criterion"]["kind"] == "zero_scale":
            fac = 1000.0 if r.get("transform") == "m_to_mm" else 1.0
            ok = ok and abs(r2["criterion"]["absolute_tolerance"] - r["criterion"]["absolute_tolerance"] * fac) <= 1e-15 * r2["criterion"]["absolute_tolerance"]
        out["rows_kept"] += ok
        chk(f"round-00 row kept {k}", ok)
    out["rows_round00"], out["rows_round01"] = len(om), len(nm)
    new_kinds = {}
    for k in nm:
        if k not in om:
            new_kinds[k[3]] = new_kinds.get(k[3], 0) + 1
    out["new_rows_by_kind"] = new_kinds
    # documents: equal except the added sp1_pair pointer and the note text
    docs_same = 0
    for ck, c in old["cases"].items():
        for hn, h in [("", c)] + list(c.get("variants", {}).items()):
            if "documents" not in h:
                continue
            h2 = new["cases"][ck] if not hn else new["cases"][ck]["variants"][hn]
            d_old, d_new = h["documents"], h2["documents"]
            same = all(d_old[k] == d_new[k] for k in ("v2_model_0.3.0", "v2_model_0.4.0", "v3_patch_for_both"))
            extra = set(d_new) - set(d_old)
            chk(f"documents unchanged {ck}{'/' + hn if hn else ''}", same and extra == {"sp1_pair"} and d_new["sp1_pair"] == "/sp1_pair_scope")
            docs_same += same
    out["document_sets_unchanged"] = docs_same
    # discriminators: round-00 entries keep id, order and value
    for ck in ("milltol_lame_membrane", "tp_phys_pressure_halves", "pressure_membrane_thin_wall_limit"):
        o, n = old["cases"][ck]["wrong_result_discriminators"], new["cases"][ck]["wrong_result_discriminators"]
        chk(f"discriminators kept in order {ck}", all(a["id"] == b["id"] and a["wrong"] == b["wrong"] and a["quantity"] == b["quantity"] for a, b in zip(o, n)) and len(n) >= len(o))
    # path-level list of every other difference (non-row, non-quantity leaves)
    ol = {p: v for p, v in leaves(old) if not is_q(v)}
    nl = {p: v for p, v in leaves(new) if not is_q(v)}
    diffs = {"changed": [], "added": [], "removed": []}
    for p in sorted(set(ol) | set(nl)):
        if p in ol and p in nl:
            if ol[p] != nl[p] and not (isinstance(ol[p], list) and ol[p] and isinstance(ol[p][0], dict) and "kind" in ol[p][0]):
                diffs["changed"].append(p)
        elif p in nl:
            diffs["added"].append(p)
        else:
            diffs["removed"].append(p)
    out["diffs"] = diffs
    return out


def main():
    new = json.load(open(sys.argv[1]))
    old = json.load(open(sys.argv[2]))
    n1, s3 = case1(new)
    n2 = case2(new)
    n3 = case3(new)
    nb = twin_b(new)
    tw = rv.twin(sys.argv[3])
    nt = transport(new)
    u = unchanged(new, old)
    print("A. rows compared both ways: case1", n1, "case2", {k: v for k, v in n2.items() if k.startswith("case")}, "case3", n3, "twinB", nb)
    print("   case2 combined A-B elastic maximum:", f"{n2['A-B maximum']:.25f}", "->", repr(float(n2["A-B maximum"])))
    print("   S-3 authored-bore control:", s3, "=", repr(s3.f()))
    print("   twin A fixture re-derivation:", tw["n"], "values, worst relative", f"{tw['worst']:.1e}")
    print("C. transport rows checked:", nt)
    print("D. unchanged:", json.dumps({k: v for k, v in u.items() if k != "diffs"}, sort_keys=True))
    for k in ("removed", "added", "changed"):
        print(f"   non-quantity leaves {k}: {len(u['diffs'][k])}")
        for p in u["diffs"][k]:
            print("     ", p)
    print(f"checks: {NCHK[0]}, failures: {len(FAILS)}")
    print("RESULT:", "PASS" if not FAILS else "FAIL")
    return 0 if not FAILS else 1


if __name__ == "__main__":
    sys.exit(main())
