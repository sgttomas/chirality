---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-10-04
package_id: PKG-10
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@7b0be4d8772a16e5a4774a17988479587d00acca
project_scope_refs: [SOW-070]
package_objective_refs: [OBJ-010]
---

# Scope of Work — DEL-10-04

## Purpose and Objective Traceability

This Scope of Work defines `DEL-10-04` in service of project scope [SOW-070] and package objectives [OBJ-010].

- **OUT-001** — The DEL-10-04 source-preserving production contract for the future OpenPipeStress fixture profile, validation tests, and adapter assumptions note, without hardcoding solver assumptions into Chirality core.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture

> #### Datasheet: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture
>
> REF-006 records an accepted reference basis, not perpetual current-byte equality. Read current observed hashes/status in `_REFERENCES.md`; retain expected hashes and use the parent D-APP-38 reconciliation for current drift. The 2026-07-12 MATCH observation is historical.
>

### CLM-002 — Identification

> ##### Identification
>
> | Field | Value |
> |---|---|
> | DeliverableID | DEL-10-04 |
> | DeliverableName | Domain Profile Validation and OpenPipeStress Fixture |
> | PackageID | PKG-10 |
> | PackageName | Domain Engine Future Boundary |
> | DecompositionVariant | SOFTWARE_DECOMP |
> | DecompositionRevision | v3.2 |
> | ResponsibleParty | Ryan Tufts (owner confirmation 2026-07-17; D-APP-59) |
> | Type | TEST_SUITE |
> | ContextEnvelope | M |
> | ScopeItem | SOW-070 |
> | Objective | OBJ-010 |
> | Source posture | Future-boundary/gated scope; not current-release domain operation execution |
> | Validation evidence owner | Ryan Tufts — human owner interpreting future fixture pass/fail evidence (owner confirmation 2026-07-17; D-APP-59) |
>

### CLM-003 — Attributes

> ##### Attributes
>
> | Attribute | Value | Source |
> |---|---|---|
> | Primary subject | Validation of generic domain profiles and OpenPipeStress as a future fixture profile | `_CONTEXT.md` Deliverable Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-10 table |
> | Domain profile contract fields | `schema_version`, `id`, `name`, `engine_type`, `profile_version`, `profile_status`, `integration_level`, `domain_root_patterns`, `authoritative_artifacts`, `chirality_readable_artifacts`, `protected_write_paths`, `agent_writable_paths`, `deterministic_tools`, `operation_proposal_contract`, `professional_boundary` | `docs/TYPES.md` Section 11.1; `docs/PRD.md` Section 8.17 FR-108 |
> | Operation proposal fields relevant to validation fixtures | Proposal identity, profile identity, operation name, inputs, intended changes, deterministic checks, expected outputs, risks, required human gate, status | `docs/TYPES.md` Section 11.2; `docs/PRD.md` Section 8.17 FR-112 |
> | OpenPipeStress role | ADOPTED tier-0 fixture profile; no Chirality core solver behavior | `docs/TYPES.md` Section 11.3; `docs/PRD.md` Section 8.17 FR-114 |
> | Validation requirement | Domain profile validation is deterministic; invalid or incomplete profiles fail before runtime exposure | `docs/PRD.md` Section 8.17 FR-109 |
> | Mutation boundary | Protected domain-engine paths are not directly agent-writable | `docs/PRD.md` Section 8.17 FR-110; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-2 |
> | Professional boundary | Domain-engine output is not professional approval, code compliance, external validation, or Chirality-owned solver truth | `docs/PRD.md` Section 8.17 FR-115; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4 |
>

### CLM-004 — Conditions

> ##### Conditions
>
> | Condition | Value | Source |
> |---|---|---|
> | Runtime sequencing | Domain-engine profiles and operation proposals are future amendment work after core harness stability | `docs/PLAN.md` R7; `docs/PRD.md` R7 |
> | Staged/live boundary | D-APP-49 through D-APP-52 authorize the staged profile/type, registry, read and PEC-scoped propose/refresh/validate interfaces. Their retained implementation is compatibility evidence, not proof of live Codex exposure. D-GOV-43 / D-APP-127 select Codex; live-path composition and named verification remain delivery work. Endpoints, operation apply, direct protected writes/hooks, integration-level advancement and general domain runtime retain F-APP-3 and their separate gates. | `docs/SPEC.md` Section 18; D-APP-49 through D-APP-52 |
> | Protected path enforcement | Prompt text is not a sufficient safety boundary for filesystem writes or domain operations | `docs/CONTRACT.md` Section 1.6 K-PERM-2 |
> | Fixture specificity | OpenPipeStress-specific assumptions must live in profile and adapter layers, not in core harness runtime | `docs/PRD.md` Section 8.17 FR-114 |
> | Dependency state | Current `Dependencies.csv` preserves assigned inputs and DEP-10-04-004 future activation PENDING; DEP-10-04-008 is reopened for the independently captured current-candidate graph check, whose result is recorded in the current DepClosure audit | `_DEPENDENCIES.md` Declared Upstream/Downstream |
> | PRD source warning | Read current observed/reference-basis status in `_REFERENCES.md`; historical MATCH observations do not establish current equality | `_REFERENCES.md` REF-006; assignment override |
> | Future amendment gate | Accepted PKG-10 amendment or explicit human authorization is required before fixture implementation becomes active work | `_DEPENDENCIES.md` Extracted Dependency Register; `docs/PLAN.md` R7 |
>

### CLM-005 — Construction

> ##### Construction
>
> | Artifact | Expected Content | Status |
> |---|---|---|
> | Future fixture profile | A future OpenPipeStress `DomainEngineProfile` example or fixture using the generic profile contract | ADOPTED tier-0 OpenPipeStress/PEC profiles exist; App consumes evidence and does not author their files |
> | Validation tests | Deterministic checks for required profile fields, path separation, manifest rules, operation descriptors, and boundary notices | Existing `frontend/src/__tests__/lib/domain-profile.test.ts`, `domain-profile-registry.test.ts`, `domain-proposal-tools.test.ts`, `operation-proposal.test.ts`; missing cases remain in CLM-012/031 |
> | Adapter assumptions note | Notes separating OpenPipeStress profile/adapter assumptions from Chirality core runtime behavior | TBD - future amendment required before adapter assumptions become implementation truth |
> | Stable evidence records | Future pass/fail records for validation checks, expected failures, and professional-boundary wording coverage | `domain-engine-profile-validation/v1` records exist in `_DomainEngines/profiles/_validation/`; wording-coverage and outstanding negative-case evidence remain |
>

### CLM-006 — References

> ##### References
>
> - `_CONTEXT.md` for deliverable identity and scope.
> - `_DEPENDENCIES.md` for declared dependency state.
> - `_REFERENCES.md` for source corpus and PRD hash warning.
> - `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Sections 2.2, 5, and PKG-10 entry.
> - `docs/PRD.md` Sections 8.17, 10.10, R7, and knowledge gaps KG-016 through KG-020.
> - `docs/CONTRACT.md` Sections 1.1, 1.6, and 1.10.
> - `docs/SPEC.md` Sections 14.3 and 18.
> - `docs/TYPES.md` Sections 11.1 through 11.3.
> - `docs/PLAN.md` R7 and risk table.
>

### CLM-007 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> The 2026-07-12 UPD-153..157 record is historical. Current profile fields are in CLM-003/010; validation format is `domain-engine-profile-validation/v1`; Current `Dependencies.csv` preserves assigned inputs and DEP-10-04-004 future activation PENDING; DEP-10-04-008 is reopened at capture for the independent current DepClosure audit. Historical seven-SATISFIED counts describe the prior basis. D-APP-58 assigned manifest convention and D-APP-59 assigned Ryan Tufts; remaining fixture, adapter-assumptions and wording evidence is explicit in CLM-012/032.

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture

> #### Specification: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture
>
> REF-006 records an accepted reference basis, not perpetual current-byte equality. Read current observed hashes/status in `_REFERENCES.md`; retain expected hashes and use the parent D-APP-38 reconciliation for current drift. The 2026-07-12 MATCH observation is historical.
>

### CLM-009 — Scope

> ##### Scope
>
> This deliverable specifies the expected future validation posture for generic `DomainEngineProfile` records and an OpenPipeStress fixture profile. It is limited to future-boundary test-suite definition and source-grounded fixture expectations for PKG-10.
>
> The deliverable excludes current-release activation of domain-engine endpoints, domain-operation application, protected-model writes, solver integration, and any claim that Chirality approves or owns domain-engine solver truth. This exclusion is required by `docs/SPEC.md` Section 18, `docs/PLAN.md` R7, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Section 2.2.
>
> ResponsibleParty: Ryan Tufts (owner confirmation 2026-07-17; D-APP-59).
>
> DEP-10-04-004 remains the pending PKG-10 future-activation gate. ResponsibleParty, test paths, adapter-manifest convention and validation record format are assigned; new expected-failure fixtures and missing evidence remain unfinished. D-APP-58 and F-APP-3 reserve `_DomainEngines/**` authoring to the tier-0 bridge loop.
>

### CLM-010 — Requirements

> ##### Requirements
>
> | ID | Requirement | Source | Verification |
> |---|---|---|---|
> | DEL-10-04-REQ-001 | The validation posture shall distinguish the D-APP-49 through D-APP-52 authorized interfaces and retained compatibility tests from unverified Codex live-path exposure; endpoints, operation apply, protected-path hooks/writes, and general domain runtime remain gated and outside core runtime behavior. | `docs/PRD.md` Section 8.17; `docs/SPEC.md` Section 18; `docs/PLAN.md` R7 | Review fixture/test scope for the ruled staged partition and absence of endpoint/apply activation. |
> | DEL-10-04-REQ-002 | A profile validation fixture shall cover the generic profile fields: `schema_version`, `id`, `name`, `engine_type`, `profile_version`, `profile_status`, `integration_level`, `domain_root_patterns`, `authoritative_artifacts`, `chirality_readable_artifacts`, `protected_write_paths`, `agent_writable_paths`, `deterministic_tools`, `operation_proposal_contract`, `professional_boundary`. | `docs/TYPES.md` Section 11.1; `docs/PRD.md` Section 8.17 FR-108 | Validate required/optional field coverage in the future test suite. |
> | DEL-10-04-REQ-003 | Validation shall be deterministic and shall fail invalid or incomplete profiles before runtime exposure. | `docs/PRD.md` Section 8.17 FR-109 | Future tests include deterministic negative cases for missing or invalid fields. |
> | DEL-10-04-REQ-004 | The OpenPipeStress fixture shall be represented as a fixture profile only, with OpenPipeStress-specific assumptions held in profile and adapter layers rather than Chirality core runtime. | `docs/PRD.md` Section 8.17 FR-114; `docs/TYPES.md` Section 11.3 | Inspect future fixture/test names and assertions for core-runtime coupling. |
> | DEL-10-04-REQ-005 | Profile validation shall preserve separation between protected paths and proposal paths. | `docs/PRD.md` Section 8.17 FR-108 through FR-111; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-2 | Negative tests reject direct agent-write treatment of protected paths. |
> | DEL-10-04-REQ-006 | Any operation-related fixture data shall align with `OperationProposal` concepts before application: inputs, intended changes, deterministic checks, expected outputs, risks, and required human gate. | `docs/PRD.md` Section 8.17 FR-112 and FR-113; `docs/TYPES.md` Section 11.2 | Review future fixture operation descriptors against proposal fields. |
> | DEL-10-04-REQ-007 | Boundary notices shall state that Chirality does not provide professional approval, code compliance, external validation, or Chirality-owned solver truth. | `docs/PRD.md` Section 8.17 FR-115; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4; `docs/TYPES.md` Section 11.3 | Tests or review checklist require boundary notice presence and wording coverage. |
> | DEL-10-04-REQ-008 | The fixture/test suite shall not rely on prompt-only restrictions for protected paths or domain operations. | `docs/CONTRACT.md` Section 1.6 K-PERM-2; `docs/SPEC.md` Section 14.3 | Future implementation tests verify runtime or deterministic enforcement surfaces, not prompt text alone. |
> | DEL-10-04-REQ-009 | The deliverable shall preserve the accepted PRD reference basis and separately report current observed drift under D-APP-38. | `_REFERENCES.md` REF-006; D-APP-38 | Run records preserve the earlier warning as dated history only. |
> | DEL-10-04-REQ-010 | Future negative tests shall define deterministic expected failures, not only checklist labels. | `docs/PRD.md` Section 8.17 FR-109; `docs/TYPES.md` Sections 11.1 and 11.2 | Missing required fields, overlapping paths, incomplete operation proposals, absent boundary notices, and core-runtime-coupling cases each have expected failure evidence. |
> | DEL-10-04-REQ-011 | Future operation-descriptor fixtures shall cover inputs, intended changes, deterministic checks, expected outputs, risks, required human gate, and status before any operation can be applied. | `docs/PRD.md` Section 8.17 FR-112/FR-113; `docs/TYPES.md` Section 11.2 | Fixture review confirms each `OperationProposal` field is represented or explicitly marked TBD. |
> | DEL-10-04-REQ-012 | Future fixture validation shall produce stable evidence records for pass/fail determinations and boundary-notice wording coverage. | `docs/PRD.md` Section 8.17 FR-115; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4; `_DEPENDENCIES.md` Extracted Dependency Register | Use the assigned `domain-engine-profile-validation/v1` format and tier-0 `_validation` records; separate wording-coverage and negative-case evidence remains outstanding. |
>

### CLM-011 — Standards

> ##### Standards
>
> | Standard / Contract | Applicability |
> |---|---|
> | `docs/PRD.md` Section 8.17 | REF-006 records an accepted reference basis, not perpetual current-byte equality. Read current observed hashes/status in `_REFERENCES.md`; retain expected hashes and use the parent D-APP-38 reconciliation for current drift. The 2026-07-12 MATCH observation is historical. |
> | `docs/TYPES.md` Section 11 | Vocabulary and target shapes for `DomainEngineProfile`, `OperationProposal`, and domain terms. |
> | `docs/CONTRACT.md` Section 1.10 | Binding invariants for domain truth ownership, protected paths, human acceptance, and professional boundaries. |
> | `docs/SPEC.md` Section 18 | Specification boundary for future domain-engine endpoints/tools and non-implementation posture. |
> | `docs/PLAN.md` R7 | Sequencing and acceptance criteria for future amendment work. |
>

### CLM-012 — Verification

> ##### Verification
>
> Future validation should include, at minimum:
>
> | Check | Expected Result | Source |
> |---|---|---|
> | Required profile fields present | Missing required fields fail deterministically | `docs/PRD.md` Section 8.17 FR-108/FR-109 |
> | Protected/proposal path separation | Protected paths are not accepted as agent-writable proposal paths | `docs/PRD.md` Section 8.17 FR-110/FR-111 |
> | Operation descriptors | Operation fixture data is compatible with `OperationProposal` review and human gate concepts | `docs/TYPES.md` Section 11.2 |
> | Boundary notice | Fixture includes boundary notice text that prevents professional-approval or solver-truth overclaiming | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4 |
> | Core-runtime separation | OpenPipeStress does not appear as core harness behavior | `docs/PRD.md` Section 8.17 FR-114 |
> | Future-scope gate | Tests do not activate domain-engine endpoints/tools as current-release implementation | `docs/SPEC.md` Section 18 |
> | Expected failure fixtures | Each negative case has deterministic expected output or failure evidence | `docs/PRD.md` Section 8.17 FR-109 |
> | Operation proposal fixture coverage | Inputs, intended changes, deterministic checks, expected outputs, risks, human gate, and status are present or explicitly TBD | `docs/TYPES.md` Section 11.2 |
> | Evidence records | Future test run output records pass/fail result, source-warning posture, boundary-notice wording coverage, and no-current-release-activation check | `docs/PRD.md` Section 8.17 FR-115; `docs/SPEC.md` Section 18 |
>

### CLM-013 — Documentation

> Required artifacts: tier-0 ADOPTED fixture profiles and `domain-engine-profile-validation/v1` records; retained App validation tests; adapter assumptions note; deterministic expected-failure and boundary-wording coverage. D-APP-58 assigns `_DomainEngines/profiles/<profileId>.adapter.yaml` / `domain-engine-adapter-manifest/v1`; manifest instances/loader remain future engine-side work. The assumptions note and human-approved wording fixture remain outstanding.

### CLM-014 — Source Warnings

> REF-006 records an accepted reference basis, not perpetual current-byte equality. Read current observed hashes/status in `_REFERENCES.md`; retain expected hashes and use the parent D-APP-38 reconciliation for current drift. The 2026-07-12 MATCH observation is historical.

### CLM-015 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> The 2026-07-12 UPD-153..157 record is historical. Current profile fields are in CLM-003/010; validation format is `domain-engine-profile-validation/v1`; Current `Dependencies.csv` preserves assigned inputs and DEP-10-04-004 future activation PENDING; DEP-10-04-008 is reopened at capture for the independent current DepClosure audit. Historical seven-SATISFIED counts describe the prior basis. D-APP-58 assigned manifest convention and D-APP-59 assigned Ryan Tufts; remaining fixture, adapter-assumptions and wording evidence is explicit in CLM-012/032.
>

### CLM-016 — D-APP-56 ownership amendment (2026-07-12)

> D-APP-56 R4-P27 assigns DEL-10-04 accountability for PEC fixture content, validation and interaction evidence, distinct from DEL-10-01 registry mechanism and DEL-10-03 proposal interface. D-APP-58/F-APP-3 reserve writes to `_DomainEngines/**` to the tier-0 bridge loop: App owns consumption, test evidence and coordination, not those authoring writes. Verify `_DomainEngines/profiles/pec.yaml` and `_validation/pec.validation.json` through their owning source and App fixture tests. No PEC engine-status judgment, integration advance or App write permission is created.

- **AC-001** — Historical conversion preservation remains separately evidenced; the current contract preserves substantive obligations and remains limited to SOW-070 and OBJ-010 future fixture-profile and validation expectations without activating endpoints, operation apply, protected-path writes, solver integration, professional approval, code compliance, external validation, or Chirality-owned solver truth.

## Production and Verification Method — Praxeology

### CLM-017 — Procedure: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture

> #### Procedure: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture
>
> REF-006 records an accepted reference basis, not perpetual current-byte equality. Read current observed hashes/status in `_REFERENCES.md`; retain expected hashes and use the parent D-APP-38 reconciliation for current drift. The 2026-07-12 MATCH observation is historical.
>

### CLM-018 — Purpose

> ##### Purpose
>
> Define the operational procedure for producing and later verifying the DEL-10-04 future fixture profile, validation tests, and adapter assumptions note without activating domain-engine implementation.
>

### CLM-019 — Prerequisites

> ##### Prerequisites
>
> - Accepted PKG-10 amendment or explicit human authorization for future domain-engine work. Current sources keep domain profiles and operation proposals in future scope.
> - Accessible source corpus for `docs/PRD.md`, `docs/TYPES.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, and `docs/PLAN.md`.
> - ResponsibleParty assignment: Ryan Tufts (owner confirmation 2026-07-17; D-APP-59).
> - Four existing App test paths are identified in CLM-005; D-APP-58 assigns the adapter-manifest convention. Manifest instances remain engine-side future work.
> - Dependency posture: Read current `Dependencies.csv`; DEP-10-04-004 future activation remains PENDING, and DEP-10-04-008 awaits the independent current DepClosure audit at register capture. The dated seven-SATISFIED count belongs to the prior basis. Do not infer future activation from the satisfied inputs.
> - REF-006 records an accepted reference basis, not perpetual current-byte equality. Read current observed hashes/status in `_REFERENCES.md`; retain expected hashes and use the parent D-APP-38 reconciliation for current drift. The 2026-07-12 MATCH observation is historical.
>

### CLM-020 — Steps

> ##### Steps
>
> 1. Confirm scope gate.
>    - Verify PKG-10 remains future-boundary/gated scope unless a human-approved amendment says otherwise.
>    - Do not create or activate domain-engine endpoints, protected-path write behavior, or operation-apply workflows during this deliverable-local drafting run.
>
> 2. Define fixture validation target.
>    - Use `docs/TYPES.md` Section 11.1 as the candidate `DomainEngineProfile` shape.
>    - Mark any field semantics not defined by the accessible source corpus as TBD.
>
> 3. Draft or review a future OpenPipeStress fixture profile.
>    - Use OpenPipeStress only as fixture profile data.
>    - Keep OpenPipeStress solver assumptions in the profile or adapter-assumptions layer.
>    - Do not add OpenPipeStress assumptions to Chirality core runtime.
>
> 4. Define deterministic validation checks.
>    - Check required profile fields.
>    - Check protected/proposal path separation.
>    - Check operation descriptors against `OperationProposal` concepts where operation fixtures are present.
>    - Check deterministic adapter manifest presence or mark manifest rules TBD.
>    - Check boundary notice presence.
>    - For each negative case, record the deterministic expected failure or mark the expected output TBD.
>
> 5. Define negative validation cases.
>    - Missing required field.
>    - Overlapping protected and proposal paths.
>    - Missing boundary notice.
>    - Operation fixture without required human gate.
>    - Fixture or documentation that implies professional approval, code compliance, external validation, or Chirality-owned solver truth.
>
> 6. Produce adapter assumptions note.
>    - Separate accepted source facts from ASSUMPTION and TBD items.
>    - Identify which assumptions are profile-level, adapter-level, operation-proposal-level, or explicitly excluded from core runtime.
>
> 7. Verify no implementation activation occurred.
>    - Confirm no current-release endpoint/tool activation was introduced.
>    - For this records reconciliation, confirm formal dependency semantics remain unchanged.
>    - Confirm ResponsibleParty remains Ryan Tufts under D-APP-59.
>    - Confirm no future fixture output is treated as professional approval, code compliance, external validation, or Chirality-owned solver truth.
>

### CLM-021 — Verification

> ##### Verification
>
> | Verification Item | Expected Evidence |
> |---|---|
> | Current contract exists | `ScopeOfWork.md` definition, requirements, procedure and guidance sections are populated. |
> | Future-boundary posture preserved | Documents state that PKG-10 remains future-boundary/gated scope. |
> | Requirements source-grounded | Requirements cite accessible source sections or are labeled ASSUMPTION/TBD. |
> | OpenPipeStress not core | No instruction treats OpenPipeStress as Chirality core runtime behavior. |
> | Protected path policy preserved | Direct protected-domain writes are disallowed in requirements and guidance. |
> | Human gate preserved | Domain operations require explicit human acceptance before application. |
> | Professional boundary preserved | No language claims automated approval, code compliance, external validation, or solver truth ownership. |
> | Expected failures documented | Future negative tests include deterministic expected failure evidence or explicit TBDs. |
> | Current repair boundary | Only authorized records change; lifecycle, approval SHA and formal dependency semantics remain unchanged. Original P3 evidence remains historical. |
>

### CLM-022 — Records

> Existing evidence: `_DomainEngines/profiles/open_pipe_stress.yaml`, `pec.yaml`, their `_validation/*.validation.json` records and the four App tests named in CLM-005. Required format: `domain-engine-profile-validation/v1`. Still owed: adapter assumptions note, expected-failure fixtures, boundary-wording fixture/coverage and no-activation evidence. Dated P3/NO_STATUS_TOUCH instructions governed their historical pass; this record repair changes no lifecycle or formal dependency.

### CLM-023 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> The 2026-07-12 UPD-153..157 record is historical. Current profile fields are in CLM-003/010; validation format is `domain-engine-profile-validation/v1`; Current `Dependencies.csv` preserves assigned inputs and DEP-10-04-004 future activation PENDING; DEP-10-04-008 is reopened at capture for the independent current DepClosure audit. Historical seven-SATISFIED counts describe the prior basis. D-APP-58 assigned manifest convention and D-APP-59 assigned Ryan Tufts; remaining fixture, adapter-assumptions and wording evidence is explicit in CLM-012/032.

- **VER-001** — Review the current ScopeOfWork claims and output matrix against their cited requirements and retained gates. Historical conversion/parity evidence is recovered in `R5/CONVERSION_EVIDENCE_REVIEW.csv` of RUN_D128_CONCORDANCE_2026-09-21_1614Z; it proves the dated conversion only. Current reconciliation uses W10_CHANGES.csv and independent changed-block review; product and human-acceptance checks remain separately required.

## Governing Values and Decisions — Axiology

### CLM-024 — Guidance: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture

> #### Guidance: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture
>
> REF-006 records an accepted reference basis, not perpetual current-byte equality. Read current observed hashes/status in `_REFERENCES.md`; retain expected hashes and use the parent D-APP-38 reconciliation for current drift. The 2026-07-12 MATCH observation is historical.
>

### CLM-025 — Purpose

> ##### Purpose
>
> DEL-10-04 exists to keep future Domain Engine Profile validation and an OpenPipeStress fixture representable without turning Chirality into a domain-specific solver or moving domain operations into current-release scope. The accepted decomposition describes this as a TEST_SUITE deliverable for validating generic domain profiles and modeling OpenPipeStress as a future fixture without hardcoding solver assumptions into core.
>

### CLM-026 — Principles

> ##### Principles
>
> 1. Treat PKG-10 as future-boundary work. `docs/PLAN.md` R7 and `docs/SPEC.md` Section 18 place domain profiles, operations, and endpoints in future amendment scope.
> 2. Keep the profile generic before fixture-specific details. `docs/PRD.md` Section 8.17 FR-107 requires a generic `DomainEngineProfile` contract before engine-specific integration.
> 3. Validate deterministically. `docs/PRD.md` Section 8.17 FR-109 requires invalid or incomplete profiles to fail before runtime exposure.
> 4. Separate protected truth from proposals. `docs/CONTRACT.md` Section 1.10 K-DOMAIN-2 and `docs/PRD.md` Section 8.17 FR-110/FR-111 require agents to write proposals and summaries, not protected domain-engine model truth.
> 5. Preserve human gates. `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 and `docs/PRD.md` Section 8.17 FR-113 require explicit human acceptance before applying domain operations.
> 6. Keep professional boundaries visible. `docs/CONTRACT.md` Section 1.1 K-AUTH-1 and Section 1.10 K-DOMAIN-4 prohibit representing agent, runtime, or domain adapter output as professional approval, code compliance, external validation, or Chirality-owned solver truth.
>

### CLM-027 — Considerations

> ##### Considerations
>
> - The future fixture should test the generic shape first: identity, protected paths, proposal paths, artifact types, operations, manifest rules, and boundary notices.
> - The ADOPTED `open_pipe_stress` profile is concrete tier-0 evidence. Further fixture production and exposure retain DEP-10-04-004; no solver assumptions become core behavior.
> - A useful future validation suite should include negative cases. Examples include missing boundary notice, protected path listed as proposal path, missing deterministic adapter manifest rule, incomplete operation descriptor, or fixture wording that implies Chirality owns solver truth.
> - Existing test locations are named in CLM-005; missing negative cases and exposure wiring still require the owning bounded implementation brief and gate.
> - ASSUMPTION: The adapter assumptions note should distinguish profile-level assumptions, adapter-manifest assumptions, operation-proposal assumptions, and explicit non-assumptions about Chirality core runtime.
> - Future adapter assumptions should separate at least four classes: profile-level fixture facts, adapter-level manifest and execution assumptions, operation-proposal-level human-gated change assumptions, and explicit core-runtime non-assumptions. This preserves `docs/PRD.md` Section 8.17 FR-114 without making OpenPipeStress behavior part of the harness core.
> - REF-006 records an accepted reference basis, not perpetual current-byte equality. Read current observed hashes/status in `_REFERENCES.md`; retain expected hashes and use the parent D-APP-38 reconciliation for current drift. The 2026-07-12 MATCH observation is historical.
>

### CLM-028 — Trade-offs

> ##### Trade-offs
>
> | Trade-off | Guidance | Source |
> |---|---|---|
> | Concrete OpenPipeStress examples vs. core neutrality | Use OpenPipeStress only as fixture data; do not put OpenPipeStress concepts in public core runtime contracts. | `docs/PRD.md` Section 8.17 FR-114 |
> | Agent convenience vs. protected domain truth | Prefer proposal paths and review aids; reject direct protected model writes. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-2 |
> | Prompt instruction vs. runtime enforcement | Do not rely on prompt-only controls for writes, tool exposure, or domain operations. | `docs/CONTRACT.md` Section 1.6 K-PERM-2 |
> | Early domain integration vs. runtime spine stability | Keep profile validation future-scoped until core harness stability. | `docs/PLAN.md` R7; `docs/PRD.md` R7 |
> | Early fixture detail vs. evidence quality | Prefer TBDs and deterministic expected-failure slots over unsupported OpenPipeStress values, solver assumptions, or file formats. | `docs/PRD.md` Section 8.17 FR-109/FR-114 |
>

### CLM-029 — Examples

> ##### Examples
>

### CLM-030 — Candidate Positive Fixture Shape

> Positive fixture evidence exists at `_DomainEngines/profiles/open_pipe_stress.yaml` (id `open_pipe_stress`) with its `_validation/open_pipe_stress.validation.json` record. Read the declared fields and integration level; this does not establish new Codex exposure or satisfy all path-separation/core-separation/wording checks.

### CLM-031 — Candidate Negative Cases

> ###### Candidate Negative Cases
>
> - Missing `professional_boundary`.
> - `protected_write_paths` and `agent_writable_paths` overlap.
> - Operation descriptor lacks deterministic checks.
> - Fixture text states or implies Chirality approves engineering work.
> - OpenPipeStress behavior is asserted as core harness runtime behavior.
>
> The missing-field cases have retained test evidence in `domain-profile.test.ts`; overlapping-path, core-coupling and wording-coverage expected failures remain unfinished. Test paths are assigned; new fixture execution retains DEP-10-04-004 and the owning implementation brief.
>

### CLM-032 — Future Evidence Checklist

> Assigned: ResponsibleParty Ryan Tufts (D-APP-59); ADOPTED positive profile paths; four App test paths (CLM-005); adapter-manifest convention/schema (D-APP-58); `domain-engine-profile-validation/v1` result format. Outstanding under DEP-10-04-004: overlapping-path/core-coupling expected failures; operation-proposal fixture records with human-gate evidence; boundary-wording fixture/coverage; adapter assumptions note; current exposure/no-activation evidence. Manifest instances remain tier-0 bridge future work.

### CLM-033 — Conflict Table (for human ruling)

> CT-001 is a dated source-status observation, not an unruled source-content conflict. Preserve the accepted reference basis and report current observed drift in `_REFERENCES.md` through D-APP-38; do not renew an owner prompt merely to repair stale MATCH prose.

### CLM-034 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

> ##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)
>
> The 2026-07-12 UPD-153..157 record is historical. Current profile fields are in CLM-003/010; validation format is `domain-engine-profile-validation/v1`; Current `Dependencies.csv` preserves assigned inputs and DEP-10-04-004 future activation PENDING; DEP-10-04-008 is reopened at capture for the independent current DepClosure audit. Historical seven-SATISFIED counts describe the prior basis. D-APP-58 assigned manifest convention and D-APP-59 assigned Ryan Tufts; remaining fixture, adapter-assumptions and wording evidence is explicit in CLM-012/032.

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-070 OBJ-010 | CLM-008 | AC-001 | VER-001 | Historical conversion mapping; current claim-block review and applicable named verification evidence |
