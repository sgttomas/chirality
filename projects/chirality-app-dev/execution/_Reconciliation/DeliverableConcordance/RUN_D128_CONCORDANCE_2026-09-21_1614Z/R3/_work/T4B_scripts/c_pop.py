import sys, os, re, collections
sys.path.insert(0, "../../_scripts")
from r3lib import read_csv, R3
ns = re.compile(r'\b(AC-001|VER-001)\b')
txt = re.compile(r'parity|legacy|claim map|claim-map|SoW conversion|conversion|migrat|D-APP-68|D-GOV-16', re.I)
out=[]
for fn in ["CLAIM_CONCORDANCE.csv", "EXTENSION_CONCORDANCE.csv"]:
    h, rows = read_csv(os.path.join(R3, fn))
    for r in rows:
        if ns.search(r["NormativeSource"]) or (re.search(r'parity', r["DeclaredState"]+r["NormativeSource"], re.I)):
            flag = bool(txt.search(r["DeclaredState"]+" "+r["NormativeSource"]))
            out.append(r)
            print(r["ClaimKey"],"|",r["Disposition"],"|",r["CauseTag"],"|",r["HumanDecisionNeeded"],"|",r["LatestDecision"][:40],"|T" if flag else "|F","|",r["DeclaredState"][:110].replace("\n"," "))
c=collections.Counter(r["Disposition"] for r in out); print(c, len(out))
