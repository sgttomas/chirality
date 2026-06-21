# Assessment INSP-03: DEL-09-02 Section 9 Runtime Validation Additions

Deliverable: DEL-09-02
Package: PKG-09 Validation, Packaging, Security, and Release
Date: 2026-06-21
Inspector: WORKING_ITEMS
Lifecycle: CHECKING
Reviewed SHA: `d0766e0f24b923f7925c711fe05e0cf5d28fd1fb`
Spec source: `Specification.md`

## Scope

This assessment inspected the Section 9 runtime validation additions: runtime-boundary IDs, report-only runner behavior, fixture grouping, stable summary output, and preservation of Section 8 while Section 9 remains maturing. It did not promote report-only Section 9 checks into a release gate.

## Requirements Conformance Matrix

| Requirement | Status | Evidence | Notes |
|---|---|---|---|
| RQ001 - Section 9 IDs cover the runtime validation requirements. | PASS | `frontend/scripts/validate-harness-section9.mjs` declares 13 Section 9 IDs and source test files at lines 25-98. | The live ID inventory is explicit. |
| RQ002 - Runtime-engine contract validates accepted input, events, permissions, tools, session linkage, interrupts, and terminals. | PASS | `frontend/src/lib/harness/turn-engine.ts` accepts/validates turn input and attachments at lines 89-107 and runs turns without HTTP at lines 186-305; `frontend/src/__tests__/lib/turn-engine.test.ts` covers no-HTTP run and session persistence at lines 160-205; route tests cover terminal failures and interruptions at lines 731-787 and 971-1040. | Coverage is distributed across runtime and route fixtures. |
| RQ003 - SDK mapping/event log preserve UIEvent vs HarnessEvent distinction. | PASS | `frontend/src/lib/harness/session-events.ts` appends/replays HarnessEvent JSONL at lines 14-84; `frontend/src/__tests__/lib/sdk-message-mapper.test.ts` and `frontend/src/__tests__/lib/session-events.test.ts` exercise mapper and replay behavior. | The distinction exists in code and fixtures. |
| RQ004 - Replay append order, unique IDs, no secrets, artifact refs, and malformed lines. | PASS | `frontend/src/lib/harness/session-events.ts` writes append-only events at lines 14-22 and counts malformed replay lines at lines 50-84; session-event tests cover append/replay and malformed tails. | Secret hygiene also depends on broader redaction paths assessed elsewhere. |
| RQ005 - `settingSources: []` isolation is validated. | PASS | `frontend/src/lib/harness/sdk-options-builder.ts` defaults `settingSources` to an empty array at lines 22-37 and 148; Section 9 maps this through `section9.settingsources_isolation`. | Isolated setting sources are explicit. |
| RQ006 - Permission overlay hard-deny behavior is validated. | PASS | `frontend/src/lib/harness/permission-overlay.ts` hard-denies reserved/unknown/network/subagent/workspace classes at lines 111-265 and enforces tool/path/shell decisions at lines 338-447. | The overlay is stronger than SDK allowedTools alone. |
| RQ007 - Chirality MCP names and policies are validated. | PASS | `frontend/src/lib/harness/mcp/tool-names.ts` defines `mcp__chirality__*` names at lines 1-44; read-tool evidence and policy checks are implemented in `frontend/src/lib/harness/mcp/read-tools.ts` lines 118-190 and 238-320. | MCP naming and policy are covered by Section 9 files and focused tests. |
| RQ008 - Path/instruction-root hooks fail closed. | PASS | `frontend/src/lib/harness/tool-path-policy.ts` enforces containment, instruction-root denial, and symlink rejection at lines 95-160, 215-258; `frontend/src/lib/harness/chirality-hooks.ts` enforces fail-closed pre-hooks at lines 337-477. | Coverage is present for write/shell/domain/subagent classes. |
| RQ009 - Tool-result budgets, artifacting, and redaction are validated. | PASS | Tool result and artifact tests are included in the Section 9 registry; implementation evidence lives in `frontend/src/lib/harness/tool-result-artifacts.ts` and related tests. | PASS is based on present Section 9 test mapping plus existing PKG-05/06 assessed implementation. |
| RQ010 - Compaction boundaries and replay implications are validated. | PARTIAL | `frontend/src/lib/harness/chirality-hooks.ts` records compaction-related hook artifacts at lines 480-618; session replay mechanics are covered by `session-events.ts` lines 50-84. | Dedicated Section 9 compaction lifecycle semantics remain thinner than the rest of the runtime boundary. |
| RQ011 - Subagent governance is fail-closed with child records/artifacts when enabled. | PASS | `frontend/src/lib/harness/permission-overlay.ts` and `frontend/src/lib/harness/chirality-hooks.ts` fail closed on subagent classes; route tests cover governance denial/allowance at lines 549-729. | Child-run taxonomy residuals remain with PKG-08, but Section 9 has coverage hooks. |
| RQ012 - Section 8 remains preserved while adding Section 9. | PASS | `frontend/scripts/validate-harness-premerge.mjs` enforces Section 8 first at lines 116-164, then runs Section 9 report-only at lines 165-188. | Section 9 cannot mask Section 8 failures. |
| RQ013 - Summary schema distinguishes Section 9 outcomes. | PARTIAL | `frontend/scripts/validate-harness-section9.mjs` writes status, testCount, and per-check result fields at lines 219-245. | The schema exists, but warning/blocker fields and the exact governed enum remain underdeveloped. |
| RQ014 - Each ID has explicit status/evidence/blocker; no pass for unlanded phases. | PARTIAL | The Section 9 summary records per-check status and missing-file failures at lines 173-212 and 219-245. | It lacks a mature blocker taxonomy and still treats Section 9 as report-only in premerge. |
| RQ015 - Registry/manifest evidence includes ID/source/status/warnings/evidence. | PARTIAL | `validate-harness-section9.mjs` functions as a registry with IDs, titles, descriptions, test files, and status output at lines 25-98 and 219-245. | There is no separate governed manifest artifact with warnings and evidence references. |
| RQ016 - Fixtures are grouped by runtime surface. | PASS | Section 9 registry entries point to grouped runtime files such as engine conformance, SDK mapper, options, permissions, MCP, hooks, artifacts, subagents, and runtime contract tests at lines 25-98. | Grouping is sufficient for current report-only validation. |

## Gap Inventory

| Gap | Severity | Finding | Recommended owner |
|---|---:|---|---|
| Section 9 remains report-only in premerge | G6 / Medium | The premerge wrapper intentionally runs Section 9 without failing the wrapper. | Validation policy tranche |
| Summary/manifest schema is not final | Medium | The runner writes useful results but does not yet provide a governed warnings/blockers/evidence manifest. | Validation/docs tranche |
| Compaction lifecycle validation is partial | Medium | Replay mechanics exist, but dedicated compaction boundary semantics remain less complete than other runtime surfaces. | Runtime validation tranche |

## Source-State Caveat

`docs/PRD.md` is warning-limited for this deliverable: `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`, expected `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`, actual `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. No semantic files were used or produced.

## Dependency Closure Note

No dependency rows were marked satisfied or mutated by this assessment. DEL-09-02 still has 25 active dependency rows with `SatisfactionStatus: TBD`; closure remains open.

## Forward Development Recommendation

1. Decide whether Section 9 should remain report-only or become a release-significant gate, then encode that policy in premerge. Type: governance/validation. Size: M. Strategic fit: ON-STRATEGY.
2. Promote the Section 9 registry into a stable manifest artifact with ID, source, status, warnings, blockers, and evidence paths. Type: validation docs/tooling. Size: M. Strategic fit: ON-STRATEGY.
3. Add dedicated compaction-boundary fixtures where lifecycle semantics are asserted directly rather than inferred from replay and hooks. Type: test. Size: S. Strategic fit: ON-STRATEGY.

## Issuance-Gate-Process Observations

The gate needs to distinguish "implemented validation surface" from "release-blocking validation gate." A deliverable can be materially useful while still not issuance-ready if its runner remains report-only and its manifest schema is not governed.
