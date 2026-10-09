"""T4-I11 tangency probe (standard library only; an emulation, not a product run).

For a corner C between straights X_in->C and C->X_out, insert tangent points with
sqrt-only formulas (the proposed insert_bend_at_corner arithmetic), then rebuild the
arc from the chord T1->T2, the radius R and y_reference = u_in two ways:
  (a) centre-based: an absolute centre M - s*n (the construction PP uses at ed012c7ccf,
      PP/src/lib.rs, build_curved_bend_macro_elements), tangents from the centre;
  (b) node-relative: t_i = cos(phi/2) d + sin(phi/2) n, t_j = cos(phi/2) d - sin(phi/2) n
      (the T4-U1 objective form: node differences, R and the plane normal only).
The kink at T1 (T2) is the angle between the straight's direction and the arc's end
tangent. Also: tangent points rounded to 1 mm and 0.1 mm grids (hand entry).
"""
import math

def sub(a, b): return [a[i] - b[i] for i in range(3)]
def add(a, b): return [a[i] + b[i] for i in range(3)]
def scl(a, s): return [a[i] * s for i in range(3)]
def dot(a, b): return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
def cross(a, b): return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]
def norm(a): return math.sqrt(dot(a, a))
def unit(a): n = norm(a); return [a[i] / n for i in range(3)]
def angle(a, b): return math.atan2(norm(cross(a, b)), dot(a, b))

def insert(c, x_in, x_out, r):
    u_in = unit(sub(c, x_in)); u_out = unit(sub(x_out, c))
    cr = norm(cross(u_in, u_out)); dt = dot(u_in, u_out)
    lt = r * cr / (1.0 + dt)  # R tan(Phi/2), sqrt-only
    return sub(c, scl(u_in, lt)), add(c, scl(u_out, lt)), u_in, math.atan2(cr, dt), lt

def arc_tangents(t1, t2, r, yref, mode):
    d = sub(t2, t1); c = norm(d); dh = scl(d, 1.0 / c)
    n = sub(yref, scl(dh, dot(yref, dh))); n = unit(n)
    sh = c / (2.0 * r); ch = math.sqrt(1.0 - sh * sh)
    if mode == "node_relative":
        return add(scl(dh, ch), scl(n, sh)), sub(scl(dh, ch), scl(n, sh))
    s = math.sqrt(r * r - 0.25 * c * c)
    m = scl(add(t1, t2), 0.5)
    centre = sub(m, scl(n, s))
    ri = unit(sub(t1, centre)); rj = unit(sub(t2, centre))
    ti = unit(sub(dh, scl(ri, dot(dh, ri))))
    tj = unit(sub(dh, scl(rj, dot(dh, rj))))
    return ti, tj

def kinks(x_in, t1, t2, x_out, r, yref, mode):
    ti, tj = arc_tangents(t1, t2, r, yref, mode)
    return angle(unit(sub(t1, x_in)), ti), angle(tj, unit(sub(x_out, t2)))

def rnd(p, g): return [round(v / g) * g for v in p]

def grid_kink(x_in, t1, t2, x_out, r, yref, g):
    try:
        return f"{max(kinks(x_in, rnd(t1, g), rnd(t2, g), x_out, r, yref, 'node_relative')):.3e}"
    except (ZeroDivisionError, ValueError):
        return "degenerate (refused)"

CASES = [
    ("L90 R0.3", [3.0, 0, 0], [0, 0, 0], [3.0, 2.0, 0], 0.3),
    ("skew3D R0.45", [2.0, 1.0, 0.5], [0, 0, 0], [3.2, 2.5, 1.9], 0.45),
    ("small Phi~5deg R0.05", [1.0, 0, 0], [0, 0, 0], [2.0, 0.0874887, 0], 0.05),
    ("tiny Phi~1deg R0.05", [1.0, 0, 0], [0, 0, 0], [2.0, 0.0174551, 0], 0.05),
    ("L90 R1.5", [6.0, 0, 0], [0, 0, 0], [6.0, 5.0, 0], 1.5),
]
OFFSETS = [("origin", [0.0, 0.0, 0.0]), ("UTM", [7.3e6, 5.0e6, 120.0])]

print("case | offset | Phi(deg) | chord(m) | kink centre-based (rad) | kink node-relative (rad) | kink 1mm grid | kink 0.1mm grid")
for name, c0, xin0, xout0, r in CASES:
    for oname, o in OFFSETS:
        c, xin, xout = add(c0, o), add(xin0, o), add(xout0, o)
        t1, t2, u_in, phi, lt = insert(c, xin, xout, r)
        chord = norm(sub(t2, t1))
        kc = max(kinks(xin, t1, t2, xout, r, u_in, "centre"))
        kn = max(kinks(xin, t1, t2, xout, r, u_in, "node_relative"))
        g1 = grid_kink(xin, t1, t2, xout, r, u_in, 1e-3)
        g2 = grid_kink(xin, t1, t2, xout, r, u_in, 1e-4)
        print(f"{name} | {oname} | {math.degrees(phi):.4f} | {chord:.6g} | {kc:.3e} | {kn:.3e} | {g1} | {g2}")

print()
print("y_reference = u_in gives the corner-side normal: max |n - unit(u_in - u_out)| over cases at origin")
print("(unit(u_in - u_out) is the analytic direction from the chord midpoint to the corner)")
worst = 0.0
for name, c, xin, xout, r in CASES:
    t1, t2, u_in, phi, lt = insert(c, xin, xout, r)
    u_out = unit(sub(xout, c))
    d = unit(sub(t2, t1)); n = unit(sub(u_in, scl(d, dot(u_in, d))))
    want = unit(sub(u_in, u_out))
    worst = max(worst, norm(sub(n, want)))
print(f"{worst:.3e}")

print()
print("Kink resultant pAi*alpha relative to the bend's own wall resultant pAi*2*sin(Phi/2), alpha = 1e-3 rad")
for deg in (90.0, 45.0, 30.0, 10.0, 5.0):
    print(f"Phi={deg:>5.1f} deg: {1e-3 / (2.0 * math.sin(math.radians(deg) / 2.0)):.3e}")
