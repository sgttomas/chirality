import sys, os, re
sys.path.insert(0, "../../_scripts")
from r3lib import read_csv, R3
exec(open("d_terms.py").read())
want=set(sys.argv[1].split(","))
for fn in ["CLAIM_CONCORDANCE.csv", "EXTENSION_CONCORDANCE.csv"]:
    h, rows = read_csv(os.path.join(R3, fn))
    for r in rows:
        blob=" ".join(r[k] for k in h if k!="SourceLedger")
        if terms.search(blob) and gov.search(blob) and r["Disposition"] in want:
            print(f"## {r['ClaimKey']} | {r['Disposition']} | {r['HumanDecisionNeeded']} | LD={r['LatestDecision'][:60]}")
            print("  NS:", r["NormativeSource"][:220].replace("\n"," "))
            print("  DS:", r["DeclaredState"][:260].replace("\n"," "))
            print("  NT:", r["Notes"][:520].replace("\n"," "))
