---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-02
package_id: PKG-04
decomposition_basis: projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@69ac259a7113d5a838fb22aa2e84df0e0f109713
project_scope_refs: [SOW-006]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-04-02

## Purpose and Objective Traceability

This migration candidate defines `DEL-04-02` in service of project scope [SOW-006] and package objectives [OBJ-003].

- **OUT-001** — A straight-pipe-element contract covering local stiffness, explicit section-property integration, weight hooks, boundary metadata, spanned loads and axial effects, unit-aware end/station resultant recovery, and deterministic solver verification is produced for the declared scope and objective.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-04-02 Straight pipe element

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":3,"line_start":1,"source_sha256":"abfae3bd7634f0717d00208b29c90d7514a46c59eb6f00ff6e6e1359b5c02d86","target_id":"CLM-001"} -->
#### Datasheet: DEL-04-02 Straight pipe element

<!-- D41-R5-T7-PDU055-CURRENTNESS -->
<!-- sow-source-end -->

### CLM-002 — D-41 R5 T7 PDU-055 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":11,"line_start":4,"source_sha256":"abfae3bd7634f0717d00208b29c90d7514a46c59eb6f00ff6e6e1359b5c02d86","target_id":"CLM-002"} -->
##### D-41 R5 T7 PDU-055 current declaration

Current authority is `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.8, approved `execution/_DAG/DAG-007/` graph context, and D-41/`DEC-074` through the completed T1-T6 bounded records. The implemented working-tree slice and its evidence supersede this surface's setup-only, future-only, or overtaken TBD wording as a current declaration; that earlier wording remains historical setup context only.

Surviving deliverable-local residuals and gates are those recorded in `_STATUS.md ## Remaining`; dated MEMORY and formal-review history remain unchanged. This refresh does not imply lifecycle, review, validation, release, professional-reliance, or code-compliance closure.

PDU-055 cited claim(s): `DEL-04-02-DECL-002`.

<!-- sow-source-end -->

### CLM-003 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":24,"line_start":12,"source_sha256":"abfae3bd7634f0717d00208b29c90d7514a46c59eb6f00ff6e6e1359b5c02d86","target_id":"CLM-003"} -->
##### Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-04-02 |
| Package ID | PKG-04 |
| Package | Solver Core and Numerical Methods |
| Type | BACKEND_FEATURE_SLICE |
| Scope item | SOW-006 |
| Objective | OBJ-003 |
| Context envelope | M |
| Anticipated artifacts | straight pipe element; solver tests |

<!-- sow-source-end -->

### CLM-004 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":35,"line_start":25,"source_sha256":"abfae3bd7634f0717d00208b29c90d7514a46c59eb6f00ff6e6e1359b5c02d86","target_id":"CLM-004"} -->
##### Attributes

| Attribute | Setup value |
|---|---|
| Element family | Straight pipe centerline/frame element |
| Analysis model boundary | 3D centerline/frame mechanics with six degrees of freedom per node; shell/solid FEA remains a local-analysis handoff path. |
| Covered mechanics | Local stiffness, section-property integration, weight hooks, and element force recovery. |
| Excluded mechanics | Code compliance decisions, rule-pack acceptability, protected standard formulas/tables, and repo-bundled protected dimensional or material values. |
| Unit policy | All inputs, intermediate values, and outputs are unit-aware and dimensionally checked. Exact unit API is `TBD`. |
| Data provenance policy | Pipe dimensions, material values, and other solve inputs are user-supplied or lawfully imported private/project data. |

<!-- sow-source-end -->

### CLM-005 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":45,"line_start":36,"source_sha256":"abfae3bd7634f0717d00208b29c90d7514a46c59eb6f00ff6e6e1359b5c02d86","target_id":"CLM-005"} -->
##### Conditions

| Condition | Status |
|---|---|
| Solver numerical library | `TBD` from architecture/implementation decision. |
| Section-property source contract | `TBD`; must connect to user/project data or lawful library inputs. |
| Weight-load integration contract | `TBD`; must remain a hook to load-case behavior, not a hidden default load application. |
| Element force recovery conventions | `TBD`; must be unit-aware and consistent with solver result envelopes. |
| Test fixture data | Must be synthetic, public-domain, or otherwise cleared for repository use. |

<!-- sow-source-end -->

### CLM-006 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":51,"line_start":46,"source_sha256":"abfae3bd7634f0717d00208b29c90d7514a46c59eb6f00ff6e6e1359b5c02d86","target_id":"CLM-006"} -->
##### Construction

The setup kit describes the future implementation boundary only. It does not implement solver code, choose element dimensions, choose material values, encode protected formulas, or create repo-level tests.

The future element is expected to receive validated geometry, section properties, material/mechanical inputs, and load hooks through governed domain/service contracts. Missing solve-required values must produce explicit findings rather than silent defaults.

<!-- sow-source-end -->

### CLM-007 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":60,"line_start":52,"source_sha256":"abfae3bd7634f0717d00208b29c90d7514a46c59eb6f00ff6e6e1359b5c02d86","target_id":"CLM-007"} -->
##### References

- `_CONTEXT.md` for deliverable identity, scope, artifacts, and architecture-basis injection.
- `docs/_Registers/Deliverables.csv` row `DEL-04-02`.
- `docs/_Registers/ScopeLedger.csv` row `SOW-006`.
- `docs/_Registers/ContextBudgetQA.csv` row `DEL-04-02`.
- `docs/CONTRACT.md` invariants listed in the sealed brief.
- `execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.7 architecture basis IDs `AB-00-01`, `AB-00-02`, `AB-00-03`, `AB-00-04`, `AB-00-06`, and `AB-00-08`.

<!-- sow-source-end -->

### CLM-008 — Open Setup Questions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":68,"line_start":61,"source_sha256":"abfae3bd7634f0717d00208b29c90d7514a46c59eb6f00ff6e6e1359b5c02d86","target_id":"CLM-008"} -->
##### Open Setup Questions

| Question | Status |
|---|---|
| Which upstream schema owns straight-pipe section-property inputs? | `TBD` |
| Which solver-kernel interface owns local-to-global transformation and assembly handoff? | `TBD` |
| Which load engine interface receives or invokes weight hooks? | `TBD` |
| Which deterministic verification cases are accepted for the element without protected data? | `TBD` |
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-009 — Specification: DEL-04-02 Straight pipe element

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":2,"line_start":1,"source_sha256":"e2592d273366475c1791c018791fd963a073f949d6b52c0ce0fdb78a240dcdee","target_id":"CLM-009"} -->
#### Specification: DEL-04-02 Straight pipe element

<!-- sow-source-end -->

### CLM-010 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":8,"line_start":3,"source_sha256":"e2592d273366475c1791c018791fd963a073f949d6b52c0ce0fdb78a240dcdee","target_id":"CLM-010"} -->
##### Scope

This deliverable specifies the implemented straight pipe element backend slice. It covers straight pipe local stiffness, section-property integration, weight hooks, boundary metadata, end/station resultant recovery, spanned loads, and axial effects within the global 3D centerline/frame solver architecture.

Current evidence lives in `core/solver/straight_pipe` with deterministic unit and witness-backed benchmark coverage. This documentation refresh does not edit solver code or fixtures, introduce protected formulas or tables, or make certification/compliance claims.

<!-- sow-source-end -->

### CLM-011 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":20,"line_start":9,"source_sha256":"e2592d273366475c1791c018791fd963a073f949d6b52c0ce0fdb78a240dcdee","target_id":"CLM-011"} -->
##### Requirements

| Req ID | Requirement | Source basis | Verification hook |
|---|---|---|---|
| DEL-04-02-RQ-001 | The straight pipe element shall fit the 3D centerline/frame solver model and shall not bypass the solver kernel boundary. | SOW-006; OPS-K-MECH-1; AB-00-02 | Architecture/module-boundary review once implementation paths are selected. |
| DEL-04-02-RQ-002 | Local stiffness behavior shall be derived only from open mechanics and user/project/lawfully imported input values. | SOW-006; OPS-K-IP-1; OPS-K-DATA-1 | Protected-content review and fixture review. |
| DEL-04-02-RQ-003 | Section-property integration shall require explicit section-property inputs or validated upstream calculations; missing solve-required properties shall produce explicit findings. | SOW-006; OPS-K-DATA-2; OPS-K-UNIT-1 | Negative tests for missing properties and units; exact cases `TBD`. |
| DEL-04-02-RQ-004 | Weight hooks shall expose the information needed for load-case application without silently applying hidden load defaults. | SOW-006; OPS-K-DATA-2; AB-00-03 | Load-interface tests once the primitive load contract is accepted. |
| DEL-04-02-RQ-005 | Element force recovery shall return unit-aware mechanical result components suitable for downstream stress recovery, without encoding code stress checks. | SOW-006; OPS-K-MECH-2; OPS-K-UNIT-1 | Solver result-envelope tests and downstream interface review. |
| DEL-04-02-RQ-006 | Solver changes shall include deterministic verification tests before release use. | OPS-K-SOLVER-1; AB-00-08 | Deterministic solver tests using synthetic or cleared inputs. |
| DEL-04-02-RQ-007 | Diagnostics shall use governed result-envelope concepts and shall not claim professional approval, certification, or compliance. | AB-00-06; OPS-K-AGENT-4 | Diagnostic/result-envelope review. |

<!-- sow-source-end -->

### CLM-012 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":24,"line_start":21,"source_sha256":"e2592d273366475c1791c018791fd963a073f949d6b52c0ce0fdb78a240dcdee","target_id":"CLM-012"} -->
##### Standards

No protected standard text, protected formulas, protected dimensional tables, material allowables, or proprietary commercial data are available in this deliverable-local setup context. Any future code or standard basis must be introduced only as a lawful private/project input or non-protected pointer with provenance. Clause-level requirements are `TBD`.

<!-- sow-source-end -->

### CLM-013 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":34,"line_start":25,"source_sha256":"e2592d273366475c1791c018791fd963a073f949d6b52c0ce0fdb78a240dcdee","target_id":"CLM-013"} -->
##### Verification

| Verification area | Minimum setup expectation |
|---|---|
| Solver boundary | Tests and reviews must show the element is a solver component, not a rule-pack or compliance component. |
| Unit safety | Tests must cover dimensional checking for section properties, stiffness-related inputs, weight-related inputs, and recovered forces. |
| Missing inputs | Tests must show explicit findings for missing solve-required values. |
| Force recovery | Tests must show deterministic recovered mechanical result components; exact benchmark cases are `TBD`. |
| IP/data boundary | Test data must be synthetic, public-domain, or otherwise cleared for redistribution. |

<!-- sow-source-end -->

### CLM-014 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":45,"line_start":35,"source_sha256":"e2592d273366475c1791c018791fd963a073f949d6b52c0ce0fdb78a240dcdee","target_id":"CLM-014"} -->
##### Documentation

Current implementation artifacts are:

- `core/solver/straight_pipe`;
- its deterministic crate tests and rights-safe straight-pipe mechanics witnesses.

Module and test paths are now evidenced in-tree. Production numerical-library
integration, final governed per-kind tolerances, and full solver-to-result-envelope
binding remain `TBD` or separately recorded residual work.

<!-- sow-source-end -->

### CLM-015 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":50,"line_start":46,"source_sha256":"e2592d273366475c1791c018791fd963a073f949d6b52c0ce0fdb78a240dcdee","target_id":"CLM-015"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Issue | Contenders | Human ruling |
|---|---|---|---|
| None | No source conflict identified in setup evidence. | N/A | N/A |
<!-- sow-source-end -->

- **AC-001** — The contract preserves the accepted straight-pipe mechanics and interface boundaries, including explicit units and lawful input provenance, no hidden load or engineering defaults, rights-cleared fixtures, mechanics-only outputs, and the unresolved governed solver-to-result-envelope integration.

## Production and Verification Method — Praxeology

### CLM-016 — Procedure: DEL-04-02 Straight pipe element

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":2,"line_start":1,"source_sha256":"f43d4b1c0fa202abfda544a22c08e5cf0ea90a640fc778aed54eeb9c9735ab1c","target_id":"CLM-016"} -->
#### Procedure: DEL-04-02 Straight pipe element

<!-- sow-source-end -->

### CLM-017 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":6,"line_start":3,"source_sha256":"f43d4b1c0fa202abfda544a22c08e5cf0ea90a640fc778aed54eeb9c9735ab1c","target_id":"CLM-017"} -->
##### Purpose

Define the bounded maintenance and verification procedure for the implemented straight pipe element without expanding its mechanics scope.

<!-- sow-source-end -->

### CLM-018 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":13,"line_start":7,"source_sha256":"f43d4b1c0fa202abfda544a22c08e5cf0ea90a640fc778aed54eeb9c9735ab1c","target_id":"CLM-018"} -->
##### Prerequisites

- Confirm the task names `DEL-04-02` and its authorized write scope.
- Confirm upstream architecture basis constraints from `AB-00-01`, `AB-00-02`, `AB-00-03`, `AB-00-04`, `AB-00-06`, and `AB-00-08`.
- Confirm the current `core/solver/straight_pipe` unit/domain and frame-kernel interfaces; unresolved integration items remain `TBD`.
- Confirm all example dimensions, material values, and fixtures are synthetic, public-domain, or otherwise cleared.

<!-- sow-source-end -->

### CLM-019 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":23,"line_start":14,"source_sha256":"f43d4b1c0fa202abfda544a22c08e5cf0ea90a640fc778aed54eeb9c9735ab1c","target_id":"CLM-019"} -->
##### Steps

1. Re-read `_CONTEXT.md`, `Specification.md`, and `_DEPENDENCIES.md`.
2. Identify the accepted module boundary for the straight pipe element and its relation to the global frame kernel.
3. Identify required input contracts for section properties, material/mechanical values, units, weight hooks, diagnostics, and result envelopes.
4. Maintain only the authorized straight-pipe local element behavior; do not broaden into stress-code or professional-acceptance logic.
5. Add explicit findings for missing solve-required values and unit mismatches; do not apply silent defaults.
6. Add deterministic solver tests with synthetic or cleared inputs.
7. Verify recovered element forces remain mechanical results and do not claim code compliance.

<!-- sow-source-end -->

### CLM-020 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":33,"line_start":24,"source_sha256":"f43d4b1c0fa202abfda544a22c08e5cf0ea90a640fc778aed54eeb9c9735ab1c","target_id":"CLM-020"} -->
##### Verification

| Check | Expected evidence |
|---|---|
| Scope boundary | Implementation changes are limited to the approved implementation scope for DEL-04-02. |
| Unit behavior | Unit-aware tests pass and dimensional mismatches fail explicitly. |
| Missing input behavior | Missing solve-required properties produce findings. |
| Solver result behavior | Element force recovery is deterministic for accepted synthetic/cleared cases. |
| IP/data boundary | No protected tables, formulas, examples, material allowables, or proprietary data are added. |

<!-- sow-source-end -->

### CLM-021 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":40,"line_start":34,"source_sha256":"f43d4b1c0fa202abfda544a22c08e5cf0ea90a640fc778aed54eeb9c9735ab1c","target_id":"CLM-021"} -->
##### Records

- Implementation or maintenance run records for authorized code work.
- Solver test results.
- Fixture provenance notes.
- Protected-content review evidence where applicable.
- Any human rulings for `TBD` items.
<!-- sow-source-end -->

- **VER-001** — Validate the contract and review source parity, straight-pipe behavior and frame-kernel boundaries, section and weight interfaces, spanned-load and resultant coverage, dimensional checks, explicit findings, protected-content controls, and result-envelope residuals.

## Governing Values and Decisions — Axiology

### CLM-022 — Guidance: DEL-04-02 Straight pipe element

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":2,"line_start":1,"source_sha256":"d88a87f6f95f0e067dfd66e4a396ae422cd19a141b3576558db870fbd5369fd9","target_id":"CLM-022"} -->
#### Guidance: DEL-04-02 Straight pipe element

<!-- sow-source-end -->

### CLM-023 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":6,"line_start":3,"source_sha256":"d88a87f6f95f0e067dfd66e4a396ae422cd19a141b3576558db870fbd5369fd9","target_id":"CLM-023"} -->
##### Purpose

This deliverable exists to isolate the straight pipe element as one bounded solver feature slice. It should give the global 3D frame solver a governed, testable element behavior while keeping section data, units, diagnostics, load hooks, and downstream force recovery explicit.

<!-- sow-source-end -->

### CLM-024 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":14,"line_start":7,"source_sha256":"d88a87f6f95f0e067dfd66e4a396ae422cd19a141b3576558db870fbd5369fd9","target_id":"CLM-024"} -->
##### Principles

- Keep mechanics computation separate from rule-pack acceptability and human compliance judgment.
- Treat dimensions, material values, and protected standard-derived values as external governed inputs, never public bundled defaults.
- Prefer explicit `TBD` and explicit diagnostics over silent assumptions when solve-required values are missing.
- Preserve unit and provenance information through element inputs and outputs.
- Keep weight behavior as an interface hook until the load-case contract determines how loads are formed and applied.

<!-- sow-source-end -->

### CLM-025 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":20,"line_start":15,"source_sha256":"d88a87f6f95f0e067dfd66e4a396ae422cd19a141b3576558db870fbd5369fd9","target_id":"CLM-025"} -->
##### Considerations

The implemented element consumes explicit section properties and mechanics inputs through the frame-kernel boundary, carries unit/boundary metadata, and supports deterministic force/resultant recovery and spanned-load behavior. Full application-service result-envelope production remains separate residual work.

Verification should use open, synthetic, or cleared test cases. Any hand-check examples must avoid copying protected standard examples, tables, or protected formula presentations.

<!-- sow-source-end -->

### CLM-026 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":29,"line_start":21,"source_sha256":"d88a87f6f95f0e067dfd66e4a396ae422cd19a141b3576558db870fbd5369fd9","target_id":"CLM-026"} -->
##### Trade-offs

| Topic | Guidance |
|---|---|
| Completeness vs data boundary | Record missing section or material values as findings rather than providing public defaults. |
| Element scope vs solver kernel scope | Keep local element behavior here; keep global assembly, transforms, and sparse solve responsibilities in the solver kernel deliverable unless the accepted implementation boundary says otherwise. |
| Load hooks vs load application | Expose weight-related information without creating hidden primitive load behavior inside the element. |
| Force recovery vs stress checks | Recover mechanical element forces; downstream stress recovery and rule checks remain separate deliverables. |

<!-- sow-source-end -->

### CLM-027 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":36,"line_start":30,"source_sha256":"d88a87f6f95f0e067dfd66e4a396ae422cd19a141b3576558db870fbd5369fd9","target_id":"CLM-027"} -->
##### Examples

Rights-safe deterministic examples exist in the straight-pipe mechanics witness
and benchmark families. They are software verification evidence, not design
examples or professional acceptance, and must not be replaced with protected
standards content.

<!-- sow-source-end -->

### CLM-028 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":41,"line_start":37,"source_sha256":"d88a87f6f95f0e067dfd66e4a396ae422cd19a141b3576558db870fbd5369fd9","target_id":"CLM-028"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Issue | Contenders | Human ruling |
|---|---|---|---|
| None | No setup conflict found. | N/A | N/A |
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-006 OBJ-003 | CLM-009 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
