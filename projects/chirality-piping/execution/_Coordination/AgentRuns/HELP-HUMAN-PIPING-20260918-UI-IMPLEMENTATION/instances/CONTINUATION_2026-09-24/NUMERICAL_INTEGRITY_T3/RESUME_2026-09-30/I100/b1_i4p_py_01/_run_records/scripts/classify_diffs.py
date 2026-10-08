"""I100: every remaining PY-vs-RS and PY-vs-TS probe difference at the head, classified.
Usage: classify_diffs.py <HEAD_PROBES_TS1.json> <out.json>
Classes:
  raw_code_rs   - bound and unbound only; PY and RS both refuse at G7 with different codes (RS's own raw G7
                  codes: B1_SC items 12 and 13, RV113's RS addendum 02 N-3, and ruling 3's declared raw class);
  ruling2_3     - the two extrema shapes (`t_extrema_global_upper_string`, `t_extrema_certified_gap_null`):
                  transport admitted by RS and TS at I4 (ruling 2 adds the demand in I101's lane), and TS's raw
                  admission (ruling 3, I101's lane);
  other         - anything else (none expected)."""
import json
import sys

d = json.load(open(sys.argv[1]))
RULED = {"r2:t_extrema_global_upper_string", "r2:t_extrema_certified_gap_null"}
out = {"raw_code_rs": [], "ruling2_3": [], "other": []}
for r in d["rows"]:
    rs, ts = r["diff"]["rs_6e3e"], r["diff"]["ts_6fa6"]
    if not rs and not ts:
        continue
    py, R, T = r[d["labels"][1]], r["rs_6e3e"], r["ts_6fa6"]
    if r["id"] in RULED:
        out["ruling2_3"].append({"id": r["id"], "py": py, "rs": R, "ts": T})
    elif not ts and set(rs) <= {"bound", "unbound"} and all(py[e].get("gate") == "G7" and R[e].get("gate") == "G7" for e in rs):
        out["raw_code_rs"].append({"id": r["id"], "item": r["item"], "py": {e: py[e]["code"] for e in rs}, "rs": {e: R[e]["code"] for e in rs}})
    else:
        out["other"].append({"id": r["id"], "py": py, "rs": R, "ts": T})
json.dump(out, open(sys.argv[2], "w"), indent=1, sort_keys=True)
print({k: len(v) for k, v in out.items()})
import collections
print(collections.Counter((x["item"], x["py"]["bound"], x["rs"]["bound"]) for x in out["raw_code_rs"]).most_common())
