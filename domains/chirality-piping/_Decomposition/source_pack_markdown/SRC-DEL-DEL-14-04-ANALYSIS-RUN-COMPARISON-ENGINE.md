# Source Pack: SRC-DEL-DEL-14-04-ANALYSIS-RUN-COMPARISON-ENGINE

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-14_Model States, Analysis Runs, and Comparison/1_Working/DEL-14-04_Analysis-run comparison engine/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-14_Model States, Analysis Runs, and Comparison/1_Working/DEL-14-04_Analysis-run comparison engine/Datasheet.md

### Datasheet: DEL-14-04 Analysis-run comparison engine

**Generated:** 2026-05-03
**Document Role:** Descriptive
**Source Basis:** `_CONTEXT.md`, `_REFERENCES.md`, `Dependencies.csv`, `execution/_Decomposition/SOFTWARE_DECOMP.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/IP_AND_DATA_BOUNDARY.md`

#### Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-14-04 | `_CONTEXT.md` |
| Name | Analysis-run comparison engine | `_CONTEXT.md` |
| Package ID | PKG-14 | `_CONTEXT.md` |
| Package name | Model States, Analysis Runs, and Comparison | `_CONTEXT.md` |
| Type | BACKEND_FEATURE_SLICE | `_CONTEXT.md`; `docs/_Registers/Deliverables.csv` |
| Scope items | SOW-073, SOW-072 | `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md` |
| Objective support | OBJ-016 | `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md` |
| Anticipated artifacts | run comparison engine; result delta tests | `_CONTEXT.md`; `docs/_Registers/Deliverables.csv` |

#### Attributes

| Attribute | Recorded Value |
|---|---|
| Primary function | Implement unit-normalized result deltas for mapped entities, diagnostics, and settings. |
| Comparison subject | Analysis runs and/or model states, as bounded by SOW-073; this deliverable focuses on analysis-run comparison. |
| Required comparison basis | Stable IDs, manual mappings where required, unit-normalized result deltas, and tolerance profiles. |
| Analysis-run basis | Exact model states, solver versions, settings, units, load cases, diagnostics, results, rule-pack references, library references, and result hashes. |
| Entity/result coverage | Mapped nodes, elements, supports, terminals, stress/result locations, diagnostics, and settings. |
| Role boundary | Diagnostic/audit functionality only; not automatic external validation, professional approval, certification, sealing, authentication, or code-compliance determination. |
| Architecture basis | Rust core/application services; schema-first command/query/job result envelopes; JSON Schema 2020-12; JCS-compatible hash basis for JSON payloads when hashed; Cargo/Vitest/Playwright/validation/protected-content gates as applicable. |
| Open implementation decisions | Exact dependency versions, solver numerical library, public API transport, import/export format list, CI provider/coverage thresholds, physical project package/container, comparison tolerance defaults, and mapping workflows remain `TBD` unless separately approved. |

#### Conditions

- The comparison engine must remain source-grounded in PKG-14 scope: immutable model states, analysis-run records, deterministic state/run comparison, mappings, tolerances, and comparison exports.
- `ASSUMPTION`: This deliverable consumes analysis-run records, mapping/tolerance contracts, result-export envelopes, and unit-system contracts as upstream evidence surfaces because `Dependencies.csv` lists those rows as ACTIVE DAG-002 mirror entries.
- The local dependency mirror records eleven ACTIVE rows and identifies the source of truth as approved DAG-006 coordination. These rows are evidence surface only and are not reclassified by this datasheet.
- Missing or ambiguous units on unit-bearing physical values are diagnostics, not silent defaults, per `docs/SPEC.md` unit-contract text.
- Result export envelopes must preserve units, diagnostics, provenance, hashes/status boundaries, and professional-boundary notices per `docs/SPEC.md` and `docs/TYPES.md`.
- Comparison tolerance defaults and mapping workflows are explicitly `TBD` in `execution/_Decomposition/SOFTWARE_DECOMP.md` open issue OI-014.

#### Construction

| Construct | Description | Status |
|---|---|---|
| Input run references | References to two analysis runs and their exact model-state/run basis. | Required by SOW-072/SOW-073; concrete schema field names `TBD`. |
| Mapping source | Manual mappings where stable IDs do not directly align. | Required by SOW-073; owned contract dependency DEL-14-05 remains upstream. |
| Unit normalization | Same-dimension comparison of result values using accepted unit metadata and conversion contracts. | Required by SOW-073 and unit contract; accepted unit catalog/tolerance details `TBD`. |
| Delta categories | Result, diagnostic, and settings deltas for mapped entities/locations. | Required by DEL-14-04 description; exact enum/API shape `TBD`. |
| Tolerance profiles | Profile-driven thresholding for comparison outcomes. | Required by SOW-073; defaults/workflows `TBD` under OI-014. |
| Deterministic output | Stable ordering and reproducible results for the same inputs. | Required by deterministic comparison scope; concrete hash/output fixture basis `TBD`. |
| Tests | Result delta tests. | Anticipated artifact; acceptance fixture set `TBD`. |

#### References

- `_CONTEXT.md` - deliverable identity, scope, architecture-basis injection, and context budget.
- `_REFERENCES.md` - governing reference list and accessible public context.
- `Dependencies.csv` - approved DAG-006 mirror/evidence surface for upstream dependency rows.
- `execution/_Decomposition/SOFTWARE_DECOMP.md` - revision 0.7 package, deliverable, scope, objective, and open-issue basis.
- `docs/CONTRACT.md` - invariant catalog, including no invention, unit-awareness, professional boundary, IP/privacy, and agent constraints.
- `docs/SPEC.md` - unit contract, analysis boundary, persistence/hash, result export, runner output, and validation mechanics.
- `docs/TYPES.md` - stable reference, diagnostic, checksum, result, result-export, and analysis-boundary vocabulary.
- `docs/IP_AND_DATA_BOUNDARY.md` - protected-content and private-data boundary.

## Component: execution/PKG-14_Model States, Analysis Runs, and Comparison/1_Working/DEL-14-04_Analysis-run comparison engine/Guidance.md

### Guidance: DEL-14-04 Analysis-run comparison engine

**Generated:** 2026-05-03
**Document Role:** Directional draft
**Source Basis:** `_CONTEXT.md`, `_REFERENCES.md`, `Dependencies.csv`, `execution/_Decomposition/SOFTWARE_DECOMP.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/IP_AND_DATA_BOUNDARY.md`

#### Purpose

DEL-14-04 exists to make analysis-run comparisons deterministic, unit-aware, traceable, and suitable for diagnostic/audit review. Its output supports design iteration and review; it does not decide external validation or professional reliance.

#### Principles

- Keep comparison evidence tied to exact run/model-state basis, solver version, settings, units, load cases, diagnostics, result hashes, and relevant rule/library references.
- Prefer stable IDs; use explicit manual mappings when stable IDs do not establish a safe comparison relationship.
- Treat unit-bearing values as comparable only when unit and dimension metadata support the comparison. Missing or ambiguous unit metadata is a diagnostic.
- Preserve raw delta evidence separately from tolerance-based classification. `ASSUMPTION`: this separation is needed so tolerance profiles can change without rewriting source evidence; the exact output structure is `TBD`.
- Keep diagnostics and settings in scope because the decomposition names them explicitly for DEL-14-04.
- Preserve the professional boundary: comparison output is review evidence, not approval, certification, sealing, authentication, or code compliance.

#### Considerations

| Topic | Guidance |
|---|---|
| Mapping | DEL-14-05 owns mapping/tolerance/export contracts. DEL-14-04 should consume those contracts rather than inventing mapping semantics. |
| Tolerances | OI-014 records comparison tolerance defaults and mapping workflows as `TBD`; do not hard-code defaults without human/product approval. |
| Units | Unit normalization depends on accepted unit metadata and conversion governance. Unsupported conversion semantics should remain `TBD` or become diagnostics. |
| Result scope | Result export envelopes are the intended review/regression/report-consumption surface. Avoid ad hoc result shapes once the schema contract is available. |
| Hashes | JSON payload hashes use the accepted JCS-compatible basis where JSON payloads are hashed. Non-JSON and binary partitioning remains `TBD` in the broader architecture. |
| Protected content | Fixtures, examples, and report sections must not embed protected standards text, protected tables, proprietary values, private project data, or private rule-pack payloads. |

#### Trade-offs

| Trade-off | Direction |
|---|---|
| Early implementation vs. contract maturity | Keep unresolved mapping, tolerance, and result-schema choices as `TBD` until upstream contracts are accepted. |
| Raw deltas vs. classified outcomes | Preserve raw evidence and expose tolerance-classified outcomes as derived interpretation. |
| Diagnostic detail vs. professional-boundary risk | Include enough diagnostics for review and audit while avoiding compliance/approval language. |
| Broad comparison scope vs. deliverable boundary | Cover mapped result entities, diagnostics, and settings; defer export semantics and mapping/tolerance contract definition to DEL-14-05. |

#### Examples

Concrete examples are `TBD`. Future examples should use invented or otherwise permitted data, documented provenance, explicit units, and no protected standards text/tables or proprietary values.

#### Open Questions

| Question ID | Question | Source |
|---|---|---|
| OQ-14-04-001 | What are the accepted default tolerance profiles and mapping workflows for comparison classification? | `execution/_Decomposition/SOFTWARE_DECOMP.md` OI-014 |
| OQ-14-04-002 | What is the final comparison output schema/API shape? | `docs/SPEC.md` result export baseline; DEL-14-05 dependency |
| OQ-14-04-003 | What fixture set proves deterministic ordering, unit-normalized delta behavior, and diagnostic/settings comparison without protected or private data? | `_CONTEXT.md` anticipated artifact; `docs/IP_AND_DATA_BOUNDARY.md` |

#### Conflict Table (for human ruling)

No source conflicts were identified in the accessible source set. Open questions above are missing-decision gaps, not contradictions.

## Component: execution/PKG-14_Model States, Analysis Runs, and Comparison/1_Working/DEL-14-04_Analysis-run comparison engine/Procedure.md

### Procedure: DEL-14-04 Analysis-run comparison engine

**Generated:** 2026-05-03
**Document Role:** Operational draft
**Source Basis:** `_CONTEXT.md`, `_REFERENCES.md`, `Dependencies.csv`, `execution/_Decomposition/SOFTWARE_DECOMP.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/IP_AND_DATA_BOUNDARY.md`

#### Purpose

Describe the conservative production procedure for creating and verifying the DEL-14-04 analysis-run comparison engine artifact without inventing implementation details or engineering values.

#### Prerequisites

- Read `_CONTEXT.md`, `_REFERENCES.md`, and the current deliverable-local dependency mirror before implementation work.
- Confirm the applicable scope items are SOW-072 and SOW-073, and that OBJ-016 is the objective context.
- Treat all existing approved DAG-006 rows in `Dependencies.csv` as ACTIVE evidence rows, not as rows to rewrite during this setup workflow.
- Confirm upstream contract availability before implementing dependent behavior:
  - DEL-14-02 analysis run records;
  - DEL-14-05 comparison mapping, tolerance, and export contracts;
  - DEL-08-04 result export format;
  - DEL-02-02 unit system and dimensional-analysis core contract;
  - architecture-basis rows AB-00-01, AB-00-02, AB-00-03, AB-00-04, AB-00-06, AB-00-07, and AB-00-08.
- Keep unsupported implementation choices as `TBD` until accepted by the appropriate upstream deliverable or human decision.

#### Steps

1. Establish the comparison input pair from exact analysis-run records.
   - Required evidence includes exact model-state basis, solver version, settings, units, load cases, diagnostics, results, rule-pack references, library references, and result hashes.
   - Concrete schema/API field names are `TBD`.

2. Resolve comparison mapping.
   - Prefer stable-ID alignment where safe.
   - Use manual mappings where required by SOW-073.
   - Do not invent mapping workflow semantics; consume the DEL-14-05 contract when available.

3. Validate unit comparability before computing deltas.
   - Compare only same-dimension unit-bearing values after accepted normalization.
   - Emit diagnostics for missing, ambiguous, or unsupported unit metadata; do not silently supply dimensionless or default units.

4. Compute result deltas for mapped comparison subjects.
   - Include mapped nodes, elements, supports, terminals, stress/result locations, diagnostics, and settings where represented by the accepted upstream result/run records.
   - Preserve raw delta evidence before tolerance-based classification.

5. Apply tolerance profiles.
   - Use accepted tolerance profile contracts.
   - Defaults and mapping workflows remain `TBD` under OI-014.

6. Produce deterministic comparison output.
   - Use stable ordering and schema-first envelopes consistent with the accepted architecture basis.
   - Preserve diagnostics, provenance, units, hashes/status boundaries, and professional-boundary notices.

7. Create result delta tests.
   - Cover deterministic repeatability, stable-ID matching, manual mapping, unit-normalized deltas, missing-unit diagnostics, settings deltas, diagnostic deltas, and tolerance classification.
   - Use invented/public/permissive fixtures only; fixture set and command are `TBD`.

#### Verification

| Check | Evidence |
|---|---|
| Inputs preserve exact run basis | Test or contract assertion that run metadata is available to comparison logic. |
| Determinism | Repeated comparison of identical input pair yields identical ordered output. |
| Mapping behavior | Stable-ID and manual-mapping cases both exercised. |
| Unit normalization | Same-dimension conversion path and missing/incompatible-unit diagnostic path both exercised. |
| Scope coverage | Mapped result locations, diagnostics, and settings are represented where upstream records expose them. |
| Tolerance behavior | Raw deltas remain available while tolerance classification changes with profile. |
| Governance boundary | Output avoids professional approval, certification, sealing, authentication, and automatic code-compliance labels. |
| Protected-content boundary | Fixtures and examples contain no protected standards text/tables, proprietary values, private project data, or private rule-pack payloads. |

#### Records

- Run comparison engine implementation artifact (`TBD` path).
- Result delta tests (`TBD` path/command).
- Fixture provenance notes for any public examples.
- Diagnostics/status assertions.
- Mapping/tolerance contract references.
- Any unresolved implementation decisions carried forward as `TBD`.

## Component: execution/PKG-14_Model States, Analysis Runs, and Comparison/1_Working/DEL-14-04_Analysis-run comparison engine/Specification.md

### Specification: DEL-14-04 Analysis-run comparison engine

**Generated:** 2026-05-03
**Document Role:** Normative draft
**Source Basis:** `_CONTEXT.md`, `_REFERENCES.md`, `Dependencies.csv`, `execution/_Decomposition/SOFTWARE_DECOMP.md`, `docs/CONTRACT.md`, `docs/SPEC.md`, `docs/TYPES.md`, `docs/IP_AND_DATA_BOUNDARY.md`

#### Scope

DEL-14-04 covers the backend feature slice for an analysis-run comparison engine. It compares two analysis runs, and where applicable their bound model states, using stable IDs, manual mappings where required, unit-normalized result deltas, diagnostics, settings, and tolerance profiles.

DEL-14-04 excludes comprehensive commercial-prover result ingestion, external validation, professional approval, certification, sealing, authentication, automatic code-compliance determination, and protected standards-data content.

#### Requirements

| ReqID | Requirement | Source | Verification |
|---|---|---|---|
| R-14-04-001 | The engine shall compare analysis runs deterministically using stable IDs and manual mappings where required. | SOW-073 in `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md` | Deterministic comparison tests with repeated identical inputs; concrete fixture set `TBD`. |
| R-14-04-002 | The engine shall treat analysis-run records as bound to exact model states, solver versions, settings, units, load cases, diagnostics, results, rule-pack references, library references, and result hashes. | SOW-072 in `_CONTEXT.md`; `execution/_Decomposition/SOFTWARE_DECOMP.md` | Tests assert comparison input metadata is preserved or surfaced; schema/API field names `TBD`. |
| R-14-04-003 | The engine shall compute unit-normalized result deltas only where unit and dimension metadata allow valid comparison. | SOW-073; `docs/SPEC.md` unit contract | Unit-normalization tests; missing/ambiguous unit metadata produces diagnostics rather than silent defaults. |
| R-14-04-004 | The engine shall include mapped nodes, elements, supports, terminals, stress/result locations, diagnostics, and settings within the comparison scope where the upstream result records expose them. | DEL-14-04 decomposition row | Coverage tests by result/entity category; exact category enum `TBD`. |
| R-14-04-005 | The engine shall use tolerance profiles for comparison classification. | SOW-073; dependency row for DEL-14-05; OI-014 | Tolerance-profile tests after DEL-14-05 contracts are available; defaults and mapping workflows remain `TBD`. |
| R-14-04-006 | The engine shall preserve professional-boundary language: comparison output is diagnostic/audit evidence and must not claim external validation or engineering acceptance. | SOW-073 notes; `docs/CONTRACT.md` OPS-K-AUTH-1/OPS-K-MECH-2; `docs/SPEC.md` analysis boundary | Protected wording/status tests; report/export assertions when applicable. |
| R-14-04-007 | The engine shall remain compatible with schema-first result/export envelopes rather than creating an ad hoc comparison result surface. | `_CONTEXT.md` architecture basis; `docs/SPEC.md` result export and runner output text | Contract tests against accepted result/export schema once available; concrete schema path `TBD`. |
| R-14-04-008 | The engine shall not introduce protected standards text, protected tables, proprietary values, private rule-pack payloads, or invented engineering defaults into public artifacts. | `docs/CONTRACT.md` OPS-K-IP-1/OPS-K-DATA-1/OPS-K-AGENT-1; `docs/IP_AND_DATA_BOUNDARY.md` | Protected-content/provenance checks; review of examples and fixtures. |
| R-14-04-009 | The deliverable shall include result delta tests as an anticipated artifact. | `_CONTEXT.md`; `docs/_Registers/Deliverables.csv` | Test presence and execution through the applicable test gate; command `TBD`. |

#### Standards

No external engineering standard text is locally present for this deliverable, and no clause-level engineering requirements are asserted here.

Project-governing references for this draft are:

- `docs/CONTRACT.md` for invariants.
- `docs/SPEC.md` for unit, analysis-boundary, persistence/hash, result-export, runner-output, and validation mechanics.
- `docs/TYPES.md` for vocabulary and boundary notes.
- `docs/IP_AND_DATA_BOUNDARY.md` for protected-content/private-data limits.
- `execution/_Decomposition/SOFTWARE_DECOMP.md` for accepted revision 0.7 scope and open issues.

#### Verification

| Verification Item | Required Evidence | Current Status |
|---|---|---|
| Determinism | Same input pair produces identical ordered comparison output. | `TBD` fixture/API shape. |
| Stable-ID/mapping behavior | Stable-ID match path and manual-mapping path are both exercised. | `TBD`; depends on DEL-14-05 mapping contract. |
| Unit-normalized deltas | Same-dimension values compare after accepted unit normalization; incompatible/missing units emit diagnostics. | `TBD`; depends on DEL-02-02 unit contract maturity. |
| Diagnostics/settings deltas | Diagnostic and settings differences are surfaced without compliance claims. | `TBD`; depends on result/run record schema. |
| Tolerance profiles | Tolerance profile affects classification without changing raw delta evidence. | `TBD`; OI-014 open. |
| Boundary wording | Output statuses avoid human approval, certification, sealing, authentication, and automatic code-compliance labels. | Required by governance; concrete assertions `TBD`. |

#### Documentation

The implementation brief or later production work should document:

- comparison input contract;
- mapping/tolerance profile dependency points;
- delta output structure;
- diagnostic/status behavior;
- unit-normalization behavior and failure diagnostics;
- deterministic ordering/hash basis;
- result delta test fixture provenance;
- limitations and professional-boundary notice.
