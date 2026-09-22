"""D3 helper: P-09 mixed-evidence count effect and reach readings. Deterministic."""
import collections, os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_scripts"))
import r4lib
conc = r4lib.load_concordance()
idx = r4lib.read_csv(os.path.join(r4lib.R4, "PACKET_INDEX.csv"))[1]
pk = collections.defaultdict(list)
for r in idx: pk[(r["PacketID"], r["Role"])].append(r["ClaimKey"])
P = pk[("P-09", "PRIMARY")]
def tags(r): return set(re.findall(r"REACH=([A-Z_]+)", r["ImplementationEvidence"]))
def toks(r): return [t.strip() for t in r["HumanDecisionNeeded"].split(";") if t.strip()]
print("P-09 PRIMARY", len(P))
allrows = [k for k, r in conc.items() if "R4-Q1" in toks(r)]
mixed_all = [k for k in allrows if {"LIVE", "LEGACY_ONLY"} <= tags(conc[k])]
print("run-wide rows citing R4-Q1:", len(allrows), "with LIVE+LEGACY:", len(mixed_all))
mixed = [k for k in P if {"LIVE", "LEGACY_ONLY"} <= tags(conc[k])]
print("P-09 PRIMARY mixed:", len(mixed))
# whole-claim reading: drop R4-Q1 on mixed; what HDN remains?
rem = collections.Counter()
for k in mixed:
    t = [x for x in toks(conc[k]) if x != "R4-Q1"]
    rem[";".join(t) or "NO"] += 1
print("remaining HDN after dropping R4-Q1 on mixed:", rem)
print("mixed by disposition:", collections.Counter(conc[k]["Disposition"] for k in mixed))
print("mixed by pkg:", sorted(collections.Counter(conc[k]["PackageID"] for k in mixed).items()))
legonly = [k for k in P if "LEGACY_ONLY" in tags(conc[k]) and "LIVE" not in tags(conc[k])]
print("legacy-only (no LIVE) PRIMARY:", len(legonly), collections.Counter(conc[k]["Disposition"] for k in legonly))
other = [k for k in P if "LEGACY_ONLY" not in tags(conc[k])]
print("no LEGACY tag:", len(other), [(k, conc[k]["HumanDecisionNeeded"]) for k in other])
# reach call (a) effect: rows whose R4-Q1 comes from RUNWIDE (a) retags LIVE->LEGACY
ra = [k for k in P if "RUNWIDE_CALLS.md (a)" in conc[k]["RemapSources"] or "(a)" in conc[k]["RemapSources"]]
print("P-09 rows with any RemapSources mention (a):", len(ra))
print("RemapSources sample:", collections.Counter(s.strip() for k in P for s in conc[k]["RemapSources"].split(";")).most_common(12))
held = [k for k in P if re.search(r"D-APP-11[6-9]", conc[k]["HumanDecisionNeeded"])]
print("held D-APP-116..119:", len(held), held)
also = pk[("P-09", "ALSO")] + pk[("P-09", "CONTEXT")]
print("ALSO", len(also))
# ClaimType x mixed
print("ClaimType all:", collections.Counter(conc[k]["ClaimType"] for k in P))
# subject: area grouping by package
print("CauseTag mixed:", collections.Counter(conc[k]["CauseTag"] for k in mixed))
