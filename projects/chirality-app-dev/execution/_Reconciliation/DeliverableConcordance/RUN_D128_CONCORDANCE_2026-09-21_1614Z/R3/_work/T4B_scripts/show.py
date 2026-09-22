import sys, os
sys.path.insert(0, "../../_scripts")
from r3lib import read_csv, R3
keys=set(sys.argv[1].split(","))
cols=sys.argv[2].split(",") if len(sys.argv)>2 else None
for fn in ["CLAIM_CONCORDANCE.csv", "EXTENSION_CONCORDANCE.csv"]:
    h, rows = read_csv(os.path.join(R3, fn))
    for r in rows:
        if r["ClaimKey"] in keys:
            print("=====", r["ClaimKey"])
            for k in (cols or h):
                print(f"  {k}: {r[k]}")
