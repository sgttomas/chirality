"""RV120 (SC): which reader's own tests failed on each corrupted expectation.
Usage: python3 exp_results.py <CORRUPTIONS.json> <rs log> <vitest json> <pytest log> <out>"""
import json
import re
import sys

corr, rslog, tsj, pylog, out = sys.argv[1:6]
C = json.load(open(corr))
rs = open(rslog, errors="replace").read()
ts = json.load(open(tsj))
tsfail = [a["fullName"] + " :: " + (a.get("failureMessages") or [""])[0].split("\n")[0] for f in ts["testResults"] for a in f["assertionResults"] if a["status"] == "failed"]
py = [l for l in open(pylog, errors="replace") if l.startswith("FAILED ")]
rows = []
for c in C:
    eid = c["entry"]
    rs_hit = bool(re.search(r'"%s"[^\n]*(expected|got|differ|unbound|transport)|"id":"%s"[^\n]*"match":false' % (re.escape(eid), re.escape(eid)), rs))
    if eid == "d38_beside_selected":
        rs_hit = "complete_synthetic_controls_carry_their_shared_eligibility ... FAILED" in rs
    ts_hit = any(eid in t for t in tsfail)
    py_hit = any(eid in l for l in py) or (eid == "d38_beside_selected" and any("bases_are_the_pinned" in l or "complete_synthetic" in l for l in py))
    rows.append({**c, "failed_in": {"RS": rs_hit, "TS": ts_hit, "PY": py_hit}})
json.dump({"rows": rows, "ts_failed": tsfail, "py_failed": py}, open(out, "w"), indent=1)
for r in rows:
    print(r["entry"].ljust(36), r["field"][:40].ljust(40), "RS" if r["failed_in"]["RS"] else "--", "TS" if r["failed_in"]["TS"] else "--", "PY" if r["failed_in"]["PY"] else "--", "| expected:", r["should_fail_in"])
