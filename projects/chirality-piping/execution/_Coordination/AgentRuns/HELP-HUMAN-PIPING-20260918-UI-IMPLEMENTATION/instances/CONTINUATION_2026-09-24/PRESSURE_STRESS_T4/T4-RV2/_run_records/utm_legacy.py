"""T4-RV2: today's PP centre + CB radius check (labelled binary64 emulation, source order of
PPL:7766-7846 and CB:150-163 as read at ed012c7ccf) on T4-I6's eight UTM controls.
usage: python -I utm_legacy.py U1_REFERENCE_CASES_JSON"""
import sys, os, json, math
def check(xi, xj, R, y):
    chord = [xj[0] - xi[0], xj[1] - xi[1], xj[2] - xi[2]]
    Lc = (chord[0] * chord[0] + chord[1] * chord[1] + chord[2] * chord[2]) ** 0.5
    h = 0.5 * Lc
    cu = [chord[0] / Lc, chord[1] / Lc, chord[2] / Lc]
    ax = y[0] * cu[0] + y[1] * cu[1] + y[2] * cu[2]
    pn = [y[0] - ax * cu[0], y[1] - ax * cu[1], y[2] - ax * cu[2]]
    pm = (pn[0] * pn[0] + pn[1] * pn[1] + pn[2] * pn[2]) ** 0.5
    so = (R * R - h * h) ** 0.5
    C = [0.5 * (xi[k] + xj[k]) - so * pn[k] / pm for k in range(3)]
    ri = [xi[k] - C[k] for k in range(3)]
    rj = [xj[k] - C[k] for k in range(3)]
    ni = math.sqrt(ri[0] * ri[0] + ri[1] * ri[1] + ri[2] * ri[2])
    nj = math.sqrt(rj[0] * rj[0] + rj[1] * rj[1] + rj[2] * rj[2])
    m = abs(ni - nj) / max(ni, nj)
    return m, m > 1e-9
doc = json.load(open(sys.argv[1]))
for c in doc["utm_controls_refused_today"]["cases"]:
    m, ref = check(c["x_i"], c["x_j"], c["R"], c["y_reference"])
    print("X %-9s mismatch %.3e refused %s (I6: %.3e)" % (c["X"], m, ref, c["legacy_emulation_radius_mismatch_rel"]))
