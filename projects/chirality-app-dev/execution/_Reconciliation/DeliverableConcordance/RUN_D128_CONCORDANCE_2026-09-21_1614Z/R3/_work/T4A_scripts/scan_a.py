"""T4A (a): for each disputed contracts module mention in ImplementationEvidence, find the REACH
tag that governs it (the first REACH= after the mention, provided no other source path intervenes)."""
import sys, re, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_scripts"))
import r3lib
MODS = {"domain-profile": "TEST_ONLY", "operation-proposal": "TEST_ONLY",
        "engine-conformance": "TEST_ONLY", "tool-catalog": "TEST_ONLY",
        "tool-descriptor": "LEGACY_ONLY", "mcp/tool-names": "LEGACY_ONLY", "sdk-version": "LEGACY_ONLY"}
MOD_RE = re.compile(r"[A-Za-z0-9_./@-]*(?:contracts|harness-contract)[A-Za-z0-9_./-]*/(domain-profile|operation-proposal|engine-conformance|tool-catalog|tool-descriptor|mcp/tool-names|sdk-version)(?:\.ts)?|@chirality/runtime-contracts/(domain-profile|operation-proposal|engine-conformance|tool-catalog|tool-descriptor|mcp/tool-names|sdk-version)")
PATH_RE = re.compile(r"[A-Za-z0-9_@.-]+(?:/[A-Za-z0-9_.@-]+)+\.(?:ts|tsx|mjs|js|json|cjs)")
REACH_RE = re.compile(r"REACH=(LIVE|LEGACY_ONLY|TEST_ONLY)")
out = []
for f in ["CLAIM_CONCORDANCE.csv", "EXTENSION_CONCORDANCE.csv"]:
    h, rows = r3lib.read_csv(os.path.join(r3lib.R3, f))
    for r in rows:
        ev = r["ImplementationEvidence"]
        for m in MOD_RE.finditer(ev):
            mod = m.group(1) or m.group(2)
            rest = ev[m.end():]
            rm = REACH_RE.search(rest)
            nxt = PATH_RE.search(rest)
            tag = None
            if rm and (not nxt or nxt.start() > rm.start()):
                tag = rm.group(1)
            out.append((f, r["ClaimKey"], mod, tag, ev[m.start():m.end() + (rm.end() if rm else 0)] if tag else ev[m.start():m.end()+80]))
for o in out:
    print("\t".join(str(x) for x in o))
