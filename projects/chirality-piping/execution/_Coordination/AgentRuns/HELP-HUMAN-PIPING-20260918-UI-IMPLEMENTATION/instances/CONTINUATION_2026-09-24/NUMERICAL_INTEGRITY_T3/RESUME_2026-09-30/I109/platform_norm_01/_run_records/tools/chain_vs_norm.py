#!/usr/bin/env python3
"""I109: how often the correctly rounded chain RN(hypot(RN(hypot(a,b)), c)) differs from the
correctly rounded 3-norm, on random comparable-magnitude triples, and whether the chain depends on
the component order. Usage: chain_vs_norm.py <seed> <count>"""
import json, math, random, sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import norm_oracle as o
rng = random.Random(int(sys.argv[1])); n = int(sys.argv[2])
diff = order = 0; ulps = {}
for _ in range(n):
    e = rng.randint(-60, 60)
    t = [o.rnd_exp(rng, e + rng.randint(-8, 0)) for _ in range(3)]
    r3 = o.ref_norm(t); ch = o.ref_chain(*t); ch2 = o.ref_chain(t[2], t[0], t[1])
    if ch != r3:
        diff += 1; u = abs(o.bits(ch) - o.bits(r3)); ulps[u] = ulps.get(u, 0) + 1
    if ch != ch2: order += 1
print(json.dumps({"triples": n, "chain_ne_norm3": diff, "ulps": ulps, "chain_order_dependent": order}))
