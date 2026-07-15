---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-07-04
package_id: PKG-07
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@2770fda4c63c98ee9f18cffbafd14c9aa59f497f
project_scope_refs: [SOW-028]
package_objective_refs: [OBJ-006]
---

# Scope of Work — DEL-07-04

## Purpose and Objective Traceability

This candidate defines `DEL-07-04` in service of project scope [SOW-028] and package objectives [OBJ-006].

- **OUT-001** — A canonical _STATUS.md parser and deny-first status transition API/MCP tool with actor authorization, approval-SHA gates, policy integration, schemas, and acceptance tests.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-07-04 Status Transition API and MCP Tool

> #### Datasheet: DEL-07-04 Status Transition API and MCP Tool
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-07-04 |
> | DeliverableName | Status Transition API and MCP Tool |
> | PackageID | PKG-07 |
> | PackageName | Filesystem Execution, Lifecycle, and Dependencies |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | RuntimeDispatchVariant | SOFTWARE |
> | DecompositionRevision | v3.2 |
> | Type | BACKEND_FEATURE_SLICE |
> | ResponsibleParty | TBD |
> | ContextEnvelope | M |
> | CoversScopeItems | SOW-028 |
> | SupportsObjectives | OBJ-006 |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary subject | Parse `_STATUS.md` and enforce lifecycle transitions. | `_CONTEXT.md` Deliverable Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` DEL-07-04 |
> | Canonical state source | `_STATUS.md` is the canonical lifecycle state file for each deliverable. | `docs/CONTRACT.md` Section 1.7 K-STATUS-1; `docs/SPEC.md` Section 4.3 |
> | Status file fields | Parser must read `Current State`, `Last Updated`, and history. | `docs/PRD.md` Section 8.9 FR-052; `docs/SPEC.md` Section 4.1 |
> | Valid lifecycle chain | `OPEN -> INITIALIZED -> SEMANTIC_READY -> IN_PROGRESS -> CHECKING -> ISSUED`. | `docs/SPEC.md` Section 4.2; `docs/TYPES.md` Section 4.1 |
> | Transition rule | Transitions are forward-only and actor-authorized. | `docs/PRD.md` Section 8.9 FR-053; `docs/SPEC.md` Section 4.3 |
> | Human gate evidence | Transitions to `CHECKING` or `ISSUED` require approval SHA evidence; PRD acceptance calls for a 7-64 character hex SHA-like token. | `docs/SPEC.md` Section 4.3; `docs/PRD.md` Section 8.9 FR-054 |
> | API surface | `GET /api/working-root/deliverable/status` reads status; `POST /api/working-root/deliverable/status/transition` applies allowed transition. | `docs/PRD.md` API inventory; `docs/SPEC.md` Section 13 |
> | MCP surface | `mcp__chirality__status_read` reads `_STATUS.md`; `mcp__chirality__status_transition` applies authorized lifecycle transition with approval SHA where required. | `docs/SPEC.md` Section 14.2; `docs/TYPES.md` Section 8.4 |
> | MCP boundary | MCP is a transport, not a bypass; in-process Chirality MCP tools pass through the same permission, hook, path, redaction, and event logging policy as SDK built-ins. | `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/DIRECTIVE.md` Design commitments |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Status |
> |---|---|
> | Source hash warning | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
> | Dependency inputs | `_DEPENDENCIES.md` declares no accepted upstream or downstream edges yet. |
> | Ownership | Responsible party is `TBD`; `_CONTEXT.md` says to preserve `ResponsibleParty: TBD` until human assignment. |
> | Semantic lensing | `_SEMANTIC.md` is `NOT_GENERATED`; this P1/P2 run does not use semantic lensing. |
> | Existing implementation path | TBD. Source documents define required behavior but do not name the implementation files for this slice. |
> | Variant naming note | `SOFTWARE_DECOMP` names the accepted decomposition family in this deliverable context; `SOFTWARE` is the four-documents runtime dispatch token. |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component | Expected role | Source grounding |
> |---|---|---|
> | Status parser | Read `_STATUS.md`, extract current state, last updated date, and history entries. | `docs/SPEC.md` Section 4.1; `docs/PRD.md` Section 8.9 FR-052 |
> | Transition validator | Enforce valid states, forward-only ordering, actor authorization, and approval SHA requirements for human gates. | `docs/SPEC.md` Sections 4.2-4.3; `docs/PRD.md` Section 8.9 FR-053/FR-054 |
> | Status API | Provide read and transition endpoints for deliverable status contract access. | `docs/PRD.md` API inventory; `docs/SPEC.md` Section 13 |
> | Chirality MCP tools | Expose status read/transition through in-process deterministic `mcp__chirality__*` tooling. | `docs/SPEC.md` Section 14.2; `docs/PRD.md` Section 8.13 FR-119 |
> | Tests | Cover parser behavior, actor authorization, forward-only rejection, approval SHA gate, and MCP/API routing. | `docs/PRD.md` Section 8.9 FR-052 through FR-054; decomposition DEL-07-04 anticipated artifacts |
>

### CLM-006 — References

> ##### References
>
> | RefID | SourcePath | SectionRef | Use |
> |---|---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | Human authority and design commitments | Approval and MCP boundary posture |
> | REF-002 | `docs/CONTRACT.md` | Sections 1.2, 1.6, 1.7 | Binding invariants for approvals, status, MCP wrappers |
> | REF-003 | `docs/SPEC.md` | Sections 4, 13, 14.2 | `_STATUS.md` format, lifecycle, API and MCP names |
> | REF-004 | `docs/TYPES.md` | Sections 4.1, 8.4 | Lifecycle vocabulary and MCP tool naming |
> | REF-005 | `docs/PLAN.md` | R3 implementation targets | Status transition tool target and approval SHA gate |
> | REF-006 | `docs/PRD.md` | Sections 8.9, 8.13, API inventory | Product requirements; MATCH status applies — reconciled under D-APP-38 |
> | REF-007 | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | PKG-07 DEL-07-04; SOW-028 | Scope and anticipated artifacts |
>

### CLM-007 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | ItemID | Disposition | Evidence |
> |---|---|---|
> | E-001 | Incorporated as a normalization note distinguishing the accepted decomposition family from the runtime dispatch token. | `_CONTEXT.md` Identification; `_SEMANTIC_LENSING.md` header; `skills/four-documents/SKILL.md` runtime override values. |
>

### CLM-008 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-132 names the landed status-transition and MCP modules while leaving ResponsibleParty assignment human-owned.

## Completion and Reliance Basis — Epistemology

### CLM-009 — Specification: DEL-07-04 Status Transition API and MCP Tool

> #### Specification: DEL-07-04 Status Transition API and MCP Tool
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-010 — Scope

> ##### Scope
>
> This deliverable specifies the backend slice that parses deliverable-local `_STATUS.md`, exposes status read/transition access through the working-root API and Chirality MCP tooling, and enforces lifecycle rules for state movement. The slice covers SOW-028 and supports OBJ-006 as recorded in `_CONTEXT.md` and the accepted SOFTWARE_DECOMP v3.2 entry for DEL-07-04.
>
> In scope:
>
> - `_STATUS.md` parser behavior for current state, last updated date, and history.
> - Lifecycle transition validation for valid state sequence, forward-only movement, authorized actors, and approval SHA evidence for human gates.
> - Status read and transition API contracts.
> - `mcp__chirality__status_read` and `mcp__chirality__status_transition` tool behavior.
> - Tests for parser, transition, actor authorization, approval SHA, and MCP/API exposure.
>
> Out of scope:
>
> - Dependency CSV parser/writer behavior except where status/dependency APIs share a contract surface.
> - UI presentation beyond consuming the API/tool result.
> - Remote MCP servers, plugin marketplaces, remote execution, or custom generic MCP transport.
> - Autonomous approval, issue, release, certification, or professional validation.
>

### CLM-011 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source |
> |---|---|---|
> | DEL-07-04-REQ-001 | The status parser SHALL read `_STATUS.md` as the canonical human-readable lifecycle file for a deliverable. | `docs/CONTRACT.md` Section 1.7 K-STATUS-1; `docs/SPEC.md` Section 4.3 |
> | DEL-07-04-REQ-002 | The parser SHALL extract `Current State`, `Last Updated`, and history entries from the `_STATUS.md` format. | `docs/SPEC.md` Section 4.1; `docs/PRD.md` Section 8.9 FR-052 |
> | DEL-07-04-REQ-003 | The validator SHALL recognize the lifecycle order `OPEN -> INITIALIZED -> SEMANTIC_READY -> IN_PROGRESS -> CHECKING -> ISSUED`. | `docs/SPEC.md` Section 4.2; `docs/TYPES.md` Section 4.1 |
> | DEL-07-04-REQ-004 | The validator SHALL reject backward transitions unless a human explicitly amends the record. | `docs/SPEC.md` Section 4.3; `docs/PRD.md` Section 8.9 FR-053 |
> | DEL-07-04-REQ-005 | The validator SHALL enforce actor authorization for lifecycle transitions according to SPEC Section 4.3. | `docs/SPEC.md` Section 4.3; `docs/PRD.md` Section 8.9 FR-053 |
> | DEL-07-04-REQ-006 | Transitions to `CHECKING` or `ISSUED` SHALL require approval SHA evidence; the PRD acceptance criterion is a 7-64 character hex SHA-like token. | `docs/SPEC.md` Section 4.3; `docs/PRD.md` Section 8.9 FR-054 |
> | DEL-07-04-REQ-007 | The implementation SHALL expose a status read API at `GET /api/working-root/deliverable/status`. | `docs/PRD.md` API inventory; `docs/SPEC.md` Section 13 |
> | DEL-07-04-REQ-008 | The implementation SHALL expose a status transition API at `POST /api/working-root/deliverable/status/transition`. | `docs/PRD.md` API inventory; `docs/SPEC.md` Section 13 |
> | DEL-07-04-REQ-009 | The implementation SHALL expose `mcp__chirality__status_read` and `mcp__chirality__status_transition` as Chirality MCP tool names. | `docs/SPEC.md` Section 14.2; `docs/TYPES.md` Section 8.4 |
> | DEL-07-04-REQ-010 | `mcp__chirality__status_transition` SHALL be write-gated and SHALL apply authorized lifecycle transitions with approval SHA where required. | `docs/SPEC.md` Section 14.2; `docs/CONTRACT.md` Section 1.7 K-STATUS-2 |
> | DEL-07-04-REQ-011 | Chirality MCP status tools SHALL pass through the same permission, hook, path, redaction, and event logging policy as SDK built-ins. | `docs/CONTRACT.md` Section 1.6 K-MCP-1; `docs/PRD.md` Section 8.13 FR-119 |
> | DEL-07-04-REQ-012 | Deny-first behavior SHALL be preserved for status transitions; denial from policy, path check, hook, governance, SDK deny rule, or human gate blocks execution. | `docs/CONTRACT.md` Section 1.6 K-PERM-1; `docs/DIRECTIVE.md` Design commitments |
> | DEL-07-04-REQ-013 | Status transition behavior SHALL NOT create or imply binding approval records by an agent, SDK, tool, runtime event, validator, or domain adapter. | `docs/CONTRACT.md` Section 1.2 K-AUTH-1/K-BIND-1; `docs/DIRECTIVE.md` Human authority |
> | DEL-07-04-REQ-014 | Approval evidence SHALL bind to specific content, normally a git SHA or equivalent immutable evidence; content changes after approval void approval until review. | `docs/DIRECTIVE.md` Human authority; `docs/CONTRACT.md` Section 1.2 K-AUTH-2 |
> | DEL-07-04-REQ-015 | Tests SHALL cover parser success/failure, invalid state handling, unauthorized actor rejection, backward transition rejection, approval SHA enforcement, and API/MCP routing. | `docs/PRD.md` Section 8.9 FR-052 through FR-054; decomposition DEL-07-04 anticipated artifacts |
> | DEL-07-04-REQ-016 | Request and response payload schemas for status read, status transition, and MCP equivalents SHALL be captured as accepted schema fixtures before implementation acceptance; until accepted, exact fields remain `TBD`. | `docs/SPEC.md` Sections 13 and 14.2; `docs/PRD.md` API inventory; `docs/PRD.md` FR-079 |
> | DEL-07-04-REQ-017 | Runtime actor identity mapping SHALL be explicit and fail closed for unmapped actors before transition authorization is treated as complete. The accepted human-gate string aliases are exactly `HUMAN`, `USER`, and `OPERATOR`; arbitrary `HUMAN*` prefixes are unmapped and MUST fail with `UNAUTHORIZED_ACTOR`. | `docs/SPEC.md` Section 4.3; `docs/CONTRACT.md` K-STATUS-2; D-APP-56 R4-P19 |
> | DEL-07-04-REQ-018 | PRD-derived approval-SHA acceptance criteria SHALL NOT be treated as final implementation acceptance authority until the `docs/PRD.md` hash status: MATCH is reconciled or a human-approved bypass record is accepted. | `_REFERENCES.md` REF-006; `docs/SPEC.md` Section 3.1 file inventory for `HASH_VERIFICATION_BYPASS.jsonl`; `docs/SPEC.md` Section 7 reference hash behavior — reconciled under D-APP-38 |
>

### CLM-012 — Standards

> ##### Standards
>
> | Standard or source | Applicability |
> |---|---|
> | `docs/SPEC.md` Section 4 | Governs `_STATUS.md` format, lifecycle states, and transition rules. |
> | `docs/SPEC.md` Sections 13 and 14.2 | Governs status API and Chirality MCP tool names. |
> | `docs/CONTRACT.md` K-STATUS-1/K-STATUS-2 | Binding invariants for canonical status state and transition enforcement. |
> | `docs/CONTRACT.md` K-MCP-1/K-PERM-1 | Binding invariants for MCP wrapper and deny-first behavior. |
> | `docs/PRD.md` Section 8.9 | Product requirements for lifecycle and dependency contracts; MATCH status applies. — reconciled under D-APP-38 |
> | `docs/TYPES.md` Section 4.1 | Defines lifecycle vocabulary and optional `INITIALIZED -> IN_PROGRESS` route when semantic lensing is skipped. |
>

### CLM-013 — Verification

> ##### Verification
>
> | Requirement IDs | Verification approach |
> |---|---|
> | REQ-001, REQ-002 | Unit tests parse representative `_STATUS.md` files and return current state, last updated date, and history. |
> | REQ-003, REQ-004 | Unit tests accept forward movement and reject backward or unknown-state transitions. |
> | REQ-005, REQ-006 | Unit/API tests check authorized actors and require valid SHA-like approval evidence for `CHECKING` and `ISSUED`. |
> | REQ-007, REQ-008 | API route tests verify request validation, status snapshot response, transition success, and transition denial results. |
> | REQ-009, REQ-010 | MCP tool tests verify names, schemas, read/write mode, and gated transition behavior. |
> | REQ-011, REQ-012 | Integration tests verify permission overlay, hook/path denials, and event logging behavior for MCP status operations. |
> | REQ-013, REQ-014 | Tests or review checks verify output copy and event records do not present tool or agent actions as human approval. |
> | REQ-015 | Test suite includes the anticipated artifacts from decomposition: status parser tests, transition API/tool tests, and approval SHA tests. |
> | REQ-016 | Schema fixture tests cover status snapshot response, transition request, transition success response, transition denial response, and MCP input/output schemas after the accepted schemas exist. |
> | REQ-017 | Actor authorization tests cover every SPEC Section 4.3 authorized transition plus unmapped/unsupported actor denial. |
> | REQ-018 | Acceptance checklist verifies the PRD hash status: MATCH has been reconciled or explicitly bypassed before relying on PRD-specific SHA-token criteria as final. — reconciled under D-APP-38 |
> | REQ-004, REQ-005, REQ-006, REQ-011, REQ-012 | Denial fixtures assert typed reasons for invalid state, backward transition, unauthorized actor, missing approval SHA, invalid approval SHA, policy/path denial, and malformed `_STATUS.md`. |
>

### CLM-014 — Documentation

> ##### Documentation
>
> Required artifacts:
>
> - Status parser.
> - Transition API/tool.
> - Approval SHA tests.
> - MCP tool contract notes or schema fixtures.
> - API contract tests for status read/transition.
> - Permission/hook/path policy tests for write-gated transition behavior.
> - PRD hash reconciliation or approved hash-bypass evidence before final PRD-derived acceptance claims.
>
> TBD:
>
> - Implementation module paths.
> - Exact request/response payload schemas for the status API and MCP tools.
> - Exact actor identity enum or policy mapping used by runtime callers.
> - Exact success and denial payload field names until schema fixtures are accepted.
>

### CLM-015 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | ItemID | Disposition | Evidence |
> |---|---|---|
> | B-001 | Converted to explicit `TBD` schema-fixture requirement rather than invented payload fields. | `docs/SPEC.md` Sections 13 and 14.2; `docs/PRD.md` FR-079. |
> | B-002 | Converted to explicit `TBD` actor-mapping requirement with fail-closed behavior. | `docs/SPEC.md` Section 4.3; `docs/CONTRACT.md` K-STATUS-2. |
> | F-001 | Incorporated as a PRD hash reconciliation acceptance check. | `_REFERENCES.md` REF-006; `docs/SPEC.md` Section 3.1 and reference-hash behavior. |
> | F-002 | Incorporated as schema fixture verification after schemas are accepted. | `docs/SPEC.md` Sections 13 and 14.2; `docs/PRD.md` FR-079. |
> | X-001 | Incorporated as denial-reason fixture coverage. | `docs/CONTRACT.md` K-PERM-1/K-MCP-1/K-STATUS-2; `docs/SPEC.md` Sections 4.1-4.3. |
>

### CLM-016 — Source Status

> ##### Source Status
>
> `docs/PRD.md` is listed as `MATCH` in `_REFERENCES.md`. Requirements using PRD clauses are retained because the source is locally accessible and explicitly listed, but the MATCH should be reconciled before treating PRD-derived acceptance details as final implementation authority. (reconciled under D-APP-38).

- **AC-001** — Status reads preserve canonical lifecycle fields; transitions follow the defined forward order, reject unknown, backward, or unauthorized actions, require exact human aliases and approval SHA evidence at human gates, and never represent tool or agent activity as human approval.

## Production and Verification Method — Praxeology

### CLM-017 — Procedure: DEL-07-04 Status Transition API and MCP Tool

> #### Procedure: DEL-07-04 Status Transition API and MCP Tool
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-018 — Purpose

> ##### Purpose
>
> Define the working procedure to produce and verify the DEL-07-04 backend feature slice for status parsing, status transition enforcement, API exposure, and Chirality MCP tool exposure.
>

### CLM-019 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status |
> |---|---|
> | Accepted scope entry for DEL-07-04 | Available in `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`. |
> | Authoritative lifecycle contract | Available in `docs/SPEC.md` Section 4 and `docs/CONTRACT.md` Section 1.7. |
> | API/MCP contract references | Available in `docs/SPEC.md` Sections 13 and 14.2 and `docs/PRD.md` API inventory. |
> | Permission/MCP boundary references | Available in `docs/CONTRACT.md` Section 1.6 and `docs/DIRECTIVE.md` design commitments. |
> | Declared upstream dependencies | TBD; `_DEPENDENCIES.md` lists no accepted upstream edges yet. |
> | Implementation module location | TBD; implementation owner must identify accepted module paths for working-root status APIs and Chirality MCP tools before implementation closeout. |
> | Accepted schema fixtures | TBD; exact request/response fields remain unresolved until API and MCP schema fixtures are accepted. |
>

### CLM-020 — Steps

> ##### Steps
>
> 1. Locate the implementation area for working-root deliverable APIs and Chirality MCP tools.
>    - If no established location exists, record candidate module paths as `TBD` until accepted by the responsible implementer.
>
> 2. Implement or update the `_STATUS.md` parser.
>    - Parse the SPEC Section 4.1 fields: title, `Current State`, `Last Updated`, and history.
>    - Reject or report malformed files without inferring lifecycle state from other files.
>
> 3. Implement lifecycle state validation.
>    - Recognize `OPEN`, `INITIALIZED`, `SEMANTIC_READY`, `IN_PROGRESS`, `CHECKING`, and `ISSUED`.
>    - Enforce the forward-only ordering from SPEC Section 4.2.
>    - Include the TYPES Section 4.1 optional route from `INITIALIZED` to `IN_PROGRESS` when semantic lensing is skipped, subject to authorized actor rules.
>
> 4. Implement actor authorization.
>    - Use the authorized actor table in SPEC Section 4.3 as the baseline.
>    - Preserve `TBD` for exact runtime actor identity mapping until the implementation surface defines caller identities.
>
> 5. Implement human gate approval SHA checks.
>    - Require approval SHA evidence for transitions to `CHECKING` or `ISSUED`.
>    - Apply the PRD Section 8.9 FR-054 acceptance detail: 7-64 character hex SHA-like token. PRD hash status: MATCH status applies. (reconciled under D-APP-38).
>
> 6. Implement the status API surface.
>    - Provide `GET /api/working-root/deliverable/status` for read-only status snapshots.
>    - Provide `POST /api/working-root/deliverable/status/transition` for allowed lifecycle transitions.
>    - Return structured success and denial outcomes. Exact response schema is `TBD`.
>    - After schema acceptance, add fixtures for status snapshot responses, transition requests, transition success responses, and transition denial responses.
>
> 7. Implement the Chirality MCP status tools.
>    - Provide `mcp__chirality__status_read` for reading `_STATUS.md`.
>    - Provide `mcp__chirality__status_transition` for write-gated status transitions.
>    - Route MCP execution through the same permission, hook, path, redaction, and event logging policy as SDK built-ins.
>    - Record test evidence for permission decisions, path containment, hook outcomes, redaction behavior, and tool/runtime event logging for status operations.
>
> 8. Add tests for the deliverable acceptance surface.
>    - Parser tests for valid and malformed `_STATUS.md`.
>    - Transition tests for valid forward moves, invalid states, backward moves, unauthorized actors, missing approval SHA, and invalid SHA-like token.
>    - API route tests for read and transition.
>    - MCP tool tests for naming, schema, read/write mode, denial, and success.
>    - Permission/path/hook tests for gated writes.
>    - Denial payload tests for invalid state, backward transition, unauthorized actor, missing approval SHA, invalid approval SHA, path/policy denial, and malformed `_STATUS.md`.
>    - Success payload tests once accepted field names exist.
>
> 9. Record unresolved implementation details.
>    - Keep `TBD` for exact module paths, request/response schemas, and actor identity mapping until accepted by implementation owners or adjacent deliverables.
>

### CLM-021 — Verification

> ##### Verification
>
> | Check | Expected result |
> |---|---|
> | Parser fixture: valid `_STATUS.md` | Current state, last updated date, and history are returned. |
> | Parser fixture: malformed `_STATUS.md` | Structured error is returned; no alternate file determines lifecycle state. |
> | Transition fixture: forward authorized transition | Transition succeeds when policy/path checks pass. |
> | Transition fixture: backward transition | Transition fails unless an explicit human amendment path exists. |
> | Transition fixture: `CHECKING` or `ISSUED` without approval SHA | Transition fails. |
> | Transition fixture: `CHECKING` or `ISSUED` with invalid SHA-like token | Transition fails under PRD FR-054 acceptance. |
> | API tests | Status read and transition endpoints behave consistently with parser/validator. |
> | MCP tests | `mcp__chirality__status_read` and `mcp__chirality__status_transition` expose deterministic Chirality operations and preserve policy overlays. |
> | Boundary tests | Status transition does not imply human approval, professional validation, issue, or release. |
> | Schema fixture tests | After schemas are accepted, exact request/response fixtures cover API and MCP read, transition success, and transition denial. |
> | Audit overlay tests | Permission, hook, path-containment, redaction, and event logging evidence exists for MCP status operations. |
>

### CLM-022 — Records

> ##### Records
>
> Expected records and artifacts:
>
> - Status parser implementation.
> - Transition validator implementation.
> - Status API route or service tests.
> - Chirality MCP status tool definitions and tests.
> - Approval SHA test fixtures.
> - Denial/success fixtures for actor authorization and forward-only lifecycle behavior.
> - Runtime/event logging evidence for write-gated status transitions when the implementation surface supports it.
> - Permission decision, hook outcome, path-containment, redaction, and event logging evidence for MCP status operations.
> - PRD hash reconciliation or approved bypass evidence before final PRD-derived acceptance claims.
>
> TBD records:
>
> - Exact implementation file paths.
> - Exact request/response schemas.
> - Exact actor identity mapping.
> - Exact success and denial payload fields.
>

### CLM-023 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | ItemID | Disposition | Evidence |
> |---|---|---|
> | D-001 | Converted to an explicit prerequisite and closeout blocker: accepted implementation module paths remain `TBD`. | `_DEPENDENCIES.md` DEP-07-04-008; decomposition DEL-07-04 anticipated artifacts. |
> | F-002 | Incorporated as post-schema fixture verification for API/MCP request and response schemas. | `docs/SPEC.md` Sections 13 and 14.2; `docs/PRD.md` FR-079. |
> | X-002 | Incorporated as audit evidence expectations for permission, hook, path, redaction, and event logging policy on MCP status operations. | `docs/CONTRACT.md` K-MCP-1/K-PERM-1; `docs/PRD.md` FR-092, FR-093, FR-104. |
> | E-002 | Converted to explicit `TBD` success/denial payload fields until schema acceptance. | `docs/SPEC.md` API inventory; `docs/PRD.md` FR-079 and NFR-009. |
>

### CLM-024 — Source Status

> ##### Source Status
>
> `docs/PRD.md` is listed as `MATCH` in `_REFERENCES.md`; reconcile the source hash before final acceptance of PRD-derived acceptance details. (reconciled under D-APP-38).
>

### CLM-025 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-132 names the landed status-transition and MCP modules while leaving ResponsibleParty assignment human-owned.

- **VER-001** — Run the source-defined parser, transition, actor-mapping, approval-SHA, API, MCP, schema-fixture, permission, hook, path-denial, event, and authority-boundary tests.

## Governing Values and Decisions — Axiology

### CLM-026 — Guidance: DEL-07-04 Status Transition API and MCP Tool

> #### Guidance: DEL-07-04 Status Transition API and MCP Tool
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-027 — Purpose

> ##### Purpose
>
> This deliverable exists to make deliverable lifecycle state a product-owned filesystem contract rather than an inferred UI or runtime condition. The accepted SOFTWARE_DECOMP v3.2 entry defines the slice as parsing `_STATUS.md` and enforcing forward-only, actor-authorized transitions with approval SHA for human gates. The source documents reinforce that `_STATUS.md` is canonical and that status transition behavior is a governed API/MCP surface, not prompt-only convention.
>

### CLM-028 — Principles

> ##### Principles
>
> 1. Treat `_STATUS.md` as the only lifecycle authority.
>    Source: `docs/CONTRACT.md` Section 1.7 K-STATUS-1; `docs/SPEC.md` Section 4.3.
>
> 2. Keep transition enforcement in code and tests.
>    Prompt instructions may reinforce the behavior, but `docs/DIRECTIVE.md` says runtime code enforces safety and prompt instructions are not sufficient enforcement.
>
> 3. Preserve forward-only lifecycle movement.
>    Source: `docs/SPEC.md` Section 4.3 and `docs/PRD.md` Section 8.9 FR-053.
>
> 4. Treat human gates as non-delegable.
>    Agents, SDKs, tools, validators, and runtime events must not author binding approval records. Source: `docs/CONTRACT.md` Section 1.2 K-AUTH-1/K-GATE-1 and `docs/DIRECTIVE.md` Human authority.
>
> 5. Make MCP a governed transport.
>    `mcp__chirality__status_transition` should not bypass permission, hook, path, redaction, or event logging policy. Source: `docs/CONTRACT.md` Section 1.6 K-MCP-1 and `docs/DIRECTIVE.md` Design commitments.
>
> 6. Keep dependency behavior separate.
>    Dependency register behavior belongs primarily to DEL-07-05; this deliverable may share API patterns but should not absorb `Dependencies.csv` reader/writer scope. Source: decomposition DEL-07-04/DEL-07-05 split and `docs/PRD.md` Section 8.9 FR-055 through FR-057.
>

### CLM-029 — Considerations

> ##### Considerations
>
> - Actor authorization should be explicit enough that unsupported actors fail closed. SPEC Section 4.3 lists authorized actors by transition; implementation-specific actor identity mapping remains `TBD`.
> - Approval SHA validation should follow the PRD acceptance detail of a 7-64 character hex SHA-like token for transitions to `CHECKING` or `ISSUED`. PRD hash status: MATCH status applies. (reconciled under D-APP-38).
> - The API and MCP tool should return structured denial information for invalid state, backward transition, unauthorized actor, missing approval SHA, invalid approval SHA, path/policy denial, and malformed `_STATUS.md`. Exact response shape is `TBD`.
> - `INITIALIZED -> SEMANTIC_READY` is optional according to `docs/TYPES.md` Section 4.1; if semantic lensing is skipped, deliverables may transition directly from `INITIALIZED -> IN_PROGRESS` under SPEC actor rules.
> - Status transition writes should remain subject to project-root containment and instruction-root protection expectations from the filesystem and permission surfaces. Source: `docs/CONTRACT.md` K-PATH-2 and K-MCP-1; `docs/PLAN.md` R3 implementation targets.
> - Runtime/event records can support audit, but they are not substitutes for accepted project-state files or human approval records. Source: `docs/DIRECTIVE.md` runtime event discussion and human authority section.
> - If alternate immutable approval evidence is ever accepted instead of a git SHA-like token, treat it as a human-approved policy extension recorded in versioned project evidence. Do not accept arbitrary runtime text as approval evidence. Source: `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-AUTH-2.
> - Review evidence should prove that status-transition outputs, tool events, hook events, and runtime records describe execution only. They must not use language that claims an agent, SDK, MCP tool, validator, or runtime event approved, issued, certified, or released work for reliance. Source: `docs/DIRECTIVE.md` Sections 2.3-2.4; `docs/CONTRACT.md` K-AUTH-1/K-BIND-1.
> - `SOFTWARE_DECOMP` is the accepted decomposition-family label in deliverable context, while `SOFTWARE` is the runtime dispatch token used by the four-documents task. Preserve both labels with their context rather than normalizing one into the other.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>

### CLM-030 — Trade-offs

> ##### Trade-offs
>
> | Topic | Guidance | Source |
> |---|---|---|
> | API versus MCP | Maintain both surfaces because the PRD/SPEC list working-root API endpoints and Chirality MCP tools. Keep validation shared or behaviorally equivalent to avoid drift. | `docs/PRD.md` API inventory; `docs/SPEC.md` Sections 13 and 14.2 |
> | SHA gate strictness | Prefer strict SHA-like validation for human gate transitions; if a human chooses alternate immutable evidence, capture it as a deliberate policy extension rather than silently accepting arbitrary text. | `docs/PRD.md` Section 8.9 FR-054; `docs/DIRECTIVE.md` Human authority |
> | Parser tolerance | Be tolerant enough to read the SPEC format, but report malformed or ambiguous status files rather than inferring state from other files. | `docs/SPEC.md` Section 4.1; `docs/CONTRACT.md` K-STATUS-1 |
> | Semantic-ready shortcut | Support the optional `INITIALIZED -> IN_PROGRESS` route when semantic lensing is skipped, but only under authorized actor rules. | `docs/TYPES.md` Section 4.1; `docs/SPEC.md` Section 4.3 |
> | Event logs | Record tool/runtime outcomes for audit, but do not treat runtime events as approval records. | `docs/DIRECTIVE.md` Runtime session logs and human authority |
> | Alternate approval evidence | Keep git SHA-like evidence as the default. Alternate immutable evidence requires human-approved policy extension and versioned evidence before implementation relies on it. | `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-AUTH-2 |
> | PRD hash warning | Continue using PRD-derived statements as warned source material for drafting, but require reconciliation or an approved bypass before final PRD-derived acceptance claims. | `_REFERENCES.md` REF-006; `docs/SPEC.md` reference hash behavior |
>

### CLM-031 — Examples

> ##### Examples
>
> | Scenario | Expected outcome | Source |
> |---|---|---|
> | Read a valid `_STATUS.md` with `Current State: INITIALIZED` | Status read returns `INITIALIZED`, last updated date, and history. | `docs/SPEC.md` Section 4.1; `docs/PRD.md` FR-052 |
> | Transition `OPEN -> INITIALIZED` by authorized document-initialization actor | Transition may be accepted if path/policy checks pass. | `docs/SPEC.md` Section 4.3 |
> | Transition `IN_PROGRESS -> CHECKING` without approval SHA | Transition is denied. | `docs/SPEC.md` Section 4.3; `docs/PRD.md` FR-054 |
> | Transition `CHECKING -> ISSUED` with a non-hex approval token | Transition is denied under PRD acceptance criterion. | `docs/PRD.md` FR-054 |
> | Transition `SEMANTIC_READY -> INITIALIZED` | Transition is denied as backward movement unless a human explicitly amends the record. | `docs/SPEC.md` Section 4.3 |
>

### CLM-032 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | TBD | No source conflict identified during P1/P2 drafting. | TBD | TBD | TBD | TBD | TBD |
>

### CLM-033 — Source Status

> ##### Source Status
>
> `docs/PRD.md` is listed as `MATCH` in `_REFERENCES.md`. Use PRD acceptance details as warned source material until the reference hash is reconciled. (reconciled under D-APP-38).
>

### CLM-034 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | ItemID | Disposition | Evidence |
> |---|---|---|
> | C-001 | Incorporated as a policy-extension rule for alternate immutable approval evidence. | `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-AUTH-2. |
> | D-002 | Incorporated as review-evidence guidance separating runtime/event records from human approval records. | `docs/DIRECTIVE.md` Sections 2.3-2.4; `docs/CONTRACT.md` K-AUTH-1/K-BIND-1. |
> | E-001 | Incorporated as contextual variant-label guidance. | `_CONTEXT.md` Identification; `_SEMANTIC_LENSING.md` header. |
> | E-003 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006; `docs/SPEC.md` reference hash behavior. — reconciled under D-APP-38 |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-028 OBJ-006 | CLM-009 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
