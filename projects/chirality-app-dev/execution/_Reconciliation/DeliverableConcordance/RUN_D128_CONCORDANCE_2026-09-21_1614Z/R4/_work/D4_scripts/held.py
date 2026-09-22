"""D4 helper: per packet, PRIMARY rows mentioning D-APP-116..119, D-APP-128 sub-conditions (read-only)."""
import sys, os, re, collections
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_scripts"))
from r4lib import load_concordance, read_csv, R4
conc = load_concordance()
h, idx = read_csv(os.path.join(R4, "PACKET_INDEX.csv"))
pat = re.compile(r"D-APP-11[6-9]\b")
for pid in sys.argv[1:]:
    keys = [r["ClaimKey"] for r in idx if r["PacketID"] == pid and r["Role"] == "PRIMARY"]
    hits = [k for k in keys if pat.search(" ".join(conc[k][f] for f in ("LatestDecision","HumanDecisionNeeded","Notes","DirectionEvidence")))]
    print(pid, len(keys), "held-candidates:", len(hits), hits[:12])
    c = collections.Counter(conc[k]["HumanDecisionNeeded"] for k in keys); print("  HDN", dict(c))
