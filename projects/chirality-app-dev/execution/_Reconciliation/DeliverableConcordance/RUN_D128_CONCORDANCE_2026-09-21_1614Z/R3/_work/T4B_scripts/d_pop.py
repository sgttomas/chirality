import sys, os, re, collections
sys.path.insert(0, "../../_scripts")
from r3lib import read_csv, R3
terms = re.compile(r'K-PERM-1\b|K-PERM-6\b|DIRECTIVE\s*§\s*(2\.8|2\.10|4\.1|4\.2)\b|§\s*(2\.8|2\.10|4\.1|4\.2)\b|Full access|full-access|~/\.codex|\.codex\b|approval polic|approvalPolicy|shared (Codex )?config|pass-through|passthrough|R4-Q6', re.I)
gov = re.compile(r'D-GOV-43')
c=collections.Counter()
for fn in ["CLAIM_CONCORDANCE.csv", "EXTENSION_CONCORDANCE.csv"]:
    h, rows = read_csv(os.path.join(R3, fn))
    for r in rows:
        blob=" ".join(r[k] for k in h if k not in ("SourceLedger",))
        m = terms.findall(blob)
        if m and gov.search(blob):
            hits=sorted({x if isinstance(x,str) else next(y for y in x if y) for x in terms.finditer(blob) for x in [x.group(0)]})
            c[(r["Disposition"])]+=1
            print(r["ClaimKey"],"|",r["Disposition"],"|",r["SealedDisposition"],"|",r["CauseTag"],"|",r["HumanDecisionNeeded"],"|",";".join(hits)[:90])
print(c)
