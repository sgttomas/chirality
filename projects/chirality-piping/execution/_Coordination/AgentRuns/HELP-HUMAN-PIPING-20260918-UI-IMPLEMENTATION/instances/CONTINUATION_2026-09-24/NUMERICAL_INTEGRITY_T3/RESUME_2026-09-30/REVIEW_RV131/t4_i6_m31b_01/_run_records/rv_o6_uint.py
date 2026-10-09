"""RV131 O6: independent re-derivation (global-quadrature element) of T4-I6's u_int_new for the
single-bend cantilever models regenerated with R = 0.3 and the bow-vector y (JSON t3_models).
usage: python -I rv_o6_uint.py U1_JSON KD5_MODELS RV5_MODELS"""
import sys, os, re, ast, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decimal import Decimal as D, getcontext
import rv_element as RV
getcontext().prec = 70
doc = json.load(open(sys.argv[1]))
src = {}
for path in sys.argv[2:4]:
    for name, body in re.findall(r"pub\(super\) const (\w+): ModelData = ModelData \{(.*?)\n\};", open(path).read(), re.S):
        g = lambda key: ast.literal_eval(re.search(key + r": &(\[.*?\]),\n", body).group(1)) if re.search(key + r": &(\[.*?\]),\n", body) else []
        src[name] = dict(nodes=ast.literal_eval(re.search(r"nodes: &(\[.*?\]\]),", body).group(1)), rigid=g("rigid"),
                         springs=ast.literal_eval(re.search(r"springs: &(\[.*?\]),\n", body).group(1)),
                         loads=ast.literal_eval(re.search(r"loads: &(\[.*?\]),\n", body).group(1)))
S = RV.SECTION
for m in doc["t3_models"]:
    name = m["model"]
    base = name if name in src else ("CSKEW_8_5" if name.startswith("CSKEW_") and name not in src else None)
    if base is None or len(m.get("regenerated_bend_inputs", [])) != 1 or len(src[base]["nodes"]) != 2:
        continue
    s = src[base]
    springs, loads = s["springs"], s["loads"]
    if name in ("CSKEW_10", "CSKEW_9"):
        kx = float(name.split("_")[1]); springs = [(3, kx), (4, 1e6), (5, 1e6)]; loads = [(9, kx * 1e-6)]
    rb = m["regenerated_bend_inputs"][0]
    xi, xj = s["nodes"]
    d = [xj[q] - xi[q] for q in range(3)]
    K, geo, _ = RV.element_global(d, rb["R"], rb["y_reference"], S["E"], S["G"], S["A"], S["I"], S["J"], rb["k"], rb["k"])
    free = [q for q in range(12) if q not in s["rigid"]]
    Kf = [[K[a][b] for b in free] for a in free]
    for dof, v in springs:
        Kf[free.index(dof)][free.index(dof)] += D(v)
    f = [D(0)] * len(free)
    for dof, v in loads:
        f[free.index(dof)] += D(v)
    u = dict(zip(free, RV.m_solve(Kf, f)))
    ref = {int(a): D(b) for a, b in m["u_int_new"].items()}
    r = RV.actual_ratio(u, ref, geo["L"])
    print("%-26s y %-60s u_int_new vs RV131: %.2e of the criterion" % (name, str(rb["y_reference"]), r))
