#!/usr/bin/env python3
"""Writes R2/PKG-04/CORRECTIONS.csv (RUN_BASIS Addendum 3) by script from the verifier shards of the
ledgers of record (_verify/V-<DEL>.csv). One row per REFUTED item whose Field is not a verdict field
(Disposition / Response). SealedValue is copied from the sealed ledger; CorrectedValue is the shard's
CorrectReading, reduced to its leading vocabulary token for enumerated fields. Never edits a ledger."""
import sys; sys.path.insert(0, __import__("os").path.dirname(__file__))
from common import *
ENUM = {"AuthorityTier", "CauseTag", "HumanDecisionNeeded", "Confidence", "PostReleaseBasis", "MechanicallyUnblocked",
        "AssessmentEvidence", "ClaimType", "LatestDecision", "LifecycleState"}
out = []
for u in UNITS:
    p = os.path.join(P, "_verify", f"V-{u}.csv")
    if not os.path.exists(p): continue
    led = {r["ClaimKey"]: r for r in rows(f(u, "_claims.csv"))}
    for r in rows(p):
        fld = r["Field"].strip()
        if r["Verdict"].strip() != "REFUTED" or fld in ("Disposition", "Response"): continue
        cr = r["CorrectReading"].strip()
        if fld in ENUM:
            m = re.match(r"^((?:[A-Z][A-Z0-9_\-]*|NOT APPLICABLE|STILL CURRENT)(?:\s*;\s*[A-Z][A-Z0-9_\-]*)*)", cr)
            cr = m.group(1) if m else cr
        sealed = led.get(r["ClaimKey"], {}).get(fld, r["RowValue"])
        out.append([r["ClaimKey"], fld, sealed, cr, f"_verify/V-{u}.csv", r["Evidence"]])
with open(os.path.join(P, "CORRECTIONS.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(["ClaimKey", "Field", "SealedValue", "CorrectedValue", "VerifierShard", "Evidence"]); w.writerows(out)
    fh.write("#END\n")
for o in out: print(o[0], o[1], "|", o[3][:80])
print("ROWS", len(out), sha(os.path.join(P, "CORRECTIONS.csv")))
