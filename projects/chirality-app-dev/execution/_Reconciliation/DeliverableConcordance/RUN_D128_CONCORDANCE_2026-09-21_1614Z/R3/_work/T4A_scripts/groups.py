"""T4A: split each ImplementationEvidence cell into REACH tag groups (text up to and including each
REACH=X), classify every source path in a group against the T4A calls (a) and (b), and report
groups whose tag differs from the call. Uniform groups get an automatic Find/Replace candidate;
mixed groups are printed for hand handling. Deterministic; reads the R3 concordance only."""
import sys, re, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "_scripts"))
import r3lib

CONTRACT_CALL = {"domain-profile": "TEST_ONLY", "operation-proposal": "TEST_ONLY",
                 "engine-conformance": "TEST_ONLY", "tool-catalog": "TEST_ONLY",
                 "tool-descriptor": "LEGACY_ONLY", "mcp/tool-names": "LEGACY_ONLY",
                 "sdk-version": "LEGACY_ONLY"}
SCRIPT_CALL = {
    # b1 packaging chain (desktop:prepare/pack/dist default path, electron-builder hooks)
    "build-electron.mjs": "LIVE", "pack-electron.mjs": "LIVE", "prepare-packaged-instruction-root.mjs": "LIVE",
    "verify-instruction-root-integrity.mjs": "LIVE", "verify-codex-pin.mjs": "LIVE",
    "verify-packaged-dependency-boundary.mjs": "LIVE", "finalize-electron-resources.mjs": "LIVE",
    "verify-electron-dist.mjs": "LIVE", "sign-electron-runtime-v2.mjs": "LIVE",
    # b2 release-artifact generators (standalone npm entries)
    "generate-sbom.mjs": "LIVE", "generate-third-party-notices.mjs": "LIVE", "verify-version-identity.mjs": "LIVE",
    # b3/b4/b5 validation, proof, CI and developer tooling
    "assert-harness-contract-deps.mjs": "TEST_ONLY", "validate-release-quality-evidence.mjs": "TEST_ONLY",
    "validate-harness-premerge.mjs": "TEST_ONLY", "validate-harness-section8.mjs": "TEST_ONLY",
    "validate-harness-section9.mjs": "TEST_ONLY", "harness-section9-manifest.json": "TEST_ONLY",
    "scan-secret-evidence.mjs": "TEST_ONLY", "run-network-policy-proof.mjs": "TEST_ONLY",
    "run-packaged-security-proof.mjs": "TEST_ONLY", "controlled-ci-runtime.ts": "TEST_ONLY",
    "build-controlled-ci-runtime.mjs": "TEST_ONLY", "generate-tool-catalog.mjs": "TEST_ONLY",
    "pec-scratch-server.mjs": "TEST_ONLY",
    # b6 legacy-path scripts
    "verify-packaged-agent-sdk-runtime.mjs": "LEGACY_ONLY", "run-live-packaged-agent-sdk-read-tool-proof.mjs": "LEGACY_ONLY",
    "run-packaged-pi-runtime-proof.mjs": "LEGACY_ONLY", "normalize-pi-lock-integrity.mjs": "LEGACY_ONLY",
    "verify-pi-supply-chain.mjs": "LEGACY_ONLY",
    # b7 nothing invokes (Addendum 1 item 4)
    "generate-macos-icon.mjs": "LEGACY_ONLY", "run-pec-bridge-rehearsal.ts": "LEGACY_ONLY",
    "run-dapp52-live-llm-demo.ts": "LEGACY_ONLY", "run-dapp52-live-sdk-probe.mjs": "LEGACY_ONLY",
}
PATH_RE = re.compile(r"(?:[A-Za-z0-9_@.-]+/)*[A-Za-z0-9_@.-]+\.(?:ts|tsx|mjs|js|json|cjs|yml)\b")
REACH_RE = re.compile(r"REACH=(LIVE|LEGACY_ONLY|TEST_ONLY)")
CONTRACT_RE = re.compile(r"(?:packages/contracts/src/harness/|frontend/packages/harness-contract/src/|^|(?<=[\s(]))(mcp/tool-names|domain-profile|operation-proposal|engine-conformance|tool-catalog|tool-descriptor|sdk-version)\.ts$")

def classify(p):
    if ".test." in p or "/__tests__/" in p:
        return None, None
    if "frontend/packages/harness-contract/src/" in p:
        return "a", "TEST_ONLY"
    m = re.search(r"packages/contracts/src/harness/(mcp/tool-names|domain-profile|operation-proposal|engine-conformance|tool-catalog|tool-descriptor|sdk-version)\.ts$", p)
    if m:
        return "a", CONTRACT_CALL[m.group(1)]
    m = re.search(r"(?:^|/)scripts/([A-Za-z0-9_.-]+)$", p)
    if m and ("frontend/scripts/" in p or p.startswith("scripts/")) and m.group(1) in SCRIPT_CALL:
        return "b", SCRIPT_CALL[m.group(1)]
    return None, None

def groups(ev):
    pos = 0
    for rm in REACH_RE.finditer(ev):
        yield pos, rm.start(), rm.end(), rm.group(1)
        pos = rm.end()

out = []
for f in ["CLAIM_CONCORDANCE.csv", "EXTENSION_CONCORDANCE.csv"]:
    h, rows = r3lib.read_csv(os.path.join(r3lib.R3, f))
    for r in rows:
        ev = r["ImplementationEvidence"]
        for gs, ts, te, tag in groups(ev):
            text = ev[gs:ts]
            paths = [(m.start() + gs, m.group(0)) for m in PATH_RE.finditer(text)]
            cls = [(s, p) + classify(p) for s, p in paths]
            disputed = [c for c in cls if c[3]]
            if not disputed:
                continue
            calls = {c[3] for c in disputed}
            if all(c[3] == tag for c in disputed):
                continue
            others = [c for c in cls if not c[3] and ".test." not in c[1]]
            out.append({"file": f, "key": r["ClaimKey"], "tag": tag, "calls": sorted(calls),
                        "callcls": sorted({c[2] for c in disputed}),
                        "mixed": len(calls) > 1 or bool(others), "first": disputed[0][0], "ts": ts, "te": te,
                        "others": [c[1] for c in others], "disputed": [c[1] for c in disputed],
                        "text": ev[disputed[0][0]:te]})
json.dump(out, open(sys.argv[1], "w"), indent=1)
print(len(out), "groups;", sum(o["mixed"] for o in out), "mixed")
