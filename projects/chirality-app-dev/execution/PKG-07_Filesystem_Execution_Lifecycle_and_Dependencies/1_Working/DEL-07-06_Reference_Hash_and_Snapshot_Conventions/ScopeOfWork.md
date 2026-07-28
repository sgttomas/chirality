---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-07-06
package_id: PKG-07
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-032, SOW-033, SOW-034, SOW-077]
package_objective_refs: [OBJ-006, OBJ-009]
---

# Scope of Work — DEL-07-06

## Purpose and Objective Traceability

This candidate defines `DEL-07-06` in service of project scope [SOW-032, SOW-033, SOW-034, SOW-077] and package objectives [OBJ-006, OBJ-009].

- **OUT-001** — Snapshot and runbook notes, a reference-hash bypass convention, and a CHANGE/SHA checklist preserving deterministic tool continuity, immutable evidence, and human-only approval boundaries.

**D-APP-80 concordance note (2026-07-28):** SOW-077 is recorded as an OUT
boundary-only trace. It does not reactivate excluded lock, freeze, budget,
usage, cost, forecast, or resource-governance functions.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-07-06 Reference Hash and Snapshot Conventions

> #### Datasheet: DEL-07-06 Reference Hash and Snapshot Conventions
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | Package ID | PKG-07 |
> | Package Name | Filesystem Execution, Lifecycle, and Dependencies |
> | Deliverable ID | DEL-07-06 |
> | Deliverable Name | Reference Hash and Snapshot Conventions |
> | Responsible Party | TBD |
> | Type | DOC_UPDATE |
> | Context Envelope | S |
> | Decomposition Variant | SOFTWARE_DECOMP v3.2 |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Deliverable purpose | Preserve deterministic tools/scripts, reference hash behavior, immutable snapshots, and SHA approval conventions without reactivating retired scope. | `_CONTEXT.md` Deliverable Scope; decomposition DEL-07-06 row |
> | Covered scope items | SOW-032 deterministic tools/scripts, SOW-033 immutable snapshots, SOW-034 CHANGE/publication SHA checks. | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SSOW and SOW-to-deliverable rows |
> | Supported objectives | OBJ-006 filesystem project truth; OBJ-009 professional boundary and reliance-boundary ownership. | `_CONTEXT.md` Traceability; decomposition Objectives |
> | Anticipated artifacts | Snapshot/runbook notes; hash bypass convention; CHANGE/SHA checklist. | `_CONTEXT.md` Anticipated Artifacts; decomposition DEL-07-06 row |
> | Reference hash bypass record | Deliverable folders may include `HASH_VERIFICATION_BYPASS.jsonl`; hash bypasses require human approval and durable bypass records. | `docs/SPEC.md` Sections 3.1 and 5.3 |
> | Snapshot convention | Snapshot-producing workflows should write timestamped immutable folders and may update `_LATEST.md` pointers. | `docs/SPEC.md` Section 2; `docs/CONTRACT.md` K-SNAP-1; `docs/PRD.md` FR-062 with REF-006 hash warning |
> | Approval evidence convention | Human approvals bind to specific content evidence, normally a git SHA; human-gate lifecycle transitions require approval SHA evidence. | `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-AUTH-2 and K-STATUS-2; `docs/SPEC.md` Section 4.3 |
> | Reference tool continuity | Accepted reference hash tooling and dependency-linter behavior remain in scope; retired hardening scope must not be reintroduced by runtime event logging. | `docs/CONTRACT.md` K-REF-1; `docs/PLAN.md` Section 9 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Handling | Source |
> |---|---|---|
> | `docs/PRD.md` source state | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006; task brief — reconciled under D-APP-38 |
> | Unknown owner | `ResponsibleParty` remains `TBD` until assigned by a human. | `_CONTEXT.md` Source Authority |
> | Retired scope boundary | Do not reactivate execution-root validator, dependency graph generator, deliverable lock, unified pipeline run records, or staleness propagation as current commitments. | `docs/PLAN.md` Section 9; `docs/PRD.md` Section 6.4 and KG-012 with REF-006 hash warning |
> | Human authority | No agent, SDK, tool, runtime event, validator, or adapter can author binding approval records. | `docs/CONTRACT.md` K-AUTH-1; `docs/DIRECTIVE.md` Section 2.4 |
>

### CLM-005 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | Item ID | Disposition | Evidence |
> |---|---|---|
> | A-002 | Already covered; ownership remains `TBD` and is not assigned by this pass. | Identification table; `_CONTEXT.md` Source Authority |
>

### CLM-006 — Construction

> ##### Construction
>
> | Component | Expected Content | Source |
> |---|---|---|
> | Snapshot/runbook notes | Rules for timestamped immutable snapshot folders, optional `_LATEST.md` pointer updates, non-overwrite of accepted snapshots, and source-state warnings. | `docs/SPEC.md` Section 2; `docs/CONTRACT.md` K-SNAP-1 |
> | Hash bypass convention | When reference hash verification is bypassed, record human approval and durable evidence in deliverable-local `HASH_VERIFICATION_BYPASS.jsonl` where applicable. | `docs/SPEC.md` Sections 3.1 and 5.3 |
> | CHANGE/SHA checklist | Checklist confirming candidate content evidence, approval token/SHA, HEAD recheck before approved actions, and continued human-only authority. | `docs/DIRECTIVE.md` Sections 2.2 and 2.4; `docs/PRD.md` FR-063 with REF-006 hash warning |
> | Tool continuity notes | Notes confirming deterministic project tools/scripts remain indexed and locally executable when present. Exact registry membership is `TBD` unless verified by the owning implementation slice. | `docs/PRD.md` FR-061 with REF-006 hash warning; decomposition SOW-032 |
>

### CLM-007 — References

> ##### References
>
> | RefID | Source | Sections Used | Source State |
> |---|---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | Sections 2.1, 2.2, 2.4, 2.5 | MATCH |
> | REF-002 | `docs/CONTRACT.md` | K-AUTH-1, K-AUTH-2, K-BIND-1, K-STATUS-1, K-STATUS-2, K-SNAP-1, K-REF-1 | MATCH |
> | REF-003 | `docs/SPEC.md` | Sections 2, 3.1, 4.3, 5.3 | MATCH |
> | REF-004 | `docs/TYPES.md` | Sections 1-2, 3.3 | MATCH |
> | REF-005 | `docs/PLAN.md` | Section 9 | MATCH |
> | REF-006 | `docs/PRD.md` | Sections 6.4, 8.10, 10.8, 15 | MATCH source state — reconciled under D-APP-38 |
> | REF-007 | `AGENT_SOFTWARE_DECOMP.md` | Decomposition method context | MATCH |

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-07-06 Reference Hash and Snapshot Conventions

> #### Specification: DEL-07-06 Reference Hash and Snapshot Conventions
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-009 — Scope

> ##### Scope
>
> This deliverable specifies documentation conventions for reference hash handling, snapshot immutability, deterministic script/tool continuity, and CHANGE/SHA approval evidence in PKG-07.
>
> In scope:
>
> - Preserve reference hash behavior and approved bypass conventions for deliverable-local references.
> - Preserve snapshot conventions for timestamped immutable folders and optional `_LATEST.md` pointers.
> - Preserve CHANGE/publication SHA checks and human-only approval boundaries.
> - Preserve notes that deterministic project tools/scripts remain indexed and locally executable when present.
>
> Out of scope:
>
> - Reintroducing retired execution-root validator, dependency graph generator, deliverable lock, unified pipeline run record persistence, or automated staleness propagation.
> - Implementing the status transition API, dependency linter, or tool registry itself except as referenced conventions.
> - Claiming automated professional approval, external validation, or human-gate authority.
>
> Sources: `_CONTEXT.md`; `docs/PLAN.md` Section 9; `docs/PRD.md` Sections 6.4 and 8.10 with REF-006 hash warning; decomposition DEL-07-06 row.
>

### CLM-010 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source |
> |---|---|---|
> | DEL-07-06-REQ-001 | Documentation for this deliverable MUST identify SOW-032, SOW-033, and SOW-034 as its covered scope items. | `_CONTEXT.md` Traceability; decomposition DEL-07-06 row |
> | DEL-07-06-REQ-002 | Reference-hash convention notes MUST keep `_REFERENCES.md` as the deliverable-local source reference and hash-note surface. | `docs/SPEC.md` Sections 3.1 and 5.3 |
> | DEL-07-06-REQ-003 | Out-of-folder references SHOULD include content hashes when tooling is available. | `docs/SPEC.md` Section 5.3 |
> | DEL-07-06-REQ-004 | Hash bypasses MUST require human approval and durable bypass records. | `docs/SPEC.md` Section 5.3 |
> | DEL-07-06-REQ-005 | `HASH_VERIFICATION_BYPASS.jsonl` MAY be used as the deliverable-local durable bypass record. | `docs/SPEC.md` Section 3.1 |
> | DEL-07-06-REQ-006 | Snapshot-producing workflows SHOULD write timestamped immutable folders. | `docs/SPEC.md` Section 2; `docs/CONTRACT.md` K-SNAP-1 |
> | DEL-07-06-REQ-007 | Snapshot-producing workflows MAY update mutable `_LATEST.md` pointers, but prior accepted snapshots MUST NOT be overwritten. | `docs/SPEC.md` Section 2; `docs/CONTRACT.md` K-SNAP-1; `docs/PRD.md` FR-062 with REF-006 hash warning |
> | DEL-07-06-REQ-008 | CHANGE/publication conventions MUST require explicit approval tokens and SHA checks. | `docs/PRD.md` FR-063 with REF-006 hash warning; decomposition SOW-034 |
> | DEL-07-06-REQ-009 | Human approvals MUST bind to specific content evidence, normally a git SHA or equivalent immutable evidence. | `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-AUTH-2 |
> | DEL-07-06-REQ-010 | Content changed after approval MUST be treated as no longer approved until reviewed again. | `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-AUTH-2 |
> | DEL-07-06-REQ-011 | Human-gate lifecycle transitions to `CHECKING` or `ISSUED` MUST require approval SHA evidence. | `docs/SPEC.md` Section 4.3; `docs/CONTRACT.md` K-STATUS-2 |
> | DEL-07-06-REQ-012 | Accepted reference hash tooling and dependency-linter tooling MUST remain available without reintroducing retired hardening scope. | `docs/CONTRACT.md` K-REF-1; `docs/PLAN.md` Section 9 |
> | DEL-07-06-REQ-013 | Deterministic project tools and scripts SHOULD remain indexed and locally executable when present. | `docs/PRD.md` FR-061 with REF-006 hash warning; decomposition SOW-032 |
> | DEL-07-06-REQ-014 | PRD-derived requirements MUST carry the REF-006 source-state warning until `docs/PRD.md` hash state is reconciled or accepted. | `_REFERENCES.md` REF-006; task brief |
> | DEL-07-06-REQ-015 | The deliverable MUST NOT state or imply that runtime events, tools, validators, SDKs, or agents approve, sign, seal, issue, certify, or externally validate work. | `docs/DIRECTIVE.md` Sections 2.3-2.4; `docs/CONTRACT.md` K-AUTH-1 and K-BIND-1 |
> | DEL-07-06-REQ-016 | Exact deterministic tool/script registry membership MUST remain `TBD` unless verified by the owning implementation slice or an accepted registry source. | `docs/PRD.md` FR-061 with REF-006 hash warning; `docs/PRD.md` KG-013 with REF-006 hash warning; `docs/CONTRACT.md` K-INVENT-1 |
>

### CLM-011 — Standards

> ##### Standards
>
> | Standard / Contract | Applicability | Source |
> |---|---|---|
> | Lifecycle file contract | Approval SHA handling and forward-only status conventions referenced by CHANGE/SHA checklist. | `docs/SPEC.md` Section 4 |
> | Deliverable folder layout | `_REFERENCES.md`, document kit, optional `HASH_VERIFICATION_BYPASS.jsonl`, and disabled `_MEMORY.md` expectations. | `docs/SPEC.md` Section 3.1; `docs/PRD.md` Section 10.8 with REF-006 hash warning |
> | Filesystem project truth | Project state and approvals must land in versioned project files and accepted git history, not hidden memory or runtime logs alone. | `docs/DIRECTIVE.md` Sections 2.1-2.3; `docs/TYPES.md` Section 1 |
> | Snapshot invariant | Immutable timestamped folders and mutable pointer convention. | `docs/CONTRACT.md` K-SNAP-1 |
> | Reference-tool invariant | Reference hash tooling continuity without retired scope reactivation. | `docs/CONTRACT.md` K-REF-1 |
>

### CLM-012 — Verification

> ##### Verification
>
> | Requirement(s) | Verification Approach |
> |---|---|
> | REQ-001 | Traceability review confirms SOW/objective rows match `_CONTEXT.md` and decomposition DEL-07-06. |
> | REQ-002 through REQ-005 | Documentation review confirms `_REFERENCES.md`, content hash, human approval, and `HASH_VERIFICATION_BYPASS.jsonl` conventions are present without inventing unaccepted bypass fields. |
> | REQ-006 through REQ-007 | Snapshot/runbook review confirms timestamped immutable snapshot folders, optional `_LATEST.md`, and non-overwrite wording. |
> | REQ-008 through REQ-011 | CHANGE/SHA checklist review confirms approval token/SHA evidence, HEAD/content evidence recheck, and human-gate SHA requirements. |
> | REQ-012 through REQ-013 | Scope review confirms tool/script continuity is documented while exact registry membership remains `TBD` unless separately verified. |
> | REQ-014 | Review confirms PRD-derived statements visibly carry the REF-006 hash warning. |
> | REQ-015 | Professional-boundary review confirms no automated approval, issue, certification, external validation, or reliance claim is introduced. |
> | REQ-016 | Registry review confirms exact tool/script membership is not asserted without accepted registry evidence. |
>

### CLM-013 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | Item ID | Disposition | Evidence |
> |---|---|---|
> | B-002 | Converted to explicit `TBD` control by REQ-016; exact registry membership awaits owning implementation evidence. | Requirements and Verification tables |
> | C-001 | Already covered and retained; REQ-014 and its verification row require visible REF-006 warning language for PRD-derived statements. | Requirements and Verification tables |
>

### CLM-014 — Documentation

> ##### Documentation
>
> Required outputs or records for this deliverable:
>
> - Snapshot/runbook notes covering immutable timestamped folders and `_LATEST.md` pointer behavior.
> - Hash bypass convention covering human approval, durable bypass records, and `HASH_VERIFICATION_BYPASS.jsonl`.
> - CHANGE/SHA checklist covering candidate SHA/action list, approval evidence, and HEAD/content recheck before approved actions.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
> - Open-item note for exact deterministic tool/script registry membership if not verified by the owning implementation slice.

- **AC-001** — The convention retains _REFERENCES.md hash handling, human-approved durable bypass evidence, immutable timestamped snapshots with governed _LATEST pointers, SHA-bound approvals and renewed review after changes, deterministic-tool continuity, retired-scope exclusions, and human-only authority.

## Production and Verification Method — Praxeology

### CLM-015 — Procedure: DEL-07-06 Reference Hash and Snapshot Conventions

> #### Procedure: DEL-07-06 Reference Hash and Snapshot Conventions
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-016 — Purpose

> ##### Purpose
>
> Use this procedure to produce or review the DEL-07-06 convention notes: snapshot/runbook notes, hash bypass convention, and CHANGE/SHA checklist.
>

### CLM-017 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status / Source |
> |---|---|
> | Deliverable-local context, references, dependencies, and status files are present. | `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` |
> | Current lifecycle state permits drafting. | `_STATUS.md` was `OPEN` at P1/P2 start |
> | Authoritative sources are locally accessible. | `_REFERENCES.md` REF-001 through REF-007; REF-006 has MATCH status — reconciled under D-APP-38 |
> | Accepted dependency edges are available. | TBD: `_DEPENDENCIES.md` declares no accepted upstream/downstream edges yet |
> | Human owner is assigned. | TBD: `_CONTEXT.md` preserves `ResponsibleParty: TBD` |
>

### CLM-018 — Steps

> ##### Steps
>
> 1. Confirm source state.
>    - Read `_REFERENCES.md`.
>    - Record the status of each authoritative reference.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>
> 2. Confirm scope boundary.
>    - Use `_CONTEXT.md` and the decomposition row for DEL-07-06.
>    - Confirm the deliverable covers SOW-032, SOW-033, and SOW-034.
>    - Confirm the work remains a `DOC_UPDATE`, not an implementation task.
>
> 3. Draft snapshot/runbook notes.
>    - State that snapshot-producing workflows should create timestamped immutable folders.
>    - State that `_LATEST.md` pointers may move when the owning workflow permits.
>    - State that accepted snapshots must not be overwritten.
>    - Cite `docs/SPEC.md` Section 2 and `docs/CONTRACT.md` K-SNAP-1.
>
> 4. Draft the hash bypass convention.
>    - State that `_REFERENCES.md` carries source references and hash notes.
>    - State that out-of-folder references should include content hashes when tooling is available.
>    - State that hash bypasses require human approval and durable bypass records.
>    - When a concrete bypass is used, confirm the review package includes both human approval evidence and the durable bypass record before treating the bypass as accepted.
>    - Identify `HASH_VERIFICATION_BYPASS.jsonl` as the deliverable-local bypass record surface where applicable.
>    - Cite `docs/SPEC.md` Sections 3.1 and 5.3.
>
> 5. Draft the CHANGE/SHA checklist.
>    - Confirm candidate content evidence and action list are recorded before approval.
>    - Confirm human approval evidence is present and SHA-like where required.
>    - Before any `CHECKING` or `ISSUED` transition, confirm approval SHA evidence exists for the exact candidate content under review.
>    - Recheck HEAD/current candidate content before executing approved CHANGE/publication actions.
>    - State that content changed after approval requires renewed review.
>    - Cite `docs/DIRECTIVE.md` Section 2.4, `docs/CONTRACT.md` K-AUTH-2, and `docs/PRD.md` FR-063 with REF-006 hash warning.
>
> 6. Guard retired scope.
>    - Confirm the convention notes do not reactivate execution-root validator, dependency graph generator, deliverable lock, unified pipeline run record persistence, or automated staleness propagation.
>    - Cite `docs/PLAN.md` Section 9 and `docs/PRD.md` KG-012 with REF-006 hash warning.
>
> 7. Confirm human-authority language.
>    - Remove any wording implying that an agent, SDK, tool, runtime event, validator, or adapter approves, issues, certifies, signs, seals, or externally validates work.
>    - Cite `docs/DIRECTIVE.md` Sections 2.3-2.4 and `docs/CONTRACT.md` K-AUTH-1/K-BIND-1.
>
> 8. Run cross-document consistency check.
>    - Confirm Datasheet attributes map to Specification requirements.
>    - Confirm Specification verification rows have corresponding procedure steps.
>    - Confirm Guidance source warnings match Datasheet and Specification warning language.
>    - Leave unresolved values as `TBD` and list human rulings in Guidance.
>

### CLM-019 — Verification

> ##### Verification
>
> | Check | Acceptance |
> |---|---|
> | Source-state warning | REF-006 `docs/PRD.md` hash status: MATCH is visible anywhere PRD-derived requirements or examples are used. — reconciled under D-APP-38 |
> | Snapshot convention | Notes include timestamped immutable folders, optional `_LATEST.md`, and non-overwrite of accepted snapshots. |
> | Hash bypass convention | Notes include human approval, durable bypass record, and `HASH_VERIFICATION_BYPASS.jsonl` where applicable. |
> | Hash bypass evidence | If a bypass is used, review confirms explicit human approval evidence and a durable bypass record exist before accepting the bypass. |
> | CHANGE/SHA checklist | Notes include candidate evidence, approval token/SHA, approval SHA evidence before `CHECKING` or `ISSUED`, HEAD/current-content recheck, and renewed review after content changes. |
> | Retired scope | No current commitment is made for retired execution-root validator, dependency graph generator, deliverable lock, unified pipeline run record persistence, or automated staleness propagation. |
> | Human authority | No automated approval, signing, sealing, issue, certification, external validation, or professional reliance claim is introduced. |
>

### CLM-020 — Records

> ##### Records
>
> - `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` for DEL-07-06.
> - `_run_records/TASK_RUN_*.md` capturing the TASK run and source-state warnings.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
> - Future exact deterministic tool/script registry evidence: TBD unless produced by the owning implementation slice.
> - Future accepted dependency edge record source: TBD until `_DEPENDENCIES.md` or `Dependencies.csv` records accepted upstream/downstream edge availability.
>

### CLM-021 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | Item ID | Disposition | Evidence |
> |---|---|---|
> | F-001 | Converted to explicit `TBD`; dependency edge availability remains unresolved until an accepted dependency record source is present. | Prerequisites; Records |
> | D-001 | Incorporated; the CHANGE/SHA checklist now requires approval SHA evidence before any `CHECKING` or `ISSUED` transition. | Steps; Verification |
> | X-001 | Incorporated; bypass review now requires human approval evidence and a durable bypass record when a bypass is used. | Steps; Verification |

- **VER-001** — Review the source-defined traceability, reference-hash and bypass, snapshot non-overwrite, CHANGE/SHA, registry-TBD, retired-scope, source-state, and professional-boundary checks.

## Governing Values and Decisions — Axiology

### CLM-022 — Guidance: DEL-07-06 Reference Hash and Snapshot Conventions

> #### Guidance: DEL-07-06 Reference Hash and Snapshot Conventions
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-023 — Purpose

> ##### Purpose
>
> This deliverable preserves the conventions that let filesystem project truth stay reviewable: reference hashes make source state explicit, snapshots preserve accepted point-in-time outputs, and approval SHA checks bind human decisions to concrete content evidence. The work is intentionally documentary and continuity-focused, not an implementation expansion.
>
> Sources: `_CONTEXT.md`; decomposition DEL-07-06; `docs/DIRECTIVE.md` Sections 2.1-2.4; `docs/CONTRACT.md` K-SNAP-1 and K-REF-1.
>

### CLM-024 — Principles

> ##### Principles
>
> 1. Evidence is stronger than plausible continuity.
>    Reference hashes, durable bypass records, snapshot names, `_LATEST.md` pointers, and git SHA evidence are all project-truth aids. If an input is unknown, mark it `TBD` rather than inferring a value. Sources: `docs/DIRECTIVE.md` Section 2.5; `docs/CONTRACT.md` K-INVENT-1.
>
> 2. Snapshot means preserved state, not a mutable workspace.
>    A snapshot-producing workflow should create a new timestamped folder and may move a pointer. It should not overwrite a previously accepted snapshot. Sources: `docs/SPEC.md` Section 2; `docs/CONTRACT.md` K-SNAP-1.
>
> 3. Hash bypass is exceptional and human-approved.
>    A bypass should not silently downgrade source fidelity. When used, it needs human approval and a durable record, with `HASH_VERIFICATION_BYPASS.jsonl` available as the deliverable-local record surface. Source: `docs/SPEC.md` Sections 3.1 and 5.3.
>
> 4. CHANGE/SHA checks are reliance controls, not ceremonial metadata.
>    Approval evidence must bind to specific content, normally a git SHA or equivalent immutable evidence. Changed content needs renewed review. Sources: `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-AUTH-2.
>
> 5. Runtime audit records do not approve project work.
>    Runtime logs may explain what happened, but they do not substitute for accepted project-state files or human approval records. Sources: `docs/DIRECTIVE.md` Section 2.3; `docs/CONTRACT.md` K-BIND-1.
>

### CLM-025 — Considerations

> ##### Considerations
>
> | Topic | Guidance | Source |
> |---|---|---|
> | PRD source warning | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | `_REFERENCES.md` REF-006; task brief — reconciled under D-APP-38 |
> | Tool/script registry | State that deterministic tools/scripts remain indexed and locally executable when present, but keep exact registry membership `TBD` unless verified by the owning implementation slice. | `docs/PRD.md` FR-061 with REF-006 hash warning; decomposition SOW-032 |
> | Retired scope | Do not turn reference hashes or snapshot notes into commitments for retired execution-root validator, graph generator, deliverable lock, unified pipeline run records, or staleness propagation. | `docs/PLAN.md` Section 9; `docs/PRD.md` KG-012 with REF-006 hash warning |
> | Human gate language | Use approval, issue, sign, seal, certify, and validate only for human-controlled processes; do not attribute those actions to agents or tools. | `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-AUTH-1 |
> | Pointers | `_LATEST.md` is mutable convenience metadata; the timestamped snapshot folder is the durable point-in-time artifact. | `docs/SPEC.md` Section 2; `docs/CONTRACT.md` K-SNAP-1 |
>

### CLM-026 — Trade-offs

> ##### Trade-offs
>
> | Choice | Benefit | Cost / Risk |
> |---|---|---|
> | Use warning-qualified PRD text where corroborated | Keeps the draft aligned with active vNext direction. | Requires later source-hash reconciliation before final acceptance. |
> | Keep tool registry membership `TBD` | Avoids inventing exact current script inventory from narrative sources. | Leaves implementation owner to confirm registry paths and tests. |
> | Allow mutable `_LATEST.md` pointers | Gives operators a convenient current pointer. | Review must distinguish the pointer from immutable snapshot evidence. |
> | Require durable bypass records | Makes source exceptions auditable. | Adds review overhead when a hash status: MATCH is intentionally accepted. — reconciled under D-APP-38 |
>

### CLM-027 — Examples

> ##### Examples
>
> | Situation | Recommended Handling |
> |---|---|
> | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
> | A workflow reruns snapshot generation. | Create a new timestamped snapshot folder and update `_LATEST.md` if the workflow owns that pointer; do not overwrite an accepted prior snapshot. |
> | CHANGE is asked to publish after edits. | Confirm approval token/SHA evidence, compare the current candidate content to the approved evidence, and recheck HEAD before approved actions. |
> | A tool needs to ignore a hash status: MATCH. | Require explicit human approval and append a durable bypass record, using deliverable-local `HASH_VERIFICATION_BYPASS.jsonl` when applicable. — reconciled under D-APP-38 |
>

### CLM-028 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | SOURCE-WARN-001 | `docs/PRD.md` is accessible and needed for active vNext direction, but `_REFERENCES.md` reports a hash status: MATCH. | `_REFERENCES.md` REF-006 | `docs/PRD.md` current accessible text | All PRD-cited requirements and examples | Continue using PRD as warning-qualified source per task brief; require hash reconciliation or explicit acceptance before closure. | TBD — reconciled under D-APP-38 |
>

### CLM-029 — Pass 3 Disposition Notes

> ##### Pass 3 Disposition Notes
>
> | Item ID | Disposition | Evidence |
> |---|---|---|
> | A-001 | Surfaced as conflict; SOURCE-WARN-001 remains open until hash reconciliation or explicit acceptance. | Conflict Table |
> | B-001 | Surfaced as conflict; PRD-derived closure-ready statements remain warning-qualified. | Conflict Table; Considerations |
> | E-001 | Surfaced as conflict; SOURCE-WARN-001 remains the active human-ruling item. | Conflict Table |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-032 SOW-033 SOW-034 OBJ-006 OBJ-009 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
