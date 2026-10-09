"""T4-RV2: re-derive every frozen K of T4-I6 (49 cases, 8 UTM controls) by rv2_lib's
global-frame quadrature and compare; check the grid/translation claims.
usage: python -I compare_k.py U1_REFERENCE_CASES_JSON"""
import sys, os, json, math, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decimal import Decimal as D, getcontext
from fractions import Fraction as Fr
import rv2_lib as L

PREC = 100
getcontext().prec = PREC
doc = json.load(open(sys.argv[1]))
G30 = Fr(1, 2 ** 30)


def cmp(Kme, Kref_str):
    Kr = [[D(v) for v in row] for row in Kref_str]
    sc = L.maxabs(Kr)
    ms = max(abs(Kme[i][j] - Kr[i][j]) for i in range(12) for j in range(12)) / sc
    # entrywise relative for entries above 1e-12 of the scale (the JSON carries 20 significant digits)
    er = max((abs(Kme[i][j] - Kr[i][j]) / abs(Kr[i][j]) for i in range(12) for j in range(12) if abs(Kr[i][j]) > sc * D("1e-12")), default=D(0))
    # entries the reference gives as nonzero but tiny vs scale, or zero
    return ms, er


t0 = time.time()
worst = {"ms": D(0), "er": D(0)}
rows = []
grid_ok = True
for c in doc["cases"]:
    inp = c["inputs"]
    nodes = c["nodes_by_X"]
    # grid / translation claims
    for X, nd in nodes.items():
        xi, xj = nd["x_i"], nd["x_j"]
        for k in range(3):
            if c["id"].startswith("CB_"):
                continue
            fi, fj = Fr(xi[k]), Fr(xj[k])
            if (fi / G30).denominator != 1 or (fj / G30).denominator != 1 or abs(xi[k]) >= 2 ** 23 or abs(xj[k]) >= 2 ** 23:
                grid_ok = False
                print("GRID FAIL", c["id"], X, k)
            if xj[k] - xi[k] != inp["d"][k] or Fr(xj[k]) - Fr(xi[k]) != Fr(inp["d"][k]):
                grid_ok = False
                print("DIFF FAIL", c["id"], X, k)
    if c["id"].startswith("CB_"):
        nd = nodes["origin"]
        r = L.curved_K(nd["x_i"], nd["x_j"], inp["R"], inp["y_reference"], inp["E"], inp["G"], inp["A"], inp["I"], inp["J"], c["k_in"], c["k_out"])
        nd2 = nodes["X7.3e6"]
        r2 = L.curved_K(nd2["x_i"], nd2["x_j"], inp["R"], inp["y_reference"], inp["E"], inp["G"], inp["A"], inp["I"], inp["J"], c["k_in"], c["k_out"])
        same = all(abs(r["K"][i][j] - r2["K"][i][j]) <= L.maxabs(r["K"]) * D("1e-80") for i in range(12) for j in range(12))
    else:
        r = L.curved_K([0.0, 0.0, 0.0], inp["d"], inp["R"], inp["y_reference"], inp["E"], inp["G"], inp["A"], inp["I"], inp["J"], c["k_in"], c["k_out"])
        same = None
    ms, er = cmp(r["K"], c["K_global"])
    dphi = abs(r["geo"]["phi"] - D(c["derived"]["phi"])) / r["geo"]["phi"]
    worst["ms"] = max(worst["ms"], ms)
    worst["er"] = max(worst["er"], er)
    rows.append((c["id"], ms, er, dphi, same))
    print("%-28s phi %-12.6e  max|dK|/max|K| %.2e  entry-rel %.2e  dphi/phi %.1e%s" % (c["id"], float(r["geo"]["phi"]), float(ms), float(er), float(dphi), "" if same is None else "  toy translated equal: %s" % same))
print("grid/translation claims (2^-30 grid, |x|<2^23, x_j - x_i == d in binary64 at every X):", grid_ok)
print("WORST over 49 cases: max|dK|/max|K| %.2e, entrywise relative (entries > 1e-12 max) %.2e" % (float(worst["ms"]), float(worst["er"])))
# quadrature convergence on the hardest geometries
for cid in ("BPI-1E-6-SK-k2.5-rotated", "B90-SK-k2.5-base", "B1E-8-SK-k1.0-rotated"):
    c = next(x for x in doc["cases"] if x["id"] == cid)
    inp = c["inputs"]
    a = L.curved_K([0.0, 0.0, 0.0], inp["d"], inp["R"], inp["y_reference"], inp["E"], inp["G"], inp["A"], inp["I"], inp["J"], c["k_in"], c["k_out"], n=48)["K"]
    b = L.curved_K([0.0, 0.0, 0.0], inp["d"], inp["R"], inp["y_reference"], inp["E"], inp["G"], inp["A"], inp["I"], inp["J"], c["k_in"], c["k_out"], n=64)["K"]
    print("quadrature n=48 vs n=64 on %s: %.1e" % (cid, float(max(abs(a[i][j] - b[i][j]) for i in range(12) for j in range(12)) / L.maxabs(a))))
# UTM controls
uc = doc["utm_controls_refused_today"]["cases"]
wu = D(0)
for c in uc:
    s = c["section"]
    r = L.curved_K(c["x_i"], c["x_j"], c["R"], c["y_reference"], s["e"], s["g"], s["a"], s["i"], s["j"], c["k"], c["k"])
    ms, er = cmp(r["K"], c["K_global"])
    # is binary64 x_j - x_i exact?
    exact = all(Fr(c["x_j"][k] - c["x_i"][k]) == Fr(c["x_j"][k]) - Fr(c["x_i"][k]) for k in range(3))
    wu = max(wu, ms)
    print("UTM control X=%-9s phi %.6f  max|dK|/max|K| %.2e entry-rel %.2e  binary64 d exact: %s" % (c["X"], float(r["geo"]["phi"]), float(ms), float(er), exact))
print("WORST UTM controls: %.2e" % float(wu))
