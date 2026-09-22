"""D1: P-23 sub-questions by final Disposition. a = STALE_SPECIFICATION (text out of date); b = ACCEPTED_DIVERGENCE
(difference already permitted); d = other rows in DEL-03-02, DEL-08-04, DEL-08-05, DEL-09-02 (managed/descendant
delegation gates, which done-declaration Q-11 bears on); c = every other PRIMARY row (open gate)."""
import sys, os, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_scripts"))
from r4lib import load_concordance, read_csv, write_csv, R4
conc = load_concordance()
h, idx = read_csv(os.path.join(R4, "PACKET_INDEX.csv"))
keys = [r["ClaimKey"] for r in idx if r["PacketID"] == "P-23" and r["Role"] == "PRIMARY"]
m = {"STALE_SPECIFICATION": "a", "ACCEPTED_DIVERGENCE": "b"}
Q11 = {"DEL-03-02", "DEL-08-04", "DEL-08-05", "DEL-09-02"}
out = [{"ClaimKey": k, "SubQ": m.get(conc[k]["Disposition"]) or ("d" if k.split("#")[0] in Q11 else "c")} for k in keys]
write_csv(os.path.join(R4, "_work", "SUBQ", "P-23_subq.csv"), ["ClaimKey", "SubQ"], out)
print(collections.Counter(o["SubQ"] for o in out))
for s in "abcd": print(s, [o["ClaimKey"] for o in out if o["SubQ"] == s])
