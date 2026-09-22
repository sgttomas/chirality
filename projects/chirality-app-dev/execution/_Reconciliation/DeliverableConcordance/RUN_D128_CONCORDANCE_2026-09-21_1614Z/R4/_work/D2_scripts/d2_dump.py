"""D2: dump packet rows (key, disposition, HDN, source, notes excerpt). Usage: d2_dump.py P-nn [PRIMARY|ALL]"""
import os, sys, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_scripts"))
from r4lib import load_concordance, read_csv, R4
conc = load_concordance()
pi = read_csv(os.path.join(R4, "PACKET_INDEX.csv"))[1]
pid = sys.argv[1]; mode = sys.argv[2] if len(sys.argv) > 2 else "PRIMARY"
n = int(sys.argv[3]) if len(sys.argv) > 3 else 160
for r in pi:
    if r["PacketID"] != pid or (mode == "PRIMARY" and r["Role"] != "PRIMARY"): continue
    c = conc[r["ClaimKey"]]
    print(f"{r['ClaimKey']} [{r['Role']}] {c['Disposition']} | HDN={c['HumanDecisionNeeded']} | LD={c['LatestDecision']} | {c['CauseTag']}")
    print("   SRC:", c["NormativeSource"][:n].replace("\n", " "))
    print("   NOTE:", c["Notes"][:n].replace("\n", " "))
