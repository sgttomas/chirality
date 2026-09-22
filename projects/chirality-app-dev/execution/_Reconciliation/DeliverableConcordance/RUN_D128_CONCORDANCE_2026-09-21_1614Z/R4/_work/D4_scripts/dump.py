"""D4 helper: dump PRIMARY rows of a packet with selected fields (read-only)."""
import sys, os, collections
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_scripts"))
from r4lib import load_concordance, read_csv, R4
pid = sys.argv[1]; fields = sys.argv[2].split(",") if len(sys.argv) > 2 else None
role = sys.argv[3] if len(sys.argv) > 3 else "PRIMARY"
conc = load_concordance()
h, idx = read_csv(os.path.join(R4, "PACKET_INDEX.csv"))
keys = [r["ClaimKey"] for r in idx if r["PacketID"] == pid and r["Role"] == role]
print(len(keys), "rows")
if fields is None:
    print(list(conc[keys[0]].keys())); sys.exit()
W = int(os.environ.get("W", "220"))
for k in keys:
    r = conc[k]
    print(k, " | ".join(f"{f}={r.get(f,'')[:W]}" for f in fields))
