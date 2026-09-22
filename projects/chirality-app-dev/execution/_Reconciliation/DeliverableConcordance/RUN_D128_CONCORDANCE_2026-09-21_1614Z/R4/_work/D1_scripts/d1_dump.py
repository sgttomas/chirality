"""D1 helper: dump rows by key or packet (read-only). usage: d1_dump.py (P-nn[:ROLE]|KEY[,KEY]) [fields|ALL]"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_scripts"))
from r4lib import load_concordance, read_csv, R4
conc = load_concordance()
sel = sys.argv[1]
if sel.startswith("P-"):
    pid, _, role = sel.partition(":")
    h, idx = read_csv(os.path.join(R4, "PACKET_INDEX.csv"))
    keys = [r["ClaimKey"] for r in idx if r["PacketID"] == pid and (not role or r["Role"] == role)]
else:
    keys = sel.split(",")
fields = sys.argv[2] if len(sys.argv) > 2 else "ALL"
W = int(os.environ.get("W", "100000"))
for k in keys:
    r = conc[k]
    fl = list(r.keys()) if fields == "ALL" else fields.split(",")
    print("=====", k)
    for f in fl:
        v = r.get(f, "")
        if v:
            print(f"  {f}: {v[:W]}")
