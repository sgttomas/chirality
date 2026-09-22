#!/usr/bin/env python3
"""T2B candidates: rows whose ImplementationEvidence lost every LIVE tag under run-wide reach calls
(a)/(b) (DEC_RUNWIDE_REACH.csv) and whose Disposition says code meets the claim in whole or part."""
import os, collections
from r3lib import *
MEET = {"ALIGNED", "PARTIALLY_IMPLEMENTED", "IMPLEMENTED_DIFFERENTLY", "ACCEPTED_DIVERGENCE", "IMPLEMENTED_UNDOCUMENTED"}
keys = {r["ClaimKey"] for r in read_csv(os.path.join(WORK, "DEC_RUNWIDE_REACH.csv"))[1]}
log = read_csv(os.path.join(R3, "REMAP_LOG.csv"))[1]
before = {}
for l in log:
    if l["ClaimKey"] in keys and l["Field"] == "ImplementationEvidence" and l["Source"] == "R3_RUNWIDE" and l["ClaimKey"] not in before:
        before[l["ClaimKey"]] = l["SealedValue"]
rows = read_csv(os.path.join(R3, "CLAIM_CONCORDANCE.csv"))[1] + read_csv(os.path.join(R3, "EXTENSION_CONCORDANCE.csv"))[1]
out = []
for r in rows:
    k = r["ClaimKey"]
    if k not in before or k in DB_B_KEYS:
        continue
    pre, post = set(reach_tags(before[k])), set(reach_tags(r["ImplementationEvidence"]))
    if "LIVE" in pre and "LIVE" not in post and r["SealedDisposition"] in MEET:
        out.append(dict(r, PreReachTags="|".join(sorted(pre)), PostReachTags="|".join(sorted(post)),
                        PreReachImplementationEvidence=before[k]))
cols = ["ClaimKey", "PackageID", "DeliverableID", "ClaimType", "NormativeSource", "DeclaredState", "PreReachTags",
        "PostReachTags", "PreReachImplementationEvidence", "ImplementationEvidence", "VerificationEvidence",
        "SealedDisposition", "CauseTag", "HumanDecisionNeeded", "Notes"]
write_csv(os.path.join(WORK, "CAND_SUBJECT.csv"), cols, out)
print(len(out), collections.Counter(x["SealedDisposition"] for x in out), collections.Counter(x["PostReachTags"] for x in out))
