#!/usr/bin/env python3
"""RV119: the nine ruled transport changes, recomputed from the committed census files at H.
PY R01 = RV113's py_head.jsonl (SR-PY at 11cc14e3e6); PY item 4 = I91's census_rv113.jsonl (2843a59a16);
RS round 2 = I90's census_head.jsonl (6e3e4fe219). For each of input/bound/unbound/transport, compares
the gate and code (or ok) per entry (set, index, id). There is no separate input lane in these files. Usage: census_nine_check.py <R folder at H>"""
import json, sys, os
R = sys.argv[1]
def load(p):
    out = {}
    for l in open(os.path.join(R, p)):
        if l.strip():
            d = json.loads(l); out[(d.get("set"), d["i"], d["id"])] = d
    return out
r01 = load("REVIEW_RV113/rvr_sr_py_01/evidence/census/py_head.jsonl")
i4 = load("I91/b1_sr_py_01/_run_records/repair_02_item4/census/census_rv113.jsonl")
rs = load("I90/b1_sr_rs_01/_run_records/repair_02/out/census_head.jsonl")
def key(v):
    if v is None: return None
    if "ok" in v: return "ok"
    e = v.get("err", v)
    return (e.get("gate"), e.get("code"))
lanes = ["bound", "unbound", "transport"]
print("entries:", len(r01), len(i4), len(rs))
k0 = next(iter(r01)); print("keys per record:", sorted(r01[k0]))
print("same entry keys in all three:", set(r01) == set(i4) == set(rs))
print("input sha256 equal PY R01 vs item 4:", sum(1 for k in r01 if r01[k].get("input_sha256") == i4[k].get("input_sha256")), "of", len(r01))
for ln in lanes:
    ch = [i for i in r01 if key(r01[i].get(ln)) != key(i4[i].get(ln))]
    print(f"PY R01 -> item 4, lane {ln}: {len(ch)} changes{(': ' + ', '.join(str(i[1]) for i in ch)) if ch else ''}")
    if ln == "transport":
        for i in ch: print(f"   {i[1]} {i[2]}: {key(r01[i][ln])} -> {key(i4[i][ln])}; RS {key(rs[i].get(ln))}")
for ln in lanes:
    neq = [i for i in i4 if key(i4[i].get(ln)) != key(rs[i].get(ln))]
    print(f"PY item 4 vs RS round 2, lane {ln}: {len(i4)-len(neq)} of {len(i4)} equal on gate/code")
