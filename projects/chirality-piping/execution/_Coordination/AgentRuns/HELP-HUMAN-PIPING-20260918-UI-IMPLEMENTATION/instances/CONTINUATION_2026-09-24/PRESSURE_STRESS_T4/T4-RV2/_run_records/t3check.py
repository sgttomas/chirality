"""T4-RV2: independent re-derivation of T4-I6's t3_models u_int_new and the K1 kill model u_int,
with rv2_lib elements; check of the y_reference (bow side) claim O6.
usage: python -I t3check.py KD5_MODELS_RS RV5_MODELS_RS U1_REFERENCE_CASES_JSON"""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decimal import Decimal as D, getcontext
import rv2_lib as L
getcontext().prec = 80


def parse(path):
    txt = open(path).read()
    out = {}
    for name, body in re.findall(r"const (\w+): ModelData = ModelData \{(.*?)\n\};", txt, re.S):
        b = body
        b = b.replace("&[", "[").replace("None", "None").replace("Some((", "((")
        b = re.sub(r"SectionData \{ (.*?) \}", lambda m: "{" + re.sub(r"(\w+): ", r"'\1': ", m.group(1)) + "}", b)
        b = re.sub(r"MemberData \{ (.*?) \}", lambda m: "{" + re.sub(r"(\b[a-z_]+): ", r"'\1': ", m.group(1)) + "}", b)
        b = re.sub(r"^\s*(\w+): ", r"'\1': ", b, flags=re.M)
        b = b.replace("'name': \"", "'name': \"")
        d = eval("{" + b + "}", {"__builtins__": {}}, {"None": None})
        out[name] = d
    return out


def assemble_solve(m, bend_inputs, chord_overrides=None):
    s = m["section"]
    n = 6 * len(m["nodes"])
    K = [[D(0)] * n for _ in range(n)]
    for idx, mem in enumerate(m["members"]):
        xi, xj = m["nodes"][mem["i"]], m["nodes"][mem["j"]]
        if mem["bend"] is None:
            Ke = L.frame_K(xi, xj, s["e"], s["g"], s["a"], s["i"], s["j"])
        else:
            R, y, k = bend_inputs[(mem["i"], mem["j"])]
            Ke = L.curved_K(xi, xj, R, y, s["e"], s["g"], s["a"], s["i"], s["j"], k, k, n=40)["K"]
        dof = [6 * mem["i"] + r for r in range(6)] + [6 * mem["j"] + r for r in range(6)]
        for a in range(12):
            for b in range(12):
                K[dof[a]][dof[b]] += Ke[a][b]
    for dd, v in m["springs"]:
        K[dd][dd] += D(v)
    f = [D(0)] * n
    for dd, v in m["loads"]:
        f[dd] += D(v)
    free = [i for i in range(n) if i not in m["rigid"]]
    u = L.lu_solve_dec([[K[a][b] for b in free] for a in free], [f[a] for a in free])
    return dict(zip(free, u))


def ratio(m, uref, u):
    st = max((abs(v) for k, v in uref.items() if k % 6 < 3), default=D(0))
    sr = max((abs(v) for k, v in uref.items() if k % 6 >= 3), default=D(0))
    ext = [max(D(p[k]) for p in m["nodes"]) - min(D(p[k]) for p in m["nodes"]) for k in range(3)]
    lb = L.vnorm(ext)
    tr, ro = max(st, lb * sr), max(sr, st / lb)
    return max(abs(D(u[k]) - v) / (D("1e-9") * max(abs(v), tr if k % 6 < 3 else ro)) for k, v in uref.items())


kd5 = parse(sys.argv[1])
rv5 = parse(sys.argv[2])
doc = json.load(open(sys.argv[3]))
allm = dict(kd5)
allm.update(rv5)
print("y_reference / bow-side check (O6): cos(angle) between member y_ref and the old arc's bow, both projected normal to d")
for name in ["E1", "E6", "CSKEW_8_5", "CSKEW_30_RADIUS_MISMATCH", "CPLANAR_60", "CSKEW_30_N122", "PP_UTM_2", "RV5_CANT90_PLANAR", "RV5_CANT60_PLANAR", "RV5_CANT30_SKEW", "RV5_CANT10_SKEW", "RV5_PP_UTM"]:
    m = allm[name]
    for mem in m["members"]:
        if mem["bend"] is None:
            continue
        xi = [D(v) for v in m["nodes"][mem["i"]]]
        xj = [D(v) for v in m["nodes"][mem["j"]]]
        C = [D(v) for v in mem["bend"][0]]
        d = L.vsub(xj, xi)
        dh = L.vmul(1 / L.vnorm(d), d)
        bow = L.vsub(L.vmul(D(1) / 2, L.vadd(xi, xj)), C)
        y = [D(v) for v in mem["y_reference"]]
        yp = L.vsub(y, L.vmul(L.vdot(y, dh), dh))
        bp = L.vsub(bow, L.vmul(L.vdot(bow, dh), dh))
        cosang = L.vdot(yp, bp) / (L.vnorm(yp) * L.vnorm(bp))
        ri, rj = L.vnorm(L.vsub(xi, C)), L.vnorm(L.vsub(xj, C))
        print("  %-26s member %d-%d  cos = %+.15f   |ri|-|rj| rel %.2e  mean R - 0.3 = %.2e" % (name, mem["i"], mem["j"], float(cosang), float((ri - rj) / ri), float((ri + rj) / 2 - D("0.3"))))

print()
print("u_int_new re-derived (rv2_lib) vs T4-I6 (criterion units, model measure) and T3's committed u_int vs mine:")
worst = D(0)
for entry in doc["t3_models"]:
    name = entry["model"]
    ui6 = {int(k): D(v) for k, v in entry["u_int_new"].items()}
    if name in allm or name in ("CSKEW_10", "CSKEW_9"):
        if name in allm:
            m = allm[name]
        else:
            import copy
            m = copy.deepcopy(kd5["CSKEW_8_5"])
            kx = 10.0 if name == "CSKEW_10" else 9.0
            m["springs"] = [(3, kx), (4, 1000000.0), (5, 1000000.0)]
            m["loads"] = [(9, kx * 1e-06)]
            m["u_int"] = []
        bi = {}
        for nb in entry["regenerated_bend_inputs"]:
            bi[tuple(nb["member"])] = (nb["R"], nb["y_reference"], nb["k"])
    else:
        # PP-route models: cantilever, R 0.3, y +y
        nodes = entry["nodes"]
        m = {"name": name, "section": dict(e=2e11, g=8e10, a=0.005969026041820614, i=2.700984283923829e-05, j=5.401968567847658e-05),
             "nodes": nodes, "members": [{"i": 0, "j": 1, "y_reference": [0.0, 1.0, 0.0], "bend": ((0, 0, 0), 1.0)}],
             "rigid": [0, 1, 2], "springs": [(3, 1e6), (4, 1e6), (5, 1e6)], "loads": [(9, 1.0), (10, 1.0), (11, 1.0)], "u_int": []}
        bi = {(0, 1): (0.3, [0.0, 1.0, 0.0], 1.0)}
    u = assemble_solve(m, bi)
    r = ratio(m, u, ui6)
    worst = max(worst, r)
    old = ""
    if m.get("u_int"):
        uo = {k: D(v) for k, v in m["u_int"]}
        old = "  T3 committed vs mine %.3e (I6 says %s)" % (float(ratio(m, u, uo)), entry.get("old_u_int_vs_new_ratio"))
    print("  %-46s I6 vs mine: %.2e criterion%s" % (name, float(r), old))
print("WORST t3_models: %.2e of the criterion" % float(worst))
print()
print("K1 / sweep kill models: u_int re-derived")
w2 = D(0)
for k in doc["m31b_kill_and_mutant"]:
    nodes = k["nodes"]
    m = {"name": k["model"], "section": dict(e=2e11, g=8e10, a=0.005969026041820614, i=2.700984283923829e-05, j=5.401968567847658e-05),
         "nodes": nodes, "members": [{"i": 0, "j": 1, "y_reference": k["y_reference"], "bend": ((0, 0, 0), 1.0)}],
         "rigid": [0, 1, 2], "springs": [(3, 1e6), (4, 1e6), (5, 1e6)], "loads": [(9, 1.0), (10, 1.0), (11, 1.0)]}
    u = assemble_solve(m, {(0, 1): (k["R"], k["y_reference"], 1.0)})
    ui6 = {int(a): D(b) for a, b in k["u_int"].items()}
    r = ratio(m, u, ui6)
    w2 = max(w2, r)
print("WORST kill models (%d): %.2e of the criterion" % (len(doc["m31b_kill_and_mutant"]), float(w2)))
