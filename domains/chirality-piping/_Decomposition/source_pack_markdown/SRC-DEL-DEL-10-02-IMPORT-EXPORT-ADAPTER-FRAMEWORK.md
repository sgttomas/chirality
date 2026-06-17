# Source Pack: SRC-DEL-DEL-10-02-IMPORT-EXPORT-ADAPTER-FRAMEWORK

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-10_Build, Packaging, API, and Interoperability/1_Working/DEL-10-02_Import-export adapter framework/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-10_Build, Packaging, API, and Interoperability/1_Working/DEL-10-02_Import-export adapter framework/Datasheet.md

### Datasheet: DEL-10-02 Import/export adapter framework

#### Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-10-02 |
| Name | Import/export adapter framework |
| Package ID | PKG-10 |
| Package | Build, Packaging, API, and Interoperability |
| Type | BACKEND_FEATURE_SLICE |
| Scope item | SOW-030 |
| Objective | OBJ-009 |
| Context envelope | L |
| Current production mode | Setup documentation only |

#### Attributes

| Attribute | Value |
|---|---|
| Deliverable purpose | Define the framework obligations for future import/export adapters. |
| Anticipated artifacts | Adapter interfaces; sample invented adapter. |
| Setup-run artifact boundary | This session produces setup documents and registers only; adapter source, tests, sample adapters, manifests, and repo-level artifacts are out of write scope. |
| Architecture baseline | Schema-first command/query/job result envelopes; JSON Schema 2020-12 contracts; canonical JSON/JCS-compatible hashing where JSON payloads are hashed. |
| Adapter boundary | Adapters may translate external data but cannot bypass units, provenance, redistribution, diagnostics, private/public data controls, validation, sandboxing, envelopes, or report controls. |
| External format list | TBD; concrete protected or proprietary external formats are not bundled defaults in this deliverable. |
| Public API transport | TBD; public transport protocol remains a later human/product decision. |

#### Conditions

| Condition | Source |
|---|---|
| All import/export operations must be unit-aware and deterministically report unit conversions. | docs/PRD.md section 6.6; docs/CONTRACT.md OPS-K-UNIT-1 |
| Imported data must flag missing required fields, missing or inconsistent units, missing provenance, unclear redistribution status, protected-table risk, and user-defined reasonableness concerns. | docs/PRD.md section 13.5 |
| Private rule packs, component libraries, material data, project files, and calculation results must not be transmitted or exported unexpectedly. | docs/PRD.md sections 18.2 and 18.3; docs/CONTRACT.md OPS-K-PRIV-1 |
| Adapter outputs for nontrivial operations use diagnostics/result envelopes and must not make certification or compliance claims. | execution/_Decomposition/SOFTWARE_DECOMP.md AB-00-06; docs/CONTRACT.md OPS-K-AUTH-1 |
| Adapter interfaces remain code-neutral and do not bundle protected standards data or proprietary tool behavior. | INIT.md; docs/DIRECTIVE.md; docs/IP_AND_DATA_BOUNDARY.md |

#### Construction

The future framework should be described as a shell around import/export providers, not as concrete bundled adapters. Required conceptual pieces are:

- adapter identity and capability metadata;
- import and export request envelopes;
- unit-validation hooks before data enters domain workflows;
- provenance and redistribution-status validation;
- diagnostics and warning emission using project warning classes;
- private/public data boundary checks before writing exported payloads;
- rule-pack and report hooks that preserve sandboxing and report controls;
- manifest/hash hooks for reproducible imported and exported artifacts.

#### References

- INIT.md
- AGENTS.md
- docs/DIRECTIVE.md
- docs/CONTRACT.md
- docs/TYPES.md
- docs/SPEC.md
- docs/IP_AND_DATA_BOUNDARY.md
- docs/PRD.md
- execution/_Decomposition/SOFTWARE_DECOMP.md
- docs/_Registers/Deliverables.csv
- docs/_Registers/ScopeLedger.csv
- docs/_Registers/ContextBudgetQA.csv
- execution/PKG-00_Software Architecture Runway/1_Working/DEL-00-03_Application service command-query-job model/Specification.md
- execution/PKG-00_Software Architecture Runway/1_Working/DEL-00-06_Diagnostics, warning, and result-envelope contract/Specification.md
- execution/PKG-00_Software Architecture Runway/1_Working/DEL-00-07_API boundary and adapter contract map/Specification.md
- execution/PKG-00_Software Architecture Runway/1_Working/DEL-00-08_Layered software test and acceptance strategy/Specification.md

## Component: execution/PKG-10_Build, Packaging, API, and Interoperability/1_Working/DEL-10-02_Import-export adapter framework/Guidance.md

### Guidance: DEL-10-02 Import/export adapter framework

#### Purpose

This deliverable prepares the import/export adapter framework so later implementation work can add adapters without weakening OpenPipeStress governance boundaries. The framework is an extension surface, not a route around domain validation, unit safety, provenance, rule-pack sandboxing, reporting controls, or professional-responsibility limits.

#### Principles

- Treat adapters as translators at the edge of the application service boundary.
- Require schema-first envelopes for nontrivial import/export operations.
- Validate units and dimensional meaning before external data becomes domain data.
- Preserve source/provenance, redistribution status, and private/public data markings.
- Emit diagnostics for missing fields, missing provenance, unclear redistribution, suspected protected content, unit inconsistencies, and private-data export risk.
- Keep concrete format support `TBD` until a human decision records the external format, license posture, redistribution status, and test obligations.
- Use invented data only for public samples.

#### Considerations

An adapter may be technically able to parse many files, but parsing does not establish redistribution rights, engineering suitability, code compliance, or professional acceptance. The framework should therefore separate:

- syntactic parse success;
- schema and unit validation;
- provenance and redistribution review;
- mechanics-readiness;
- rule-check-readiness;
- human-review-needed state.

Adapters that import private material libraries, component records, rule-pack references, or project data should default to local/private handling. Export operations should warn before writing private or protected-suspected values to shared payloads.

#### Trade-offs

| Trade-off | Guidance |
|---|---|
| Flexible adapter ecosystem vs. governance control | Favor a narrow framework with mandatory validation hooks; add format-specific adapters later. |
| User convenience vs. data provenance | Missing source or redistribution status is a finding, not an auto-filled default. |
| Broad public formats vs. IP safety | Do not bundle protected or proprietary defaults without documented rights and human approval. |
| Fast export vs. auditability | Exports should carry diagnostics, hashes/manifests where applicable, and warning state. |

#### Examples

- Acceptable public sample: an invented adapter that imports a small invented component record with invented dimensions, invented source metadata, and permissive redistribution marked as invented/original.
- Not acceptable public sample: a bundled adapter fixture copied from a standards table, vendor catalog, commercial software example, or private project library without documented redistribution rights.

#### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| None | No current conflicts detected in setup sources. | NA | NA | NA | NA | TBD |

## Component: execution/PKG-10_Build, Packaging, API, and Interoperability/1_Working/DEL-10-02_Import-export adapter framework/Procedure.md

### Procedure: DEL-10-02 Import/export adapter framework

#### Purpose

Define how a future implementation agent should produce the import/export adapter framework while preserving the sealed scope and governance boundaries recorded for `DEL-10-02`.

#### Prerequisites

- Confirm the sealed brief authorizes implementation work beyond this setup/document production run.
- Read `_CONTEXT.md`, `Specification.md`, and the applicable `AB-00-*` architecture basis rows.
- Confirm the write scope before creating adapter source, tests, sample adapters, package manifests, or repo-level artifacts.
- Confirm whether the target work is framework-only or a concrete external format. Concrete external format selection requires human approval if not already recorded.

#### Steps

1. Identify the adapter operation types needed by the authorized implementation slice: import, export, validation, diagnostics, manifest/hash, rule-pack hook, report hook, and private-data boundary check.
2. Define adapter metadata fields for identity, capability, supported direction, supported payload class, source/provenance requirements, redistribution posture, and privacy behavior.
3. Route nontrivial adapter operations through schema-first command/query/job result envelopes.
4. Add unit-validation hooks before imported values can become domain objects.
5. Add provenance and redistribution-status validation before imported data can be accepted for reuse or public contribution.
6. Add diagnostics for missing fields, invalid units, missing provenance, unclear redistribution, protected-content suspicion, private-data export risk, and failed reasonableness checks.
7. Add rule-pack hooks only through the sandboxed, unit-aware rule-pack boundary; do not allow adapters to execute arbitrary rule code.
8. Add report/export hooks that preserve warnings, assumptions, limitations, provenance, and professional-responsibility notices.
9. Keep specific external formats, commercial tool behavior, public API transport, and package/container details as `TBD` unless a human ruling is cited.
10. Use invented data only for public sample adapters or fixtures.

#### Verification

- Verify no protected standards text, copied tables, proprietary examples, or private project data are introduced.
- Verify missing required data and missing provenance produce diagnostics rather than defaults.
- Verify unit-bearing imported/exported values are dimensionally checked.
- Verify private-boundary checks run before shared exports.
- Verify result envelopes do not claim certification, approval, sealing, or automatic code compliance.
- Verify tests and examples use invented or otherwise redistributable data with provenance.

#### Records

Future implementation work should record:

- interface files and schema contracts created;
- adapter validation tests and diagnostics tests;
- provenance/protected-content gate results;
- external format decisions and human approval references when applicable;
- open `TBD` decisions that remain after implementation.

## Component: execution/PKG-10_Build, Packaging, API, and Interoperability/1_Working/DEL-10-02_Import-export adapter framework/Specification.md

### Specification: DEL-10-02 Import/export adapter framework

#### Scope

This specification covers the setup definition for the future import/export adapter framework under `DEL-10-02`. It establishes adapter-interface obligations, validation hooks, governance boundaries, and acceptance checks. It does not implement adapter source code, sample adapters, tests, external format support, package manifests, public API transport, or repo-level artifacts.

Concrete import/export formats remain `TBD`. Protected standards data, proprietary commercial formats, copied code tables, proprietary examples, and private user libraries are not bundled defaults.

#### Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| REQ-10-02-01 | The adapter framework shall operate through schema-first command/query/job result envelopes and shall not bypass the public API/plugin boundary. | execution/_Decomposition/SOFTWARE_DECOMP.md AB-00-03 and AB-00-07 | Review adapter-interface design before implementation. |
| REQ-10-02-02 | Every import path shall validate units before accepting external data into domain workflows. | docs/PRD.md section 6.6; docs/CONTRACT.md OPS-K-UNIT-1 | Unit-validation test plan in future implementation. |
| REQ-10-02-03 | Every import path shall capture source/provenance, license or redistribution status, and review disposition for data records that may be contributed publicly or reused. | docs/CONTRACT.md OPS-K-IP-2; docs/IP_AND_DATA_BOUNDARY.md section 4 | Provenance-field checks in future implementation. |
| REQ-10-02-04 | Imported records with missing required fields, inconsistent units, missing provenance, unclear redistribution status, suspected protected origin, or out-of-range user checks shall produce diagnostics rather than silent defaults. | docs/PRD.md section 13.5; docs/CONTRACT.md OPS-K-DATA-2 | Diagnostic coverage review. |
| REQ-10-02-05 | Export paths shall check private/public data boundary status before writing payloads that may leave the local project context. | docs/PRD.md section 18.3; docs/CONTRACT.md OPS-K-PRIV-1 | Export-boundary checklist in future implementation. |
| REQ-10-02-06 | Adapter diagnostics shall include code, class, severity, source, affected object, message, remediation, and provenance when applicable. | execution/_Decomposition/SOFTWARE_DECOMP.md AB-00-06 | Result-envelope schema review. |
| REQ-10-02-07 | Adapter hooks for rule packs shall preserve rule-pack sandboxing, unit awareness, versioning, checksums, and public/private status. | docs/CONTRACT.md OPS-K-RULE-1 through OPS-K-RULE-3; execution/_Decomposition/SOFTWARE_DECOMP.md AB-00-07 | Rule-hook boundary review. |
| REQ-10-02-08 | Adapter hooks for reports shall preserve report warnings, assumptions, provenance, limitations, protected-content controls, and professional-responsibility notices. | docs/CONTRACT.md OPS-K-REPORT-1, OPS-K-REPORT-2, OPS-K-AUTH-1 | Report-boundary review. |
| REQ-10-02-09 | The framework shall not choose protected external formats, proprietary tool behavior, or specific commercial integration defaults without human approval and documented redistribution rights. | docs/IP_AND_DATA_BOUNDARY.md; execution/_Decomposition/SOFTWARE_DECOMP.md OI-004 and DEC-012 | Human decision log required before format selection. |
| REQ-10-02-10 | The framework shall leave mechanics solve, user-rule check, and professional approval states distinct in all adapter result payloads. | docs/TYPES.md section 4; docs/CONTRACT.md OPS-K-AUTH-1 | Status-field review in future interface artifacts. |

#### Standards

No external engineering code or proprietary format standard is incorporated by this setup artifact. Applicable project standards are internal governance invariants:

- OPS-K-IP-1, OPS-K-IP-2, OPS-K-IP-3
- OPS-K-DATA-1, OPS-K-DATA-2, OPS-K-DATA-3
- OPS-K-UNIT-1
- OPS-K-RULE-1, OPS-K-RULE-2, OPS-K-RULE-3
- OPS-K-PRIV-1, OPS-K-PRIV-2
- OPS-K-AUTH-1
- OPS-K-AGENT-1 through OPS-K-AGENT-4

#### Verification

Future implementation verification should include:

- schema validation for adapter request/result envelopes;
- unit conversion and dimensional-consistency tests;
- provenance and redistribution-status rejection/flagging tests;
- private-data export-warning tests;
- protected-content/provenance gates for public examples and fixtures;
- diagnostics envelope tests for import, export, and failed validation paths;
- rule-pack hook tests proving adapters cannot execute arbitrary rule code or bypass evaluator sandboxing;
- report-boundary tests proving exports do not suppress warnings, limitations, or professional-responsibility notices.

#### Documentation

Required future artifacts remain:

- adapter interfaces;
- sample invented adapter using invented, non-code, non-proprietary data only.

This setup run does not create those implementation artifacts.
