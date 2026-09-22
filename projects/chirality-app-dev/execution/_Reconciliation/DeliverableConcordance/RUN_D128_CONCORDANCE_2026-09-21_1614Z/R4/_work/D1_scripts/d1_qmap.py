"""D1 helper: map done-declaration questions Q-01..Q-13 to concordance rows naming them (any field), with Disposition and packet."""
import sys, os, re, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "_scripts"))
from r4lib import load_concordance, read_csv, R4
conc = load_concordance()
h, idx = read_csv(os.path.join(R4, "PACKET_INDEX.csv"))
prim = {r["ClaimKey"]: r["PacketID"] for r in idx if r["Role"] == "PRIMARY"}
pat = re.compile(r"(?<![\w-])Q-(0[1-9]|1[0-3])(?!\d)")
m = collections.defaultdict(list)
for k, r in conc.items():
    for f, v in r.items():
        for q in set(pat.findall(v)):
            m[q].append((k, f))
for q in sorted(m):
    seen = {}
    for k, f in m[q]:
        seen.setdefault(k, []).append(f)
    print(f"Q-{q}: {len(seen)} rows")
    for k, fs in seen.items():
        print("   ", k, conc[k]["Disposition"], conc[k]["HumanDecisionNeeded"], prim.get(k), ",".join(fs))
