"""RV131 O5: how far a binary64 product's formation error can sit above the correctly-rounded floor (crK).
F122 (straight skew frame, K-D5's required true positive, published Passed with actual 2.43 dense / 1.21 sparse
per formation_check_runtime.rs:8-10 and kd5 records) against its own crK; CSKEW_8_5's crK recomputed with RV131's element.
The straight frame is T4-I6's curved_ref.frame_element (a labelled cross-check; Euler-Bernoulli, no shear).
usage: python -I rv_o5_floor.py T4I6_RUN_RECORDS_DIR U1_JSON KD5_MODELS_RS"""
import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(1, sys.argv[1])
from decimal import Decimal as D, getcontext
import curved_ref as C
import rv_element as RV
getcontext().prec = 70
def solve_free(K, rigid, springs, loads):
    free = [q for q in range(len(K)) if q not in rigid]
    Kf = [[K[a][b] for b in free] for a in free]
    for dof, v in springs:
        Kf[free.index(dof)][free.index(dof)] += D(v)
    f = [D(0)] * len(free)
    for dof, v in loads:
        f[free.index(dof)] += D(v)
    return dict(zip(free, RV.m_solve(Kf, f)))
S = RV.SECTION
# F122 (kd5_models.rs:8-16): nodes (0,0,0),(1,2,2); y (1,0,0); springs (3,144),(4,1e6),(5,1e6); loads (9,.0048),(10,.0096),(11,.0096)
sec = dict(e=200000000000.0, g=80000000000.0)
import re, ast
txt = open(sys.argv[3]).read()
body = re.search(r"pub\(super\) const F122: ModelData = ModelData \{(.*?)\n\};", txt, re.S).group(1)
secd = {k: float(v) for k, v in re.findall(r"(\w+): ([-0-9.e+]+)", re.search(r"section: SectionData \{([^}]*)\}", body).group(1))}
K = C.frame_element([0.0, 0, 0], [1.0, 2.0, 2.0], [1.0, 0.0, 0.0], secd["e"], secd["g"], secd["a"], secd["i"], secd["i"], secd["j"])
rigid = [0, 1, 2]; springs = [(3, 144.0), (4, 1e6), (5, 1e6)]; loads = [(9, 0.0048), (10, 0.0096), (11, 0.0096)]
u = solve_free(K, rigid, springs, loads)
Kr = [[D(float(v)) for v in row] for row in K]
ucr = solve_free(Kr, rigid, springs, loads)
print("F122 crK (correctly rounded frame entries, exact solve): %.3e of the criterion; recorded product actual 2.43 (dense) / 1.21 (sparse)" % RV.actual_ratio(u, ucr, D(3)))
doc = json.load(open(sys.argv[2]))
m = [x for x in doc["t3_models"] if x["model"] == "CSKEW_8_5"][0]
rb = m["regenerated_bend_inputs"][0]
Kc, geo, _ = RV.element_global([0.3, 0.0, 0.3], rb["R"], rb["y_reference"], S["E"], S["G"], S["A"], S["I"], S["J"], 1.0, 1.0)
uc = solve_free(Kc, rigid, [(3, 8.5), (4, 1e6), (5, 1e6)], [(9, 8.5e-06)])
ucr = solve_free([[D(float(v)) for v in row] for row in Kc], rigid, [(3, 8.5), (4, 1e6), (5, 1e6)], [(9, 8.5e-06)])
print("CSKEW_8_5 crK (RV131 element, correctly rounded): %.3e (T4-I6: %s)" % (RV.actual_ratio(uc, ucr, geo["L"]), m["estimate_correctly_rounded_K_ratio"]))
