#!/usr/bin/env python3
"""Build R2/PKG-07/CORRECTIONS.csv (RUN_BASIS Addendum 3) from the verifier shards of the ledgers of record.
One row per (ClaimKey, non-verdict Field) REFUTED by a shard. Verdict fields (Disposition; reverse Response /
its ClaimKey) are excluded: they count toward the rerun threshold and are listed in VERIFICATION.md instead.
SealedValue is copied from the sealed ledger; CorrectedValue is the shard's CorrectReading (whitespace-normalised),
or, for vocabulary fields (PostReleaseBasis, AuthorityTier, HumanDecisionNeeded), the bare token extracted from it
with the full reading appended to Evidence.
A shard Field naming several fields ("a; b; c") yields one row per non-verdict field, each carrying the full reading."""
import csv, io, os, re, sys
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECORD = {"DEL-07-01": "DEL-07-01", "DEL-07-02": "DEL-07-02_A", "DEL-07-03": "DEL-07-03", "DEL-07-04": "DEL-07-04", "DEL-07-05": "DEL-07-05", "DEL-07-06": "DEL-07-06"}
VERDICT = {"Disposition", "Response", "ClaimKey"}
TOKEN = {"PostReleaseBasis": r"^(YES|NO)\b", "AuthorityTier": r"AuthorityTier = (GOVERNANCE_INVARIANT|PRD|LOCAL_DESIGN|NOT_APPLICABLE)",
         "HumanDecisionNeeded": r"HumanDecisionNeeded (NO|R4-Q[1-5]|R4|D-(?:APP|GOV)-\d+)\b",
         "CauseTag": r"^([A-Z][A-Z0-9_]+(?::[A-Z0-9_]+)?)\b", "AssessmentEvidence": r"^(OVERTAKEN|STILL CURRENT|NOT APPLICABLE)\b"}
def rows(p):
    t = open(p, encoding="utf-8").read().rstrip()
    t = t[:-6] if t.endswith('"#END"') else (t[:-4] if t.endswith("#END") else t)
    return list(csv.DictReader(io.StringIO(t)))
out = []
for d, u in RECORD.items():
    led = {r["ClaimKey"]: r for r in rows(os.path.join(P, u, d + "_claims.csv"))}
    shard = "V-" + u
    for v in rows(os.path.join(P, "_verify", shard + ".csv")):
        if v["Verdict"] != "REFUTED" or v["Class"] == "c": continue
        for fld in [x.strip() for x in v["Field"].split(";") if x.strip()]:
            if fld in VERDICT: continue
            if fld not in led[v["ClaimKey"]]: sys.exit(f"unknown field {fld} for {v['ClaimKey']}")
            reading = " ".join(v["CorrectReading"].split()); ev = " ".join(v["Evidence"].split())
            m = TOKEN.get(fld) and re.search(TOKEN[fld], reading)
            if m:  # vocabulary field: CorrectedValue is the bare token; the verifier's reading moves to Evidence
                out.append([v["ClaimKey"], fld, led[v["ClaimKey"]][fld], m.group(1), shard, ev + " || reading: " + reading])
            else:
                out.append([v["ClaimKey"], fld, led[v["ClaimKey"]][fld], reading, shard, ev])
out.sort(key=lambda r: (r[0], r[1]))
with open(os.path.join(P, "CORRECTIONS.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh); w.writerow(["ClaimKey", "Field", "SealedValue", "CorrectedValue", "VerifierShard", "Evidence"]); w.writerows(out); fh.write("#END\n")
print(len(out), "rows")
