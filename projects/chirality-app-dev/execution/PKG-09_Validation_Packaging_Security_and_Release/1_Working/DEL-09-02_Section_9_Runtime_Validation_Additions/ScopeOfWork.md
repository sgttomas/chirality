---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-09-02
package_id: PKG-09
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@d6f6cadb2be0c6e2e9c5ba331a553a54c60a8a0f
project_scope_refs: [SOW-036, SOW-037, SOW-039, SOW-045, SOW-054, SOW-057, SOW-063]
package_objective_refs: [OBJ-002, OBJ-003, OBJ-005, OBJ-007, OBJ-008]
---

# Scope of Work — DEL-09-02

## Purpose and Objective Traceability

This Scope of Work defines `DEL-09-02` in service of project scope [SOW-036, SOW-037, SOW-039, SOW-045, SOW-054, SOW-057, SOW-063] and package objectives [OBJ-002, OBJ-003, OBJ-005, OBJ-007, OBJ-008].

- **OUT-001** — Section 9 validation ID registry, harness runner updates and summary schema for the current App-owned Runtime/stock Codex boundary, complete event preservation and replay, Codex configuration/authentication separation, user-selected policy, applicable application-tool controls, tool-result budgets, compaction and governed child lineage. Retained first-adapter IDs and fixtures are compatibility evidence with explicit reach and status.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-09-02 Section 9 Runtime Validation Additions

> #### Datasheet: DEL-09-02 Section 9 Runtime Validation Additions
>
> > **D-APP-56 / D-APP-38 historical source note (2026-07-12):** REF-006 `docs/PRD.md` was recorded as `MATCH` in that reconciliation snapshot. This is historical evidence, not a current hash result. Before reliance, verify the candidate source bytes through `execution/_Scripts/references_hash_tool.py`; retain mismatch or authorized bypass evidence without inferring a corpus re-pin.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | PackageID | PKG-09 |
> | PackageName | Validation, Packaging, Security, and Release |
> | DeliverableID | DEL-09-02 |
> | DeliverableName | Section 9 Runtime Validation Additions |
> | ResponsibleParty | TBD |
> | Type | TEST_SUITE |
> | ContextEnvelope | M |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary scope | Bind Section 9 IDs to current Codex/Runtime conformance, events/replay, configuration/authentication, policy, application tools, compaction and child lineage; retain first-adapter IDs as labelled compatibility coverage. | `_CONTEXT.md`; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-09-02 |
> | Anticipated artifacts | Section 9 validation IDs; harness runner updates; summary schema. | `_CONTEXT.md`; decomposition DEL-09-02 |
> | Covered SOW items | SOW-036, SOW-037, SOW-039, SOW-045, SOW-054, SOW-057, SOW-063. | `_CONTEXT.md`; decomposition DEL-09-02 |
> | Supported objectives | OBJ-002, OBJ-003, OBJ-005, OBJ-007, OBJ-008. | `_CONTEXT.md`; decomposition DEL-09-02 |
> | Baseline validation context | Section 8 IDs preserve their original baseline coverage; each current Codex/Runtime obligation needs source-bound live-path evidence. Historical SDK-native checks qualify only their retained subject. | `docs/PRD.md` Section 12.3; `docs/SPEC.md` Section 19.2 |
> | Section 9 validation ID source list | `section9.runtime_engine_contract`, `section9.adapter_turn_engine_event_log`, `section9.adapter_message_mapper`, `section9.session_event_replay`, `section9.reliance_boundary_register`, `section9.settingsources_isolation`, `section9.sdk_session_link_resume`, `section9.permission_overlay_hard_deny_precedence`, `section9.tool_runtime_read_file`, `section9.chirality_mcp_status_dependencies`, `section9.path_containment_hook`, `section9.instruction_root_protection_hook`, `section9.tool_result_budget`, `section9.context_compaction_boundary`, `section9.subagent_governance_hook`, `section9.domain_profile_validation`. | `docs/PRD.md` Section 12.4; `docs/SPEC.md` Section 19.3 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | PRD source status | The old expected/observed hash pair described the initialization snapshot. Current reliance requires candidate-bound verification through references_hash_tool.py; no old warning or MATCH is perpetually current. | Assignment; `_REFERENCES.md` REF-006 |
> | Source grounding | Requirements and validation IDs are limited to accessible local sources. Unsupported implementation details remain `TBD` or `ASSUMPTION`. | `skills/four-documents/SKILL.md`; `_REFERENCES.md` Notes |
> | Dependency state | Declared upstream and downstream dependencies remain `TBD`; an extracted dependency register exists, but `_DEPENDENCIES.md` says not to compute blocked/available state until the project-level FULL_GRAPH register has been checked. | `_DEPENDENCIES.md` Dependency Tracking; `_DEPENDENCIES.md` Extracted Dependency Register |
> | Domain-profile validation | `section9.domain_profile_validation` appears in the Section 9 list, but PRD says it applies after a governed domain-profile amendment enters scope. | `docs/PRD.md` Section 12.4 |
>

### CLM-005 — Construction

> Use the accepted requirement and verification contract in CLM-024 and frontend/scripts/harness-section9-manifest.json. Selected implementation modules, result schemas and test hooks are evidence, not unresolved naming decisions or fresh pass results. Record the candidate, actual command/result paths, checked source basis, and live Runtime/Codex versus retained compatibility reach. Preserve every requirement in the requirement table; missing tests, native results and consumer wiring remain explicit work in Remaining. D-APP-38 source statements are historical; verify current source bytes and retain any mismatch/bypass. Earlier P3 path/schema slots and four-file record lists are superseded by the current ScopeOfWork representation and named evidence. This record grants no product, scope, lifecycle or release acceptance.

### CLM-006 — References

> ##### References
>
> | RefID | Source | Notes |
> |---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | Runtime events, reliance boundaries, SDK boundary posture, capability-forward policy with explicit hard-deny precedence and MCP constraints. |
> | REF-002 | `docs/CONTRACT.md` | Invariants for engine, events, permissions, MCP, hooks, paths, and subagents. |
> | REF-003 | `docs/SPEC.md` | Runtime event schema, engine contract, MCP names, hook rules, Section 9 IDs. |
> | REF-004 | `docs/TYPES.md` | HarnessEvent target, MCP names, hook terms, Section 9 vocabulary. |
> | REF-005 | `docs/PLAN.md` | Roadmap sequencing and validation themes. |
> | REF-006 | `docs/PRD.md` | Product requirements and Section 9 runtime validation additions; historical D-APP-38 source state; verify current candidate bytes status applies. — reconciled under D-APP-38 |
> | REF-007 | `../../workflows/software-decomp/WORKFLOW.md` | Decomposition method context; no deliverable-specific requirement extracted. |
>

### CLM-007 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-143 records the landed `harness-section9-manifest.json` and stable artifacts manifest. UPD-144 records the ruled domain-profile ID as registered and validated within the in-process read-evidence fence.

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-09-02 Section 9 Runtime Validation Additions

> #### Specification: DEL-09-02 Section 9 Runtime Validation Additions
>
> > **D-APP-56 / D-APP-38 historical source note (2026-07-12):** REF-006 `docs/PRD.md` was recorded as `MATCH` in that reconciliation snapshot. This is historical evidence, not a current hash result. Before reliance, verify the candidate source bytes through `execution/_Scripts/references_hash_tool.py`; retain mismatch or authorized bypass evidence without inferring a corpus re-pin.
>

### CLM-009 — Scope

> ##### Scope
>
> This deliverable specifies Section 9 validation IDs, harness runner updates and summary schema for the current App-owned Runtime/stock Codex path. Separate current conformance, complete event/replay/redaction, configuration/authentication separation, user-selected policy, application-tool validation, compaction and child-lineage checks from retained first-adapter compatibility IDs; preserve explicit status and evidence reach for each.
>
> Excluded from this deliverable:
>
> - Feature implementation outside test fixtures and packaging glue, per package exclusions in `_CONTEXT.md`.
> - Creation of dependency register entries or `Dependencies.csv`.
> - Domain-profile runtime validation before a governed domain-profile amendment enters scope; the ID may remain listed but should be gated or marked pending.
>

### CLM-010 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source |
> |---|---|---|
> | DEL-09-02-RQ-001 | Section 9 validation additions MUST include the runtime validation IDs enumerated by PRD Section 12.4 and SPEC Section 19.3. | `docs/PRD.md` Section 12.4; `docs/SPEC.md` Section 19.3 |
> | DEL-09-02-RQ-002 | Validation for `section9.runtime_engine_contract` MUST confirm Chirality owns an `AgentEnginePort` / `RuntimeEngineContract` boundary separate from SDK APIs, including accepted turn input, UI events, canonical events, permission decisions, permitted tool exposure, session linkage, interrupt/cancel handling, and terminal outcomes. | `docs/SPEC.md` Sections 10.1-10.4; `docs/CONTRACT.md` K-ENGINE-1, K-ENGINE-2, K-ENGINE-4 |
> | DEL-09-02-RQ-003 | Validate browser representation and Runtime persistence without loss of full Codex events or unfamiliar notifications, with structural secret protection before sinks. Known-event normalization and legacy mapper fixtures do not prove native preservation. | `docs/SPEC.md` Sections 9 and 10.3; `docs/CONTRACT.md` K-EVENT-1, K-SDK-3 |
> | DEL-09-02-RQ-004 | Validation for session replay MUST confirm newline-delimited append order, unique event IDs, no secret storage, artifact references for large payloads, and tolerance for malformed trailing lines. | `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5, K-EVENT-6, K-EVENT-7 |
> | DEL-09-02-RQ-005 | On the live Codex path, validate the effective Codex home sharing configuration/resources by reference while protecting Chirality-private credentials and models cache; S-8 verifies other clients are unaffected. Legacy settingSources isolation is compatibility evidence. | `docs/CONTRACT.md` K-SDK-1; `docs/PRD.md` FR-117, NFR-028 |
> | DEL-09-02-RQ-006 | Validate the user-selected Codex sandbox/approval policy and actual allow/deny outcomes. Prompt text or a mode label is not enforcement evidence. Applicable Chirality application controls and protected-record/domain duties remain; retired fixed SDK policy is compatibility history. | `docs/CONTRACT.md` K-PERM-1 through K-PERM-4; `docs/SPEC.md` Sections 14.3 and 15.1 |
> | DEL-09-02-RQ-007 | Validate registered Chirality application-tool catalog/call contracts and applicable path, redaction and event obligations on the Runtime path. Native Codex tools follow user-selected Codex policy; retained mcp__chirality__ interfaces are compatibility evidence. | `docs/SPEC.md` Sections 14.1-14.3; `docs/TYPES.md` Section 8.4; `docs/CONTRACT.md` K-MCP-1 |
> | DEL-09-02-RQ-008 | Validation for path and instruction-root hooks MUST confirm active project-root containment, instruction-root write denial, initial symlink-write rejection, and fail-closed behavior for write, shell, domain, and subagent actions. | `docs/SPEC.md` Section 15.2; `docs/CONTRACT.md` K-HOOK-1, K-PATH-2, K-PATH-3 |
> | DEL-09-02-RQ-009 | Validation for tool result budgets MUST confirm large or sensitive tool results are budgeted, previewed, stored as artifacts, or redacted according to policy. | `docs/CONTRACT.md` K-EVENT-7; `docs/PRD.md` FR-096 |
> | DEL-09-02-RQ-010 | Validation for compaction MUST confirm compaction boundaries are persisted when available and replay implications are recorded. | `docs/SPEC.md` Section 15.2; `docs/TYPES.md` Section 8.5; `docs/PRD.md` FR-098, FR-099 |
> | DEL-09-02-RQ-011 | Validation for subagent governance MUST confirm subagent delegation fails closed unless governance gates pass, child capabilities do not expand parent permissions, and child run records/artifact references are produced when execution is enabled. | `docs/CONTRACT.md` K-SUBAGENT-1 through K-SUBAGENT-3; `docs/PRD.md` FR-101, FR-102 |
> | DEL-09-02-RQ-012 | Harness runner updates MUST preserve existing Section 8 validation coverage while adding Section 9 IDs as runtime phases land. | `docs/PRD.md` Sections 12.3-12.4; `docs/SPEC.md` Sections 19.2-19.3 |
> | DEL-09-02-RQ-013 | The summary schema MUST identify Section 9 validation outcomes distinctly enough to support validation review. The selected schema records `status`, `testCount`, and per-ID `results`; the release-quality wrapper validates consistency for that schema. | `_CONTEXT.md`; `docs/PRD.md` Section 12.4; ADQ-14 implementation evidence |
> | DEL-09-02-RQ-014 | Section 9 remains report-only. Each landed ID MUST carry pass/fail status and evidence; no unlanded phase may be reported as passing. Pending/skipped/blocked/gated enum extension is deferred until a non-landed phase exists. | `docs/PRD.md` Section 12.4; `docs/SPEC.md` Section 19.3; D-APP-56 R4-P23 |
> | DEL-09-02-RQ-015 | The registry or manifest evidence SHOULD include each Section 9 ID, source reference, status metadata, warning/blocker notes, and evidence artifact reference when available. Current registry is `frontend/scripts/harness-section9-manifest.json`; the runner is `frontend/scripts/validate-harness-section9.mjs`. | `docs/PRD.md` Section 12.4; `docs/SPEC.md` Section 19.3; `_CONTEXT.md` Anticipated Artifacts; ADQ-14 implementation evidence |
> | DEL-09-02-RQ-016 | Section 9 fixture coverage SHOULD distinguish current Codex/Runtime engine, full events/replay/redaction, effective-home separation, user-selected policy, applicable application tools, tool-result budgets, compaction and child lineage from retained SDK mapper/settings/overlay/hook compatibility fixtures. Current fixture paths are listed in `frontend/scripts/harness-section9-manifest.json`. | `docs/CONTRACT.md` Sections 1.4-1.6; `docs/SPEC.md` Sections 9, 10, 14, 15, 19.3; ADQ-14 implementation evidence |
>

### CLM-011 — Standards

> ##### Standards
>
> | Standard / Contract | Applicability |
> |---|---|
> | `docs/CONTRACT.md` K-ENGINE, K-SDK, K-EVENT, K-PERM, K-TOOL, K-MCP, K-HOOK, K-PATH, K-SUBAGENT | Governs invariant-level validation targets. |
> | `docs/SPEC.md` Sections 9, 10, 14, 15, 19.3 | Governs event schema, runtime engine contract, MCP names, permissions/hooks, and Section 9 validation IDs. |
> | `docs/TYPES.md` Sections 7.3, 8.4, 8.5 | Governs type targets and vocabulary for events, MCP names, and hook terms. |
> | `docs/PRD.md` Sections 8.12-8.16 and 12.4 | Governs product requirements for runtime boundaries and validation additions. PRD historical D-APP-38 source state; verify current candidate bytes status applies. — reconciled under D-APP-38 |
>

### CLM-012 — Verification

> Use the accepted requirement and verification contract in CLM-024 and frontend/scripts/harness-section9-manifest.json. Selected implementation modules, result schemas and test hooks are evidence, not unresolved naming decisions or fresh pass results. Record the candidate, actual command/result paths, checked source basis, and live Runtime/Codex versus retained compatibility reach. Preserve every requirement in the requirement table; missing tests, native results and consumer wiring remain explicit work in Remaining. D-APP-38 source statements are historical; verify current source bytes and retain any mismatch/bypass. Earlier P3 path/schema slots and four-file record lists are superseded by the current ScopeOfWork representation and named evidence. This record grants no product, scope, lifecycle or release acceptance.

### CLM-013 — Documentation

> ##### Documentation
>
> Required deliverable artifacts:
>
> - Section 9 validation ID registry or equivalent manifest.
> - Harness runner changes that execute/report the Section 9 IDs.
> - Summary schema or fixture update showing Section 9 results.
> - ADQ-14 evidence: `execution/PKG-09_Validation_Packaging_Security_and_Release/1_Working/Evidence_ADQ-14_Release_Quality_Validation_Wrapper.md`.
> - Test fixtures for event log, permissions, MCP, hooks, compaction, and subagent governance where implementation exists.
> - Human-facing notes for any IDs marked pending because their runtime phase has not landed.
> - Section 8 preservation evidence or premerge summary reference alongside new Section 9 outcomes.
> - REF-006 was MATCH in the dated D-APP-38 reconciliation; current reliance requires verification of the candidate source bytes.
>

### CLM-014 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-143 records the landed `harness-section9-manifest.json` and stable artifacts manifest. UPD-144 records the ruled domain-profile ID as registered and validated within the in-process read-evidence fence.

- **AC-001** — Every Section 9 runtime validation ID enumerated by PRD Section 12.4 and SPEC Section 19.3 appears with explicit status and evidence, the Section 8 baseline remains visible, and no unlanded runtime phase is reported as passing.

## Production and Verification Method — Praxeology

### CLM-015 — Procedure: DEL-09-02 Section 9 Runtime Validation Additions

> #### Procedure: DEL-09-02 Section 9 Runtime Validation Additions
>
> > **D-APP-56 / D-APP-38 historical source note (2026-07-12):** REF-006 `docs/PRD.md` was recorded as `MATCH` in that reconciliation snapshot. This is historical evidence, not a current hash result. Before reliance, verify the candidate source bytes through `execution/_Scripts/references_hash_tool.py`; retain mismatch or authorized bypass evidence without inferring a corpus re-pin.
>

### CLM-016 — Purpose

> ##### Purpose
>
> Define the operational steps to produce and verify the Section 9 runtime validation additions for DEL-09-02 while preserving source-grounding, existing Section 8 behavior, and deliverable-local boundaries.
>

### CLM-017 — Prerequisites

> ##### Prerequisites
>
> - `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available in the deliverable folder.
> - Authoritative source slices are available from `docs/PRD.md`, `docs/SPEC.md`, `docs/CONTRACT.md`, `docs/TYPES.md`, `docs/DIRECTIVE.md`, and the v3.2 software decomposition.
> - Declared upstream and downstream dependencies remain `TBD`; an extracted dependency register exists, but do not compute blocked/available state until project-level FULL_GRAPH closure has been checked.
> - D-APP-38 source results are historical; verify the current candidate bytes.
> - Responsible party remains `TBD`.
>

### CLM-018 — Steps

> Use the accepted requirement and verification contract in CLM-024 and frontend/scripts/harness-section9-manifest.json. Selected implementation modules, result schemas and test hooks are evidence, not unresolved naming decisions or fresh pass results. Record the candidate, actual command/result paths, checked source basis, and live Runtime/Codex versus retained compatibility reach. Preserve every requirement in the requirement table; missing tests, native results and consumer wiring remain explicit work in Remaining. D-APP-38 source statements are historical; verify current source bytes and retain any mismatch/bypass. Earlier P3 path/schema slots and four-file record lists are superseded by the current ScopeOfWork representation and named evidence. This record grants no product, scope, lifecycle or release acceptance.

### CLM-019 — Verification

> ##### Verification
>
> | Check | Expected Evidence |
> |---|---|
> | ID completeness | Every ID listed in PRD Section 12.4 / SPEC Section 19.3 appears in the Section 9 registry or summary. |
> | ID status honesty | Every Section 9 ID has explicit status metadata; unimplemented runtime phases are pending, skipped, blocked, or gated rather than pass. |
> | Section 8 preservation | Existing Section 8 checks remain present and runnable. |
> | Engine contract | Current conformance evidence proves the App-owned stock Codex/Runtime boundary, supported additive inputs, complete event intake and answered server requests; retained SDK adapters are compatibility evidence. |
> | Event schema and replay | JSONL event test proves append order, unique IDs, redaction, artifact references, malformed-tail tolerance, and terminal outcomes. |
> | Configuration and authentication | Verify effective shared Codex configuration/resources remain available and authentication stays Chirality-private and Codex-custodied; historical SDK `settingSources` isolation is not the current requirement. |
> | Policy and application authority | Verify the user-selected Codex approval/sandbox policy is preserved and faithfully surfaced, with actual host enforcement reported; separately test project truth, human-only governed decisions, instruction integrity and application-tool validation. Historical `allowedTools`/deny-overlay tests do not establish current enforcement. |
> | Application tools and event hooks | Current Runtime application-tool checks prove applicable input/path/domain validation, redaction, event logging and fail-closed behavior without vetoing the user's Codex configuration or native tools. Retained MCP wrappers are labelled by actual compatibility reach. |
> | Compaction and subagents | Current Codex notification/request and Runtime record checks prove available compaction and native/managed child lineage are preserved, unfamiliar notifications are retained, server requests are answered and each turn has exactly one durable noncontradictory terminal outcome. Missing current native evidence remains explicit. |
> | Summary schema | Stable summary artifact includes Section 9 ID status and test-file evidence references; release-quality wrapper consistency check passes. |
> | Source warnings and dependency closure | Bind current authority corpus checks and current graph evidence; retain dated prior warnings as history and report actual current mismatches or unresolved relationships without inventing a new owner vote. |
>

### CLM-020 — Records

> Use the accepted requirement and verification contract in CLM-024 and frontend/scripts/harness-section9-manifest.json. Selected implementation modules, result schemas and test hooks are evidence, not unresolved naming decisions or fresh pass results. Record the candidate, actual command/result paths, checked source basis, and live Runtime/Codex versus retained compatibility reach. Preserve every requirement in the requirement table; missing tests, native results and consumer wiring remain explicit work in Remaining. D-APP-38 source statements are historical; verify current source bytes and retain any mismatch/bypass. Earlier P3 path/schema slots and four-file record lists are superseded by the current ScopeOfWork representation and named evidence. This record grants no product, scope, lifecycle or release acceptance.

- **VER-001** — Run the harness premerge validation and inspect its manifest and summary evidence for Section 8 preservation, complete Section 9 ID coverage, explicit per-ID status and evidence, and absence of false passing outcomes for unlanded phases.

## Governing Values and Decisions — Axiology

### CLM-021 — Guidance: DEL-09-02 Section 9 Runtime Validation Additions

> #### Guidance: DEL-09-02 Section 9 Runtime Validation Additions
>
> > **D-APP-56 / D-APP-38 historical source note (2026-07-12):** REF-006 `docs/PRD.md` was recorded as `MATCH` in that reconciliation snapshot. This is historical evidence, not a current hash result. Before reliance, verify the candidate source bytes through `execution/_Scripts/references_hash_tool.py`; retain mismatch or authorized bypass evidence without inferring a corpus re-pin.
>

### CLM-022 — Purpose

> ##### Purpose
>
> This deliverable turns the vNext runtime-governance requirements into Section 9 validation coverage. Its purpose is to expose candidate-bound coverage and gaps as the App-owned Runtime/Codex path changes. Contracts, complete event records and actual tests establish the checked boundary; a named phase or retained SDK test does not establish current release readiness.
>

### CLM-023 — Principles

> ##### Principles
>
> - Validate product-owned contracts, not SDK implementation details. SDK names, sessions, transcripts, hooks, and messages may appear as adapter metadata, but Chirality `UIEvent`, `HarnessEvent`, permission, session, and governance contracts remain authoritative. Source: `docs/SPEC.md` Sections 9-10; `docs/CONTRACT.md` K-ENGINE-4.
> - Adapter metadata is acceptable only when it helps prove or diagnose Chirality-owned behavior. SDK transcripts, sessions, hooks, and message names remain secondary unless imported into `HarnessEvent` form or mapped through product-owned APIs, which preserves release evidence under Chirality contracts rather than SDK-shaped truth. Source: `docs/CONTRACT.md` K-ENGINE-4 and K-SDK-3; `docs/SPEC.md` Sections 9-10.
> - Keep Section 8 stable while Section 9 expands. Section 9 additions should not regress server reachability, session CRUD, boot taxonomy, stream ordering, persistence/resume, permissions markers, interrupts, or SDK-native stream handling. Source: `docs/PRD.md` Sections 12.3-12.4.
> - Prefer explicit pending states over false pass/fail results for runtime phases that have not landed. Source: PRD Section 12.4 states IDs are added "as runtime phases land"; domain-profile validation is conditional on governed amendment.
> - Verify current source bytes and preserve actual mismatch or authorized bypass evidence; the original warning remains historical.
> - Keep `ResponsibleParty` as `TBD` until a human assigns ownership. Source: `_CONTEXT.md` Source Authority.
>

### CLM-024 — Considerations

> The landed Section 9 contract uses pass/fail per-ID results, `status`, `testCount` and `results` under D-APP-56 R4-P23. Do not claim unlanded or unexecuted coverage as passing. Registry and fixture mapping: `frontend/scripts/harness-section9-manifest.json`; runner: `frontend/scripts/validate-harness-section9.mjs`; commands: `harness:validate:section9` and `validate:release-quality`; summaries under `frontend/artifacts/harness/section9/` and `release-quality/`.
>
> Map each surviving correctness, event, replay, application-tool, protection, budget, compaction and class-aware delegation obligation to actual live Codex/Runtime evidence and S-1–S-8 where relevant. Reuse valid checks; run missing distinct checks without treating the full legacy suite as either mandatory live equivalence or a waiver. Domain validation remains bounded by its accepted stage. Additional status enums remain deferred rather than a current schema naming dispute.

### CLM-025 — Trade-offs

> Use the accepted requirement and verification contract in CLM-024 and frontend/scripts/harness-section9-manifest.json. Selected implementation modules, result schemas and test hooks are evidence, not unresolved naming decisions or fresh pass results. Record the candidate, actual command/result paths, checked source basis, and live Runtime/Codex versus retained compatibility reach. Preserve every requirement in the requirement table; missing tests, native results and consumer wiring remain explicit work in Remaining. D-APP-38 source statements are historical; verify current source bytes and retain any mismatch/bypass. Earlier P3 path/schema slots and four-file record lists are superseded by the current ScopeOfWork representation and named evidence. This record grants no product, scope, lifecycle or release acceptance.

### CLM-026 — Examples

> ##### Examples
>
> Example validation record shape, ASSUMPTION based on anticipated "summary schema":
>
> ```json
> {
>   "id": "section9.permission_overlay_hard_deny_precedence",
>   "status": "TBD",
>   "evidence": [],
>   "source": "docs/PRD.md Section 12.4; docs/CONTRACT.md K-PERM-1"
> }
> ```
>
> Example gating note for conditional domain validation:
>
> ```json
> {
>   "id": "section9.domain_profile_validation",
>   "status": "pending_governed_amendment",
>   "reason": "PRD Section 12.4 scopes this after a governed domain-profile amendment enters scope."
> }
> ```
>

### CLM-027 — Conflict Table (for human ruling)

> CONFLICT-001 is the historical D-APP-38 source-state issue; current reliance requires actual hash verification. CONFLICT-002 is narrowed by the ruled staged domain surface and report-only pass/fail contract (D-APP-56 R4-P23): a fixture result does not activate gated domain behavior. CONFLICT-003 must be read against the existing Dependencies.csv and accepted closure pointer, not an old absent-register assumption. No dependency satisfaction is changed here. Missing live-path validation and the class-aware V3-01 families remain delivery work.

### CLM-028 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-143 records the landed `harness-section9-manifest.json` and stable artifacts manifest. UPD-144 records the ruled domain-profile ID as registered and validated within the in-process read-evidence fence.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-036 SOW-037 SOW-039 SOW-045 SOW-054 SOW-057 SOW-063 OBJ-002 OBJ-003 OBJ-005 OBJ-007 OBJ-008 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
