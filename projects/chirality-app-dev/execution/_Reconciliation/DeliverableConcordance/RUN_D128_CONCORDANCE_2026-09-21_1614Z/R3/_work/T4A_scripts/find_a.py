"""T4A (a): list concordance rows whose ImplementationEvidence cites a disputed contracts module."""
import sys, re, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_scripts"))
import r3lib
PAT = re.compile(r"(domain-profile|operation-proposal|engine-conformance|tool-catalog|tool-descriptor|tool-names|sdk-version|harness-contract)")
for f in ["CLAIM_CONCORDANCE.csv", "EXTENSION_CONCORDANCE.csv"]:
    h, rows = r3lib.read_csv(os.path.join(r3lib.R3, f))
    for r in rows:
        ev = r["ImplementationEvidence"]
        if PAT.search(ev):
            print("=" * 5, f, r["ClaimKey"], r["Disposition"], "| HDN:", r["HumanDecisionNeeded"])
            print(ev)
