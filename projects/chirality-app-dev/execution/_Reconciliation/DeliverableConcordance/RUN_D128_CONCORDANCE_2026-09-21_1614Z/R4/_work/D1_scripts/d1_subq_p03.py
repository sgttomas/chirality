"""D1: P-03 sub-questions. Rule: b = DeclaredState names the G6a exact-candidate gate, WP-11, or the owner-directed
consolidated signed build (regex G6a|WP-11|owner directs); a = every other PRIMARY row (signing posture)."""
import sys, os, re, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_scripts"))
from r4lib import load_concordance, read_csv, write_csv, R4
conc = load_concordance()
h, idx = read_csv(os.path.join(R4, "PACKET_INDEX.csv"))
keys = [r["ClaimKey"] for r in idx if r["PacketID"] == "P-03" and r["Role"] == "PRIMARY"]
pat = re.compile(r"G6a|WP-11|owner directs", re.I)
out = [{"ClaimKey": k, "SubQ": "b" if pat.search(conc[k]["DeclaredState"]) else "a"} for k in keys]
write_csv(os.path.join(R4, "_work", "SUBQ", "P-03_subq.csv"), ["ClaimKey", "SubQ"], out)
print(collections.Counter(o["SubQ"] for o in out)); print([o["ClaimKey"] for o in out if o["SubQ"] == "b"])
