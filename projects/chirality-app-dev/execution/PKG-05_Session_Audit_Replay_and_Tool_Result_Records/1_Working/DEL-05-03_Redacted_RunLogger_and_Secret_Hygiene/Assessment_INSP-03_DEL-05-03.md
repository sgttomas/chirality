# Assessment INSP-03: DEL-05-03 Redacted RunLogger and Secret Hygiene

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-05-03 |
| Package | PKG-05 Session Audit, Replay, and Tool Result Records |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `18511e933233b90ff2a84dd41f5b40041719c300` |
| Spec source | `Specification.md` lines 5-63 |

## Scope

DEL-05-03 covers redaction for runtime events, run logs, tool artifacts, provider errors, SDK failures/debug output, HarnessEvent payloads, large/sensitive tool results, and helper APIs for configured secret variants.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-05-03-R1 | PARTIAL | `frontend/src/lib/harness/run-logger.ts` lines 64-109; `frontend/src/lib/harness/session-events.ts` lines 14-22; `frontend/src/lib/harness/tool-result-artifacts.ts` lines 41-98. Focused validation passed. | Runtime events and tool artifacts are redacted for configured API keys, but whole-product proof across every log/transcript/display path is not complete. |
| DEL-05-03-R2 | PARTIAL | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 54-70 and 356-367; `frontend/src/__tests__/lib/claude-agent-sdk-manager.test.ts` lines 225-262. Focused validation passed. | Active-turn key handoff is scoped and SDK failures are redacted, but SDK transcript/debug surfaces remain secondary and not fully enumerated. |
| DEL-05-03-R3 | PARTIAL | `frontend/src/lib/harness/run-logger.ts` lines 64-109; `frontend/src/__tests__/lib/harness-ui-bridge.test.ts` lines 49-62. Focused validation passed. | Raw, URL-encoded, and JSON-like configured API key values are redacted; non-API arbitrary secret schema is not accepted yet. |
| DEL-05-03-R4 | PARTIAL | `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 356-367; `frontend/src/lib/harness/anthropic-agent-sdk-manager.ts` provider classification tests from DEL-04-05. Focused validation passed. | Typed `SDK_FAILURE` redaction exists, but timeout/debug/log breadth still needs cross-surface release proof. |
| DEL-05-03-R5 | PARTIAL | `frontend/src/lib/harness/harness-ui-bridge.ts` lines 15-32; `frontend/src/lib/harness/claude-agent-sdk-manager.ts` lines 356-367. | Persisted/displayed bridged payloads are redacted, but SDK debug logs and stderr capture paths were not fully found as first-class owned surfaces in this wave. |
| DEL-05-03-R6 | PASS | `frontend/src/lib/harness/session-events.ts` lines 14-22; `frontend/src/lib/harness/harness-ui-bridge.ts` lines 25-33; `frontend/src/__tests__/lib/harness-ui-bridge.test.ts` lines 49-62. Focused validation passed. | HarnessEvent persistence and browser forwarding pass through redaction. |
| DEL-05-03-R7 | PARTIAL | `frontend/src/lib/harness/tool-evidence.ts` lines 132-172; `frontend/src/lib/harness/tool-result-artifacts.ts` lines 29-98; `frontend/src/__tests__/lib/tool-result-artifacts.test.ts` lines 39-83. Focused validation passed. | Large tool results are budgeted, redacted, and artifacted; explicit sensitive-result withheld policy is not yet separate from redaction/truncation. |
| DEL-05-03-R8 | PASS | `frontend/src/lib/harness/session-events.ts` lines 6-22; `frontend/src/lib/harness/types.ts` lines 30-35. Focused validation passed. | SDK transcript fields are metadata; canonical replay remains event JSONL. |
| DEL-05-03-R9 | PASS | `frontend/src/lib/harness/run-logger.ts` lines 64-91; focused tests in `frontend/src/__tests__/lib/session-events.test.ts` lines 77-197. Focused validation passed. | Configured key variants are expanded and replaced before persistence/display. |
| DEL-05-03-R10 | PASS | `frontend/src/lib/harness/run-logger.ts` lines 93-109; `frontend/src/lib/harness/tool-evidence.ts` lines 201-235. Focused validation passed. | Redaction preserves non-secret metadata shape. |
| DEL-05-03-R11 | PARTIAL | `frontend/src/lib/harness/session-events.ts` lines 14-22; `frontend/src/lib/harness/tool-result-artifacts.ts` lines 41-98; `frontend/src/lib/harness/chirality-hooks.ts` lines 527-588. Focused validation passed. | Main event/artifact/hook paths are covered, but "every path" still needs a release-quality proof matrix. |
| DEL-05-03-R12 | PARTIAL | `frontend/src/lib/harness/run-logger.ts` lines 64-109. | Final helper module path exists, but configured-secret schema beyond API-key sources remains TBD. |
| DEL-05-03-R13 | PARTIAL | `frontend/src/lib/harness/tool-evidence.ts` lines 22-39 and 132-172; `frontend/src/lib/harness/tool-result-artifacts.ts` lines 29-98. Focused validation passed. | Inline/artifact/truncated cases are covered; explicit preview and withheld-sensitive cases remain incomplete. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Redaction proof is strong for configured API keys but not yet an exhaustive all-runtime-path matrix. | High | `Specification.md` lines 24-36; `frontend/src/lib/harness/run-logger.ts` lines 64-109. | Build a release-gate redaction matrix spanning events, UI bridge, provider failures, tool artifacts, hook failures, session metadata, and any SDK transcript/debug paths. |
| Arbitrary configured secret taxonomy is not accepted. | Medium | `frontend/src/lib/harness/run-logger.ts` lines 64-77. | Decide whether the helper remains API-key-specific or accepts a broader secret registry. |
| Withheld-sensitive result policy is not distinct from redaction/truncation. | Medium | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 59-75. | Add a typed withheld/sensitive outcome only if product policy requires retaining evidence without storing raw payloads. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active pending rows remain for REF-006, DEL-04-05 provider-boundary redaction breadth, ToolResultStore downstream proof, and final helper/secret-schema acceptance.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Create a redaction-path proof matrix and link each path to a focused fixture. | test/evidence | M | FIT | Keep existing session-event/tool-artifact tests green. |
| Decide whether configured secrets remain API-key-specific or become a small explicit registry. | architecture | S | FIT | Product/security ruling if broadening beyond API keys. |
| Add preview/withheld-sensitive result cases only after ToolResultStore threshold and retention rules are accepted. | code/test | S | FIT | DEL-05-05 thresholds accepted. |

## Issuance-Gate-Process Observations

DEL-05-03 should not be issued on the current evidence alone because its strongest claim is deliberately broad: no secrets in all runtime logs/events/transcripts/artifacts/display paths. The process is correctly surfacing that broad claim as a release-quality proof requirement, not a source-inspection assumption.

## D-APP-56 R5 P40 annotation (2026-07-12)

The source-state caveat above is preserved as historical assessment evidence. REF-006 now records `docs/PRD.md` expected and actual SHA-256 as `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd` (`MATCH`) under D-APP-38; it is not a current warning or blocker. No assessment verdict or lifecycle state changes here.
