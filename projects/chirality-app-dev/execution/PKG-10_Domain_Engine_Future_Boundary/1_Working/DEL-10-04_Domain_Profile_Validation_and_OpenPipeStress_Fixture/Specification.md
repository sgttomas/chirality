# Specification: DEL-10-04 Domain Profile Validation and OpenPipeStress Fixture

> **D-APP-56 R5 P40 current-state note (2026-07-12):** REF-006 `docs/PRD.md` is `MATCH` under D-APP-38. Any older warning, bypass, or human-ruling wording about the former hash mismatch in this document is dated drafting history and does not describe current source state.

## Scope

This deliverable specifies the expected future validation posture for generic `DomainEngineProfile` records and an OpenPipeStress fixture profile. It is limited to future-boundary test-suite definition and source-grounded fixture expectations for PKG-10.

The deliverable excludes current-release activation of domain-engine endpoints, domain-operation application, protected-model writes, solver integration, and any claim that Chirality approves or owns domain-engine solver truth. This exclusion is required by `docs/SPEC.md` Section 18, `docs/PLAN.md` R7, and `execution/_Decomposition/Chirality_App_vNext_SOFTWARE_DECOMP_v3_2.md` Section 2.2.

ResponsibleParty remains TBD.

Current fixture implementation authority remains TBD. Before this deliverable can become executable implementation work, a human-approved PKG-10 amendment or explicit authorization must identify the ResponsibleParty, concrete test path, adapter manifest location, evidence-record format, and expected-failure fixtures.

## Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| DEL-10-04-REQ-001 | The validation posture shall treat `DomainEngineProfile` as a future platform contract, not current core runtime behavior. | `docs/PRD.md` Section 8.17; `docs/SPEC.md` Section 18; `docs/PLAN.md` R7 | Review fixture/test scope for absence of current-release endpoint activation. |
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

## Standards

| Standard / Contract | Applicability |
|---|---|
| `docs/PRD.md` Section 8.17 | REF-006 is MATCH under D-APP-38; the earlier warning is dated history. |
| `docs/TYPES.md` Section 11 | Vocabulary and target shapes for `DomainEngineProfile`, `OperationProposal`, and domain terms. |
| `docs/CONTRACT.md` Section 1.10 | Binding invariants for domain truth ownership, protected paths, human acceptance, and professional boundaries. |
| `docs/SPEC.md` Section 18 | Specification boundary for future domain-engine endpoints/tools and non-implementation posture. |
| `docs/PLAN.md` R7 | Sequencing and acceptance criteria for future amendment work. |

## Verification

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

## Documentation

Required or anticipated artifacts:

- Future fixture profile.
- Validation tests.
- Adapter assumptions note.
- ASSUMPTION: A future amendment will identify concrete file paths, test framework locations, and adapter manifest format before implementation.
- TBD: Future evidence-record path and format for deterministic pass/fail decisions.
- TBD: Human-approved boundary-notice wording fixture for professional-boundary coverage.

## Source Warnings

| Warning | Impact |
|---|---|
| REF-006 `docs/PRD.md` has expected SHA256 `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd` and observed SHA256 `ac35fba40fabf3d5788b8dd285d376900dbfa4577a83bcf77798d06770c30bfd`. | Treated as source status per assignment override; requirements cite PRD sections conservatively, preserve the MATCH visibly, and require human acceptance or refreshed source metadata before closure reliance. — reconciled under D-APP-38 |
