#!/usr/bin/env python3
"""Step 7 / RUN_BASIS Addendum 3: build CORRECTIONS.csv from verifier shards (REFUTED lines on
non-verdict fields) and print the verdict-field rerun threshold per ledger, rows and reverse separately.
Verdict fields: Disposition (ledger rows, incl. errata changing it), Response (reverse)."""
import csv, glob, io, os, collections
PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def rows(p):
    t = open(p, encoding="utf-8").read().rstrip("\n")
    recs = [r for r in csv.reader(io.StringIO(t)) if r and r != ["#END"]]
    return [dict(zip(recs[0], r)) for r in recs[1:]]
VERDICT = {"Disposition", "Response"}
corr = []; stat = collections.defaultdict(lambda: {"rows": set(), "rows_ref": set(), "rev": set(), "rev_ref": set()})
for f in sorted(glob.glob(os.path.join(PKG, "_verify", "V-*.csv"))):
    shard = os.path.basename(f)[2:-4]
    for r in rows(f):
        u = r["Unit"]; key = r["ClaimKey"] + ("|" + r["CapabilityID"] if r["Class"] == "c" else "")
        tgt = "rev" if r["Class"] == "c" else "rows"
        stat[u][tgt].add(key)
        if r["Verdict"] == "REFUTED":
            if r["Field"] in VERDICT: stat[u][tgt + "_ref"].add(key)
            else: corr.append([r["ClaimKey"], r["Field"], r["SealedValue"], r["CorrectReading"], shard, r["Evidence"]])
with open(os.path.join(PKG, "CORRECTIONS.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh, lineterminator="\n"); w.writerow(["ClaimKey", "Field", "SealedValue", "CorrectedValue", "VerifierShard", "Evidence"]); w.writerows(corr); fh.write("#END\n")
print("corrections", len(corr))
for u, s in sorted(stat.items()):
    for t in ("rows", "rev"):
        n, k = len(s[t]), len(s[t + "_ref"])
        if n: print(f"{u} {t}: {k}/{n} distinct verdict-field REFUTED = {100*k/n:.1f}% -> {'RERUN' if k/n > 0.10 else 'no rerun'}")
