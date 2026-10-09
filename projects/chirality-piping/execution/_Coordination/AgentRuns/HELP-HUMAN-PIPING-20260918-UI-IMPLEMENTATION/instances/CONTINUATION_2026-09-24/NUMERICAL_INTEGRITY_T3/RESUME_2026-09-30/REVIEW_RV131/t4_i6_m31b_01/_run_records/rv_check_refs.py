"""RV131: independent check of T4-I6's frozen K (u1_reference_cases.json) and of the K1 kill model.
usage: python -I rv_check_refs.py U1_JSON"""
import sys, os, json, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from decimal import Decimal as D, getcontext
import rv_element as RV
getcontext().prec = 70
doc = json.load(open(sys.argv[1]))
S = RV.SECTION
print("== frozen K vs RV131 global-quadrature element (max|dK|/max|K|), all cases")
worst = (D(0), None)
for c in doc["cases"]:
    inp = c["inputs"]
    K, geo, F = RV.element_global(inp["d"], inp["R"], inp["y_reference"], inp["E"], inp["G"], inp["A"], inp["I"], inp["J"], c["k_in"], c["k_out"])
    ref = [[D(v) for v in row] for row in c["K_global"]]
    sc = max(abs(v) for r in ref for v in r)
    dev = max(abs(K[i][j] - ref[i][j]) for i in range(12) for j in range(12)) / sc
    phidev = abs(geo["phi"] - D(c["derived"]["phi"])) / geo["phi"]
    if dev > worst[0]:
        worst = (dev, c["id"])
    print("  %-26s phi %-12s rel dev %.2e  phi rel dev %.1e" % (c["id"], "%.6e" % float(geo["phi"]), dev, phidev))
print("worst:", "%.2e" % worst[0], worst[1])

print()
print("== K1 kill models (m31b_kill_and_mutant): u_int and the binary64 formula-chord mutant, recomputed")
for k in doc["m31b_kill_and_mutant"]:
    if not (k["model"].startswith("K1-IP-1E-8") or k["model"].startswith("K1-SK-1E-8") or k["model"].startswith("K1-IP-2E-8") or k["model"].startswith("K1-IP-PI-1E-7") or k["model"].startswith("K1-IP-1E-4")):
        continue
    xi, xj = k["nodes"]
    d = [xj[q] - xi[q] for q in range(3)]
    assert all(xi[q] + d[q] == xj[q] for q in range(3))
    R, y = k["R"], k["y_reference"]
    K, geo, F = RV.element_global(d, R, y, S["E"], S["G"], S["A"], S["I"], S["J"], 1.0, 1.0)
    u, Kf, free = RV.cantilever_solve(K)
    ref = {int(a): D(b) for a, b in k["u_int"].items()}
    L_b = geo["L"]
    r_u = RV.actual_ratio(u, ref, L_b)
    # the mutant: binary64 formula chord in B1's local frame, mapped to global with B1's axes
    phi_b = 2.0 * math.asin(math.sqrt(d[0]**2 + d[1]**2 + d[2]**2) / (2.0 * R))
    cl = [R * (math.cos(phi_b) - 1.0), R * math.sin(phi_b), 0.0]
    ax = RV.b1_axes(geo)
    cg = [sum(D(cl[a]) * ax[a][q] for a in range(3)) for q in range(3)]
    Km, _, _ = RV.element_global(d, R, y, S["E"], S["G"], S["A"], S["I"], S["J"], 1.0, 1.0, chord_global=cg)
    um, _, _ = RV.cantilever_solve(Km)
    r_m = RV.actual_ratio(u, um, L_b)
    dcL = RV.v_norm(RV.v_sub(cg, geo["d"])) / geo["L"]
    print("  %-20s u_int(T4-I6) vs RV131: %.2e crit | mutant ratio RV131 %.4f (T4-I6 %s) | dc/L %.3e | cos(phi_b)==1: %s" % (k["model"], r_u, r_m, k["mutant_libm"]["ratio"], dcL, math.cos(phi_b) == 1.0))
