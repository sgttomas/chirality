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
| DEL-06-05-REQ009 | PASS | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 38-118; `frontend/src/lib/harness/sdk-message-mapper.ts` lines 455-495; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 455-475. | D-APP-42 artifact metadata includes SHA-256, `toolName`, optional `turnId` where available, byte counts, redaction/truncation flags, paths, and session-lifetime retention; ADQ-11 links interrupted Bash results to `tool.failed` outcome evidence. |
| DEL-06-05-REQ010 | PASS | `frontend/src/lib/harness/tool-evidence.ts` lines 237-241; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 409-475; D-APP-43. | Deterministic adapter-level evidence proves `Bash` tool results with `interrupted: true` are non-success outcomes (`tool.failed`) with safe stream metadata. D-APP-43 does not require live provider process-cancellation proof for ADQ-11 closure. |
| DEL-06-05-REQ011 | PASS | `frontend/src/lib/harness/permission-overlay.ts` lines 288-315; `frontend/src/lib/harness/chirality-hooks.ts` lines 359-421 and 480-595; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 261-449. | Permission, hook started/completed/failed, output, and interruption metadata are auditable in events. |
| DEL-06-05-REQ012 | PASS | `frontend/src/lib/harness/chirality-hooks.ts` lines 462-477; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 370-449. | Hook failures and shell policy denials fail closed. |
| DEL-06-05-REQ013 | PASS | `frontend/src/lib/harness/tool-shell-policy.ts` lines 220-344; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 370-449. | Bash blocks network commands/URLs, parent traversal, instruction-root paths, symlink redirections, sandbox override, and background commands. |
| DEL-06-05-REQ014 | PASS | `frontend/src/lib/harness/tool-descriptor.ts` lines 727-775; `frontend/src/lib/harness/tool-shell-policy.ts` lines 7-21. | Bash public policy objects are Chirality-owned; SDK `Bash` appears only as adapter metadata. |
| DEL-06-05-REQ015 | PASS | `frontend/src/__tests__/lib/permission-overlay.test.ts` lines 102-135 and 238-337; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 261-449; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 336-407. | Tests cover mode denies, denied-never-spawns callbacks, timeout injection, stdout/stderr metadata, artifacts, and interruption metadata. |
| DEL-06-05-REQ016 | PASS | `frontend/src/lib/harness/tool-shell-policy.ts` lines 7-21 and 220-344; `frontend/src/__tests__/lib/chirality-hooks.test.ts` lines 370-449; `_REFERENCES.md` REF-006 `MATCH`. | Command metadata and network-posture checks exist, numeric timeout policy is implemented, and PRD-derived preflight completeness is no longer warning-limited in active review records. |

## Gap Inventory

| Gap | Severity | Evidence | Recommendation |
|---|---:|---|---|
| Live Bash process-cancellation proof is not required for ADQ-11 closure. | Low | D-APP-43; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 409-475. | Keep live provider/process cancellation as optional future adapter evidence, not a default issue-readiness blocker. |
| Bash result metadata and outcome linkage residual is closed by D-APP-42 plus ADQ-11. | Low | `frontend/src/lib/harness/tool-result-artifacts.ts` lines 38-118; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` lines 455-475. | Preserve checksum/retention/turn/tool metadata and interrupted failure mapping across future artifact changes. |
| Historical REF-006 warning text in older run records is retired for active review. | Low | `_REFERENCES.md` REF-006 is `MATCH` under the D-APP-38 authority corpus v2. | Keep the D-APP-38 reference status check in closeout validation. |

## Source-State Caveat

`docs/PRD.md` is no longer warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as
`MATCH` under the D-APP-38 authority corpus v2. Historical HASH_MISMATCH notes in `_run_records`
remain archival only.

## Dependency Closure Note

ADQ-11 satisfies the interrupted Bash adapter-proof, result metadata/outcome linkage, and REF-006
source-state residuals for this deliverable. Other active rows remain pending for DEL-06-01 overlay,
DEL-06-04 write/path hooks, DEL-06-06 lifecycle/evidence hooks, and validation docs unless separately
closed by their owning deliverables.

## Forward Development Recommendation

| Step | Type | Size | Strategic fit | Prerequisite |
|---|---|---:|---|---|
| Keep interrupted Bash adapter fixtures aligned with D-APP-43 non-success semantics. | test/governance | S | FIT | Future SDK Bash result-shape change. |
| Keep shell artifact metadata aligned with D-APP-42 checksum/retention policy. | code/test | S | FIT | Future ToolResultStore metadata change. |
| Keep D-APP-38 authority-corpus status clean during future authority-document edits. | governance | S | FIT | Authority-document edits occur. |

## Issuance-Gate-Process Observations

DEL-06-05 has strong no-spawn, timeout, stream-metadata, artifact, interruption, and network/path
policy evidence. ADQ-11 closes the Bash interruption and metadata residuals targeted by the
autonomous queue. This does not advance lifecycle state or make an issuance claim.
