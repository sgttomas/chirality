# T4-I2 emulation (standard library only; not a product run).
# Ports PP's binary64 arc centre (P/core/product_physics/src/lib.rs:7766-7844@70e7f49ced)
# and the element's geometry()/formula chord (P/core/solver/curved_bend/src/lib.rs:150-179,
# 246-251@70e7f49ced), and compares them with a node-relative centre (offset from node i,
# never formed in absolute coordinates). Run: python3 -I centre_probe.py
import math, random

def sub(a, b): return [a[i] - b[i] for i in range(3)]
def dot(a, b): return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
def norm(a): return math.sqrt(dot(a, a))
def cross(a, b): return [a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]]

def pp_centre(f, t, R, y):  # PP order of operations, absolute coordinates
    ch = [t[i]-f[i] for i in range(3)]; L = math.sqrt(ch[0]*ch[0]+ch[1]*ch[1]+ch[2]*ch[2]); h = 0.5*L
    u = [ch[i]/L for i in range(3)]; ax = y[0]*u[0]+y[1]*u[1]+y[2]*u[2]
    n = [y[i]-ax*u[i] for i in range(3)]; m = math.sqrt(n[0]*n[0]+n[1]*n[1]+n[2]*n[2])
    s = math.sqrt(R*R-h*h)
    return [0.5*(f[i]+t[i]) - s*n[i]/m for i in range(3)]

def rel_offset(f, t, R, y):  # centre - node_i, from the chord only
    ch = sub(t, f); L = norm(ch); h = 0.5*L
    u = [v/L for v in ch]; ax = dot(y, u); n = [y[i]-ax*u[i] for i in range(3)]; m = norm(n)
    s = math.sqrt(R*R-h*h)
    return [0.5*ch[i]-s*n[i]/m for i in range(3)]

def element_metrics(ri, rj, actual):
    Ri, Rj = norm(ri), norm(rj); R = 0.5*(Ri+Rj)
    pn = cross(ri, rj); phi = math.atan2(norm(pn), dot(ri, rj))
    ex = [v/Ri for v in ri]; ez = [v/norm(pn) for v in pn]; ey = cross(ez, ex)
    loc = [dot(ex, actual), dot(ey, actual), dot(ez, actual)]
    formula = [R*(math.cos(phi)-1.0), R*math.sin(phi), 0.0]
    return abs(Ri-Rj)/max(Ri, Rj), norm(sub(loc, formula))/R

random.seed(7); R = 0.3
for X in [0.0, 5e5, 2e6, 5e6, 7.3e6]:
    refused = 0; mm_pp = ce_pp = mm_rel = ce_rel = 0.0
    for _ in range(2000):
        phi = math.radians(random.choice([2, 5, 10, 30, 60, 90])); a = random.uniform(0, 2*math.pi)
        o = [X+random.uniform(-10, 10), 0.7*X+random.uniform(-10, 10), random.uniform(-5, 5)]
        f = [o[0]+R*math.cos(a), o[1]+R*math.sin(a), o[2]]
        t = [o[0]+R*math.cos(a+phi), o[1]+R*math.sin(a+phi), o[2]]
        y = [math.cos(a+phi/2), math.sin(a+phi/2), 0.0]      # arc bows toward +y_reference
        c = pp_centre(f, t, R, y); mm, ce = element_metrics(sub(f, c), sub(t, c), sub(t, f))
        if mm > 1e-9: refused += 1                           # RADIUS_MATCH_TOLERANCE refusal
        else: ce_pp = max(ce_pp, ce)
        mm_pp = max(mm_pp, mm)
        off = rel_offset(f, t, R, y); ch = sub(t, f)
        mm2, ce2 = element_metrics([-v for v in off], [ch[i]-off[i] for i in range(3)], ch)
        mm_rel = max(mm_rel, mm2); ce_rel = max(ce_rel, ce2)
    print(f"X={X:8.3g} PP centre: max|ri-rj|/R={mm_pp:.2e} refused={refused}/2000 "
          f"max|c_formula-c_actual|/R (admitted)={ce_pp:.2e} | node-relative: {mm_rel:.2e} {ce_rel:.2e}")
