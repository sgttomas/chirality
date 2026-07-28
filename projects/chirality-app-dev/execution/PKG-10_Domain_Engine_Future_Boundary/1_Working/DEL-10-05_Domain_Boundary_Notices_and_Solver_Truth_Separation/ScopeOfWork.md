---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-10-05
package_id: PKG-10
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-071]
package_objective_refs: [OBJ-009, OBJ-010]
---

# Scope of Work — DEL-10-05

## Purpose and Objective Traceability

This Scope of Work defines `DEL-10-05` in service of project scope [SOW-071] and package objectives [OBJ-009, OBJ-010].

- **OUT-001** — Boundary notice copy, domain review checklist, and UI/documentation examples that preserve domain-engine ownership of domain truth, Chirality non-approval/non-validation/non-ownership boundaries, proposal-only semantics, and explicit human acceptance before reliance, as preserved from the exact legacy source.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-10-05 Domain Boundary Notices and Solver Truth Separation

> #### Datasheet: DEL-10-05 Domain Boundary Notices and Solver Truth Separation
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-10-05 |
> | DeliverableName | Domain Boundary Notices and Solver Truth Separation |
> | PackageID | PKG-10 |
> | PackageName | Domain Engine Future Boundary |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | ResponsibleParty | TBD |
> | Type | DOC_UPDATE |
> | ContextEnvelope | S |
> | Current Scope Posture | Future-boundary/gated scope; not current-release domain operation execution |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Covered scope item | SOW-071: domain outputs must not imply professional approval, code compliance, external validation, or solver truth | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` SOW table; `docs/PRD.md` Section 8.17 |
> | Supported objectives | OBJ-009 and OBJ-010 | `_CONTEXT.md`; decomposition objective table |
> | Primary artifact class | Boundary notice copy, domain review checklist, UI/doc examples | `_CONTEXT.md`; decomposition DEL-10-05 row |
> | Domain truth ownership rule | Domain engines own authoritative domain truth when adopted by amendment; Chirality governs interaction, proposals, records, and human gates | `docs/PRD.md` FR-106; `docs/CONTRACT.md` K-DOMAIN-1 |
> | Solver-truth separation rule | Domain-engine output must not be represented as professional approval, code compliance, external validation, or solver truth owned by Chirality | `docs/PRD.md` FR-115; `docs/CONTRACT.md` K-DOMAIN-4 |
> | Human authority rule | Professional approval, issue, reliance, standard selection, residual-risk acceptance, and conflict adjudication remain human-only | `docs/DIRECTIVE.md` Sections 2.4 and 3.2; `docs/CONTRACT.md` K-AUTH-1 and K-GATE-1 |
> | Protected-path implication | Agents may write proposals and summaries, not protected domain-engine model truth | `docs/PRD.md` FR-110 and FR-111; `docs/CONTRACT.md` K-DOMAIN-2 |
> | Operation acceptance implication | Domain operations require OperationProposal records and explicit human acceptance before application | `docs/PRD.md` FR-112 and FR-113; `docs/CONTRACT.md` K-DOMAIN-3 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Current implementation partition | D-APP-49 through D-APP-52 rule source types/guards, a closed registry, read tools, and pec-scoped loopback propose/refresh/validate tools live; endpoints, apply, protected-path hooks/writes, and general runtime remain future/gated | `docs/SPEC.md` Section 18; `docs/PRD.md` KG-016; D-APP-49 through D-APP-52 |
> | Adoption gate | Future domain-engine work requires governed amendment and stable core harness/runtime boundaries | Decomposition OI-005 and DEC-006; `docs/PRD.md` Section 8.17 |
> | Fixture posture | OpenPipeStress may be a first fixture profile if adopted, but it is not Chirality core behavior | `docs/PRD.md` FR-114; `docs/TYPES.md` Section 11.3 |
> | PRD reference integrity | WARNING: `_REFERENCES.md` records PRD ExpectedSHA256 `86cb6f...eb34` and ActualSHA256 `fb1c73...6fc8`; per dispatch, this is treated as a source status | `_REFERENCES.md`; user dispatch |
>

### CLM-005 — Construction

> ##### Construction
>
> The deliverable is constructed as a copy and review package, not an implementation package. It should provide:
>
> - Boundary notice language for UI, documentation, event records, domain profile descriptions, and operation proposal surfaces.
> - A domain review checklist that catches claims of Chirality-owned solver truth, professional approval, code compliance, external validation, or direct protected-model mutation.
> - Examples that preserve the split between domain-engine truth, deterministic adapter outputs, Chirality records/proposals, and human acceptance.
> - Future amendment notes where current source material does not define accepted domain profile details.
>

### CLM-006 — References

> ##### References
>
> | RefID | Source | Use |
> |---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | Human authority, professional boundaries, project truth hierarchy |
> | REF-002 | `docs/CONTRACT.md` | K-AUTH, K-PROF, K-DOMAIN invariants |
> | REF-003 | `docs/SPEC.md` | Future domain endpoint and profile interface posture |
> | REF-004 | `docs/TYPES.md` | Domain terms: protected path, proposal path, deterministic adapter, boundary notice |
> | REF-005 | `docs/PLAN.md` | Future domain-engine direction and OpenPipeStress fixture posture |
> | REF-006 | `docs/PRD.md` | Product requirements FR-106 through FR-115 and current-release non-goals |
> | REF-007 | `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` | DEL-10-05 scope, SOW-071, OBJ-009, OBJ-010, OI-005, DEC-006 |

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-10-05 Domain Boundary Notices and Solver Truth Separation

> #### Specification: DEL-10-05 Domain Boundary Notices and Solver Truth Separation
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-008 — Scope

> ##### Scope
>
> This deliverable specifies boundary-notice and review requirements for future domain-engine surfaces in Chirality. It covers documentation/UI/event-record copy and review checks that preserve the distinction between:
>
> - domain-engine authoritative truth,
> - deterministic adapter or domain-tool outputs,
> - Chirality proposals, summaries, manifests, and audit records,
> - explicit human acceptance and professional reliance decisions.
>
> This deliverable excludes `/api/domain/*` endpoints, operation apply, direct protected-path mutation/hooks, and general domain-runtime activation. D-APP-49 through D-APP-52 separately authorize the staged-live source-type/guard, closed-registry, read-tool, and pec-scoped loopback propose/refresh/validate surface; this copy/review deliverable does not own that implementation.
>

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source | Verification |
> |---|---|---|---|
> | REQ-001 | Boundary notices MUST state that Chirality does not approve, validate, certify, issue, sign, seal, or externally validate professional work. | `docs/DIRECTIVE.md` Sections 2.4, 3.2; `docs/CONTRACT.md` K-AUTH-1 | Copy review confirms no automated approval/validation claim. |
> | REQ-002 | Boundary notices MUST state that Chirality does not own solver truth and does not become the domain solver. | `docs/PRD.md` FR-106, FR-115; `docs/CONTRACT.md` K-DOMAIN-1, K-DOMAIN-4 | Copy review confirms solver-truth ownership is assigned to the domain engine/domain tool, not Chirality. |
> | REQ-003 | UI/documentation/event copy MUST NOT represent domain-engine output as professional approval, code compliance, external validation, or Chirality-owned solver truth. | `docs/PRD.md` FR-115; decomposition SOW-071 | Checklist review flags prohibited claims. |
> | REQ-004 | Domain operation copy MUST require explicit human acceptance before any applied operation is treated as accepted domain state. | `docs/PRD.md` FR-113; `docs/CONTRACT.md` K-DOMAIN-3 and K-GATE-1 | Operation-related copy includes human-gate language. |
> | REQ-005 | Protected domain artifact copy MUST distinguish protected paths from agent-writable proposal or summary paths. | `docs/PRD.md` FR-110, FR-111; `docs/CONTRACT.md` K-DOMAIN-2; `docs/TYPES.md` Section 11.3 | Review confirms no direct agent-write language for protected model truth. |
> | REQ-006 | OpenPipeStress examples, if used, MUST describe it as a possible fixture profile and not as Chirality core behavior. | `docs/PRD.md` FR-114; `docs/TYPES.md` Section 11.3 | Example review confirms fixture-only language. |
> | REQ-007 | Domain-surface wording MUST distinguish the D-APP-49 through D-APP-52 staged-live types/guards, registry, read tools, and pec-scoped propose/refresh/validate tools from still-gated endpoints, apply, protected-path hooks/writes, and general runtime. | `docs/SPEC.md` Section 18; `docs/PRD.md` KG-016; D-APP-49 through D-APP-52 | Scope review confirms the staged partition without implying broader activation. |
> | REQ-008 | Unsupported domain-profile or solver-specific details MUST remain `TBD`, `ASSUMPTION`, `PROPOSAL`, or a human-ruling item. | Skill contract; `_REFERENCES.md` notes | Document review confirms no invented solver facts. |
>

### CLM-010 — Standards

> ##### Standards
>
> No external engineering code or domain-solver standard is selected by this deliverable. Governing project standards for this slice are the Chirality governance and product documents listed in `_REFERENCES.md`.
>
> | Standard/Control | Status |
> |---|---|
> | Chirality professional-boundary invariants | Applicable from `docs/DIRECTIVE.md` and `docs/CONTRACT.md` |
> | Chirality domain-engine future requirements | Applicable from `docs/PRD.md` FR-106 through FR-115 |
> | DomainEngineProfile accepted schema | TBD: no accepted generic profile specification exists yet per `docs/PRD.md` KG-017 |
> | Engine-specific solver validation standards | TBD: out of scope until a future amendment and domain profile identify the engine and governing standards |
>

### CLM-011 — Verification

> ##### Verification
>
> | Check | Pass Criteria |
> |---|---|
> | Prohibited claim scan | No copy says or implies Chirality approves, validates, certifies, issues, signs, seals, proves code compliance, externally validates, or owns solver truth. |
> | Ownership separation scan | Domain-engine/tool outputs, Chirality records, and human acceptance are separately named. |
> | Scope gate scan | Domain-engine operation execution remains future-boundary/gated scope. |
> | Protected/proposal path scan | Protected domain paths are not described as agent-writable; proposal/review aid paths are distinct. |
> | Fixture scan | OpenPipeStress is fixture/profile language only, not core runtime behavior. |
> | Unsupported fact scan | Missing solver/profile specifics are marked TBD, ASSUMPTION, PROPOSAL, or human-ruling items. |
> | Surface inventory scan | Each selected future surface category has either a required notice pattern or an explicit out-of-scope rationale. Selected surfaces are `TBD` until a future amendment identifies accepted UI, documentation, API, event-record, profile, or proposal-record locations. |
> | OperationProposal schema scan | Operation-proposal notice examples are not used as closure evidence unless an accepted upstream `OperationProposal` schema or record shape is cited; until then, operation-proposal examples remain `PROPOSAL` copy only. |
>

### CLM-012 — Documentation

> ##### Documentation
>
> This deliverable produces and maintains:
>
> - Boundary notice copy.
> - Domain review checklist.
> - UI/documentation examples.
> - Human-ruling list for unresolved future-amendment details.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
> - Surface inventory or out-of-scope rationale for selected future surfaces.
> - OperationProposal schema citation status before operation-proposal examples are used for closure evidence.

- **AC-001** — PASS when the source-preserving contract contains the exact legacy boundary notices, review checklist, and UI/documentation examples; makes no claim that Chirality approves, validates, certifies, owns, or professionally relies on solver results; keeps proposals and review aids non-binding; authorizes no protected-path mutation or operation approval; and maps the output to SOW-071 and OBJ-009/OBJ-010 with every legacy source line dispositioned.

## Production and Verification Method — Praxeology

### CLM-013 — Procedure: DEL-10-05 Domain Boundary Notices and Solver Truth Separation

> #### Procedure: DEL-10-05 Domain Boundary Notices and Solver Truth Separation
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-014 — Purpose

> ##### Purpose
>
> Use this procedure to produce or review boundary-notice copy for future domain-engine surfaces without activating domain-engine implementation or implying Chirality-owned solver truth.
>

### CLM-015 — Prerequisites

> ##### Prerequisites
>
> - Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and the current four-document kit.
> - Confirm `ResponsibleParty` remains `TBD` unless a human assigns ownership.
> - Confirm PKG-10 remains future-boundary/gated scope unless a governed amendment says otherwise.
> - Confirm no accepted upstream dependency edges are available yet; `_DEPENDENCIES.md` records upstream/downstream as TBD.
> - Use `docs/DIRECTIVE.md`, `docs/CONTRACT.md`, `docs/PRD.md`, `docs/SPEC.md`, `docs/TYPES.md`, and the v3.2 SOFTWARE_DECOMP as source authority.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
>

### CLM-016 — Steps

> ##### Steps
>
> 1. Identify the domain-engine surface under review.
>    - Examples: UI result panel, operation proposal record, domain profile documentation, event record summary, protected artifact warning, fixture-profile example.
>
> 2. Classify the surface.
>    - Mark it as one or more of: domain output, operation proposal, protected artifact, proposal/review aid, fixture profile, human acceptance gate, documentation example.
>
> 3. Apply the required notice pattern.
>    - Use the standard notice for documentation and durable records.
>    - Use the compact UI notice where space is constrained.
>    - Use operation proposal, protected artifact, or fixture notices where the surface matches those categories.
>
> 4. Check for prohibited claims.
>    - Reject or revise any wording that says or implies Chirality approves, validates, certifies, issues, signs, seals, externally validates, proves code compliance, decides professional adequacy, or owns solver truth.
>
> 5. Check ownership separation.
>    - Confirm domain-engine outputs, deterministic checks, Chirality records/proposals, protected artifacts, and human acceptance are not conflated.
>
> 6. Check future-boundary posture.
>    - If the copy references domain endpoints, adapters, OpenPipeStress, protected domain paths, operation application, or profile validation, ensure it is framed as future-boundary/gated scope unless an accepted amendment exists.
>
> 7. Mark unsupported details.
>    - Use `TBD` for missing accepted facts.
>    - Use `ASSUMPTION:` for best-effort inference.
>    - Use `PROPOSAL:` for proposed copy or workflow wording.
>    - Add or update a conflict table when source materials disagree or require human judgment.
>
> 8. Record review outcome.
>    - Note pass/fail against the checklist in `Guidance.md`.
>    - Record any human-ruling items.
>    - Record the reviewed surface, reviewer, review date, source-warning status, closure verdict, unresolved human rulings, and carryforward items using the review output record fields below.
>    - Do not create or update `Dependencies.csv` as part of this procedure.
>

### CLM-017 — Verification

> ##### Verification
>
> | Verification Item | Method |
> |---|---|
> | Notice present | Confirm every domain-engine surface has a boundary notice appropriate to its category. |
> | Prohibited claims absent | Search/review for approve, validate, certify, issue, sign, seal, code compliance, external validation, professional adequacy, and solver truth ownership claims. |
> | Human gate preserved | Confirm accepted domain state or reliance decisions require accountable human acceptance. |
> | Protected paths preserved | Confirm protected domain artifacts are not described as directly agent-writable. |
> | Future scope preserved | Confirm current-release implementation is not implied. |
> | Unsupported facts labeled | Confirm unknowns are `TBD`, `ASSUMPTION`, `PROPOSAL`, or conflict-table items. |
> | Closure evidence complete | Confirm the review output record includes reviewed surface, reviewer, date, checklist result, source-warning status, unresolved human rulings, and closure verdict. |
> | PRD warning maintained | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
>

### CLM-018 — Review Output Record

> ##### Review Output Record
>
> Use this minimum record shape for each boundary-notice review until a future product-native record is accepted:
>
> | Field | Required Content |
> |---|---|
> | Reviewed surface | UI, documentation, event record, domain profile, operation proposal, protected artifact notice, fixture example, or other named surface. |
> | Reviewed source | File/path, screen, mockup, record, or proposed copy location reviewed. |
> | Reviewer | Accountable reviewer name or `TBD` if not yet assigned. |
> | Review date | Calendar date or `TBD`. |
> | Checklist result | Pass/fail for each `Guidance.md#Domain Review Checklist` row, or a reference to the completed checklist. |
> | Notice pattern used | Standard, compact UI, operation proposal, protected artifact, fixture, or `TBD`. |
> | Source-warning status | PRD hash warning open/closed/waived; closure evidence must cite the reconciliation or waiver record. |
> | Human-ruling carryforward | Unresolved wording, profile-location, engine-specific, source-warning, or acceptance-authority questions. |
> | Closure verdict | `PROPOSAL`, `BLOCKED`, `READY_FOR_HUMAN_RULING`, or `ACCEPTED_BY_HUMAN` with evidence. |
>

### CLM-019 — Closure Evidence

> ##### Closure Evidence
>
> A reviewed notice package is not complete merely because copy exists. Closure evidence must show:
>
> - Required notice pattern or out-of-scope rationale for each selected future surface category.
> - Completed checklist capture location, or `TBD` when no accepted storage location exists.
> - OperationProposal schema citation status before operation-proposal notice examples are used as closure evidence.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
> - Unresolved human-ruling items carried forward explicitly.
>

### CLM-020 — Records

> ##### Records
>
> - Reviewed boundary notice copy.
> - Completed domain review checklist from `Guidance.md`.
> - Human-ruling list for unresolved wording, profile, or engine-specific questions.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
> - Review output record containing reviewed surface, reviewer, date, checklist result, source-warning status, closure verdict, and human-ruling carryforward.
> - This deliverable's `_STATUS.md` lifecycle state.

- **VER-001** — Validate the SOW_V1 schema under exact MIGRATION_DUAL authority; map and report parity for every legacy source line; derive the exact AC checklist; render deterministically; and review the preserved notice copy for proposal-only language, solver-truth separation, and absence of added solver reliance or certification, protected-path mutation, operation approval, lifecycle meaning, or semantic obligation.

## Governing Values and Decisions — Axiology

### CLM-021 — Guidance: DEL-10-05 Domain Boundary Notices and Solver Truth Separation

> #### Guidance: DEL-10-05 Domain Boundary Notices and Solver Truth Separation
>
> > **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.
>

### CLM-022 — Purpose

> ##### Purpose
>
> Use this deliverable to keep future domain-engine language clear, conservative, and reviewable. Chirality may govern interaction, proposal records, audit records, adapter policy, protected/proposal path boundaries, and human gates. It must not present itself as the domain solver, the professional approver, the code-compliance authority, or the owner of solver truth.
>

### CLM-023 — Principles

> ##### Principles
>
> 1. Keep ownership explicit: the domain engine or deterministic adapter owns its domain output; Chirality owns the governed interaction record; humans own acceptance and professional reliance decisions.
> 2. Use boundary notices wherever domain outputs, proposed domain operations, protected artifacts, or fixture profiles are shown to users.
> 3. Treat future domain-engine work as gated amendment scope until the accepted project state says otherwise.
> 4. Separate proposal language from acceptance language. "Proposed", "review aid", "summary", and "candidate operation" are non-binding; "accepted" requires explicit human evidence.
> 5. Prefer concrete prohibitions over vague disclaimers. State what Chirality does not do: approve, validate, certify, issue, sign, seal, prove compliance, or own solver truth.
>

### CLM-024 — Considerations

> ##### Considerations
>
> - Domain-engine boundary language overlaps with general professional-boundary language in `docs/DIRECTIVE.md` and `docs/CONTRACT.md`; keep the wording mutually consistent.
> - REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.
> - DomainEngineProfile details remain future work. Do not invent profile fields beyond the source-backed set: engine identity, optional version, protected paths, proposal paths, artifact types, operations, manifest rules, and boundary notices.
> - OpenPipeStress may be useful as a first fixture profile, but examples must not hardcode OpenPipeStress assumptions into Chirality core behavior.
> - Runtime events, adapter results, and deterministic checks can support review; they do not make a deliverable professionally reliable by themselves.
> - The notice wording below is proposal-quality copy until an accountable human accepts it for a specific future UI, documentation, event-record, profile, or operation-proposal surface.
>

### CLM-025 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Guidance |
> |---|---|
> | Strong notice vs. concise UI | Keep UI notice short but unambiguous; put longer rationale in documentation and review checklists. |
> | Future compatibility vs. premature implementation | Preserve terms, examples, and requirements that keep a future path open; do not describe endpoints/tools as active current-release capabilities. |
> | Adapter validation vs. professional validation | Deterministic adapters can validate format, manifest, operation preconditions, or profile rules; they do not replace professional review or acceptance. |
> | Fixture examples vs. product identity | Fixture examples can make boundaries concrete, but must remain marked as profiles/adapters outside Chirality core. |
>

### CLM-026 — Boundary Notice Copy

> ##### Boundary Notice Copy
>

### CLM-027 — Standard Notice

> ###### Standard Notice
>
> Chirality records and governs domain-engine interactions, proposals, and review evidence. It does not approve, certify, issue, sign, seal, prove code compliance, externally validate, or own solver truth. Domain results require review and explicit acceptance by an accountable human before reliance.
>

### CLM-028 — Compact UI Notice

> ###### Compact UI Notice
>
> Domain output is a review aid. Chirality does not approve, validate, or own solver truth. Human acceptance is required before reliance.
>

### CLM-029 — Operation Proposal Notice

> ###### Operation Proposal Notice
>
> This operation is a proposal. It identifies candidate inputs, checks, intended changes, risks, and outputs for human review. It does not apply accepted domain state until the required human gate is completed.
>

### CLM-030 — Protected Artifact Notice

> ###### Protected Artifact Notice
>
> Protected domain artifacts are not agent-writable Chirality files. Agents may write proposals, summaries, and review aids only; accepted domain-state changes require an approved adapter or operation workflow and explicit human acceptance.
>

### CLM-031 — Fixture Notice

> ###### Fixture Notice
>
> OpenPipeStress, if used, is a fixture profile or adapter example. Its assumptions belong in the profile/adapter layer and must not be treated as Chirality core runtime behavior.
>

### CLM-032 — Domain Review Checklist

> ##### Domain Review Checklist
>
> | Check | Question | Expected Answer |
> |---|---|---|
> | Professional authority | Does the copy avoid claims that Chirality approves, signs, seals, certifies, issues, transmits, or releases work for reliance? | Yes |
> | Code compliance | Does the copy avoid claims that Chirality proves code compliance or professional adequacy? | Yes |
> | Solver truth | Does the copy avoid claims that Chirality owns solver truth? | Yes |
> | Domain truth | Does the copy state or imply that authoritative domain truth belongs to the domain engine/domain workflow, not Chirality? | Yes |
> | Human gate | Does accepted domain state require explicit human acceptance? | Yes |
> | Protected paths | Are protected domain artifacts separated from proposal/review-aid paths? | Yes |
> | Current scope | Is domain operation execution marked future-boundary/gated where relevant? | Yes |
> | Fixture posture | Is OpenPipeStress treated as a fixture profile if mentioned? | Yes |
> | Unsupported facts | Are missing details marked TBD, ASSUMPTION, PROPOSAL, or human-ruling items? | Yes |
>

### CLM-033 — Completed Checklist Capture

> ##### Completed Checklist Capture
>
> Completed checklist evidence should be captured as part of the review output record described in `Procedure.md#Review Output Record`. Until a future amendment defines a product-native storage location, the capture location is `TBD` and the completed checklist is closure support only, not a human approval record.
>

### CLM-034 — Examples

> ##### Examples
>
> | Context | Acceptable Wording | Avoid |
> |---|---|---|
> | Domain result panel | "Result imported from the domain engine for review. Chirality records the interaction and does not own solver truth." | Any claim that Chirality has validated the domain result. |
> | Operation proposal | "Proposed operation pending human acceptance." | Any claim that Chirality has approved the operation. |
> | Compliance note | "Reviewer must determine whether the result supports project requirements and applicable standards." | Any claim that the output establishes code compliance. |
> | Protected artifact | "Write a proposal or summary; do not directly modify protected model truth." | Any claim that an agent may update protected solver model files directly. |
> | Fixture mention | "OpenPipeStress fixture profile, if adopted by amendment." | Any claim that OpenPipeStress is Chirality core behavior. |
>

### CLM-035 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
> |---|---|---|---|---|---|---|
> | CT-001 | PRD source hash status: MATCH recorded in `_REFERENCES.md`; dispatch instructs treating MATCH as source status. | `_REFERENCES.md` REF-006 expected/actual SHA values | User dispatch instruction | Datasheet Conditions; Specification Documentation; this Guidance section | Use current accessible `docs/PRD.md` for P1/P2 drafting while preserving the warning until reconciled. | TBD — reconciled under D-APP-38 |
>

### CLM-036 — Human Rulings Needed

> ##### Human Rulings Needed
>
> - Confirm whether the standard and compact boundary notices are accepted wording or remain proposal copy.
> - Confirm who may accept proposed boundary notice copy as sufficient for specific future surfaces.
> - Confirm future `DomainEngineProfile` copy locations once DEL-10-01 is accepted.
> - Confirm engine-specific wording if OpenPipeStress or another domain engine is adopted by amendment.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-071 OBJ-009 OBJ-010 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
