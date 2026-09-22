"""T2 (R3): R4-Q1 verdicts on rows the REACH-tag script cannot decide.

Verdicts are agent judgments recorded in DECISIONS below (evidence read from the frozen tree,
REACHABILITY.csv and the row). This script only checks and writes them: every TagFix Find must
occur exactly once in the current ImplementationEvidence cell, and every module path a TagFix
adds must be LEGACY_ONLY in REACHABILITY.csv or carry a symbol-level basis in the row set.
"""
import collections, csv, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "_scripts"))
import r3lib  # noqa: E402

H = "projects/chirality-app-dev/frontend/src/lib/harness/"
OVERLAY = H + "permission-overlay.ts"
HOOKS = H + "chirality-hooks.ts"
MAPPER = H + "sdk-message-mapper.ts"
EVENTS = H + "session-events.ts"
ARTIFACTS = H + "tool-result-artifacts.ts"
EVIDENCE = H + "tool-evidence.ts"
POOL = H + "tool-pool.ts"
TURN = H + "turn-engine.ts"
BUILDER = H + "sdk-options-builder.ts"
READTOOLS = H + "mcp/read-tools.ts"
ANTHROPIC = H + "anthropic-agent-sdk-manager.ts"
GOV = H + "subagent-governance.ts"
OPTIONS = H + "options.ts"
SESSMGR = H + "session-manager.ts"  # module LIVE; FileSessionManager symbol LEGACY_ONLY (DEL-05-01#CLM-010.4)
SYMBOL_LEVEL = {SESSMGR}

L = "REACH=LEGACY_ONLY"


def ex(*mods):
    return " exercising " + " and ".join(mods) + " " + L


D = {}


def add(key, verdict, basis, tagfix=None, also=""):
    D[key] = dict(Verdict=verdict, Basis=basis, TagFix=tagfix, AlsoModule=also)


# ---- KEEP? rows -------------------------------------------------------------------------------
add("DEL-01-02#CLM-016", "DROP",
    "The only code cited is LIVE codex-supervisor.ts:104-110,219, and the stated gap (Codex mechanisms not mapped in the register) holds whatever R4-Q1 decides; the row gives no R4-Q1 reason.")
add("DEL-01-02#CLM-018.24", "KEEP_OTHER",
    "RemainingWork: 'currency is not (core rows cite legacy surfaces ...)'; whether register rows citing the retained harness are current turns on R4-Q1.")
add("DEL-01-02#CLM-020", "KEEP_OTHER",
    "RemainingWork: 'exclusion evidence rests on legacy surfaces'; whether that evidence still counts turns on R4-Q1.")
add("DEL-03-02#CLM-004", "KEEP_OTHER",
    "Notes: 'The settingSources [] condition restates SPEC §12.2 for the retired Claude SDK path ..., which turns on R4-Q1'; RemainingWork 'settingSources condition per the R4-Q1 outcome'.")
add("DEL-04-01#CLM-021.2", "KEEP_RULE3",
    "IE 'as CLM-014.2' imports DEL-04-01#CLM-014.2's evidence, whose only code is sdk-message-mapper.ts:633 mapSdkMessageToHarness REACH=LEGACY_ONLY; the tag is missing here.",
    ("documentary claim: as CLM-014.2;",
     "documentary claim: as CLM-014.2 (" + MAPPER + ":633 mapSdkMessageToHarness " + L + ");"))
add("DEL-04-02#STATE-1", "DROP",
    "Evidence is LIVE only (codex-supervisor.ts:219, codex-effective-home.ts:5-12); the retained Claude path does not meet 'first concrete/current path', and the row states no R4-Q1 reason (its authority question is the R3_RUNWIDE(d) R4-Q6 cluster).")
add("DEL-04-04#CLM-024", "UNDECIDED",
    "Reading 1 KEEP_RULE3: RemainingWork 'principles 1 and 3 name SDK mechanisms', which only the LEGACY_ONLY Claude builder provides (no legacy path cited, so no TagFix). Reading 2 DROP: Notes 'Principles 2, 3, 5 hold on the live path in substance' via LIVE runtime-method-service.ts, so LIVE code meets the claim.")
add("DEL-04-05#CLM-004", "KEEP_RULE3",
    "Sealed IE cited sdk-options-builder.ts:30-33,248 REACH=LEGACY_ONLY (settingSources parsed to []); the PKG-04 CORRECTION replaced the whole cell and dropped it while stating 'R4-Q1; R4-Q2 hold'.",
    ("projects/chirality-runtime/packages/daemon/src/app-owned-composition.ts:214 REACH=LIVE (Codex engine registered as the only engine);",
     BUILDER + ":30-33,248 settingSources " + L + "; projects/chirality-runtime/packages/daemon/src/app-owned-composition.ts:214 REACH=LIVE (Codex engine registered as the only engine);"),
    "ALSO_MODULE:STALE_SPECIFICATION")
add("DEL-04-05#CLM-009.3", "KEEP_OTHER",
    "RemainingWork: 'Decide whether the retained safeStorage store is history or obligation'; the errata re-tag of SafeStorageCredentialStore to TEST_ONLY (instantiated only in tests) stands.")
add("DEL-04-05#CLM-009.16", "KEEP_RULE3",
    "Notes: 'whether tests of the retained legacy module remain an obligation is R4-Q1'; the cited manager test exercises anthropic-agent-sdk-manager.ts, LEGACY_ONLY in REACHABILITY.csv, untagged here.",
    ("harness-anthropic-agent-sdk-manager.test.ts REACH=TEST_ONLY;",
     "harness-anthropic-agent-sdk-manager.test.ts REACH=TEST_ONLY" + ex(ANTHROPIC) + ";"))
add("DEL-04-05#CLM-011", "KEEP_RULE3",
    "Notes: 'Verification rows exist for the legacy module'; the cited manager test exercises anthropic-agent-sdk-manager.ts (LEGACY_ONLY in REACHABILITY.csv), untagged here.",
    ("harness-anthropic-agent-sdk-manager.test.ts REACH=TEST_ONLY;",
     "harness-anthropic-agent-sdk-manager.test.ts REACH=TEST_ONLY" + ex(ANTHROPIC) + ";"))
add("DEL-04-05#CLM-012", "KEEP_RULE3",
    "Sealed IE cited anthropic-agent-sdk-manager.ts REACH=LEGACY_ONLY as the key-handoff artifact; the PKG-04 CORRECTION replaced the cell and dropped it while stating the Disposition holds.",
    ("projects/chirality-app-dev/frontend/electron/api-key-storage.ts:45 isProviderCredentialId REACH=LIVE;",
     ANTHROPIC + " " + L + "; projects/chirality-app-dev/frontend/electron/api-key-storage.ts:45 isProviderCredentialId REACH=LIVE;"))
add("DEL-04-05#CLM-019", "KEEP_RULE3",
    "SEE:DEL-04-05#CLM-011 (same verification statements); the cited manager test exercises LEGACY_ONLY anthropic-agent-sdk-manager.ts, untagged here.",
    ("harness-anthropic-agent-sdk-manager.test.ts REACH=TEST_ONLY;",
     "harness-anthropic-agent-sdk-manager.test.ts REACH=TEST_ONLY" + ex(ANTHROPIC) + ";"))
add("DEL-04-05#CLM-022.1", "KEEP_RULE3",
    "RemainingWork 'As DEL-04-05#CLM-014', whose only non-test code is anthropic-agent-sdk-manager.ts:181-271,530-556 REACH=LEGACY_ONLY; the cited test exercises it, untagged here.",
    ("harness-anthropic-agent-sdk-manager.test.ts REACH=TEST_ONLY;",
     "harness-anthropic-agent-sdk-manager.test.ts REACH=TEST_ONLY" + ex(ANTHROPIC + ":181-271,530-556") + ";"))
add("DEL-04-05#CLM-024", "UNDECIDED",
    "Reading 1 KEEP_OTHER: whether the retained Claude SDK substrate is history or obligation is R4-Q1. Reading 2 DROP: the row turns on the unamended App DIRECTIVE 2.8 default-provider clause ('Owner ruling on the unamended App DIRECTIVE 2.8'), which is R4-Q6 scope (Addendum 9); dropping R4-Q1 alone would leave AUTHORITY_CONFLICT with NO, so the HDN is left unchanged.")
add("DEL-04-05#STATE-3", "KEEP_OTHER",
    "RemainingWork: 'Decide whether the retained Anthropic credential store and its IPC channels are removed or rewired'; the errata TEST_ONLY tag on SafeStorageCredentialStore stands.")
add("DEL-05-01#CLM-016", "KEEP_RULE3",
    "Notes: 'the project-local behaviour is met only by LEGACY_ONLY code'; that code is FileSessionManager (session-manager.ts:153-155,632-802), LEGACY_ONLY at symbol level as tagged on DEL-05-01#CLM-010.4, untagged here.",
    ("projects/chirality-runtime/packages/core/src/session-store.ts:112-119, :160-178 REACH=LIVE",
     "projects/chirality-runtime/packages/core/src/session-store.ts:112-119, :160-178 REACH=LIVE; " + SESSMGR + ":153-155 and :632-802 (FileSessionManager, constructed only by LEGACY_ONLY runtime.ts:158) " + L))
add("DEL-05-01#CLM-024", "KEEP_RULE3",
    "Notes: 'the project-local behaviour is met only by LEGACY_ONLY code'; FileSessionManager (session-manager.ts:632-802) performs the eager flat-record materialization principle 2 requires, LEGACY_ONLY at symbol level (DEL-05-01#CLM-010.4), untagged here.",
    ("(lazy, not eager) REACH=LIVE",
     "(lazy, not eager) REACH=LIVE; " + SESSMGR + ":632-802 (FileSessionManager eager materialization, constructed only by LEGACY_ONLY runtime.ts:158) " + L))
add("DEL-05-05#CLM-003", "KEEP_RULE3",
    "Sealed and errata IE cited tool-result-artifacts.ts:58-139 persistToolResultArtifact REACH=LEGACY_ONLY; the PKG-05 CORRECTION replaced the whole cell with prose and dropped every path while stating 'R4-Q1 and ALSO_MODULE hold'.",
    ("Facade REACH=TEST_ONLY (sole importer is the rollback test; corrected by errata).",
     "Facade REACH=TEST_ONLY (sole importer is the rollback test; corrected by errata); " + ARTIFACTS + ":58-139 persistToolResultArtifact (artifacts/tools/<toolUseId>-<tool>.json; sha256; retentionPolicy) " + L + "."))
add("DEL-05-05#CLM-012.1", "KEEP_RULE3",
    "IE says the tests run 'over LEGACY_ONLY modules' without a REACH tag; the tests import tool-result-artifacts.ts and session-events.ts, both LEGACY_ONLY in REACHABILITY.csv.",
    ("REACH=TEST_ONLY over LEGACY_ONLY modules", "REACH=TEST_ONLY over " + ARTIFACTS + " and " + EVENTS + " " + L))
add("DEL-05-05#CLM-012.2", "KEEP_RULE3",
    "IE says the tests run 'over LEGACY_ONLY modules' without a REACH tag; the tests import tool-result-artifacts.ts and tool-evidence.ts, both LEGACY_ONLY in REACHABILITY.csv.",
    ("REACH=TEST_ONLY over LEGACY_ONLY modules", "REACH=TEST_ONLY over " + ARTIFACTS + " and " + EVIDENCE + " " + L))
add("DEL-05-05#CLM-012.4", "KEEP_RULE3",
    "IE 'REACH=TEST_ONLY over LEGACY_ONLY session-events.ts' names the legacy module without its own tag; Notes 'Secret redaction of persisted events is tested only on the legacy path'.",
    ("REACH=TEST_ONLY over LEGACY_ONLY session-events.ts", "REACH=TEST_ONLY over " + EVENTS + " " + L))
add("DEL-05-05#CLM-020.2", "KEEP_RULE3",
    "IE says the three tests run 'over LEGACY_ONLY modules' without a REACH tag; they import tool-result-artifacts.ts, session-events.ts and tool-evidence.ts, all LEGACY_ONLY in REACHABILITY.csv.",
    ("REACH=TEST_ONLY over LEGACY_ONLY modules", "REACH=TEST_ONLY over " + ARTIFACTS + ", " + EVENTS + " and " + EVIDENCE + " " + L))
add("DEL-05-05#CLM-022", "KEEP_RULE3",
    "Notes carry ALSO_MODULE:ALIGNED: the artifact and preview policy is met only by the legacy tool-result-artifacts.ts:58-139 store cited on DEL-05-05#CLM-003 (LEGACY_ONLY), which this IE omits.",
    ("projects/chirality-app-dev/frontend/electron/runtime-service-host.ts:75 runtimeDirectory = <userData>/runtime REACH=LIVE",
     "projects/chirality-app-dev/frontend/electron/runtime-service-host.ts:75 runtimeDirectory = <userData>/runtime REACH=LIVE; " + ARTIFACTS + ":58-139 persistToolResultArtifact (artifact store and budget, as DEL-05-05#CLM-003) " + L))
add("DEL-06-01#CLM-009.14", "KEEP_RULE3",
    "IE names 'legacy dontAsk/readOnly/ask and callback tests'; they import permission-overlay.ts (LEGACY_ONLY), the only code with per-mode behaviour; the live test covers approval routing only.",
    ("legacy dontAsk/readOnly/ask and callback tests REACH=TEST_ONLY",
     "legacy dontAsk/readOnly/ask and callback tests REACH=TEST_ONLY" + ex(OVERLAY)))
add("DEL-06-01#CLM-011", "KEEP_RULE3",
    "IE names 'legacy overlay tests'; Notes 'Approaches are satisfied for the retained overlay module but not on the live Codex path'; permission-overlay.ts is LEGACY_ONLY.",
    ("callback denials REACH=TEST_ONLY", "callback denials REACH=TEST_ONLY" + ex(OVERLAY)))
add("DEL-06-01#CLM-015.2", "KEEP_RULE3",
    "IE names the 'legacy overlay test suite'; RemainingWork 'canUseTool and dontAsk evidence exists only for the retained overlay' (permission-overlay.ts, LEGACY_ONLY).",
    ("legacy overlay test suite REACH=TEST_ONLY", "legacy overlay test suite REACH=TEST_ONLY" + ex(OVERLAY)))
add("DEL-06-01#CLM-020", "KEEP_RULE3",
    "SEE:DEL-06-01#CLM-011; IE names 'legacy overlay tests' of permission-overlay.ts (LEGACY_ONLY), untagged.",
    ("legacy overlay tests REACH=TEST_ONLY", "legacy overlay tests REACH=TEST_ONLY" + ex(OVERLAY)))
add("DEL-06-02#CLM-010.13", "KEEP_RULE3",
    "Notes: 'tests exist for the legacy pool'; the cited tests import tool-pool.ts and turn-engine.ts, both LEGACY_ONLY; no test covers the live tool surface.",
    ("projects/chirality-app-dev/frontend/src/__tests__/lib/turn-engine.test.ts:275-292 REACH=TEST_ONLY",
     "projects/chirality-app-dev/frontend/src/__tests__/lib/turn-engine.test.ts:275-292 REACH=TEST_ONLY; tested modules " + POOL + " and " + TURN + " " + L))
add("DEL-06-02#CLM-012", "KEEP_RULE3",
    "Notes: 'Legacy tests cover unknown names, implementation-vs-exposure, read-first, allowedTools and filtering'; the tests import tool-pool.ts, sdk-options-builder.ts and turn-engine.ts, all LEGACY_ONLY.",
    ("projects/chirality-app-dev/frontend/src/__tests__/lib/turn-engine.test.ts:275-292 REACH=TEST_ONLY",
     "projects/chirality-app-dev/frontend/src/__tests__/lib/turn-engine.test.ts:275-292 REACH=TEST_ONLY; tested modules " + POOL + ", " + BUILDER + " and " + TURN + " " + L))
add("DEL-06-02#CLM-020", "KEEP_RULE3",
    "SEE:DEL-06-02#CLM-012; the cited tests import tool-pool.ts and sdk-options-builder.ts, both LEGACY_ONLY, untagged here.",
    ("projects/chirality-app-dev/frontend/src/__tests__/lib/sdk-options-builder.test.ts:162-575 REACH=TEST_ONLY",
     "projects/chirality-app-dev/frontend/src/__tests__/lib/sdk-options-builder.test.ts:162-575 REACH=TEST_ONLY; tested modules " + POOL + " and " + BUILDER + " " + L))
add("DEL-06-02#CLM-021.2", "KEEP_RULE3",
    "The name/ordering/exposure tests import tool-pool.ts (LEGACY_ONLY); the LIVE runtime-service.ts:559-584 fingerprint 'lacks tool/MCP identifiers to inspect', so it does not meet the claim.",
    ("projects/chirality-app-dev/frontend/src/__tests__/lib/tool-descriptor.test.ts:376-409,552-620 REACH=TEST_ONLY;",
     "projects/chirality-app-dev/frontend/src/__tests__/lib/tool-descriptor.test.ts:376-409,552-620 REACH=TEST_ONLY" + ex(POOL) + ";"))
add("DEL-06-04#CLM-009.15", "KEEP_RULE3",
    "IE 'REACH=TEST_ONLY exercising LEGACY_ONLY modules' names no module tag; the three tests import chirality-hooks.ts, permission-overlay.ts and mcp/read-tools.ts, all LEGACY_ONLY.",
    ("REACH=TEST_ONLY exercising LEGACY_ONLY modules",
     "REACH=TEST_ONLY exercising " + HOOKS + ", " + OVERLAY + " and " + READTOOLS + " " + L))
add("DEL-06-04#CLM-011", "KEEP_RULE3",
    "Notes: approaches 'have in-process tests'; four of the five cited tests import chirality-hooks.ts, permission-overlay.ts, sdk-options-builder.ts and mcp/read-tools.ts (LEGACY_ONLY); atomic-write.ts is LIVE but covers only the exact-edit write helper.",
    ("atomic-write.test.ts REACH=TEST_ONLY",
     "atomic-write.test.ts REACH=TEST_ONLY (the first four exercise " + HOOKS + ", " + OVERLAY + ", " + BUILDER + " and " + READTOOLS + " " + L + ")"))
add("DEL-06-04#CLM-019.1", "KEEP_RULE3",
    "IE 'REACH=TEST_ONLY exercising LEGACY_ONLY modules' names no module tag; the tests import chirality-hooks.ts, permission-overlay.ts, mcp/read-tools.ts and sdk-options-builder.ts, all LEGACY_ONLY.",
    ("REACH=TEST_ONLY exercising LEGACY_ONLY modules",
     "REACH=TEST_ONLY exercising " + HOOKS + ", " + OVERLAY + ", " + READTOOLS + " and " + BUILDER + " " + L))
add("DEL-06-05#CLM-009.11", "DROP",
    "LIVE delegated-engine-adapter.ts:268-298 and codex-supervisor.ts:700-705 meet permission/start/terminal/interruption; the timeout gap is a live-path gap, and the row states no R4-Q1 reason.")
add("DEL-06-05#CLM-009.15", "KEEP_RULE3",
    "Notes: 'Legacy tests cover the list except the 600000 ms maximum'; the cited tests import permission-overlay.ts, chirality-hooks.ts and sdk-message-mapper.ts, all LEGACY_ONLY.",
    ("projects/chirality-app-dev/frontend/src/__tests__/lib/sdk-message-mapper.test.ts:441 REACH=TEST_ONLY",
     "projects/chirality-app-dev/frontend/src/__tests__/lib/sdk-message-mapper.test.ts:441 REACH=TEST_ONLY; tested modules " + OVERLAY + ", " + HOOKS + " and " + MAPPER + " " + L))
add("DEL-06-05#CLM-011", "KEEP_RULE3",
    "Notes: 'Legacy tests realise most approaches'; the cited tests import permission-overlay.ts, chirality-hooks.ts and sdk-message-mapper.ts, all LEGACY_ONLY.",
    ("projects/chirality-app-dev/frontend/src/__tests__/lib/sdk-message-mapper.test.ts:441 REACH=TEST_ONLY",
     "projects/chirality-app-dev/frontend/src/__tests__/lib/sdk-message-mapper.test.ts:441 REACH=TEST_ONLY; tested modules " + OVERLAY + ", " + HOOKS + " and " + MAPPER + " " + L))
add("DEL-06-05#CLM-019.2", "DROP",
    "No code evidence (documentary claim: Assessment_INSP-03_DEL-06-05.md); the defect is the overtaken INSP-03 matrix, and the row states no R4-Q1 reason.")
add("DEL-06-05#CLM-030", "KEEP_OTHER",
    "RemainingWork: 'Record the K-BASH-1/K-PERM/K-HOOK vs D-GOV-43 conflict'; the unamended K-HOOK/K-PERM clauses on retained code are the R4-Q1 subject (CONVENTIONS §2.4).")
add("DEL-06-06#CLM-010.13", "KEEP_RULE3",
    "Notes: 'compaction coverage exists only for the legacy mapper'; the cited test imports sdk-message-mapper.ts (LEGACY_ONLY), untagged here.",
    ("projects/chirality-app-dev/frontend/src/__tests__/lib/sdk-message-mapper.test.ts:750 REACH=TEST_ONLY;",
     "projects/chirality-app-dev/frontend/src/__tests__/lib/sdk-message-mapper.test.ts:750 REACH=TEST_ONLY" + ex(MAPPER) + ";"))
add("DEL-06-06#CLM-012", "KEEP_RULE3",
    "IE 'REACH=TEST_ONLY (exercise LEGACY_ONLY modules)' names no module tag; the four tests import sdk-message-mapper.ts, chirality-hooks.ts, session-events.ts and tool-result-artifacts.ts, all LEGACY_ONLY.",
    ("REACH=TEST_ONLY (exercise LEGACY_ONLY modules)",
     "REACH=TEST_ONLY (exercise " + MAPPER + ", " + HOOKS + ", " + EVENTS + " and " + ARTIFACTS + " " + L + ")"))
add("DEL-06-06#CLM-020", "KEEP_RULE3",
    "RemainingWork 'Same residuals as CLM-015.1', whose IE records the hook, compaction and redaction checks only in 'cited modules REACH=LEGACY_ONLY' (the legacy mapper, hooks and event writer named in DEL-06-06#CLM-018).",
    ("projects/chirality-runtime/packages/core/src/session-store.ts:813-823 REACH=LIVE",
     "projects/chirality-runtime/packages/core/src/session-store.ts:813-823 REACH=LIVE; hook start, compaction and redaction only in " + MAPPER + ", " + HOOKS + " and " + EVENTS + " " + L + " (as DEL-06-06#CLM-015.1)"))
add("DEL-06-06#CLM-022.1", "KEEP_RULE3",
    "IE 'cited tests ... REACH=TEST_ONLY target LEGACY_ONLY modules' names no module tag; the VER-001 tests target sdk-message-mapper.ts, chirality-hooks.ts, session-events.ts and tool-result-artifacts.ts (LEGACY_ONLY).",
    ("REACH=TEST_ONLY target LEGACY_ONLY modules",
     "REACH=TEST_ONLY target " + MAPPER + ", " + HOOKS + ", " + EVENTS + " and " + ARTIFACTS + " " + L))
add("DEL-06-06#CLM-032", "KEEP_OTHER",
    "RemainingWork: 'Record the D-GOV-43 vs SPEC 15.2/K-HOOK-1/TYPES 8.5 conflict'; SPEC §15.2 and K-HOOK unamended for D-GOV-43 are the named R4-Q1 subject (CONVENTIONS §2.4).")
add("DEL-06-06#STATE-1", "DROP",
    "Evidence is documentary plus LIVE codex-supervisor.ts/delegated-engine-adapter.ts; the row concerns the retired daemon and the unamended SCA-APP-001 text, covered by R4 and R4-Q6, and states no R4-Q1 reason.")
add("DEL-07-01#CLM-011.10", "KEEP_RULE3",
    "Notes: 'Outside-project, IR-write and symlink cases exist only as tests of LEGACY_ONLY code'; the cited hooks test imports chirality-hooks.ts (LEGACY_ONLY), untagged.",
    ("projects/chirality-app-dev/frontend/src/__tests__/lib/chirality-hooks.test.ts REACH=TEST_ONLY",
     "projects/chirality-app-dev/frontend/src/__tests__/lib/chirality-hooks.test.ts REACH=TEST_ONLY" + ex(HOOKS)))
add("DEL-07-01#CLM-013", "KEEP_RULE3",
    "Notes: 'containment, IR-write and symlink tests exercise LEGACY_ONLY code'; chirality-hooks.ts is LEGACY_ONLY (instruction-root.ts, tested by harness-instruction-root.test.ts, is LIVE and covers root validation only).",
    ("projects/chirality-app-dev/frontend/src/__tests__/lib/chirality-hooks.test.ts REACH=TEST_ONLY",
     "projects/chirality-app-dev/frontend/src/__tests__/lib/chirality-hooks.test.ts REACH=TEST_ONLY" + ex(HOOKS)))
add("DEL-07-01#CLM-020", "KEEP_RULE3",
    "SEE:DEL-07-01#CLM-013; the hooks test exercises LEGACY_ONLY chirality-hooks.ts, untagged here.",
    ("projects/chirality-app-dev/frontend/src/__tests__/lib/chirality-hooks.test.ts REACH=TEST_ONLY",
     "projects/chirality-app-dev/frontend/src/__tests__/lib/chirality-hooks.test.ts REACH=TEST_ONLY" + ex(HOOKS)))
add("DEL-07-01#CLM-022", "KEEP_RULE3",
    "Notes: 'path-policy, symlink and hook-denial families exercise LEGACY_ONLY code'; the hooks test imports chirality-hooks.ts (LEGACY_ONLY), untagged.",
    ("projects/chirality-app-dev/frontend/src/__tests__/lib/chirality-hooks.test.ts REACH=TEST_ONLY",
     "projects/chirality-app-dev/frontend/src/__tests__/lib/chirality-hooks.test.ts REACH=TEST_ONLY" + ex(HOOKS)))
add("DEL-07-04#CLM-011.15", "KEEP_RULE3",
    "Notes: 'MCP-routing coverage exists only for LEGACY_ONLY code'; chirality-mutating-mcp.test.ts imports mcp/read-tools.ts (status_transition at :934), LEGACY_ONLY, untagged.",
    ("frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts REACH=TEST_ONLY",
     "frontend/src/__tests__/lib/chirality-mutating-mcp.test.ts REACH=TEST_ONLY" + ex(READTOOLS + ":934 status_transition")))
add("DEL-07-04#CLM-013.12", "KEEP_RULE3",
    "Notes: 'R4-Q1 for the policy-denial reason met only by LEGACY_ONLY code'; the policy-denial path is the legacy MCP status_transition tool (mcp/read-tools.ts:934, LEGACY_ONLY), not cited in IE.",
    ("frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts REACH=TEST_ONLY",
     "frontend/src/__tests__/api/working-root/deliverable-contracts.test.ts REACH=TEST_ONLY; policy/path denial only via " + READTOOLS + ":934 status_transition " + L))
add("DEL-07-04#STATE-1", "KEEP_OTHER",
    "RemainingWork lists 'live-path status tool per R4-Q1' among the warranted open items the empty Remaining omits.")
add("DEL-07-05#CLM-014", "KEEP_RULE3",
    "IE: MCP tests 'cover MCP deps tools of the legacy module'; Notes 'exists only against the LEGACY_ONLY module (R4-Q1)'; the module is mcp/read-tools.ts (deps_read :728, deps_write :976), untagged.",
    ("cover MCP deps tools of the legacy module REACH=TEST_ONLY",
     "cover MCP deps tools of the legacy module REACH=TEST_ONLY (module " + READTOOLS + " " + L + ")"))
add("DEL-07-05#CLM-024.2", "KEEP_RULE3",
    "IE: '(MCP deps tools on the legacy module)'; Notes 'MCP and hook verification met only by tests of LEGACY_ONLY code (R4-Q1)'; the module is mcp/read-tools.ts, untagged.",
    ("(MCP deps tools on the legacy module) REACH=TEST_ONLY",
     "(MCP deps tools on the legacy module) REACH=TEST_ONLY (module " + READTOOLS + " " + L + ")"))
add("DEL-07-05#STATE-1", "KEEP_OTHER",
    "Notes: 'Whether those requirements are history or obligation is R4-Q1' (the SoW's Claude-SDK MCP/hook model versus runtime-service.ts:580 mcpServers: [] on the live path).")
add("DEL-08-03#CLM-015", "KEEP_RULE3",
    "Notes 'REQ-011 proof on legacy path'; DEL-08-03#CLM-013.11 (REQ-011) tags that proof options.ts:19 and subagent-governance.ts REACH=LEGACY_ONLY, which this IE omits.",
    ("projects/chirality-app-dev/frontend/src/__tests__/lib/pkg08-compatibility-boundaries.test.ts REACH=TEST_ONLY",
     "projects/chirality-app-dev/frontend/src/__tests__/lib/pkg08-compatibility-boundaries.test.ts REACH=TEST_ONLY; REQ-011 evidence " + OPTIONS + ":19 and " + GOV + " " + L + " (as DEL-08-03#CLM-013.11)"))
add("DEL-08-03#CLM-019.1", "KEEP_RULE3",
    "RemainingWork 'governance-guard evidence not on the live Codex path'; the guard evidence is the REQ-011 proof that DEL-08-03#CLM-013.11 tags options.ts:19 and subagent-governance.ts REACH=LEGACY_ONLY.",
    ("`void legacy` REACH=LIVE)",
     "`void legacy` REACH=LIVE); governance-guard evidence " + OPTIONS + ":19 and " + GOV + " " + L + " (as DEL-08-03#CLM-013.11)"))
add("DEL-10-02#CLM-010.11", "KEEP_OTHER",
    "Notes: 'K-PERM-2 ... is present-tense and names legacy enforcement (overlay, hooks); ordinary agent tools on the Codex path are Codex-native tools'; whether that legacy enforcement is an obligation is R4-Q1.")

# ---- ADD? rows --------------------------------------------------------------------------------
NA = "NO_ADD"
add("DEL-01-02#REM-1", NA, "The open item (PEC v2 client seam) is not met by legacy pec-bridge-client.ts, which the row cites as the retired seam, not as meeting the item.")
add("DEL-01-04#CLM-006.6", NA, "EXCLUSION: legacy pi-agent-engine-adapter.ts contradicts 'no adapter, import ... authorized'; it does not meet it.")
add("DEL-01-04#STATE-1", NA, "Legacy pi-agent-engine-adapter.ts contradicts 'register must prohibit a Pi adapter'; it does not meet the claim.")
add("DEL-03-04#STATE-3", "ADD",
    "'disconnect recorded as turn.cancelled' is met only by LEGACY_ONLY turn-engine.ts:314-338 (writes turn.cancelled); the drain-proof test file is absent.",
    also="ALSO_MODULE:STALE_SPECIFICATION")
add("DEL-04-02#CLM-010.12", "ADD",
    "REQ-012 concerns the SDK option property names; the only code carrying them is LEGACY_ONLY sdk-options-builder.ts:1,26-28 (typed Options/SettingSource against the pinned SDK).")
add("DEL-04-02#CLM-013", NA, "STATE_ASSERTION of open TBDs; legacy sdk-options-builder.ts and turn-engine.ts are cited to show the TBDs are closed, not as meeting the claim.")
add("DEL-04-02#CLM-017", NA, "STATE_ASSERTION of prerequisite statuses; legacy sdk-options-builder.ts:1 shows the path TBD is false, not that the claim is met.")
add("DEL-04-02#CLM-020", NA, "STATE_ASSERTION that records are TBD; legacy sdk-options-builder.ts:125 refutes it.")
add("DEL-04-02#CLM-025", "ADD",
    "Notes: the other guidance rows (pure fallback, settings posture, registry, resume, subagent fail-closed) 'hold at module level', met only by LEGACY_ONLY sdk-options-builder.ts:152-162,247.",
    also="ALSO_MODULE:STALE_SPECIFICATION")
add("DEL-04-03#CLM-003", "ADD",
    "The fixed seven-name UIEvent browser output (session:init, chat:delta, chat:complete, session:complete, process:exit, tool:result) is produced only by LEGACY_ONLY sdk-message-mapper.ts:648-855.",
    also="ALSO_MODULE:STALE_SPECIFICATION")
add("DEL-04-03#CLM-011", NA, "STATE_ASSERTION that verification items are 'TBD implementation'; the legacy mapper and its tests refute the status, they do not meet it.")
add("DEL-04-03#CLM-016", NA, "STATE_ASSERTION of TBD prerequisites; the legacy mapper path refutes 'mapper path TBD'.")
add("DEL-04-05#CLM-009.14", "ADD",
    "Adapter-metadata failure details (provider, category, upstreamType inside HarnessError) exist only in LEGACY_ONLY anthropic-agent-sdk-manager.ts:517-526; the live path forwards Codex-shaped notifications.",
    also="ALSO_MODULE:ALIGNED")
add("DEL-05-02#REM-2", NA, "proposal.* consumption is NONE_FOUND; legacy session-events.ts/event-factory.ts are the named write locus, not code meeting the item.")
add("DEL-05-02#REGISTER-3", NA, "REGISTER_DEFECT about retired gates; legacy sdk-message-mapper.ts is only the target of DEP-05-02-012, not code meeting the register claim.")
add("DEL-06-01#CLM-015.1", "ADD",
    "The 'other modes hard-deny through evaluateSubagentPreflight' part is met only by LEGACY_ONLY subagent-bridge.ts:92-117 and permission-overlay.ts:195-221 (which also deny workspaceWrite).",
    also="ALSO_MODULE:STALE_SPECIFICATION")
add("DEL-06-01#CLM-018", NA, "STATE_ASSERTION of TBD paths and PRD MATCH; legacy permission-overlay.ts refutes the TBD.")
add("DEL-06-01#CLM-034.1", "ADD",
    "The v7 coordination-mode policy the row assigns is implemented only in LEGACY_ONLY permission-overlay.ts:12,223-245 and tool-descriptor.ts:35,156 (call a LEGACY_ONLY); the facade is TEST_ONLY.")
add("DEL-06-02#CLM-005", "ADD",
    "The resolver construction (validate, order, filter read-first, hand off to overlay) is met in part only by LEGACY_ONLY tool-pool.ts:36-111, turn-engine.ts:137-153 and sdk-options-builder.ts:147-210; owner-deferred (Addendum 5) Disposition untouched, worker B already cites R4-Q1.")
add("DEL-06-02#CLM-006", NA, "STATE_ASSERTION that paths are TBD; the LEGACY_ONLY registry, pool and fingerprint refute it.")
add("DEL-06-02#CLM-013", NA, "STATE_ASSERTION that paths remain TBD; the LEGACY_ONLY registry and pool refute it.")
add("DEL-06-02#CLM-014", "ADD",
    "REQUIREMENT: of the required evidence, 'Resolver, registry and structured error contract exist' (Notes) only as LEGACY_ONLY tool-descriptor.ts:107-119 and tool-pool.ts:36-111.")
add("DEL-06-02#CLM-021.1", NA, "STATE_ASSERTION that record paths are TBD; the LEGACY_ONLY registry and pool refute it.")
add("DEL-06-02#CLM-026", "ADD",
    "The resolver shape (explicit registry, structured UNKNOWN_TOOL error, SDK names as adapter.claudeAgentSdk metadata) is met in part only by LEGACY_ONLY tool-descriptor.ts:84-119,1296-1401 and tool-pool.ts.")
add("DEL-06-04#CLM-016", NA, "STATE_ASSERTION of TBD prerequisites; legacy tool-path-policy.ts and chirality-hooks.ts refute the path TBD.")
add("DEL-06-04#CLM-019.2", NA, "Records list asserting TBD; legacy chirality-hooks.ts and tool-path-policy.ts show the records could be filled, they do not meet a TBD.")
add("DEL-06-05#CLM-016", NA, "STATE_ASSERTION of TBD paths; legacy tool-shell-policy.ts is cited as 'contrary' evidence.")
add("DEL-06-05#CLM-019.1", "ADD",
    "'timeout implemented in tool-shell-policy.ts' is true only of LEGACY_ONLY tool-shell-policy.ts:7-9 (Notes: 'the timeout line is accurate at module level').")
add("DEL-06-06#CLM-006", NA, "CONTEXT_CLAIM that the mapper path is TBD; legacy sdk-message-mapper.ts refutes it.")
add("DEL-06-06#CLM-018", "ADD",
    "'implementation/test paths are the legacy harness modules' is true only of the LEGACY_ONLY sdk-message-mapper.ts, chirality-hooks.ts, session-events.ts and tool-result-artifacts.ts cited.")
add("DEL-08-04#CLM-019", NA, "STATE_ASSERTION of INITIALIZED/TBD prerequisites; legacy subagent-governance.ts, permission-overlay.ts and chirality-hooks.ts refute the TBDs.")
add("DEL-08-05#CLM-032", NA, "The example's string contractVersion is contradicted by LEGACY_ONLY agent-runtime-contract.ts:10 (numeric); the code does not meet the claim.")
add("DEL-10-01#CLM-003.2", NA, "STATE_ASSERTION that instances remain TBD; legacy domain-profile-registry.ts:53-115 refutes it.")
add("DEL-10-01#CLM-004.5", NA, "No code meets the human-gated apply workflow ('positive gate workflow is absent'); legacy domain-proposal-tools.ts only shows no apply path exists on either path.")
add("DEL-10-01#CLM-026", NA, "Legacy domain-profile-registry.ts:55-84 contradicts 'must not become an app-dev runtime assumption'; it does not meet the claim.")
add("DEL-10-01#CLM-027", NA, "STATE_ASSERTION that instances and MCP tools are deferred; legacy read-tools.ts:654 and domain-proposal-tools.ts:139 refute it.")
add("DEL-10-02#CLM-003.2", NA, "STATE_ASSERTION that path patterns are undefined; legacy domain-profile-registry.ts refutes it.")
add("DEL-10-02#CLM-010.12", NA, "Proposal-path write and gated-apply proofs are NONE_FOUND; legacy propose/validate tools do not meet them.")
add("DEL-10-03#CLM-009", NA, "EXCLUSION met by absence on the live path too (no frontend/src/app/api/domain routes); the legacy tools are not needed to meet it.")
add("DEL-10-03#CLM-010.10", NA, "STATE_ASSERTION of future TBDs; legacy adapter handlers refute three of them, not meet them.")
add("DEL-10-03#CLM-028", NA, "Only the rationale sentence is false; legacy adapters refute it, and the example keys match TEST_ONLY operation-proposal.ts.")
add("DEL-10-03#STATE-1", NA, "Legacy domain-proposal-tools.ts is cited to show the Claude/Pi path is retained, which does not meet 'first concrete/current path'.")
add("DEL-10-04#CLM-009", NA, "EXCLUSION met by absence on the live path too (no /api/domain route); legacy descriptors only confirm no apply tool exists.")
add("DEL-10-04#CLM-016.1", "ADD",
    "Of the owned items, the 'PEC registry-entry content' exists only in LEGACY_ONLY domain-profile-registry.ts:85-114 (pec-scratch-server.mjs TEST_ONLY, run-pec-bridge-rehearsal.ts LEGACY_ONLY).")
add("DOC:VALSTRAT#7", NA, "Legacy pi-agent-engine-adapter.ts shows the Pi path is retained, which refutes 'current Anthropic path'; it does not meet the claim.")
add("DOC:ADDING_A_TOOL#0", "ADD",
    "Of the named primary sources, the present ones are LEGACY_ONLY sdk-options-builder.ts:125 and mcp/read-tools.ts:1048, with the registry and tool names at LEGACY_ONLY runtime-contracts (call a).")


def main():
    _, cand = r3lib.read_csv(os.path.join(r3lib.WORK, "CAND_R4Q1_TASK.csv"))
    _, cc = r3lib.read_csv(os.path.join(r3lib.R3, "CLAIM_CONCORDANCE.csv"))
    _, ec = r3lib.read_csv(os.path.join(r3lib.R3, "EXTENSION_CONCORDANCE.csv"))
    cur = {r["ClaimKey"]: r for r in cc + ec}
    reach = {}
    with open(os.path.join(r3lib.R2, "_shared", "EVIDENCE_PACK", "REACHABILITY.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            reach[r["Path"]] = r["Reach"]
    assert set(D) == {r["ClaimKey"] for r in cand}, (set(D) ^ {r["ClaimKey"] for r in cand})
    out, errs = [], []
    for r in cand:
        k = r["ClaimKey"]
        d = D[k]
        row = cur[k]
        v = d["Verdict"]
        allowed = {"ADD?": {"ADD", "NO_ADD", "UNDECIDED"},
                   "KEEP?": {"KEEP_RULE3", "KEEP_OTHER", "DROP", "UNDECIDED"}}[r["Question"]]
        if v not in allowed:
            errs.append(f"{k}: verdict {v} not allowed for {r['Question']}")
        toks = r3lib.hdn_tokens(row["HumanDecisionNeeded"])
        if v == "ADD":
            toks = [t for t in toks if t != "NO"] + ["R4-Q1"]
        elif v == "DROP":
            toks = [t for t in toks if t != "R4-Q1"]
        new = "; ".join(t for t in toks if t != "NO") or "NO"
        tf = ""
        if d["TagFix"]:
            if v != "KEEP_RULE3":
                errs.append(f"{k}: TagFix on non-KEEP_RULE3")
            find, rep = d["TagFix"]
            n = row["ImplementationEvidence"].count(find)
            if n != 1:
                errs.append(f"{k}: Find occurs {n}x")
            for p in [x for x in [OVERLAY, HOOKS, MAPPER, EVENTS, ARTIFACTS, EVIDENCE, POOL, TURN, BUILDER,
                                  READTOOLS, ANTHROPIC, GOV, OPTIONS, SESSMGR] if x in rep and x not in find]:
                if reach.get(p) != "LEGACY_ONLY" and p not in SYMBOL_LEVEL:
                    errs.append(f"{k}: added {p} is {reach.get(p)}")
            if "=>" in find or "=>" in rep:
                errs.append(f"{k}: '=>' inside TagFix text")
            tf = find + "=>" + rep
        elif v == "KEEP_RULE3":
            errs.append(f"{k}: KEEP_RULE3 without TagFix")
        if d["AlsoModule"] and "ALSO_MODULE:" in row["Notes"]:
            errs.append(f"{k}: Notes already carry ALSO_MODULE")
        out.append(dict(ClaimKey=k, Question=r["Question"], Verdict=v, NewHumanDecisionNeeded=new,
                        TagFix=tf, AlsoModule=d["AlsoModule"], Basis=d["Basis"]))
    if errs:
        print("\n".join(errs))
        sys.exit(1)
    hdr = ["ClaimKey", "Question", "Verdict", "NewHumanDecisionNeeded", "TagFix", "AlsoModule", "Basis"]
    r3lib.write_csv(os.path.join(r3lib.WORK, "T2_R4Q1_VERDICTS.csv"), hdr, out)
    print(collections.Counter((o["Question"], o["Verdict"]) for o in out))
    print("TagFix", sum(1 for o in out if o["TagFix"]), "AlsoModule", sum(1 for o in out if o["AlsoModule"]))


if __name__ == "__main__":
    main()
