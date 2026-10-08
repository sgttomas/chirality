#!/usr/bin/env python3
"""RV119: leaf paths that differ between I97's statics (v0 -> r1 -> r2) for DEF-C and PTABLE, from the files at H.
Usage: statics_paths_diff.py <I97 b2_c_01 folder at H>"""
import json, sys, os
D = sys.argv[1]
def leaves(x, p=""):
    if isinstance(x, dict):
        for k, v in x.items(): yield from leaves(v, f"{p}/{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x): yield from leaves(v, f"{p}/{i}")
    else: yield p, x
def diff(a, b):
    la, lb = dict(leaves(a)), dict(leaves(b))
    return sorted(k for k in set(la) | set(lb) if la.get(k, object()) != lb.get(k, object()))
for name in ("retained_precision_prepared_combination_v1.json", "semantic_contract_v0_3_preview_physics_retained_1.json"):
    v0 = json.load(open(os.path.join(D, "statics", name))); r1 = json.load(open(os.path.join(D, "statics/r1", name))); r2 = json.load(open(os.path.join(D, "statics/r2", name)))
    d01, d12 = diff(v0, r1), diff(r1, r2)
    print(f"{name}: v0->r1 {len(d01)} leaf paths; r1->r2 {len(d12)} leaf paths")
    for k in d12: print("   r1->r2:", k[:160])
