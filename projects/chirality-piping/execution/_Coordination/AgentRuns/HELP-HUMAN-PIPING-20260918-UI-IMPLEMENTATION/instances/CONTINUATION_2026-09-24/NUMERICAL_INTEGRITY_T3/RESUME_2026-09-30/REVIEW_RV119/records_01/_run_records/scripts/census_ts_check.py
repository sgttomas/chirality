#!/usr/bin/env python3
"""RV119: TS's census, 7e47e51b5d (I92 REPAIR_01's census_base.jsonl) against 6fa6a64658 (REPAIR_01_ITEM3's
census_head.jsonl), per entry (set, index, id) and lane, from the committed files at H.
Usage: census_ts_check.py <I92 _run_records folder at H>"""
import json, sys, os
D = sys.argv[1]
def load(p):
    out = {}
    for l in open(os.path.join(D, p)):
        if l.strip():
            d = json.loads(l); out[(d.get("set"), d.get("i"), d.get("id"))] = d
    return out
b = load("repair_01/census/census_base.jsonl"); h = load("repair_01_item3/census/census_head.jsonl")
print("entries:", len(b), len(h), "same keys:", set(b) == set(h))
print("input sha256 equal:", sum(1 for k in b if b[k]["input_sha256"] == h[k]["input_sha256"]), "of", len(b))
for ln in ("bound", "unbound", "transport"):
    ch = [k for k in b if json.dumps(b[k].get(ln), sort_keys=True) != json.dumps(h[k].get(ln), sort_keys=True)]
    print(f"lane {ln}: {len(ch)} changes {[k[1] for k in ch]}")
    if ln == "transport":
        for k in ch:
            o = b[k][ln]; n = h[k][ln]
            os_ = "admitted" if "ok" in o else f"{o['err']['gate']} {o['err']['code']}"
            print(f"   {k[1]} {k[2]}: {os_} -> {n['err']['gate']} {n['err']['code']}")
