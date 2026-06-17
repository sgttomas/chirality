# Source Pack: SRC-DEL-DEL-15-01-CANONICAL-HANDOFF-PACKAGE-SCHEMA-AND-MANIFEST

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-15_Handoff and External Prover Workflow/1_Working/DEL-15-01_Canonical handoff package schema and manifest/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-15_Handoff and External Prover Workflow/1_Working/DEL-15-01_Canonical handoff package schema and manifest/Datasheet.md

### Datasheet: DEL-15-01 Canonical handoff package schema and manifest

#### Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-15-01 | `_CONTEXT.md` |
| Name | Canonical handoff package schema and manifest | `_CONTEXT.md`; `docs/_Registers/Deliverables.csv` |
| Package | PKG-15 Handoff and External Prover Workflow | `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md` |
| Type | API_CONTRACT | `_CONTEXT.md`; `docs/TYPES.md#3-software-deliverable-types` |
| Scope item | SOW-074 | `_CONTEXT.md`; `docs/_Registers/ScopeLedger.csv` |
| Objective | OBJ-017 | `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md#5-objectives` |
| Anticipated artifacts | `schemas/handoff_package.schema.json`; handoff manifest schema | `_CONTEXT.md` |
| Lifecycle input state | `IN_PROGRESS` at review-readiness intake | `_STATUS.md` |

#### Attributes

| Attribute | Value | Source / status |
|---|---|---|
| Contract surface | Schema-compliant handoff package plus manifest | SOW-074 in `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md#4-structured-scope-of-work-ssow` |
| Schema baseline | JSON Schema 2020-12 contracts | `_CONTEXT.md#Architecture Basis Injection`; `execution/_Decomposition/SOFTWARE_DECOMP.md#82-resolved-architecture-baseline` |
| Hash baseline | Canonical JSON/JCS-compatible hash basis where JSON payloads are hashed; manifest hashes for non-JSON/binary assets | `_CONTEXT.md#Architecture Basis Injection`; `execution/_Decomposition/SOFTWARE_DECOMP.md#81-architecture-basis-register` |
| Required package contents named by scope | model hash, units manifest, entity IDs, library/rule references, unresolved assumptions, warnings, target mapping metadata, unsupported-target flags | SOW-074 in `_CONTEXT.md`; `docs/_Registers/ScopeLedger.csv` |
| Professional boundary | Handoff packages support downstream modeling and professional validation workflows without automatic professional approval states | OBJ-017 in `execution/_Decomposition/SOFTWARE_DECOMP.md#5-objectives`; `docs/CONTRACT.md#1-invariant-index` |
| Target-specific commercial parsers | Deferred / out of this deliverable | SOW-074 notes; `execution/_Decomposition/SOFTWARE_DECOMP.md#11-open-issues` |
| Canonical package container | TBD | OI-015 in `execution/_Decomposition/SOFTWARE_DECOMP.md#11-open-issues` |
| Handoff target surfaces | Initial export and target surfaces are named by OI-015; concrete mappings, unsupported-behavior taxonomy extensions, target field coverage, and target-specific implementation remain gated by DEL-17-01 and DEL-17-02 | OI-015 in `execution/_Decomposition/SOFTWARE_DECOMP.md#11-open-issues` |
| Schema property names and `$id` values | `$id`: `https://openpipestress.org/schemas/handoff_package.schema.json`; root and nested properties are materialized in `schemas/handoff_package.schema.json` | DEL-15-01 implementation evidence |

#### Conditions

| Condition | Record |
|---|---|
| Data boundary | The public repository must not include protected standards text, protected tables, proprietary vendor data, private project data, or private rule-pack payloads. Source: `docs/IP_AND_DATA_BOUNDARY.md#3-public-repository-must-not-contain`. |
| Unit boundary | Physical values crossing schema, import/export, report, or rule-evaluation boundaries must carry explicit unit metadata unless explicitly dimensionless. Source: `docs/SPEC.md#4-unit-system-and-dimensional-analysis`. |
| Diagnostics boundary | Warnings and diagnostics must preserve structured source/provenance fields and must not become code-compliance or professional-approval claims. Source: `docs/CONTRACT.md#1-invariant-index`; AB-00-06 in decomposition. |
| API/adapter boundary | Adapters and plugins cannot bypass validation, unit checks, provenance, diagnostics, privacy, protected-content, or professional-boundary controls. Source: AB-00-07 in `execution/_Decomposition/SOFTWARE_DECOMP.md#81-architecture-basis-register`. |
| Dependency context | DAG-002 mirror lists upstream architecture-basis, result export, audit manifest/model hash, immutable model state, analysis run, local FEA handoff, and canonical domain model rows as ACTIVE evidence. Source: local `Dependencies.csv`. |

#### Construction

The deliverable is a contract-definition unit with a materialized JSON Schema and invented validation fixture. Construction evidence currently supports the following schema/manifest slots:

| Slot | Required treatment | Source |
|---|---|---|
| Package identity | Include stable package identity, schema version, deliverable/package/scope/objective identifiers, and review state fields. | SOW-074; `schemas/handoff_package.schema.json` |
| Model hash | Represent model basis through the required `model_hash` checksum object, including algorithm, value, canonicalization, and provenance. | SOW-074; AB-00-04 hash basis; `schemas/handoff_package.schema.json` |
| Units manifest | Represent explicit units through the required `units_manifest` object, including unit system, dimensional basis, entries, diagnostics, and provenance. | SOW-074; `docs/SPEC.md#4-unit-system-and-dimensional-analysis`; `schemas/handoff_package.schema.json` |
| Entity IDs | Preserve stable model/entity identifiers through required `entity_ids` records with `entity_id`, `entity_kind`, `source_ref`, and optional mapping keys. | SOW-074; `docs/TYPES.md#2-stable-identifiers`; `schemas/handoff_package.schema.json` |
| Library/rule references | Reference libraries and rule packs through `library_refs` and `rule_pack_refs` identity/checksum/provenance records without copying protected/private payloads. | SOW-074; `docs/IP_AND_DATA_BOUNDARY.md`; `docs/SPEC.md#9-reporting-and-audit`; `schemas/handoff_package.schema.json` |
| Warnings and unresolved assumptions | Carry structured `warnings`, `unresolved_assumptions`, and `diagnostics` as review evidence with source/provenance fields. | SOW-074; `docs/SPEC.md#8-gui-requirements`; `docs/SPEC.md#9-reporting-and-audit`; `schemas/handoff_package.schema.json` |
| Target mapping metadata | Reserve a manifest surface for mapping to downstream target fields. Detailed target mapping contract is DEL-15-02. | SOW-074; DEL-15-02 row in decomposition |
| Unsupported-target flags | Reserve explicit unsupported/approximate target behavior flags. Detailed target contract is DEL-15-02. | SOW-074; OI-015 |
| Provenance | Preserve source/provenance for reliance-affecting data through the schema's required `provenance` object and nested reference provenance records. | `docs/DIRECTIVE.md#22-epistemology--what-is-warranted`; `docs/CONTRACT.md#1-invariant-index`; `schemas/handoff_package.schema.json` |

#### References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_STATUS.md`
- local `Dependencies.csv`
- `execution/_Decomposition/SOFTWARE_DECOMP.md`
- `docs/_Registers/Deliverables.csv`
- `docs/_Registers/ScopeLedger.csv`
- `docs/_Registers/ContextBudgetQA.csv`
- `docs/CONTRACT.md`
- `docs/TYPES.md`
- `docs/SPEC.md`
- `docs/DIRECTIVE.md`
- `docs/IP_AND_DATA_BOUNDARY.md`

## Component: execution/PKG-15_Handoff and External Prover Workflow/1_Working/DEL-15-01_Canonical handoff package schema and manifest/Guidance.md

### Guidance: DEL-15-01 Canonical handoff package schema and manifest

#### Purpose

DEL-15-01 exists to define a canonical handoff package schema and manifest for downstream modeling and professional validation workflows. The package is evidence-transfer infrastructure: it should make model basis, units, identifiers, warnings, assumptions, provenance, and mapping limitations visible without claiming that software output is professional approval.

Sources: `_CONTEXT.md`; SOW-074; OBJ-017; `execution/_Decomposition/SOFTWARE_DECOMP.md#7-deliverables`.

#### Principles

| Principle | Guidance | Source |
|---|---|---|
| Schema-first contract | Treat `schemas/handoff_package.schema.json` as the stable JSON Schema 2020-12 API/data contract for this deliverable. | Deliverable type `API_CONTRACT`; JSON Schema 2020-12 architecture basis; June 7 remediation evidence |
| Evidence preservation | Prefer references, hashes, manifests, and provenance over copied private/protected payloads. | `docs/IP_AND_DATA_BOUNDARY.md`; OPS-K-IP-1 through OPS-K-DATA-3 |
| Unit explicitness | Do not allow missing or ambiguous units to become downstream assumptions. | `docs/SPEC.md#4-unit-system-and-dimensional-analysis`; OPS-K-UNIT-1 |
| Stable identity | Preserve stable object/entity identity so downstream mapping can be reviewed and reconciled. | SOW-074; `docs/TYPES.md#2-stable-identifiers` |
| Boundary clarity | Keep target mapping and unsupported behavior explicit. OI-015 now names initial export and target surfaces, while concrete mappings, unsupported-behavior taxonomy extensions, target field coverage, and target-specific implementation remain gated by DEL-17-01 and DEL-17-02. | SOW-074; DEL-15-02 row; OI-015 |
| Professional non-authority | The handoff package may support professional validation workflows, but it must not create automatic approval, certification, sealing, endorsement, or code-compliance states. | OBJ-017; OPS-K-AUTH-1; `docs/TYPES.md#4-analysis-status-vocabulary` |

#### Considerations

- The physical package/container remains unresolved for this deliverable. OI-015 names initial export and target surfaces, but concrete mappings, unsupported-behavior taxonomy extensions, target field coverage, and target-specific implementation remain gated by DEL-17-01 and DEL-17-02.
- DAG-002 rows identify important upstream context, including architecture basis, local FEA handoff contract, result export format, audit manifest/model hash, immutable model states, analysis run records, and canonical domain model schema. These rows are dependency evidence, not authority to inspect or modify sibling deliverable folders during this task.
- Target mapping metadata and unsupported-target flags are required by SOW-074, but detailed semantics belong to DEL-15-02. DEL-15-01 should reserve clear schema surfaces for those records.
- The deliverable now has an invented, non-engineering fixture at `fixtures/invented_handoff_package.json`. Public examples or fixtures for this contract must remain invented or otherwise reviewed and must not include protected standards text, private rule-pack payloads, proprietary commercial files, or real project data.
- Handoff package validation is covered by `tests/test_handoff_package_schema.py`, including Draft 2020-12 schema validation and fixture validation. It should not attempt to prove external solver correctness or code compliance.

#### Trade-offs

| Trade-off | Preferred direction | Reason |
|---|---|---|
| Rich payload vs reference-heavy manifest | Prefer reference-heavy records for private/protected or large payloads. | Preserves data boundary and avoids copying private/protected values. |
| Target-neutral vs target-specific fields | Keep DEL-15-01 target-neutral and reserve extension/mapping surfaces. | Detailed target mapping belongs to DEL-15-02 and target-specific implementation remains gated by DEL-17-01 and DEL-17-02. |
| Strict required fields vs unresolved project reality | Require the slots named by SOW-074 using the materialized schema property map. | Avoids hidden defaults while preserving target-specific and container deferrals. |
| Software status vs professional status | Emit diagnostics/findings and human-review-needed notices, not approval/compliance states. | Maintains OPS-K-AUTH-1 and OBJ-017. |

#### Examples

The current invented example payload is `fixtures/invented_handoff_package.json`. It is provenance-labeled, non-engineering fixture data used to validate `schemas/handoff_package.schema.json` with `jsonschema.Draft202012Validator` through `tests/test_handoff_package_schema.py`.

Any future example must avoid protected standards content, private project data, private rule-pack content, proprietary values, real secrets, and automatic professional-approval claims.

#### Conflict Table (for human ruling)

No direct source conflicts were identified in this setup pass. The following open items are unresolved rather than conflicting:

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| OI-015-OPEN | Current decomposition names initial export and target surfaces, but concrete mappings, unsupported-behavior taxonomy extensions, target field coverage, target-specific implementation, and this deliverable's physical package/container remain gated. | `execution/_Decomposition/SOFTWARE_DECOMP.md#11-open-issues` | `_CONTEXT.md#Scope Detail` | Datasheet Attributes; Specification Requirements; Procedure Steps | Keep DEL-15-01 target-neutral; do not claim target-specific mapping maturity before DEL-17-01 and DEL-17-02 evidence. | TBD |

## Component: execution/PKG-15_Handoff and External Prover Workflow/1_Working/DEL-15-01_Canonical handoff package schema and manifest/Procedure.md

### Procedure: DEL-15-01 Canonical handoff package schema and manifest

#### Purpose

Define the bounded procedure for producing and reviewing the canonical handoff package schema and manifest contract for DEL-15-01. This procedure is operational guidance for the deliverable artifact; it does not implement runtime export behavior.

Sources: `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md`; `docs/CONTRACT.md`; `docs/SPEC.md`.

#### Prerequisites

| Prerequisite | Evidence / status |
|---|---|
| DEL-15-01 context and references are available. | `_CONTEXT.md`; `_REFERENCES.md` |
| SOW-074 and OBJ-017 are the active scope/objective basis. | `_CONTEXT.md`; decomposition; registers |
| JSON Schema 2020-12 is the schema baseline. | `_CONTEXT.md#Architecture Basis Injection`; AB-00-04/AB-00-07 |
| Unit, provenance, diagnostics, privacy, protected-content, and professional-boundary invariants are available. | `docs/CONTRACT.md`; `docs/SPEC.md`; `docs/IP_AND_DATA_BOUNDARY.md` |
| Existing DAG-002 mirror rows remain ACTIVE evidence and are not reclassified by this setup run. | local `Dependencies.csv`; `_DEPENDENCIES.md` |
| Package container, concrete mappings, target field coverage, and target-specific implementation remain unresolved. | OI-015; DEL-17-01; DEL-17-02 |

#### Steps

1. Confirm deliverable identity from `_CONTEXT.md`, including DEL-15-01, PKG-15, type `API_CONTRACT`, SOW-074, OBJ-017, and anticipated artifacts.
2. Read the DEL-15-01 decomposition entry and associated SOW-074 / OBJ-017 rows. Record scope as schema/manifest contract work, not runtime export implementation.
3. List required handoff-package slots from SOW-074: model hash, units manifest, entity IDs, library/rule references, unresolved assumptions, warnings, target mapping metadata, unsupported-target flags, and provenance.
4. Apply architecture-basis constraints that are explicitly injected into `_CONTEXT.md`: JSON Schema 2020-12 contracts, canonical JSON/JCS-compatible hash basis for JSON payloads, schema-first envelopes, and no-bypass adapter controls.
5. Treat `schemas/handoff_package.schema.json`, its `$id`, and `fixtures/invented_handoff_package.json` as materialized contract evidence; keep package container, concrete mappings, target field coverage, and target-specific implementation gated under OI-015 / DEL-17-01 / DEL-17-02.
6. Draft or review schema artifacts and fixtures so they preserve references and metadata without copying protected standards text, private project data, private rule-pack payloads, proprietary commercial data, or real secrets.
7. Ensure the manifest design includes structured warnings, assumptions, provenance, unit metadata, hashes, and professional-boundary posture.
8. Verify that target mapping metadata and unsupported-target flags are present as contract surfaces while detailed semantics remain delegated to DEL-15-02.
9. Check that no field, enum, status, or explanatory text creates automatic professional approval, certification, sealing, authentication, endorsement, or code-compliance claims.
10. Validate dependency artifacts locally if `Dependencies.csv` exists using `python3 tools/validation/validate_dependencies_schema.py`.

#### Verification

| Verification item | Method |
|---|---|
| Source grounding | Check each non-trivial requirement against `_CONTEXT.md`, decomposition, registers, local DAG-002 mirror, or governing references. |
| Schema baseline | Validate `schemas/handoff_package.schema.json` with `jsonschema.Draft202012Validator.check_schema` and validate the invented fixture with `python3 tests/test_handoff_package_schema.py`. |
| Required slots | Confirm the SOW-074 slots are present as requirements or explicit TBD surfaces. |
| TBD discipline | Confirm package container, concrete mappings, target field coverage, and target-specific implementation are not invented. Schema property names and validation fixture are now materialized evidence. |
| Data boundary | Check that schema guidance does not embed protected/private/proprietary payloads or examples. |
| Professional boundary | Check that the contract does not emit automatic approval/compliance/certification statuses. |
| Dependency mirror preservation | Confirm approved DAG-006 rows remain ACTIVE and are not retired, deleted, or reclassified. |

#### Records

Maintain these records in the DEL-15-01 folder for setup:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_SEMANTIC.md`
- `_SEMANTIC_LENSING.md`
- existing `_DEPENDENCIES.md`
- existing `Dependencies.csv`
- `schemas/handoff_package.schema.json`
- `tests/test_handoff_package_schema.py`
- `fixtures/invented_handoff_package.json`
- final run report with dependency-schema validation result and any dependency-extract conflicts

## Component: execution/PKG-15_Handoff and External Prover Workflow/1_Working/DEL-15-01_Canonical handoff package schema and manifest/Specification.md

### Specification: DEL-15-01 Canonical handoff package schema and manifest

#### Scope

This deliverable defines the contract surface for a canonical handoff package schema and handoff manifest for downstream modeling and professional validation workflows. The scope is bounded to DEL-15-01, PKG-15, SOW-074, and OBJ-017.

Included:

- schema/manifest requirements for model hash, units manifest, entity IDs, library/rule references, unresolved assumptions, warnings, target mapping metadata, unsupported-target flags, and provenance;
- JSON Schema 2020-12 alignment for the anticipated `schemas/handoff_package.schema.json` artifact;
- professional-boundary, unit, provenance, diagnostics, and data-boundary constraints that affect handoff package shape.

Excluded:

- implementation of the downstream export workflow, which belongs to DEL-15-03;
- detailed target mapping semantics and unsupported-behavior taxonomy beyond reserving the required surface, which belongs to DEL-15-02;
- external-prover lifecycle or approval metadata, which belongs to DEL-15-04;
- target-specific commercial parser implementation, commercial output ingestion, or automatic professional approval records.

Sources: `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md#7-deliverables`; SOW-074; OBJ-017; OI-015.

#### Requirements

| Req ID | Requirement | Source | Verification |
|---|---|---|---|
| DEL-15-01-R01 | The handoff package contract shall be represented as a schema-first API/data contract. | `_CONTEXT.md` Type `API_CONTRACT`; `docs/TYPES.md#3-software-deliverable-types` | Confirm artifact naming and schema document role in this deliverable. |
| DEL-15-01-R02 | The schema baseline shall use JSON Schema 2020-12 unless a later approved architecture change supersedes it. | `_CONTEXT.md#Architecture Basis Injection`; `execution/_Decomposition/SOFTWARE_DECOMP.md#82-resolved-architecture-baseline` | Validate `schemas/handoff_package.schema.json` with Draft 2020-12 tooling. |
| DEL-15-01-R03 | The package shall include or reference a model hash through the required `model_hash` checksum object, including algorithm, value, canonicalization, and provenance. | SOW-074; AB-00-04 | Review schema properties and fixture validation for model-hash presence. |
| DEL-15-01-R04 | The package shall include a `units_manifest` with unit system, dimensional basis, entries, diagnostics, and provenance sufficient to avoid silent missing-unit behavior. | SOW-074; `docs/SPEC.md#4-unit-system-and-dimensional-analysis`; OPS-K-UNIT-1 | Schema review plus fixture validation for unit-related fields. |
| DEL-15-01-R05 | The package shall preserve stable entity IDs used by downstream mapping and review through `entity_ids` records. | SOW-074; `docs/TYPES.md#2-stable-identifiers`; `docs/TYPES.md#8-canonical-domain-object-registry` | Schema review for required ID/reference fields and no positional-only coupling. |
| DEL-15-01-R06 | The package shall carry library and rule-pack references by identity, version/checksum/source note, or equivalent reference metadata without copying protected/private payloads through `library_refs` and `rule_pack_refs`. | SOW-074; `docs/IP_AND_DATA_BOUNDARY.md#6-private-user-data`; `docs/SPEC.md#9-reporting-and-audit` | Protected-content/privacy review and schema review for reference-only design. |
| DEL-15-01-R07 | The package shall carry unresolved assumptions, warnings, and diagnostics as explicit review evidence, not silent defaults. | SOW-074; OPS-K-DATA-2; AB-00-06; `docs/SPEC.md#8-gui-requirements` | Schema review for `unresolved_assumptions`, `warnings`, `diagnostics`, and provenance fields. |
| DEL-15-01-R08 | The package shall reserve target mapping metadata required by SOW-074 while leaving detailed target mapping rules to DEL-15-02. | SOW-074; DEL-15-02 row in decomposition | Cross-deliverable interface review against `schemas/target_mapping.schema.json`. |
| DEL-15-01-R09 | The package shall reserve unsupported-target flags required by SOW-074 while leaving detailed unsupported behavior semantics to DEL-15-02. | SOW-074; OI-015 | Cross-deliverable interface review against `schemas/target_mapping.schema.json`. |
| DEL-15-01-R10 | The package and manifest shall preserve provenance for reliance-affecting data and references. | OPS-K-DATA-3; `docs/DIRECTIVE.md#25-axiology--what-values-govern`; `docs/IP_AND_DATA_BOUNDARY.md#4-required-provenance-fields` | Schema review for provenance-bearing records and protected-content gate. |
| DEL-15-01-R11 | The contract shall not declare certification, sealing, approval, authentication, code compliance, or professional acceptance as automatic software output. | OPS-K-AUTH-1; OBJ-017; `docs/TYPES.md#4-analysis-status-vocabulary` | Text/schema enum review for prohibited automatic statuses. |
| DEL-15-01-R12 | The package container remains TBD. OI-015 names initial export and target surfaces, while concrete mappings, unsupported-behavior taxonomy extensions, target field coverage, and target-specific implementation remain gated by DEL-17-01 and DEL-17-02. | OI-015; `_CONTEXT.md#Architecture Basis Injection` | Confirm the handoff schema remains target-neutral and does not claim target-specific mapping maturity. |

#### Standards

| Standard / governing source | Applicability | Status |
|---|---|---|
| JSON Schema 2020-12 | Public schema/interchange baseline for the handoff schema. | Applicable by architecture basis; `$id` is `https://openpipestress.org/schemas/handoff_package.schema.json`. |
| Project invariant catalog (`docs/CONTRACT.md`) | Governs IP, units, data, professional-boundary, report, governance, and agent behavior. | Applicable. |
| Project type vocabulary (`docs/TYPES.md`) | Governs deliverable/API contract meaning, stable identifiers, status vocabulary, and epistemic labels. | Applicable. |
| IP and Data Boundary Policy (`docs/IP_AND_DATA_BOUNDARY.md`) | Governs protected/private data exclusion and provenance fields. | Applicable. |
| Product/decomposition basis (`execution/_Decomposition/SOFTWARE_DECOMP.md`) | Governs DEL-15-01 scope, SOW-074, OBJ-017, PKG-15 exclusions, architecture basis, and OI-015 TBDs. | Applicable. |

#### Verification

| Check ID | Check | Expected result |
|---|---|---|
| V-01 | Confirm required four documents exist and keep the default schema sections. | PASS for this setup output. |
| V-02 | Confirm all non-trivial schema requirements trace to `_CONTEXT.md`, decomposition, registers, or governing references. | PASS if every requirement has a source. |
| V-03 | Confirm unsupported specifics are marked `TBD` or `ASSUMPTION`. | PASS if package container, concrete mappings, target field coverage, and target-specific implementation are not invented. |
| V-04 | Confirm professional-boundary prohibited terms are not used as automatic software statuses. | PASS if no schema requirement creates automatic approval/compliance/certification states. |
| V-05 | Confirm local `Dependencies.csv` remains a DAG-002 mirror with approved rows preserved as ACTIVE. | PASS if dependency mirror is not retired/reclassified by setup. |
| V-06 | Run `python3 tests/test_handoff_package_schema.py` and `python3 tools/validation/validate_dependencies_schema.py <DEL folder>/Dependencies.csv` when `Dependencies.csv` exists. | PASS/FAIL recorded in final run report. |

#### Documentation

Required deliverable records:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_SEMANTIC.md`
- `_SEMANTIC_LENSING.md`
- local dependency validation result in the final run report

Implemented evidence artifacts from `_CONTEXT.md`:

- `schemas/handoff_package.schema.json`
- `tests/test_handoff_package_schema.py`
- `fixtures/invented_handoff_package.json`
