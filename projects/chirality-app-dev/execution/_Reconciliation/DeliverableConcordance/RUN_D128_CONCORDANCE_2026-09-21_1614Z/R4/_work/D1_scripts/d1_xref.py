"""D1 helper: for a packet's PRIMARY rows, list other packets where they are ALSO/CONTEXT members; and D-APP-116..119 mentions."""
import sys, os, collections, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_scripts"))
from r4lib import load_concordance, read_csv, R4
conc = load_concordance()
h, idx = read_csv(os.path.join(R4, "PACKET_INDEX.csv"))
by = collections.defaultdict(list)
for r in idx: by[r["ClaimKey"]].append((r["PacketID"], r["Role"]))
for pid in sys.argv[1:]:
    keys = [r["ClaimKey"] for r in idx if r["PacketID"] == pid and r["Role"] == "PRIMARY"]
    c = collections.Counter(p for k in keys for p, role in by[k] if p != pid)
    held = [k for k in keys if re.search(r"D-APP-11[6-9]", " ".join(conc[k].values()))]
    print(pid, len(keys), "other:", dict(c), "D-APP-116..119 mentions:", held)
