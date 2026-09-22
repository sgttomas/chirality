"""D4: build R4/_work/SUBQ/P-nn_subq.csv for D4 packets. Deterministic rules:
- P-17: b = SOW:SOW-079.1 (no live deliverable carries the row); a = every other PRIMARY row.
- P-19: b = Disposition in {PARTIALLY_IMPLEMENTED, DOCUMENTED_UNIMPLEMENTED, IMPLEMENTED_DIFFERENTLY}; a = rest.
- P-20, P-21, P-22: b = Disposition in {PARTIALLY_IMPLEMENTED, DOCUMENTED_UNIMPLEMENTED}; a = rest."""
import sys, os, collections
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_scripts"))
from r4lib import load_concordance, read_csv, R4
conc = load_concordance()
h, idx = read_csv(os.path.join(R4, "PACKET_INDEX.csv"))
GAP = {"PARTIALLY_IMPLEMENTED", "DOCUMENTED_UNIMPLEMENTED"}
def rule(pid, k):
    d = conc[k]["Disposition"]
    if pid == "P-17": return "b" if k == "SOW:SOW-079.1" else "a"
    if pid == "P-19": return "b" if d in GAP | {"IMPLEMENTED_DIFFERENTLY"} else "a"
    return "b" if d in GAP else "a"
out = os.path.join(R4, "_work", "SUBQ"); os.makedirs(out, exist_ok=True)
for pid in ("P-17", "P-19", "P-20", "P-21", "P-22"):
    keys = [r["ClaimKey"] for r in idx if r["PacketID"] == pid and r["Role"] == "PRIMARY"]
    rows = [(k, rule(pid, k)) for k in keys]
    with open(os.path.join(out, f"{pid}_subq.csv"), "w", newline="") as f:
        f.write("ClaimKey,SubQ\n")
        for k, s in rows:
            f.write(f"\"{k}\",{s}\n" if "," in k else f"{k},{s}\n")
        f.write("#END\n")
    print(pid, len(keys), dict(collections.Counter(s for _, s in rows)))
