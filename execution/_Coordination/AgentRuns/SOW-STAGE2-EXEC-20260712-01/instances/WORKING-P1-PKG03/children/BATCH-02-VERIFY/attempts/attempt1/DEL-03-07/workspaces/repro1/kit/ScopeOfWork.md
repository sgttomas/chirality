---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-03-07
package_id: PKG-03
decomposition_basis: projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@69ac259a7113d5a838fb22aa2e84df0e0f109713
project_scope_refs: [SOW-019,  SOW-044]
package_objective_refs: [OBJ-002,  OBJ-004]
---

# Scope of Work — DEL-03-07

## Purpose and Objective Traceability

This migration candidate defines `DEL-03-07` in service of project scope [SOW-019,  SOW-044] and package objectives [OBJ-002,  OBJ-004].

- **OUT-001** — A public/private library import-provenance checker contract covering source, license, redistribution, contributor and review metadata, privacy posture, unit preservation, quarantine, and diagnostics is produced for the declared scope and objectives.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-03-07 Public/private library import provenance checker

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":2,"line_start":1,"source_sha256":"850f207d5da0658759e2fde85b4b264e07d0d99ab390b1960ffc14f834b0ed6c","target_id":"CLM-001"} -->
#### Datasheet: DEL-03-07 Public/private library import provenance checker

<!-- sow-source-end -->

### CLM-002 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":16,"line_start":3,"source_sha256":"850f207d5da0658759e2fde85b4b264e07d0d99ab390b1960ffc14f834b0ed6c","target_id":"CLM-002"} -->
##### Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-03-07 |
| Package ID | PKG-03 |
| Package Name | Piping Components, Materials, and Library Data Model |
| Deliverable Type | BACKEND_FEATURE_SLICE |
| Scope Items | SOW-019; SOW-044 |
| Objectives | OBJ-002; OBJ-004 |
| Anticipated Artifacts | library import validator; provenance tests |
| Decomposition Basis | execution/_Decomposition/SOFTWARE_DECOMP.md revision 0.7 |
| Status | Implementation evidence reconciled; lifecycle remains governed by `_STATUS.md` |

<!-- sow-source-end -->

### CLM-003 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":27,"line_start":17,"source_sha256":"850f207d5da0658759e2fde85b4b264e07d0d99ab390b1960ffc14f834b0ed6c","target_id":"CLM-003"} -->
##### Attributes

| Attribute | Source-grounded value |
|---|---|
| Primary function | Validate already-parsed material, section, and component library payloads so source, provenance, license, contributor/reviewer disposition, redistribution metadata, privacy posture, and unit metadata are checked before import acceptance. |
| Data boundary | Public component data requires documented provenance and redistribution rights; private library data must not become a bundled public default. |
| Input format list | TBD. The implemented checker validates already-parsed payloads and intentionally does not parse external import formats. |
| Rights determination authority | TBD. The checker can record and flag metadata, but legal acceptance requires human/project review. |
| Protected-content response | Suspected protected standards or vendor content is quarantined and escalated rather than transformed into public data. |
| Unit handling | Imported component/material numeric values must retain unit and dimension metadata; no unit defaults are introduced by the checker. |

<!-- sow-source-end -->

### CLM-004 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":34,"line_start":28,"source_sha256":"850f207d5da0658759e2fde85b4b264e07d0d99ab390b1960ffc14f834b0ed6c","target_id":"CLM-004"} -->
##### Conditions

- Public data contributions are acceptable only when provenance and redistribution status are documented.
- Import mechanisms must record source, provenance, and license metadata for component and material data.
- Missing solve-required or rule-check-required values are findings, not silent defaults.
- Public deliverable evidence must not include protected standards text, protected tables, vendor data, or real rights/provenance examples.

<!-- sow-source-end -->

### CLM-005 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":50,"line_start":35,"source_sha256":"850f207d5da0658759e2fde85b4b264e07d0d99ab390b1960ffc14f834b0ed6c","target_id":"CLM-005"} -->
##### Construction

Reconciled implementation evidence contains:

- `core/library_import/provenance_checker.py`, a stdlib-only validator for already-parsed material, section, and component library payloads;
- `validate_library_import(...)`, returning `ACCEPTED_PUBLIC`, `PRIVATE_LOCAL_ONLY`, `REVIEW_REQUIRED`, `REJECTED`, or `QUARANTINE` outcomes;
- metadata checks for library-level and record-level provenance fields: source name/location, source license, contributor, contributor certification, redistribution status, and review status;
- public/private disposition checks that block private-only or unresolved-rights data from public acceptance while permitting eligible private imports to remain local/private;
- protected-content quarantine signaling for suspected protected or rejected sources;
- nested numeric value checks that require unit/dimension metadata and value-level provenance;
- `ImportFinding.to_diagnostic()` and `ImportValidationResult.diagnostics`, which project findings into a PKG-02-style diagnostic envelope with code, severity, class, source, affected object, remediation, and provenance;
- `core/library_import/README.md`, documenting the boundary that the checker does not parse external formats and does not make legal conclusions;
- `tests/test_library_import_provenance.py`, covering accepted public imports, public rejection for unresolved rights, private-local handling, missing provenance, protected-content quarantine, unit metadata, and diagnostic-envelope mapping using invented fixtures.

Remaining unresolved items are concrete external import formats and parser contracts, accepted source catalogs and legal/license policy, fixture-value authority for engineering reliance, dependency satisfaction outside this bounded evidence, human disposition of review findings, and lifecycle closure.

<!-- sow-source-end -->

### CLM-006 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":59,"line_start":51,"source_sha256":"850f207d5da0658759e2fde85b4b264e07d0d99ab390b1960ffc14f834b0ed6c","target_id":"CLM-006"} -->
##### References

- `_CONTEXT.md` for deliverable identity, scope envelope, objectives, and architecture-basis injection.
- `_REFERENCES.md` for governing source pointers.
- `docs/_Registers/Deliverables.csv` row DEL-03-07.
- `docs/_Registers/ScopeLedger.csv` rows SOW-019 and SOW-044.
- `docs/_Registers/ContextBudgetQA.csv` row DEL-03-07.
- `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.7.
- `docs/CONTRACT.md` invariants OPS-K-IP-1..3, OPS-K-DATA-1..3, OPS-K-UNIT-1, OPS-K-PRIV-1, OPS-K-GOV-4, and OPS-K-AGENT-1..4.
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-007 — Specification: DEL-03-07 Public/private library import provenance checker

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":2,"line_start":1,"source_sha256":"97b044e14ccecf62fc9df620a79ca748571e1918260e558178d60bb7e3c73b64","target_id":"CLM-007"} -->
#### Specification: DEL-03-07 Public/private library import provenance checker

<!-- sow-source-end -->

### CLM-008 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":21,"line_start":3,"source_sha256":"97b044e14ccecf62fc9df620a79ca748571e1918260e558178d60bb7e3c73b64","target_id":"CLM-008"} -->
##### Scope

This deliverable specifies reconciled evidence for a backend feature slice that validates already-parsed public/private component, section, and material library payloads for provenance, license, redistribution status, privacy posture, unit metadata, and protected-content handling.

It covers:

- metadata presence checks for source, provenance, license, contributor/reviewer disposition, and redistribution status;
- public/private data boundary checks for component, section, and material library imports;
- diagnostics for missing provenance, unresolved redistribution metadata, protected-content suspicion, missing unit metadata, and review-required public imports;
- PKG-02-style diagnostic-envelope projection for import findings;
- provenance-focused tests using invented fixture payloads.

It excludes:

- concrete external import formats and parsers, which are TBD;
- legal conclusions about whether a license grants redistribution rights;
- protected standards text, copied tables, vendor data, or derived protected examples;
- global solver, rule evaluator, or GUI implementation work.

<!-- sow-source-end -->

### CLM-009 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":33,"line_start":22,"source_sha256":"97b044e14ccecf62fc9df620a79ca748571e1918260e558178d60bb7e3c73b64","target_id":"CLM-009"} -->
##### Requirements

| ID | Requirement | Evidence basis | Verification |
|---|---|---|---|
| DEL-03-07-R1 | The checker shall require recorded source, provenance, license, contributor certification, review status, and redistribution-status metadata before a public component/material data import can be accepted. | SOW-019; SOW-044; OPS-K-IP-2; OPS-K-DATA-3 | `test_public_component_import_requires_accepted_public_provenance` and missing-provenance tests cover present/missing metadata fields. |
| DEL-03-07-R2 | The checker shall flag or reject imports with missing provenance or missing redistribution-status metadata without creating silent defaults. | SOW-044; OPS-K-DATA-2; OPS-K-AGENT-1 | Negative tests assert diagnostic output, rejected outcome, and no accepted record. |
| DEL-03-07-R3 | The checker shall separate public and private library handling so private project, material, component, and rule-pack data is not transmitted or committed publicly by default. | OPS-K-PRIV-1; OPS-K-DATA-1 | Tests distinguish public-import disposition from private-local records. |
| DEL-03-07-R4 | The checker shall quarantine or escalate suspected protected content rather than paraphrasing, transforming, or accepting it into public data. | OPS-K-IP-1; OPS-K-IP-3; OPS-K-GOV-4 | Tests use invented markers only and assert quarantine outcome. |
| DEL-03-07-R5 | The checker shall preserve unit metadata for imported numeric component/material values where such values are present. | OPS-K-UNIT-1; AB-00-04; AB-00-07 | Unit-aware fixture tests use invented values and verify missing unit metadata blocks public acceptance. |
| DEL-03-07-R6 | The checker shall produce diagnostics/result envelopes compatible with the schema-first command/query/job boundary. | AB-00-02; AB-00-06; AB-00-07 | `test_import_findings_map_to_pkg02_diagnostic_envelope` asserts stable diagnostic fields and no bypass around import validation. |
| DEL-03-07-R7 | The checker shall not make legal acceptance claims; unresolved license or rights questions shall remain review dispositions requiring human/project authority. | OPS-K-AGENT-1; OPS-K-GOV-4 | Tests assert `TBD`/review-needed style statuses for unresolved rights metadata. |

<!-- sow-source-end -->

### CLM-010 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":42,"line_start":34,"source_sha256":"97b044e14ccecf62fc9df620a79ca748571e1918260e558178d60bb7e3c73b64","target_id":"CLM-010"} -->
##### Standards

| Standard or governing source | Applicability | Status |
|---|---|---|
| docs/CONTRACT.md | Invariant source for IP, data, unit, privacy, governance, and agent behavior. | Locally accessible |
| execution/_Decomposition/SOFTWARE_DECOMP.md revision 0.7 | Scope and objective source for DEL-03-07. | Locally accessible |
| External import format specifications | Potential parser/import constraints once selected. | TBD |
| Legal license interpretation sources | May govern redistribution-right acceptance. | TBD; human/legal review required |

<!-- sow-source-end -->

### CLM-011 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":51,"line_start":43,"source_sha256":"97b044e14ccecf62fc9df620a79ca748571e1918260e558178d60bb7e3c73b64","target_id":"CLM-011"} -->
##### Verification

- Run `python3 -m pytest tests/test_library_import_provenance.py` for accepted, private-local, rejected, quarantine, and diagnostic-envelope outcomes.
- Use only invented, minimal fixtures for public tests.
- Confirm accepted public imports contain source, provenance, license, redistribution status, contributor/review disposition, and unit metadata where applicable.
- Confirm missing or uncertain rights/provenance fields yield explicit diagnostics rather than accepted defaults.
- Confirm suspected protected content yields quarantine/escalation status and no public data output.
- Confirm diagnostics do not include protected content excerpts.

<!-- sow-source-end -->

### CLM-012 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":61,"line_start":52,"source_sha256":"97b044e14ccecf62fc9df620a79ca748571e1918260e558178d60bb7e3c73b64","target_id":"CLM-012"} -->
##### Documentation

Implemented and reconciled artifacts are:

- `core/library_import/provenance_checker.py`;
- `core/library_import/README.md`;
- `tests/test_library_import_provenance.py`;
- active deliverable docs recording implementation evidence and remaining TBDs.

Remaining non-implementation decisions are external import formats, public-source/catalog policy, fixture-value authority for engineering reliance, dependency satisfaction outside this bounded evidence, human disposition of local review findings, and lifecycle closure.
<!-- sow-source-end -->

- **AC-001** — The contract preserves accepted public/private data boundaries, conservative missing-provenance handling, protected-content quarantine, unit and diagnostic requirements, and unresolved rights, vocabulary, source-catalog, and legal-acceptance decisions without creating legal conclusions or public defaults.

## Production and Verification Method — Praxeology

### CLM-013 — Procedure: DEL-03-07 Public/private library import provenance checker

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":2,"line_start":1,"source_sha256":"383aa7595b53e1fa604ab02ab4d2e2cda2e6c1f57f69a6f0e8d35967b01b8ecf","target_id":"CLM-013"} -->
#### Procedure: DEL-03-07 Public/private library import provenance checker

<!-- sow-source-end -->

### CLM-014 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":6,"line_start":3,"source_sha256":"383aa7595b53e1fa604ab02ab4d2e2cda2e6c1f57f69a6f0e8d35967b01b8ecf","target_id":"CLM-014"} -->
##### Purpose

Define the procedure for checking and maintaining the implemented library import provenance checker while preserving unresolved policy, parser, review, and lifecycle boundaries.

<!-- sow-source-end -->

### CLM-015 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":14,"line_start":7,"source_sha256":"383aa7595b53e1fa604ab02ab4d2e2cda2e6c1f57f69a6f0e8d35967b01b8ecf","target_id":"CLM-015"} -->
##### Prerequisites

- Sealed context for DEL-03-07.
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.7.
- Applicable invariants from `docs/CONTRACT.md`.
- Implementation evidence in `core/library_import/provenance_checker.py`, `core/library_import/README.md`, and `tests/test_library_import_provenance.py`.
- Human-approved decisions for license/redistribution acceptance vocabulary, public source catalogs, and import parser contracts before those fields are treated as project policy.

<!-- sow-source-end -->

### CLM-016 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":26,"line_start":15,"source_sha256":"383aa7595b53e1fa604ab02ab4d2e2cda2e6c1f57f69a6f0e8d35967b01b8ecf","target_id":"CLM-016"} -->
##### Steps

1. Confirm the import record type being checked is within material, section, or component library scope.
2. Confirm the record carries source, provenance, license, redistribution-status, contributor, and review-disposition metadata fields or emits an explicit missing-field diagnostic.
3. Confirm public imports with missing provenance or missing redistribution status are blocked, rejected, or marked not publicly acceptable.
4. Confirm private imports remain marked private/local and do not become public bundled data by default.
5. Confirm suspected protected content produces a quarantine/escalation diagnostic without copying or paraphrasing protected content into public data.
6. Confirm numeric imported values preserve unit metadata where numeric component/material values are present.
7. Confirm result diagnostics fit the schema-first command/query/job result-envelope pattern and expose unresolved items as `TBD` or review-needed statuses.
8. Confirm provenance tests use invented fixtures only and do not establish engineering reliance for fixture values.
9. Confirm review findings remain technically addressed pending human disposition unless an authorized human review updates them.

<!-- sow-source-end -->

### CLM-017 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":38,"line_start":27,"source_sha256":"383aa7595b53e1fa604ab02ab4d2e2cda2e6c1f57f69a6f0e8d35967b01b8ecf","target_id":"CLM-017"} -->
##### Verification

| Check | Expected evidence |
|---|---|
| Metadata completeness | Tests for accepted records and missing-field diagnostics. |
| Public/private boundary | Tests that private records remain private and public records require provenance metadata. |
| Protected-content response | Tests assert quarantine/escalation status using invented markers only. |
| Unit handling | Tests assert unit fields are preserved for invented numeric values. |
| No legal conclusions | Tests assert unresolved rights questions remain review-needed/TBD. |
| No protected examples | Fixture review confirms no standards tables, vendor data, or real protected examples are included. |
| Review disposition boundary | Local review findings remain pending human disposition; no CSV status promotion is made by this procedure. |

<!-- sow-source-end -->

### CLM-018 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":46,"line_start":39,"source_sha256":"383aa7595b53e1fa604ab02ab4d2e2cda2e6c1f57f69a6f0e8d35967b01b8ecf","target_id":"CLM-018"} -->
##### Records

- `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md`.
- `core/library_import/provenance_checker.py`, `core/library_import/README.md`, and `tests/test_library_import_provenance.py` as implementation evidence.
- `_SEMANTIC.md` semantic matrix lens.
- `_SEMANTIC_LENSING.md` lensing register.
- `Dependencies.csv` v3.1 and `_DEPENDENCIES.md`.
- `_run_records/TASK_RUN_*.md` records for the deliverable work sequence.
<!-- sow-source-end -->

- **VER-001** — Validate the contract and review source parity, metadata and diagnostic coverage, public/private separation, unit preservation, protected-content quarantine, invented-fixture boundaries, and unresolved human or legal review items.

## Governing Values and Decisions — Axiology

### CLM-019 — Guidance: DEL-03-07 Public/private library import provenance checker

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":2,"line_start":1,"source_sha256":"99e5ce49ab32d14dbb53295658175981f6d453e3e65a0a582f5e884b322a96e2","target_id":"CLM-019"} -->
#### Guidance: DEL-03-07 Public/private library import provenance checker

<!-- sow-source-end -->

### CLM-020 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":6,"line_start":3,"source_sha256":"99e5ce49ab32d14dbb53295658175981f6d453e3e65a0a582f5e884b322a96e2","target_id":"CLM-020"} -->
##### Purpose

This deliverable exists to connect PKG-03 library data models with the project governance boundary: component and material data may be imported, but public acceptance requires recorded provenance and redistribution status, and private data must remain private by default.

<!-- sow-source-end -->

### CLM-021 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":15,"line_start":7,"source_sha256":"99e5ce49ab32d14dbb53295658175981f6d453e3e65a0a582f5e884b322a96e2","target_id":"CLM-021"} -->
##### Principles

- Treat provenance as required metadata, not optional commentary.
- Treat redistribution status as a review field. The checker records and gates; it does not make legal conclusions.
- Prefer explicit `TBD`, `REVIEW_NEEDED`, or equivalent unresolved states over guessed acceptance.
- Keep public tests and fixtures invented. Do not use protected standards tables, vendor catalogs, or copied examples.
- Preserve public/private separation at the import boundary and at any diagnostic/export boundary.
- Maintain unit metadata for numeric engineering values; do not introduce unitless accepted records.

<!-- sow-source-end -->

### CLM-022 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":23,"line_start":16,"source_sha256":"99e5ce49ab32d14dbb53295658175981f6d453e3e65a0a582f5e884b322a96e2","target_id":"CLM-022"} -->
##### Considerations

- SOW-019 requires documented provenance and redistribution rights before public component data can be accepted.
- SOW-044 requires import mechanisms to record source, provenance, and license metadata for component/material data.
- OPS-K-IP-3 and OPS-K-GOV-4 make protected-content suspicion a stop-and-escalate condition, not a transformation task.
- AB-00-07 indicates adapters must validate units, provenance, redistribution, diagnostics, and public/private boundaries.
- Exact external import formats are still TBD, so this deliverable evidence describes already-parsed payload validation without committing to parser details.

<!-- sow-source-end -->

### CLM-023 — Current Evidence

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":30,"line_start":24,"source_sha256":"99e5ce49ab32d14dbb53295658175981f6d453e3e65a0a582f5e884b322a96e2","target_id":"CLM-023"} -->
##### Current Evidence

- `core/library_import/provenance_checker.py` provides `validate_library_import(...)` for already-parsed material, section, and component library payloads.
- `ImportValidationResult` reports `ACCEPTED_PUBLIC`, `PRIVATE_LOCAL_ONLY`, `REVIEW_REQUIRED`, `REJECTED`, or `QUARANTINE`.
- `ImportFinding.to_diagnostic()` projects findings to PKG-02-style diagnostic envelope fields for downstream compatibility evidence.
- `tests/test_library_import_provenance.py` uses invented fixtures to cover public acceptance, unresolved-rights rejection, private-local handling, missing provenance, protected-content quarantine, unit metadata, and diagnostic-envelope mapping.

<!-- sow-source-end -->

### CLM-024 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":40,"line_start":31,"source_sha256":"99e5ce49ab32d14dbb53295658175981f6d453e3e65a0a582f5e884b322a96e2","target_id":"CLM-024"} -->
##### Trade-offs

| Topic | Preferred posture | Reason |
|---|---|---|
| Missing provenance | Reject, block, or flag as not publicly acceptable. | Avoid silent acceptance of unsupported public data. |
| Unclear license status | Mark review-needed/TBD. | The checker cannot make legal conclusions. |
| Private imports | Permit local-private handling only when privacy markers and storage boundaries are respected. | Supports private libraries without bundling protected data. |
| Public test data | Use invented fixtures. | Prevent protected data from entering the public repository. |
| Strictness | Conservative by default. | Scope item notes emphasize contributor certification and missing-provenance flags. |

<!-- sow-source-end -->

### CLM-025 — Examples And Fixtures

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":44,"line_start":41,"source_sha256":"99e5ce49ab32d14dbb53295658175981f6d453e3e65a0a582f5e884b322a96e2","target_id":"CLM-025"} -->
##### Examples And Fixtures

Concrete external import examples are not provided because protected/vendor data examples are forbidden and external import formats are TBD. Current test payloads are invented fixtures only; fixture values are not engineering reference values and do not establish a real license, provenance trail, accepted source catalog, or redistribution policy.

<!-- sow-source-end -->

### CLM-026 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":52,"line_start":45,"source_sha256":"99e5ce49ab32d14dbb53295658175981f6d453e3e65a0a582f5e884b322a96e2","target_id":"CLM-026"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Topic | Contenders | Human ruling |
|---|---|---|---|
| DEL-03-07-C1 | Exact license/redistribution disposition vocabulary | Source scope requires metadata and review, but no approved enum names are defined in this deliverable. | TBD |
| DEL-03-07-C2 | Public acceptance authority | Validator can flag missing/uncertain metadata; legal or maintainer acceptance authority is not defined locally. | TBD |
| DEL-03-07-C3 | Public source catalog and policy | The checker gates on metadata values, but no approved public source catalog or legal/license policy is defined locally. | TBD |
| DEL-03-07-C4 | Fixture-value authority | Tests use invented minimal values; no fixture value is approved for engineering reliance. | TBD |
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-019  SOW-044 OBJ-002  OBJ-004 | CLM-007 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
