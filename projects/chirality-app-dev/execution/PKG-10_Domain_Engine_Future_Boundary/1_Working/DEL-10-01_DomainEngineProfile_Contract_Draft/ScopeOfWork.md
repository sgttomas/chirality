---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-10-01
package_id: PKG-10
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-066, SOW-067]
package_objective_refs: [OBJ-010]
---

# Scope of Work — DEL-10-01

## Purpose and Objective Traceability

This Scope of Work defines `DEL-10-01` in service of project scope [SOW-066, SOW-067] and package objectives [OBJ-010].

- **OUT-001** — The DEL-10-01 future-boundary generic DomainEngineProfile contract draft, comprising a profile schema draft, validation notes, and a future amendment checklist, while preserving future compatibility without immediate runtime implementation.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-10-01 DomainEngineProfile Contract Draft

> #### Datasheet: DEL-10-01 DomainEngineProfile Contract Draft
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-10-01 |
> | DeliverableName | DomainEngineProfile Contract Draft |
> | PackageID | PKG-10 |
> | PackageName | Domain Engine Future Boundary |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | Type | API_CONTRACT |
> | ResponsibleParty | TBD |
> | ContextEnvelope | M |
> | Current posture | Future-boundary contract, not current implementation |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Contract subject | Future `DomainEngineProfile` profile contract conforming to framework-root canon at `77a327727`. | `_CONTEXT.md`; `_REFERENCES.md` REF-008; `docs/TYPES.md` §11.1 |
> | Canonical identity fields | `schema_version`, `id`, `name`, `engine_type`, `profile_version`. | historical persona basis; current method REF-008/REF-011/REF-012; `docs/TYPES.md` §11.1 |
> | Profile lifecycle fields | `profile_status` using `NONE | DRAFT | VALIDATED | ADOPTED | STALE | INVALID | UNKNOWN`; `integration_level` using `MANUAL_BRIDGE | READ_ONLY | DOMAIN_CONTROLLED_WRITE | OPERATION_PROPOSAL | EXTERNAL_RESULT_STATE`. | historical persona basis; current method REF-008/REF-011/REF-012; `docs/TYPES.md` §11.1 |
> | Path and artifact role fields | `domain_root_patterns`, `authoritative_artifacts`, `chirality_readable_artifacts`, `protected_write_paths`, `agent_writable_paths`. | historical persona basis; current method REF-008/REF-011/REF-012; `docs/CONTRACT.md` §1.10 |
> | Tool contract fields | `deterministic_tools[].id`, `mode`, `requires_human_confirmation`, `validate_result_schema`, and `apply_result_schema`. | historical persona basis; current method REF-008/REF-011/REF-012; `docs/TYPES.md` §11.1 |
> | Proposal contract field | `operation_proposal_contract` with lifecycle, risk classes, deterministic-check result schema, and accepted/applied requirements. | historical persona basis; current method REF-008/REF-011/REF-012; `docs/TYPES.md` §11.1 |
> | Professional boundary field | Structured `professional_boundary.agent_must_not_claim` list. | historical persona basis; current method REF-008/REF-011/REF-012; `docs/CONTRACT.md` §1.10 K-DOMAIN-4 |
> | True future TBDs | ADOPTED profile instances and their applicable schema hooks are supplied (see CLM-028). New adapters, tool/operation stores, endpoints, apply tooling and per-instance notice review remain gated delivery work. | `docs/PLAN.md` §R7; `docs/SPEC.md` §18 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Release scope | D-APP-49 through D-APP-52 authorize the staged profile/type, registry, read and PEC-scoped propose/refresh/validate interfaces. Their retained implementation is compatibility evidence, not proof of live Codex exposure. D-GOV-43 / D-APP-127 select Codex; live-path composition and named verification remain delivery work. Endpoints, operation apply, direct protected writes/hooks, integration-level advancement and general domain runtime retain F-APP-3 and their separate gates. | `docs/SPEC.md` §18; D-APP-49 through D-APP-52 |
> | Sequencing | The ruled staged authority survives; retained-path behavior does not establish Codex live-path availability. Broader profile/operation capabilities retain their own governed amendment. | `docs/PLAN.md` §R7; `docs/PRD.md` §8.17 |
> | Engine-specific integration | A generic `DomainEngineProfile` contract precedes any engine-specific integration. | `docs/PRD.md` §8.17 FR-107 |
> | Protected path posture | Protected domain paths are write-quarantined; agents write proposals, summaries, and review aids only under profile-approved `agent_writable_paths`. | `docs/CONTRACT.md` §1.10 K-DOMAIN-2; REF-008 |
> | Human gate posture | Accepted/applied proposal transitions require human approval bound to git SHA per K-AUTH-2 and domain-engine-controlled apply or external terminal acceptance records. | `docs/CONTRACT.md` §1.10 K-DOMAIN-3; REF-008 |
> | Professional boundary | Domain-engine outputs must not be represented as professional approval, code compliance, certification, sealing, authentication, external validation, or solver truth owned by Chirality. | `docs/CONTRACT.md` §1.10 K-DOMAIN-4; REF-008 |
>

### CLM-005 — Construction

> ##### Construction
>

### CLM-006 — Canonical Profile Shape

> ###### Canonical Profile Shape
>
> ```yaml
> domain_profile:
>   schema_version: "1.0"
>   id: "<domain_engine_id>"
>   name: "<Domain Engine Name>"
>   engine_type: "<domain classification>"
>   profile_version: "0.1"
>   profile_status: "DRAFT"
>   integration_level: "MANUAL_BRIDGE"
>   domain_root_patterns:
>     - "<path or glob>"
>   authoritative_artifacts:
>     - "<engine-owned path or glob>"
>   chirality_readable_artifacts:
>     - "<manifest/summary/report path or glob>"
>   protected_write_paths:
>     - "<agent-prohibited path or glob>"
>   agent_writable_paths:
>     - "<proposal/review/checklist path or glob>"
>   deterministic_tools:
>     - id: "<tool.id>"
>       mode: "read_only"
>       requires_human_confirmation: false
>       validate_result_schema: "<schema ref or TBD>"
>       apply_result_schema: "<schema ref or TBD>"
>   operation_proposal_contract:
>     lifecycle: ["draft", "ready_for_review", "accepted", "rejected", "applied"]
>     risk_classes: ["engine_checkable", "engine_silent"]
>     deterministic_check_result_schema: "<schema ref or TBD>"
>     accepted_or_applied_requires:
>       - "human approval bound to git SHA per K-AUTH-2"
>       - "domain-engine-controlled apply or external terminal acceptance record"
>   professional_boundary:
>     agent_must_not_claim:
>       - "code compliant for reliance"
>       - "professionally approved"
>       - "externally validated"
> ```
>
> Source: historical `agents/AGENT_DOMAIN_ENGINE.md@77a327727` (retained source basis); current method references are `_REFERENCES.md` REF-008/REF-011/REF-012 and reflected in `docs/TYPES.md` §11.1.
>

### CLM-007 — Validation Notes

> ###### Validation Notes
>
> | Check | Draft rule | Source |
> |---|---|---|
> | Required fields present | A future validator should reject profiles missing identity, status, integration-level, path-role, deterministic-tool, operation-proposal-contract, or professional-boundary fields. | REF-008; `docs/PRD.md` §8.17 FR-108, FR-109 |
> | Deterministic validation | Profile validation must be deterministic before runtime exposure. | `docs/PRD.md` §8.17 FR-109; D-T0-06 |
> | Result schema refs | Missing `validate_result_schema`, `apply_result_schema`, or deterministic-check result schemas remain explicit `TBD`; chat must not infer them. | REF-008 |
> | Future-only exposure | Candidate domain endpoints/tools must remain provisional until governed future amendment. | `docs/SPEC.md` §18 |
> | Solver separation | Profile contract must preserve that domain engines own authoritative domain truth. | `docs/CONTRACT.md` §1.10 K-DOMAIN-1 |
>

### CLM-008 — References

> ##### References
>
> - `_CONTEXT.md`
> - `_REFERENCES.md`
> - `_DEPENDENCIES.md`
> - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` §PKG-10, SOW-066, SOW-067, DEC-006
> - historical `agents/AGENT_DOMAIN_ENGINE.md@77a327727` (retained source basis); current method references are `_REFERENCES.md` REF-008/REF-011/REF-012
> - `docs/CONTRACT.md` §1.10
> - `docs/SPEC.md` §18
> - `docs/TYPES.md` §11
> - `docs/PLAN.md` §R7
> - `docs/PRD.md` §8.17, §10.10, §R7, KG-016 through KG-020
>

### CLM-009 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-148 distinguishes supplied ruled-amendment fields (profile instances and hook-field schema references) from genuine remaining TBDs (adapters, stores, endpoints, apply tooling, and per-instance notice review).

## Completion and Reliance Basis — Epistemology

### CLM-010 — Specification: DEL-10-01 DomainEngineProfile Contract Draft

> #### Specification: DEL-10-01 DomainEngineProfile Contract Draft
>

### CLM-011 — Scope

> ##### Scope
>
> This deliverable specifies a future-boundary draft for `DomainEngineProfile`: profile identity,
> integration level, domain artifact roles, protected and agent-writable paths, deterministic tools,
> operation-proposal contract hooks, and professional-boundary notices.
>
> In scope:
>
> - Future `DomainEngineProfile` documentation contract conforming to framework-root
>   `agents/AGENT_DOMAIN_ENGINE.md` at commit `77a327727`.
> - App-dev vocabulary alignment in `docs/TYPES.md` §11.
> - Validation notes for deterministic profile acceptance.
> - Future amendment checklist for accepting concrete profile instances after core harness stability.
>
> Out of scope:
>
> - `/api/domain/*` endpoints, operation apply, direct protected-path writes/hooks, and general domain-runtime activation. D-APP-49 through D-APP-52 separately authorize source types/guards, a closed registry, ruled read tools, and pec-scoped loopback propose/refresh/validate tools.
> - Engine-specific integration, including OpenPipeStress-specific runtime assumptions.
> - Direct writes to protected domain-engine model paths.
> - Professional approval, code compliance, certification, sealing, authentication, external validation, or
>   solver-truth claims.
>
> Sources: `_CONTEXT.md`; `_REFERENCES.md` REF-008; `agents/AGENT_DOMAIN_ENGINE.md` pinned at
> `77a327727`; `docs/CONTRACT.md` §1.10; `docs/TYPES.md` §11; `docs/SPEC.md` §18; `docs/PRD.md` §8.17.
>

### CLM-012 — Requirements

> ##### Requirements
>
> | ID | Requirement | Verification |
> |---|---|---|
> | DEL-10-01-REQ-001 | The contract draft MUST preserve `ResponsibleParty: TBD` until human assignment. | Inspect document identification sections. |
> | DEL-10-01-REQ-002 | The contract draft MUST distinguish the D-APP-49 through D-APP-52 authorized staged surface, its retained compatibility implementation and unverified Codex composition from the still-gated endpoints, apply, protected-path hooks/writes, and general domain runtime. | Inspect Scope, Conditions, and Procedure gate checks. |
> | DEL-10-01-REQ-003 | A generic `DomainEngineProfile` contract MUST precede any engine-specific integration. | Confirm no OpenPipeStress-specific runtime assumptions are embedded in the generic profile contract. |
> | DEL-10-01-REQ-004 | A future `DomainEngineProfile` MUST include canonical identity, status, integration-level, path-role, deterministic-tool, operation-proposal-contract, and professional-boundary fields from the retained framework persona basis `77a327727`, read with current domain-engine workflow resources. | Validate field list against `docs/TYPES.md` §11.1 and `_REFERENCES.md` REF-008. |
> | DEL-10-01-REQ-005 | `profile_status` MUST use `NONE | DRAFT | VALIDATED | ADOPTED | STALE | INVALID | UNKNOWN`; integrated workflows require `ADOPTED`, while `MANUAL_BRIDGE` may explicitly record no adopted profile. | Inspect `docs/TYPES.md` §11.1 and future profile records. |
> | DEL-10-01-REQ-006 | `integration_level` MUST use `MANUAL_BRIDGE | READ_ONLY | DOMAIN_CONTROLLED_WRITE | OPERATION_PROPOSAL | EXTERNAL_RESULT_STATE` and MUST NOT skip levels. | Inspect profile documentation and future amendment packets. |
> | DEL-10-01-REQ-007 | Protected domain paths MUST be write-quarantined, and agent writes MUST be limited to profile-approved `agent_writable_paths`. | Future path policy separates authoritative/readable/protected/agent-writable path roles. |
> | DEL-10-01-REQ-008 | Declared deterministic tools MUST include `id`, `mode`, `requires_human_confirmation`, `validate_result_schema`, and `apply_result_schema`; missing schema refs remain explicit `TBD`, not inferred. | Inspect deterministic-tool records and validation notes. |
> | DEL-10-01-REQ-009 | The profile MUST carry an `operation_proposal_contract` covering lifecycle, risk classes, deterministic-check result schema, and accepted/applied requirements. | Inspect profile contract section and DEL-10-03 alignment. |
> | DEL-10-01-REQ-010 | Applying a domain operation MUST require explicit human acceptance bound to K-AUTH-2 evidence and domain-engine-controlled apply or external terminal acceptance records. | Future operation workflow links application to the human gate and accepted/applied requirements. |
> | DEL-10-01-REQ-011 | Boundary notices MUST state that Chirality does not approve, certify, seal, code-validate, externally validate, or own solver truth. | Review `professional_boundary` copy in future profile instances. |
>

### CLM-013 — Standards

> ##### Standards
>
> | Source | Applicable authority | Notes |
> |---|---|---|
> | historical `agents/AGENT_DOMAIN_ENGINE.md@77a327727`; current method REF-008/REF-011/REF-012 | Historical persona field basis and current domain-engine method/profile governance | Historical pin retained; REF-008/011/012 are current workflow identities. |
> | `docs/CONTRACT.md` §1.10 | App-dev K-DOMAIN invariants specializing framework K-DOMAIN without weakening them | Governs truth ownership, path quarantine, operation proposals, and professional boundary. |
> | `docs/SPEC.md` §18 | Future specification boundary and candidate endpoint families | Candidate endpoints are provisional and must not be implemented as current-release scope. |
> | `docs/TYPES.md` §11 | App-dev vocabulary target conforming to framework canon | Defines required vocabulary; D-APP-49 separately supplies the inert source type. No live tool exposure follows from the vocabulary alone. |
> | `docs/PRD.md` §8.17 | Product requirements FR-106 through FR-115 | Current reference drift is reported separately under D-APP-38; no basis re-pin is implied. |
> | `docs/PLAN.md` §R7 | Future amendment sequencing | Domain profiles come after core harness stability and human-gated R7 activation. |
>

### CLM-014 — Verification

> Verification shall review this ScopeOfWork, including CLM-003/006/012 profile fields and CLM-004 staged boundary. Compare canonical vocabulary with current domain-engine workflow resources and the retained persona basis; do not conflate those origins. Inspect ADOPTED profile hooks against their declared schemas. Check `frontend/src/__tests__/lib/domain-profile.test.ts` and `domain-profile-registry.test.ts` as retained conformance evidence; a new Codex registration/exposure witness is outstanding. Verify no endpoint/apply activation, no direct protected write, and no integration-level advance. Current lifecycle and approval SHA remain unchanged.

### CLM-015 — Documentation

> Required documentation is carried by this ScopeOfWork: CLM-003/006 profile shape, CLM-007 validation obligations, CLM-020 amendment procedure, and CLM-028 illustrative skeleton/instance evidence. The former Datasheet, Specification, Guidance and Procedure are conversion-source identities, not missing current files. Dependency registers remain separate governed sources.

### CLM-016 — D-APP-56 ownership amendment (2026-07-12)

> Under D-APP-56 R4-P27, DEL-10-01 owns the generic profile contract, registration interface and gate; DEL-10-04 owns fixture content and validation evidence. The canonical type carrier is `projects/chirality-runtime/packages/contracts/src/harness/domain-profile.ts` through `@chirality/runtime-contracts`; App retained registration evidence is `frontend/src/lib/harness/mcp/domain-profile-registry.ts`. D-APP-118 retires `@chirality/harness-contract` and its rollback-support obligation; no facade approval is pending. Verification: direct canonical imports and `domain-profile.test.ts` / `domain-profile-registry.test.ts`; retained registry checks do not prove live Codex registration. Carrier location does not transfer fixture authoring into this App loop.

- **AC-001** — The Scope of Work identifies DEL-10-01 as a future-boundary generic DomainEngineProfile contract, covers SOW-066 and SOW-067 for OBJ-010, and preserves all domain requirements and source traceability. Exact four-document parity is the completed historical conversion criterion; subsequent authorized claim repairs are checked against their decisions and current evidence.

## Production and Verification Method — Praxeology

### CLM-017 — Procedure: DEL-10-01 DomainEngineProfile Contract Draft

> #### Procedure: DEL-10-01 DomainEngineProfile Contract Draft
>

### CLM-018 — Purpose

> ##### Purpose
>
> Define the bounded procedure for maintaining the future `DomainEngineProfile` contract draft while preserving the F3 domain-engine implementation fence.
>

### CLM-019 — Prerequisites

> ##### Prerequisites
>
> | Prerequisite | Status |
> |---|---|
> | Deliverable-local context is present. | Satisfied: `_CONTEXT.md` exists. |
> | Authoritative references are accessible. | Satisfied: `_REFERENCES.md` includes REF-008 for framework `AGENT_DOMAIN_ENGINE.md` pinned at `77a327727`. |
> | Framework source identity is known. | Satisfied: D-T0-01 makes the historical framework-root persona canonical on its recorded basis; app-dev `docs/TYPES.md` Section 11 conforms to it. |
> | Current status posture is preserved. | Required: read current state from `_STATUS.md`; this tranche performs no lifecycle transition or release-readiness act. |
> | Current scope remains future-boundary. | Required by `docs/SPEC.md` Section 18, `docs/PLAN.md` R7, and D-APP-39 F3. |
>

### CLM-020 — Steps

> ##### Steps
>
> 1. Confirm identity from `_CONTEXT.md`.
>    - DeliverableID: DEL-10-01.
>    - ResponsibleParty: TBD.
>    - Type: API_CONTRACT.
>    - Scope: future profile contract for engine identity, integration level, path/artifact roles, deterministic tools, operation-proposal contract, and professional boundary.
>
> 2. Confirm source posture from `_REFERENCES.md`.
>    - Use REF-008/REF-011/REF-012 for the current domain-engine workflow; the persona at 77a327727 is the preserved historical field-shape basis.
>    - Use app-dev `docs/TYPES.md` Section 11 only as the local vocabulary target conforming to REF-008.
>    - Do not create `Dependencies.csv`.
>
> 3. Read source slices for the domain-engine future boundary.
>    - historical `agents/AGENT_DOMAIN_ENGINE.md@77a327727`; current method REF-008/REF-011/REF-012 for Minimal Profile Shape, valid operation proposal table, lifecycle, and `operation_proposal_contract`.
>    - `docs/CONTRACT.md` Section 1.10 for app-dev K-DOMAIN invariants, which specialize framework `docs/CONTRACT.md` Section 1.12 without weakening it.
>    - `docs/SPEC.md` Section 18 for provisional future endpoint/tool boundary.
>    - `docs/TYPES.md` Section 11 for app-dev vocabulary.
>    - `docs/PLAN.md` R7 for future-amendment sequencing.
>    - `docs/PRD.md` Section 8.17 for FR-106 through FR-115.
>    - Decomposition PKG-10 / DEL-10-01 entry for local scope.
>
> 4. Draft or maintain the profile contract.
>    - Preserve canonical identity fields: `schema_version`, `id`, `name`, `engine_type`, and `profile_version`.
>    - Preserve canonical `ProfileStatus`: `NONE | DRAFT | VALIDATED | ADOPTED | STALE | INVALID | UNKNOWN`.
>    - Preserve canonical `IntegrationLevel`: `MANUAL_BRIDGE | READ_ONLY | DOMAIN_CONTROLLED_WRITE | OPERATION_PROPOSAL | EXTERNAL_RESULT_STATE`.
>    - Preserve path/artifact role fields: `domain_root_patterns`, `authoritative_artifacts`, `chirality_readable_artifacts`, `protected_write_paths`, and `agent_writable_paths`.
>    - Preserve deterministic tool fields, including `validate_result_schema` and `apply_result_schema`.
>    - Preserve `operation_proposal_contract`, including lifecycle, risk classes, deterministic-check result schema, and accepted/applied requirements.
>    - Preserve structured `professional_boundary`.
>
> 5. Mark only true future implementation details as `TBD`.
>    - New profile instances beyond the ADOPTED OpenPipeStress and PEC records.
>    - Schema refs not already bound by the ADOPTED profile; retain explicit inapplicable/TBD hooks individually.
>    - Unbuilt live Codex composition, new adapters/stores, endpoint handlers, protected-path enforcement and apply tooling; retained ruled tools are compatibility evidence.
>    - Concrete boundary notice copy for each accepted profile instance.
>
> 6. Preserve future-boundary constraints.
>    - Do not implement candidate endpoints.
>    - Do not define executable tool behavior.
>    - Do not authorize direct protected-path writes.
>    - Do not represent domain output as professional approval, code compliance, certification, sealing, authentication, external validation, or Chirality-owned solver truth.
>
> 7. Cross-check documents.
>    - Confirm the profile definition, requirements, procedure and guidance sections of this ScopeOfWork use consistent canonical terms.
>    - Confirm DEL-10-03 uses the same lifecycle and proposal contract fields.
>    - Confirm old compact-draft blockers are not reintroduced as unresolved human-ruling blockers.
>
> 8. Record the run without lifecycle transition.
>    - Keep `_STATUS.md` unchanged.
>    - Record conformance notes in `MEMORY.md` and coordination closeout.
>    - Let D-APP-38 reconciliation update authority-corpus hashes after authority-doc edits.
>

### CLM-021 — Verification

> Check CLM-006/012 profile field conformance and CLM-004/016 ownership and staged boundary against `domain-profile.test.ts` / `domain-profile-registry.test.ts`. Read ADOPTED profiles and their declared hooks; do not call supplied profiles or bound hooks TBD. Current Codex registration/exposure checks remain outstanding. No endpoint/apply/protected-write activation is claimed. Keep the dependency register, lifecycle and approval SHA unchanged; verify current ScopeOfWork sections rather than demanding four retired files.

### CLM-022 — Records

> Current records: `ScopeOfWork.md`, `MEMORY.md`, `_STATUS.md`, `_REFERENCES.md`, and the existing dependency register. D-APP-45 and the four-document conversion records remain historical evidence. Current changed-block evidence is W10_CHANGES.csv; no new product qualification or human review is asserted.

- **VER-001** — Review the current ScopeOfWork claims and output matrix against their cited requirements and retained gates. Historical conversion/parity evidence is recovered in `R5/CONVERSION_EVIDENCE_REVIEW.csv` of RUN_D128_CONCORDANCE_2026-09-21_1614Z; it proves the dated conversion only. Current reconciliation uses W10_CHANGES.csv and independent changed-block review; product and human-acceptance checks remain separately required.

## Governing Values and Decisions — Axiology

### CLM-023 — Guidance: DEL-10-01 DomainEngineProfile Contract Draft

> #### Guidance: DEL-10-01 DomainEngineProfile Contract Draft
>

### CLM-024 — Purpose

> ##### Purpose
>
> This guidance explains how to read and maintain the `DomainEngineProfile` contract draft as a future-boundary artifact. The draft preserves compatibility with future domain-engine integrations without activating domain execution in the current app-dev slice.
>
> Historical field-shape basis: `agents/AGENT_DOMAIN_ENGINE.md@77a327727`. Current domain-engine method sources are `_REFERENCES.md` REF-008/REF-011/REF-012; they are not the historical persona bytes. Under D-T0-01, the framework-root persona is canonical; app-dev `docs/TYPES.md` Section 11 conforms to it and must not weaken framework invariants.
>

### CLM-025 — Principles

> ##### Principles
>
> | Principle | Guidance | Source |
> |---|---|---|
> | Canon first | Maintain the profile shape from REF-008: identity fields, `ProfileStatus`, `IntegrationLevel`, path/artifact roles, deterministic tools, `operation_proposal_contract`, and professional boundary. | REF-008; `docs/TYPES.md` Section 11.1 |
> | Generic first | Keep the profile contract generic before any engine-specific integration. OpenPipeStress may be a future concrete profile, but it must not shape Chirality core runtime assumptions. | `docs/PRD.md` Section 8.17 FR-107 |
> | Future gated | Treat endpoints, tools, validators, adapters, operation stores, and path hooks as future platform interfaces until a governed amendment accepts them. | `docs/SPEC.md` Section 18; `docs/PLAN.md` R7 |
> | Truth separation | Domain engines own authoritative domain truth; Chirality governs interaction, profile records, proposals, review aids, and human gates. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-1 |
> | Path quarantine | Protected paths and agent-writable paths must remain distinct. Agents may draft proposals and summaries only under approved writable proposal/review paths. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-2; REF-008 |
> | Human acceptance | Accepted/applied proposal states require explicit human approval bound to K-AUTH-2 evidence and a domain-engine-controlled apply or external terminal acceptance record. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3; REF-008 |
> | Professional boundary | Boundary notices must prevent solver outputs from being presented as professional approval, code compliance, certification, sealing, authentication, external validation, or solver truth owned by Chirality. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4; REF-008 |
>

### CLM-026 — Considerations

> ##### Considerations
>
> - Use `docs/TYPES.md` Section 11.1 as the app-dev vocabulary target, but resolve conflicts against REF-008.
> - The older compact draft fields `DomainEngineOperationDescriptor` and `manifestRules` are superseded by canonical `deterministic_tools`, path/artifact role sets, and `operation_proposal_contract`; they are no longer human-ruling blockers for DEL-10-01.
> - Keep `validate_result_schema`, `apply_result_schema`, and deterministic-check result schema references explicit. A concrete schema may remain `TBD`, but the schema hook itself is canonical.
> - Keep OpenPipeStress references fixture-level only. OpenPipeStress and PEC profiles are ADOPTED under tier-0 authority; their existence does not authorize App live integration or core solver assumptions.
> - Any future validator should be deterministic and reject invalid or incomplete profiles before runtime exposure.
> - Preserve `_STATUS.md` as-is. This conformance tranche does not authorize `CHECKING -> ISSUED`, release readiness, or R7 implementation.
>

### CLM-027 — True Future TBDs

> ##### True Future TBDs
>
> | Topic | Conservative position | Risk if loosened |
> |---|---|---|
> | Concrete profile instances | Read existing ADOPTED OpenPipeStress and PEC profiles; additional instances require their owning amendment. | An illustrative profile could be mistaken for accepted integration. |
> | Concrete schema refs | Record `validate_result_schema`, `apply_result_schema`, and deterministic-check result schema as explicit refs or `TBD`. | Prompt-inferred result schemas could become false contract surface. |
> | Adapter/tool implementation | Retain ruled staged-tool authority and compatibility evidence; unbuilt Codex composition, new adapters/stores, endpoints, path enforcement and apply remain gated. | Crosses F3 and activates domain runtime without tier-0 gate. |
> | Boundary notice copy | Require structured boundary fields now; review concrete text per profile instance later. | Generic copy may imply professional reliance in a domain-specific context. |
>

### CLM-028 — Example Generic Skeleton

> ##### Example Generic Skeleton
>
> ```yaml
> domain_profile:
>   schema_version: "1.0"
>   id: "TBD"
>   name: "TBD"
>   engine_type: "TBD"
>   profile_version: "0.1"
>   profile_status: "DRAFT"
>   integration_level: "MANUAL_BRIDGE"
>   domain_root_patterns: []
>   authoritative_artifacts: []
>   chirality_readable_artifacts: []
>   protected_write_paths: []
>   agent_writable_paths: []
>   deterministic_tools:
>     - id: "TBD"
>       mode: "read_only"
>       requires_human_confirmation: false
>       validate_result_schema: "TBD"
>       apply_result_schema: "TBD"
>   operation_proposal_contract:
>     lifecycle: ["draft", "ready_for_review", "accepted", "rejected", "applied"]
>     deterministic_check_result_schema: "TBD"
>   professional_boundary:
>     agent_must_not_claim:
>       - "code compliant for reliance"
>       - "professionally approved"
>       - "externally validated"
> ```
>
> This example is illustrative only. It is not an accepted runtime fixture and must not be treated as implementation-ready.
>
> Cross-reference (2026-07-02, agent decision under `TRB-chirality-app-dev-DEL-10-01-2026-07-02`): a concrete ADOPTED instance of this contract now exists — `_DomainEngines/profiles/open_pipe_stress.yaml` (tier-0, ADOPTED per D-T0-06) — and the concrete result-schema refs the example marks `TBD` are published for that instance: `projects/chirality-piping/schemas/operation_outcome.schema.json` (`validate_result_schema` / `apply_result_schema`; operation_applier `OperationOutcome`) and `projects/chirality-piping/schemas/rule_check_run_result.schema.json` (`deterministic_check_result_schema`; rule_check_runner `RuleCheckRunResult`). The Rust sources govern on disagreement; applicable validation/apply/check hooks are now bound in the ADOPTED profile. Inapplicable or unsupplied hooks remain explicit TBD. The example skeleton above stays as-is: its `TBD` placeholders are template positions, and other engines supply their own refs. Note the repo qualifier: piping DEL-10-03 (Local FEA handoff) published those schemas; app-dev DEL-10-03 is a different deliverable.
>

### CLM-029 — References

> ##### References
>
> - `_REFERENCES.md` REF-008
> - historical `agents/AGENT_DOMAIN_ENGINE.md@77a327727` (retained source basis); current method references are `_REFERENCES.md` REF-008/REF-011/REF-012
> - `docs/CONTRACT.md` Section 1.10
> - `docs/SPEC.md` Section 18
> - `docs/TYPES.md` Section 11
> - `docs/PLAN.md` R7
> - `docs/PRD.md` Section 8.17, Section 10.10, KG-016 through KG-020
>

### CLM-030 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> UPD-148 distinguishes supplied ruled-amendment fields (profile instances and hook-field schema references) from genuine remaining TBDs (adapters, stores, endpoints, apply tooling, and per-instance notice review).

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-066 SOW-067 OBJ-010 | CLM-010 | AC-001 | VER-001 | Historical conversion mapping; current claim-block review and applicable named verification evidence |
