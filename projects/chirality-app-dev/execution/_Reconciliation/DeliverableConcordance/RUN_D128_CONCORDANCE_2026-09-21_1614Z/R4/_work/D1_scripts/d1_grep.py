"""D1 helper: rows whose any field matches a regex (case-insensitive); prints key, Disposition, HDN, PRIMARY packet."""
import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_scripts"))
from r4lib import load_concordance, read_csv, R4
conc = load_concordance()
h, idx = read_csv(os.path.join(R4, "PACKET_INDEX.csv"))
prim = {r["ClaimKey"]: r["PacketID"] for r in idx if r["Role"] == "PRIMARY"}
pat = re.compile(sys.argv[1], re.I)
hits = [(k, r) for k, r in conc.items() if any(pat.search(v) for v in r.values())]
print(len(hits), "rows")
for k, r in hits[: int(os.environ.get("N", "30"))]:
    print(" ", k, r["Disposition"], r["HumanDecisionNeeded"], prim.get(k))
