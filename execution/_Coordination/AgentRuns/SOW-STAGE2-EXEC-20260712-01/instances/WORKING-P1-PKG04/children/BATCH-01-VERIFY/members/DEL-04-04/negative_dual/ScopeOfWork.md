---
schema: chirality-deliverable-sow/v1
deliverable_id: DEL-04-04
package_id: PKG-04
decomposition_basis: projects/chirality-piping/execution/_Decomposition/SOFTWARE_DECOMP.md@69ac259a7113d5a838fb22aa2e84df0e0f109713
project_scope_refs: [SOW-012]
package_objective_refs: [OBJ-003]
---

# Scope of Work — DEL-04-04

## Purpose and Objective Traceability

This migration candidate defines `DEL-04-04` in service of project scope [SOW-012] and package objectives [OBJ-003].

- **OUT-001** — A nonlinear-support classifier and state-oracle contract covering one-way restraints, gaps, lift-off, friction, state-switched transitions, convergence and non-convergence reporting, report-facing records, and integration-facing deterministic verification is produced for the declared scope and objective.

## Deliverable Definition — Ontology

### CLM-001 — Datasheet: DEL-04-04 Nonlinear support active-set solver

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":2,"line_start":1,"source_sha256":"903a4644cd018175b13781bc5b13aa177d25bed5e0825ecb55565f557273560a","target_id":"CLM-001"} -->
#### Datasheet: DEL-04-04 Nonlinear support active-set solver

<!-- sow-source-end -->

### CLM-002 — Identification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":15,"line_start":3,"source_sha256":"903a4644cd018175b13781bc5b13aa177d25bed5e0825ecb55565f557273560a","target_id":"CLM-002"} -->
##### Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-04-04 |
| Name | Nonlinear support active-set solver |
| Package | PKG-04 Solver Core and Numerical Methods |
| Type | BACKEND_FEATURE_SLICE |
| Decomposition basis | execution/_Decomposition/SOFTWARE_DECOMP.md revision 0.7 |
| Scope item | SOW-012 |
| Objective | OBJ-003 |
| Context envelope | L; WATCH |

<!-- sow-source-end -->

### CLM-003 — Attributes

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":25,"line_start":16,"source_sha256":"903a4644cd018175b13781bc5b13aa177d25bed5e0825ecb55565f557273560a","target_id":"CLM-003"} -->
##### Attributes

| Attribute | Value | Source |
|---|---|---|
| Solver role | Per-iteration active-set classifier/state oracle for nonlinear support behavior consumed by the global 3D centerline/frame solver integration loop. | _CONTEXT.md Description; ScopeLedger.csv SOW-012; DEC-044 |
| Covered behavior categories | One-way supports, gaps, lift-off, and friction. | Deliverables.csv DEL-04-04; ScopeLedger.csv SOW-012 |
| Reporting obligation | Convergence reporting, active-set state, and unresolved non-convergence reporting are in scope. | CONTRACT.md OPS-K-SOLVER-2; _CONTEXT.md Description |
| Anticipated artifacts | Active-set classifier/state oracle; report-facing active-set records; classifier and integration-facing convergence tests. | _CONTEXT.md Anticipated Artifacts; DEC-044 |
| Explicit deferrals | Assembled loop ownership is re-pointed to `core/solver/nonlinear_integration`; sparse live-path adoption, class-tiered convergence values, and implementation-level defaults remain governed follow-on work. | _CONTEXT.md Architecture Basis Injection; DEC-044; DEC-046; human brief hard stops |

<!-- sow-source-end -->

### CLM-004 — Conditions

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":35,"line_start":26,"source_sha256":"903a4644cd018175b13781bc5b13aa177d25bed5e0825ecb55565f557273560a","target_id":"CLM-004"} -->
##### Conditions

| Condition | Status |
|---|---|
| The primary mechanics model remains a 3D centerline/frame model. | Required by OPS-K-MECH-1. |
| The solver computes mechanics and does not decide professional compliance. | Required by OPS-K-MECH-2 and package exclusions. |
| Missing solve-required values are findings, not silent defaults. | Required by OPS-K-DATA-2. |
| Unit-bearing quantities must be unit-aware and dimensionally checked. | Required by OPS-K-UNIT-1. |
| Nonlinear convergence tolerances, friction defaults, and case-specific values are not invented in this setup kit. | Required by OPS-K-AGENT-1 and human hard stops. |

<!-- sow-source-end -->

### CLM-005 — Construction

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":50,"line_start":36,"source_sha256":"903a4644cd018175b13781bc5b13aa177d25bed5e0825ecb55565f557273560a","target_id":"CLM-005"} -->
##### Construction

This setup kit defines the nonlinear active-set classifier boundary. The
assembled nonlinear loop is owned by the PKG-04 integration tranche under
`DEC-044`; this deliverable remains the classifier/state-oracle surface.

| Construction element | Local setup position |
|---|---|
| Active-set iteration loop | Re-pointed by `DEC-044`: assembled loop ownership is `core/solver/nonlinear_integration`; this deliverable supplies the per-iteration classifier/state oracle. |
| Support activation state model | In scope for this deliverable; exact downstream integration contract is owned by the integration tranche. |
| Gap/lift-off/one-way state transitions | In scope for this deliverable; rules must be evidence-backed and tested. |
| Friction behavior | In scope as a named behavior category; numerical model, defaults, and limits are TBD. |
| Convergence reporting | Required output surface; result-envelope integration follows AB-00-03 and diagnostics follow AB-00-06. |
| Convergence tests | Required anticipated artifact; deterministic verification follows OPS-K-SOLVER-1 and AB-00-08. |

<!-- sow-source-end -->

### CLM-006 — References

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":59,"line_start":51,"source_sha256":"903a4644cd018175b13781bc5b13aa177d25bed5e0825ecb55565f557273560a","target_id":"CLM-006"} -->
##### References

- _CONTEXT.md for sealed deliverable identity, scope, objective, and architecture basis.
- docs/_Registers/Deliverables.csv row DEL-04-04.
- docs/_Registers/ScopeLedger.csv row SOW-012.
- docs/_Registers/ContextBudgetQA.csv row DEL-04-04.
- execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.7 rows for PKG-04, DEL-04-04, SOW-012, OBJ-003, and AB-00-01/02/03/06/08.
- docs/CONTRACT.md invariants OPS-K-MECH-1, OPS-K-MECH-2, OPS-K-UNIT-1, OPS-K-SOLVER-1, OPS-K-SOLVER-2, OPS-K-DATA-2, OPS-K-REPORT-1, and OPS-K-AGENT-1 through OPS-K-AGENT-4.

<!-- sow-source-end -->

### CLM-007 — D-41 R5 T7 PDU-054 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Datasheet.md","line_end":62,"line_start":60,"source_sha256":"903a4644cd018175b13781bc5b13aa177d25bed5e0825ecb55565f557273560a","target_id":"CLM-007"} -->
##### D-41 R5 T7 PDU-054 current declaration

Earlier setup-era statements on this surface are retained as historical setup context where applicable; this section is the active current-state declaration. The nonlinear support slice and DEC-067 Coulomb-friction basis (`±mu*N`) are implemented and evidenced. Broader nonlinear policies and validation thresholds survive only where explicitly recorded; this currentness declaration is not an engineering acceptance.
<!-- sow-source-end -->

## Completion and Reliance Basis — Epistemology

### CLM-008 — Specification: DEL-04-04 Nonlinear support active-set solver

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":2,"line_start":1,"source_sha256":"51c0fd3f7a582e18507e15183ccba59d9522fbb50769177a393a5c5329325f9d","target_id":"CLM-008"} -->
#### Specification: DEL-04-04 Nonlinear support active-set solver

<!-- sow-source-end -->

### CLM-009 — Scope

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":12,"line_start":3,"source_sha256":"51c0fd3f7a582e18507e15183ccba59d9522fbb50769177a393a5c5329325f9d","target_id":"CLM-009"} -->
##### Scope

DEL-04-04 covers the per-iteration active-set classifier/state oracle for
nonlinear support behavior: one-way supports, gaps, lift-off, friction, and
convergence reporting. Per `DEC-044`, the assembled nonlinear loop that wraps
frame assembly/solve around this classifier is owned by the PKG-04 integration
tranche `core/solver/nonlinear_integration`. This deliverable does not set
numerical tolerances, choose friction defaults, or make certification/compliance
claims.

<!-- sow-source-end -->

### CLM-010 — Requirements

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":26,"line_start":13,"source_sha256":"51c0fd3f7a582e18507e15183ccba59d9522fbb50769177a393a5c5329325f9d","target_id":"CLM-010"} -->
##### Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| DEL-04-04-REQ-01 | The deliverable shall preserve the 3D centerline/frame mechanics boundary for global piping analysis. | OPS-K-MECH-1; PKG-04 package scope | Architecture and solver-boundary tests confirm no local FEA substitution is introduced. |
| DEL-04-04-REQ-02 | The nonlinear support classifier shall address one-way restraints, lift-off, gaps, and friction for consumption by a controlled iterative method. | SOW-012; Deliverables.csv DEL-04-04; DEC-044 | Classifier and integration tests cover invented representative cases for each behavior category. |
| DEL-04-04-REQ-03 | The implementation shall report convergence state, active-set state, and unresolved non-convergence. | OPS-K-SOLVER-2; AB-00-06 | Result-envelope and diagnostic tests assert reported state fields and warning class behavior. |
| DEL-04-04-REQ-04 | Solver changes shall have deterministic verification tests before release use. | OPS-K-SOLVER-1; AB-00-08 | Test inventory includes nonlinear support classifier and assembled-loop convergence/non-convergence regression cases. |
| DEL-04-04-REQ-05 | Missing solve-required nonlinear support inputs shall be explicit findings, never silent defaults. | OPS-K-DATA-2; AB-00-06 | Negative tests assert missing data produces diagnostics rather than assumed values. |
| DEL-04-04-REQ-06 | Unit-bearing support, displacement, force, and friction-related quantities shall be unit-aware and dimensionally checked where applicable. | OPS-K-UNIT-1 | Unit tests cover accepted, rejected, and missing unit metadata. |
| DEL-04-04-REQ-07 | The solver shall compute mechanics only; rule-pack acceptability and professional compliance remain outside this deliverable. | OPS-K-MECH-2; package exclusions | Reports and result labels avoid compliance/certification language. |
| DEL-04-04-REQ-08 | Result and diagnostic outputs shall support report disclosure of solver version, warnings, assumptions, limitations, and provenance notes. | OPS-K-REPORT-1; AB-00-06 | Report-facing fixture tests confirm required metadata is present or explicitly TBD. |
| DEL-04-04-REQ-09 | Implementation choices for sparse live-path adoption, class-tiered convergence values, friction defaults, and final data contracts remain governed or TBD until later authorized work. | _CONTEXT.md Still TBD; OPS-K-AGENT-1; DEC-044; DEC-046; human hard stops | Review confirms no invented values or defaults appear in setup artifacts. |

<!-- sow-source-end -->

### CLM-011 — Standards

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":30,"line_start":27,"source_sha256":"51c0fd3f7a582e18507e15183ccba59d9522fbb50769177a393a5c5329325f9d","target_id":"CLM-011"} -->
##### Standards

No protected standards text, formulas, tables, examples, or code-specific values are included in this setup kit. Public/protected data boundaries follow docs/CONTRACT.md. Any later code-specific or project-specific engineering values must be user-supplied or lawfully imported private data where applicable.

<!-- sow-source-end -->

### CLM-012 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":47,"line_start":31,"source_sha256":"51c0fd3f7a582e18507e15183ccba59d9522fbb50769177a393a5c5329325f9d","target_id":"CLM-012"} -->
##### Verification

Verification shall include deterministic invented-example tests for active-set
activation/deactivation, gap closure/opening, lift-off, one-way support
behavior, friction state reporting, convergence, and non-convergence
diagnostics. Per `DEC-067`, unilateral-support classification is
state-switched: engaged supports (including closed gaps) classify on trial
reaction sign and released supports classify on trial displacement penetration
(or the explicit gap clearance), so re-engagement and lift-off transitions are
observable and the converged state does not depend on seeded initial states;
verification includes transition witnesses for re-engagement of a lifted
one-way support, lift-off of a closed gap, and bounded +/- mu*N friction
sliding. Assembled-loop verification is owned by
`core/solver/nonlinear_integration` under `DEC-044`; exact pass/fail
thresholds, test matrices, and measured convergence values remain governed by
`DEC-046` and must not be invented by this setup pass.

<!-- sow-source-end -->

### CLM-013 — Documentation

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Specification.md","line_end":54,"line_start":48,"source_sha256":"51c0fd3f7a582e18507e15183ccba59d9522fbb50769177a393a5c5329325f9d","target_id":"CLM-013"} -->
##### Documentation

Required documentation artifacts for this setup are `Datasheet.md`,
`Specification.md`, `Guidance.md`, `Procedure.md`, `_SEMANTIC.md`,
`_SEMANTIC_LENSING.md`, `_DEPENDENCIES.md`, `Dependencies.csv`, and
`_run_records/`. The assembled-loop integration artifact is
`core/solver/nonlinear_integration`.
<!-- sow-source-end -->

- **AC-001** — The contract preserves the accepted classifier versus assembled-loop ownership, implemented state-transition and bounded Coulomb-friction basis, unit and diagnostic boundaries, explicit missing inputs, mechanics-only posture, and unresolved path-history, convergence-threshold, sparse-live-path, and validation policies without inventing defaults or engineering acceptance.

## Production and Verification Method — Praxeology

### CLM-014 — Procedure: DEL-04-04 Nonlinear support active-set solver

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":2,"line_start":1,"source_sha256":"28cd10eeeeb0e011adba11d90b9b1aa67123b075c32a56fddf7baf4097e2f64b","target_id":"CLM-014"} -->
#### Procedure: DEL-04-04 Nonlinear support active-set solver

<!-- sow-source-end -->

### CLM-015 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":6,"line_start":3,"source_sha256":"28cd10eeeeb0e011adba11d90b9b1aa67123b075c32a56fddf7baf4097e2f64b","target_id":"CLM-015"} -->
##### Purpose

Define the documentation setup procedure for DEL-04-04 without implementing nonlinear solver code.

<!-- sow-source-end -->

### CLM-016 — Prerequisites

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":13,"line_start":7,"source_sha256":"28cd10eeeeb0e011adba11d90b9b1aa67123b075c32a56fddf7baf4097e2f64b","target_id":"CLM-016"} -->
##### Prerequisites

- Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Apply docs/CONTRACT.md invariants OPS-K-MECH-1, OPS-K-MECH-2, OPS-K-UNIT-1, OPS-K-SOLVER-1, OPS-K-SOLVER-2, OPS-K-DATA-2, OPS-K-REPORT-1, and OPS-K-AGENT-1 through OPS-K-AGENT-4.
- Apply architecture basis AB-00-01, AB-00-02, AB-00-03, AB-00-06, and AB-00-08.
- Keep all writes inside the DEL-04-04 folder.

<!-- sow-source-end -->

### CLM-017 — Steps

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":23,"line_start":14,"source_sha256":"28cd10eeeeb0e011adba11d90b9b1aa67123b075c32a56fddf7baf4097e2f64b","target_id":"CLM-017"} -->
##### Steps

1. Confirm the deliverable identity is DEL-04-04 under PKG-04.
2. Confirm the setup scope is documentation only: four documents, semantic files, dependency artifacts, and run records.
3. Capture nonlinear support behavior categories from SOW-012 and the deliverables register: one-way supports, gaps, lift-off, and friction. Per `DEC-067`, the implemented classifier decision boundary is state-switched (engaged supports classify on reaction sign, released supports on displacement penetration/clearance) and a sliding friction support carries the bounded `+/- mu*N` tangential force in the assembled loop rather than a full DOF release.
4. Record future implementation needs as `TBD` when exact numerical library choices, convergence thresholds, friction defaults, or data contracts are not provided.
5. Preserve mechanics/reporting boundaries: mechanics solved by solver, acceptability handled by rule packs or humans, and no compliance/certification claims.
6. Generate dependency rows only from explicit scope, architecture, invariant, or local-document evidence.
7. Run local schema validation for `Dependencies.csv`.

<!-- sow-source-end -->

### CLM-018 — Verification

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":31,"line_start":24,"source_sha256":"28cd10eeeeb0e011adba11d90b9b1aa67123b075c32a56fddf7baf4097e2f64b","target_id":"CLM-018"} -->
##### Verification

- Four production documents exist and retain Datasheet, Specification, Guidance, and Procedure roles.
- `_SEMANTIC.md` exists and separates semantic lensing from engineering authority.
- `_SEMANTIC_LENSING.md` exists and records warranted enrichment items without rewriting production documents.
- `Dependencies.csv` validates against v3.1 schema.
- `_STATUS.md` is not advanced to `ISSUED`.

<!-- sow-source-end -->

### CLM-019 — Records

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Procedure.md","line_end":42,"line_start":32,"source_sha256":"28cd10eeeeb0e011adba11d90b9b1aa67123b075c32a56fddf7baf4097e2f64b","target_id":"CLM-019"} -->
##### Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_SEMANTIC.md`
- `_SEMANTIC_LENSING.md`
- `Dependencies.csv`
- `_DEPENDENCIES.md`
- `_run_records/TASK_RUN_2026-04-30_1015_*.md`
<!-- sow-source-end -->

- **VER-001** — Validate the contract and review source parity, nonlinear behavior categories and state transitions, classifier/integration ownership, convergence diagnostics, units and provenance, protected-content and professional boundaries, deterministic transition witnesses, and every surviving governed residual.

## Governing Values and Decisions — Axiology

### CLM-020 — Guidance: DEL-04-04 Nonlinear support active-set solver

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":2,"line_start":1,"source_sha256":"689f6fe4f398f940cc2f32859383ba4f698f8bb218c12592de64faa5edad350a","target_id":"CLM-020"} -->
#### Guidance: DEL-04-04 Nonlinear support active-set solver

<!-- sow-source-end -->

### CLM-021 — Purpose

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":6,"line_start":3,"source_sha256":"689f6fe4f398f940cc2f32859383ba4f698f8bb218c12592de64faa5edad350a","target_id":"CLM-021"} -->
##### Purpose

This deliverable prepares a future nonlinear support active-set solver slice within PKG-04. Its value is to keep nonlinear mechanical behavior, diagnostics, unit handling, and result reporting bounded before implementation work begins.

<!-- sow-source-end -->

### CLM-022 — Principles

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":14,"line_start":7,"source_sha256":"689f6fe4f398f940cc2f32859383ba4f698f8bb218c12592de64faa5edad350a","target_id":"CLM-022"} -->
##### Principles

- Treat active-set matrices and support states as mechanics-solving concerns, not rule-pack compliance decisions.
- Keep friction, gap, lift-off, and one-way support behavior explicit in state and diagnostics rather than hidden in defaults.
- Use `TBD` for numerical tolerances, friction defaults, and exact data contracts until an authorized implementation brief supplies or derives them.
- Preserve result-envelope discipline from AB-00-03 and diagnostic discipline from AB-00-06.
- Use invented verification fixtures only; do not reproduce protected code examples, tables, or formulas.

<!-- sow-source-end -->

### CLM-023 — Considerations

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":20,"line_start":15,"source_sha256":"689f6fe4f398f940cc2f32859383ba4f698f8bb218c12592de64faa5edad350a","target_id":"CLM-023"} -->
##### Considerations

The future implementation will likely need to coordinate with linear support models, the frame stiffness kernel, solver diagnostics, and sparse solver behavior. Those are execution relationships for later work; this setup pass records them without editing other deliverables or implementing code.

Convergence reporting needs enough information for downstream diagnostics and reports to disclose unresolved non-convergence, assumptions, and limitations. It must not imply engineering approval or code compliance.

<!-- sow-source-end -->

### CLM-024 — Trade-offs

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":29,"line_start":21,"source_sha256":"689f6fe4f398f940cc2f32859383ba4f698f8bb218c12592de64faa5edad350a","target_id":"CLM-024"} -->
##### Trade-offs

| Topic | Setup guidance |
|---|---|
| Scope size | DEL-04-04 is large but remains one numerical domain per ContextBudgetQA. Split only if later implementation crosses package boundaries or expands beyond nonlinear support behavior. |
| Completeness vs invention | Prefer `TBD` over invented convergence tolerances, friction coefficients, or activation defaults. |
| Diagnostic detail | Favor structured diagnostic/result fields over prose-only errors so AB-00-06 and OPS-K-SOLVER-2 remain testable. |
| Test realism | Use invented mechanical examples sufficient for deterministic verification; do not copy protected benchmark tables or code examples. |

<!-- sow-source-end -->

### CLM-025 — Examples

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":33,"line_start":30,"source_sha256":"689f6fe4f398f940cc2f32859383ba4f698f8bb218c12592de64faa5edad350a","target_id":"CLM-025"} -->
##### Examples

Example cases are intentionally not specified in this setup pass. Future examples should use invented geometry, invented loads, and invented support properties, with explicit units and no protected standards content.

<!-- sow-source-end -->

### CLM-026 — Conflict Table (for human ruling)

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":39,"line_start":34,"source_sha256":"689f6fe4f398f940cc2f32859383ba4f698f8bb218c12592de64faa5edad350a","target_id":"CLM-026"} -->
##### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| None | No source conflict detected in setup pass. | N/A | N/A | N/A | N/A | N/A |

<!-- sow-source-end -->

### CLM-027 — D-41 R5 T7 PDU-054 current declaration

<!-- sow-source-begin {"disposition":"PRESERVED","file":"Guidance.md","line_end":42,"line_start":40,"source_sha256":"689f6fe4f398f940cc2f32859383ba4f698f8bb218c12592de64faa5edad350a","target_id":"CLM-027"} -->
##### D-41 R5 T7 PDU-054 current declaration

Earlier setup-era statements on this surface are retained as historical setup context where applicable; this section is the active current-state declaration. The nonlinear support slice and DEC-067 Coulomb-friction basis (`±mu*N`) are implemented and evidenced. Broader nonlinear policies and validation thresholds survive only where explicitly recorded; this currentness declaration is not an engineering acceptance.
<!-- sow-source-end -->

## Output and Evaluation Matrix

| Output | Objective refs | Requirement/claim refs | Acceptance refs | Verification refs | Evidence expectation |
|---|---|---|---|---|---|
| OUT-001 | SOW-012 OBJ-003 | CLM-008 | AC-001 | VER-001 | Claim map, parity report, and applicable verification evidence |

<!-- migration-authority: D-GOV-16@7584718aa32b112e415331736d1a8e68c12ac176 -->
