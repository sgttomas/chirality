"""T4-RV5: independent re-derivation of T4-I12's NI friction replacement (item 8).

The active-set loop is modelled from my own reading of NI/src/lib.rs@ed012c7ccf
(solve_active_set_frame_with_mode_and_springs, solve_iteration_with_sliding_friction_evidence,
resolve_sliding_friction_states, sliding_friction_candidates, sliding_direction,
derived_normal_branch_admissible, build_trial_states, friction_normal_for_support,
reported_reactions, nonconverged_exit_diagnostic) and nonlinear_supports
classify_support_state / evaluate_active_set_iteration_with_resolved_friction_states.
T4-I12's model code was not read. The node-1 block is formed from the textbook 12x12
frame stiffness of the fixture's own section, rotated by exact rational direction
cosines, not from the k_a ee^T + k_l(I - ee^T) shortcut.

The model is first validated against the 20 values pinned at the four call sites for the
old block (150, -50); it then gives the replacement values, compared with T4-I12's JSON.
Usage: python -I rv5_ni.py <json>
"""
import json
import sys
from fractions import Fraction as Fr

FAILS = []
NCHK = [0]


def chk(name, ok):
    NCHK[0] += 1
    if not ok:
        FAILS.append(name)
        print("FAIL", name)


def sgn(x):
    return (x > 0) - (x < 0)


def node1_block_from_frame(E, G, A, Iy, Iz, J, xj, yref):
    L2 = sum(c * c for c in xj)
    from math import isqrt
    L = Fr(isqrt(L2.numerator), isqrt(L2.denominator))
    assert L * L == L2
    ex = [c / L for c in xj]
    p = sum(a * b for a, b in zip(yref, ex))
    yc = [yref[k] - p * ex[k] for k in range(3)]
    n2 = sum(c * c for c in yc)
    n = Fr(isqrt(n2.numerator), isqrt(n2.denominator))
    assert n * n == n2
    ey = [c / n for c in yc]
    ez = [ex[1] * ey[2] - ex[2] * ey[1], ex[2] * ey[0] - ex[0] * ey[2], ex[0] * ey[1] - ex[1] * ey[0]]
    lam = [ex, ey, ez]
    k = [[Fr(0)] * 12 for _ in range(12)]

    def s(i, j, v):
        k[i][j] = v
        k[j][i] = v
    a, t = E * A / L, G * J / L
    s(0, 0, a); s(6, 6, a); s(0, 6, -a); s(3, 3, t); s(9, 9, t); s(3, 9, -t)
    c12, c6, c4, c2 = 12 * E * Iz / L**3, 6 * E * Iz / L**2, 4 * E * Iz / L, 2 * E * Iz / L
    s(1, 1, c12); s(7, 7, c12); s(1, 7, -c12); s(1, 5, c6); s(1, 11, c6); s(5, 7, -c6); s(7, 11, -c6)
    s(5, 5, c4); s(11, 11, c4); s(5, 11, c2)
    c12, c6, c4, c2 = 12 * E * Iy / L**3, 6 * E * Iy / L**2, 4 * E * Iy / L, 2 * E * Iy / L
    s(2, 2, c12); s(8, 8, c12); s(2, 8, -c12); s(2, 4, -c6); s(2, 10, -c6); s(4, 8, c6); s(8, 10, c6)
    s(4, 4, c4); s(10, 10, c4); s(4, 10, c2)
    R = [[Fr(0)] * 12 for _ in range(12)]
    for b in range(4):
        for i in range(3):
            for j in range(3):
                R[3 * b + i][3 * b + j] = lam[i][j]
    Kg = [[sum(R[m][i] * k[m][n] * R[n][j] for m in range(12) for n in range(12)) for j in range(12)] for i in range(12)]
    return Kg[6][6], Kg[7][6], Kg


def run(a, b, fx, fy, mu, seed, max_iter):
    """One free DOF u (node-1 Ux); restrained source Uy with K_yx = b. Returns iteration list."""
    state = seed
    its = []
    for it in range(1, max_iter + 1):
        prev = its[-1] if its else None
        deferred = (not its) and state == "Sliding"
        applied = None
        derived_ok = True
        if state == "Sticking":
            u = Fr(0)
            Rx = a * u - fx
            Ry = b * u - fy
        else:  # Sliding (Inactive does not occur here)
            cand = False
            if prev is not None:
                s = sgn(prev["u"]) if prev["u"] != 0 else -sgn(prev["Rx"])
                if s != 0:
                    cand = True
            if cand and mu > 0:
                ub = fx / a
                Ryb = b * ub - fy
                beta = sgn(prev["Ry"]) if prev["Ry"] != 0 else sgn(Ryb)
                infl = b / a  # unit force at x: (b (fx+1)/a - fy) - Ryb
                c = s * mu * beta
                f = -c * Ryb / (1 + c * infl)
                applied = f if f != 0 else None
            fapp = applied or Fr(0)
            u = (fx + fapp) / a
            Ry = b * u - fy
            Rx = (a * u - (fx + fapp)) + fapp  # reported reaction adds the applied friction back
            if cand and mu > 0:
                derived_ok = True if beta == 0 and Ry == 0 else (beta * Ry >= 0 if beta != 0 else Ry == 0)
        N = abs(Ry)
        T = Rx
        # state update
        if state == "Sliding":
            if N <= 0:
                new, tan_ok = "Inactive", True
            elif deferred:
                new, tan_ok = "Sliding", True
            elif not derived_ok:
                new, tan_ok = "Sliding", True
            else:
                limit = mu * N
                if limit == 0:
                    adm = applied is None and u != 0
                else:
                    adm = applied is not None and u != 0 and applied * u < 0 and T * u < 0
                new, tan_ok = ("Sliding" if adm else "Sticking"), adm
        else:
            new = "Inactive" if N <= 0 else ("Sticking" if abs(T) <= mu * abs(N) else "Sliding")
            tan_ok = True
        changed = new != state
        converged = (not changed) and (not deferred) and tan_ok and derived_ok
        its.append(dict(it=it, state_in=state, state_out=new, u=u, Rx=Rx, Ry=Ry, applied=applied, derived_ok=derived_ok, converged=converged))
        state = new
        if converged or it == max_iter:
            break
    return its


def suite(a, b):
    out = {}
    for fx, fy in [(10, -10), (-10, -10)]:
        for seed in ["Sticking", "Sliding"]:
            its = run(a, b, Fr(fx), Fr(fy), Fr(3, 10), seed, 4)
            out[("t1", fx, fy, seed)] = its
    for fx, fy in [(10, -1), (-10, 1)]:
        out[("t2", fx, fy)] = run(a, b, Fr(fx), Fr(fy), Fr(3, 10), "Sticking", 4)
        out[("t2cap", fx, fy)] = run(a, b, Fr(fx), Fr(fy), Fr(3, 10), "Sticking", 2)
    out["t4"] = run(a, b, Fr(10), Fr(-10), Fr(0), "Sliding", 4)
    return out


def assert_structure(label, out):
    for fx, fy in [(10, -10), (-10, -10)]:
        res = [out[("t1", fx, fy, s)] for s in ["Sticking", "Sliding"]]
        for its in res:
            fin = its[-1]
            chk(label + " t1 (%d,%d): converged in 2, final Sliding, |f| = .3|N|, one applied force" % (fx, fy),
                fin["converged"] and len(its) == 2 and fin["state_out"] == "Sliding" and fin["applied"] is not None
                and abs(fin["Rx"]) == Fr(3, 10) * abs(fin["Ry"]) and fin["Rx"] == fin["applied"])
        chk(label + " t1 (%d,%d): seeds give identical final values" % (fx, fy), (res[0][-1]["u"], res[0][-1]["Ry"], res[0][-1]["Rx"]) == (res[1][-1]["u"], res[1][-1]["Ry"], res[1][-1]["Rx"]))
    for fx, fy in [(10, -1), (-10, 1)]:
        its = out[("t2", fx, fy)]
        sg = sgn(fx)
        chk(label + " t2 (%d,%d): 3 iterations; retry iterate Sliding with derived branch inadmissible; final friction*u < 0, |f| = .3|N|" % (fx, fy),
            its[-1]["converged"] and len(its) == 3 and its[1]["state_out"] == "Sliding" and not its[1]["derived_ok"]
            and its[-1]["Rx"] * its[-1]["u"] < 0 and abs(its[-1]["Rx"]) == Fr(3, 10) * abs(its[-1]["Ry"]))
        chk(label + " t2 (%d,%d): sign flip of the normal between retry and final" % (fx, fy), sgn(its[1]["Ry"]) == sgn(its[2]["Ry"]) and sgn(its[1]["applied"]) == -sgn(its[2]["applied"]))
        cap = out[("t2cap", fx, fy)]
        chk(label + " t2 cap 2 (%d,%d): not converged after 2, exit cause = derived-normal branch (classifier residual 0)" % (fx, fy),
            not cap[-1]["converged"] and len(cap) == 2 and not cap[-1]["derived_ok"] and cap[-1]["state_out"] == cap[-1]["state_in"])
    t4 = out["t4"]
    chk(label + " t4 (mu = 0): converged, no applied force in any iteration", t4[-1]["converged"] and all(x["applied"] is None for x in t4))
    return out


def vals(out):
    v = {}
    for fx, fy in [(10, -10), (-10, -10)]:
        fin = out[("t1", fx, fy, "Sticking")][-1]
        v[(fx, fy)] = (fin["u"], fin["Ry"], fin["Rx"])
    for fx, fy in [(10, -1), (-10, 1)]:
        its = out[("t2", fx, fy)]
        v[("retry", fx, fy)] = (its[1]["u"], its[1]["applied"], its[1]["Rx"], its[1]["Ry"])
        v[("final", fx, fy)] = (its[2]["u"], its[2]["Rx"], its[2]["Ry"])
    v["t4"] = (len(out["t4"]), out["t4"][-1]["u"])
    return v


# --- the old block, model validation against the pinned literals
old = assert_structure("old block (150,-50)", suite(Fr(150), Fr(-50)))
vo = vals(old)
chk("old pinned :3770 (10,-10): 7/135, 200/27, -20/9", vo[(10, -10)] == (Fr(7, 135), Fr(200, 27), Fr(-20, 9)))
chk("old pinned :3770 (-10,-10): -7/165, 400/33, 40/11", vo[(-10, -10)] == (Fr(-7, 165), Fr(400, 33), Fr(40, 11)))
for sg, fx, fy in [(1, 10, -1), (-1, -10, 1)]:
    chk("old pinned :3907 (%d,%d) retry: u = s 97/1350, applied = Rx = s 7/9, Ry = -s 70/27" % (fx, fy),
        vo[("retry", fx, fy)] == (sg * Fr(97, 1350), sg * Fr(7, 9), sg * Fr(7, 9), -sg * Fr(70, 27)))
    chk("old pinned :3907 (%d,%d) final: u = s 103/1650, friction = -s 7/11, normal = -s 70/33" % (fx, fy),
        vo[("final", fx, fy)] == (sg * Fr(103, 1650), -sg * Fr(7, 11), -sg * Fr(70, 33)))
# old block from the old element's definition: k_a ee^T + k_l(I - ee^T), e = (1,1,0)/sqrt2, k_a = 100, k_l = 200
chk("old block = 100 ee^T + 200 (I - ee^T): Kxx 150, Kxy -50", (Fr(100, 2) + Fr(200, 2), Fr(100, 2) - Fr(200, 2)) == (150, -50))

# --- the replacement: FrameElement (0,0,0) -> (3,-4,0), FrameSection::new(100, 40, 1, 1, 1, 1), y_reference (0,1,0)
Kxx, Kyx, Kg = node1_block_from_frame(Fr(100), Fr(40), Fr(1), Fr(1), Fr(1), Fr(1), [Fr(3), Fr(-4), Fr(0)], [Fr(0), Fr(1), Fr(0)])
chk("replacement node-1 block from the rotated 12x12 frame: Kxx = 1668/125, Kyx = -624/125", (Kxx, Kyx) == (Fr(1668, 125), Fr(-624, 125)))
Kxx2, Kyx2, _ = node1_block_from_frame(Fr(100), Fr(40), Fr(1), Fr(1), Fr(1), Fr(1), [Fr(3), Fr(-4), Fr(0)], [Fr(0), Fr(0), Fr(1)])
chk("replacement block unchanged for y_reference (0,0,1) (Iy = Iz)", (Kxx2, Kyx2) == (Kxx, Kyx))
chk("replacement: EA/L = 20 != 12EI/L^3 = 48/5 (normal stays affine-coupled)", Fr(100, 5) == 20 and Fr(1200, 125) == Fr(48, 5))
new = assert_structure("replacement frame", suite(Kxx, Kyx))
vn = vals(new)

doc = json.load(open(sys.argv[1]))
ni = doc["cases"]["U3-NI-FRICTION-FRAME"]
flat = []


def walk(o, p=""):
    if isinstance(o, dict):
        for k, v in o.items():
            walk(v, p + "/" + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, p + "[%d]" % i)
    else:
        flat.append((p, o))


walk(ni["expected"])
exact_strings = {str(v) for _, v in flat if isinstance(v, str) and "/" in v}
mine = [vn[(10, -10)], vn[(-10, -10)], vn[("retry", 10, -1)], vn[("final", 10, -1)], vn[("retry", -10, 1)], vn[("final", -10, 1)]]
missing = [str(x) for tup in mine for x in tup if x is not None and str(x) not in exact_strings and str(x).lstrip("-") not in exact_strings and Fr(x).denominator != 1]
print("replacement values (mine):")
print("  :3770 (10,-10)  u, normal, friction =", ", ".join(map(str, vn[(10, -10)])))
print("  :3770 (-10,-10) u, normal, friction =", ", ".join(map(str, vn[(-10, -10)])))
print("  :3907 (10,-1) retry u, applied, Rx, Ry =", ", ".join(map(str, vn[("retry", 10, -1)])))
print("  :3907 (10,-1) final u, friction, normal =", ", ".join(map(str, vn[("final", 10, -1)])))
print("  :3907 (-10,1) retry u, applied, Rx, Ry =", ", ".join(map(str, vn[("retry", -10, 1)])))
print("  :3907 (-10,1) final u, friction, normal =", ", ".join(map(str, vn[("final", -10, 1)])))
print("  :4251 (mu = 0) iterations, u =", vn["t4"][0], vn["t4"][1])
chk("replacement :3770 (10,-10) = 4375/7404, 4350/617, -1305/617", vn[(10, -10)] == (Fr(4375, 7404), Fr(4350, 617), Fr(-1305, 617)))
chk("replacement :3770 (-10,-10) = -4375/9276, 9550/773, 2865/773", vn[(-10, -10)] == (Fr(-4375, 9276), Fr(9550, 773), Fr(2865, 773)))
chk("replacement :3907 (10,-1) retry = 12125/14808, 1143/1234 (= Rx), -1905/617", vn[("retry", 10, -1)] == (Fr(12125, 14808), Fr(1143, 1234), Fr(1143, 1234), Fr(-1905, 617)))
chk("replacement :3907 (10,-1) final = 12875/18552, -1143/1546, -1905/773", vn[("final", 10, -1)] == (Fr(12875, 18552), Fr(-1143, 1546), Fr(-1905, 773)))
chk("replacement :3907 (-10,1) sign-reversed", vn[("retry", -10, 1)] == tuple(-x for x in vn[("retry", 10, -1)]) and vn[("final", -10, 1)] == tuple(-x for x in vn[("final", 10, -1)]))
chk("replacement :4251 two iterations, u = 625/834", vn["t4"] == (2, Fr(625, 834)))
chk("every replacement fraction appears in T4-I12's JSON (exact strings)", not missing)
if missing:
    print("missing from JSON:", missing)
print("ni checks: %d run, %d fail" % (NCHK[0], len(FAILS)))
print("PASS" if not FAILS else "FAIL")
