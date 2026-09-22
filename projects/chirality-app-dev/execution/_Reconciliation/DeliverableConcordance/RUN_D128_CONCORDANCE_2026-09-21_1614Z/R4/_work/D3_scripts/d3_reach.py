"""D3 helper: effect of the module-level reach reading on P-09 (call (a) retags LIVE->LEGACY_ONLY). Deterministic."""
import collections, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_scripts"))
import r4lib
conc = r4lib.load_concordance()
idx = r4lib.read_csv(os.path.join(r4lib.R4, "PACKET_INDEX.csv"))[1]
P = {r["ClaimKey"] for r in idx if r["PacketID"] == "P-09" and r["Role"] == "PRIMARY"}
_, log = r4lib.read_csv(os.path.join(r4lib.R3, "REMAP_LOG.csv"))
reachA = collections.defaultdict(list)
q1 = {}
for r in log:
    if r["Source"] == "R3_RUNWIDE" and r["Field"] == "ImplementationEvidence" and "DEC_RUNWIDE_REACH" in r["RuleOrEvidence"]:
        reachA[r["ClaimKey"]].append(r)
    if r["Field"] == "HumanDecisionNeeded" and "R4-Q1" in r["NewValue"] and "R4-Q1" not in r["SealedValue"]:
        q1[r["ClaimKey"]] = r["Source"] + ": " + r["RuleOrEvidence"][:60]
def tags(s): return set(re.findall(r"REACH=([A-Z_]+)", s))
n = 0; dep = []
for k in P:
    if k in reachA and k in q1:
        # did sealed evidence have LIVE that retag removed?
        sealed = reachA[k][0]["SealedValue"]; final = conc[k]["ImplementationEvidence"]
        if "LIVE" in tags(sealed) and "LIVE" not in tags(final):
            dep.append(k)
print("P-09 PRIMARY rows retagged by reach calls:", len([k for k in P if k in reachA]))
print("P-09 PRIMARY rows gaining R4-Q1 in R3:", len([k for k in P if k in q1]))
print("rows whose R4-Q1 depends on the symbol-level reading (LIVE lost by retag, R4-Q1 added in R3):", len(dep))
print(sorted(dep))
print(collections.Counter(conc[k]["Disposition"] for k in dep))
print(collections.Counter(q1[k][:30] for k in P if k in q1))
