---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-10-04
package_id: PKG-10
decomposition_basis: projects/chirality-app-dev/execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md@ff59428ff27d929bc1172e6c049a5e274d487fc0
project_scope_refs: [SOW-070]
package_objective_refs: [OBJ-010]
---

# Scope of Work — DEL-10-04

## Purpose and Objective Traceability

This migration candidate defines `DEL-10-04` in service of project scope [SOW-070] and package objectives [OBJ-010].

- **OUT-001** — The DEL-10-04 source-preserving production contract for the future OpenPipeStress fixture profile, validation tests, and adapter assumptions note, without hardcoding solver assumptions into Chirality core.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":4,"line_start":1,"source_sha256":"b7a0b38d1dc6940a8fc85a2c139f81bb153850d117b435710d4c573c38a69331","target_id":"CLM-001"} -->
#### Datasheet: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-002 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":22,"line_start":5,"source_sha256":"b7a0b38d1dc6940a8fc85a2c139f81bb153850d117b435710d4c573c38a69331","target_id":"CLM-002"} -->
##### Identification

| Field | Value |
|---|---|
| DeliverableID | DEL-10-04 |
| DeliverableName | Domain Profile Validation and OpenPipeStress Fixture |
| PackageID | PKG-10 |
| PackageName | Domain Engine Future Boundary |
| DecompositionVariant | SOFTWARE_DECOMP |
| DecompositionRevision | v3.2 |
| ResponsibleParty | TBD |
| Type | TEST_SUITE |
| ContextEnvelope | M |
| ScopeItem | SOW-070 |
| Objective | OBJ-010 |
| Source posture | Future-boundary/gated scope; not current-release domain operation execution |
| Validation evidence owner | TBD - no human owner is assigned for interpreting future fixture pass/fail evidence |

<!-- sow-source-end -->

### CLM-003 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":34,"line_start":23,"source_sha256":"b7a0b38d1dc6940a8fc85a2c139f81bb153850d117b435710d4c573c38a69331","target_id":"CLM-003"} -->
##### Attributes

| Attribute | Value | Source |
|---|---|---|
| Primary subject | Validation of generic domain profiles and OpenPipeStress as a future fixture profile | `_CONTEXT.md` Deliverable Scope; `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` PKG-10 table |
| Domain profile contract fields | `profileId`, `engineName`, optional `engineVersion`, `protectedPaths`, `proposalPaths`, `artifactTypes`, `operations`, `manifestRules`, `boundaryNotice` | `docs/TYPES.md` Section 11.1; `docs/PRD.md` Section 8.17 FR-108 |
| Operation proposal fields relevant to validation fixtures | Proposal identity, profile identity, operation name, inputs, intended changes, deterministic checks, expected outputs, risks, required human gate, status | `docs/TYPES.md` Section 11.2; `docs/PRD.md` Section 8.17 FR-112 |
| OpenPipeStress role | Potential first domain profile fixture, not Chirality core runtime behavior | `docs/TYPES.md` Section 11.3; `docs/PRD.md` Section 8.17 FR-114 |
| Validation requirement | Domain profile validation is deterministic; invalid or incomplete profiles fail before runtime exposure | `docs/PRD.md` Section 8.17 FR-109 |
| Mutation boundary | Protected domain-engine paths are not directly agent-writable | `docs/PRD.md` Section 8.17 FR-110; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-2 |
| Professional boundary | Domain-engine output is not professional approval, code compliance, external validation, or Chirality-owned solver truth | `docs/PRD.md` Section 8.17 FR-115; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4 |

<!-- sow-source-end -->

### CLM-004 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":46,"line_start":35,"source_sha256":"b7a0b38d1dc6940a8fc85a2c139f81bb153850d117b435710d4c573c38a69331","target_id":"CLM-004"} -->
##### Conditions

| Condition | Value | Source |
|---|---|---|
| Runtime sequencing | Domain-engine profiles and operation proposals are future amendment work after core harness stability | `docs/PLAN.md` R7; `docs/PRD.md` R7 |
| Staged/live boundary | Source types/guards, the closed registry, ruled read tools, and pec-scoped loopback propose/refresh/validate tools are live under D-APP-49 through D-APP-52; endpoints, apply, and protected-path hooks/writes remain future/gated | `docs/SPEC.md` Section 18; D-APP-49 through D-APP-52 |
| Protected path enforcement | Prompt text is not a sufficient safety boundary for filesystem writes or domain operations | `docs/CONTRACT.md` Section 1.6 K-PERM-2 |
| Fixture specificity | OpenPipeStress-specific assumptions must live in profile and adapter layers, not in core harness runtime | `docs/PRD.md` Section 8.17 FR-114 |
| Dependency state | Declared upstream and downstream dependencies are TBD until dependency extraction and project graph validation occur | `_DEPENDENCIES.md` Declared Upstream/Downstream |
| PRD source warning | expected and observed PRD hashes match under D-APP-38; dispatch treats this as a source status | `_REFERENCES.md` REF-006; assignment override |
| Future amendment gate | Accepted PKG-10 amendment or explicit human authorization is required before fixture implementation becomes active work | `_DEPENDENCIES.md` Extracted Dependency Register; `docs/PLAN.md` R7 |

<!-- sow-source-end -->

### CLM-005 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":55,"line_start":47,"source_sha256":"b7a0b38d1dc6940a8fc85a2c139f81bb153850d117b435710d4c573c38a69331","target_id":"CLM-005"} -->
##### Construction

| Artifact | Expected Content | Status |
|---|---|---|
| Future fixture profile | A future OpenPipeStress `DomainEngineProfile` example or fixture using the generic profile contract | TBD - no accepted fixture file exists in this deliverable yet |
| Validation tests | Deterministic checks for required profile fields, path separation, manifest rules, operation descriptors, and boundary notices | TBD - test framework and target files are not assigned in this gated scope |
| Adapter assumptions note | Notes separating OpenPipeStress profile/adapter assumptions from Chirality core runtime behavior | TBD - future amendment required before adapter assumptions become implementation truth |
| Stable evidence records | Future pass/fail records for validation checks, expected failures, and professional-boundary wording coverage | TBD - no record format or artifact path has been assigned |

<!-- sow-source-end -->

### CLM-006 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":67,"line_start":56,"source_sha256":"b7a0b38d1dc6940a8fc85a2c139f81bb153850d117b435710d4c573c38a69331","target_id":"CLM-006"} -->
##### References

- `_CONTEXT.md` for deliverable identity and scope.
- `_DEPENDENCIES.md` for declared dependency state.
- `_REFERENCES.md` for source corpus and PRD hash warning.
- `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Sections 2.2, 5, and PKG-10 entry.
- `docs/PRD.md` Sections 8.17, 10.10, R7, and knowledge gaps KG-016 through KG-020.
- `docs/CONTRACT.md` Sections 1.1, 1.6, and 1.10.
- `docs/SPEC.md` Sections 14.3 and 18.
- `docs/TYPES.md` Sections 11.1 through 11.3.
- `docs/PLAN.md` R7 and risk table.

<!-- sow-source-end -->

### CLM-007 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":70,"line_start":68,"source_sha256":"b7a0b38d1dc6940a8fc85a2c139f81bb153850d117b435710d4c573c38a69331","target_id":"CLM-007"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-153/154/155/156 align profile fields to the canonical snake_case view, adopt `domain-engine-profile-validation/v1`, record SATISFIED 4 / PENDING 4 with named residuals, and distinguish landed profiles/tests/reports from genuine adapter-manifest and wording-coverage TBDs. UPD-157 closes DEP-10-04-008 against D53A.
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":4,"line_start":1,"source_sha256":"1619f0f26e86fdbe5decedd14ce55399b9608b4a8ab2d0f44792c514dee7c6ed","target_id":"CLM-008"} -->
#### Specification: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-009 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":14,"line_start":5,"source_sha256":"1619f0f26e86fdbe5decedd14ce55399b9608b4a8ab2d0f44792c514dee7c6ed","target_id":"CLM-009"} -->
##### Scope

This deliverable specifies the expected future validation posture for generic `DomainEngineProfile` records and an OpenPipeStress fixture profile. It is limited to future-boundary test-suite definition and source-grounded fixture expectations for PKG-10.

The deliverable excludes current-release activation of domain-engine endpoints, domain-operation application, protected-model writes, solver integration, and any claim that Chirality approves or owns domain-engine solver truth. This exclusion is required by `docs/SPEC.md` Section 18, `docs/PLAN.md` R7, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Section 2.2.

ResponsibleParty remains TBD.

Current fixture implementation authority remains TBD. Before this deliverable can become executable implementation work, a human-approved PKG-10 amendment or explicit authorization must identify the ResponsibleParty, concrete test path, adapter manifest location, evidence-record format, and expected-failure fixtures.

<!-- sow-source-end -->

### CLM-010 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":31,"line_start":15,"source_sha256":"1619f0f26e86fdbe5decedd14ce55399b9608b4a8ab2d0f44792c514dee7c6ed","target_id":"CLM-010"} -->
##### Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| DEL-10-04-REQ-001 | The validation posture shall treat source types/guards, the closed registry, and loopback read/propose/validate tools as the D-APP-49 through D-APP-52 staged-live surface; endpoints, operation apply, protected-path hooks/writes, and general domain runtime remain gated and outside core runtime behavior. | `docs/PRD.md` Section 8.17; `docs/SPEC.md` Section 18; `docs/PLAN.md` R7 | Review fixture/test scope for the ruled staged partition and absence of endpoint/apply activation. |
| DEL-10-04-REQ-002 | A profile validation fixture shall cover the generic profile fields: `profileId`, `engineName`, optional `engineVersion`, `protectedPaths`, `proposalPaths`, `artifactTypes`, `operations`, `manifestRules`, and `boundaryNotice`. | `docs/TYPES.md` Section 11.1; `docs/PRD.md` Section 8.17 FR-108 | Validate required/optional field coverage in the future test suite. |
| DEL-10-04-REQ-003 | Validation shall be deterministic and shall fail invalid or incomplete profiles before runtime exposure. | `docs/PRD.md` Section 8.17 FR-109 | Future tests include deterministic negative cases for missing or invalid fields. |
| DEL-10-04-REQ-004 | The OpenPipeStress fixture shall be represented as a fixture profile only, with OpenPipeStress-specific assumptions held in profile and adapter layers rather than Chirality core runtime. | `docs/PRD.md` Section 8.17 FR-114; `docs/TYPES.md` Section 11.3 | Inspect future fixture/test names and assertions for core-runtime coupling. |
| DEL-10-04-REQ-005 | Profile validation shall preserve separation between protected paths and proposal paths. | `docs/PRD.md` Section 8.17 FR-108 through FR-111; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-2 | Negative tests reject direct agent-write treatment of protected paths. |
| DEL-10-04-REQ-006 | Any operation-related fixture data shall align with `OperationProposal` concepts before application: inputs, intended changes, deterministic checks, expected outputs, risks, and required human gate. | `docs/PRD.md` Section 8.17 FR-112 and FR-113; `docs/TYPES.md` Section 11.2 | Review future fixture operation descriptors against proposal fields. |
| DEL-10-04-REQ-007 | Boundary notices shall state that Chirality does not provide professional approval, code compliance, external validation, or Chirality-owned solver truth. | `docs/PRD.md` Section 8.17 FR-115; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4; `docs/TYPES.md` Section 11.3 | Tests or review checklist require boundary notice presence and wording coverage. |
| DEL-10-04-REQ-008 | The fixture/test suite shall not rely on prompt-only restrictions for protected paths or domain operations. | `docs/CONTRACT.md` Section 1.6 K-PERM-2; `docs/SPEC.md` Section 14.3 | Future implementation tests verify runtime or deterministic enforcement surfaces, not prompt text alone. |
| DEL-10-04-REQ-009 | The deliverable shall preserve the reconciled PRD reference state: REF-006 is `MATCH` under D-APP-38. | `_REFERENCES.md` REF-006; D-APP-38 | Run records preserve the earlier warning as dated history only. |
| DEL-10-04-REQ-010 | Future negative tests shall define deterministic expected failures, not only checklist labels. | `docs/PRD.md` Section 8.17 FR-109; `docs/TYPES.md` Sections 11.1 and 11.2 | Missing required fields, overlapping paths, incomplete operation proposals, absent boundary notices, and core-runtime-coupling cases each have expected failure evidence. |
| DEL-10-04-REQ-011 | Future operation-descriptor fixtures shall cover inputs, intended changes, deterministic checks, expected outputs, risks, required human gate, and status before any operation can be applied. | `docs/PRD.md` Section 8.17 FR-112/FR-113; `docs/TYPES.md` Section 11.2 | Fixture review confirms each `OperationProposal` field is represented or explicitly marked TBD. |
| DEL-10-04-REQ-012 | Future fixture validation shall produce stable evidence records for pass/fail determinations and boundary-notice wording coverage. | `docs/PRD.md` Section 8.17 FR-115; `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4; `_DEPENDENCIES.md` Extracted Dependency Register | Evidence record path and format remain TBD until future amendment assigns them. |

<!-- sow-source-end -->

### CLM-011 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":41,"line_start":32,"source_sha256":"1619f0f26e86fdbe5decedd14ce55399b9608b4a8ab2d0f44792c514dee7c6ed","target_id":"CLM-011"} -->
##### Standards

| Standard / Contract | Applicability |
|---|---|
| `docs/PRD.md` Section 8.17 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
| `docs/TYPES.md` Section 11 | Vocabulary and target shapes for `DomainEngineProfile`, `OperationProposal`, and domain terms. |
| `docs/CONTRACT.md` Section 1.10 | Binding invariants for domain truth ownership, protected paths, human acceptance, and professional boundaries. |
| `docs/SPEC.md` Section 18 | Specification boundary for future domain-engine endpoints/tools and non-implementation posture. |
| `docs/PLAN.md` R7 | Sequencing and acceptance criteria for future amendment work. |

<!-- sow-source-end -->

### CLM-012 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":57,"line_start":42,"source_sha256":"1619f0f26e86fdbe5decedd14ce55399b9608b4a8ab2d0f44792c514dee7c6ed","target_id":"CLM-012"} -->
##### Verification

Future validation should include, at minimum:

| Check | Expected Result | Source |
|---|---|---|
| Required profile fields present | Missing required fields fail deterministically | `docs/PRD.md` Section 8.17 FR-108/FR-109 |
| Protected/proposal path separation | Protected paths are not accepted as agent-writable proposal paths | `docs/PRD.md` Section 8.17 FR-110/FR-111 |
| Operation descriptors | Operation fixture data is compatible with `OperationProposal` review and human gate concepts | `docs/TYPES.md` Section 11.2 |
| Boundary notice | Fixture includes boundary notice text that prevents professional-approval or solver-truth overclaiming | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-4 |
| Core-runtime separation | OpenPipeStress does not appear as core harness behavior | `docs/PRD.md` Section 8.17 FR-114 |
| Future-scope gate | Tests do not activate domain-engine endpoints/tools as current-release implementation | `docs/SPEC.md` Section 18 |
| Expected failure fixtures | Each negative case has deterministic expected output or failure evidence | `docs/PRD.md` Section 8.17 FR-109 |
| Operation proposal fixture coverage | Inputs, intended changes, deterministic checks, expected outputs, risks, human gate, and status are present or explicitly TBD | `docs/TYPES.md` Section 11.2 |
| Evidence records | Future test run output records pass/fail result, source-warning posture, boundary-notice wording coverage, and no-current-release-activation check | `docs/PRD.md` Section 8.17 FR-115; `docs/SPEC.md` Section 18 |

<!-- sow-source-end -->

### CLM-013 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":68,"line_start":58,"source_sha256":"1619f0f26e86fdbe5decedd14ce55399b9608b4a8ab2d0f44792c514dee7c6ed","target_id":"CLM-013"} -->
##### Documentation

Required or anticipated artifacts:

- Future fixture profile.
- Validation tests.
- Adapter assumptions note.
- ASSUMPTION: A future amendment will identify concrete file paths, test framework locations, and adapter manifest format before implementation.
- TBD: Future evidence-record path and format for deterministic pass/fail decisions.
- TBD: Human-approved boundary-notice wording fixture for professional-boundary coverage.

<!-- sow-source-end -->

### CLM-014 — Source Warnings

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":74,"line_start":69,"source_sha256":"1619f0f26e86fdbe5decedd14ce55399b9608b4a8ab2d0f44792c514dee7c6ed","target_id":"CLM-014"} -->
##### Source Warnings

| Warning | Impact |
|---|---|
| REF-006 `docs/PRD.md` has expected SHA256 `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd` and observed SHA256 `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd`. | Treated as source status per assignment override; requirements cite PRD sections conservatively, preserve the MATCH visibly, and require human acceptance or refreshed source metadata before closure reliance. — reconciled under D-APP-38 |

<!-- sow-source-end -->

### CLM-015 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":78,"line_start":75,"source_sha256":"1619f0f26e86fdbe5decedd14ce55399b9608b4a8ab2d0f44792c514dee7c6ed","target_id":"CLM-015"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-153/154/155/156 align profile fields to the canonical snake_case view, adopt `domain-engine-profile-validation/v1`, record SATISFIED 4 / PENDING 4 with named residuals, and distinguish landed profiles/tests/reports from genuine adapter-manifest and wording-coverage TBDs. UPD-157 closes DEP-10-04-008 against D53A.

<!-- sow-source-end -->

### CLM-016 — D-APP-56 ownership amendment (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":81,"line_start":79,"source_sha256":"1619f0f26e86fdbe5decedd14ce55399b9608b4a8ab2d0f44792c514dee7c6ed","target_id":"CLM-016"} -->
##### D-APP-56 ownership amendment (2026-07-12)

Under R4-P27, this deliverable owns the PEC fixture profile (`_DomainEngines/profiles/pec.yaml`), its v1 validation record (`_validation/pec.validation.json`), the PEC registry-entry content, and evidence from PEC-profile-scoped fixture interaction. The shared registry mechanism and gate remain DEL-10-01 scope; the generic proposal-tool surface remains DEL-10-03 scope. PEC engine status is not judged by this amendment.
<!-- sow-source-end -->

- **AC-001** — Every exact legacy source range is preserved, and the converted contract remains limited to SOW-070 and OBJ-010 future fixture-profile and validation expectations without activating endpoints, operation apply, protected-path writes, solver integration, professional approval, code compliance, external validation, or Chirality-owned solver truth.

## Production and Verification Method — Praxeology

### CLM-017 — Procedure: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":4,"line_start":1,"source_sha256":"111352948b891e57df8d809c303fd5cb5e9dc9f30ded07eafcdd91ceedfd8893","target_id":"CLM-017"} -->
#### Procedure: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-018 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":8,"line_start":5,"source_sha256":"111352948b891e57df8d809c303fd5cb5e9dc9f30ded07eafcdd91ceedfd8893","target_id":"CLM-018"} -->
##### Purpose

Define the operational procedure for producing and later verifying the DEL-10-04 future fixture profile, validation tests, and adapter assumptions note without activating domain-engine implementation.

<!-- sow-source-end -->

### CLM-019 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":17,"line_start":9,"source_sha256":"111352948b891e57df8d809c303fd5cb5e9dc9f30ded07eafcdd91ceedfd8893","target_id":"CLM-019"} -->
##### Prerequisites

- Accepted PKG-10 amendment or explicit human authorization for future domain-engine work. Current sources keep domain profiles and operation proposals in future scope.
- Accessible source corpus for `docs/PRD.md`, `docs/TYPES.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, and `docs/PLAN.md`.
- ResponsibleParty assignment: TBD.
- Concrete future test path and adapter manifest location: TBD.
- Dependency posture: `_DEPENDENCIES.md` now contains extracted ACTIVE rows, but all satisfaction remains `PENDING`; accepted declared upstream/downstream closure and project graph validation remain TBD.
- REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

<!-- sow-source-end -->

### CLM-020 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":57,"line_start":18,"source_sha256":"111352948b891e57df8d809c303fd5cb5e9dc9f30ded07eafcdd91ceedfd8893","target_id":"CLM-020"} -->
##### Steps

1. Confirm scope gate.
   - Verify PKG-10 remains future-boundary/gated scope unless a human-approved amendment says otherwise.
   - Do not create or activate domain-engine endpoints, protected-path write behavior, or operation-apply workflows during this deliverable-local drafting run.

2. Define fixture validation target.
   - Use `docs/TYPES.md` Section 11.1 as the candidate `DomainEngineProfile` shape.
   - Mark any field semantics not defined by the accessible source corpus as TBD.

3. Draft or review a future OpenPipeStress fixture profile.
   - Use OpenPipeStress only as fixture profile data.
   - Keep OpenPipeStress solver assumptions in the profile or adapter-assumptions layer.
   - Do not add OpenPipeStress assumptions to Chirality core runtime.

4. Define deterministic validation checks.
   - Check required profile fields.
   - Check protected/proposal path separation.
   - Check operation descriptors against `OperationProposal` concepts where operation fixtures are present.
   - Check deterministic adapter manifest presence or mark manifest rules TBD.
   - Check boundary notice presence.
   - For each negative case, record the deterministic expected failure or mark the expected output TBD.

5. Define negative validation cases.
   - Missing required field.
   - Overlapping protected and proposal paths.
   - Missing boundary notice.
   - Operation fixture without required human gate.
   - Fixture or documentation that implies professional approval, code compliance, external validation, or Chirality-owned solver truth.

6. Produce adapter assumptions note.
   - Separate accepted source facts from ASSUMPTION and TBD items.
   - Identify which assumptions are profile-level, adapter-level, operation-proposal-level, or explicitly excluded from core runtime.

7. Verify no implementation activation occurred.
   - Confirm no current-release endpoint/tool activation was introduced.
   - Confirm this P3 four-documents task did not create, edit, or promote `Dependencies.csv`.
   - Confirm ResponsibleParty remains TBD.
   - Confirm no future fixture output is treated as professional approval, code compliance, external validation, or Chirality-owned solver truth.

<!-- sow-source-end -->

### CLM-021 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":71,"line_start":58,"source_sha256":"111352948b891e57df8d809c303fd5cb5e9dc9f30ded07eafcdd91ceedfd8893","target_id":"CLM-021"} -->
##### Verification

| Verification Item | Expected Evidence |
|---|---|
| Four-document kit exists | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are non-empty. |
| Future-boundary posture preserved | Documents state that PKG-10 remains future-boundary/gated scope. |
| Requirements source-grounded | Requirements cite accessible source sections or are labeled ASSUMPTION/TBD. |
| OpenPipeStress not core | No instruction treats OpenPipeStress as Chirality core runtime behavior. |
| Protected path policy preserved | Direct protected-domain writes are disallowed in requirements and guidance. |
| Human gate preserved | Domain operations require explicit human acceptance before application. |
| Professional boundary preserved | No language claims automated approval, code compliance, external validation, or solver truth ownership. |
| Expected failures documented | Future negative tests include deterministic expected failure evidence or explicit TBDs. |
| P3 scope preserved | `_STATUS.md`, `_SEMANTIC_LENSING.md`, metadata files, and dependency registers are not modified by the P3 four-documents pass. |

<!-- sow-source-end -->

### CLM-022 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":81,"line_start":72,"source_sha256":"111352948b891e57df8d809c303fd5cb5e9dc9f30ded07eafcdd91ceedfd8893","target_id":"CLM-022"} -->
##### Records

- Future fixture profile: TBD.
- Validation tests: TBD.
- Adapter assumptions note: TBD.
- Stable validation evidence record format: TBD.
- Human-approved boundary-notice wording fixture: TBD.
- TASK run record under `_run_records/`.
- `_STATUS.md` not changed during P3_ONLY because `_SEMANTIC_LENSING.md` declares `NO_STATUS_TOUCH`.

<!-- sow-source-end -->

### CLM-023 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":84,"line_start":82,"source_sha256":"111352948b891e57df8d809c303fd5cb5e9dc9f30ded07eafcdd91ceedfd8893","target_id":"CLM-023"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-153/154/155/156 align profile fields to the canonical snake_case view, adopt `domain-engine-profile-validation/v1`, record SATISFIED 4 / PENDING 4 with named residuals, and distinguish landed profiles/tests/reports from genuine adapter-manifest and wording-coverage TBDs. UPD-157 closes DEP-10-04-008 against D53A.
<!-- sow-source-end -->

- **VER-001** — Run the deterministic validator, claim mapper, parity reporter, checklist compiler, and renderer against the exact source/control kit; confirm source and status bytes are unchanged and negative format/checklist fixtures fail closed.

## Governing Values and Decisions — Axiology

### CLM-024 — Guidance: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":4,"line_start":1,"source_sha256":"432be5db7636121e9948fe5f2c1a2bad1cccbe9e9c3f92c79baf693bd42f97a0","target_id":"CLM-024"} -->
#### Guidance: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

<!-- sow-source-end -->

### CLM-025 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":8,"line_start":5,"source_sha256":"432be5db7636121e9948fe5f2c1a2bad1cccbe9e9c3f92c79baf693bd42f97a0","target_id":"CLM-025"} -->
##### Purpose

DEL-10-04 exists to keep future Domain Engine Profile validation and an OpenPipeStress fixture representable without turning Chirality into a domain-specific solver or moving domain operations into current-release scope. The accepted decomposition describes this as a TEST_SUITE deliverable for validating generic domain profiles and modeling OpenPipeStress as a future fixture without hardcoding solver assumptions into core.

<!-- sow-source-end -->

### CLM-026 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":17,"line_start":9,"source_sha256":"432be5db7636121e9948fe5f2c1a2bad1cccbe9e9c3f92c79baf693bd42f97a0","target_id":"CLM-026"} -->
##### Principles

1. Treat PKG-10 as future-boundary work. `docs/PLAN.md` R7 and `docs/SPEC.md` Section 18 place domain profiles, operations, and endpoints in future amendment scope.
2. Keep the profile generic before fixture-specific details. `docs/PRD.md` Section 8.17 FR-107 requires a generic `DomainEngineProfile` contract before engine-specific integration.
3. Validate deterministically. `docs/PRD.md` Section 8.17 FR-109 requires invalid or incomplete profiles to fail before runtime exposure.
4. Separate protected truth from proposals. `docs/CONTRACT.md` Section 1.10 K-DOMAIN-2 and `docs/PRD.md` Section 8.17 FR-110/FR-111 require agents to write proposals and summaries, not protected domain-engine model truth.
5. Preserve human gates. `docs/CONTRACT.md` Section 1.10 K-DOMAIN-3 and `docs/PRD.md` Section 8.17 FR-113 require explicit human acceptance before applying domain operations.
6. Keep professional boundaries visible. `docs/CONTRACT.md` Section 1.1 K-AUTH-1 and Section 1.10 K-DOMAIN-4 prohibit representing agent, runtime, or domain adapter output as professional approval, code compliance, external validation, or Chirality-owned solver truth.

<!-- sow-source-end -->

### CLM-027 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":27,"line_start":18,"source_sha256":"432be5db7636121e9948fe5f2c1a2bad1cccbe9e9c3f92c79baf693bd42f97a0","target_id":"CLM-027"} -->
##### Considerations

- The future fixture should test the generic shape first: identity, protected paths, proposal paths, artifact types, operations, manifest rules, and boundary notices.
- OpenPipeStress can be a concrete profile fixture only after the generic profile boundary is accepted by amendment. Until then, OpenPipeStress-specific values, solver assumptions, file formats, and execution semantics remain TBD.
- A useful future validation suite should include negative cases. Examples include missing boundary notice, protected path listed as proposal path, missing deterministic adapter manifest rule, incomplete operation descriptor, or fixture wording that implies Chirality owns solver truth.
- ASSUMPTION: Future test locations will be selected by the package implementation plan after PKG-10 amendment; no current source assigns concrete test paths for DEL-10-04.
- ASSUMPTION: The adapter assumptions note should distinguish profile-level assumptions, adapter-manifest assumptions, operation-proposal assumptions, and explicit non-assumptions about Chirality core runtime.
- Future adapter assumptions should separate at least four classes: profile-level fixture facts, adapter-level manifest and execution assumptions, operation-proposal-level human-gated change assumptions, and explicit core-runtime non-assumptions. This preserves `docs/PRD.md` Section 8.17 FR-114 without making OpenPipeStress behavior part of the harness core.
- REF-006 is `MATCH` under D-APP-38; the earlier warning is dated history.

<!-- sow-source-end -->

### CLM-028 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":37,"line_start":28,"source_sha256":"432be5db7636121e9948fe5f2c1a2bad1cccbe9e9c3f92c79baf693bd42f97a0","target_id":"CLM-028"} -->
##### Trade-offs

| Trade-off | Guidance | Source |
|---|---|---|
| Concrete OpenPipeStress examples vs. core neutrality | Use OpenPipeStress only as fixture data; do not put OpenPipeStress concepts in public core runtime contracts. | `docs/PRD.md` Section 8.17 FR-114 |
| Agent convenience vs. protected domain truth | Prefer proposal paths and review aids; reject direct protected model writes. | `docs/CONTRACT.md` Section 1.10 K-DOMAIN-2 |
| Prompt instruction vs. runtime enforcement | Do not rely on prompt-only controls for writes, tool exposure, or domain operations. | `docs/CONTRACT.md` Section 1.6 K-PERM-2 |
| Early domain integration vs. runtime spine stability | Keep profile validation future-scoped until core harness stability. | `docs/PLAN.md` R7; `docs/PRD.md` R7 |
| Early fixture detail vs. evidence quality | Prefer TBDs and deterministic expected-failure slots over unsupported OpenPipeStress values, solver assumptions, or file formats. | `docs/PRD.md` Section 8.17 FR-109/FR-114 |

<!-- sow-source-end -->

### CLM-029 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":39,"line_start":38,"source_sha256":"432be5db7636121e9948fe5f2c1a2bad1cccbe9e9c3f92c79baf693bd42f97a0","target_id":"CLM-029"} -->
##### Examples

<!-- sow-source-end -->

### CLM-030 — Candidate Positive Fixture Shape

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":43,"line_start":40,"source_sha256":"432be5db7636121e9948fe5f2c1a2bad1cccbe9e9c3f92c79baf693bd42f97a0","target_id":"CLM-030"} -->
###### Candidate Positive Fixture Shape

TBD - no accepted fixture file exists. A future positive fixture should be a generic `DomainEngineProfile` instance for `openpipestress` with required fields present, protected/proposal path separation, operation descriptors, manifest rules, and boundary notice.

<!-- sow-source-end -->

### CLM-031 — Candidate Negative Cases

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":53,"line_start":44,"source_sha256":"432be5db7636121e9948fe5f2c1a2bad1cccbe9e9c3f92c79baf693bd42f97a0","target_id":"CLM-031"} -->
###### Candidate Negative Cases

- Missing `boundaryNotice`.
- `protectedPaths` and `proposalPaths` overlap.
- Operation descriptor lacks deterministic checks.
- Fixture text states or implies Chirality approves engineering work.
- OpenPipeStress behavior is asserted as core harness runtime behavior.

These are candidate examples only; they require future amendment and test-path assignment before implementation.

<!-- sow-source-end -->

### CLM-032 — Future Evidence Checklist

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":65,"line_start":54,"source_sha256":"432be5db7636121e9948fe5f2c1a2bad1cccbe9e9c3f92c79baf693bd42f97a0","target_id":"CLM-032"} -->
###### Future Evidence Checklist

TBD until amendment assigns files and owner:

- Concrete positive fixture path.
- Negative fixture paths and deterministic expected failures.
- Adapter manifest location and rule semantics.
- Operation proposal fixture records with required human gate.
- Boundary notice wording fixture.
- Stable validation result record format.
- No-current-release-activation evidence.

<!-- sow-source-end -->

### CLM-033 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":71,"line_start":66,"source_sha256":"432be5db7636121e9948fe5f2c1a2bad1cccbe9e9c3f92c79baf693bd42f97a0","target_id":"CLM-033"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CT-001 | No source-content conflict identified during P1/P2. PRD hash status: MATCH is recorded as a source status per dispatch. | `_REFERENCES.md` REF-006 | Assignment override | All documents citing PRD | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. | TBD — reconciled under D-APP-38 |

<!-- sow-source-end -->

### CLM-034 — D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":74,"line_start":72,"source_sha256":"432be5db7636121e9948fe5f2c1a2bad1cccbe9e9c3f92c79baf693bd42f97a0","target_id":"CLM-034"} -->
##### D-APP-56 R5 P45 current-state reconciliation (2026-07-12)

UPD-153/154/155/156 align profile fields to the canonical snake_case view, adopt `domain-engine-profile-validation/v1`, record SATISFIED 4 / PENDING 4 with named residuals, and distinguish landed profiles/tests/reports from genuine adapter-manifest and wording-coverage TBDs. UPD-157 closes DEP-10-04-008 against D53A.
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-070 OBJ-010 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
