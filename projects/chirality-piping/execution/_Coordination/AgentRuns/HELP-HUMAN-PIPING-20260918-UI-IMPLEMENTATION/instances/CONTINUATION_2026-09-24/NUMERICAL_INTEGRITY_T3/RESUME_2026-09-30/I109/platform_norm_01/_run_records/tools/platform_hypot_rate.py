#!/usr/bin/env python3
"""I109: how often this platform's libm hypot (through ctypes) is not correctly rounded, and how
often its chain hypot(hypot(a, b), c) differs from the correctly rounded 3-norm, on random
comparable-magnitude inputs. Usage: platform_hypot_rate.py <seed> <count>"""
import ctypes, ctypes.util, json, os, platform, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import norm_oracle as o
libm = ctypes.CDLL(ctypes.util.find_library("m"))
libm.hypot.restype = ctypes.c_double; libm.hypot.argtypes = [ctypes.c_double, ctypes.c_double]
rng = random.Random(int(sys.argv[1])); n = int(sys.argv[2])
bad2 = bad3 = 0
for _ in range(n):
    e = rng.randint(-60, 60)
    a, b, c = (o.rnd_exp(rng, e + rng.randint(-8, 0)) for _ in range(3))
    if not o.same(libm.hypot(a, b), o.ref_norm([a, b])): bad2 += 1
    if not o.same(libm.hypot(libm.hypot(a, b), c), o.ref_norm([a, b, c])): bad3 += 1
print(json.dumps({"platform": platform.system() + " " + platform.machine(), "pairs": n, "hypot_not_cr": bad2, "chain_ne_norm3": bad3}))
