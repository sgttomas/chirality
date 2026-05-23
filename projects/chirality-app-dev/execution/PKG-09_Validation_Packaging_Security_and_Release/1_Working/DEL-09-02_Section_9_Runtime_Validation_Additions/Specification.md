# Specification: DEL-09-02 Section 9 Runtime Validation Additions

## Scope

This deliverable specifies runtime validation additions for Section 9 of the harness validation surface. It covers validation IDs, harness runner updates, and summary schema expectations for runtime boundaries related to the engine contract, SDK mapper, event log, settings isolation, permissions, MCP tools, hooks, compaction, and subagents.

Excluded from this deliverable:

- Feature implementation outside test fixtures and packaging glue, per package exclusions in `_CONTEXT.md`.
- Creation of dependency register entries or `Dependencies.csv`.
- Domain-profile runtime validation before a governed domain-profile amendment enters scope; the ID may remain listed but should be gated or marked pending.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| DEL-09-02-RQ-001 | Section 9 validation additions MUST include the runtime validation IDs enumerated by PRD Section 12.4 and SPEC Section 19.3. | `docs/PRD.md` Section 12.4; `docs/SPEC.md` Section 19.3 |
| DEL-09-02-RQ-002 | Validation for `section9.runtime_engine_contract` MUST confirm Chirality owns an `AgentEnginePort` / `RuntimeEngineContract` boundary separate from SDK APIs, including accepted turn input, UI events, canonical events, permission decisions, permitted tool exposure, session linkage, interrupt/cancel handling, and terminal outcomes. | `docs/SPEC.md` Sections 10.1-10.4; `docs/CONTRACT.md` K-ENGINE-1, K-ENGINE-2, K-ENGINE-4 |
| DEL-09-02-RQ-003 | Validation for SDK mapping and event-log IDs MUST preserve the distinction between browser `UIEvent`s and persisted `HarnessEvent`s; SDK messages and transcripts are adapter metadata or secondary state unless imported into `HarnessEvent` form. | `docs/SPEC.md` Sections 9 and 10.3; `docs/CONTRACT.md` K-EVENT-1, K-SDK-3 |
| DEL-09-02-RQ-004 | Validation for session replay MUST confirm newline-delimited append order, unique event IDs, no secret storage, artifact references for large payloads, and tolerance for malformed trailing lines. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5, K-EVENT-6, K-EVENT-7 |
| DEL-09-02-RQ-005 | Validation for `section9.settingsources_isolation` MUST confirm shipped runtime does not load ambient user/global Claude Code settings or local `.claude/settings.local.json`; default `settingSources: []` is required where applicable. | `docs/CONTRACT.md` K-SDK-1; `docs/PRD.md` FR-117, NFR-028 |
| DEL-09-02-RQ-006 | Validation for permission overlay MUST confirm deny-first behavior, that prompt text and `allowedTools` alone are not safety boundaries, and that `disallowedTools`, mode policy, hooks, `canUseTool`, and/or `dontAsk` enforce restrictions. | `docs/CONTRACT.md` K-PERM-1 through K-PERM-4; `docs/SPEC.md` Sections 14.3 and 15.1 |
| DEL-09-02-RQ-007 | Validation for Chirality MCP status/dependency tools MUST use `mcp__chirality__*` naming and confirm MCP tools pass through the same permission, hook, path, redaction, and event logging policy as SDK built-ins. | `docs/SPEC.md` Sections 14.1-14.3; `docs/TYPES.md` Section 8.4; `docs/CONTRACT.md` K-MCP-1 |
| DEL-09-02-RQ-008 | Validation for path and instruction-root hooks MUST confirm active project-root containment, instruction-root write denial, initial symlink-write rejection, and fail-closed behavior for write, shell, domain, and subagent actions. | `docs/SPEC.md` Section 15.2; `docs/CONTRACT.md` K-HOOK-1, K-PATH-2, K-PATH-3 |
| DEL-09-02-RQ-009 | Validation for tool result budgets MUST confirm large or sensitive tool results are budgeted, previewed, stored as artifacts, or redacted according to policy. | `docs/CONTRACT.md` K-EVENT-7; `docs/PRD.md` FR-096 |
| DEL-09-02-RQ-010 | Validation for compaction MUST confirm compaction boundaries are persisted when available and replay implications are recorded. | `docs/SPEC.md` Section 15.2; `docs/TYPES.md` Section 8.5; `docs/PRD.md` FR-098, FR-099 |
| DEL-09-02-RQ-011 | Validation for subagent governance MUST confirm subagent delegation fails closed unless governance gates pass, child capabilities do not expand parent permissions, and child run records/artifact references are produced when execution is enabled. | `docs/CONTRACT.md` K-SUBAGENT-1 through K-SUBAGENT-3; `docs/PRD.md` FR-101, FR-102 |
| DEL-09-02-RQ-012 | Harness runner updates MUST preserve existing Section 8 validation coverage while adding Section 9 IDs as runtime phases land. | `docs/PRD.md` Sections 12.3-12.4; `docs/SPEC.md` Sections 19.2-19.3 |
| DEL-09-02-RQ-013 | The summary schema MUST identify Section 9 validation outcomes distinctly enough to support release readiness review. Exact schema fields are TBD. | `_CONTEXT.md`; `docs/PRD.md` Section 12.4; ASSUMPTION based on anticipated artifact "summary schema" |
| DEL-09-02-RQ-014 | Each Section 9 ID MUST carry an explicit status and evidence reference or blocker note; runtime phases that have not landed MUST NOT be reported as passing. Accepted status enum is TBD, but natural-language status terms MUST preserve the distinction between pass, fail, pending, skipped, blocked, and gated. | `docs/PRD.md` Section 12.4; `docs/SPEC.md` Section 19.3; `_SEMANTIC_LENSING.md` A-001/C-001/E-002 worklist |
| DEL-09-02-RQ-015 | The registry or manifest evidence SHOULD include each Section 9 ID, source reference, status metadata, warning/blocker notes, and evidence artifact reference when available. Exact registry/manifest path and field names are TBD. | `docs/PRD.md` Section 12.4; `docs/SPEC.md` Section 19.3; `_CONTEXT.md` Anticipated Artifacts; `_SEMANTIC_LENSING.md` F-001/B-002 worklist |
| DEL-09-02-RQ-016 | Section 9 fixture coverage SHOULD be grouped by runtime surface: engine boundary, SDK mapper/event log/replay, settings isolation, permission overlay, tool/MCP exposure, path/instruction-root hooks, tool-result budget, compaction boundary, and subagent governance. Exact fixture file paths remain TBD. | `docs/CONTRACT.md` Sections 1.4-1.6; `docs/SPEC.md` Sections 9, 10, 14, 15, 19.3; `_SEMANTIC_LENSING.md` X-001 worklist |

## Standards

| Standard / Contract | Applicability |
|---|---|
| `docs/CONTRACT.md` K-ENGINE, K-SDK, K-EVENT, K-PERM, K-TOOL, K-MCP, K-HOOK, K-PATH, K-SUBAGENT | Governs invariant-level validation targets. |
| `docs/SPEC.md` Sections 9, 10, 14, 15, 19.3 | Governs event schema, runtime engine contract, MCP names, permissions/hooks, and Section 9 validation IDs. |
| `docs/TYPES.md` Sections 7.3, 8.4, 8.5 | Governs type targets and vocabulary for events, MCP names, and hook terms. |
| `docs/PRD.md` Sections 8.12-8.16 and 12.4 | Governs product requirements for runtime boundaries and validation additions. PRD hash mismatch warning applies. |

## Verification

| Requirement | Verification Approach |
|---|---|
| DEL-09-02-RQ-001 | Static test or manifest assertion that every Section 9 ID from PRD/SPEC is present with status metadata. |
| DEL-09-02-RQ-002 | Engine conformance test against `AgentEnginePort` / `RuntimeEngineContract`, including terminal outcome and interrupt/cancel cases. |
| DEL-09-02-RQ-003 | Mapper tests that assert SDK message names do not leak into browser contract or canonical persisted event contract except as explicit adapter metadata. |
| DEL-09-02-RQ-004 | JSONL replay tests covering ordered events, malformed trailing line tolerance, redaction, and artifact references. |
| DEL-09-02-RQ-005 | SDK options builder test asserting shipped default settings-source posture. |
| DEL-09-02-RQ-006 | Permission tests for denied writes, shell, unknown tools, `allowedTools` misuse, and `dontAsk` denial behavior. |
| DEL-09-02-RQ-007 | MCP wrapper tests for status/dependency tool names, permission policy, hook invocation, and redaction/event logging. |
| DEL-09-02-RQ-008 | Hook tests for project-root containment, instruction-root protection, symlink writes, and fail-closed pre-tool failures. |
| DEL-09-02-RQ-009 | Tool-result tests for inline/preview/artifact/redaction behavior. |
| DEL-09-02-RQ-010 | Compaction callback or event-mapping test for `context.compacted` persistence. |
| DEL-09-02-RQ-011 | Subagent governance tests for fail-closed gating, restricted child tools/cwd, and child-run records. |
| DEL-09-02-RQ-012 | Harness premerge run proving Section 8 validations remain present while Section 9 IDs are added. |
| DEL-09-02-RQ-013 | Summary fixture/schema test; exact schema path and fields TBD. |
| DEL-09-02-RQ-014 | Manifest or summary assertion that no ID lacking an implemented runtime phase is marked pass; accepted enum and schema path TBD. |
| DEL-09-02-RQ-015 | Manifest/fixture review that every Section 9 ID has source reference, status metadata, and evidence/blocker reference; exact file path TBD. |
| DEL-09-02-RQ-016 | Fixture-family or evidence-ID review for each runtime surface; exact fixture names and paths TBD. |

## Documentation

Required deliverable artifacts:

- Section 9 validation ID registry or equivalent manifest.
- Harness runner changes that execute/report the Section 9 IDs.
- Summary schema or fixture update showing Section 9 results.
- Test fixtures for event log, permissions, MCP, hooks, compaction, and subagent governance where implementation exists.
- Human-facing notes for any IDs marked pending because their runtime phase has not landed.
- Section 8 preservation evidence or premerge summary reference alongside new Section 9 outcomes.
- Warning-qualified PRD source-state note while `_REFERENCES.md` records REF-006 as `HASH_MISMATCH`.
