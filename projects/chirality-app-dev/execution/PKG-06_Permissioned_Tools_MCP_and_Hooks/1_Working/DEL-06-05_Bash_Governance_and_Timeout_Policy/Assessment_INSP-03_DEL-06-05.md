# Assessment INSP-03: DEL-06-05 Bash Governance and Timeout Policy

## Header

| Field | Value |
|---|---|
| Deliverable | DEL-06-05 |
| Package | PKG-06 Permissioned Tools, MCP, and Hooks |
| Date | 2026-06-21 |
| Inspector | WORKING_ITEMS |
| Lifecycle | CHECKING |
| Reviewed SHA | `09c840be20ee22de6bae99cf0fe3ec226d2ad3ae` |
| Spec source | `Specification.md` lines 5-76 |

## Scope

DEL-06-05 covers deny-by-default Bash exposure, mode restrictions, permission/hook/timeout requirements, no-spawn denials, stdout/stderr metadata, artifact handling for large output, interruption evidence, and filesystem/network policy for shell commands.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| DEL-06-05-REQ001 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 975-1062; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 57-87. | Bash is disallowed by default unless explicitly requested and allowed by mode. |
| DEL-06-05-REQ002 | PASS | `frontend/src/__tests__/lib/tool-descriptor.test.ts` lines 242-277; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 57-87. | Read-only exposure keeps Bash omitted/disallowed. |
| DEL-06-05-REQ003 | PASS | `frontend/src/lib/harness/permission-overlay.ts` lines 140-168; `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 153-180. | `dontAsk` denies Bash without prompting; no safe subset exists in the current implementation. |
| DEL-06-05-REQ004 | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` lines 87-138; `frontend/src/__tests__/lib/sdk-options-builder.test.ts` lines 290-319. | Bash is not enabled by `allowedTools` alone; callbacks and hooks remain attached. |
| DEL-06-05-REQ005 | PASS | `frontend/src/lib/harness/permission-overlay.ts` lines 338-447; `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 238-337. | Denied Bash callbacks return deny before SDK execution and record permission evidence. |
| DEL-06-05-REQ006 | PASS | `frontend/src/lib/harness/tool-shell-policy.ts` lines 7-10 and 175-218; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 261-337. | Bash has default and maximum timeout policy; invalid or excessive timeouts deny. |
| DEL-06-05-REQ007 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 527-545; `frontend/src/lib/harness/tool-evidence.ts` lines 174-214; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 338-358. | Bash results summarize stdout and stderr separately without storing raw output inline. |
| DEL-06-05-REQ008 | PASS | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 29-98; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 261-368. | Large shell output is redacted and persisted as an artifact with metadata rather than unbounded chat/model output. |
| DEL-06-05-REQ009 | PARTIAL | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 77-98; `frontend/src/lib/harness/chirality-hooks.ts` lines 527-548; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 336-407. | Metadata includes byte lengths, truncation/artifact flags, paths, and stream presence; explicit turn ID and final channel/outcome linkage remain partial. |
| DEL-06-05-REQ010 | PARTIAL | `frontend/src/lib/harness/tool-descriptor.ts` lines 727-775; `frontend/src/lib/harness/chirality-hooks.ts` lines 559-595. | Bash descriptor is cancellable and failure hooks record `interrupted`, but real process interrupt/cancel behavior is not proven by an execution fixture. |
| DEL-06-05-REQ011 | PASS | `frontend/src/lib/harness/permission-overlay.ts` lines 288-315; `frontend/src/lib/harness/chirality-hooks.ts` lines 359-421 and 480-595; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 261-449. | Permission, hook started/completed/failed, output, and interruption metadata are auditable in events. |
| DEL-06-05-REQ012 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 462-477; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 370-449. | Hook failures and shell policy denials fail closed. |
| DEL-06-05-REQ013 | PASS | `frontend/src/lib/harness/tool-shell-policy.ts` lines 220-344; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 370-449. | Bash blocks network commands/URLs, parent traversal, instruction-root paths, symlink redirections, sandbox override, and background commands. |
| DEL-06-05-REQ014 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 727-775; `frontend/src/lib/harness/tool-shell-policy.ts` lines 7-21. | Bash public policy objects are Chirality-owned; SDK `Bash` appears only as adapter metadata. |
| DEL-06-05-REQ015 | PASS | `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 102-135 and 238-337; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 261-449; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 336-407. | Tests cover mode denies, denied-never-spawns callbacks, timeout injection, stdout/stderr metadata, artifacts, and interruption metadata. |
| DEL-06-05-REQ016 | PARTIAL | `frontend/src/lib/harness/tool-shell-policy.ts` lines 23-34 and 246-271; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 370-449. | Command metadata and network-posture checks exist, but final PRD-derived preflight completeness remains warning-qualified pending REF-006. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Real Bash process cancellation/interrupt behavior is not proven end to end. | Medium | `frontend/src/lib/harness/chirality-hooks.ts` lines 559-595. | Add an adapter-level cancellation fixture or record a supported/unsupported behavior decision. |
| Bash result metadata lacks explicit turn ID and complete outcome linkage. | Low | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 77-98. | Extend artifact metadata once the common ToolResultStore metadata contract is updated. |
| PRD-derived preflight completeness is warning-limited. | Low | `_REFERENCES.md` REF-006 hash mismatch. | Close or waive the PRD hash before issuance. |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

This assessment does not satisfy or mutate any `Dependencies.csv` row. Active pending rows remain for DEL-06-01 overlay, DEL-06-04 write/path hooks, DEL-06-06 lifecycle/evidence hooks, validation docs, and REF-006 warning closure.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Add or explicitly defer a real process interruption fixture for Bash. | test/governance | S | FIT | Adapter interrupt behavior accepted. |
| Add optional `turnId` and clearer outcome linkage to shell artifact metadata through the shared ToolResultStore contract. | code/test | S | FIT | DEL-05-05 metadata decision. |
| Close REF-006 before issuance. | governance | S | FIT | Human source-state decision. |

## Issuance-Gate-Process Observations

DEL-06-05 has strong no-spawn, timeout, stream-metadata, artifact, and network/path policy evidence. The gate should treat interruption behavior and final metadata fields as the main residuals.
