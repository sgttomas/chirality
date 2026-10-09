"""T4-I7 repair round 01: show that every surviving frozen value of round 00 is unchanged.

    python -I repair01_compare.py <round-00 dir> <round-01 dir>

The round-00 directory holds u2_reference_cases.json and u2_document_sketches.json as committed at
80b1e97e2b (extracted with git show); the round-01 directory holds the regenerated files.
"""
import hashlib
import json
import os
import sys

old_dir, new_dir = sys.argv[1], sys.argv[2]


def load(d, name):
    path = os.path.join(d, name)
    with open(path, "rb") as fh:
        raw = fh.read()
    return json.loads(raw), hashlib.sha256(raw).hexdigest()


old, h_old = load(old_dir, "u2_reference_cases.json")
new, h_new = load(new_dir, "u2_reference_cases.json")
olds, hs_old = load(old_dir, "u2_document_sketches.json")
news, hs_new = load(new_dir, "u2_document_sketches.json")
print("round 00 u2_reference_cases.json sha256", h_old)
print("round 00 u2_document_sketches.json sha256", hs_old)
print("round 01 u2_reference_cases.json sha256", h_new)
print("round 01 u2_document_sketches.json sha256", hs_new)

REVISED = {"U2-L-KINK-FREE-P-K2", "U2-L-KINK-ANCH-P-K2"}  # S-2: kink moved to atan(5e-4)


def leaves(x, path=""):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from leaves(v, path + "/" + k)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from leaves(v, path + "/" + str(i))
    else:
        yield path, x


def removed_by_s1(path):
    return "/end_rows/" in path and "/chord_frame/" in path or path.startswith("/zero_scale/end_action_force_chord_frame")


# ---- header
changed = [k for k in old if k not in ("cases", "polygon_limit_control") and old[k] != new.get(k)]
added = [k for k in new if k not in old]
print("header keys changed:", changed, "added:", added)

# ---- cases
n_cmp = n_same = n_removed = 0
diffs = []
added_leaves = {}
for cid, oc in old["cases"].items():
    if cid in REVISED:
        print("case %s: revised in repair 01 (S-2), excluded from the unchanged comparison" % cid)
        continue
    nc = new["cases"][cid]
    nl = dict(leaves({k: v for k, v in nc.items() if k != "wrong_result_discriminators"}))
    ol = dict(leaves({k: v for k, v in oc.items() if k != "wrong_result_discriminators"}))
    for p, v in ol.items():
        if removed_by_s1(p):
            n_removed += 1
            if p in nl:
                diffs.append((cid, p, "removed block still present"))
            continue
        n_cmp += 1
        if nl.get(p, "<missing>") == v:
            n_same += 1
        else:
            diffs.append((cid, p, v, nl.get(p, "<missing>")))
    for p in nl:
        if p not in ol:
            key = p.split("/")[1] + ("/.../" + p.split("/")[-2] if "end_rows" in p else "/" + p.split("/")[-1]
                                     if p.startswith("/derived") else "")
            added_leaves[key] = added_leaves.get(key, 0) + 1
print("round-00 leaves compared (all cases except the two revised kink cases, controls handled below): %d; "
      "unchanged %d; changed %d" % (n_cmp, n_same, len([d for d in diffs if len(d) == 4])))
print("round-00 wall-basis chord-frame leaves removed by S-1 (replaced by chord_frame_elastic): %d" % n_removed)
for d in diffs[:20]:
    print("DIFF", d)
print("leaves added to surviving cases:", json.dumps(added_leaves, sort_keys=True))
new_cases = [c for c in new["cases"] if c not in old["cases"]]
print("cases added (%d):" % len(new_cases), ", ".join(new_cases))

# ---- negative controls
rows_kept = rows_dropped = 0
for cid, oc in old["cases"].items():
    if cid in REVISED or "wrong_result_discriminators" not in oc:
        continue
    nctl = {c["id"]: c for c in new["cases"][cid]["wrong_result_discriminators"]}
    for octl in oc["wrong_result_discriminators"]:
        ncl = nctl[octl["id"]]
        assert ncl["max_distance_in_tolerances"] == octl["max_distance_in_tolerances"], (cid, octl["id"])
        listed = {r["pointer"]: r for r in ncl["discriminating_values"]}
        dropped = {r["pointer"]: r for r in ncl["rows_dropped_repair_01"]}
        for r in octl["discriminating_values"]:
            if r["pointer"] in listed:
                assert listed[r["pointer"]] == r, (cid, octl["id"], r, listed[r["pointer"]])
                rows_kept += 1
            else:
                d = dropped[r["pointer"]]
                rows_dropped += 1
                print("dropped %s %s %s: round-00 wrong %s, distance %s; now %s (%s)" % (
                    cid, octl["id"], r["pointer"].split("/expected/")[1], r["wrong_value"],
                    r["distance_in_tolerances"], d["distance_in_tolerances"], d["reason"]))
        assert len(listed) == len([r for r in octl["discriminating_values"] if r["pointer"] in listed])
print("controls: every max distance unchanged; round-00 rows kept byte-identical %d, dropped %d" % (
    rows_kept, rows_dropped))
for cid in sorted(REVISED):
    for c in new["cases"][cid]["wrong_result_discriminators"]:
        print("revised %s %s: max distance %s; rows dropped %d" % (
            cid, c["id"], c["max_distance_in_tolerances"], len(c["rows_dropped_repair_01"])))

# ---- polygon control
onp = {p["case_id"]: p for p in old["polygon_limit_control"]}
nnp = {p["case_id"]: p for p in new["polygon_limit_control"]}
same = all(nnp[c] == onp[c] for c in onp)
print("polygon entries of round 00 unchanged: %s (%d); added: %s" % (same, len(onp),
                                                                 ", ".join(c for c in nnp if c not in onp)))

# ---- document sketches
eq = sum(1 for c in olds["sketches"] if c not in REVISED and news["sketches"][c] == olds["sketches"][c])
tot = sum(1 for c in olds["sketches"] if c not in REVISED)
print("document sketches of surviving round-00 cases unchanged: %d of %d; sketches now %d" % (
    eq, tot, len(news["sketches"])))
