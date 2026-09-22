"""T4A: apply T4A_REMAPS.csv in memory and report, per call, affected rows whose tag set loses its
last LIVE tag (so the row's code evidence becomes TEST_ONLY and/or LEGACY_ONLY only)."""
import sys, os, re
from collections import defaultdict, Counter
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_scripts"))
import r3lib
_, rem = r3lib.read_csv(os.path.join(r3lib.WORK, "T4A_REMAPS.csv"))
rows = {}
for f in ("CLAIM_CONCORDANCE.csv", "EXTENSION_CONCORDANCE.csv"):
    _, rr = r3lib.read_csv(os.path.join(r3lib.R3, f))
    for r in rr:
        rows[r["ClaimKey"]] = r
new = {k: r["ImplementationEvidence"] for k, r in rows.items()}
calls = defaultdict(set)
for m in rem:
    new[m["ClaimKey"]] = new[m["ClaimKey"]].replace(m["Find"], m["Replace"], 1)
    calls[m["ClaimKey"]].add(m["Call"])
for c in ("a", "b"):
    keys = sorted(k for k in calls if c in calls[k])
    lost = [k for k in keys if "LIVE" in r3lib.reach_tags(rows[k]["ImplementationEvidence"]) and "LIVE" not in r3lib.reach_tags(new[k])]
    onlyleg = [k for k in lost if set(r3lib.reach_tags(new[k])) <= {"LEGACY_ONLY", "TEST_ONLY"} and "LEGACY_ONLY" in r3lib.reach_tags(new[k])]
    print(f"== call {c}: rows {len(keys)}; by deliverable", dict(Counter(rows[k]["DeliverableID"] or rows[k]["PackageID"] for k in keys)))
    print(f"   lose last LIVE tag: {len(lost)}; dispositions", dict(Counter(rows[k]["Disposition"] for k in lost)))
    print(f"   of which LEGACY_ONLY present (R4-Q1 rule 3 candidates) and HDN lacks R4-Q1:",
          [k for k in onlyleg if "R4-Q1" not in rows[k]["HumanDecisionNeeded"]])
    print("   lost-LIVE keys:", " ".join(lost))
    print("   aligned/implemented lost-LIVE:", [k + ":" + rows[k]["Disposition"] for k in lost if rows[k]["Disposition"] in ("ALIGNED", "IMPLEMENTED_DIFFERENTLY", "PARTIALLY_IMPLEMENTED")])
print("owner-deferred touched:", [k for k in calls if k in ("DEL-06-02#CLM-005", "DEL-06-02#CLM-032")])
