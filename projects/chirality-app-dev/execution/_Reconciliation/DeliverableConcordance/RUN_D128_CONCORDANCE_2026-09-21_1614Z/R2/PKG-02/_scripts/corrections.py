#!/usr/bin/env python3
"""Build R2/PKG-02/CORRECTIONS.csv (RUN_BASIS Addendum 3) from the verifier shards of the ledgers of
record (_verify/V-SHARD-*.csv; superseded attempts under _verify/_ORIGINAL are excluded).
One row per REFUTED item whose Field is not a verdict field. Verdict fields: Disposition (ledger or
errata row) and reverse Response. Class-e items (errata rows) refuted on a non-verdict field are
recorded against the errata field. Columns: ClaimKey,Field,SealedValue,CorrectedValue,VerifierShard,Evidence.
Also prints the verdict-field refutation share per deliverable: distinct checked rows = checked
ledger rows (classes a, a30, b, e) plus checked reverse rows (class c, keyed CapabilityID); a row counts
as refuted when REFUTED on Disposition (ledger/errata) or Response (reverse). Rerun trigger: > 10%."""
import csv, glob, io, os, collections
PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERDICT = {"Disposition", "Response"}
def dicts(p):
    r = list(csv.reader(io.StringIO(open(p, encoding="utf-8", newline="").read())))
    if r and r[-1] == ["#END"]: r = r[:-1]
    return [dict(zip(r[0], x)) for x in r[1:]]
def fieldname(f):
    f = f.strip()
    for v in VERDICT:
        if f.startswith(v): return v
    return f
out, stats = [], collections.defaultdict(lambda: [set(), set(), 0, 0])
for p in sorted(glob.glob(os.path.join(PKG, "_verify", "V-SHARD-*.csv"))):
    shard = os.path.basename(p)[2:-4]
    for v in dicts(p):
        f = fieldname(v["Field"]); s = stats[v["Unit"]]
        if v["Class"] in ("a", "a30", "b", "e"):
            s[0].add(v["ClaimKey"])
            if v["Verdict"] == "REFUTED" and f == "Disposition": s[1].add(v["ClaimKey"])
        if v["Class"] == "c":
            s[0].add("REV:" + v["CapabilityID"] + "|" + v["ClaimKey"])
            if v["Verdict"] == "REFUTED" and f == "Response": s[1].add("REV:" + v["CapabilityID"] + "|" + v["ClaimKey"])
        if v["Verdict"] == "REFUTED" and f not in VERDICT:
            key = v["ClaimKey"] if not v["CapabilityID"] else f"{v['ClaimKey']}|{v['CapabilityID']}"
            out.append([key, v["Field"] + (" (errata ProposedValue)" if v["Class"] == "e" else ""), v["RowValue"], v["CorrectReading"], shard, v["Evidence"]])
out.sort(key=lambda r: (r[0], r[1]))
with open(os.path.join(PKG, "CORRECTIONS.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh, lineterminator="\n"); w.writerow(["ClaimKey", "Field", "SealedValue", "CorrectedValue", "VerifierShard", "Evidence"]); w.writerows(out); fh.write("#END\n")
print("CORRECTIONS rows", len(out))
for u in sorted(stats):
    rows, rd, _, _ = stats[u]
    share = 100 * len(rd) / len(rows) if rows else 0
    print(f"{u}: distinct rows checked {len(rows)} (ledger {sum(1 for r in rows if not r.startswith('REV:'))}, reverse {sum(1 for r in rows if r.startswith('REV:'))}); verdict-field REFUTED rows {len(rd)} {sorted(rd)} ({share:.1f}%); {'RERUN' if share > 10 else 'PASS'}")
