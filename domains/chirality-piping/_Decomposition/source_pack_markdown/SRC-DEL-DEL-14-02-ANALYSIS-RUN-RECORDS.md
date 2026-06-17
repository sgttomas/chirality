# Source Pack: SRC-DEL-DEL-14-02-ANALYSIS-RUN-RECORDS

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-14_Model States, Analysis Runs, and Comparison/1_Working/DEL-14-02_Analysis run records/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-14_Model States, Analysis Runs, and Comparison/1_Working/DEL-14-02_Analysis run records/Datasheet.md

### Datasheet: DEL-14-02 Analysis run records

#### Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-14-02 | `_CONTEXT.md` |
| Name | Analysis run records | `_CONTEXT.md` |
| Package ID | PKG-14 | `_CONTEXT.md` |
| Package name | Model States, Analysis Runs, and Comparison | `_CONTEXT.md` |
| Deliverable type | DATA_MODEL_CHANGE | `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md` PKG-14 table |
| Scope item | SOW-072 | `_CONTEXT.md`; `docs/_Registers/ScopeLedger.csv` row SOW-072 |
| Objective support | OBJ-016 | `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md` objective mapping |
| Anticipated artifacts | `schemas/analysis_run.schema.json`; run reproducibility tests | `_CONTEXT.md`; `docs/_Registers/Deliverables.csv` row DEL-14-02 |
| Lifecycle role | Draft production-unit document; not implementation evidence | `_CONTEXT.md` PREPARATION notes; `docs/CONTRACT.md` OPS-K-AGENT-4 |

#### Attributes

| Attribute | Value | Source |
|---|---|---|
| Required product behavior | Save analysis runs bound to exact model states, solver versions, settings, units, load cases, diagnostics, results, rule-pack references, library references, and result hashes. | `docs/_Registers/ScopeLedger.csv` row SOW-072; `execution/_Decomposition/SOFTWARE_DECOMP.md` SOW-072 |
| Record immutability intent | Results attach to immutable analysis runs rather than a mutable current model only. | `docs/_Registers/ScopeLedger.csv` row SOW-072; `_CONTEXT.md` envelope notes |
| Package boundary | PKG-14 implements immutable model-state records, analysis-run records, deterministic state/run comparison, mappings, tolerances, and comparison exports. | `execution/_Decomposition/SOFTWARE_DECOMP.md` package table |
| Package exclusion | PKG-14 does not ingest commercial prover outputs comprehensively or determine external validation. | `execution/_Decomposition/SOFTWARE_DECOMP.md` package table |
| Architecture basis | Rust core/application services; JSON Schema 2020-12 contracts; schema-first command/query/job result envelopes; canonical JSON/JCS-compatible hash basis where JSON payloads are hashed. | `_CONTEXT.md` Architecture Basis Injection |
| Unit boundary | Unit-bearing physical values crossing schema, service, solver, import/export, report, or rule-evaluation boundaries must carry explicit unit metadata unless explicitly dimensionless or equivalent. | `docs/SPEC.md` section 4 |
| Hash boundary | JSON payload hashes use the accepted JCS-compatible canonical JSON basis where the payload is JSON; non-JSON and binary partitioning remains TBD. | `docs/SPEC.md` section 4.4 |
| Result-envelope relationship | Result export envelopes must identify result set, model/run basis, solver version, unit-system reference, load-case or combination basis, diagnostics, provenance, reproducibility hashes or audit-manifest reference, analysis statuses, rule-pack references where present, and professional-boundary notice. | `docs/SPEC.md` result export section |
| Professional boundary | Software must not emit automatic human approval, certification, sealing, authentication, or code-compliance labels. | `docs/SPEC.md` analysis boundary section; `docs/CONTRACT.md` OPS-K-AUTH-1 |
| Protected/private data boundary | Public artifacts must not copy private formulas, protected standards text, protected tables, proprietary values, or private rule-pack payloads. | `docs/SPEC.md` result export section; `docs/IP_AND_DATA_BOUNDARY.md` |

#### Conditions

| Condition | Status | Source |
|---|---|---|
| Exact analysis-run schema fields | TBD pending implementation design. Only the required binding categories are source-supported here. | `_CONTEXT.md`; SOW-072 |
| Analysis run identifier format | TBD. No deliverable-local source defines the field name, format, or namespace. | `_CONTEXT.md`; `docs/TYPES.md` general identifier guidance only |
| Model-state reference semantics | Must bind to exact model states; detailed state-record schema is upstream and outside this folder. | SOW-072; `Dependencies.csv` DAG-002-E0783 |
| Solver version and settings representation | Required as part of the saved run record; exact object shape is TBD. | SOW-072 |
| Unit-system representation | Required as part of the saved run record; missing unit metadata for unit-bearing physical values must be diagnostic rather than silently supplied. | SOW-072; `docs/SPEC.md` section 4 |
| Load-case or combination basis | Required as part of the saved run record; exact references and cardinality are TBD. | SOW-072; `docs/SPEC.md` result export section |
| Diagnostics and analysis statuses | Required as part of the saved run record; must preserve the professional-boundary status model. | SOW-072; `docs/SPEC.md` analysis boundary section |
| Rule-pack and library references | Required as references/checksum/provenance surfaces; private payloads and protected content are not public artifact content. | SOW-072; `docs/SPEC.md` rule-pack/result export sections |
| Result hashes | Required; payload scope and canonicalization metadata must be explicit. | SOW-072; `docs/SPEC.md` section 4.4 |
| Reproducibility tests | Required artifact class; exact test harness, fixtures, and assertions are TBD. | `_CONTEXT.md` anticipated artifacts |

#### Construction

This deliverable is a data-model change. The conservative construction surface is:

1. Define `schemas/analysis_run.schema.json` as the canonical analysis-run record contract.
2. Include fields or referenced sub-objects sufficient to bind each analysis run to the source-supported categories in SOW-072: model state, solver version, settings, units, load cases, diagnostics, results, rule-pack references, library references, and result hashes.
3. Treat result attachment as immutable run-record evidence, not as mutable "current model" state.
4. Preserve unit metadata and dimensional diagnostics across run records wherever unit-bearing values are included or referenced.
5. Record reproducibility hash metadata using the accepted JSON/JCS-compatible basis for JSON payloads; mark non-JSON or binary partitioning as TBD until explicitly designed.
6. Preserve professional-boundary and protected/private-data controls in schema shape, diagnostics, tests, and examples.

Implementation evidence, committed product code, and passing tests are not present in this folder at setup time.

#### References

| Reference | Use in this datasheet |
|---|---|
| `_CONTEXT.md` | Deliverable identity, scope, artifact expectations, architecture-basis injection |
| `_REFERENCES.md` | Reference inventory and authority boundary |
| `_DEPENDENCIES.md`; `Dependencies.csv` | Approved DAG-002 local mirror/evidence surface |
| `execution/_Decomposition/SOFTWARE_DECOMP.md` | SOW-072, OBJ-016, PKG-14, DEL-14-02 decomposition basis |
| `docs/_Registers/Deliverables.csv` | Deliverable row and anticipated artifacts |
| `docs/_Registers/ScopeLedger.csv` | Scope item SOW-072 wording |
| `docs/CONTRACT.md` | Agent, data, unit, report, privacy, and professional-boundary invariants |
| `docs/SPEC.md` | Unit, persistence/hash, analysis-boundary, result-export, runner/result-envelope guidance |
| `docs/TYPES.md` | Canonical model/schema vocabulary and boundary notes |
| `docs/IP_AND_DATA_BOUNDARY.md` | Public/private and protected-content constraints |

## Component: execution/PKG-14_Model States, Analysis Runs, and Comparison/1_Working/DEL-14-02_Analysis run records/Guidance.md

### Guidance: DEL-14-02 Analysis run records

#### Purpose

Analysis run records exist so solver outputs can be reviewed as reproducible records bound to the exact model state, execution context, diagnostics, references, and hashes that produced them. The record is a traceability surface for design iteration and review; it is not an automatic professional approval or external validation state.

#### Principles

| Principle | Guidance | Source |
|---|---|---|
| Bind results to their run basis | Treat the run record as the durable home for result evidence, not as a transient view of the current model. | SOW-072; `_CONTEXT.md` envelope notes |
| Preserve exact upstream references | Model state, solver version, settings, units, load-case basis, diagnostics, rule packs, libraries, and result hashes are binding categories, not optional narrative notes. | SOW-072 |
| Keep units explicit | Unit-bearing physical values need unit metadata; missing or ambiguous units become diagnostics rather than inferred defaults. | `docs/SPEC.md` section 4 |
| Make hashes scoped and reproducible | Hash records should say what was hashed and what canonicalization basis was used. JSON payloads use the accepted JCS-compatible basis where applicable. | `docs/SPEC.md` section 4.4 |
| Keep authority domains separate | Solver results and diagnostics are software outputs. User-rule checks use user-supplied rule-pack data. Human acceptance, if used, is external and hash-bound. | `docs/SPEC.md` analysis boundary section |
| Protect private/protected payloads | Rule-pack and library references may carry identity, version, checksum, provenance, privacy, and review metadata, but public artifacts must not copy private/protected content. | `docs/IP_AND_DATA_BOUNDARY.md`; `docs/SPEC.md` result export section |

#### Considerations

- The folder is a setup-stage production unit. It contains no implementation evidence yet; statements about passing behavior, field names, storage APIs, or committed tests must remain TBD until produced by later Type 2 work.
- SOW-072 is sufficient to identify required binding categories, but it is not sufficient to define exact schema field names, cardinality, or migration behavior.
- The dependency mirror records approved DAG-006 predecessor evidence for architecture basis, immutable model state records, analysis status semantics, audit manifest/hash conventions, result export format, and persistence/round-trip support. Those rows are an evidence surface, not independent graph authority.
- The deliverable should align with `schemas/results.schema.yaml` and result-export envelopes where run records include or point to result payloads, but this folder does not define the final result export schema.
- `PRD v0.2` references are cited by decomposition/register rows but the PRD source text was not locally read in this task. Requirements must not exceed accessible SOW/decomposition wording.

#### Trade-offs

| Topic | Conservative posture |
|---|---|
| Embedded results vs references | Use the source-supported term "results" without deciding whether the schema embeds result payloads, references result envelopes, or supports both. Exact representation is TBD. |
| Hash granularity | Require explicit payload scope. Do not decide final partitioning for non-JSON or binary payloads; `docs/SPEC.md` leaves that TBD. |
| Rule-pack/library metadata depth | Preserve identity/provenance/checksum/reference metadata without copying private formulas, protected tables, proprietary values, or private payloads. |
| Status vocabulary | Use software status/diagnostic categories only within the professional-boundary model. Do not introduce automatic human approval or code-compliance statuses. |
| Comparison readiness | DEL-14-02 should not pre-solve DEL-14-04 comparison semantics. It should preserve enough run basis and result hash evidence to support deterministic comparison later. |

#### Examples

TBD. No approved example analysis-run payloads or fixture values are present in the accessible sources. Public examples must be invented or otherwise cleared for redistribution before use.

#### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| None identified | No direct source conflict was identified in the accessible source slices. Several details remain TBD because source text is absent or implementation-specific. | N/A | N/A | N/A | N/A | N/A |

## Component: execution/PKG-14_Model States, Analysis Runs, and Comparison/1_Working/DEL-14-02_Analysis run records/Procedure.md

### Procedure: DEL-14-02 Analysis run records

#### Purpose

This procedure describes how later Type 2 implementation work should produce and verify the DEL-14-02 analysis-run record artifacts from the current setup-stage sources. It is a production workflow guide, not evidence that implementation has already occurred.

#### Prerequisites

| Prerequisite | Status | Source |
|---|---|---|
| Accepted decomposition basis | Available: `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.7 | `_CONTEXT.md` |
| Deliverable identity and scope | Available: DEL-14-02, SOW-072, OBJ-016 | `_CONTEXT.md`; registers |
| Approved dependency evidence | Available as local DAG-002 mirror in `Dependencies.csv` | `_DEPENDENCIES.md`; `Dependencies.csv` |
| Architecture basis constraints | Available in `_CONTEXT.md`; exact package-specific implementation choices remain decision-gated | `_CONTEXT.md` |
| Field-level schema design | TBD | No accessible source defines final field names/cardinality. |
| Implementation code and tests | TBD | PREPARATION notes say no Type 2 implementation artifacts were drafted. |

#### Steps

1. Re-read `_CONTEXT.md`, `_REFERENCES.md`, `Dependencies.csv`, and the DEL-14-02 rows in the decomposition and registers.
2. Confirm that the work remains limited to DEL-14-02 and does not require protected standards text, private project data, or sibling deliverable edits.
3. Draft or update `schemas/analysis_run.schema.json` using JSON Schema 2020-12 conventions, subject to repository schema patterns available at implementation time.
4. Represent the SOW-072 binding categories: exact model state, solver version, solver/settings basis, units, load-case basis, diagnostics, results, rule-pack references, library references, and result hashes.
5. Mark unsupported field-level choices as TBD until a source, accepted architecture decision, or human ruling supports them.
6. Ensure unit-bearing values are unit-aware or produce explicit diagnostics for missing/ambiguous units.
7. Ensure hash records identify payload scope and canonicalization basis. Use the accepted JSON/JCS-compatible basis where JSON payloads are hashed.
8. Preserve professional-boundary constraints: do not generate approval, certification, sealing, authentication, or code-compliance labels as software statuses.
9. Preserve protected/private-data constraints: do not embed private formulas, protected standards text, protected tables, proprietary values, or private rule-pack/library payloads in public fixtures or examples.
10. Add run reproducibility tests covering stable serialization/hash behavior, binding to model-state/run basis, unit diagnostics, and professional-boundary status behavior.
11. Record remaining TBDs and assumptions in implementation notes or tests rather than silently defaulting engineering behavior.

#### Verification

| Check | Expected result |
|---|---|
| Source traceability | Requirements and tests cite accessible sources or mark unsupported details as TBD/ASSUMPTION. |
| Schema parse | `schemas/analysis_run.schema.json` parses and satisfies repository schema validation once implemented. |
| Binding coverage | Tests or schema review confirm all SOW-072 categories are present or explicitly referenced. |
| Reproducibility | Stable run-record payloads produce stable hashes under the selected canonicalization basis. |
| Unit handling | Missing unit metadata for unit-bearing values produces diagnostics rather than silent defaults. |
| Boundary controls | Statuses and examples avoid automatic professional approval/compliance claims and protected/private data leakage. |
| Dependency preservation | Existing DAG-002 mirror rows remain ACTIVE unless later CHANGE/RECONCILIATION authority changes them. |

#### Records

The implementation pass should leave:

- `schemas/analysis_run.schema.json`.
- Run reproducibility tests.
- Validation output for schema and tests.
- Notes for any TBD schema fields, hash partitions, migration behavior, or fixture policies.
- Protected-content/private-data review notes for public examples.
- Any dependency-register changes only if they preserve approved DAG-006 rows or have explicit human/change authority.

## Component: execution/PKG-14_Model States, Analysis Runs, and Comparison/1_Working/DEL-14-02_Analysis run records/Specification.md

### Specification: DEL-14-02 Analysis run records

#### Scope

DEL-14-02 defines the analysis-run record data model and the supporting reproducibility test surface for saving analysis runs as immutable, traceable product records.

In scope:

- `schemas/analysis_run.schema.json`.
- Run reproducibility tests.
- Data-model coverage for the SOW-072 binding categories: exact model states, solver versions, settings, units, load cases, diagnostics, results, rule-pack references, library references, and result hashes.
- Professional-boundary, unit, hash, provenance, protected-content, and private-data constraints that apply to persisted run records.

Out of scope:

- Comprehensive commercial prover output ingestion.
- External validation or professional acceptance decisions.
- Exact implementation code, storage container choice, dependency versions, solver numerical library, rule expression grammar/library, and public API transport.
- Field-level schema design beyond source-supported categories; unsupported details remain TBD.

#### Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| DEL-14-02-R001 | The deliverable shall produce or define `schemas/analysis_run.schema.json` as the analysis-run record schema artifact. | `_CONTEXT.md` anticipated artifacts; `docs/_Registers/Deliverables.csv` row DEL-14-02 | Artifact exists and is schema-validated once implementation occurs. |
| DEL-14-02-R002 | The analysis-run record shall bind each saved run to an exact model state reference. | SOW-072 in `docs/_Registers/ScopeLedger.csv`; `execution/_Decomposition/SOFTWARE_DECOMP.md` DEL-14-02 row | Schema contains a required model-state reference or equivalent validated binding. |
| DEL-14-02-R003 | The analysis-run record shall preserve solver version, solver/settings basis, units, load-case basis, diagnostics, results, rule-pack references, library references, and result hashes. | SOW-072; `_CONTEXT.md` scope detail | Schema inspection and reproducibility tests confirm the categories are present or explicitly referenced. |
| DEL-14-02-R004 | Results shall attach to immutable analysis-run records rather than only to mutable current model state. | `docs/_Registers/ScopeLedger.csv` row SOW-072; `_CONTEXT.md` envelope notes | Mutation/round-trip test demonstrates stored run evidence remains associated with the original run basis. |
| DEL-14-02-R005 | Unit-bearing physical values included or referenced by run records shall carry explicit unit metadata unless explicitly classified as dimensionless, ratio, percentage, or coefficient. | `docs/SPEC.md` section 4; `docs/CONTRACT.md` OPS-K-UNIT-1 | Schema validation and negative tests reject or diagnose missing unit metadata where required. |
| DEL-14-02-R006 | Missing solve-required or rule-check-required values shall be explicit findings with diagnostics and provenance, not silent defaults. | `docs/SPEC.md` analysis boundary section; `docs/CONTRACT.md` OPS-K-DATA-2 | Tests confirm missing required values produce structured diagnostics. |
| DEL-14-02-R007 | Hash records shall identify payload scope and use the accepted JSON/JCS-compatible canonical JSON basis where JSON payloads are hashed. | `_CONTEXT.md` architecture basis; `docs/SPEC.md` section 4.4 | Reproducibility tests compare canonical hash outputs for stable JSON payloads. |
| DEL-14-02-R008 | The record shall preserve the software authority boundary: solver results and diagnostics are software outputs; human acceptance is external and hash-bound. | `docs/SPEC.md` analysis boundary section; `docs/CONTRACT.md` OPS-K-AUTH-1 and OPS-K-AUTH-2 | Schema/status tests ensure automatic approval, certification, sealing, authentication, or code-compliance labels are not emitted. |
| DEL-14-02-R009 | Rule-pack and library references shall expose identity/provenance/checksum-style metadata where source-supported, without embedding protected standards text, protected tables, proprietary values, private formulas, or private payloads in public artifacts. | SOW-072; `docs/SPEC.md` result export section; `docs/IP_AND_DATA_BOUNDARY.md` | Protected-content/private-data tests inspect examples and fixtures before acceptance. |
| DEL-14-02-R010 | Run reproducibility tests shall be part of the deliverable output surface. | `_CONTEXT.md` anticipated artifacts | Test files exist and exercise stable run-record/hash behavior once implementation occurs. |
| DEL-14-02-R011 | The schema and tests shall remain compatible with schema-first command/query/job result-envelope architecture. | `_CONTEXT.md` architecture basis; `docs/SPEC.md` runner/result-envelope sections | Service/result-envelope integration tests or contract tests are added when implementation scope reaches that boundary. |

#### Standards

| Standard or governing basis | Status in this folder | Notes |
|---|---|---|
| JSON Schema 2020-12 contracts | Applicable architecture basis | `_CONTEXT.md` identifies JSON Schema 2020-12 contracts. Exact `$schema`, `$id`, and schema-module placement remain implementation TBD. |
| Canonical JSON / JCS-compatible hash basis | Applicable where JSON payloads are hashed | `_CONTEXT.md` and `docs/SPEC.md` support the basis. Exact library/dependency choice remains TBD. |
| PRD v0.2 sections 8.7 and 15.2 / FR-CMP-002 | Referenced but not locally accessible as primary source text | Decomposition and registers cite these references. Do not derive clause-level requirements beyond the accessible SOW-072 wording. |
| Protected-content and private-data governance | Applicable | `docs/CONTRACT.md` and `docs/IP_AND_DATA_BOUNDARY.md` govern public/private data handling. |
| Professional responsibility boundary | Applicable | `docs/CONTRACT.md` and `docs/SPEC.md` prohibit software-generated professional approval/compliance claims. |

#### Verification

| Verification target | Method | Acceptance signal |
|---|---|---|
| Schema artifact | JSON Schema validation and repository schema gate | `schemas/analysis_run.schema.json` parses and satisfies local schema conventions once implemented. |
| Required binding categories | Schema review plus tests | Model state, solver version/settings, units, load-case basis, diagnostics, results, rule-pack/library references, and result hashes are represented or explicitly referenced. |
| Immutability of run evidence | Round-trip/persistence test | A saved run remains bound to the original model-state/run basis after unrelated model changes. |
| Hash reproducibility | Deterministic canonicalization test | Equivalent canonical JSON payloads produce stable hashes; payload scope is recorded. |
| Unit safety | Negative and positive unit tests | Unit-bearing values include unit metadata or produce blocking diagnostics. |
| Professional boundary | Status/label tests | No automatic human approval, certification, sealing, authentication, or code-compliance label is emitted. |
| Protected/private data boundary | Protected-content and fixture review | Public examples do not embed private/protected rule, library, standards, or proprietary payload content. |

#### Documentation

Required or expected records for later implementation:

- `schemas/analysis_run.schema.json`.
- Run reproducibility tests.
- Schema-source notes for each binding category.
- Hash/reproducibility test notes, including payload scope.
- Unit and diagnostic test notes.
- Protected-content/private-data review notes for any public examples or fixtures.

All exact field names, object identities, schema `$id` values, migration behavior, and fixture values are TBD until supported by implementation work or human-approved design decisions.
