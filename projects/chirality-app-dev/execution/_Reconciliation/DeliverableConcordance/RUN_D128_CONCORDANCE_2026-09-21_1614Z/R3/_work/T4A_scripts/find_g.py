"""T4A (g): list concordance rows naming D-APP-104/107/122/123 in any field, with flag-reliance cues."""
import sys, re, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_scripts"))
import r3lib
IDS = re.compile(r"D-APP-(104|107|122|123)(?!\d)")
CUE = re.compile(r"(?i)(flag|HELD|held until|pending|not landed|unapplied|not applied|EFFECT_NOT_LANDED)")
for f in ["CLAIM_CONCORDANCE.csv", "EXTENSION_CONCORDANCE.csv"]:
    h, rows = r3lib.read_csv(os.path.join(r3lib.R3, f))
    for r in rows:
        blob = " ".join(r[c] for c in h)
        ids = sorted(set(IDS.findall(blob)))
        if not ids:
            continue
        fields = [c for c in h if IDS.search(r[c])]
        cues = []
        for c in h:
            for m in IDS.finditer(r[c]):
                win = r[c][max(0, m.start() - 120): m.end() + 160]
                if CUE.search(win):
                    cues.append(c)
        print("\t".join([f[:3], r["ClaimKey"], ",".join("D-APP-" + i for i in ids), r["Disposition"],
                         r["LatestDecision"], r["HumanDecisionNeeded"], "|".join(fields), "CUE:" + ",".join(sorted(set(cues)))]))
