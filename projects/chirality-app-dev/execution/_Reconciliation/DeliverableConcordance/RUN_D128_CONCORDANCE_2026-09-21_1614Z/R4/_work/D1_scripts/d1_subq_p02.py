"""D1: P-02 sub-questions. Rule: a = Disposition UNKNOWN and Notes name OC-20 (SoW-conversion checks);
b = Disposition UNKNOWN otherwise (OC-14/18/19); c = every other PRIMARY row (Disposition stands on code or text)."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_scripts"))
from r4lib import load_concordance, read_csv, write_csv, R4
conc = load_concordance()
h, idx = read_csv(os.path.join(R4, "PACKET_INDEX.csv"))
keys = [r["ClaimKey"] for r in idx if r["PacketID"] == "P-02" and r["Role"] == "PRIMARY"]
out = []
for k in keys:
    r = conc[k]
    s = ("a" if "OC-20" in r["Notes"] else "b") if r["Disposition"] == "UNKNOWN" else "c"
    out.append({"ClaimKey": k, "SubQ": s})
write_csv(os.path.join(R4, "_work", "SUBQ", "P-02_subq.csv"), ["ClaimKey", "SubQ"], out)
import collections; print(collections.Counter(o["SubQ"] for o in out))
