#!/usr/bin/env python3
"""Deterministic stratified sample for the R3 independent spot check (blind to REMAP_LOG rationale).
S1: ~5% of rows (not AUTHORITY_CONFLICT/UNKNOWN), stratified by PackageID x Disposition (largest-remainder
allocation, at least 1 per stratum of >= 8 rows), picked by SHA-256 order of the key.
S2: every AUTHORITY_CONFLICT and UNKNOWN row, ordered so the first 40 are package-stratified (mandatory).
S3: 30 REMAP_LOG entries from R3_RULE / R3_RUNWIDE (non-Notes), stratified by Source x Field.
Outputs _work/SPOT_S1_A.csv, SPOT_S1_B.csv, SPOT_S2S3.csv (cells shown are final values; no rationale)."""
import os, hashlib, collections, math
from r3lib import *
h = lambda s: hashlib.sha256(s.encode()).hexdigest()
rows = read_csv(os.path.join(R3, "CLAIM_CONCORDANCE.csv"))[1] + read_csv(os.path.join(R3, "EXTENSION_CONCORDANCE.csv"))[1]
log = read_csv(os.path.join(R3, "REMAP_LOG.csv"))[1]
SHOW = ["ClaimKey", "PackageID", "DeliverableID", "ClaimType", "NormativeSource", "AuthorityTier", "LatestDecision",
        "DeclaredState", "ImplementationEvidence", "VerificationEvidence", "Disposition", "CauseTag", "HumanDecisionNeeded"]
pool = [r for r in rows if r["Disposition"] not in ("AUTHORITY_CONFLICT", "UNKNOWN")]
strata = collections.defaultdict(list)
for r in pool:
    strata[(r["PackageID"], r["Disposition"])].append(r)
target = round(0.05 * len(rows))
alloc = {k: (1 if len(v) >= 8 else 0) for k, v in strata.items()}
rest = target - sum(alloc.values())
quota = {k: len(v) / len(pool) * rest for k, v in strata.items()}
for k in quota:
    alloc[k] += int(quota[k])
left = target - sum(alloc.values())
for k in sorted(quota, key=lambda k: -(quota[k] - int(quota[k])))[:max(left, 0)]:
    alloc[k] += 1
s1 = []
for k, v in sorted(strata.items()):
    s1 += sorted(v, key=lambda r: h(r["ClaimKey"]))[:min(alloc[k], len(v))]
A = [r for r in s1 if r["PackageID"] in ("PKG-00", "PKG-01", "PKG-02", "PKG-03", "PKG-04", "PKG-05")]
B = [r for r in s1 if r not in A]
cols = ["SampleID", "CheckField"] + SHOW
write_csv(os.path.join(WORK, "SPOT_S1_A.csv"), cols, [dict(r, SampleID=f"S1-{i+1:03d}", CheckField="Disposition") for i, r in enumerate(A)])
write_csv(os.path.join(WORK, "SPOT_S1_B.csv"), cols, [dict(r, SampleID=f"S1-{len(A)+i+1:03d}", CheckField="Disposition") for i, r in enumerate(B)])
s2 = [r for r in rows if r["Disposition"] in ("AUTHORITY_CONFLICT", "UNKNOWN")]
bypk = collections.defaultdict(list)
for r in sorted(s2, key=lambda r: h(r["ClaimKey"])):
    bypk[(r["PackageID"], r["Disposition"])].append(r)
order = []
while any(bypk.values()):
    for k in sorted(bypk):
        if bypk[k]:
            order.append(bypk[k].pop(0))
cand = [l for l in log if l["Source"] in ("R3_RULE", "R3_RUNWIDE") and l["Field"] != "Notes"]
st = collections.defaultdict(list)
for i, l in enumerate(cand):
    st[(l["Source"], l["Field"])].append((i, l))
pick = []
keys = sorted(st)
while len(pick) < 30 and any(st.values()):
    for k in keys:
        if st[k] and len(pick) < 30:
            st[k].sort(key=lambda x: h(x[1]["ClaimKey"] + x[1]["Field"] + x[1]["NewValue"]))
            pick.append(st[k].pop(0)[1])
byk = {r["ClaimKey"]: r for r in rows}
out = []
for i, r in enumerate(order):
    out.append(dict(r, SampleID=f"S2-{i+1:03d}", CheckField="Disposition+HumanDecisionNeeded", Priority="MANDATORY" if i < 40 else "OPTIONAL"))
for i, l in enumerate(pick):
    r = byk[l["ClaimKey"]]
    out.append(dict(r, SampleID=f"S3-{i+1:03d}", CheckField=l["Field"], Priority="MANDATORY",
                    PriorValue=l["SealedValue"], RemappedValue=l["NewValue"]))
write_csv(os.path.join(WORK, "SPOT_S2S3.csv"), ["SampleID", "Priority", "CheckField", "PriorValue", "RemappedValue"] + SHOW, out)
print("S1", len(s1), "A", len(A), "B", len(B), "| S2", len(order), "| S3", len(pick), collections.Counter((l["Source"], l["Field"]) for l in pick))
