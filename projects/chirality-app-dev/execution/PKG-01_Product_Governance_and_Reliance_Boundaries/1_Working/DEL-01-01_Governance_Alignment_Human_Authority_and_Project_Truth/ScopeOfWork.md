---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-01
package_id: PKG-01
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
project_scope_refs: [SOW-074, SOW-075]
package_objective_refs: [OBJ-009]
---

# Scope of Work — DEL-01-01

## Purpose and Objective Traceability

This Scope of Work defines `DEL-01-01` in service of project scope [SOW-074, SOW-075] and package objectives [OBJ-009].

- **OUT-001** — Governance-alignment record and human-authority, project-truth, and runtime-audit checklists grounded in SOW-074, SOW-075, and OBJ-009.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-01-01 Governance Alignment, Human Authority, and Project Truth

> #### Datasheet: DEL-01-01 Governance Alignment, Human Authority, and Project Truth
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | DecompositionPath | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` |
> | PackageID | PKG-01 |
> | PackageName | Product Governance and Reliance Boundaries |
> | DeliverableID | DEL-01-01 |
> | DeliverableName | Governance Alignment, Human Authority, and Project Truth |
> | ResponsibleParty | Ryan Tufts (K-AUTH-1) — assigned 2026-07-18 by D-APP-65 (demonstrator scope) |
> | Type | DOC_UPDATE |
> | ContextEnvelope | M |
> | CurrentLifecycleState | Read from `_STATUS.md` (currently `IN_PROGRESS`; prior states remain historical evidence) |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Source-grounded value |
> |---|---|
> | Deliverable purpose | Keep `docs/PRD.md`, `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, and the active decomposition mutually consistent while preserving human authority, filesystem project truth, accepted git history, and runtime-audit boundaries. |
> | Package scope | Product intent, invariants, professional boundary, reliance-boundary ownership, and out-of-scope discipline. |
> | Inclusion criteria | Governance docs, acceptance checks, product identity, and scope boundaries. |
> | Exclusions | Runtime implementation details except as required for boundary enforcement. |
> | Covered scope items | SOW-074; SOW-075. |
> | Supported objective | OBJ-009. |
> | Anticipated artifacts | Governance consistency notes; human-authority checklist; project-truth checklist; doc diff checklist; acceptance checklist. |
> | Reference integrity | Authority-doc references were reconciled under the current D-APP-38 corpus snapshot; REF-006 `docs/PRD.md` is currently `MATCH` in `_REFERENCES.md`. |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value |
> |---|---|
> | Human authority condition | Only humans may author binding approval records, approve issue/release actions, select governing standards, accept residual risk, adjudicate judgment conflicts, and decide whether work may be relied upon. |
> | Project truth condition | Gate-relevant project state must be represented in versioned project files under the working root and accepted git history. Hidden app state, chats, SDK transcripts, runtime logs, model context, caches, API keys, and provider transcripts are not project truth unless imported through a governed process. |
> | Runtime audit condition | Runtime events explain work and support replay, but they do not approve deliverables, issue work, prove code compliance, or substitute for accepted project files and human approval records. |
> | Reliance-boundary condition | Product-critical boundaries must be documented, implemented, and tested in Chirality terms; prompt text or opaque SDK defaults alone are insufficient for P0 boundaries. |
> | Lifecycle condition | `_STATUS.md` is the canonical lifecycle file and the current state is read from it; any future human-gate transition remains non-delegable. |
> | Dependency-register condition | `Dependencies.csv` is a derivative dependency-extract artifact. This reconciliation may describe it but must not mark rows satisfied or mutate dependency status. |
>

### CLM-005 — Construction

> ##### Construction
>
> | Component | Required treatment |
> |---|---|
> | Governance consistency notes | Compare the governing document set using the authority order in `docs/DIRECTIVE.md` and the invariant catalog in `docs/CONTRACT.md`; record conflicts rather than silently resolving them. |
> | Human-authority checklist | Verify no document, UI copy, runtime event, validator, SDK behavior, agent, tool, or domain adapter claims to approve, certify, sign, seal, issue, transmit, externally validate, or make professional work reliable by itself. |
> | Project-truth checklist | Verify reliance-relevant facts land in proper project files and accepted git history, not only in runtime state, chat, SDK transcripts, UI state, caches, or hidden memory. |
> | Runtime-audit checklist | Verify Chirality-owned `.chirality/sessions/<sessionId>/events.jsonl` remains the canonical runtime audit mirror and that SDK transcripts remain secondary unless imported into `HarnessEvent` form. |
> | Diff/acceptance checklist | Verify PRD, DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN, and decomposition changes remain mutually consistent with SOW-074, SOW-075, OBJ-009, and CONTRACT invariant families owned by PKG-01. |
>

### CLM-006 — References

> ##### References
>
> | RefID | Source | Use in this datasheet |
> |---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | Authority order, filesystem truth, human authority, evidence posture, reliance boundaries, professional responsibility. |
> | REF-002 | `docs/CONTRACT.md` | Binding invariants for project truth, human authority, lifecycle, invention/conflict discipline, runtime boundaries, and professional boundaries. |
> | REF-003 | `docs/SPEC.md` | Execution-root layout, deliverable file contract, lifecycle states, runtime audit and engine contracts. |
> | REF-004 | `docs/TYPES.md` | Canonical vocabulary for project truth, runtime audit mirror, deliverables, stable IDs, and agent authority. |
> | REF-005 | `docs/PLAN.md` | Roadmap acceptance principles, current R0/R1 focus, SDK-governance boundaries, out-of-scope items. |
> | REF-006 | `docs/PRD.md` | Current product requirements and acceptance criteria; the current D-APP-38 corpus snapshot records a matching authority-doc hash. |
> | REF-007 | `/Users/ryan/ai-env/projects/chirality/agents/AGENT_SOFTWARE_DECOMP.md` | SOFTWARE_DECOMP no-invention, human gate, stable-ID, bounded-deliverable method context. |
> | DEC-001 | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | DEL-01-01 scope, SOW-074, SOW-075, OBJ-009, package scope, and anticipated artifacts. |

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-01-01 Governance Alignment, Human Authority, and Project Truth

> #### Specification: DEL-01-01 Governance Alignment, Human Authority, and Project Truth
>

### CLM-008 — Scope

> ##### Scope
>
> This deliverable covers the governance-alignment work needed to keep `docs/PRD.md`, `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, and the active SOFTWARE_DECOMP v3.2 working surface mutually consistent as the runtime evolves.
>
> The scope is bounded to preserving human authority, filesystem project truth, accepted git history, runtime-audit boundaries, product identity, professional-boundary posture, and reliance-boundary ownership. Runtime implementation details are excluded except where they are necessary to define or check a governance boundary.
>
> ResponsibleParty remains `TBD` until assigned by a human.
>

### CLM-009 — Requirements

> ##### Requirements
>
> | ReqID | Requirement | Source basis | Verification |
> |---|---|---|---|
> | DEL-01-01-REQ-001 | Governance alignment work must preserve the authority order: DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN, PRD, then agent instructions and accepted execution records for concrete operations. | `docs/DIRECTIVE.md` Section 0. | Governance consistency notes identify any lower-authority conflict and proposed correction path. |
> | DEL-01-01-REQ-002 | Human approval, professional acceptance, issue/release actions, residual-risk acceptance, and judgment conflict rulings must remain human-only. | `docs/DIRECTIVE.md` Sections 2.4 and 3; `docs/CONTRACT.md` K-AUTH/K-GATE/K-PROF. | Human-authority checklist confirms no automated approval claim is introduced. |
> | DEL-01-01-REQ-003 | Agent, SDK, runtime, validator, deterministic tool, domain adapter, and runtime-event outputs must be described as drafts, evidence, diagnostics, or decision support unless accepted by a governed human process. | `docs/DIRECTIVE.md` Sections 2.3 and 3.1; `docs/CONTRACT.md` K-BIND-1. | Checklist reviews copy and document changes for binding/non-binding separation. |
> | DEL-01-01-REQ-004 | Project truth must remain in versioned project files under the working root and accepted git history; hidden app state, chat, SDK transcripts, runtime logs, caches, model context, API keys, and provider transcripts must not be treated as project truth unless imported through governance. | `docs/DIRECTIVE.md` Sections 2.1, 2.2, 2.6; `docs/TYPES.md` Project Truth. | Project-truth checklist verifies claims and storage locations. |
> | DEL-01-01-REQ-005 | Runtime events must support audit and replay without approving or issuing deliverables. | `docs/DIRECTIVE.md` Section 2.3; `docs/SPEC.md` Sections 8-10; `docs/PRD.md` session/audit requirements. | Runtime-audit checklist confirms `.chirality/sessions/<sessionId>/events.jsonl` is canonical and SDK transcripts are secondary unless imported. |
> | DEL-01-01-REQ-006 | Product-critical reliance boundaries must be Chirality-owned or verified at explicit enforcement surfaces; prompt text and opaque SDK defaults are not sufficient for P0 boundaries. | `docs/DIRECTIVE.md` Section 2.9; `docs/CONTRACT.md` K-RELIANCE-1/K-RELIANCE-2; `docs/PLAN.md` R0/R1. | Acceptance checklist verifies each P0 reliance boundary has a documented non-prompt-only enforcement plan or an open gap. |
> | DEL-01-01-REQ-007 | SDK adoption must remain privileged but replaceable; SDK APIs, transcript shape, tool names, and vendor defaults must not define Chirality public semantics or product identity. | `docs/DIRECTIVE.md` Sections 2.8-2.11; `docs/CONTRACT.md` K-ENGINE/K-SDK; `docs/PLAN.md` Controlling Runtime Direction. | Diff checklist verifies product-owned contracts and Chirality terminology remain intact. |
> | DEL-01-01-REQ-008 | Unknown, unsupported, or conflicting facts must be represented as `TBD`, `ASSUMPTION`, `PROPOSAL`, source warning, or human-ruling-needed. | `docs/DIRECTIVE.md` Section 2.5; `docs/CONTRACT.md` K-INVENT-1/K-CONFLICT-1; `AGENT_SOFTWARE_DECOMP.md`. | Review checks the four-document kit and later governance notes for unsupported claims. |
> | DEL-01-01-REQ-009 | Lifecycle state must only transition according to SPEC; current state is read from `_STATUS.md`, while historical `CHECKING` admission is not issuance approval. | `docs/SPEC.md` Section 4; `_STATUS.md`; D-APP-54. | `_STATUS.md` remains the sole lifecycle authority during docs reconciliation; any human-gate transition requires its governed evidence. |
> | DEL-01-01-REQ-010 | Dependency-extract output is derivative evidence and must not be treated as authoritative decomposition truth or silently marked satisfied. | `_DEPENDENCIES.md`; `Dependencies.csv`; D-APP-38 reference-integrity model. | `Dependencies.csv` may exist, but this deliverable records row status without satisfying, retiring, or mutating rows outside a governed dependency/evidence tranche. |
>

### CLM-010 — Standards

> ##### Standards
>
> | Standard / governing source | Status |
> |---|---|
> | `docs/DIRECTIVE.md` | Accessible; hash match. |
> | `docs/CONTRACT.md` | Accessible; hash match. |
> | `docs/SPEC.md` | Accessible; hash match. |
> | `docs/TYPES.md` | Accessible; hash match. |
> | `docs/PLAN.md` | Accessible; hash match. |
> | `docs/PRD.md` | Accessible; the current D-APP-38 corpus snapshot records matching REF-006 authority-doc hashes. |
> | Active decomposition `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | Accessible. |
> | `AGENT_SOFTWARE_DECOMP.md` | Accessible; hash match. |
>

### CLM-011 — Verification

> ##### Verification
>
> | Verification item | Method | Acceptance |
> |---|---|---|
> | Four-document kit exists | File check | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` exist and are non-empty. |
> | Human-authority preservation | Checklist review | No automated actor is represented as able to approve, issue, certify, sign, seal, externally validate, or make professional work reliable. |
> | Project-truth preservation | Checklist review | Reliance-relevant facts are represented in project files and git evidence, not only runtime state or hidden memory. |
> | Runtime-audit boundary | Checklist review | Runtime audit is evidence/replay support only; it does not replace approval records. |
> | Cross-document consistency | Diff checklist | PRD, DIRECTIVE, CONTRACT, SPEC, TYPES, PLAN, and decomposition remain aligned or conflicts are surfaced. |
> | Reference integrity handling | Reference-row check | Authority-doc references, including REF-006, match the current D-APP-38 corpus before issue-readiness reliance is claimed. |
> | Historical warning handling | Conflict/source-warning table | Historical PRD hash warnings are treated as superseded by the current D-APP-38 corpus snapshot; other path/source conflicts remain visible pending human ruling. |
> | Dependency-register handling | Scope check | This reconciliation does not satisfy, retire, or otherwise mutate local dependency rows. |
>

### CLM-012 — Documentation

> ##### Documentation
>
> The expected documentation artifacts are:
>
> - Governance consistency notes.
> - Human-authority checklist.
> - Project-truth checklist.
> - Runtime-audit boundary checklist.
> - Document diff checklist.
> - Acceptance checklist.
> - Conflict/source-warning table for human rulings where source records disagree or source hashes are not accepted.
>
> `TBD`: final artifact filenames and destination locations for the above checklists are not specified by the available sources. This includes the governance consistency notes, human-authority checklist, project-truth checklist, runtime-audit checklist, document diff checklist, acceptance checklist, and conflict/source-warning table.

- **AC-001** — The converted contract preserves all legacy source content and traceability to SOW-074, SOW-075, and OBJ-009 without changing lifecycle or dependency state.

## Production and Verification Method — Praxeology

### CLM-013 — Procedure: DEL-01-01 Governance Alignment, Human Authority, and Project Truth

> #### Procedure: DEL-01-01 Governance Alignment, Human Authority, and Project Truth
>

### CLM-014 — Purpose

> ##### Purpose
>
> This procedure describes how to produce and use the DEL-01-01 governance-alignment artifacts while preserving human authority, project truth, accepted git evidence, and runtime-audit boundaries.
>

### CLM-015 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status |
> |---|---|
> | Deliverable-local context files exist: `_STATUS.md`, `_CONTEXT.md`, `_DEPENDENCIES.md`, `_REFERENCES.md`, `_SEMANTIC.md`, `_SEMANTIC_LENSING.md` | Present at P3 enrichment. |
> | Current lifecycle state permits documentation reconciliation | Read from `_STATUS.md` (currently `IN_PROGRESS`); this procedure performs no lifecycle transition. |
> | Authoritative references are locally accessible | Accessible; the current D-APP-38 corpus snapshot records REF-006 `docs/PRD.md` as `MATCH`. |
> | Upstream dependencies | See derivative `Dependencies.csv`; rows remain pending unless separately disposed. |
> | Downstream dependencies | No downstream deliverable edges are accepted in this reconciliation. |
> | Human owner | `ResponsibleParty`: Ryan Tufts (K-AUTH-1) — assigned 2026-07-18 by D-APP-65 (demonstrator scope). |
>

### CLM-016 — Steps

> ##### Steps
>
> 1. Confirm scope identity.
>    - Verify `PackageID=PKG-01`, `DeliverableID=DEL-01-01`, `Type=DOC_UPDATE`, and `ResponsibleParty=TBD` against `_CONTEXT.md` and SOFTWARE_DECOMP v3.2.
>    - If path labels disagree but stable IDs match, record the mismatch as a source warning or human-ruling-needed item.
>
> 2. Check source status.
>    - Read `_REFERENCES.md`.
>    - Confirm hash status for each source.
>    - Confirm REF-006 `docs/PRD.md` is reconciled to the current D-APP-38 corpus version before issue-readiness reliance is claimed.
>    - Treat older PRD hash-mismatch prose as historical if `_REFERENCES.md` records `MATCH`.
>    - Mark any inaccessible or unsupported source-dependent content as `TBD`.
>
> 3. Build governance consistency notes.
>    - Compare changes against the authority order in `docs/DIRECTIVE.md`.
>    - Check CONTRACT invariant families owned or co-owned by PKG-01: project truth, human authority, binding/non-binding records, gates, professional boundary, reliance boundaries, SDK identity, lifecycle, invention/conflict discipline, validation/release boundaries, and retired scope.
>    - Record conflicts rather than resolving them silently.
>
> 4. Build the human-authority checklist.
>    - Check that no document, UI copy, runtime event, SDK behavior, tool, validator, agent, or domain adapter claims to approve, certify, sign, seal, issue, transmit, externally validate, or make professional work reliable by itself.
>    - Check that CHECKING, ISSUED, domain-operation acceptance, residual-risk acceptance, and source-conflict rulings remain human-gated where applicable.
>
> 5. Build the project-truth checklist.
>    - Check that reliance-relevant facts land in versioned project files or accepted artifacts.
>    - Check that hidden app state, chat, SDK transcripts, runtime logs, model context, caches, UI state, API keys, provider transcripts, and convenience state are not treated as project truth unless imported by governance.
>    - Check that accepted decisions bind to git SHA or equivalent immutable evidence where approval is claimed.
>
> 6. Build the runtime-audit boundary checklist.
>    - Check that `.chirality/sessions/<sessionId>/events.jsonl` remains the Chirality-owned runtime audit mirror.
>    - Check that SDK transcripts remain secondary runtime state unless imported into `HarnessEvent` form or a governed artifact.
>    - Check that runtime events explain execution and do not approve deliverables.
>
> 7. Build the document diff checklist.
>    - Review `docs/PRD.md`, `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, and active SOFTWARE_DECOMP changes for mutual consistency.
>    - Confirm SOW-074, SOW-075, and OBJ-009 remain satisfied.
>    - Flag lower-authority conflicts with higher-authority sources for human ruling.
>
> 8. Build the acceptance checklist.
>    - Confirm every P0 reliance boundary referenced by this deliverable has a documented enforcement surface or open gap.
>    - Confirm unknowns are marked `TBD`, `ASSUMPTION`, `PROPOSAL`, source warning, or human-ruling-needed.
>    - Confirm dependency rows are not satisfied, retired, or otherwise mutated unless a later task explicitly authorizes dependency/evidence disposition.
>
> 9. Record results.
>    - Write outputs to authorized deliverable-local artifacts only.
>    - Do not mark dependency rows satisfied or mutate `Dependencies.csv` during this documentation reconciliation.
>    - Preserve `_STATUS.md` unless an explicit governed status policy authorizes a transition.
>

### CLM-017 — Verification

> ##### Verification
>
> | Check | Pass condition |
> |---|---|
> | Four-doc kit | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` exist and are non-empty. |
> | Lifecycle | `_STATUS.md` remains the sole lifecycle authority; no transition is performed. |
> | Reference integrity | REF-006 `docs/PRD.md` is `MATCH` in `_REFERENCES.md`; historical PRD hash-warning prose is not carried forward as an active blocker. |
> | Responsible party | `ResponsibleParty` is Ryan Tufts (K-AUTH-1) — assigned 2026-07-18 by D-APP-65 (demonstrator scope). |
> | Dependency-register handling | Existing `Dependencies.csv` rows are not satisfied, retired, or otherwise mutated. |
> | No invention | Unsupported facts are `TBD`, `ASSUMPTION`, `PROPOSAL`, conflict, source warning, or human-ruling-needed. |
> | Boundary posture | Human authority, project truth, and runtime-audit boundaries are not weakened by the drafted artifacts. |
> | Immutable acceptance evidence | Governance notes or checklist outputs used as acceptance evidence are bound to a git SHA or equivalent immutable evidence, and a separate accountable human approval record exists. |
>

### CLM-018 — Records

> ##### Records
>
> | Record | Status |
> |---|---|
> | `Datasheet.md` | Active local-kit artifact; reconciled to current lifecycle/reference posture. |
> | `Specification.md` | Active local-kit artifact; reconciled to current lifecycle/reference posture. |
> | `Guidance.md` | Active local-kit artifact; preserves any unresolved conflicts as current only when still true. |
> | `Procedure.md` | Active local-kit artifact; reconciled to current lifecycle/reference posture. |
> | `_STATUS.md` | Not changed by this documentation reconciliation; current state is read from that file. |
> | `_run_records/TASK_RUN_2026-05-20_1610.md` | Durable run record for this task. |
> | P3 run record | Records semantic-lensing dispositions, source rereads, validation results, and status policy outcome. |
> | Dependency records | Not created or updated by this P3 run. |

- **VER-001** — Run deterministic schema validation, source mapping, parity, checklist derivation, and render stability checks, then perform human review against the accepted legacy basis.

## Governing Values and Decisions — Axiology

### CLM-019 — Guidance: DEL-01-01 Governance Alignment, Human Authority, and Project Truth

> #### Guidance: DEL-01-01 Governance Alignment, Human Authority, and Project Truth
>

### CLM-020 — Purpose

> ##### Purpose
>
> Use this deliverable to keep the governing document set coherent while the Chirality App runtime moves toward the vNext SDK-privileged, contract-owned, Chirality-governed architecture. The work is not to add runtime implementation detail for its own sake. The work is to preserve the governance boundaries that make implementation acceptable: human authority, local filesystem project truth, accepted git history, runtime auditability, reliance-boundary ownership, product identity, and professional-boundary posture.
>

### CLM-021 — Principles

> ##### Principles
>
> 1. Human approval remains non-delegable. Agents, SDKs, tools, validators, runtime events, and domain adapters may assist, draft, record, diagnose, or validate in limited ways, but they do not approve or issue work for reliance.
> 2. Filesystem project truth controls. If a decision matters for reliance, it belongs in a proper versioned project file or accepted artifact, not only in chat, runtime logs, UI state, SDK transcripts, model context, caches, or hidden memory.
> 3. Runtime audit records explain execution. They support replay, diagnosis, and review, but they are not approval records and do not make work code-compliant, safe for reliance, issued, or professionally adequate.
> 4. Reliance boundaries are product semantics. They must be documented, implemented, and tested in Chirality terms. Do not treat prompt instructions, SDK defaults, or visible tool settings alone as sufficient boundary enforcement.
> 5. Chirality product identity must remain explicit. SDK usage may be an implementation detail, but it must not redefine public APIs, UI events, persisted events, copy, or governance language as SDK-shaped behavior.
> 6. Source uncertainty must remain visible. Use `TBD`, `ASSUMPTION`, `PROPOSAL`, source warnings, and human-ruling-needed records instead of smoothing over unsupported claims.
>

### CLM-022 — Considerations

> ##### Considerations
>
> | Area | Guidance |
> |---|---|
> | Authority order | Start with `docs/DIRECTIVE.md`, then `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/PLAN.md`, and `docs/PRD.md`; use decomposition and agent instructions for scoped execution context. |
> | PRD reference integrity | the current D-APP-38 corpus snapshot reconciled REF-006; current `_REFERENCES.md` records `docs/PRD.md` as `MATCH`. Treat older hash-mismatch warnings as historical unless a fresh corpus audit reports drift. |
> | Accepted git history | When governance notes become acceptance evidence, bind them to a git SHA or equivalent immutable evidence. Content changes after approval require review again. |
> | Evidence roles | Runtime audit records support replay, diagnosis, and review; checklist outputs organize review evidence; accepted git history or equivalent immutable evidence binds any human approval to specific content. None of these records is approval by itself unless the accountable human approval record exists. |
> | Runtime implementation detail | Include runtime specifics only when they prove or preserve a boundary, such as accepted-turn persistence, event canonicality, settings isolation, permission denial, path containment, or SDK transcript non-authority. |
> | Scope discipline | Keep remote MCP, plugins, broad tool search, shipped bypass, Windows/Linux packaging, retired PKG-08 scope, and domain-operation execution out of this deliverable except as boundary examples. |
> | Responsible party | Keep `ResponsibleParty` as `TBD` until a human assigns ownership. |
>

### CLM-023 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Recommended posture |
> |---|---|
> | Faster runtime delivery vs. governance completeness | Prefer a smaller runtime slice that preserves human gates, audit, path policy, settings isolation, and product-owned contracts. |
> | SDK convenience vs. product-owned semantics | Use SDK mechanics only behind Chirality-owned contracts, mappers, events, permission overlay, hooks, and fallback criteria. |
> | Audit richness vs. approval clarity | Preserve rich runtime records while making clear that approval is a separate human-authored project record. |
> | Local-first truth vs. convenience state | Permit convenience state only when explicitly non-authoritative and unable to override governance. |
> | Broad guidance vs. executable deliverable | Keep this deliverable at governance-alignment level; send implementation-specific requirements to the owning runtime packages unless required for a boundary check. |
>

### CLM-024 — Examples

> ##### Examples
>
> | Situation | Acceptable treatment |
> |---|---|
> | SDK transcript contains a useful event detail | Record or import the relevant detail into Chirality `HarnessEvent` form or a governed project artifact before treating it as reliance evidence. |
> | A document says a runtime event proves approval | Mark as nonconforming; runtime events explain work and do not approve work. |
> | A UI copy change implies Chirality certifies professional adequacy | Mark as nonconforming; preserve draft/decision-support posture and human authority. |
> | A dependency or source fact is plausible but unsupported | Mark `TBD` or `ASSUMPTION`; do not promote it to a requirement. |
> | A lower-authority artifact conflicts with the directive or contract | Surface the conflict and propose that the higher-authority source controls until a governed change updates the record. |
>

### CLM-025 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
> |---|---|---|---|---|---|---|
> | DEL-01-01-C002 | Dispatch path used package label `PKG-01_Governance_and_Product_Boundaries`, but the existing deliverable folder and `_CONTEXT.md` use `PKG-01_Product_Governance_and_Reliance_Boundaries`. | TASK dispatch assignment path | Existing deliverable folder, `_CONTEXT.md`, and SOFTWARE_DECOMP v3.2 package name | Run record; all document Identification sections | Use stable IDs `PKG-01` and `DEL-01-01` plus existing `_CONTEXT.md`/decomposition package name; ask human to correct the stale dispatch label if needed. | TBD |
>
> Closed historical conflict: `DEL-01-01-C001` is superseded by the current D-APP-38 corpus snapshot; REF-006
> `docs/PRD.md` now matches in `_REFERENCES.md`.
>

### CLM-026 — Rulings And Open Questions

> ##### Rulings And Open Questions
>
> | Ruling ID | Status / needed decision |
> |---|---|
> | DEL-01-01-R001 | Closed by the current D-APP-38 corpus snapshot; rerun authority-corpus status if an authority document changes. |
> | DEL-01-01-R002 | Resolved by D-APP-56 R4-P48 on 2026-07-12: preserve stable IDs and the live package path; no obsolete dispatch label is needed to discover or execute remaining work. |
> | DEL-01-01-R003 | `ResponsibleParty` assignment explicitly deferred by D-APP-56 R4-P47 on 2026-07-12; retain `TBD` until an accountable human assigns it. Assigned 2026-07-18 by D-APP-65 to Ryan Tufts (K-AUTH-1), demonstrator scope. |
> | DEL-01-01-R004 | Define final filenames and destinations for governance consistency notes, human-authority checklist, project-truth checklist, runtime-audit checklist, document diff checklist, acceptance checklist, and conflict/source-warning table. Resolved 2026-07-18 under D-APP-65 disposition 4: final filenames/destinations selected by reasoned agent judgment (D-APP-64) — see TASK_RUN_2026-07-18_DAPP65_docs_production.md; artifacts live in the deliverable folder. |

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-074 SOW-075 OBJ-009 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
