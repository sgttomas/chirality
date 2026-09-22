import sys, os, re, collections
sys.path.insert(0, "../../_scripts")
from r3lib import read_csv, R3
pat = re.compile(sys.argv[1], re.I)
cols = sys.argv[2].split(",") if len(sys.argv)>2 else None
for fn in ["CLAIM_CONCORDANCE.csv", "EXTENSION_CONCORDANCE.csv"]:
    h, rows = read_csv(os.path.join(R3, fn))
    for r in rows:
        hit = [k for k,v in r.items() if pat.search(v)]
        if hit:
            print(r["ClaimKey"], "|", r["ClaimType"], "|", r["Disposition"], "|", r["SealedDisposition"], "|", r["CauseTag"], "|", r["HumanDecisionNeeded"], "| hit:", ",".join(hit))
