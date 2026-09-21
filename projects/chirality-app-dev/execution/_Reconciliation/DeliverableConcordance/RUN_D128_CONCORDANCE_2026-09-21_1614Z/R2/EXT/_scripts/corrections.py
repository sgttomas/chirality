#!/usr/bin/env python3
"""From the verifier shards (_verify/V-*.csv) build CORRECTIONS.csv (non-verdict-field
refutations, RUN_BASIS Addendum 3) and print the per-ledger rerun test:
structural failure, or > 10% of checked distinct rows REFUTED on Disposition.
Writes _verify/VERDICTS.csv (all shard lines merged) for the summary and VERIFICATION.md."""
import csv, glob, json, os, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extlib import EXT, LEDGERS, ledger_path, read_rows, SUPERSEDED

VERDICT_FIELDS = {"Disposition"}
lines = []
for p in sorted(glob.glob(os.path.join(EXT, "_verify", "V-*.csv"))):
    _, rs = read_rows(p)
    lines += [x for x in rs if (x["Shard"], x["Ledger"]) not in SUPERSEDED]
sel_hdr, sel = read_rows(os.path.join(EXT, "_verify", "SELECTION.csv"))
checked = collections.defaultdict(set)
sel = [s for s in sel if (s["Shard"], s["Ledger"]) not in SUPERSEDED]
for s in sel: checked[s["Ledger"]].add(s["ClaimKey"])
seen = {(l["Ledger"], l["ClaimKey"]) for l in lines}
missing = [(s["Shard"], s["ClaimKey"]) for s in sel if (s["Ledger"], s["ClaimKey"]) not in seen]

corr = []
refd = collections.defaultdict(set)
for l in lines:
    if l["Verdict"] != "REFUTED": continue
    if l["Field"] in VERDICT_FIELDS:
        refd[l["Ledger"]].add(l["ClaimKey"]); continue
    if l["Class"] == "e": continue  # errata-row refutations are reported, not corrected
    corr.append([l["ClaimKey"], l["Field"], l["RowValue"], l["CorrectReading"], l["Shard"], l["Evidence"]])
with open(os.path.join(EXT, "CORRECTIONS.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh, lineterminator="\n")
    w.writerow(["ClaimKey", "Field", "SealedValue", "CorrectedValue", "VerifierShard", "Evidence"])
    w.writerows(sorted(corr)); fh.write("#END\n")
with open(os.path.join(EXT, "_verify", "VERDICTS.csv"), "w", newline="", encoding="utf-8") as fh:
    hdr = ["Shard", "Ledger", "Class", "ClaimKey", "Verdict", "Field", "RowValue", "CorrectReading", "Evidence", "ConventionIssue"]
    w = csv.writer(fh, lineterminator="\n"); w.writerow(hdr)
    for l in lines: w.writerow([l.get(k, "") for k in hdr])
    fh.write("#END\n")
res = {}
for stem, _, _ in LEDGERS:
    n = len(checked.get(stem, ())); r = len(refd.get(stem, ()))
    res[stem] = {"checked": n, "disp_refuted": r, "rate": round(r / n, 3) if n else 0.0,
                 "rerun": bool(n and r / n > 0.10), "refuted_keys": sorted(refd.get(stem, ()))}
print(json.dumps({"missing_items": missing, "corrections": len(corr), "ledgers": res}, indent=1))
