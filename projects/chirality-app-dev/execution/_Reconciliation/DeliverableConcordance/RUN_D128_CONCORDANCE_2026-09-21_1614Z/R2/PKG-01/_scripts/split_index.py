#!/usr/bin/env python3
"""Write R2/PKG-01/_split/INDEX_S1.csv and INDEX_S2.csv: DEL-01-02 subsets of R1_INVENTORY/CLAIM_INDEX.csv
for the two split workers (brief step 3; CONVENTIONS §10). S1 = SoW Ontology + Epistemology
(CLM-001..CLM-023) and the Remaining item REM-1; S2 = Praxeology + Axiology (CLM-024..CLM-060).
Every other deliverable's rows are dropped. Used only as the --index for per-half validation;
the merged ledger is validated against the full CLAIM_INDEX."""
import csv, os
P = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); RUN = os.path.dirname(os.path.dirname(P))
src = os.path.join(RUN, "R1_INVENTORY", "CLAIM_INDEX.csv")
lines = [l for l in open(src, encoding="utf-8").read().split("\n") if l.strip() and l.strip() != "#END"]
rows = list(csv.DictReader(lines)); hdr = list(rows[0].keys())
d = [r for r in rows if r["DeliverableID"] == "DEL-01-02"]
def s1(r): return r["LocalID"].startswith("REM") or (r["LocalID"].startswith("CLM") and int(r["LocalID"][4:]) <= 23)
for name, sel in (("S1", [r for r in d if s1(r)]), ("S2", [r for r in d if not s1(r)])):
    with open(os.path.join(P, "_split", f"INDEX_{name}.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, hdr); w.writeheader(); w.writerows(sel); fh.write("#END\n")
    print(name, len(sel), sel[0]["LocalID"], sel[-1]["LocalID"])
