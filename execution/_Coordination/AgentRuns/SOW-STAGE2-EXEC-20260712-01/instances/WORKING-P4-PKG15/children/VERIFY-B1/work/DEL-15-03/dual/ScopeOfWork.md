---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-15-03
package_id: PKG-15
decomposition_basis: projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@e8f59a63372f38d9e788ac39b39995558f5aba73
project_scope_refs: [SOW-074]
package_objective_refs: [OBJ-017]
---

# Scope of Work — DEL-15-03

## Purpose and Objective Traceability

This migration candidate defines `DEL-15-03` in service of project scope [SOW-074] and package objectives [OBJ-017].

- **OUT-001** — A generic schema-compliant downstream modeling export workflow contract using invented target evidence and explicit unsupported-target findings is produced.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-15-03 Downstream modeling export workflow

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":3,"line_start":1,"source_sha256":"8fbb54cf31d998872bd1834cf3dea3cfe4db500594f168425e58b8e6746cd4a8","target_id":"CLM-001"} -->
#### Datasheet: DEL-15-03 Downstream modeling export workflow

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-002 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":11,"line_start":4,"source_sha256":"8fbb54cf31d998872bd1834cf3dea3cfe4db500594f168425e58b8e6746cd4a8","target_id":"CLM-002"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-15-03-DECL-002`.

<!-- sow-source-end -->

### CLM-003 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":26,"line_start":12,"source_sha256":"8fbb54cf31d998872bd1834cf3dea3cfe4db500594f168425e58b8e6746cd4a8","target_id":"CLM-003"} -->
##### Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-15-03 | `_CONTEXT.md` |
| Name | Downstream modeling export workflow | `_CONTEXT.md` |
| Package ID | PKG-15 | `_CONTEXT.md` |
| Package name | Handoff and External Prover Workflow | `_CONTEXT.md` |
| Type | BACKEND_FEATURE_SLICE | `_CONTEXT.md` |
| Discipline | ASSUMPTION: software backend / interop handoff workflow | `_CONTEXT.md`; `SOFTWARE_DECOMP.md#PKG-15` |
| Scope coverage | SOW-074 | `_CONTEXT.md`; `SOFTWARE_DECOMP.md#Structured Scope of Work` |
| Objective support | OBJ-017 | `_CONTEXT.md`; `SOFTWARE_DECOMP.md#Objectives` |
| Context envelope | L; WATCH | `_CONTEXT.md`; `docs/_Registers/ContextBudgetQA.csv` |
| Anticipated artifacts | handoff exporter; export validation tests; invented target fixture | `_CONTEXT.md` |

<!-- sow-source-end -->

### CLM-004 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":38,"line_start":27,"source_sha256":"8fbb54cf31d998872bd1834cf3dea3cfe4db500594f168425e58b8e6746cd4a8","target_id":"CLM-004"} -->
##### Attributes

| Attribute | Value | Source |
|---|---|---|
| Workflow purpose | Implement the generic handoff export path before target-specific commercial-tool parsers are in scope. | `_CONTEXT.md`; `SOFTWARE_DECOMP.md#PKG-15` |
| Required handoff package content | Model hash, units manifest, entity IDs, library/rule references, unresolved assumptions, warnings, target mapping metadata, and unsupported-target flags. | `_CONTEXT.md#Scope Detail`; `SOFTWARE_DECOMP.md#SOW-074` |
| Handoff object meaning | Schema-compliant export for downstream modeling and professional validation workflows. | `SOFTWARE_DECOMP.md#Vocabulary and semantic commitments` |
| Architecture baseline | Rust core/application services; JSON Schema 2020-12 contracts; schema-first command/query/job result envelopes; producer-declared JSON hash byte-basis labels carried unchanged; Cargo/Vitest/Playwright/validation/protected-content test gates as applicable. | `_CONTEXT.md#Architecture Basis Injection`; D-41 R5 T2A |
| Backend artifact boundary | Generic export workflow only; target-specific commercial parser behavior remains deferred. | `_CONTEXT.md#Context Envelope`; `SOFTWARE_DECOMP.md#Open issues` |
| Professional boundary | Handoff and external-prover metadata support must not create automatic professional approval states. | `SOFTWARE_DECOMP.md#OBJ-017`; `docs/CONTRACT.md#Invariant catalog` |
| Data boundary | Public artifacts must not bundle protected standards text, protected tables, proprietary commercial data, private rule packs, owner standards, or code-specific acceptance criteria. | `docs/IP_AND_DATA_BOUNDARY.md#Public repository must not contain`; `docs/CONTRACT.md#Invariant catalog` |

<!-- sow-source-end -->

### CLM-005 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":49,"line_start":39,"source_sha256":"8fbb54cf31d998872bd1834cf3dea3cfe4db500594f168425e58b8e6746cd4a8","target_id":"CLM-005"} -->
##### Conditions

| Condition | Status |
|---|---|
| Target surfaces, canonical package container, and target-specific implementation | OI-015 names initial export and target surfaces; canonical package container, concrete mappings, target field coverage, and target-specific implementation remain gated by DEL-17-01 and DEL-17-02. |
| Exact dependency versions and package-specific implementation choices | TBD per `_CONTEXT.md#Architecture Basis Injection`. |
| Target-specific commercial stress output parsers | Deferred per `_CONTEXT.md#Context Envelope` and `SOFTWARE_DECOMP.md#SOW-074`. |
| Professional approval, certification, sealing, or code-compliance claims | Excluded by `docs/CONTRACT.md` OPS-K-AUTH-1 and OPS-K-AGENT-4. |
| Unit handling | Exports must remain unit-aware and validate against `schemas/handoff_package.schema.json` and `schemas/target_mapping.schema.json`; target-specific unit export strategy remains TBD under OI-015. |
| Private/protected data | Must be excluded unless intentionally supplied with documented rights through a governed path. |

<!-- sow-source-end -->

### CLM-006 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":60,"line_start":50,"source_sha256":"8fbb54cf31d998872bd1834cf3dea3cfe4db500594f168425e58b8e6746cd4a8","target_id":"CLM-006"} -->
##### Construction

| Construct | Datasheet value |
|---|---|
| Primary input contracts | ACTIVE upstream rows in local `Dependencies.csv`, plus `schemas/handoff_package.schema.json` and `schemas/target_mapping.schema.json`. |
| Primary output | Generic handoff exporter at `core/handoff/exporter/workflow.py` capable of producing a schema-compliant handoff package and provider-neutral target mapping record. |
| Validation evidence | `tests/test_handoff_export_workflow.py` validates exported handoff/mapping inputs against schema contracts and checks `fixtures/invented_target_fixture.json` provenance. |
| Unsupported target behavior | Must surface unsupported-target flags and warnings; taxonomy and target mapping records are provided by upstream contract work. |
| Hash handling | Package/model checksum/reference fields preserve the producer-declared byte-basis label. DEL-15-03 does not recompute, relabel, or assert JCS conformance; package container and target-specific hash packaging remain TBD. |
| Fixture data | Invented target fixture only; no protected commercial-tool examples or proprietary data. |

<!-- sow-source-end -->

### CLM-007 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":71,"line_start":61,"source_sha256":"8fbb54cf31d998872bd1834cf3dea3cfe4db500594f168425e58b8e6746cd4a8","target_id":"CLM-007"} -->
##### References

- `_CONTEXT.md` - deliverable identity, scope, architecture-basis injection, and anticipated artifacts.
- `_REFERENCES.md` - source list for this deliverable.
- `_DEPENDENCIES.md` and `Dependencies.csv` - approved DAG-006 mirror/evidence surface for upstream workflow context.
- `execution/_Decomposition/SOFTWARE_DECOMP.md` - revision 0.7 package, scope, objective, decision, and open-issue context.
- `docs/CONTRACT.md` - invariant catalog.
- `docs/SPEC.md` - schema-first, unit-aware, provenance, diagnostics, and handoff-related architecture context.
- `docs/TYPES.md` - canonical object and boundary vocabulary.
- `docs/IP_AND_DATA_BOUNDARY.md` - public/private and protected-content boundary.
- `docs/AGENTIC_DEVELOPMENT_WORKFLOW.md` - deliverable execution and review rules.
<!-- sow-source-end -->

### CLM-008 — D-41 R5 T2A supplied-checksum evidence (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":74,"line_start":72,"source_sha256":"8fbb54cf31d998872bd1834cf3dea3cfe4db500594f168425e58b8e6746cd4a8","target_id":"CLM-008"} -->
##### D-41 R5 T2A supplied-checksum evidence (2026-07-12)

The downstream workflow carries supplied checksum records without recomputing them. Its governed invented records now use `deterministic_sorted_compact_json_payload_hash`; this is a narrow byte-basis label, not a JCS assertion by DEL-15-03.
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-009 — Specification: DEL-15-03 Downstream modeling export workflow

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":2,"line_start":1,"source_sha256":"376f959ae588a66db1690543b55827b46a4b850539b6657ec0874cb045c35f74","target_id":"CLM-009"} -->
#### Specification: DEL-15-03 Downstream modeling export workflow

<!-- sow-source-end -->

### CLM-010 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":20,"line_start":3,"source_sha256":"376f959ae588a66db1690543b55827b46a4b850539b6657ec0874cb045c35f74","target_id":"CLM-010"} -->
##### Scope

This deliverable covers a generic backend export workflow for downstream modeling handoff packages. It is scoped to SOW-074 and OBJ-017: producing traceable, schema-compliant handoff packages for downstream modeling and professional validation workflows without creating automatic professional approval states.

Included artifacts are:

- handoff exporter;
- export validation tests;
- invented target fixture.

Excluded work:

- target-specific commercial stress output parsers;
- comprehensive commercial-tool result ingestion;
- formal prover-status lifecycle, automatic professional acceptance record, certification, sealing, approval, authentication, or code-compliance status;
- protected standards text, tables, examples, formulas, proprietary commercial data, private rule packs, owner standards, or code-specific acceptance criteria;
- canonical package container, concrete mappings, target field coverage, target-specific implementation, dependency versions, and package-specific implementation choices until separately resolved.

<!-- sow-source-end -->

### CLM-011 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":35,"line_start":21,"source_sha256":"376f959ae588a66db1690543b55827b46a4b850539b6657ec0874cb045c35f74","target_id":"CLM-011"} -->
##### Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| DEL-15-03-REQ-001 | The workflow shall generate schema-compliant handoff packages. | SOW-074 in `_CONTEXT.md` and `SOFTWARE_DECOMP.md` | `tests/test_handoff_export_workflow.py` validates exported handoff packages against `schemas/handoff_package.schema.json`. |
| DEL-15-03-REQ-002 | The package data surfaced by the workflow shall include or preserve model hash, units manifest, entity IDs, library/rule references, unresolved assumptions, warnings, target mapping metadata, and unsupported-target flags. | SOW-074 in `_CONTEXT.md` and `SOFTWARE_DECOMP.md` | Fixture-based validation that required fields are present or explicitly reported as TBD/unsupported according to upstream schema contracts. |
| DEL-15-03-REQ-003 | The workflow shall remain generic and shall not implement target-specific commercial-tool parsers in this deliverable. | `_CONTEXT.md#Context Envelope`; `SOFTWARE_DECOMP.md#SOW-074`; OI-015 | Tests or review evidence confirming invented target fixture use and no commercial parser fixture dependency. |
| DEL-15-03-REQ-004 | The workflow shall preserve unit metadata across the export boundary. | `docs/CONTRACT.md` OPS-K-UNIT-1; `docs/SPEC.md#Unit system and dimensional analysis` | Schema validation and unit-manifest checks. |
| DEL-15-03-REQ-005 | The workflow shall preserve diagnostics, warnings, unresolved assumptions, provenance, and hashes rather than hiding missing data or boundary risks. | `docs/CONTRACT.md` OPS-K-DATA-2, OPS-K-REPORT-1; `docs/TYPES.md` Diagnostic, Assumption, Checksum, ResultExportEnvelope | Export validation tests and review of generated diagnostics/warnings. |
| DEL-15-03-REQ-006 | The workflow shall not claim certification, sealing, approval, authentication, professional acceptance, or engineering code compliance. | `docs/CONTRACT.md` OPS-K-AUTH-1, OPS-K-AGENT-4; `SOFTWARE_DECOMP.md` OBJ-017 and DEC-015 | Protected/professional-boundary wording review and tests where applicable. |
| DEL-15-03-REQ-007 | Public fixtures and examples shall use invented or otherwise cleared data and shall not copy protected standards content, commercial software examples, or proprietary data. | `docs/IP_AND_DATA_BOUNDARY.md`; `docs/CONTRACT.md` OPS-K-IP-1 through OPS-K-IP-3 | Protected-content review, fixture provenance review, and validation gate. |
| DEL-15-03-REQ-008 | The workflow shall respect schema-first contracts and JSON Schema 2020-12 and shall preserve the producer-declared checksum byte-basis label. DEL-15-03 carries supplied hashes without recomputing or relabeling them and therefore makes no independent JCS claim. | `_CONTEXT.md#Architecture Basis Injection`; `SOFTWARE_DECOMP.md` DEC-009 through DEC-012; D-41 R5 T2A | Implementation review verifies checksum metadata is carried unchanged and no unproved JCS assertion is introduced. |
| DEL-15-03-REQ-009 | The workflow shall consume upstream handoff/mapping/security/model-transformation context only through explicit contracts or approved dependency evidence. | Local `Dependencies.csv`; `_DEPENDENCIES.md` | Dependency review; no sibling deliverable source copying without an approved input contract. |
| DEL-15-03-REQ-010 | Missing target behavior, missing mapping support, or unsupported features shall be explicit findings or unsupported-target flags, not silent defaults. | SOW-074; `docs/CONTRACT.md` OPS-K-DATA-2; OI-015 | Validation tests using the invented target fixture. |

<!-- sow-source-end -->

### CLM-012 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":45,"line_start":36,"source_sha256":"376f959ae588a66db1690543b55827b46a4b850539b6657ec0874cb045c35f74","target_id":"CLM-012"} -->
##### Standards

| Standard or governing source | Applicability | Status |
|---|---|---|
| JSON Schema 2020-12 | Contract basis for schema-backed handoff/package validation. | Applicable from `_CONTEXT.md#Architecture Basis Injection`; current upstream schemas are `schemas/handoff_package.schema.json` and `schemas/target_mapping.schema.json`. |
| Producer-declared JSON hash basis | Carry supplied checksum algorithm, payload scope, digest, and canonicalization label unchanged; no recomputation or conformance ruling by this workflow. | Applicable from `_CONTEXT.md#Architecture Basis Injection`; exact producer payload boundaries remain external to DEL-15-03. |
| OpenPipeStress invariant catalog | Governs data, unit, professional-boundary, IP, privacy, and agent-output constraints. | Applicable from `docs/CONTRACT.md`. |
| IP and Data Boundary Policy | Governs protected-content, private-data, fixture, and provenance handling. | Applicable from `docs/IP_AND_DATA_BOUNDARY.md`. |
| Commercial stress tool formats | Target-specific parsers and commercial examples are out of scope. | Deferred; concrete mappings, target field coverage, and target-specific implementation remain gated by OI-015, DEL-17-01, and DEL-17-02. |

<!-- sow-source-end -->

### CLM-013 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":56,"line_start":46,"source_sha256":"376f959ae588a66db1690543b55827b46a4b850539b6657ec0874cb045c35f74","target_id":"CLM-013"} -->
##### Verification

| Verification item | Evidence expected |
|---|---|
| Schema compliance | Validation tests for handoff package output against `schemas/handoff_package.schema.json` and target mapping input against `schemas/target_mapping.schema.json`. |
| Unit manifest preservation | Tests that exported values carry explicit unit metadata or are explicitly dimensionless/TBD according to schema rules. |
| Hash/provenance preservation | Tests or review evidence for model/package hash fields, provenance fields, and unresolved assumptions. |
| Unsupported-target behavior | Invented target fixture that exercises unsupported or approximate mapping behavior without using proprietary commercial examples. |
| Boundary wording | Review confirming no generated metadata or report-adjacent output claims professional approval, certification, sealing, authentication, or code compliance. |
| Protected-content screening | Protected-content/provenance gate for fixture and example data. |

<!-- sow-source-end -->

### CLM-014 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":65,"line_start":57,"source_sha256":"376f959ae588a66db1690543b55827b46a4b850539b6657ec0874cb045c35f74","target_id":"CLM-014"} -->
##### Documentation

Required records for this deliverable are:

- implementation notes identifying `core/handoff/exporter/workflow.py` and the schema-backed output contract;
- export validation test evidence;
- invented target fixture provenance and protected-content review status;
- any unresolved target mapping, package container, hash boundary, or dependency-version TBDs;
- dependency closure evidence for required upstream contracts before this workflow is treated as implementation-ready.
<!-- sow-source-end -->

### CLM-015 — D-41 R5 T2A checksum-boundary requirement (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":68,"line_start":66,"source_sha256":"376f959ae588a66db1690543b55827b46a4b850539b6657ec0874cb045c35f74","target_id":"CLM-015"} -->
##### D-41 R5 T2A checksum-boundary requirement (2026-07-12)

DEL-15-03 SHALL preserve supplied checksum metadata without relabeling it as JCS and SHALL NOT imply that carrying a checksum constitutes recomputation, validation, or RFC 8785 conformance.
<!-- sow-source-end -->

- **AC-001** — The contract preserves all SOW-074 handoff contents, supplied checksum metadata without recomputation or relabeling, unit and provenance boundaries, diagnostics, warnings, assumptions, schema validation, public-safe invented fixtures, explicit unsupported behavior, upstream contract boundaries, target-specific parser and package-container gates, and professional non-authority without claiming JCS conformance, external validation, or approval.

## Production and Verification Method — Praxeology

### CLM-016 — Procedure: DEL-15-03 Downstream modeling export workflow

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":2,"line_start":1,"source_sha256":"9542e9e6b7d2f5adad73650cecf2d13e46ac6e89a6ec5027160abe9e11f28d2d","target_id":"CLM-016"} -->
#### Procedure: DEL-15-03 Downstream modeling export workflow

<!-- sow-source-end -->

### CLM-017 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":6,"line_start":3,"source_sha256":"9542e9e6b7d2f5adad73650cecf2d13e46ac6e89a6ec5027160abe9e11f28d2d","target_id":"CLM-017"} -->
##### Purpose

Define the conservative procedure for producing and validating the generic downstream modeling export workflow for DEL-15-03.

<!-- sow-source-end -->

### CLM-018 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":17,"line_start":7,"source_sha256":"9542e9e6b7d2f5adad73650cecf2d13e46ac6e89a6ec5027160abe9e11f28d2d","target_id":"CLM-018"} -->
##### Prerequisites

| Prerequisite | Source / status |
|---|---|
| Deliverable scope, package, artifacts, and architecture basis reviewed. | `_CONTEXT.md` |
| Invariants for data boundary, unit handling, professional boundary, and agent output reviewed. | `docs/CONTRACT.md` |
| Protected-content and public/private data boundary reviewed. | `docs/IP_AND_DATA_BOUNDARY.md` |
| Approved DAG-002 mirror rows preserved as ACTIVE evidence. | `_DEPENDENCIES.md`; `Dependencies.csv` |
| Upstream architecture-basis context available for DEL-00-01, DEL-00-02, DEL-00-03, DEL-00-04, DEL-00-06, DEL-00-07, and DEL-00-08. | Local `Dependencies.csv` |
| Upstream interop/handoff/security/model context identified for DEL-15-01, DEL-15-02, DEL-10-02, DEL-10-03, DEL-12-02, DEL-13-04, and DEL-14-05. | Local `Dependencies.csv` |

<!-- sow-source-end -->

### CLM-019 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":30,"line_start":18,"source_sha256":"9542e9e6b7d2f5adad73650cecf2d13e46ac6e89a6ec5027160abe9e11f28d2d","target_id":"CLM-019"} -->
##### Steps

1. Confirm the work remains inside DEL-15-03 and SOW-074. If implementation needs target-specific commercial parsers, commercial examples, professional approval states, or cross-package rewrites, stop and escalate.
2. Identify the upstream handoff package schema and target-mapping contracts available to the implementation: `schemas/handoff_package.schema.json` and `schemas/target_mapping.schema.json`. If later target-specific inputs are not implementation-ready, record the missing inputs as TBD rather than inventing schema fields.
3. Define the generic exporter boundary: input model/result context, output handoff package envelope, validation result, warnings, unresolved assumptions, target mapping metadata, unsupported-target flags, and hash/provenance handling.
4. Implement or review the exporter using the accepted architecture basis applicable to this backend slice at `core/handoff/exporter/workflow.py`; package-specific dependency versions remain TBD unless resolved by accepted source material.
5. Ensure exported payloads preserve unit metadata, entity IDs, references, diagnostics/warnings, assumptions, and hash metadata required by the upstream handoff package contract.
6. Add unsupported-target handling that records explicit findings or flags when the target fixture lacks a supported mapping. Do not silently drop or coerce unsupported behavior.
7. Create an invented target fixture. Record fixture provenance and protected-content review status; do not use commercial-tool examples or protected standards-derived examples.
8. Add export validation tests for schema compliance, unit manifest presence, required identity/reference fields, warnings/assumptions, unsupported-target flags, and professional-boundary wording.
9. Run applicable validation gates: `python3 tests/test_handoff_export_workflow.py`, schema validation for exported handoff and mapping inputs, dependency validation, and protected-content/provenance review.
10. Record unresolved assumptions, upstream contract gaps, unsupported features, and any dependency conflicts in deliverable-local evidence.

<!-- sow-source-end -->

### CLM-020 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":42,"line_start":31,"source_sha256":"9542e9e6b7d2f5adad73650cecf2d13e46ac6e89a6ec5027160abe9e11f28d2d","target_id":"CLM-020"} -->
##### Verification

| Check | Expected result |
|---|---|
| Scope check | Work remains a generic handoff export workflow for DEL-15-03. |
| Schema check | Output validates against `schemas/handoff_package.schema.json` and `schemas/target_mapping.schema.json`. |
| Unit check | Unit-bearing exported values carry explicit unit metadata or a documented dimensionless/TBD classification. |
| Warning/assumption check | Missing data and unsupported target behavior are explicit findings, not silent defaults. |
| Boundary check | Output does not claim certification, sealing, approval, authentication, professional acceptance, or code compliance. |
| Fixture check | Invented target fixture has provenance and does not use protected or commercial-tool example data. |
| Dependency check | Approved DAG-002 mirror rows remain preserved; no dependency extraction refresh reclassifies them without human approval. |

<!-- sow-source-end -->

### CLM-021 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":51,"line_start":43,"source_sha256":"9542e9e6b7d2f5adad73650cecf2d13e46ac6e89a6ec5027160abe9e11f28d2d","target_id":"CLM-021"} -->
##### Records

- Exporter implementation path: `core/handoff/exporter/workflow.py`.
- Export validation test path: `tests/test_handoff_export_workflow.py`.
- Invented target fixture path and provenance: `fixtures/invented_target_fixture.json`, validated as invented public metadata.
- Handoff schema version or source: `schemas/handoff_package.schema.json`.
- Target mapping taxonomy/source: `schemas/target_mapping.schema.json`.
- Dependency validation evidence: `Dependencies.csv` schema validation output.
- Boundary review evidence: focused protected/private/prohibited-authority term scan and exporter tests.
<!-- sow-source-end -->

### CLM-022 — D-41 R5 T2A checksum-boundary check (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":54,"line_start":52,"source_sha256":"9542e9e6b7d2f5adad73650cecf2d13e46ac6e89a6ec5027160abe9e11f28d2d","target_id":"CLM-022"} -->
##### D-41 R5 T2A checksum-boundary check (2026-07-12)

Verify that model and manifest checksum labels are carried unchanged into export payload context and that DEL-15-03 makes no independent JCS claim or checksum-validity ruling.
<!-- sow-source-end -->

- **VER-001** — Validate the contract and review source parity, complete handoff content preservation, schema and unit checks, supplied-checksum byte-basis labels, diagnostic and unsupported-target behavior, invented-fixture and protected-content controls, retained target-specific and container TBDs, upstream contract boundaries, and prohibited professional-authority claims.

## Governing Values and Decisions — Axiology

### CLM-023 — Guidance: DEL-15-03 Downstream modeling export workflow

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":2,"line_start":1,"source_sha256":"0d2618f3dcd836bbf981e65d8036971a585e044157194e7882fe60032561f315","target_id":"CLM-023"} -->
#### Guidance: DEL-15-03 Downstream modeling export workflow

<!-- sow-source-end -->

### CLM-024 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":6,"line_start":3,"source_sha256":"0d2618f3dcd836bbf981e65d8036971a585e044157194e7882fe60032561f315","target_id":"CLM-024"} -->
##### Purpose

This deliverable exists to provide the generic handoff export workflow that turns OpenPipeStress model and analysis context into schema-compliant downstream modeling handoff packages. Its purpose is traceable transfer, not external-tool validation or professional approval.

<!-- sow-source-end -->

### CLM-025 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":17,"line_start":7,"source_sha256":"0d2618f3dcd836bbf981e65d8036971a585e044157194e7882fe60032561f315","target_id":"CLM-025"} -->
##### Principles

| Principle | Guidance | Source |
|---|---|---|
| Generic before target-specific | Keep the workflow around `schemas/handoff_package.schema.json`, `schemas/target_mapping.schema.json`, and the generic exporter before adding target-specific parsers or profiles. | `_CONTEXT.md#Context Envelope`; `SOFTWARE_DECOMP.md#SOW-074`; OI-015 |
| Explicit missingness | Missing mapping support, unresolved assumptions, warnings, and unsupported target behavior should be visible in the export output. | SOW-074; `docs/CONTRACT.md` OPS-K-DATA-2 |
| Unit-aware export | Unit metadata must cross the export boundary unless a field is explicitly dimensionless or otherwise classified. | `docs/SPEC.md#Unit system and dimensional analysis`; OPS-K-UNIT-1 |
| Provenance and hash discipline | Exported packages should preserve references, provenance, rule/library refs, diagnostics, and hashes without treating them as professional acceptance. | `docs/TYPES.md` Assumption, TraceabilityLink, Diagnostic, Checksum, ResultExportEnvelope |
| Professional boundary | The workflow may support professional review; it must not claim approval, certification, sealing, authentication, or code compliance. | OBJ-017; DEC-015; OPS-K-AUTH-1 |
| Protected-content boundary | Fixtures must be invented or cleared; do not import protected standards examples or commercial tool files. | `docs/IP_AND_DATA_BOUNDARY.md`; OPS-K-IP-1 through OPS-K-IP-3 |

<!-- sow-source-end -->

### CLM-026 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":25,"line_start":18,"source_sha256":"0d2618f3dcd836bbf981e65d8036971a585e044157194e7882fe60032561f315","target_id":"CLM-026"} -->
##### Considerations

- The local `Dependencies.csv` records upstream architecture-basis and interop/security/model-contract inputs as ACTIVE DAG-002 mirror evidence. Treat those rows as coordination evidence, not as permission to copy sibling deliverable prose or implementation details into this folder.
- Upstream contracts named by the mirror include the canonical handoff package schema, target mapping and unsupported-behavior contract, import/export adapter framework, local FEA handoff data contract, private-data redaction/export controls, physical-to-analytical transformation contract, and comparison export contracts.
- The workflow should report unsupported-target behavior rather than silently approximating it. Provider-neutral unsupported behavior and target mapping records are now supplied by `schemas/target_mapping.schema.json`; target-specific extensions remain gated by DEL-17-01 and DEL-17-02.
- The current fixture is `fixtures/invented_target_fixture.json`; it is invented public metadata used by `tests/test_handoff_export_workflow.py` to exercise schema shape, warnings, assumptions, provenance, and unsupported-target flags without resembling commercial-tool examples.
- The generic exporter entry point is `core/handoff/exporter/workflow.py`. Package container structure, concrete mappings, target field coverage, and target-specific implementation remain gated.

<!-- sow-source-end -->

### CLM-027 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":34,"line_start":26,"source_sha256":"0d2618f3dcd836bbf981e65d8036971a585e044157194e7882fe60032561f315","target_id":"CLM-027"} -->
##### Trade-offs

| Trade-off | Conservative direction |
|---|---|
| Generic exporter vs. target-specific parser | Prefer a generic exporter with explicit unsupported-target flags; defer target-specific parsing behavior. |
| Strict schema validation vs. permissive export | Prefer schema validation and explicit findings over silent coercion. |
| Helpful external metadata vs. professional status | Preserve references, notes, hashes, and diagnostics, but avoid approval/certification/status claims. |
| Realistic fixture vs. protected/commercial data risk | Prefer invented fixture data with clear provenance. |

<!-- sow-source-end -->

### CLM-028 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":40,"line_start":35,"source_sha256":"0d2618f3dcd836bbf981e65d8036971a585e044157194e7882fe60032561f315","target_id":"CLM-028"} -->
##### Examples

The current example fixture is `fixtures/invented_target_fixture.json`. It is invented public metadata only and is checked by `tests/test_handoff_export_workflow.py` alongside schema validation for `schemas/handoff_package.schema.json` and `schemas/target_mapping.schema.json`.

Do not derive future example values from protected standards, commercial software files, proprietary catalogs, owner standards, or private project data.

<!-- sow-source-end -->

### CLM-029 — Open Questions and TBDs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":49,"line_start":41,"source_sha256":"0d2618f3dcd836bbf981e65d8036971a585e044157194e7882fe60032561f315","target_id":"CLM-029"} -->
##### Open Questions and TBDs

| ID | Item | Source |
|---|---|---|
| DEL-15-03-TBD-001 | Canonical package container, concrete mappings, target field coverage, and target-specific implementation. | `SOFTWARE_DECOMP.md` OI-015; DEL-17-01; DEL-17-02 |
| DEL-15-03-TBD-002 | Target-specific parser/profile behavior and commercial-tool result ingestion remain out of this deliverable. | `_CONTEXT.md#Context Envelope`; OI-015 |
| DEL-15-03-TBD-003 | Package-specific dependency versions and broader architecture implementation choices remain governed by architecture-basis TBDs. | `_CONTEXT.md#Architecture Basis Injection` |
| DEL-15-03-TBD-004 | Future fixtures for target-specific profiles require protected-content and provenance review. | `docs/IP_AND_DATA_BOUNDARY.md`; DEL-17-01; DEL-17-02 |

<!-- sow-source-end -->

### CLM-030 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":52,"line_start":50,"source_sha256":"0d2618f3dcd836bbf981e65d8036971a585e044157194e7882fe60032561f315","target_id":"CLM-030"} -->
##### Conflict Table (for human ruling)

No source conflicts were identified during the setup pass. TBDs above are missing-detail boundaries, not resolved conflicts.
<!-- sow-source-end -->

### CLM-031 — D-41 R5 T2A checksum-boundary guidance (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":55,"line_start":53,"source_sha256":"0d2618f3dcd836bbf981e65d8036971a585e044157194e7882fe60032561f315","target_id":"CLM-031"} -->
##### D-41 R5 T2A checksum-boundary guidance (2026-07-12)

Treat incoming checksum records as carried evidence. Do not describe them as JCS unless the owning producer supplies governed RFC 8785 conformance evidence; preserve the precise producer label and surface validation elsewhere.
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-074 OBJ-017 | CLM-009 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
