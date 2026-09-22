#!/usr/bin/env python3
"""T1 (R4 step 1): list the OWNER_CHECK.md rows (decided/noted per OC) with their current final fields."""
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_scripts"))
from r3lib import *

def oc_rows():
    txt = open(os.path.join(R3, "OWNER_CHECK.md"), encoding="utf-8").read()
    out = []
    for blk in re.split(r"(?m)^\*\*(OC-\d+)\.\*\*", txt)[1:]:
        pass
    parts = re.split(r"(?m)^\*\*(OC-\d+)\.\*\*", txt)
    for i in range(1, len(parts), 2):
        oc, body = parts[i], parts[i + 1]
        for kind in ("decided", "noted"):
            m = re.search(rf"Rows {kind} \(\d+\): (.*)", body)
            for k in re.findall(r"`([^`]+)`", m.group(1)):
                out.append((oc, kind, k))
    return out

if __name__ == "__main__":
    rows = {r["ClaimKey"]: r for r in read_csv(os.path.join(R3, "CLAIM_CONCORDANCE.csv"))[1] + read_csv(os.path.join(R3, "EXTENSION_CONCORDANCE.csv"))[1]}
    lst = oc_rows()
    print(len(lst), len({k for _, _, k in lst}))
    sel = sys.argv[1:] 
    for oc, kind, k in lst:
        if sel and oc not in sel: continue
        r = rows[k]
        print(f"=== {oc} {kind} {k}")
        for f in ("ClaimType","DeclaredState","Disposition","CauseTag","Confidence","RemainingWork","HumanDecisionNeeded","DirectionEvidence","ImplementationEvidence","VerificationEvidence","Notes","SourceLedger"):
            print(f"  {f}: {r[f]}")
