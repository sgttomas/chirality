---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-09-03
package_id: PKG-09
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-011, SOW-012, SOW-014, SOW-015, SOW-022, SOW-028, SOW-029]
package_objective_refs: [OBJ-002, OBJ-003, OBJ-006, OBJ-008]
---

# Scope of Work — DEL-09-03

## Purpose and Objective Traceability

This Scope of Work defines `DEL-09-03` in service of project scope [SOW-011, SOW-012, SOW-014, SOW-015, SOW-022, SOW-028, SOW-029] and package objectives [OBJ-002, OBJ-003, OBJ-006, OBJ-008].

- **OUT-001** — A focused unit, API, and integration test expansion with fixtures and regression cases for TurnEngine, SSE compatibility, event replay, attachments, status lifecycle, dependencies, interrupts/cancellation, and denied actions, plus recorded behavior-group coverage decisions and validation evidence.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-09-03 Unit and Integration Test Expansion

> #### Datasheet: DEL-09-03 Unit and Integration Test Expansion
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-09-03 |
> | DeliverableName | Unit and Integration Test Expansion |
> | PackageID | PKG-09 |
> | PackageName | Validation, Packaging, Security, and Release |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | TEST_SUITE |
> | ResponsibleParty | TBD |
> | ContextEnvelope | M |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Scope | Focused unit/API/integration tests for TurnEngine, SSE, event replay, attachments, status, dependencies, interrupts, and denied actions. | `_CONTEXT.md` Deliverable Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-09 row for DEL-09-03 |
> | Anticipated artifacts | Jest/API/integration tests; fixtures; regression cases. | `_CONTEXT.md` Anticipated Artifacts |
> | Covered SOW items | SOW-011, SOW-012, SOW-014, SOW-015, SOW-022, SOW-028, SOW-029. | `_CONTEXT.md` Traceability; decomposition SOW table |
> | Supported objectives | OBJ-002, OBJ-003, OBJ-006, OBJ-008. | `_CONTEXT.md` Traceability; decomposition objective table |
> | Test command context | `npm run test` is the local unit/API test gate. | `docs/PRD.md` Section 12.2; `docs/CONTRACT.md` K-VALIDATE-1 |
> | Validation adjacency | Section 8 and Section 9 validation are adjacent validation surfaces, but this deliverable is scoped to unit/API/integration test expansion rather than authoring the Section 9 runner itself. | `docs/PRD.md` Sections 12.3-12.6; decomposition rows DEL-09-02 and DEL-09-03 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | PRD source warning | Expected PRD hash `86cb6fb9f3342c5e36e794d3f3c6316d876f519e171a7c432f1308bfeb56eb34`; observed `fb1c73f7ca54a0508e3fa2157d8b2e8af49f18ac03814aef67d762eb151c6fc8`. Treated as source status per dispatch. | `_REFERENCES.md`; TASK dispatch |
> | Dependency register output | `Dependencies.csv` must not be created by this run. Dependency extraction remains deferred until later workflow. | TASK dispatch; `_DEPENDENCIES.md` InitialPopulationRule |
> | Source-grounding rule | Unsupported facts remain `TBD`, `ASSUMPTION`, or conflict entries. | `docs/CONTRACT.md` K-INVENT-1 and K-CONFLICT-1 |
> | Lifecycle state | Initial state was `OPEN`; safe transition target after non-empty four-document initialization is `INITIALIZED`. | `_STATUS.md`; `docs/SPEC.md` Section 4 |
>

### CLM-005 — Construction

> ##### Construction
>
> | Test Area | Required Coverage Target | Source |
> |---|---|---|
> | TurnEngine lifecycle | Unit-test `TurnEngine.runTurn()` without HTTP and verify accepted-turn persistence, UI event yield, canonical event persistence, permissions/tool exposure linkage, interrupt/cancel handling, and terminal outcomes. | `docs/SPEC.md` Section 10; `docs/PRD.md` FR-070, FR-123, Section 12.5 |
> | SSE compatibility | Integration-test `/api/harness/turn` as a transport adapter that preserves browser-facing SSE event names and terminates correctly. | `docs/SPEC.md` Sections 10.4 and 11; `docs/PRD.md` Sections 9.1, 9.3, 12.6 |
> | Event replay | Test append-only `events.jsonl` serialization/replay, malformed trailing JSONL tolerance, valid-prior-event preservation, and transcript reconstruction inputs. | `docs/SPEC.md` Sections 9.1-9.4; `docs/CONTRACT.md` K-EVENT-4 and K-EVENT-5; `docs/PRD.md` FR-073, FR-076 |
> | Attachments | Test server-side attachment resolver path validation, regular-file checks, symlink rejection, extension allowlist, readability, file-size budget, total-byte budget, and partial/all-failure behavior. | `docs/SPEC.md` Section 16.1; `docs/CONTRACT.md` K-ATTACH-1; `docs/PRD.md` FR-064 |
> | Status lifecycle | Test `_STATUS.md` parser and forward-only, actor-authorized transitions including approval SHA requirements for human gates. | `docs/SPEC.md` Section 4; `docs/CONTRACT.md` K-STATUS-1 and K-STATUS-2; `docs/PRD.md` FR-052 through FR-054 |
> | Dependencies | Test `Dependencies.csv` v3.1 parser/validator/writer behavior, provenance fields, host deliverable consistency, row retirement, and legacy normalization. | `docs/SPEC.md` Section 6; `docs/CONTRACT.md` K-DEP-1, K-DEP-2, K-PROV-1; `docs/PRD.md` FR-055 through FR-057 |
> | Interrupts/cancellation | Test interrupt endpoint behavior, cancellation cleanup, lock release, and terminal cancellation/failure persistence. | `docs/PRD.md` FR-071, FR-073, Section 12.6; `docs/SPEC.md` Sections 10.1-10.2 |
> | Denied actions | Test deny precedence, `dontAsk`, `readOnly`, denied writes, denied Bash, unknown tools, hook fail-closed behavior, and permission event persistence where runtime event support exists. | `docs/SPEC.md` Sections 14-15; `docs/CONTRACT.md` K-PERM-1 through K-PERM-5, K-BASH-1, K-HOOK-1; `docs/PRD.md` FR-081, FR-087 through FR-092 |
>

### CLM-006 — References

> ##### References
>
> - `_CONTEXT.md`
> - `_REFERENCES.md`
> - `_DEPENDENCIES.md`
> - `docs/CONTRACT.md` Sections 1.5-1.9
> - `docs/SPEC.md` Sections 4, 6, 9-11, 14-16, 17
> - `docs/TYPES.md` Sections 7, 8, 12
> - `docs/PRD.md` Sections 8.9, 8.11-8.16, 9, 12.3-12.6
> - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-09 and SOW mapping rows

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-09-03 Unit and Integration Test Expansion

> #### Specification: DEL-09-03 Unit and Integration Test Expansion
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-008 — Scope

> ##### Scope
>
> DEL-09-03 shall define and implement focused unit, API, and integration test expansion for TurnEngine, SSE compatibility, event replay, attachment validation, status lifecycle behavior, dependency register behavior, interrupts/cancellation, and denied actions.
>
> This deliverable excludes feature implementation except test fixtures and packaging glue, and it shall not create or populate `Dependencies.csv` during this four-document initialization run. Source: `_CONTEXT.md` Package Scope and Deliverable Scope; decomposition row for DEL-09-03.
>

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Verification |
> |---|---|---|
> | DEL-09-03-REQ-001 | Tests shall cover `TurnEngine.runTurn()` as a product-owned lifecycle boundary, separate from HTTP route ownership. | Unit tests instantiate or exercise TurnEngine without HTTP; assertions cover accepted-turn persistence, event yield, terminal outcomes, and adapter boundary behavior. Source: `docs/SPEC.md` Section 10; `docs/PRD.md` FR-070 and Section 12.5. |
> | DEL-09-03-REQ-002 | Tests shall preserve `/api/harness/turn` SSE route compatibility, including stable browser event names. | API/integration tests assert `session:init`, `chat:delta`, `chat:complete`, `tool:result`, `session:complete`, `turn:error`, and `process:exit` behavior as applicable. Source: `docs/SPEC.md` Section 11; `docs/PRD.md` Section 9.3. |
> | DEL-09-03-REQ-003 | Tests shall verify that accepted user input is persisted before SDK/model execution begins. | Integration or unit tests assert `turn.accepted` precedes model/request execution records. Source: `docs/CONTRACT.md` K-EVENT-2; `docs/PRD.md` Sections 8.12 and 12.6. |
> | DEL-09-03-REQ-004 | Tests shall verify every accepted turn reaches a durable terminal success, failure, cancellation, or interruption event. | Tests assert terminal event persistence for success, failure, interrupt, and cancellation paths. Source: `docs/CONTRACT.md` K-EVENT-3; `docs/PRD.md` FR-073 and Section 12.6. |
> | DEL-09-03-REQ-005 | Tests shall cover append-only `HarnessEvent` JSONL replay, including malformed trailing line tolerance and preservation of valid prior events. | Unit tests write valid events plus malformed tail and assert replay diagnostics without loss of valid prior events. Source: `docs/SPEC.md` Section 9.2; `docs/CONTRACT.md` K-EVENT-5. |
> | DEL-09-03-REQ-006 | Tests shall verify attachment resolver enforcement for path validation, regular-file status, symlink rejection, extension allowlist, readability, per-file 10 MB limit, total raw-byte 18 MB limit, partial failure, and all-failure empty-text rejection. | Attachment resolver unit/API tests use fixtures for allowed file types, symlink/path failures, budget failures, partial failure, and `ATTACHMENT_FAILURE`. Source: `docs/SPEC.md` Section 16.1; `docs/CONTRACT.md` K-ATTACH-1. |
> | DEL-09-03-REQ-007 | Tests shall verify `_STATUS.md` parsing and forward-only lifecycle transition enforcement, including approval SHA requirements for `CHECKING` and `ISSUED`. | Status parser/API tests cover valid states, invalid/backward transitions, unauthorized actors, and SHA-like token requirements. Source: `docs/SPEC.md` Section 4; `docs/PRD.md` FR-052 through FR-054. |
> | DEL-09-03-REQ-008 | Tests shall verify `Dependencies.csv` v3.1 parsing, validation, writing, provenance preservation, host deliverable consistency, row retirement, and legacy normalization. | Dependency parser/writer/linter tests assert required headers, enums, `FromDeliverableID` consistency, active extracted-row evidence fields, and retired-not-deleted behavior. Source: `docs/SPEC.md` Section 6; `docs/PRD.md` FR-055 through FR-057. |
> | DEL-09-03-REQ-009 | Tests shall verify denied actions do not execute and, where runtime event support exists, emit permission/runtime events. | Permission tests cover deny-over-allow, `dontAsk`, `readOnly`, unknown tool names, denied writes, denied Bash, hook failure, and structured decisions. Source: `docs/SPEC.md` Sections 14-15; `docs/CONTRACT.md` K-PERM-1 through K-PERM-5 and K-BASH-1. |
> | DEL-09-03-REQ-010 | Tests shall keep public APIs and canonical events provider-neutral, with SDK-specific names and IDs only as adapter metadata. | Conformance tests reject SDK-shaped leakage in public APIs and canonical `HarnessEvent` fields except explicit adapter metadata. Source: `docs/SPEC.md` Section 10.3; `docs/PRD.md` FR-122 and FR-123. |
> | DEL-09-03-REQ-011 | Closure shall include at least one implemented or explicitly deferred test case for each required behavior group: TurnEngine, SSE compatibility, event replay, attachments, status lifecycle, dependencies, interrupts/cancellation, and denied actions. | Review the implemented test inventory against the eight behavior groups and record any group without executable coverage as `TBD`, deferred, or blocked with source-backed rationale. Source: `_CONTEXT.md` Deliverable Scope; `docs/PRD.md` Sections 12.5-12.6; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-09-03 row. |
> | DEL-09-03-REQ-012 | Closure shall preserve stable validation evidence for `npm run test` after implementation paths are selected. | Implementation run record or PR notes capture passing command output or a stable validation artifact; until execution occurs, command evidence remains `TBD`. Source: `docs/CONTRACT.md` K-VALIDATE-1; `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1. |
>

### CLM-010 — Standards

> ##### Standards
>
> | Standard / Source | Applicability |
> |---|---|
> | `docs/CONTRACT.md` | Binding invariants for event audit, permissions, lifecycle, dependencies, attachments, validation, and no-invention behavior. |
> | `docs/SPEC.md` | Physical file/API/runtime contracts for `_STATUS.md`, `Dependencies.csv`, `HarnessEvent`, TurnEngine, SSE, tools, permissions, and attachments. |
> | `docs/TYPES.md` | Vocabulary and canonical terms for runtime, session, permission, validation, and dependency concepts. |
> | `docs/PRD.md` | Product requirements for validation/test coverage and runtime behavior; hash status: MATCH is a source status for this run. — reconciled under D-APP-38 |
> | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Accepted decomposition routing, DEL-09-03 scope, SOW mapping, and objective mapping. |
>

### CLM-011 — Verification

> ##### Verification
>
> | Verification Item | Required Evidence |
> |---|---|
> | Unit tests | Jest or equivalent unit tests for TurnEngine, event replay, attachment resolver, status parser, dependency parser/writer/linter, permission overlay, and hook behavior. |
> | API tests | `/api/harness/turn`, `/api/harness/interrupt`, `/api/working-root/deliverable/status`, and `/api/working-root/deliverable/dependencies` route tests where implemented. |
> | Integration tests | Accepted-turn-before-execution, interrupt cancellation, SSE compatibility, denied write under `dontAsk`, denied Bash, and governed allowed-write paths when those phases are available. |
> | Regression fixtures | Files and runtime records for malformed JSONL, symlinks, budget-sized attachments, invalid dependency rows, invalid status transitions, unknown tools, and denied permission cases. |
> | Command gate | `npm run test` from `frontend/` remains passing when dependencies and required instruction-root assets are present. Source: `docs/PRD.md` Section 12.2; `docs/CONTRACT.md` K-VALIDATE-1. |
> | Closure evidence | A behavior-group coverage table, final test source paths, fixture paths, and command evidence are recorded before closure; unavailable implementation surfaces remain `TBD` or explicitly deferred. Source: DEL-09-03-REQ-011 and DEL-09-03-REQ-012. |
>

### CLM-012 — Documentation

> ##### Documentation
>
> - Test names or descriptions should cite the governing contract section or FR where practical.
> - Any unsupported implementation target remains `TBD` rather than being converted into a false requirement.
> - Test fixtures should be documented enough to distinguish source-derived requirements from assumptions.
> - ResponsibleParty remains TBD until assigned by a human.

- **AC-001** — Each named behavior group has at least one implemented test or an explicit deferral or blocker, final test and fixture paths and validation command evidence are recorded or explicitly remain TBD with a blocker, and npm run test passes when dependencies and required instruction-root assets are present.

## Production and Verification Method — Praxeology

### CLM-013 — Procedure: DEL-09-03 Unit and Integration Test Expansion

> #### Procedure: DEL-09-03 Unit and Integration Test Expansion
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-014 — Purpose

> ##### Purpose
>
> This procedure describes how to produce and verify the DEL-09-03 test expansion artifacts while preserving the bounded scope, source-grounded requirements, and deferred dependency workflow.
>

### CLM-015 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status / Note | Source |
> |---|---|---|
> | Accepted DEL-09-03 scope | Available in `_CONTEXT.md` and decomposition v3.2. | `_CONTEXT.md`; decomposition row DEL-09-03 |
> | Authoritative source corpus | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md`; TASK dispatch — reconciled under D-APP-38 |
> | Upstream dependencies | `Dependencies.csv` exists with 13 ACTIVE extracted rows and all satisfaction statuses remain `TBD`; final release-readiness review must either satisfy, waive, or explicitly defer applicable dependency evidence. | `_DEPENDENCIES.md`; `Dependencies.csv`; `_run_records/TASK_RUN_2026-05-20_2102.md` |
> | Responsible party | TBD until human assignment. | `_CONTEXT.md` Source Authority |
> | Implementation paths | TBD; exact frontend test directories/files must be identified during implementation work. | ASSUMPTION based on anticipated artifacts and `docs/PRD.md` Section 12.2 |
>

### CLM-016 — Steps

> ##### Steps
>
> 1. Confirm the current source state.
>    - Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and the DEL-09-03 decomposition row.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>
> 2. Build the test inventory.
>    - Map each test candidate to at least one source requirement or invariant.
>    - Required behavior groups: TurnEngine, SSE compatibility, event replay, attachments, status lifecycle, dependencies, interrupts/cancellation, denied actions.
>    - For closure, record at least one implemented test case, explicit deferral, or blocker for each required behavior group.
>    - Mark unavailable or phase-dependent implementation surfaces as `TBD`.
>
> 3. Create or update unit tests.
>    - Add TurnEngine lifecycle tests for `runTurn()` without HTTP.
>    - Add event replay tests for append-only JSONL, malformed trailing line tolerance, event schema shape, and terminal outcome records.
>    - Add parser/validator tests for `_STATUS.md` lifecycle and `Dependencies.csv` v3.1.
>    - Add attachment resolver and permission overlay tests using fixtures.
>
> 4. Create or update API/integration tests.
>    - Add `/api/harness/turn` SSE compatibility tests.
>    - Add `/api/harness/interrupt` cancellation cleanup tests where implementation exists.
>    - Add workspace status and dependency route tests where implementation exists.
>    - Add denied-action integration tests for `dontAsk`, read-only posture, denied writes, denied Bash, and unknown tools where implementation exists.
>
> 5. Create fixtures and regression cases.
>    - Use small named fixtures for symlink attachments, unsupported extensions, budget excess, malformed JSONL tail, invalid dependency rows, invalid status transitions, and denied tool requests.
>    - Replace fixture path `TBD`s only when actual fixture files exist; otherwise record the planned fixture class and the blocking implementation-path decision.
>    - Avoid storing secrets, API keys, or source paths that violate project-root containment.
>
> 6. Run local validation.
>    - From `frontend/`, run `npm run test`.
>    - Run `npm run typecheck` if touched test code requires TypeScript confidence or if source policy requires it for the change.
>    - Run `npm run harness:validate:premerge` only when the change affects validation surfaces or route behavior.
>
> 7. Record evidence.
>    - Capture passing command output or stable artifacts in the implementation run record or PR notes.
>    - Record final test source files, fixture files, behavior-group coverage decisions, and validation commands before closure.
>    - Do not regenerate `Dependencies.csv` from this procedure; consume the existing dependency register as review context unless a separate dependency workflow is dispatched.
>

### CLM-017 — Verification

> ##### Verification
>
> | Check | Pass Condition |
> |---|---|
> | Scope check | Tests map to DEL-09-03 behaviors and do not implement unrelated features. |
> | Source check | Non-trivial assertions cite or trace to `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PRD.md`, or decomposition v3.2. |
> | Event check | Accepted-turn, terminal, replay, and redaction tests align with product-owned `HarnessEvent` contracts. |
> | API check | SSE route tests preserve browser event names and route shape. |
> | Lifecycle check | `_STATUS.md` and `Dependencies.csv` tests follow SPEC sections 4 and 6. |
> | Permission check | Explicit hard-deny precedence is tested as an enforcement boundary, not as prompt text. |
> | Fixture check | Fixtures are deterministic, small, and free of secrets. |
> | Command check | `npm run test` passes when dependencies and required instruction-root assets are present. |
> | Closure evidence check | Test source paths, fixture paths, behavior-group coverage decisions, and command evidence are recorded, or explicitly remain `TBD` with a blocker. |
>

### CLM-018 — Records

> ##### Records
>
> - Test source files: TBD until implementation work identifies exact paths.
> - Fixtures: TBD until implementation work identifies exact paths.
> - Command evidence: TBD until implementation work runs validation.
> - Behavior-group closure: TBD until implementation work records implemented tests, explicit deferrals, or blockers for TurnEngine, SSE compatibility, event replay, attachments, status lifecycle, dependencies, interrupts/cancellation, and denied actions.
> - Dependency review evidence: existing `Dependencies.csv` contains 13 ACTIVE rows with satisfaction `TBD`; final release-readiness review must resolve or explicitly defer applicable dependency evidence.
> - Four-document initialization run record: `_run_records/TASK_RUN_2026-05-20_1619.md`.
>

### CLM-019 — Pass 3 Semantic Lensing Disposition

> ##### Pass 3 Semantic Lensing Disposition
>
> | ItemID | Disposition | Evidence / Reread |
> |---|---|---|
> | A-001 | Incorporated. | Added DEL-09-03-REQ-011 requiring one implemented or explicitly deferred test decision per required behavior group. Reread: `_CONTEXT.md` Deliverable Scope; `docs/PRD.md` Sections 12.5-12.6; decomposition DEL-09-03 row. |
> | B-001 | Incorporated as closure evidence. | Records now require final test source files, fixture files, behavior-group coverage decisions, and command evidence, or explicit `TBD` blockers. Reread: Procedure Records; `docs/PRD.md` Section 12.2. |
> | C-001 | Incorporated as prerequisite and fixture guard. | Procedure keeps implementation paths `TBD` until selected and Step 5 now blocks fixture path replacement until actual files exist. Reread: Procedure Prerequisites and Steps; `docs/PRD.md` Section 12.2. |
> | F-001 | Incorporated. | Added DEL-09-03-REQ-012 and closure-evidence verification for stable `npm run test` evidence. Reread: `docs/CONTRACT.md` K-VALIDATE-1; `docs/PRD.md` Section 12.2; `docs/SPEC.md` Section 19.1. |
> | D-001 | Already covered and preserved. | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
> | X-001 | Incorporated as closure evidence. | Records now require test source paths, fixture paths, behavior-group coverage decisions, and command evidence before determination closure, with blockers if still `TBD`. Reread: Procedure Records and Verification. |
> | E-001 | Incorporated as fixture-path guard. | Step 5 now requires actual fixture files before replacing fixture path `TBD`s for symlink, budget, malformed JSONL, dependency, status, and denied-tool cases. Reread: `docs/SPEC.md` Sections 9.2 and 16.1; `docs/PRD.md` Sections 12.5-12.6. |
> | E-002 | Incorporated with current dependency state. | Prerequisites and Records now note existing `Dependencies.csv`, 13 ACTIVE rows, and satisfaction `TBD`; final release-readiness review must resolve or explicitly defer applicable dependency evidence. Reread: `_DEPENDENCIES.md`, `Dependencies.csv`, and `_run_records/TASK_RUN_2026-05-20_2102.md`. |
>

### CLM-020 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-145 replaces closure-record TBDs with the existing GATE-TRANSCRIPT/ADQ-14 command evidence.

- **VER-001** — Review the test inventory and closure evidence against all eight named behavior groups, inspect recorded test paths, fixture paths, deferrals or blockers, and stable command evidence, and run npm run test when dependencies and required instruction-root assets are present.

## Governing Values and Decisions — Axiology

### CLM-021 — Guidance: DEL-09-03 Unit and Integration Test Expansion

> #### Guidance: DEL-09-03 Unit and Integration Test Expansion
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-022 — Purpose

> ##### Purpose
>
> DEL-09-03 exists to make the vNext runtime, lifecycle, dependency, attachment, and permission behavior testable at focused unit/API/integration levels. The deliverable supports release readiness by expanding regression coverage for the named behaviors rather than by implementing those behaviors directly.
>
> Sources: `_CONTEXT.md` Deliverable Scope; `docs/PRD.md` Sections 8.11-8.16 and 12.5-12.6; decomposition row for DEL-09-03.
>

### CLM-023 — Principles

> ##### Principles
>
> | Principle | Guidance | Source |
> |---|---|---|
> | Test product-owned contracts, not SDK defaults | Assertions should target `AgentEnginePort`, `TurnEngine`, browser `UIEvent`s, canonical `HarnessEvent`s, and permission decisions. SDK-specific values belong only in adapter metadata assertions. | `docs/SPEC.md` Section 10.3; `docs/PRD.md` FR-122 and FR-123 |
> | Preserve browser compatibility | `/api/harness/turn` tests should protect stable SSE event names and route shape while allowing runtime internals to move behind TurnEngine. | `docs/SPEC.md` Sections 10.4 and 11; `docs/PRD.md` Section 9.3 |
> | Make audit order observable | Accepted-turn persistence, terminal outcomes, replay tolerance, and redaction are audit requirements and should be asserted as ordered records where possible. | `docs/CONTRACT.md` K-EVENT-2 through K-EVENT-6 |
> | Deny paths need first-class tests | Denied writes, denied Bash, unknown tools, failed hooks, `dontAsk`, and `readOnly` are not edge cases; they are product-critical boundaries. | `docs/CONTRACT.md` K-PERM-1 through K-PERM-5, K-BASH-1, K-HOOK-1 |
> | Fixture design should expose failure mode | Attachment, dependency, status, and JSONL fixtures should be small, named by failure condition, and reusable across unit/API tests. | `docs/SPEC.md` Sections 4, 6, 9, 16 |
>

### CLM-024 — Considerations

> ##### Considerations
>
> - Prefer narrow tests around a single invariant when the invariant is explicitly source-defined, such as `_STATUS.md` forward-only transitions or `Dependencies.csv` required columns.
> - Use integration tests when behavior depends on route cleanup, session locking, SSE termination, cancellation, or multiple services.
> - Use unit tests for deterministic parsers, mappers, permission resolution, fixture validation, and event replay.
> - Keep Section 9 validation IDs aligned with DEL-09-02; this deliverable can provide underlying unit/API/integration coverage, but authoring the runner/ID catalog belongs to DEL-09-02 unless a later human ruling changes scope.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
> - Mark unimplemented or phase-dependent coverage as `TBD` or `ASSUMPTION` in planning notes rather than creating tests that assert unavailable behavior.
> - Treat missing implementation paths, fixture paths, and command output as closure evidence gaps, not as permission to invent paths. The implementation pass should replace those `TBD` values only after files and commands exist.
>

### CLM-025 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Guidance |
> |---|---|
> | Broad matrix vs focused regression cases | Favor source-mapped regression cases for the named DEL-09-03 behaviors. Exhaustive cross-product matrices can be deferred unless a source requirement demands them. |
> | Mocked engine vs real SDK adapter | Use stubs for deterministic product-owned contract tests; use SDK-backed adapter tests only where the source requirement is adapter conformance or Provider/SDK message mapping. |
> | API route tests vs service tests | Keep route tests focused on request validation, locking, SSE encoding, cleanup, and stable shape. Put runtime policy assertions in TurnEngine/permission/event tests. |
> | Current behavior vs future phase behavior | Tests for future phase behavior should be pending/TBD or fixture-ready until the corresponding implementation deliverable lands. |
> | Minimum coverage vs unavailable surfaces | Require one implemented or explicitly deferred test decision for each DEL-09-03 behavior group, but keep future-phase surfaces marked `TBD` until the owning implementation exists. |
>

### CLM-026 — Examples

> ##### Examples
>
> | Example Test / Fixture | Expected Intent | Source |
> |---|---|---|
> | `turn-engine.accepted-before-query.test` | Assert accepted input is written before model/SDK execution begins. | `docs/CONTRACT.md` K-EVENT-2; `docs/PRD.md` Section 12.6 |
> | `sse.compatibility.events.test` | Assert browser-facing SSE event names remain stable. | `docs/SPEC.md` Section 11 |
> | `session-events.malformed-tail.test` | Assert replay preserves valid prior events and reports malformed tail diagnostics. | `docs/SPEC.md` Section 9.2 |
> | `attachments.symlink-budget.test` | Assert symlink rejection and byte-budget failures are server-side. | `docs/SPEC.md` Section 16.1 |
> | `status-transition.human-gate-sha.test` | Assert `CHECKING`/`ISSUED` require approval SHA evidence and actor authorization. | `docs/SPEC.md` Section 4 |
> | `dependencies-v31.provenance.test` | Assert active extracted rows require evidence fields or explicit `location TBD`. | `docs/SPEC.md` Section 6; `docs/CONTRACT.md` K-PROV-1 |
> | `permissions.dontask-denied-write.test` | Assert denied writes do not execute under `dontAsk`. | `docs/SPEC.md` Section 15.1; `docs/PRD.md` Section 12.6 |
>

### CLM-027 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
> |---|---|---|---|---|---|---|
> | CONFLICT-001 | PRD reference hash status: MATCH: expected and observed SHA256 differ. | `_REFERENCES.md` REF-006 | TASK dispatch source-warning override | All source-grounded PRD references | Treat as source status for this run, per dispatch. | TBD — reconciled under D-APP-38 |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-011 SOW-012 SOW-014 SOW-015 SOW-022 SOW-028 SOW-029 OBJ-002 OBJ-003 OBJ-006 OBJ-008 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
