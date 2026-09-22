"""D2: P-10 sub-questions by HumanDecisionNeeded token.
Rule: a = HDN names D-APP-116..119 (AWAITING_RULING; held from R5); b = else HDN names D-APP-127 or D-GOV-43;
c = else (another RULED decision: D-APP-43, D-APP-73, D-APP-121). Also lists every row in either concordance
whose HDN names D-APP-116..119, with its PRIMARY packet."""
import os, sys, re, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_scripts"))
from r4lib import load_concordance, read_csv, R4, counts_table
conc = load_concordance()
pi = read_csv(os.path.join(R4, "PACKET_INDEX.csv"))[1]
role = {r["ClaimKey"]: r["PacketID"] for r in pi if r["Role"] == "PRIMARY"}
p10 = [r["ClaimKey"] for r in pi if r["PacketID"] == "P-10" and r["Role"] == "PRIMARY"]
HELD = re.compile(r"D-APP-11[6-9]\b")
def sq(k):
    h = conc[k]["HumanDecisionNeeded"]
    if HELD.search(h): return "a"
    if re.search(r"D-APP-127\b|D-GOV-43\b", h): return "b"
    return "c"
os.makedirs(os.path.join(R4, "_work", "SUBQ"), exist_ok=True)
with open(os.path.join(R4, "_work", "SUBQ", "P-10_subq.csv"), "w", newline="") as f:
    f.write("ClaimKey,SubQ\n")
    for k in p10: f.write(f"{k},{sq(k)}\n")
    f.write("#END\n")
g = collections.defaultdict(list)
for k in p10: g[sq(k)].append(k)
for s in "abc":
    print(s, len(g[s]), [(k, conc[k]["HumanDecisionNeeded"]) for k in g[s]])
held = [k for k, r in conc.items() if HELD.search(r["HumanDecisionNeeded"])]
print("all rows naming D-APP-116..119:", len(held))
print(collections.Counter(role.get(k, "none") for k in held))
for k in held:
    if role.get(k) != "P-10": print("  outside P-10:", k, role.get(k), conc[k]["HumanDecisionNeeded"])
