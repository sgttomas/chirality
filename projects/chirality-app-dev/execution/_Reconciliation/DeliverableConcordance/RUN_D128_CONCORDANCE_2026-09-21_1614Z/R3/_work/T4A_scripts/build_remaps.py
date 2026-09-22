"""T4A: build R3/_work/T4A_REMAPS.csv from groups.py output plus hand-decided entries, then
verify that every Find occurs exactly once in its cell when the rows are applied in order."""
import sys, re, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "_scripts"))
sys.path.insert(0, HERE)
import r3lib

groups = json.load(open(sys.argv[1]))
CFG = "R3/_work/T4A_RUNWIDE.md"
EV_A_TEST = "a: {m} exported symbols have no non-test consumer; module LIVE only via contracts/src/index.ts barrel from daemon/src/standalone-bin.ts (symbol scan T4A_scripts/symbol_use.py; RTCONTRACT {cap}); see " + CFG
EV_A_LEG = "a: {m} symbols consumed only by LEGACY_ONLY lib/harness modules; module LIVE only via contracts barrel (symbol scan T4A_scripts/symbol_use.py; RTCONTRACT {cap}); see " + CFG
EV_A_FACADE = "a: frontend/packages/harness-contract facade imported only by src/__tests__/lib/harness-contract-rollback.test.ts; see " + CFG
CAP = {"domain-profile": "CAP-RTCONTRACT-040", "operation-proposal": "CAP-RTCONTRACT-041",
       "engine-conformance": "CAP-RTCONTRACT-039", "tool-catalog": "CAP-RTCONTRACT-043",
       "tool-descriptor": "CAP-RTCONTRACT-042", "mcp/tool-names": "CAP-RTCONTRACT-044", "sdk-version": "CAP-RTCONTRACT-045"}
EV_B = {
    "LIVE_CHAIN": "b1: packaging-chain script (desktop:prepare/pack/dist default path or electron-builder hook, frontend/package.json:39-43,109); see " + CFG,
    "TEST_ONLY": "b3-b5: validation/proof/CI/developer script; no desktop:prepare/pack/dist chain or product entry invokes it; invoked by its own npm entry, a validation wrapper, CI or tests; see " + CFG,
    "LEGACY_ONLY": "b6: script serves only the retained Claude Agent SDK / Pi packaging path (BUILD CAP-BUILD-031..035); see " + CFG,
}

def ev_for(path, call):
    if "harness-contract/src/" in path:
        return EV_A_FACADE
    m = re.search(r"contracts/src/harness/(mcp/tool-names|domain-profile|operation-proposal|engine-conformance|tool-catalog|tool-descriptor|sdk-version)\.ts", path)
    if m:
        mod = m.group(1)
        return (EV_A_TEST if call == "TEST_ONLY" else EV_A_LEG).format(m=mod + ".ts", cap=CAP[mod])
    if call == "LIVE":
        return EV_B["LIVE_CHAIN"]
    return EV_B[call]

remaps = []
for g in groups:
    if g["mixed"]:
        continue
    call = g["calls"][0]
    find = g["text"]
    rep = find[: find.rfind("REACH=")] + "REACH=" + call
    remaps.append({"key": g["key"], "file": g["file"], "find": find, "rep": rep, "call": g["callcls"][0],
                   "ev": ev_for(g["disputed"][0], call)})

C = "CLAIM_CONCORDANCE.csv"; E = "EXTENSION_CONCORDANCE.csv"
TO = "REACH=TEST_ONLY"; LO = "REACH=LEGACY_ONLY"
man = [
    (C, "DEL-06-02#CLM-035.1", "(deprecated re-export facades) REACH=LEGACY_ONLY", "(deprecated re-export facades) " + TO, "a", EV_A_FACADE),
    (C, "DEL-09-01#CLM-013", ":445-450 runs premerge in-process REACH=LIVE", ":445-450 runs premerge in-process " + TO, "b", EV_B["TEST_ONLY"]),
    (C, "DEL-09-05#CLM-020", "(premerge skip with reason) REACH=LIVE", "(premerge skip with reason) " + TO, "b", EV_B["TEST_ONLY"]),
    (C, "DEL-10-03#CLM-010.4", "operation-proposal.ts:19-24 (doc contract), no transition code anywhere;",
        "operation-proposal.ts:19-24 (doc contract) " + TO + ", no transition code anywhere;", "a",
        EV_A_TEST.format(m="operation-proposal.ts", cap=CAP["operation-proposal"]) + " (tag inserted: the group tag LEGACY_ONLY belongs to domain-proposal-tools.ts)"),
    (C, "DEL-10-05#CLM-004.1", "exposedToModel true at :922, projects/", "exposedToModel true at :922 " + LO + "; projects/", "a",
        EV_A_LEG.format(m="tool-descriptor.ts", cap=CAP["tool-descriptor"]) + " (group split: one tag covered three contracts modules)"),
    (C, "DEL-10-05#CLM-004.1", ":109-126 source types REACH=LIVE", ":109-126 source types " + TO, "a",
        EV_A_TEST.format(m="operation-proposal.ts and domain-profile.ts", cap="CAP-RTCONTRACT-040/041")),
    (E, "SOW:SOW-048.2", "tool-catalog.ts and tool-descriptor.ts descriptors REACH=LIVE",
        "tool-catalog.ts " + TO + " and tool-descriptor.ts descriptors " + LO, "a",
        "a: tool-catalog.ts TEST_ONLY (CAP-RTCONTRACT-043) and tool-descriptor.ts LEGACY_ONLY (CAP-RTCONTRACT-042); one shared tag split; see " + CFG),
    (E, "DOC:ADDING_A_TOOL#0", "tool-descriptor.ts:490 HARNESS_TOOL_DESCRIPTORS REACH=LIVE", "tool-descriptor.ts:490 HARNESS_TOOL_DESCRIPTORS " + LO, "a",
        EV_A_LEG.format(m="tool-descriptor.ts", cap=CAP["tool-descriptor"])),
    (E, "DOC:ADDING_A_TOOL#7", "contracts/src/harness/tool-catalog.ts REACH=LIVE", "contracts/src/harness/tool-catalog.ts " + TO, "a",
        EV_A_TEST.format(m="tool-catalog.ts", cap=CAP["tool-catalog"])),
]
# package.json npm entries that name only validation/test scripts (b3)
PKG = [
    ("DEL-09-01#CLM-009.1", "package.json:19 harness:validate:section8, :21 harness:validate:premerge REACH=LIVE"),
    ("DEL-09-01#CLM-013", "package.json:29 validate:release-quality REACH=LIVE"),
    ("DEL-09-02#CLM-005", "package.json:20 harness:validate:section9 REACH=LIVE"),
    ("DEL-09-02#CLM-018", "package.json:20-21,29 commands harness:validate:section9, harness:validate:premerge, validate:release-quality REACH=LIVE"),
    ("DEL-09-03#CLM-003", "package.json:17 (\"test\": \"vitest run\") REACH=LIVE"),
    ("DEL-09-03#CLM-009.12", "package.json:17 test script REACH=LIVE"),
    ("DEL-09-05#CLM-010.8", "package.json:29 validate:release-quality REACH=LIVE"),
    ("DEL-09-06#CLM-010.14", "package.json:29 (validate:release-quality) REACH=LIVE"),
]
for k, f in PKG:
    man.append((C, k, f, f[: f.rfind("REACH=")] + TO, "b",
                "b3: frontend/package.json entry names only a validation/test command (vitest, harness validators, release-quality wrapper); not in desktop:prepare/pack/dist; see " + CFG))
for f, k, fi, rp, c, ev in man:
    remaps.append({"key": k, "file": f, "find": fi, "rep": rp, "call": c, "ev": ev})

# verify by simulated application
cells = {}
for f in (C, E):
    h, rows = r3lib.read_csv(os.path.join(r3lib.R3, f))
    for r in rows:
        cells[r["ClaimKey"]] = r["ImplementationEvidence"]
bad = 0
for m in remaps:
    cell = cells[m["key"]]
    n = cell.count(m["find"])
    if n != 1:
        # extend Find leftwards until unique
        start = -1
        bad += 1
        print("NONUNIQUE", m["key"], n, m["find"][:80])
        continue
    cells[m["key"]] = cell.replace(m["find"], m["rep"], 1)
remaps.sort(key=lambda m: (m["file"], m["key"]))
out = [{"ClaimKey": m["key"], "Field": "ImplementationEvidence", "Find": m["find"], "Replace": m["rep"],
        "Call": m["call"], "Evidence": m["ev"]} for m in remaps]
r3lib.write_csv(os.path.join(r3lib.WORK, "T4A_REMAPS.csv"),
                ["ClaimKey", "Field", "Find", "Replace", "Call", "Evidence"], out)
from collections import Counter
print("rows", len(out), "bad", bad, Counter(o["Call"] for o in out), "keys", len({o["ClaimKey"] for o in out}))
print(Counter((m["find"][m["find"].rfind("REACH="):], m["rep"][m["rep"].rfind("REACH="):]) for m in remaps))
