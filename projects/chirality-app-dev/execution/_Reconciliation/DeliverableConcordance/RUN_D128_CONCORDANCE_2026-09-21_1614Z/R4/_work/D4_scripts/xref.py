"""D4 helper: for each packet's PRIMARY rows, which other packets also list them (read-only)."""
import sys, os, collections
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_scripts"))
from r4lib import load_concordance, read_csv, R4
conc = load_concordance()
h, idx = read_csv(os.path.join(R4, "PACKET_INDEX.csv"))
by = collections.defaultdict(list)
for r in idx: by[r["ClaimKey"]].append((r["PacketID"], r["Role"]))
for pid in sys.argv[1:]:
    keys = [r["ClaimKey"] for r in idx if r["PacketID"] == pid and r["Role"] == "PRIMARY"]
    c = collections.Counter(p for k in keys for p, ro in by[k] if p != pid)
    print(pid, len(keys), "also-in:", dict(c.most_common()))
    d = collections.Counter(conc[k]["Disposition"] for k in keys); print("  ", dict(d))
