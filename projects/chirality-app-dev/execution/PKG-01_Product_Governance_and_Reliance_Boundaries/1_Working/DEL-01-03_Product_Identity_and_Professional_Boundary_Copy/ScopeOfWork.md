---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-01-03
package_id: PKG-01
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@0724f26f6ef79d733c8f1c513b29d837fd43c8eb
project_scope_refs: [SOW-071, SOW-074]
package_objective_refs: [OBJ-009, OBJ-010]
---

# Scope of Work — DEL-01-03

## Purpose and Objective Traceability

This Scope of Work defines `DEL-01-03` in service of project scope [SOW-071, SOW-074] and package objectives [OBJ-009, OBJ-010].

- **OUT-001** — Product-identity and professional-boundary copy guidance and review record for DEL-01-03, traceable to SOW-071, SOW-074, OBJ-009, and OBJ-010.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-01-03 Product Identity and Professional Boundary Copy

> #### Datasheet: DEL-01-03 Product Identity and Professional Boundary Copy
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | PackageID | PKG-01 |
> | PackageName | Product Governance and Reliance Boundaries |
> | DeliverableID | DEL-01-03 |
> | DeliverableName | Product Identity and Professional Boundary Copy |
> | ResponsibleParty | TBD |
> | Type | DOC_UPDATE |
> | ContextEnvelope | S |
> | Current lifecycle state | Read from `_STATUS.md` (currently `IN_PROGRESS`; prior states remain historical evidence) |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary product identity | Chirality desktop harness and bundled agent operating system | `docs/DIRECTIVE.md` header; `docs/PRD.md` header |
> | Product posture | Local-first governed desktop harness for running AI agents against a user-selected filesystem workspace | `docs/DIRECTIVE.md` Section 1; `docs/PRD.md` Section 2 |
> | Identity boundary | User-facing text must identify the product as Chirality, not Claude Code, Anthropic, a vendor CLI, or a feature-parity target | `docs/DIRECTIVE.md` Section 2.11; `docs/CONTRACT.md` K-SDK-4; `docs/PRD.md` Section 3.2 |
> | Professional authority posture | Agents propose; humans approve and retain binding decision rights | `docs/DIRECTIVE.md` Section 3; `docs/CONTRACT.md` K-AUTH-1 through K-GATE-1 |
> | Draft status of agent outputs | Agent outputs are drafts and decision support until accepted by an accountable human | `docs/DIRECTIVE.md` Section 3.1 and Section 3.4; `docs/PRD.md` Section 2 |
> | Reliance-boundary posture | Product-critical boundaries must be documented, implemented, and tested in Chirality terms; prompt text alone is insufficient | `docs/DIRECTIVE.md` Section 2.9; `docs/CONTRACT.md` K-RELIANCE-1 and K-RELIANCE-2 |
> | Domain-engine boundary posture | Domain engines own domain truth; Chirality governs interaction, proposals, records, and human gates | `docs/CONTRACT.md` K-DOMAIN-1 through K-DOMAIN-4; `docs/SPEC.md` Section 18 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Required treatment | Source |
> |---|---|---|
> | UI, documentation, packaging, runtime messages, and future domain notices mention the product | Use Chirality-owned product language; do not imply the product is Claude Code or an Anthropic product | `_CONTEXT.md` Deliverable Scope; `docs/DIRECTIVE.md` Section 2.11; `docs/PRD.md` FR-127 |
> | Agent output, runtime event, validator result, SDK transcript, or domain-adapter output is presented to a user | Preserve draft/non-binding wording unless a human approval record exists | `docs/DIRECTIVE.md` Sections 2.3 and 3; `docs/CONTRACT.md` K-BIND-1 |
> | Copy refers to approval, certification, code compliance, external validation, issuance, signature, seal, transmittal, or release for reliance | Reserve the action for accountable humans; do not attribute it to Chirality, agents, SDKs, tools, validators, runtime events, or domain adapters | `docs/DIRECTIVE.md` Section 3.2; `docs/CONTRACT.md` K-AUTH-1 and K-PROF-1 |
> | Copy refers to SDK integration | Describe SDK use as implementation/provider detail behind Chirality-owned contracts, not as product identity or governance authority | `docs/DIRECTIVE.md` Sections 2.8 and 2.11; `docs/CONTRACT.md` K-ENGINE-3 |
> | Copy refers to future domain engines | State that domain-operation acceptance is human-gated and domain outputs are not Chirality-owned solver truth | `docs/PRD.md` Section 8.17; `docs/SPEC.md` Section 18 |
>

### CLM-005 — Construction

> ##### Construction
>
> The deliverable is a documentation and copy-boundary package. Anticipated artifacts from `_CONTEXT.md` are:
>
> - UI copy guidelines.
> - Release review checklist.
> - Boundary notice examples.
>
> ADQ-03 materialized the shared checklist and example package at `docs/BOUNDARY_REVIEW_CHECKLISTS.md`.
> That file is review evidence only; it does not assign `ResponsibleParty`, satisfy dependencies, issue
> this deliverable, or approve release/professional reliance.
>
> | Artifact | Current location in this deliverable | Final destination path | Source |
> |---|---|---|---|
> | UI copy guidelines | This `ScopeOfWork.md` CLM-025–029 | `docs/BOUNDARY_REVIEW_CHECKLISTS.md` Professional Boundary Checklist and Boundary Notice Examples | `_CONTEXT.md` Anticipated Artifacts; decomposition DEL-01-03 AnticipatedArtifacts |
> | Release review checklist | This `ScopeOfWork.md` CLM-018/020 | `docs/BOUNDARY_REVIEW_CHECKLISTS.md` Review Evidence Template | `_CONTEXT.md` Anticipated Artifacts; `docs/DIRECTIVE.md` Sections 2.4 and 3.2 |
> | Boundary notice examples | This `ScopeOfWork.md` CLM-029 | `docs/BOUNDARY_REVIEW_CHECKLISTS.md` Boundary Notice Examples | `_CONTEXT.md` Anticipated Artifacts; `docs/CONTRACT.md` K-AUTH-1 and K-DOMAIN-4 |
> | Review notes | This `ScopeOfWork.md` CLM-021 | `docs/BOUNDARY_REVIEW_CHECKLISTS.md` Finding Template | `docs/DIRECTIVE.md` Section 2.5; `docs/CONTRACT.md` K-INVENT-1 and K-CONFLICT-1 |
>

### CLM-006 — References

> ##### References
>
> | RefID | Source | Use |
> |---|---|---|
> | REF-001 | `docs/DIRECTIVE.md` | Founding intent, product identity, professional responsibility, evidence posture |
> | REF-002 | `docs/CONTRACT.md` | Binding invariants for authority, identity, reliance boundaries, domain boundaries |
> | REF-003 | `docs/SPEC.md` | Physical structures, persona composer professional-boundary reminders, domain future boundary |
> | REF-004 | `docs/TYPES.md` | Stable identifiers, project truth, artifact vocabulary, human approval authority |
> | REF-005 | `docs/PLAN.md` | Product identity and release/local-check posture |
> | REF-006 | `docs/PRD.md` | Product requirements and accepted vNext runtime direction; the current D-APP-38 corpus snapshot records a matching authority-doc hash |
> | REF-007 | `agents/AGENT_SOFTWARE_DECOMP.md` | Decomposition method context; no copy requirements extracted |

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-01-03 Product Identity and Professional Boundary Copy

> #### Specification: DEL-01-03 Product Identity and Professional Boundary Copy
>

### CLM-008 — Scope

> ##### Scope
>
> This deliverable specifies copy requirements for preserving Chirality product identity and human-only professional authority across UI, documentation, packaging, runtime messages, and future domain notices.
>
> Included:
>
> - Product identity language for Chirality-owned surfaces.
> - Professional-boundary language for draft output, human approval, reliance, and release.
> - Boundary notice requirements for future domain-engine surfaces.
> - Release-review checks for identity and professional-boundary copy.
>
> Excluded:
>
> - Runtime implementation details except where copy must reflect product-owned boundaries.
> - Dependency satisfaction closure; `Dependencies.csv` exists, but its rows remain `SatisfactionStatus=TBD` pending downstream FULL_GRAPH/cycle checks and any human closure decisions.
> - Final assignment of `ResponsibleParty`; it remains TBD.
> - Current-release domain operation implementation.
>

### CLM-009 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source |
> |---|---|---|
> | REQ-01 | User-facing copy MUST identify the product as Chirality and describe Chirality's governed-work posture. | `docs/DIRECTIVE.md` Section 2.11; `docs/PLAN.md` Section 6.5 |
> | REQ-02 | User-facing copy MUST NOT make Chirality appear to be Claude Code, an Anthropic product, a vendor CLI, or a feature-parity target. | `docs/DIRECTIVE.md` Section 2.11; `docs/PRD.md` Section 3.2; `docs/CONTRACT.md` K-SDK-4 |
> | REQ-03 | SDK references, when needed, MUST be framed as implementation/provider detail behind Chirality-owned contracts. | `docs/DIRECTIVE.md` Sections 2.8 and 2.10; `docs/CONTRACT.md` K-ENGINE-1 through K-ENGINE-4 |
> | REQ-04 | Copy MUST state or preserve that agent outputs are drafts or decision support until accepted by an accountable human through a governed process. | `docs/DIRECTIVE.md` Sections 3.1 and 3.4; `docs/PRD.md` Section 2 |
> | REQ-05 | Copy MUST NOT state or imply that an AI system, agent, tool, SDK, transcript, runtime event, deterministic validator, or domain adapter can approve, certify, sign, seal, issue, transmit, externally validate, or release professional work for reliance. | `docs/DIRECTIVE.md` Section 3.2; `docs/CONTRACT.md` K-AUTH-1; `docs/PRD.md` Section 3.2 |
> | REQ-06 | Copy MUST distinguish non-binding records such as drafts, proposals, summaries, and runtime transcripts from binding approval records. | `docs/CONTRACT.md` K-BIND-1; `docs/DIRECTIVE.md` Sections 2.3 and 3 |
> | REQ-07 | Copy that describes reliance boundaries MUST NOT imply prompt text or opaque SDK defaults are sufficient enforcement for product-critical safety, audit, filesystem, lifecycle, transcript, settings, subagent, or human-gate semantics. | `docs/DIRECTIVE.md` Section 2.9; `docs/CONTRACT.md` K-RELIANCE-2; `docs/PRD.md` FR-124 and FR-125 |
> | REQ-08 | Future domain-engine notices MUST state that domain engines own authoritative domain truth and Chirality does not own solver truth, code compliance, external validation, or professional approval. | `docs/CONTRACT.md` K-DOMAIN-1 and K-DOMAIN-4; `docs/SPEC.md` Section 18; `docs/PRD.md` FR-115 |
> | REQ-09 | Copy for future domain operations MUST preserve explicit human acceptance before any domain operation is applied. | `docs/CONTRACT.md` K-DOMAIN-3; `docs/SPEC.md` Section 18; `docs/PRD.md` FR-113 |
> | REQ-10 | Copy and review artifacts MUST preserve explicit uncertainty when source support is missing; unknowns remain `TBD`, assumptions are labeled, and conflicts are surfaced. | `docs/DIRECTIVE.md` Section 2.5; `docs/CONTRACT.md` K-INVENT-1 and K-CONFLICT-1 |
>

### CLM-010 — Standards

> ##### Standards
>
> | Standard / authority | Status | Application |
> |---|---|---|
> | `docs/DIRECTIVE.md` | Accessible | Governs intent, product identity, professional responsibility, evidence posture |
> | `docs/CONTRACT.md` | Accessible | Governs binding copy invariants |
> | `docs/SPEC.md` | Accessible | Governs runtime/document structures and future domain specification boundary |
> | `docs/TYPES.md` | Accessible | Governs vocabulary for project truth, artifacts, stable IDs, and authority |
> | `docs/PLAN.md` | Accessible | Governs roadmap/release copy checks |
> | `docs/PRD.md` | Accessible; the current D-APP-38 corpus snapshot records matching REF-006 authority-doc hashes | Governs product requirements and accepted vNext direction |
>

### CLM-011 — Verification

> ##### Verification
>
> | Requirement | Verification approach |
> |---|---|
> | REQ-01, REQ-02 | Review UI labels, empty states, permission prompts, status-transition messages, runtime/session summaries, documentation, packaging metadata, release notes, and future domain notices for Chirality-owned identity and absence of Claude Code/Anthropic product-identity claims. |
> | REQ-03 | Review SDK-related copy for implementation-detail framing and Chirality-owned contract language. |
> | REQ-04 through REQ-06 | Review copy for draft/non-binding language and human-only approval language. |
> | REQ-07 | Review reliance-boundary copy for non-prompt-only enforcement language and concrete ownership references. |
> | REQ-08, REQ-09 | Review future domain notices for domain-truth separation and explicit human acceptance. |
> | REQ-10 | Review deliverable and downstream copy for `TBD`, `ASSUMPTION`, `PROPOSAL`, and conflict labeling where source support is incomplete. |
>
> Closure evidence before downstream production copy updates:
>
> - `ResponsibleParty` assigned by an accountable human: TBD.
> - Final destination paths for UI copy guidelines, release review checklist, boundary notice examples, and review notes: `docs/BOUNDARY_REVIEW_CHECKLISTS.md` (ADQ-03 review evidence only).
> - `Dependencies.csv` satisfaction and any project-level FULL_GRAPH/cycle checks closed or explicitly deferred by a human: TBD.
> - Conflict Table CT-001 path-label ruling recorded or explicitly deferred: TBD. Historical CT-002 PRD hash warning is closed by the current D-APP-38 corpus snapshot.
> - Release review evidence record completed for the checked surfaces and source sections: TBD.
>

### CLM-012 — Documentation

> ##### Documentation
>
> Required or anticipated artifacts:
>
> - UI copy guidelines: `docs/BOUNDARY_REVIEW_CHECKLISTS.md`.
> - Release review checklist: `docs/BOUNDARY_REVIEW_CHECKLISTS.md`.
> - Boundary notice examples: `docs/BOUNDARY_REVIEW_CHECKLISTS.md`.
> - Review notes template: `docs/BOUNDARY_REVIEW_CHECKLISTS.md`.
>
> TBD:
>
> - Human assignment of `ResponsibleParty`.
> - Human closure decision for `Dependencies.csv` rows whose `SatisfactionStatus` remains `TBD`.
>

### CLM-013 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-103 records the post-D-APP-53 state: the dependency-reconciliation act is human-closed and the earlier INSP-03 dependency wording is historical. This does not imply every dependency is satisfied or any lifecycle transition.

- **AC-001** — The Scope of Work preserves the DEL-01-03 legacy source content and traceability to SOW-071, SOW-074, OBJ-009, and OBJ-010.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-01-03 Product Identity and Professional Boundary Copy

> #### Procedure: DEL-01-03 Product Identity and Professional Boundary Copy
>

### CLM-015 — Purpose

> ##### Purpose
>
> This procedure describes how to produce and use product-identity and professional-boundary copy for DEL-01-03 without inventing unsupported claims or weakening Chirality's governance posture.
>

### CLM-016 — Prerequisites

> ##### Prerequisites
>
> - Read `_CONTEXT.md` for deliverable identity, scope, artifacts, and `ResponsibleParty: TBD`.
> - Read `_REFERENCES.md` for the authoritative source corpus and hash status.
> - Read `_DEPENDENCIES.md` and `Dependencies.csv`; dependency extraction has produced active rows, but satisfaction status remains `TBD` pending downstream FULL_GRAPH/cycle checks and human closure decisions.
> - Read relevant source slices from:
>   - `docs/DIRECTIVE.md`
>   - `docs/CONTRACT.md`
>   - `docs/SPEC.md`
>   - `docs/TYPES.md`
>   - `docs/PLAN.md`
>   - `docs/PRD.md` under the current D-APP-38 corpus snapshot
>   - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md`
>

### CLM-017 — Steps

> ##### Steps
>
> 1. Confirm stable identity.
>    - Use `DEL-01-03`, `PKG-01`, and the canonical deliverable name from `_CONTEXT.md`.
>    - Keep `ResponsibleParty` as `TBD` until a human assigns ownership.
>
> 2. Establish source authority.
>    - Use `docs/DIRECTIVE.md` for intent, product identity, professional responsibility, evidence posture, and source hierarchy.
>    - Use `docs/CONTRACT.md` for binding invariants.
>    - Use `docs/PRD.md` for accepted vNext product requirements under the current D-APP-38 corpus snapshot reference state.
>
> 3. Draft or review product identity copy.
>    - Confirm the surface names Chirality as the product.
>    - Confirm SDK/provider references are implementation detail, not product identity.
>    - Remove or flag copy that makes Chirality appear to be Claude Code, Anthropic, a vendor CLI, or a feature-parity target.
>
> 4. Draft or review professional-boundary copy.
>    - State that agent outputs are drafts, proposals, or decision support until accepted by an accountable human.
>    - Reserve approval, certification, signature, seal, issue, transmittal, release for reliance, residual-risk acceptance, and professional judgment for humans.
>    - Flag copy that conflates runtime events, transcripts, validators, or generated artifacts with approval records.
>
> 5. Draft or review reliance-boundary copy.
>    - Confirm product-critical boundaries are described as Chirality-owned or verified through concrete enforcement surfaces.
>    - Flag statements that rely on prompt text, model behavior, or opaque SDK defaults alone for safety or authority.
>
> 6. Draft or review future domain-engine notices.
>    - State that domain engines own authoritative domain truth where applicable.
>    - State that Chirality governs interaction, proposals, records, and human gates.
>    - State that domain-engine outputs are not Chirality-owned solver truth, code compliance, external validation, or professional approval.
>
> 7. Preserve uncertainty.
>    - Mark missing target paths, owner assignments, and unsupported implementation details as `TBD`.
>    - Mark inferred guidance as `ASSUMPTION`.
>    - Add conflicts requiring judgment to the Conflict Table in this `ScopeOfWork.md` CLM-030.
>
> 8. Prepare release review evidence.
>    - Record the surfaces checked.
>    - Record source sections used.
>    - Record any `TBD`, `ASSUMPTION`, or human-ruling-needed item.
>    - Record reviewer name or role, review date, pass/fail result, findings, proposed copy, and human ruling status.
>    - Include authority-corpus status and Conflict Table status as explicit evidence checkpoints.
>
> 9. Route authority-sensitive wording.
>    - If copy uses approve, certify, sign, seal, issue, transmit, release, externally validate, code-compliant, solver truth, or safe for reliance, record the exact phrase and route it to the accountable human or human review body.
>    - If no accountable role has been assigned, record `TBD` rather than approving the wording.
>    - Do not close the item until the human ruling or deferral is recorded.
>

### CLM-018 — Verification

> ##### Verification
>
> | Check | Pass condition | Evidence fields |
> |---|---|---|
> | Identity check | Product-facing copy names Chirality and does not present the app as Claude Code, Anthropic, or a vendor CLI. | Surface; copy excerpt; source section; pass/fail; finding ID |
> | SDK framing check | SDK references are implementation/provider detail behind Chirality-owned contracts. | Surface; SDK phrase; source section; pass/fail; finding ID |
> | Human authority check | No copy claims automated approval, certification, issue, signature, seal, external validation, code compliance, or release for reliance. | Surface; authority-sensitive phrase; routed-to human role; ruling status |
> | Binding-record check | Drafts, proposals, summaries, transcripts, runtime events, and validator results are not described as approval records. | Record type; proposed label; source section; pass/fail |
> | Reliance-boundary check | Product-critical boundaries are not described as prompt-only or SDK-default-only. | Boundary; enforcement surface if known; unsupported claims marked `TBD` |
> | Domain-boundary check | Domain-engine notices preserve human acceptance and do not assign solver truth or professional approval to Chirality. | Domain surface; notice text; human-gate statement; pass/fail |
> | Uncertainty check | Unsupported facts remain `TBD`, `ASSUMPTION`, `PROPOSAL`, conflict, or human-ruling-needed. | Item; label used; owner/ruling field; closure status |
> | Source-status check | D-APP-38 corpus status and active Conflict Table status are visible in review evidence. | REF-006 corpus status; CT-001 status; human ruling status |
>

### CLM-019 — Records

> ##### Records
>
> Create or maintain these records as applicable:
>
> - UI copy guidelines: this `ScopeOfWork.md` CLM-025–029, materialized in `docs/BOUNDARY_REVIEW_CHECKLISTS.md`.
> - Release review checklist: this `ScopeOfWork.md` CLM-018/020, materialized in `docs/BOUNDARY_REVIEW_CHECKLISTS.md`.
> - Boundary notice examples: this `ScopeOfWork.md` CLM-029, materialized in `docs/BOUNDARY_REVIEW_CHECKLISTS.md`.
> - Review notes with checked surfaces and source sections: this `ScopeOfWork.md` CLM-021, materialized in `docs/BOUNDARY_REVIEW_CHECKLISTS.md`.
> - Human rulings for Conflict Table entries: TBD.
> - `Dependencies.csv` satisfaction closure notes: TBD.
>

### CLM-020 — Release Review Evidence Template

> ###### Release Review Evidence Template
>
> | Field | Value |
> |---|---|
> | Review ID | TBD |
> | Reviewer / accountable role | TBD |
> | Review date | TBD |
> | Release or surface set | TBD |
> | Surfaces checked | TBD |
> | Source sections used | TBD |
> | Authority-corpus treatment | REF-006 matches under the current D-APP-38 corpus snapshot; rerun reconciliation if authority docs change |
> | Conflict Table status | CT-001 TBD; historical CT-002 closed by the current D-APP-38 corpus snapshot |
> | Overall result | TBD |
>

### CLM-021 — Review Note Record Template

> ###### Review Note Record Template
>
> | Field | Value |
> |---|---|
> | Checked surface | TBD |
> | Source basis | TBD |
> | Issue type | Identity / SDK framing / human authority / binding record / reliance boundary / domain boundary / uncertainty / source status |
> | Current copy excerpt | TBD |
> | Proposed copy | TBD |
> | Finding | TBD |
> | Human ruling | TBD |
>

### CLM-022 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-103 records the post-D-APP-53 state: the dependency-reconciliation act is human-closed and the earlier INSP-03 dependency wording is historical. This does not imply every dependency is satisfied or any lifecycle transition.

- **VER-001** — Run deterministic Scope-of-Work validation, claim mapping, parity, checklist, and rendering checks, followed by human review of the candidate.

## Governing Values and Decisions — Axiology

### CLM-023 — Guidance: DEL-01-03 Product Identity and Professional Boundary Copy

> #### Guidance: DEL-01-03 Product Identity and Professional Boundary Copy
>

### CLM-024 — Purpose

> ##### Purpose
>
> This deliverable gives product and release writers a conservative boundary for Chirality copy. Its purpose is to preserve Chirality identity and human-only professional authority across UI, documentation, packaging, runtime messages, and future domain notices.
>
> The governing posture is:
>
> - Chirality is a governed desktop harness, not a vendor CLI wrapper.
> - The SDK may be privileged as implementation substrate, but Chirality owns product semantics, runtime contracts, audit posture, permission policy, professional-boundary language, and user-facing product identity.
> - Agents, tools, SDKs, validators, transcripts, and runtime events assist; accountable humans decide what can be relied upon.
>
> Sources: `docs/DIRECTIVE.md` Sections 1, 2.8, 2.11, and 3; `docs/CONTRACT.md` K-AUTH-1, K-ENGINE-3, K-SDK-4.
>

### CLM-025 — Principles

> ##### Principles
>
> | Principle | Guidance | Source |
> |---|---|---|
> | Name Chirality first | Use "Chirality" for product identity. Mention external SDK/provider details only when useful and only as implementation detail. | `docs/DIRECTIVE.md` Section 2.11 |
> | Keep assistance non-binding | Prefer "draft", "proposal", "decision support", "review", "evidence", and "human acceptance" over "approved", "certified", "issued", or "validated" unless referring to a human approval record. | `docs/DIRECTIVE.md` Section 3; `docs/CONTRACT.md` K-BIND-1 |
> | Preserve human gates | Copy should make clear that humans approve reliance-affecting transitions, release actions, issue actions, residual risk, and professional judgments. | `docs/DIRECTIVE.md` Section 3.2; `docs/CONTRACT.md` K-GATE-1 |
> | Avoid prompt-only safety claims | Do not describe prompt text, model instruction, or SDK default behavior as sufficient enforcement for product-critical boundaries. | `docs/DIRECTIVE.md` Section 2.9; `docs/CONTRACT.md` K-RELIANCE-2 |
> | Separate runtime evidence from approval | Runtime events and transcripts explain what happened; they do not approve work. | `docs/DIRECTIVE.md` Section 2.3; `docs/CONTRACT.md` K-BIND-1 |
> | Keep domain truth separate | Future domain-engine copy should distinguish Chirality interaction governance from domain-engine truth and professional review. | `docs/CONTRACT.md` K-DOMAIN-1 through K-DOMAIN-4 |
>

### CLM-026 — Considerations

> ##### Considerations
>
> - Copy can disclose SDK usage when it improves transparency, diagnostics, implementation context, or release evidence. It risks product-identity drift when the SDK brand becomes the subject of the product claim, appears to own governance semantics, or makes Chirality look like Claude Code, an Anthropic product, a vendor CLI, or a feature-parity target.
> - Professional-boundary copy should be visible where a user could confuse output generation, validation, event logging, or domain-engine results with approval.
> - Release review should include UI labels, empty states, permission prompts, status-transition messages, runtime/session summaries, documentation, packaging metadata, and domain-engine future notices. The checked-surface inventory for a given release remains TBD until the release owner identifies the affected surfaces.
> - ASSUMPTION: "Boundary notice examples" will be used as reusable copy snippets, not as a substitute for implementation enforcement. This is inferred from the deliverable scope and the reliance-boundary requirements.
>

### CLM-027 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Preferred posture |
> |---|---|
> | Transparent SDK disclosure vs. product identity drift | Disclose SDK use where appropriate, but keep Chirality as the product and contract owner. |
> | Concise UI copy vs. professional-boundary clarity | Use concise language, but do not remove human-review and non-binding qualifiers where reliance confusion is plausible. For very short UI strings, pair concise labels with nearby help text, tooltip text, empty-state copy, or release notes when the label alone cannot carry the boundary without becoming misleading. |
> | Friendly automation language vs. authority confusion | Prefer "helps draft", "organizes", "records", "checks", and "proposes" over "approves", "certifies", "issues", or "validates for reliance". |
> | Future domain-engine capability vs. current scope | Present domain engines as future-boundary scope until governed amendment and implementation evidence exist. |
>

### CLM-028 — Term Normalization

> ##### Term Normalization
>
> | Term | Copy treatment | Source basis |
> |---|---|---|
> | Draft | Non-binding working output that requires accountable human acceptance before reliance. | `docs/DIRECTIVE.md` Section 3.1; `docs/CONTRACT.md` K-BIND-1 |
> | Proposal | A suggested change, operation, or copy treatment requiring review or acceptance. | `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-GATE-1 |
> | Decision support | Assistance that informs judgment but does not replace accountable human decision rights. | `docs/DIRECTIVE.md` Section 3.4 |
> | Summary | Non-authoritative condensation unless imported into governed project files and accepted. | `docs/DIRECTIVE.md` Sections 2.5 and 2.6 |
> | Transcript | Runtime or SDK record used for diagnosis/review, not an approval record. | `docs/DIRECTIVE.md` Section 2.3; `docs/CONTRACT.md` K-SDK-3 |
> | Runtime event | Audit evidence of what happened during a turn; not approval, issuance, code compliance, external validation, or reliance clearance. | `docs/DIRECTIVE.md` Section 2.3 |
> | Validator result | Deterministic check evidence; not professional approval or external validation. | `docs/DIRECTIVE.md` Sections 2.4 and 3.2; `docs/CONTRACT.md` K-AUTH-1 |
> | Approval record | Human-authored binding evidence tied to specific content, normally a git SHA. | `docs/DIRECTIVE.md` Section 2.4; `docs/CONTRACT.md` K-AUTH-2 |
>
> Validators and runtime events cannot be treated as external validation or approval records because the sources separate evidence from human authority. They can show what was checked or what happened, but gate-relevant decisions still require versioned project files and accountable human acceptance.
>

### CLM-029 — Examples

> ##### Examples
>
> Acceptable examples, grounded in source posture:
>
> | Context | Example copy | Source basis |
> |---|---|---|
> | Product description | "Chirality is a governed desktop harness for AI-assisted project work over local files." | `docs/DIRECTIVE.md` Section 1 |
> | Draft output notice | "This output is draft assistance. An accountable human must review and accept it before reliance." | `docs/DIRECTIVE.md` Section 3.1 |
> | SDK disclosure | "This runtime may use an SDK-backed engine behind Chirality-owned contracts and audit records." | `docs/DIRECTIVE.md` Sections 2.8 and 2.10 |
> | Runtime event notice | "Runtime events record what happened during the turn; they are not approval records." | `docs/DIRECTIVE.md` Section 2.3 |
> | Domain notice | "Domain-engine results require human review and do not represent Chirality-owned solver truth or professional approval." | `docs/CONTRACT.md` K-DOMAIN-4; `docs/PRD.md` FR-115 |
> | Validator result notice | "This validator result is check evidence, not external validation or professional approval." | `docs/DIRECTIVE.md` Sections 2.4 and 3.2; `docs/CONTRACT.md` K-AUTH-1 |
>
> Avoid examples:
>
> | Context | Avoid | Reason |
> |---|---|---|
> | Product identity | "Chirality is Claude Code for professional workflows." | Violates product identity boundary. |
> | Approval | "The agent approved this deliverable." | Violates human-only approval boundary. |
> | Validation | "Chirality certifies this result as code-compliant." | Violates professional-boundary and domain-truth boundaries. |
> | Reliance boundary | "The prompt prevents unsafe writes." | Prompt text alone is not a sufficient safety boundary. |
>

### CLM-030 — Conflict Table (for human ruling)

> ##### Conflict Table (for human ruling)
>
> | Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
> |---|---|---|---|---|---|---|
> | CT-001 | Dispatch path used `PKG-01_Governance_and_Product_Boundaries`, but the matching folder on disk is `PKG-01_Product_Governance_and_Reliance_Boundaries`. | User dispatch path | `_CONTEXT.md` PackageName and actual folder path | Run record; final report | Treat actual matching DEL-01-03 folder as resolved scope; preserve stable PackageID/DeliverableID. | **RULED 2026-07-12 (D-APP-56 R4-P35): proposed authority ratified.** |
>
> Closed historical conflict: `CT-002` is superseded by the current D-APP-38 corpus snapshot; current `_REFERENCES.md`
> records REF-006 `docs/PRD.md` as `MATCH`.
>

### CLM-031 — Normalized Checklist Artifact

> ##### Normalized Checklist Artifact
>
> ADQ-03 materialized `docs/BOUNDARY_REVIEW_CHECKLISTS.md` as the shared professional-boundary and
> scope-boundary checklist package. For DEL-01-03, that file supplies the UI copy review checklist,
> release review evidence template, boundary notice examples, and finding template. It is CHECKING-stage
> review evidence only; it does not assign `ResponsibleParty`, satisfy dependencies, issue this
> deliverable, or approve release/professional reliance.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-071 SOW-074 OBJ-009 OBJ-010 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |
