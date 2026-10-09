"""T4-RV3 addendum 01: my own comparison of T4-I7 round 00 (80b1e97e2b) against round 01 (fa0b43f3c1),
independent of T4-I7's repair01_compare.py.

    python -I -B rv3_r01_diff.py <round-00 dir> <round-01 dir>

Both directories hold u2_reference_cases.json and u2_document_sketches.json."""
import json
import os
import sys
from decimal import Decimal as D

r00, r01 = sys.argv[1], sys.argv[2]
a = json.load(open(os.path.join(r00, "u2_reference_cases.json")))
b = json.load(open(os.path.join(r01, "u2_reference_cases.json")))
sa = json.load(open(os.path.join(r00, "u2_document_sketches.json")))
sb = json.load(open(os.path.join(r01, "u2_document_sketches.json")))

# my round-00 B-1 list: (case, control, pointer)
B1 = set()
for cid, c in a["cases"].items():
    for x in c.get("wrong_result_discriminators", []):
        for r in x["discriminating_values"]:
            if D(r["distance_in_tolerances"]) < 1000:
                B1.add((cid, x["id"], r["pointer"]))
print("round-00 rows below 1e3 tolerances (RV3 B-1): %d" % len(B1))

print("header keys changed:", sorted(k for k in a if k != "cases" and k in b and a[k] != b[k]),
      "added:", sorted(k for k in b if k not in a), "removed:", sorted(k for k in a if k not in b))
print("round-00 polygon entries unchanged and first:", b["polygon_limit_control"][:len(a["polygon_limit_control"])]
      == a["polygon_limit_control"], "; added:", [p["case_id"] for p in b["polygon_limit_control"][len(a["polygon_limit_control"]):]])
print("cases added:", [k for k in b["cases"] if k not in a["cases"]])
print("cases removed:", [k for k in a["cases"] if k not in b["cases"]])


def leaves(o, path=()):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from leaves(v, path + (k,))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from leaves(v, path + (str(i),))
    else:
        yield path, o


REVISED = {"U2-L-KINK-FREE-P-K2", "U2-L-KINK-ANCH-P-K2"}
tot = changed = removed = 0
removed_kinds = {}
added_kinds = {}
other = []
dropped_found = set()
for cid, ca in a["cases"].items():
    cb = b["cases"][cid]
    for key in set(ca) | set(cb):
        if key in ("expected", "zero_scale", "derived", "wrong_result_discriminators"):
            continue
        if ca.get(key) != cb.get(key) and cid not in REVISED:
            other.append((cid, key))
    if cid in REVISED:
        continue
    la = dict(leaves({"expected": ca["expected"], "zero_scale": ca["zero_scale"], "derived": ca["derived"]}))
    lb = dict(leaves({"expected": cb["expected"], "zero_scale": cb["zero_scale"], "derived": cb["derived"]}))
    for p, v in la.items():
        tot += 1
        if p not in lb:
            removed += 1
            k = "chord_frame(wall)" if "chord_frame" in p else ("zero_scale/" + p[1] if p[0] == "zero_scale" else "/".join(p))
            removed_kinds[k] = removed_kinds.get(k, 0) + 1
        elif lb[p] != v:
            changed += 1
            other.append((cid, "/".join(p)))
    for p in lb:
        if p not in la:
            k = ("chord_frame_elastic" if "chord_frame_elastic" in p else
                 ("zero_scale/" + p[1] if p[0] == "zero_scale" else p[0] + "/" + p[1]))
            added_kinds[k] = added_kinds.get(k, 0) + 1
    # controls
    xa = {x["id"]: x for x in ca.get("wrong_result_discriminators", [])}
    xb = {x["id"]: x for x in cb.get("wrong_result_discriminators", [])}
    if set(xa) != set(xb):
        other.append((cid, "control ids"))
    for i, x in xa.items():
        y = xb[i]
        if x["max_distance_in_tolerances"] != y["max_distance_in_tolerances"]:
            other.append((cid, i + " max"))
        kept = [r for r in x["discriminating_values"] if (cid, i, r["pointer"]) not in B1]
        if kept != y["discriminating_values"]:
            other.append((cid, i + " kept rows differ"))
        drop_ptrs = {r["pointer"] for r in y.get("rows_dropped_repair_01", [])}
        for r in x["discriminating_values"]:
            if (cid, i, r["pointer"]) in B1:
                if r["pointer"] in drop_ptrs:
                    dropped_found.add((cid, i, r["pointer"]))
        for k in set(x) | set(y):
            if k not in ("discriminating_values", "rows_dropped_repair_01", "listing_rule") and x.get(k) != y.get(k):
                other.append((cid, i + " " + k))
print("surviving cases (65, kink cases excluded): round-00 leaves %d, changed %d, removed %d" % (tot, changed, removed))
print("removed by kind:", removed_kinds)
print("added by kind:", added_kinds)
print("other differences outside expected/zero_scale/derived/controls:", other)
b1_kink = {t for t in B1 if t[0] in REVISED}
print("B-1 rows dropped and recorded in rows_dropped_repair_01 (surviving cases): %d of %d" % (
    len(dropped_found), len(B1 - b1_kink)))
print("B-1 rows in the revised kink cases (control regenerated): %d" % len(b1_kink))

# every listed row in round 01 discriminates, and the listed maximum equals the control maximum
weak = 0
maxmis = []
nrows = 0
for cid, c in b["cases"].items():
    for x in c.get("wrong_result_discriminators", []):
        ds = [D(r["distance_in_tolerances"]) for r in x["discriminating_values"]]
        nrows += len(ds)
        weak += sum(1 for d in ds if d < 1000)
        if format(max(ds), ".3e") != x["max_distance_in_tolerances"] and max(ds) != D(x["max_distance_in_tolerances"]):
            maxmis.append((cid, x["id"]))
        for r in x["discriminating_values"]:
            for fld in ("wrong_value", "reference_value", "distance_in_tolerances"):
                s = r[fld]
                if "e-" in s and D(s) == 0:
                    weak += 1
print("round-01 listed rows %d; rows below 1e3 tolerances or with zero printed in exponent form: %d;"
      " controls whose listed maximum differs from max_distance: %s" % (nrows, weak, maxmis))

# kink cases: inputs differ only in node:D x
for cid in sorted(REVISED):
    ia, ib = a["cases"][cid]["inputs"], b["cases"][cid]["inputs"]
    diffs = [("/".join(p), v, dict(leaves(ib)).get(p)) for p, v in leaves(ia) if dict(leaves(ib)).get(p) != v]
    print("%s input differences: %s" % (cid, diffs))

# sketches
same = sum(1 for cid in sa["sketches"] if cid not in REVISED and sa["sketches"][cid] == sb["sketches"][cid])
print("sketches: surviving non-kink cases identical %d of %d; sketches now %d; new: %s" % (
    same, len(sa["sketches"]) - 2, len(sb["sketches"]), sorted(set(sb["sketches"]) - set(sa["sketches"]))))
for cid in sorted(REVISED):
    la = dict(leaves(sa["sketches"][cid]))
    lb = dict(leaves(sb["sketches"][cid]))
    print("%s sketch differences: %s" % (cid, [("/".join(p), la.get(p), lb.get(p)) for p in sorted(set(la) | set(lb))
                                              if la.get(p) != lb.get(p)]))
print("sketch header unchanged:", {k: sa[k] == sb[k] for k in sa if k != "sketches"})
