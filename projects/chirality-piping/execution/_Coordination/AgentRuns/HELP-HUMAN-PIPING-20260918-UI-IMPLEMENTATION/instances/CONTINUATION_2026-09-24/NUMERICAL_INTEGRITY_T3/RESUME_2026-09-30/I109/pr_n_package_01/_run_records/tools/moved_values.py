#!/usr/bin/env python3
"""I109 round 3: each moved magnitude with its components, from I109 round 1's base-against-candidate
regeneration (WT/scratch/i109_norm/{regen,dumps}_{base,cand}: the base NUM af53e1447c, the candidate
d538f469af, whose product code equals PR-N's). Checks that the components are the same on both sides and
that the candidate value is the exact correctly rounded 3-norm (norm_oracle.ref_norm, exact integers).
Usage (from WT/scratch/i109_norm): python3 moved_values.py > pkg/moved_values.json"""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import norm_oracle as o
CASES = [
 ("W-C2 dense", "dumps_{s}/wc2/retained_precision_w_c2_successor_dense_scrutiny.json", "result:support-action:6:case-c:8:rigid:N0:force_magnitude"),
 ("SF-2 (C, B, A) dense", "dumps_{s}/sf2/c_b_a__dense_scrutiny.json", "result:support-action:6:case-c:8:rigid:N0:force_magnitude"),
 ("rf_skew milestone dense ordinary (u1)", "regen_{s}/fixtures_product_preview_rf_skew_t_cant_off_122_r1e-04.request.json.dense_scrutiny.json", "result:support-action:4:case:8:rigid:N0:force_magnitude"),
 ("load_reference/connected sparse cold", "regen_{s}/fixtures_product_preview_load_reference_connected.request.json.sparse_interactive.json", "result:support-action:9:case:cold:12:support:root:force_magnitude"),
 ("load_reference/connected sparse hot", "regen_{s}/fixtures_product_preview_load_reference_connected.request.json.sparse_interactive.json", "result:support-action:8:case:hot:12:support:root:force_magnitude"),
 ("load_reference/connected dense hot", "regen_{s}/fixtures_product_preview_load_reference_connected.request.json.dense_scrutiny.json", "result:support-action:8:case:hot:12:support:root:force_magnitude"),
 ("load_reference_fallback_uz sparse anchor moment (t13)", "regen_{s}/core_reporting_result_export_tests_fixtures_load_reference_fallback_uz.request.json.sparse_interactive.json", "result:support-action:9:case:join:6:anchor:moment_magnitude"),
]
def rows(d): return d["results"] if "results" in d else d["source"]["results"]
def comps(d, row):
    names = ["Fx", "Fy", "Fz"] if (row.get("metadata") or {}).get("component") == "force_magnitude" else ["Mx", "My", "Mz"]
    out = []
    for n in names:
        hit = [r for r in rows(d) if r.get("entity_ref") == row["entity_ref"] and r.get("basis_ref") == row.get("basis_ref")
               and (r.get("metadata") or {}).get("component") == n and r["kind"] == "support_reaction_component_v2"]
        assert len(hit) == 1
        out.append(hit[0]["value"])
    return out
out = []
for label, path, rid in CASES:
    dc, db = json.load(open(path.format(s="cand"))), json.load(open(path.format(s="base")))
    rc = [r for r in rows(dc) if r["id"] == rid][0]; rb = [r for r in rows(db) if r["id"] == rid][0]
    xs = comps(dc, rc); assert xs == comps(db, rb)
    n3 = o.ref_norm(xs)
    out.append({"where": label, "id": rid, "components": [x.hex() for x in xs], "before_macos": repr(rb["value"]), "after": repr(rc["value"]),
                "after_is_cr_norm3": o.same(rc["value"], n3), "cr_chain": repr(o.ref_chain(*xs)), "ulps": abs(o.bits(rc["value"]) - o.bits(rb["value"]))})
print(json.dumps(out, indent=1))
