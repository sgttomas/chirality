#!/usr/bin/env python3
"""Write the DEL-02-01 half indexes for the split (CONVENTIONS §10; brief step 3).
Half A: SEC-1..SEC-5 and CLM-001..CLM-015 (ScopeOfWork.md lines 1-319: SCA gate contracts, Ontology,
Epistemology). Half B: CLM-016..CLM-030 and REM-1..REM-7 (ScopeOfWork.md line 320 to end: Praxeology,
Axiology; and _STATUS.md Remaining). Each half index holds the CLAIM_INDEX header plus that half's
DEL-02-01 rows, so `validate_ledger.py ledger --index <half>` checks coverage of that half only.
Output: _split/INDEX_A.csv, _split/INDEX_B.csv (CLAIM_INDEX byte format; no #END added unless the
source has one)."""
import csv, io, os
PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); RUN = os.path.dirname(os.path.dirname(PKG))
src = open(os.path.join(RUN, "R1_INVENTORY", "CLAIM_INDEX.csv"), encoding="utf-8", newline="").read()
rows = list(csv.reader(io.StringIO(src))); end = rows[-1] == ["#END"]
hdr, data = rows[0], [r for r in rows[1:] if r != ["#END"]]
H = {h: i for i, h in enumerate(hdr)}
def half(r):
    loc = r[H["LocalID"]]
    if loc.startswith("SEC-"): return "A"
    if loc.startswith("REM"): return "B"
    return "A" if int(loc.split("-")[1]) <= 15 else "B"
for h in "AB":
    sel = [r for r in data if r[H["DeliverableID"]] == "DEL-02-01" and half(r) == h]
    with open(os.path.join(PKG, "_split", f"INDEX_{h}.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n"); w.writerow(hdr); w.writerows(sel)
        if end: fh.write("#END\n")
    print(h, len(sel), [r[H["LocalID"]] for r in sel])
