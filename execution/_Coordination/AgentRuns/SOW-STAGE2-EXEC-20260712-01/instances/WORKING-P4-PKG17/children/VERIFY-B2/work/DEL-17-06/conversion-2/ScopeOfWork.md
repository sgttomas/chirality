---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-17-06
package_id: PKG-17
decomposition_basis: projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@e8f59a63372f38d9e788ac39b39995558f5aba73
project_scope_refs: [SOW-046, SOW-074]
package_objective_refs: [OBJ-007, OBJ-017, OBJ-018]
---

# Scope of Work — DEL-17-06

## Purpose and Objective Traceability

This migration candidate defines `DEL-17-06` in service of project scope [SOW-046, SOW-074] and package objectives [OBJ-007, OBJ-017, OBJ-018].

- **OUT-001** — A project-controlled stress-neutral CSV/JSON package contract for review, regression comparison, debugging, and governed downstream tooling is produced.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-17-06 Stress-neutral CSV/JSON package

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":3,"line_start":1,"source_sha256":"ba9055b8f214b35c86d861c939168d96acc084d59374d1d6cbd2ca9b31c2333a","target_id":"CLM-001"} -->
#### Datasheet: DEL-17-06 Stress-neutral CSV/JSON package

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-002 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":11,"line_start":4,"source_sha256":"ba9055b8f214b35c86d861c939168d96acc084d59374d1d6cbd2ca9b31c2333a","target_id":"CLM-002"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-17-06-DECL-002`.

<!-- sow-source-end -->

### CLM-003 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":23,"line_start":12,"source_sha256":"ba9055b8f214b35c86d861c939168d96acc084d59374d1d6cbd2ca9b31c2333a","target_id":"CLM-003"} -->
##### Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-17-06 |
| Package | PKG-17 Export Format Interoperability |
| Name | Stress-neutral CSV/JSON package |
| Type | BACKEND_FEATURE_SLICE |
| Scope Items | SOW-046, SOW-074 |
| Objectives | OBJ-007, OBJ-017, OBJ-018 |
| Runtime pass | Phase A four-document P1/P2 only |

<!-- sow-source-end -->

### CLM-004 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":33,"line_start":24,"source_sha256":"ba9055b8f214b35c86d861c939168d96acc084d59374d1d6cbd2ca9b31c2333a","target_id":"CLM-004"} -->
##### Attributes

| Attribute | Current value | Source |
|---|---|---|
| Package purpose | Project-controlled stress-oriented neutral package for review, debugging, community adapter development, and comparison across target exporters. It is not a vendor format and not a replacement for a commercial solver input deck. | `plans/EXPORT_FORMAT_INTEROPERABILITY_PLAN.md` section "Stress Neutral CSV/JSON Package" |
| Formats | CSV for inspection/spreadsheet review and JSON for structured import/export. | `plans/EXPORT_FORMAT_INTEROPERABILITY_PLAN.md` section "Stress Neutral CSV/JSON Package" |
| Required relationship to result exports | Result exports are for review, regression comparison, report consumption, headless automation, and governed downstream tooling; they preserve units, diagnostics, provenance, hashes, and professional-boundary limits. | `docs/SPEC.md` result export section; `docs/TYPES.md` `ResultExportEnvelope` |
| Required relationship to DEL-17-02 | Use loss reports and stable IDs for stress-neutral CSV/JSON result packages. | `DEL-17-02/Specification.md` "Downstream Requirements" |
| Required relationship to DEL-17-01 | Do not use CAEPIPE CSV/text behavior as professional acceptance; target-specific CSV coverage remains `TBD` unless source-confirmed. | `DEL-17-01/Specification.md` boundary and downstream rules |

<!-- sow-source-end -->

### CLM-005 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":47,"line_start":34,"source_sha256":"ba9055b8f214b35c86d861c939168d96acc084d59374d1d6cbd2ca9b31c2333a","target_id":"CLM-005"} -->
##### Conditions

| Condition | Status |
|---|---|
| Source model reference | Required by result-export and handoff scope; exact source model identifier, version, and package reference path are `TBD`. |
| Source model hash basis | Required where the package or manifest records deterministic source evidence; exact payload scope and hash field are `TBD`. |
| Analysis-run reference | Required when exported values come from an analysis run; exact analysis-run identifier, solver version reference, load-case or combination basis, and package reference path are `TBD`. |
| Package member path references | Required by the common export package contract; exact CSV, JSON, manifest, ID-map, loss-report, and validation-report paths are `TBD`. |
| Unit and dimensional metadata | Required for exported result values; exact CSV column names and JSON property names are `TBD`. |
| Stable ID preservation | Required through direct fields or sidecar mapping; exact stress-neutral ID-map layout is `TBD`. |
| Diagnostics and boundary notes | Required so review consumers can see limitations, unresolved assumptions, warnings, and non-authoritative status. |
| Protected/private content handling | Public fixtures and examples must not include protected standards data, proprietary examples, private project data, code allowables, SIF/flexibility tables, or owner criteria. |
| Professional boundary | The package is evidence for review/regression/downstream tooling only; it must not declare code compliance, certification, sealing, professional approval, formal validation, or engineering acceptance. |

<!-- sow-source-end -->

### CLM-006 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":63,"line_start":48,"source_sha256":"ba9055b8f214b35c86d861c939168d96acc084d59374d1d6cbd2ca9b31c2333a","target_id":"CLM-006"} -->
##### Construction

| Candidate package member | Required role | Current detail level |
|---|---|---|
| Node table | Reviewable node identity and coordinate/result-reference surface. | Table fields `TBD`. |
| Element table | Reviewable element identity and connectivity/result-reference surface. | Table fields `TBD`. |
| Component table | Reviewable component identity and relationship to elements/nodes. | Table fields `TBD`. |
| Restraint/support table | Reviewable support/restraint identity and mapping to model/result records. | Table fields `TBD`; nonlinear/support-state behavior remains source-dependent. |
| Equipment/nozzle table | Reviewable terminal/equipment interface identity and mapping surface. | Table fields `TBD`. |
| Material table | Reference identity/provenance surface only; no bundled proprietary or protected values. | Table fields `TBD`. |
| Section table | Reference identity/provenance surface only; no protected dimensional tables or catalog defaults. | Table fields `TBD`. |
| Load/design case table | Reviewable load/design case identity and basis. | Table fields `TBD`. |
| Units metadata | Declares unit system, dimensions, and conversion basis needed by CSV and JSON consumers. | Exact layout `TBD`. |
| ID map | Maps canonical OpenPipeStress IDs to package rows, JSON objects, or sidecars. | Exact layout `TBD`; consume DEL-17-02 rules. |
| Validation report | Records parse/shape checks, loss entries, warnings, and boundary notes. | Exact layout `TBD`; machine-readable and human-readable forms expected where applicable. |

<!-- sow-source-end -->

### CLM-007 — Future Detail Slots

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":76,"line_start":64,"source_sha256":"ba9055b8f214b35c86d861c939168d96acc084d59374d1d6cbd2ca9b31c2333a","target_id":"CLM-007"} -->
##### Future Detail Slots

These slots are placeholders for later schema, writer, fixture, and validation work. They are not populated by this Phase A/Pass 3 task.

| Slot | Future content | Current disposition | Source basis |
|---|---|---|---|
| CSV fields | Exact table names, column names, ordering, quoting/null rules, and per-table required/optional status. | `TBD` until schema work begins. | Stress-neutral package contents from `plans/EXPORT_FORMAT_INTEROPERABILITY_PLAN.md`; package-member inventory rules from `DEL-17-02/Specification.md`. |
| JSON properties | Exact object layout, property names, required/optional status, schema identifier, and validation profile. | `TBD` until JSON Schema 2020-12 contract work begins. | Architecture basis in `_CONTEXT.md`; `DEL-17-02/Specification.md` architecture-basis requirements. |
| Manifest layout | Package ID, source model/run basis, profile ID, member inventory, hashes where applicable, diagnostics, and boundary notes. | `TBD` layout; required concept retained. | `DEL-17-02/Specification.md` manifest requirements; `docs/SPEC.md` result export and audit-manifest sections. |
| ID-map layout | Canonical ID, package member path, row/object reference, target/generated identity where any exists, and omission/unsupported reason. | `TBD` layout; stable-ID role retained. | `DEL-17-02/Specification.md` stable ID map requirements; export plan stable identity rules. |
| Loss-report layout | Exported, omitted, approximated, delegated, unsupported, and `TBD` behavior with affected IDs and downstream implication. | `TBD` layout; loss report remains mandatory for native project-owned exports. | `DEL-17-02/Specification.md` loss report requirements. |
| Validation-report layout | Shape checks, synchronization checks, source-evidence checks, protected-content checks, diagnostics, and boundary findings. | `TBD`; future implementation evidence only. | `docs/SPEC.md` result export boundary; `docs/IP_AND_DATA_BOUNDARY.md` contribution and public-data policy. |

<!-- sow-source-end -->

### CLM-008 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":88,"line_start":77,"source_sha256":"ba9055b8f214b35c86d861c939168d96acc084d59374d1d6cbd2ca9b31c2333a","target_id":"CLM-008"} -->
##### References

| Source | Use |
|---|---|
| `plans/EXPORT_FORMAT_INTEROPERABILITY_PLAN.md` | Stress-neutral package purpose, recommended contents, CSV/JSON format split, export risk framing. |
| `execution/_Decomposition/SOFTWARE_DECOMP.md` | DEL-17-06 scope, SOW-046/SOW-074 assignment, PKG-17 exclusions, architecture-basis context. |
| `docs/SPEC.md` | Result export envelope boundary, required result-export metadata, `TBD` status for additional formats. |
| `docs/TYPES.md` | Result/export, stable identity, data-boundary, no-bypass, and professional-boundary vocabulary. |
| `docs/CONTRACT.md` | IP, data, unit, and professional-responsibility invariants. |
| `docs/IP_AND_DATA_BOUNDARY.md` | Public/private/protected data boundary and contribution constraints. |
| `DEL-17-01` four-document kit | Source-basis and target-claim boundaries for PKG-17. |
| `DEL-17-02` four-document kit | Common export package, profile, stable ID map, manifest, and loss-report contract consumed by DEL-17-06. |
<!-- sow-source-end -->

### CLM-009 — D-41 R5 T2A canonicalization evidence (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":91,"line_start":89,"source_sha256":"ba9055b8f214b35c86d861c939168d96acc084d59374d1d6cbd2ca9b31c2333a","target_id":"CLM-009"} -->
##### D-41 R5 T2A canonicalization evidence (2026-07-12)

JSON checksum records emitted by DEL-17-06 use `deterministic_sorted_compact_json_payload_hash`: UTF-8 Python JSON with lexicographically sorted keys, compact separators, and ASCII escaping. This is a deterministic local byte contract, not an RFC 8785/JCS claim. CSV members retain `normalized_ascii_lf_text`.
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-010 — Specification: DEL-17-06 Stress-neutral CSV/JSON package

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":3,"line_start":1,"source_sha256":"381e308ea208d3762ba5563c1a583f77c6eab4cd6992d736dabcf92e44624602","target_id":"CLM-010"} -->
#### Specification: DEL-17-06 Stress-neutral CSV/JSON package

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-011 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":11,"line_start":4,"source_sha256":"381e308ea208d3762ba5563c1a583f77c6eab4cd6992d736dabcf92e44624602","target_id":"CLM-011"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-17-06-DECL-001`.

<!-- sow-source-end -->

### CLM-012 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":19,"line_start":12,"source_sha256":"381e308ea208d3762ba5563c1a583f77c6eab4cd6992d736dabcf92e44624602","target_id":"CLM-012"} -->
##### Scope

DEL-17-06 shall define the documentation-level requirements for a project-controlled stress-neutral CSV/JSON package used for review, regression comparison, and downstream tooling.

This Phase A deliverable is a four-document kit only. It shall not implement code, create or edit JSON schemas, create CSV fixtures, write exporters, define release compatibility, or claim professional/code-compliance acceptance.

The stress-neutral package shall remain result/package evidence. It is not a vendor solver format, not a commercial solver input deck, not a CAEPIPE compatibility claim, and not a substitute for human professional review.

<!-- sow-source-end -->

### CLM-013 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":35,"line_start":20,"source_sha256":"381e308ea208d3762ba5563c1a583f77c6eab4cd6992d736dabcf92e44624602","target_id":"CLM-013"} -->
##### Requirements

| Req ID | Requirement | Source basis |
|---|---|---|
| DEL-17-06-REQ-001 | The package shall support review, debugging, community adapter development, and comparison across target exporters without presenting itself as a vendor format. | `plans/EXPORT_FORMAT_INTEROPERABILITY_PLAN.md` "Stress Neutral CSV/JSON Package" |
| DEL-17-06-REQ-002 | The package shall provide CSV output for inspection/spreadsheet review and JSON output for structured import/export. | `plans/EXPORT_FORMAT_INTEROPERABILITY_PLAN.md` "Stress Neutral CSV/JSON Package" |
| DEL-17-06-REQ-003 | The package shall preserve canonical OpenPipeStress identity through direct row/object fields or sidecar ID-map records. Exact field names are `TBD`. | `DEL-17-02/Specification.md` stable ID map requirements |
| DEL-17-06-REQ-004 | The package shall include or reference a manifest that records source model/run basis, package member inventory, hashes where applicable, diagnostics, and boundary notes. Exact manifest layout is `TBD`. | `DEL-17-02/Specification.md` manifest requirements; `docs/SPEC.md` result export section |
| DEL-17-06-REQ-005 | The package shall include a loss report even when export succeeds, with exported, omitted, approximated, delegated, unsupported, and `TBD` behavior visible. | `DEL-17-02/Specification.md` loss report requirements |
| DEL-17-06-REQ-006 | Result values shall carry explicit unit and dimensional metadata or produce blocking diagnostics. Exact CSV/JSON representation is `TBD`. | `docs/SPEC.md` result export section; `docs/CONTRACT.md` OPS-K-UNIT-1 |
| DEL-17-06-REQ-007 | The package shall carry diagnostics, warnings, unresolved assumptions, provenance, reproducibility references, and professional-boundary notices when those are present in the source result/export envelope. | `docs/SPEC.md` result export section; `docs/TYPES.md` `ResultExportEnvelope` |
| DEL-17-06-REQ-008 | The package shall not copy protected standards text, protected tables, proprietary formulas, code-specific allowables, SIF/flexibility values, private rule-pack payloads, private project data, or proprietary commercial examples into public artifacts. | `docs/CONTRACT.md`; `docs/IP_AND_DATA_BOUNDARY.md`; `docs/TYPES.md` |
| DEL-17-06-REQ-009 | The package shall not declare code compliance, certification, sealing, professional approval, formal validation, engineering acceptance, or release readiness. | `docs/CONTRACT.md` OPS-K-AUTH-1; `DEL-17-01/Specification.md`; `DEL-17-02/Specification.md` |
| DEL-17-06-REQ-010 | Target-specific or version-sensitive behavior not resolved by source evidence shall remain `TBD` and shall not be represented as supported behavior. | `DEL-17-01/Specification.md`; `DEL-17-02/Specification.md` |
| DEL-17-06-REQ-011 | The stress-neutral profile shall carry source-basis references for DEL-08-04, DEL-14-02, DEL-14-05, and DEL-17-02; missing references shall block package acceptance. | DAG-006 DEL-17-06 dependency edges; DEL-17-02 export contract; DEL-08-04 result export format; DEL-14-02 analysis run records; DEL-14-05 comparison export contracts. |

<!-- sow-source-end -->

### CLM-014 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":45,"line_start":36,"source_sha256":"381e308ea208d3762ba5563c1a583f77c6eab4cd6992d736dabcf92e44624602","target_id":"CLM-014"} -->
##### Standards

| Standard or contract | Applicability | Status |
|---|---|---|
| JSON Schema 2020-12 | Baseline for future public JSON schemas/interchange contracts. | Applicable architecture basis; no schema file is created in this Phase A task. |
| Declared deterministic JSON hash basis | JSON package members use sorted-key compact ASCII-escaped Python JSON labeled `deterministic_sorted_compact_json_payload_hash`; this is explicitly not JCS. CSV normalization is separately labeled. | D-41 R5 T2A; exact non-current payload partitioning remains `TBD`. |
| OpenPipeStress result export envelope | Governs result identity, model/run references, unit-aware values, diagnostics, provenance, reproducibility refs, statuses, rule-pack refs, and downstream-use declarations. | Source-grounded contract basis; additional CSV/JSON package layout remains `TBD`. |
| DEL-17-02 common export contract | Governs export package, profile, stable ID map, manifest, and loss-report behavior. | Required upstream contract for DEL-17-06. |
| IP and data-boundary policy | Governs public/private/protected data use and contribution review. | Required for fixtures, examples, reports, and exported artifacts. |

<!-- sow-source-end -->

### CLM-015 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":67,"line_start":46,"source_sha256":"381e308ea208d3762ba5563c1a583f77c6eab4cd6992d736dabcf92e44624602","target_id":"CLM-015"} -->
##### Verification

| Verification ID | Check | Acceptance evidence |
|---|---|---|
| DEL-17-06-VER-001 | Confirm all four documents exist and preserve required default sections. | `tools/validation/check_four_documents.sh` result. |
| DEL-17-06-VER-002 | Confirm the deliverable-local minimum fileset remains present. | `tools/validation/check_min_viable_fileset.sh` result. |
| DEL-17-06-VER-003 | Review the four documents for prohibited claims: code compliance, professional approval, formal validation, release compatibility, or engineering acceptance. | Manual text review or grep-based evidence in run record. |
| DEL-17-06-VER-004 | Review the four documents for protected/proprietary copied examples or protected standards data. | Manual text review or grep-based evidence in run record. |
| DEL-17-06-VER-005 | Confirm unresolved target behavior, exact table columns, JSON shape, manifest layout, tolerance thresholds, and comparison semantics remain `TBD`. | Four-document review. |

Future implementation verification, once schemas, writer outputs, fixtures, manifests, and comparison records exist:

| Verification ID | Check | Acceptance evidence |
|---|---|---|
| DEL-17-06-VER-006 | Map DEL-17-06-REQ-001 through DEL-17-06-REQ-010 to concrete schema, exporter, fixture, manifest, loss-report, and validation evidence. | Traceability table in a future implementation run record; unresolved entries remain `TBD` rather than accepted. |
| DEL-17-06-VER-007 | Confirm CSV and JSON representations are synchronized for canonical identity, units/dimensions, source model/run references, manifest basis, loss-report content, diagnostics, and boundary notices. | Future paired CSV/JSON fixture diff, manifest review, and validation-report result. |
| DEL-17-06-VER-008 | Confirm manifest or package-member hashes identify payload scope and use the declared sorted-compact JSON basis for JSON payloads; confirm the label makes no JCS claim and non-JSON partitioning remains explicit. | Exact-byte/fixed-hash, ordering, mutation, schema/fixture, and JSON/CSV label-split evidence. |
| DEL-17-06-VER-009 | Review generated schemas, CSV outputs, JSON outputs, manifests, loss reports, validation reports, and fixtures for prohibited claims and protected/private content. | Future protected-content and professional-boundary review evidence; suspected protected content quarantined per policy. |
| DEL-17-06-VER-010 | Confirm CSV/JSON examples or fixtures are invented or rights-cleared and demonstrate only shape, identity, units, diagnostics, loss reporting, and boundary notices. | Future contribution/provenance review evidence; examples without redistribution evidence remain absent or `TBD`. |
| DEL-17-06-VER-011 | Confirm any target-specific or version-sensitive support flag is backed by cited source evidence, or is marked `TBD` and blocked from support claims. | Future source-evidence review against DEL-17-01/DEL-17-02 and the applicable source-basis register. |
| DEL-17-06-VER-012 | Confirm comparison tolerance profiles, pass/fail language, and export comparison semantics are consumed from DEL-14-02/DEL-14-05 before comparison claims are made. | Future upstream dependency review; comparison semantics remain diagnostic/audit-only until sourced. |

<!-- sow-source-end -->

### CLM-016 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":86,"line_start":68,"source_sha256":"381e308ea208d3762ba5563c1a583f77c6eab4cd6992d736dabcf92e44624602","target_id":"CLM-016"} -->
##### Documentation

Required Phase A documentation artifacts:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` safe update from `OPEN` to `INITIALIZED` if permitted by the four-documents skill
- `_run_records/TASK_RUN_2026-05-18_1155.md`
- `_run_records/TASK_RUN_2026-05-18_1218.md` for Pass 3 disposition evidence

Future implementation artifacts listed in `_CONTEXT.md` remain not produced in this Phase A task:

- stress-neutral CSV schema
- stress-neutral JSON schema
- export writer
- comparison fixtures

<!-- sow-source-end -->

### CLM-017 — Conflict Table

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":91,"line_start":87,"source_sha256":"381e308ea208d3762ba5563c1a583f77c6eab4cd6992d736dabcf92e44624602","target_id":"CLM-017"} -->
##### Conflict Table

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| none | No source conflict identified in Phase A. Remaining details are unresolved `TBD` items, not source contradictions. | n/a | n/a | n/a | n/a | n/a |
<!-- sow-source-end -->

### CLM-018 — D-41 R5 T2A canonicalization requirement (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":94,"line_start":92,"source_sha256":"381e308ea208d3762ba5563c1a583f77c6eab4cd6992d736dabcf92e44624602","target_id":"CLM-018"} -->
##### D-41 R5 T2A canonicalization requirement (2026-07-12)

DEL-17-06 JSON hashes SHALL use `deterministic_sorted_compact_json_payload_hash` for the existing sorted-key compact ASCII-escaped Python JSON serializer. The label SHALL NOT be interpreted as RFC 8785/JCS conformance. Normalized CSV hashes SHALL remain separately labeled `normalized_ascii_lf_text`.
<!-- sow-source-end -->

- **AC-001** — The contract preserves synchronized CSV/JSON identity, units and dimensions, source model/run references, manifest, stable-ID map, loss report, diagnostics, provenance, declared sorted-compact JSON hashing, protected/private-data controls, explicit TBD behavior, and professional non-authority without claiming vendor compatibility or code compliance.

## Production and Verification Method — Praxeology

### CLM-019 — Procedure: DEL-17-06 Stress-neutral CSV/JSON package

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":3,"line_start":1,"source_sha256":"3cec21c032503ed8b83acaf652cf3cecdaa694f397c1878861aba0daa466a3e5","target_id":"CLM-019"} -->
#### Procedure: DEL-17-06 Stress-neutral CSV/JSON package

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-020 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":11,"line_start":4,"source_sha256":"3cec21c032503ed8b83acaf652cf3cecdaa694f397c1878861aba0daa466a3e5","target_id":"CLM-020"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-17-06-DECL-004`.

<!-- sow-source-end -->

### CLM-021 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":15,"line_start":12,"source_sha256":"3cec21c032503ed8b83acaf652cf3cecdaa694f397c1878861aba0daa466a3e5","target_id":"CLM-021"} -->
##### Purpose

This procedure describes how to produce and review the Phase A four-document kit for the stress-neutral CSV/JSON package, and how later implementation work should consume it without crossing into code, schema, release, compatibility, or professional-approval claims.

<!-- sow-source-end -->

### CLM-022 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":26,"line_start":16,"source_sha256":"3cec21c032503ed8b83acaf652cf3cecdaa694f397c1878861aba0daa466a3e5","target_id":"CLM-022"} -->
##### Prerequisites

| Prerequisite | Status in Phase A |
|---|---|
| DEL-17-01 source-basis kit available | Read as upstream context. |
| DEL-17-02 export package/profile/stable-ID/loss-report contract available | Read as upstream context. |
| DEL-08-04 result export format | Declared upstream dependency; detailed result schema behavior remains `TBD` in this deliverable. |
| DEL-14-02 and DEL-14-05 comparison/run contracts | Declared upstream dependencies; exact comparison export semantics remain `TBD` in this deliverable. |
| Governing references in `_REFERENCES.md` | Read as source basis. |
| Protected/proprietary examples | Not admitted. |

<!-- sow-source-end -->

### CLM-023 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":40,"line_start":27,"source_sha256":"3cec21c032503ed8b83acaf652cf3cecdaa694f397c1878861aba0daa466a3e5","target_id":"CLM-023"} -->
##### Steps

1. Confirm the deliverable identity from `_CONTEXT.md`: DEL-17-06, PKG-17, `BACKEND_FEATURE_SLICE`, SOW-046 and SOW-074.
2. Confirm `_STATUS.md` permits a P1/P2 four-documents write. If current state is outside the allowed overwrite states, stop without overwriting production documents.
3. Read `_REFERENCES.md`, `_DEPENDENCIES.md`, `MEMORY.md`, and the local `_SEMANTIC.md` placeholder.
4. Read the relevant decomposition, export plan, governance, data-boundary, and result-export source slices.
5. Read DEL-17-01 and DEL-17-02 four-document kits for source-basis, target-boundary, stable-ID, manifest, and loss-report carryforward.
6. Populate `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` with source-grounded statements only.
7. Preserve `TBD` for unresolved target behavior, including exact CSV table names, CSV columns, JSON schema/object layout, package-member paths, comparison tolerances, validation thresholds, and external-target mappings.
8. Exclude proprietary examples, protected standards content, private project data, code-specific allowables, SIF/flexibility values, and professional/code-compliance claims.
9. Run local validation checks allowed for this Phase A documentation task.
10. If the starting lifecycle state is `OPEN`, update `_STATUS.md` to `INITIALIZED` using the four-documents safe-update rule.
11. Update the run record with changed files, validation, missing inputs, and remaining human-ruling items.

<!-- sow-source-end -->

### CLM-024 — Later Implementation Consumption

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":52,"line_start":41,"source_sha256":"3cec21c032503ed8b83acaf652cf3cecdaa694f397c1878861aba0daa466a3e5","target_id":"CLM-024"} -->
##### Later Implementation Consumption

When a later sealed TASK is authorized to implement the stress-neutral package, use this document kit as an input and keep the implementation inside that later task's approved write scope.

1. Re-read DEL-17-01 and DEL-17-02 before defining support claims, package contracts, stable-ID behavior, manifest content, or loss-report behavior.
2. Generate or update stress-neutral CSV and JSON schemas only in the later authorized schema/code scope; keep exact field names, package paths, and object layouts `TBD` until then.
3. Implement writer behavior against the common package/profile/ID-map/manifest/loss-report contract and the result export envelope boundary.
4. Create invented or rights-cleared fixtures only after recording provenance, redistribution status, and protected-content review evidence.
5. Validate CSV and JSON outputs for shared identity, unit/dimensional metadata, source model/run references, manifest basis, loss-report content, diagnostics, and boundary notices.
6. Preserve comparison tolerances, pass/fail wording, and export comparison semantics as `TBD` until DEL-14-02/DEL-14-05 provide the applicable upstream basis.
7. Record generated schemas, CSV outputs, JSON outputs, manifests, loss reports, validation reports, and fixtures as future implementation evidence, not as code-compliance or professional-acceptance evidence.

<!-- sow-source-end -->

### CLM-025 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":71,"line_start":53,"source_sha256":"3cec21c032503ed8b83acaf652cf3cecdaa694f397c1878861aba0daa466a3e5","target_id":"CLM-025"} -->
##### Verification

Run from repository root:

```bash
tools/validation/check_four_documents.sh "execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-06_Stress-neutral CSV JSON package"
tools/validation/check_min_viable_fileset.sh "execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-06_Stress-neutral CSV JSON package"
rg -n "certif|seal|code compliance|professional approval|engineering acceptance|formal validation|release readiness|proprietary example|protected standards" "execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-06_Stress-neutral CSV JSON package"
git diff --check -- "execution/PKG-17_Export Format Interoperability/1_Working/DEL-17-06_Stress-neutral CSV JSON package"
```

Expected Phase A verification result:

- four-document kit exists;
- minimum viable fileset remains present;
- professional-boundary terms appear only as prohibited-claim language;
- no implementation code, schema files, fixtures, or dependency extraction artifacts are created;
- `TBD` remains visible for unresolved implementation and target behavior.

<!-- sow-source-end -->

### CLM-026 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":93,"line_start":72,"source_sha256":"3cec21c032503ed8b83acaf652cf3cecdaa694f397c1878861aba0daa466a3e5","target_id":"CLM-026"} -->
##### Records

Phase A records:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md`
- `_run_records/TASK_RUN_2026-05-18_1155.md`
- `_run_records/TASK_RUN_2026-05-18_1218.md`

Records intentionally not produced in this Phase A task:

- `Dependencies.csv`
- `_SEMANTIC_LENSING.md`
- stress-neutral CSV schema
- stress-neutral JSON schema
- export writer
- comparison fixtures
- implementation tests

<!-- sow-source-end -->

### CLM-027 — Closeout Checks

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":110,"line_start":94,"source_sha256":"3cec21c032503ed8b83acaf652cf3cecdaa694f397c1878861aba0daa466a3e5","target_id":"CLM-027"} -->
##### Closeout Checks

- Changed files remain inside the allowed DEL-17-06 write scope.
- `MEMORY.md` remains unchanged as instructed.
- No sibling DEL-17 folders are edited.
- No later skills are run.
- No schema, code, release, compatibility, code-compliance, professional-approval, formal-validation, or engineering-acceptance claim is made.

Future implementation closeout checks, once implementation artifacts exist:

- Generated stress-neutral CSV schemas, JSON schemas, CSV outputs, JSON outputs, manifests, loss reports, and fixtures are present only if authorized by that later task.
- Package-member paths, source model references, analysis-run references, manifest references, ID-map references, and validation-report references are populated or explicitly left `TBD`.
- CSV and JSON representations pass a synchronization check for identity, units, manifest basis, loss-report content, diagnostics, and boundary notices.
- Hash records identify payload scope; JSON payload hashes use the declared sorted-compact Python JSON basis without a JCS claim, CSV hashes use normalized ASCII/LF text, and non-JSON partitioning remains explicit.
- Fixture/example data has provenance and redistribution evidence, or remains absent/`TBD`.
- Target-specific support flags cite source evidence or remain `TBD`.
- Comparison semantics cite DEL-14-02/DEL-14-05 or remain diagnostic/audit-only and `TBD`.
<!-- sow-source-end -->

### CLM-028 — D-41 R5 T2A canonicalization check (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":113,"line_start":111,"source_sha256":"3cec21c032503ed8b83acaf652cf3cecdaa694f397c1878861aba0daa466a3e5","target_id":"CLM-028"} -->
##### D-41 R5 T2A canonicalization check (2026-07-12)

Verify exact serialized bytes, a fixed SHA-256 vector, ordering stability, mutation sensitivity, the JSON/CSV label split, schema acceptance, and absence of a JCS claim before accepting checksum evidence.
<!-- sow-source-end -->

- **VER-001** — Validate the contract and review source parity, synchronized CSV/JSON package obligations, canonical identity, units and hash labels, source/run and manifest bindings, loss and diagnostic visibility, retained TBDs, protected-content exclusions, and absence of vendor, release, compliance, validation, or professional-acceptance claims.

## Governing Values and Decisions — Axiology

### CLM-029 — Guidance: DEL-17-06 Stress-neutral CSV/JSON package

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":3,"line_start":1,"source_sha256":"2dafa84e89a8436fd910a52b1b0ec261c40c51a167135e57fa0a823b53f674a3","target_id":"CLM-029"} -->
#### Guidance: DEL-17-06 Stress-neutral CSV/JSON package

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-030 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":11,"line_start":4,"source_sha256":"2dafa84e89a8436fd910a52b1b0ec261c40c51a167135e57fa0a823b53f674a3","target_id":"CLM-030"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-17-06-DECL-003`.

<!-- sow-source-end -->

### CLM-031 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":17,"line_start":12,"source_sha256":"2dafa84e89a8436fd910a52b1b0ec261c40c51a167135e57fa0a823b53f674a3","target_id":"CLM-031"} -->
##### Purpose

Use this deliverable to keep the stress-neutral CSV/JSON package narrow and auditable. Its job is to expose result/package evidence in a project-controlled form that humans and downstream tools can inspect, compare, and adapt.

The package must not be described as a solver certification, code-compliance result, professional approval state, formal validation record, or vendor compatibility guarantee.

<!-- sow-source-end -->

### CLM-032 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":19,"line_start":18,"source_sha256":"2dafa84e89a8436fd910a52b1b0ec261c40c51a167135e57fa0a823b53f674a3","target_id":"CLM-032"} -->
##### Principles

<!-- sow-source-end -->

### CLM-033 — Keep the package stress-neutral

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":23,"line_start":20,"source_sha256":"2dafa84e89a8436fd910a52b1b0ec261c40c51a167135e57fa0a823b53f674a3","target_id":"CLM-033"} -->
###### Keep the package stress-neutral

The package should describe stress-model and result concepts in OpenPipeStress terms, then preserve enough identity, units, diagnostics, provenance, and loss reporting for consumers to understand what was exported. It should not encode target-solver hidden defaults or code-specific acceptance criteria.

<!-- sow-source-end -->

### CLM-034 — Prefer explicit gaps over silent meaning

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":27,"line_start":24,"source_sha256":"2dafa84e89a8436fd910a52b1b0ec261c40c51a167135e57fa0a823b53f674a3","target_id":"CLM-034"} -->
###### Prefer explicit gaps over silent meaning

A useful stress-neutral export can still be incomplete. Missing columns, omitted entity families, unsupported result classes, unresolved unit mappings, and unsupported comparison semantics should be represented as `TBD`, loss-report entries, diagnostics, or blocking findings rather than guessed defaults.

<!-- sow-source-end -->

### CLM-035 — Preserve identity before convenience

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":31,"line_start":28,"source_sha256":"2dafa84e89a8436fd910a52b1b0ec261c40c51a167135e57fa0a823b53f674a3","target_id":"CLM-035"} -->
###### Preserve identity before convenience

CSV is useful for review, but row order is not identity. JSON is useful for structured interchange, but object nesting is not enough by itself. Both formats should preserve stable canonical IDs or reference an ID map so rows and objects can be reconciled with source model entities, analysis runs, and comparison records.

<!-- sow-source-end -->

### CLM-036 — Treat results as evidence

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":37,"line_start":32,"source_sha256":"2dafa84e89a8436fd910a52b1b0ec261c40c51a167135e57fa0a823b53f674a3","target_id":"CLM-036"} -->
###### Treat results as evidence

The package may help review, regression comparison, downstream tooling, and adapter development. It does not authenticate an engineering design or establish professional reliance. Any human acceptance reference remains separate and hash-bound outside this package.

If a future workflow needs to point at a human acceptance reference, this package should carry only a neutral external reference such as a model-state, report, analysis-run, or project-governance record identifier plus the reviewed hash basis. The reference target, reviewer authority, and acceptance meaning stay outside the stress-neutral CSV/JSON package, and the package must not convert that reference into a software-generated approval, certification, code-compliance, or professional-reliance status.

<!-- sow-source-end -->

### CLM-037 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":50,"line_start":38,"source_sha256":"2dafa84e89a8436fd910a52b1b0ec261c40c51a167135e57fa0a823b53f674a3","target_id":"CLM-037"} -->
##### Considerations

| Topic | Guidance |
|---|---|
| CSV tables | Use table-oriented outputs for inspection and spreadsheet workflows, but keep exact table names, columns, ordering, quoting rules, and null handling `TBD` until schema work begins. |
| JSON package | Use JSON for structured import/export and future validation, but do not create a schema in this Phase A task. JSON Schema 2020-12 remains the expected future baseline. |
| Units | Every result value needs explicit unit and dimensional context or a blocking diagnostic. Do not rely on spreadsheet headers alone for unit meaning. |
| Result values | Displacements, rotations, forces, moments, reactions, stress, ratios, and rule-check values are governed by result-export boundaries. Which result families appear in the stress-neutral package is `TBD`. |
| Materials and sections | Include identity/provenance surfaces only unless user-cleared data is present. Do not bundle protected tables, allowables, catalog defaults, SIF/flexibility values, or proprietary values. |
| Load/design cases | Preserve source basis and identity. Do not imply code-specific load combinations unless user/private rule data supplies them with provenance. |
| Comparisons | Use stable IDs and declared tolerance profiles when comparison semantics are later defined. Tolerances and pass/fail language are `TBD` in Phase A. |
| External solver data | CAEPIPE CSV/text parsing can provide regression or handoff evidence under DEL-17-05, but it does not make this package professionally authoritative. |

<!-- sow-source-end -->

### CLM-038 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":60,"line_start":51,"source_sha256":"2dafa84e89a8436fd910a52b1b0ec261c40c51a167135e57fa0a823b53f674a3","target_id":"CLM-038"} -->
##### Trade-offs

| Choice | Benefit | Risk | Phase A disposition |
|---|---|---|---|
| CSV plus JSON | Serves both spreadsheet review and structured downstream tooling. | Two representations can drift. | Require shared identity, units, manifest, and validation basis; exact synchronization checks `TBD`. |
| Broad table inventory | Makes the package useful across adapters. | Can imply support for semantics not yet implemented. | List candidate table families but keep field-level behavior `TBD`. |
| Loss report on successful exports | Prevents silent omissions and approximations. | Adds package complexity. | Required by DEL-17-02 common contract. |
| Stress-neutral vocabulary | Avoids vendor lock-in. | Consumers may need adapter-specific mapping. | Use profile/manifest/ID map/loss report to keep mappings explicit. |
| Regression comparison support | Supports deterministic review over time. | Users may mistake comparison evidence for professional acceptance. | Comparison remains diagnostic/audit functionality only. |

<!-- sow-source-end -->

### CLM-039 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":66,"line_start":61,"source_sha256":"2dafa84e89a8436fd910a52b1b0ec261c40c51a167135e57fa0a823b53f674a3","target_id":"CLM-039"} -->
##### Examples

No concrete CSV rows, JSON payloads, proprietary examples, solver outputs, protected standards data, or public engineering fixtures are included in Phase A.

Acceptable future examples should be invented or otherwise rights-cleared and should demonstrate shape, identity, units, diagnostics, loss reporting, and boundary notices without embedding protected or private engineering values.

<!-- sow-source-end -->

### CLM-040 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":71,"line_start":67,"source_sha256":"2dafa84e89a8436fd910a52b1b0ec261c40c51a167135e57fa0a823b53f674a3","target_id":"CLM-040"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| none | No source conflict identified in Phase A. | n/a | n/a | n/a | n/a | n/a |
<!-- sow-source-end -->

### CLM-041 — D-41 R5 T2A canonicalization guidance (2026-07-12)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":74,"line_start":72,"source_sha256":"2dafa84e89a8436fd910a52b1b0ec261c40c51a167135e57fa0a823b53f674a3","target_id":"CLM-041"} -->
##### D-41 R5 T2A canonicalization guidance (2026-07-12)

Do not describe `canonical_json` as JCS. Preserve exact sorted-key compact Python JSON bytes and the precise `deterministic_sorted_compact_json_payload_hash` label unless a later governed change introduces and proves an RFC 8785 implementation.
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-046 SOW-074 OBJ-007 OBJ-017 OBJ-018 | CLM-010 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
