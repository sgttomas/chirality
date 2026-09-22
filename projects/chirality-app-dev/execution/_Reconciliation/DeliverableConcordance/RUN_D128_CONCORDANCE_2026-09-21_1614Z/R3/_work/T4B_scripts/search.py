import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_scripts"))
from r3lib import read_csv, R3
pat = re.compile(sys.argv[1], re.I)
fields = sys.argv[2].split(",") if len(sys.argv) > 2 else None
for fn in ["CLAIM_CONCORDANCE.csv", "EXTENSION_CONCORDANCE.csv"]:
    h, rows = read_csv(os.path.join(R3, fn))
    for r in rows:
        blob = " | ".join(r.values())
        if pat.search(blob):
            if fields:
                print(fn[:3], " || ".join(f"{f}={r.get(f,'')}" for f in fields))
            else:
                print(fn[:3], r)
