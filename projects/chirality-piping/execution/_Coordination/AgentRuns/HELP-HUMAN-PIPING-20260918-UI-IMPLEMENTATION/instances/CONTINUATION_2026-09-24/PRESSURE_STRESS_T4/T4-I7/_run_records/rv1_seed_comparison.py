"""T4-I7: compare the direct engine with T4-RV1's independent binary64 planar script (F3, explicit
wall/cap free body) on RV1's own geometry. A cross-check of two independent implementations; neither
is the frozen reference for T4-U2's cases.

    python -I rv1_seed_comparison.py <path to WT/scratch/t4_RV1/h2_check.py>
"""
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import u2_engine as E  # noqa: E402
from u2_engine import D, v  # noqa: E402

spec = importlib.util.spec_from_file_location("h2_check", sys.argv[1])
H = importlib.util.module_from_spec(spec)
spec.loader.exec_module(H)

sec = E.Section("0.1683", "0.00711")
mat = E.Material("2.0e11", "0.3", "1.2e-5")
R = D("0.229")


def chain(k, kink=0.0):
    A, B, C = v(0, 0, 0), v(3, 0, 0), v(D(3) + R, R, 0)
    nodes, elems, arc = H.build(k=float(k), kink=kink)
    Dn = tuple(D(c) for c in nodes[3]) + (D(0),)
    coords = {"A": A, "B": B, "C": C, "D": Dn}
    mems = [E.Member("S1", "straight", "A", "B", A, B, sec, mat, v(0, 0, 1)),
            E.Member("BEND", "arc", "B", "C", B, C, sec, mat, v(1, -1, 0), R=R, k=k),
            E.Member("S2", "straight", "C", "Dn", C, Dn, sec, mat, v(0, 0, 1))]
    mems[2].j_id = "D"
    return E.Chain(["A", "B", "C", "D"], coords, mems), nodes, elems


def rel(a, b):
    a, b = D(a), D(b)
    return abs(a - b) / max(abs(a), abs(b), D("1e-300"))


worst = D(0)
for k in ("1", "2"):
    ch, nodes, elems = chain(k)
    for label, kw, ekw in (("anchored", dict(anchors=(0, 3)), dict(anchor_D=True)),
                           ("D separate", dict(anchors=(0, 3), term_transfer=(True, False)),
                            dict(anchor_D=True, transfer_D=False)),
                           ("p+thermal", dict(anchors=(0, 3), eps_th=1.2e-3), dict(anchor_D=True, dT="100"))):
        o = H.run("F3", nodes, elems, **kw)
        s = E.analyse(ch, E.LoadCase(p="5e6", **ekw))
        mine = [s.R_A[0], s.R_A[1], s.R_A[5]]
        theirs = o["reac"][0]
        r = max(rel(a, b) for a, b in zip(mine, theirs))
        worst = max(worst, r)
        print("k=%s %-10s RV1 F3 reac A %s | engine %s | max rel %.2e" % (
            k, label, ["%.15e" % x for x in theirs], ["%.15e" % float(x) for x in mine], r))
print("max relative difference engine vs RV1 F3: %.2e" % worst)
