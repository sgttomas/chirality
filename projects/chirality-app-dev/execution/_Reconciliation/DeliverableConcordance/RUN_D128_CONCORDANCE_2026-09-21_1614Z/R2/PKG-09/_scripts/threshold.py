#!/usr/bin/env python3
"""Rerun threshold per ledger of record (RUN_BASIS Addendum 3), computed separately on ledger rows
(classes a, a30, b, e -> distinct ClaimKeys; verdict field = Disposition) and on reverse responses
(class c -> distinct CapabilityIDs; verdict field = Response or its ClaimKey). Prints a Markdown table."""
import csv, glob, io, os
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def rows(p):
    t = open(p, encoding="utf-8").read().rstrip()
    t = t[:-6] if t.endswith('"#END"') else (t[:-4] if t.endswith("#END") else t)
    return list(csv.DictReader(io.StringIO(t)))
def fields(x): return {y.strip() for y in x["Field"].split(";")}
print("| Shard | Ledger rows checked (distinct) | Disposition REFUTED | Ledger share | Reverse responses checked | Response REFUTED | Reverse share | Rerun? |")
print("|---|---:|---:|---:|---:|---:|---:|---|")
for f in sorted(glob.glob(os.path.join(P, "_verify", "V-*.csv"))):
    v = rows(f); s = os.path.basename(f)[:-4]
    L = {x["ClaimKey"] for x in v if x["Class"] != "c"}
    LR = {x["ClaimKey"] for x in v if x["Class"] != "c" and x["Verdict"] == "REFUTED" and "Disposition" in fields(x)}
    R = {x["CapabilityID"] for x in v if x["Class"] == "c"}
    RR = {x["CapabilityID"] for x in v if x["Class"] == "c" and x["Verdict"] == "REFUTED" and fields(x) & {"Response", "ClaimKey"}}
    ls = 100 * len(LR) / max(len(L), 1); rs = 100 * len(RR) / max(len(R), 1)
    print(f"| {s} | {len(L)} | {len(LR)} | {ls:.1f}% | {len(R)} | {len(RR)} | {rs:.1f}% | {'YES' if ls > 10 or rs > 10 else 'no'} |")
