"""T8A: dump sample rows with claim-index location and SoW excerpt (read-only)."""
import csv, os, sys, io
HERE = os.path.dirname(os.path.abspath(__file__))
R3 = os.path.dirname(os.path.dirname(HERE))
RUN = os.path.dirname(R3)
sys.path.insert(0, os.path.join(R3, "_scripts"))
from r3lib import read_csv

FROZEN = sys.argv[1]
start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
end = int(sys.argv[3]) if len(sys.argv) > 3 else 999
ctx = int(sys.argv[4]) if len(sys.argv) > 4 else 25

h, rows = read_csv(os.path.join(R3, "_work", "SPOT_S1_A.csv"))
with open(os.path.join(RUN, "R1_INVENTORY", "CLAIM_INDEX.csv"), newline="", encoding="utf-8") as f:
    idx = {r["ClaimKey"]: r for r in csv.DictReader(f)}
with open(os.path.join(RUN, "R1_INVENTORY", "DELIVERABLE_INVENTORY.csv"), newline="", encoding="utf-8") as f:
    inv = {r["DeliverableID"]: r for r in csv.DictReader(f)}
# next unit line for bounding
by_file = {}
for k, r in idx.items():
    by_file.setdefault((r["DeliverableID"], r["SourceFile"]), []).append(int(r["SourceLine"]) if r["SourceLine"].isdigit() else 0)

for i, r in enumerate(rows):
    if i < start or i >= end:
        continue
    print("=" * 100)
    for c in h:
        if c in ("PackageID", "DeliverableID"):
            continue
        print(f"{c}: {r[c]}")
    base = r["ClaimKey"].split("#")[0] + "#" + r["ClaimKey"].split("#")[1].split(".")[0]
    ir = idx.get(base) or idx.get(r["ClaimKey"])
    if not ir:
        print("-- no index row")
        continue
    d = inv[r["DeliverableID"]]["Path"]
    p = os.path.join(FROZEN, d, ir["SourceFile"])
    print(f"-- INDEX {ir['SourceFile']}:{ir['SourceLine']} [{ir['Section']} / {ir['Label']}] sub={ir['SubItems']}")
    try:
        lines = open(p, encoding="utf-8").read().split("\n")
    except Exception as e:
        print("-- cannot read", e)
        continue
    s = int(ir["SourceLine"])
    nxt = sorted(x for x in by_file[(r["DeliverableID"], ir["SourceFile"])] if x > s)
    e = min(nxt[0] - 1 if nxt else s + ctx, s + ctx)
    for n in range(s - 1, min(e, len(lines))):
        print(f"  {n+1}: {lines[n][:400]}")
