"""T4-I9: counts the ball and midpoint operations of one certificate in the
emulation (arc_cert_probe.py; 90 deg bend, self-weight). Argument: the probe path."""
import importlib.util, sys
spec = importlib.util.spec_from_file_location("probe", sys.argv[1])
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
counts = {"add":0,"mul":0,"div":0,"sqrt":0,"atan":0,"point":0}
def wrap(name, f):
    def g(*a):
        counts[name]+=1
        return f(*a)
    return g
m.b_add = wrap("add", m.b_add); m.b_mul = wrap("mul", m.b_mul); m.b_div = wrap("div", m.b_div)
m.b_sqrt = wrap("sqrt", m.b_sqrt); m.b_atan = wrap("atan", m.b_atan)
orig_rnd = m.rnd
m.rnd = wrap("point", orig_rnd)
import math
em=2.03e11; gm=em/2.6; area,inertia,torsion=m.section(0.1683,0.00711)
R=0.2286; phi=math.radians(90)
xi=[3.0,0,0]; xj=[3.0+R*math.sin(phi), R*(1-math.cos(phi)), 0]
m.formula(m.BallCtx(), xi, xj, R, [0,-1,0], em, gm, area, inertia, torsion, 1.0, 1.0, [0,0,-450.0])
print(counts, "ball ops:", sum(v for k,v in counts.items() if k!="point"), "all rounded midpoint ops (incl. point inverse):", counts["point"])
