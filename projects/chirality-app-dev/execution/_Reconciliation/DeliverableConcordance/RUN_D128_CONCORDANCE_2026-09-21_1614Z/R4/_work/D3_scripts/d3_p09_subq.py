"""D3: assign every P-09 PRIMARY row to a sub-question. Deterministic rule:
c = ImplementationEvidence carries both REACH=LIVE and REACH=LEGACY_ONLY (live code meets part);
b = otherwise, the claim states a safety or control guarantee (subject-test rule 1 list): claim text
    (DeclaredState) or NormativeSource matches GUARANTEE regex;
a = every other row (features or engine-specific mechanisms only the legacy harness provides).
Writes R4/_work/SUBQ/P-09_subq.csv."""
import collections, csv, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_scripts"))
import r4lib
GUARANTEE = re.compile(r"hook|K-HOOK|K-PATH|K-ROOT|K-PERM|K-BASH|K-SUBAGENT|K-GATE|K-DOMAIN-2|15\.2|contain|instruction[- ]root|symlink|"
                       r"permission|deny|denied|denies|fail[- ]closed|redact|secret|credential|approv|gate|protected|quarantin|bash|shell|subagent governance", re.I)
conc = r4lib.load_concordance()
idx = r4lib.read_csv(os.path.join(r4lib.R4, "PACKET_INDEX.csv"))[1]
P = sorted(r["ClaimKey"] for r in idx if r["PacketID"] == "P-09" and r["Role"] == "PRIMARY")
def tags(r): return set(re.findall(r"REACH=([A-Z_]+)", r["ImplementationEvidence"]))
out = []
for k in P:
    r = conc[k]; t = tags(r)
    if {"LIVE", "LEGACY_ONLY"} <= t: s = "c"
    elif GUARANTEE.search(r["DeclaredState"] + " " + r["NormativeSource"]): s = "b"
    else: s = "a"
    out.append((k, s))
p = os.path.join(r4lib.R4, "_work", "SUBQ", "P-09_subq.csv")
with open(p, "w", newline="") as f:
    w = csv.writer(f, lineterminator="\n"); w.writerow(["ClaimKey", "SubQ"]); w.writerows(out); f.write("#END\n")
cnt = collections.Counter(s for _, s in out); print(cnt, len(out))
for s in "abc":
    ks = [k for k, x in out if x == s]
    print(s, sorted(collections.Counter(conc[k]["PackageID"] for k in ks).items()))
    print("  ", collections.Counter(conc[k]["Disposition"] for k in ks).most_common())
import random; random.seed(1)
for s in "ab":
    for k in random.sample([k for k, x in out if x == s], 6): print(s, k, conc[k]["DeclaredState"][:110])
