# Source Pack: SRC-DEL-DEL-14-05-COMPARISON-MAPPING-TOLERANCE-AND-EXPORT-CONTRACTS

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-14_Model States, Analysis Runs, and Comparison/1_Working/DEL-14-05_Comparison mapping, tolerance, and export contracts/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-14_Model States, Analysis Runs, and Comparison/1_Working/DEL-14-05_Comparison mapping, tolerance, and export contracts/Datasheet.md

### Datasheet: DEL-14-05 Comparison mapping, tolerance, and export contracts

#### Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-14-05 | `_CONTEXT.md` |
| Name | Comparison mapping, tolerance, and export contracts | `_CONTEXT.md` |
| Package ID | PKG-14 | `_CONTEXT.md` |
| Package | Model States, Analysis Runs, and Comparison | `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md#PKG-14` |
| Type | API_CONTRACT | `_CONTEXT.md` |
| Scope item | SOW-073 | `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md#SOW-073` |
| Primary objective | OBJ-016 | `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md#OBJ-016` |
| Context envelope | M | `_CONTEXT.md` |
| Anticipated artifacts | comparison mapping schema; tolerance profile schema; comparison exporters | `_CONTEXT.md` |

#### Attributes

| Attribute | Current value |
|---|---|
| Contract subject | Manual comparison mappings, unmatched classifications, tolerance profiles, and CSV/JSON/report-section export semantics. Source: `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md#DEL-14-05`. |
| Comparison basis | Two model states and/or two analysis runs are compared deterministically using stable IDs, manual mappings where required, unit-normalized result deltas, and tolerance profiles. Source: `execution/_Decomposition/SOFTWARE_DECOMP.md#SOW-073`. |
| State/run context | Model states and analysis runs are first-class product records for design iteration and review. Source: `execution/_Decomposition/SOFTWARE_DECOMP.md#OBJ-016`. |
| Export boundary | Result export envelopes identify result set, model/run basis, solver version, unit-system reference, diagnostics, provenance, hashes or audit manifest reference, analysis statuses, and professional-boundary notice. Source: `docs/SPEC.md#result-export-format`. |
| Unit boundary | Calculations, formulas, imported values, and exports must be unit-aware and dimensionally checked. Source: `docs/CONTRACT.md#OPS-K-UNIT-1`. |
| Professional boundary | Comparison output is diagnostic/audit functionality, not automatic external validation or acceptance. Source: `execution/_Decomposition/SOFTWARE_DECOMP.md#SOW-073`; `docs/TYPES.md#TraceabilityLink`. |
| Public data boundary | Public artifacts must not copy private formulas, protected standards text, protected tables, proprietary values, or private rule-pack payloads. Source: `docs/SPEC.md#result-export-format`; `docs/IP_AND_DATA_BOUNDARY.md#public-repository-must-not-contain`. |
| Architecture basis | JSON Schema 2020-12 contracts, schema-first envelopes, and canonical JSON/JCS-compatible hash basis apply where payloads are hashed. Source: `_CONTEXT.md#Architecture-Basis-Injection`. |

#### Conditions

| Condition | Status |
|---|---|
| Tolerance defaults | TBD. `execution/_Decomposition/SOFTWARE_DECOMP.md#OI-014` states comparison tolerance defaults and mapping workflows are pending solver/result schema prototypes. |
| Exact CSV fields | TBD. DEL-14-05 is assigned CSV export semantics, but the accessible sources do not define field names or column order. |
| Exact JSON schema | TBD. The baseline is schema-first JSON, but the accessible sources do not include a deliverable-specific schema body. |
| Report-section layout | TBD. Report sections must preserve privacy, provenance, units, diagnostics, limitations, and professional-boundary notices; final rendering and layout remain outside the accessible source slice. |
| External validation | Excluded. PKG-14 does not ingest commercial prover outputs comprehensively or determine external validation. Source: `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md#PKG-14`. |
| Protected standards data | Excluded from public artifacts unless separately authorized by provenance and review. Source: `docs/CONTRACT.md#OPS-K-IP-1`; `docs/IP_AND_DATA_BOUNDARY.md#public-repository-must-not-contain`. |

#### Construction

| Construct | Description |
|---|---|
| Comparison mapping schema | Defines stable-ID mapping records and manual mapping evidence needed when state/run entities do not align automatically. Details remain TBD pending DEL-14-03/DEL-14-04 interfaces. |
| Unmatched classification schema | Defines explicit classifications for compared entities or results that have no accepted counterpart. Specific enum values are TBD unless later source material supplies them. |
| Tolerance profile schema | Defines unit-aware tolerance profile records for comparison deltas. Default numeric values are TBD and must not be silently supplied. |
| JSON export contract | Schema-first result/comparison envelope compatible with governed downstream tooling and report consumption. Exact schema fields are TBD. |
| CSV export contract | Tabular export semantics for comparison review. Exact columns, ordering, and serialization rules are TBD. |
| Report-section contract | Report-facing comparison section references that preserve units, diagnostics, provenance, hashes, assumptions, limitations, and professional-boundary notice. Exact layout is TBD. |

#### References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- `Dependencies.csv`
- `execution/_Decomposition/SOFTWARE_DECOMP.md`
- `docs/CONTRACT.md`
- `docs/TYPES.md`
- `docs/SPEC.md`
- `docs/IP_AND_DATA_BOUNDARY.md`
- `docs/DIRECTIVE.md`
- `execution/_DAG/DAG-006/APPROVAL_RECORD.md`

## Component: execution/PKG-14_Model States, Analysis Runs, and Comparison/1_Working/DEL-14-05_Comparison mapping, tolerance, and export contracts/Guidance.md

### Guidance: DEL-14-05 Comparison mapping, tolerance, and export contracts

#### Purpose

DEL-14-05 exists to define the comparison-facing contracts that let model-state and analysis-run comparison results be mapped, interpreted with tolerances, and exported for review without turning diagnostic comparison output into professional approval or external validation.

Sources: `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md#DEL-14-05`; `execution/_Decomposition/SOFTWARE_DECOMP.md#SOW-073`.

#### Principles

| Principle | Guidance |
|---|---|
| Deterministic identity first | Stable IDs are the baseline for comparison. Manual mapping should be explicit evidence where stable-ID alignment is insufficient. Source: `execution/_Decomposition/SOFTWARE_DECOMP.md#SOW-073`. |
| Missing values stay visible | Tolerance defaults, mapping workflow details, and exact export field sets remain `TBD` where sources do not define them. Do not substitute engineering defaults. Source: `docs/CONTRACT.md#OPS-K-DATA-2`; `execution/_Decomposition/SOFTWARE_DECOMP.md#OI-014`. |
| Units are contract data | Unit-normalized deltas still need explicit unit/dimensional metadata or diagnostics. Source: `docs/CONTRACT.md#OPS-K-UNIT-1`; `docs/SPEC.md#result-export-format`. |
| Export is review evidence | Exports should carry enough context for review, regression comparison, report consumption, and downstream tooling without claiming external validation. Source: `docs/SPEC.md#result-export-format`; `execution/_Decomposition/SOFTWARE_DECOMP.md#SOW-073`. |
| Professional authority remains human | Avoid terms or statuses that imply software certification, sealing, professional approval, authentication, or code compliance. Source: `docs/CONTRACT.md#OPS-K-AUTH-1`; `docs/TYPES.md#Analysis-status-vocabulary`. |
| Public artifacts stay clean | Public examples and contract documentation must not embed protected standards text, protected tables, code-specific values, proprietary data, or private rule-pack payloads. Source: `docs/IP_AND_DATA_BOUNDARY.md#public-repository-must-not-contain`. |

#### Considerations

- The comparison mapping contract depends on upstream model-state and analysis-run identity surfaces. The local approved DAG-006 mirror records upstream dependencies on DEL-14-01 and DEL-14-02.
- Unit-aware tolerance behavior depends on the unit-system contract. The local approved DAG-006 mirror records an upstream dependency on DEL-02-02.
- Export semantics should remain compatible with result export envelopes. The local approved DAG-006 mirror records an upstream dependency on DEL-08-04.
- Architecture basis rows in the local mirror are context evidence, not independent Type 2 dispatch authority.
- The accessible sources do not define exact mapping enums, unmatched classification values, tolerance formulas, tolerance default values, CSV columns, JSON property names, or report-section layout. These remain `TBD`.

#### Trade-offs

| Trade-off | Direction |
|---|---|
| Strict schema versus future external result states | Prefer schema-first contracts with explicit extension/TBD slots because `_CONTEXT.md` notes that future external result states may be represented without changing core compare logic. |
| Human readability versus machine validation | Preserve both reviewable export forms and schema validation hooks; exact CSV/report fields remain TBD until contract details are sourced. |
| Default tolerances versus no silent defaults | Keep defaults TBD unless a future governed source supplies them. Silent tolerances would conflict with the no-silent-defaults principle. |
| Broad external comparison support versus bounded MVP | Stay within deterministic state/run comparison and comparison export semantics; comprehensive commercial prover ingestion is excluded by PKG-14. |

#### Examples

TBD. No locally accessible source provides approved example mappings, tolerance profiles, CSV rows, JSON payloads, or report-section examples for DEL-14-05.

#### Conflict Table (for human ruling)

No source conflict requiring human ruling was identified during the P1/P2 setup pass. The main unresolved items are source gaps, recorded as `TBD`: tolerance defaults, mapping workflow details, exact export fields, and report-section layout.

## Component: execution/PKG-14_Model States, Analysis Runs, and Comparison/1_Working/DEL-14-05_Comparison mapping, tolerance, and export contracts/Procedure.md

### Procedure: DEL-14-05 Comparison mapping, tolerance, and export contracts

#### Purpose

This procedure describes how to produce and verify the DEL-14-05 contract artifacts using only the current governed source basis. It is a setup-stage production procedure, not an implementation procedure for runtime comparison code.

#### Prerequisites

| Prerequisite | Source |
|---|---|
| Deliverable context for DEL-14-05 is present and readable. | `_CONTEXT.md` |
| Accepted SOFTWARE_DECOMP revision 0.7 is available. | `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md` |
| Governing project invariants are available. | `_REFERENCES.md`; `docs/CONTRACT.md`; `docs/TYPES.md`; `docs/SPEC.md`; `docs/IP_AND_DATA_BOUNDARY.md`; `docs/DIRECTIVE.md` |
| Approved DAG-002 local mirror is present and preserved. | `_DEPENDENCIES.md`; `Dependencies.csv`; `execution/_DAG/DAG-006/APPROVAL_RECORD.md` |
| Upstream architecture basis rows remain context evidence only. | `_CONTEXT.md#Architecture-Basis-Injection`; `_DEPENDENCIES.md#Authority-Boundary` |

Approved local dependency mirror, summarized:

- architecture basis: DEL-00-01, DEL-00-02, DEL-00-03, DEL-00-04, DEL-00-06, DEL-00-07, DEL-00-08;
- state/run prerequisites: DEL-14-01 and DEL-14-02;
- result export prerequisite: DEL-08-04;
- unit contract prerequisite: DEL-02-02.

#### Steps

1. Confirm scope identity from `_CONTEXT.md`: DEL-14-05, PKG-14, API_CONTRACT, SOW-073, OBJ-016.
2. Confirm decomposition scope from `execution/_Decomposition/SOFTWARE_DECOMP.md`: DEL-14-05 defines manual mappings, unmatched classifications, tolerance profiles, and CSV/JSON/report-section export semantics.
3. Record exclusions before defining contract details: no comprehensive commercial prover result ingestion, no external validation decision, no professional approval state, and no protected/private data in public artifacts.
4. Define the comparison mapping schema surface at a contract level:
   - stable source and target references;
   - manual mapping evidence/provenance;
   - relation to model-state and analysis-run comparison outputs;
   - unresolved fields marked `TBD`.
5. Define the unmatched classification surface:
   - explicit classification slot for entities/results without an accepted counterpart;
   - specific enum values marked `TBD` unless later source material supplies them.
6. Define the tolerance profile surface:
   - unit-aware comparison quantities and delta interpretation;
   - required unit/dimensional metadata;
   - tolerance default values marked `TBD`.
7. Define JSON export semantics:
   - schema-first envelope basis;
   - result set, model/run basis, solver version, unit-system reference, diagnostics, provenance, hashes or audit-manifest reference, analysis statuses, and professional-boundary notice;
   - exact fields marked `TBD`.
8. Define CSV export semantics:
   - parseable tabular representation for comparison review;
   - no protected standards text, proprietary values, private project data, or private rule-pack payloads;
   - columns and ordering marked `TBD`.
9. Define report-section export semantics:
   - report-facing comparison evidence, limitations, diagnostics, assumptions, and professional-boundary notice;
   - final layout marked `TBD`.
10. Verify the resulting contract draft against unit safety, data-boundary, professional-boundary, and no-silent-defaults invariants.
11. Preserve approved DAG-006 mirror rows as ACTIVE. Do not delete, retire, or reclassify them during setup handling.

#### Verification

| Check | Expected result |
|---|---|
| Scope check | Contract content is limited to DEL-14-05 and does not implement DEL-14-03 or DEL-14-04 engines. |
| Source-grounding check | Non-trivial requirements cite `_CONTEXT.md`, `_REFERENCES.md`, decomposition, local dependency mirror, or referenced governance docs. |
| TBD check | Unsupported details are marked `TBD` or `ASSUMPTION`; no engineering values are invented. |
| Unit check | Unit-bearing comparison/export values are specified as unit-aware or diagnostic-producing. |
| Boundary check | No professional approval, certification, code-compliance, or external-validation claim is introduced. |
| IP/privacy check | No protected standards content, proprietary data, private project data, or private rule-pack payload is embedded. |
| Dependency mirror check | Existing approved DAG-006 rows remain present and ACTIVE. |

#### Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_SEMANTIC.md`
- `_SEMANTIC_LENSING.md`
- `Dependencies.csv`
- `_DEPENDENCIES.md`
- `_STATUS.md`

## Component: execution/PKG-14_Model States, Analysis Runs, and Comparison/1_Working/DEL-14-05_Comparison mapping, tolerance, and export contracts/Specification.md

### Specification: DEL-14-05 Comparison mapping, tolerance, and export contracts

#### Scope

This deliverable defines API/data contracts for comparison mappings, unmatched classifications, tolerance profiles, and comparison exports for model-state and analysis-run comparisons.

In scope:

- comparison mapping schema;
- tolerance profile schema;
- comparison exporters for CSV, JSON, and report-section use;
- explicit `TBD` handling for unresolved tolerance defaults, mapping workflows, exact field names, and export layout.

Out of scope:

- implementation of the model-state comparison engine owned by DEL-14-03;
- implementation of the analysis-run comparison engine owned by DEL-14-04;
- comprehensive commercial prover result ingestion;
- external validation or professional approval;
- protected standards text, protected tables, proprietary values, private rule-pack payloads, or code-specific tolerance defaults.

Sources: `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md#DEL-14-05`; `execution/_Decomposition/SOFTWARE_DECOMP.md#PKG-14`; `docs/IP_AND_DATA_BOUNDARY.md#public-repository-must-not-contain`.

#### Requirements

| Req ID | Requirement | Source |
|---|---|---|
| DEL-14-05-R001 | The contract shall support deterministic comparison of two model states and/or two analysis runs using stable IDs. | `execution/_Decomposition/SOFTWARE_DECOMP.md#SOW-073` |
| DEL-14-05-R002 | The mapping schema shall represent manual mappings where automatic stable-ID alignment is insufficient. | `_CONTEXT.md#Description`; `execution/_Decomposition/SOFTWARE_DECOMP.md#SOW-073` |
| DEL-14-05-R003 | The contract shall represent unmatched classifications for compared entities or results that lack an accepted counterpart. Specific classification values are TBD. | `_CONTEXT.md#Description`; `_CONTEXT.md#Anticipated-Artifacts` |
| DEL-14-05-R004 | The tolerance profile schema shall support unit-normalized result deltas and tolerance profiles without silently supplying default engineering values. Numeric defaults are TBD. | `execution/_Decomposition/SOFTWARE_DECOMP.md#SOW-073`; `execution/_Decomposition/SOFTWARE_DECOMP.md#OI-014`; `docs/CONTRACT.md#OPS-K-DATA-2` |
| DEL-14-05-R005 | Export contracts shall preserve explicit unit and dimensional metadata for unit-bearing values or produce blocking diagnostics when required unit metadata is missing. | `docs/CONTRACT.md#OPS-K-UNIT-1`; `docs/SPEC.md#result-export-format` |
| DEL-14-05-R006 | JSON export semantics shall align with the schema-first result-envelope baseline. Exact deliverable-specific JSON fields are TBD. | `_CONTEXT.md#Architecture-Basis-Injection`; `docs/SPEC.md#result-export-format` |
| DEL-14-05-R007 | CSV export semantics shall be specified without embedding protected standards data, proprietary engineering values, private project data, or private rule-pack payloads. Exact columns are TBD. | `_CONTEXT.md#Description`; `docs/IP_AND_DATA_BOUNDARY.md#public-repository-must-not-contain`; `docs/SPEC.md#result-export-format` |
| DEL-14-05-R008 | Report-section export semantics shall preserve diagnostics, provenance, hashes or audit-manifest references, analysis statuses, limitations, and professional-boundary notices. Layout is TBD. | `docs/SPEC.md#result-export-format`; `docs/SPEC.md#report-boundary`; `docs/CONTRACT.md#OPS-K-REPORT-1` |
| DEL-14-05-R009 | The contracts shall not claim certification, sealing, approval, authentication, external validation, or code compliance. | `docs/CONTRACT.md#OPS-K-AUTH-1`; `execution/_Decomposition/SOFTWARE_DECOMP.md#SOW-073` |
| DEL-14-05-R010 | Public artifacts shall not bundle protected standards text, protected tables, code-specific acceptance criteria, proprietary values, or private user data. | `docs/CONTRACT.md#OPS-K-IP-1`; `docs/IP_AND_DATA_BOUNDARY.md#public-repository-must-not-contain` |
| DEL-14-05-R011 | The contract shall remain compatible with model-state records, analysis-run records, result export envelopes, and unit-system contracts identified as upstream dependency evidence. | `Dependencies.csv`; `_DEPENDENCIES.md` |

#### Standards

| Standard or governance source | Applicability | Status |
|---|---|---|
| JSON Schema 2020-12 | Schema-first contract basis where JSON contracts are materialized. | Source: `_CONTEXT.md#Architecture-Basis-Injection`. |
| Chirality/OpenPipeStress lifecycle vocabulary | Deliverable state and draft/proposal status. | Source: `docs/TYPES.md#Lifecycle-states`; `docs/CONTRACT.md#OPS-K-AGENT-4`. |
| OpenPipeStress unit boundary | Unit-aware, dimensionally checked values and exports. | Source: `docs/CONTRACT.md#OPS-K-UNIT-1`; `docs/SPEC.md#unit-system-and-dimensional-analysis`. |
| OpenPipeStress IP/data boundary | Protected/private data exclusion for public artifacts. | Source: `docs/IP_AND_DATA_BOUNDARY.md`. |
| Professional responsibility boundary | Software output is decision support and not professional approval. | Source: `docs/CONTRACT.md#OPS-K-AUTH-1`; `docs/DIRECTIVE.md#Human-authority`. |

No external engineering standard text is locally provided as an authoritative source for this deliverable. Any code- or owner-standard-derived tolerance or acceptance rule is `TBD` unless later supplied through a governed private/user data path.

#### Verification

| Requirement | Verification approach |
|---|---|
| DEL-14-05-R001 | Determinism tests comparing equivalent input states/runs once DEL-14-03 and DEL-14-04 interfaces exist. Current status: TBD. |
| DEL-14-05-R002 | Schema validation for manual mapping records, including stable source/target references and evidence/provenance fields. Current status: TBD. |
| DEL-14-05-R003 | Schema validation for unmatched classifications once enum values are human-approved or source-defined. Current status: TBD. |
| DEL-14-05-R004 | Unit-aware tolerance-profile validation with missing default values treated as explicit findings. Current status: TBD. |
| DEL-14-05-R005 | Unit/dimension validation for exported comparison values. Current status: TBD. |
| DEL-14-05-R006 | JSON Schema validation against the deliverable schema after the schema body is created. Current status: TBD. |
| DEL-14-05-R007 | CSV parse/round-trip checks after column set and ordering are defined. Current status: TBD. |
| DEL-14-05-R008 | Report-section fixture checks for provenance, diagnostics, hashes, limitations, and professional-boundary notices. Current status: TBD. |
| DEL-14-05-R009 | Protected wording/professional-claim review checking for prohibited approval/compliance language. Current status: TBD. |
| DEL-14-05-R010 | Protected-content/private-data lint or review gate. Current status: TBD. |
| DEL-14-05-R011 | Dependency closure review against the approved local DAG-002 mirror. Current status: mirror present; closure not independently reclassified by this deliverable. |

#### Documentation

Required records for later implementation work:

- comparison mapping schema documentation;
- tolerance profile schema documentation;
- JSON export contract documentation;
- CSV export contract documentation;
- report-section export contract documentation;
- unresolved `TBD` register for tolerance defaults, mapping workflows, exact fields, and export layout;
- dependency evidence record preserving the approved DAG-006 mirror rows.
