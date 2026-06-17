# Source Pack: SRC-DEL-DEL-04-04-NONLINEAR-SUPPORT-ACTIVE-SET-SOLVER

Grouping: `GROUPED_DELIVERABLE`  RepoGlob: `execution/PKG-04_Solver Core and Numerical Methods/1_Working/DEL-04-04_Nonlinear support active-set solver/`

Source truth remains the original repo component files listed under each
component heading. This generated markdown is a DOMAIN_DECOMP review and
worker substrate only.

## Component: execution/PKG-04_Solver Core and Numerical Methods/1_Working/DEL-04-04_Nonlinear support active-set solver/Datasheet.md

### Datasheet: DEL-04-04 Nonlinear support active-set solver

#### Identification

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

#### Attributes

| Attribute | Value | Source |
|---|---|---|
| Solver role | Iterative activation for nonlinear support behavior in the global 3D centerline/frame solver. | _CONTEXT.md Description; ScopeLedger.csv SOW-012 |
| Covered behavior categories | One-way supports, gaps, lift-off, and friction. | Deliverables.csv DEL-04-04; ScopeLedger.csv SOW-012 |
| Reporting obligation | Convergence reporting, active-set state, and unresolved non-convergence reporting are in scope. | CONTRACT.md OPS-K-SOLVER-2; _CONTEXT.md Description |
| Anticipated artifacts | Nonlinear solver loop; convergence tests. | _CONTEXT.md Anticipated Artifacts |
| Explicit deferrals | Exact solver numerical library, detailed convergence criteria, and implementation-level defaults are TBD. | _CONTEXT.md Architecture Basis Injection; human brief hard stops |

#### Conditions

| Condition | Status |
|---|---|
| The primary mechanics model remains a 3D centerline/frame model. | Required by OPS-K-MECH-1. |
| The solver computes mechanics and does not decide professional compliance. | Required by OPS-K-MECH-2 and package exclusions. |
| Missing solve-required values are findings, not silent defaults. | Required by OPS-K-DATA-2. |
| Unit-bearing quantities must be unit-aware and dimensionally checked. | Required by OPS-K-UNIT-1. |
| Nonlinear convergence tolerances, friction defaults, and case-specific values are not invented in this setup kit. | Required by OPS-K-AGENT-1 and human hard stops. |

#### Construction

This setup kit defines a documentation boundary for a future nonlinear active-set solver deliverable. It does not implement solver code.

| Construction element | Local setup position |
|---|---|
| Active-set iteration loop | In scope for future implementation; algorithm details TBD. |
| Support activation state model | In scope for future implementation; exact data contract TBD. |
| Gap/lift-off/one-way state transitions | In scope for future implementation; rules must be evidence-backed and tested. |
| Friction behavior | In scope as a named behavior category; numerical model, defaults, and limits are TBD. |
| Convergence reporting | Required output surface; result-envelope integration follows AB-00-03 and diagnostics follow AB-00-06. |
| Convergence tests | Required anticipated artifact; deterministic verification follows OPS-K-SOLVER-1 and AB-00-08. |

#### References

- _CONTEXT.md for sealed deliverable identity, scope, objective, and architecture basis.
- docs/_Registers/Deliverables.csv row DEL-04-04.
- docs/_Registers/ScopeLedger.csv row SOW-012.
- docs/_Registers/ContextBudgetQA.csv row DEL-04-04.
- execution/_Decomposition/SOFTWARE_DECOMP.md` revision 0.7 rows for PKG-04, DEL-04-04, SOW-012, OBJ-003, and AB-00-01/02/03/06/08.
- docs/CONTRACT.md invariants OPS-K-MECH-1, OPS-K-MECH-2, OPS-K-UNIT-1, OPS-K-SOLVER-1, OPS-K-SOLVER-2, OPS-K-DATA-2, OPS-K-REPORT-1, and OPS-K-AGENT-1 through OPS-K-AGENT-4.

## Component: execution/PKG-04_Solver Core and Numerical Methods/1_Working/DEL-04-04_Nonlinear support active-set solver/Guidance.md

### Guidance: DEL-04-04 Nonlinear support active-set solver

#### Purpose

This deliverable prepares a future nonlinear support active-set solver slice within PKG-04. Its value is to keep nonlinear mechanical behavior, diagnostics, unit handling, and result reporting bounded before implementation work begins.

#### Principles

- Treat active-set matrices and support states as mechanics-solving concerns, not rule-pack compliance decisions.
- Keep friction, gap, lift-off, and one-way support behavior explicit in state and diagnostics rather than hidden in defaults.
- Use `TBD` for numerical tolerances, friction defaults, and exact data contracts until an authorized implementation brief supplies or derives them.
- Preserve result-envelope discipline from AB-00-03 and diagnostic discipline from AB-00-06.
- Use invented verification fixtures only; do not reproduce protected code examples, tables, or formulas.

#### Considerations

The future implementation will likely need to coordinate with linear support models, the frame stiffness kernel, solver diagnostics, and sparse solver behavior. Those are execution relationships for later work; this setup pass records them without editing other deliverables or implementing code.

Convergence reporting needs enough information for downstream diagnostics and reports to disclose unresolved non-convergence, assumptions, and limitations. It must not imply engineering approval or code compliance.

#### Trade-offs

| Topic | Setup guidance |
|---|---|
| Scope size | DEL-04-04 is large but remains one numerical domain per ContextBudgetQA. Split only if later implementation crosses package boundaries or expands beyond nonlinear support behavior. |
| Completeness vs invention | Prefer `TBD` over invented convergence tolerances, friction coefficients, or activation defaults. |
| Diagnostic detail | Favor structured diagnostic/result fields over prose-only errors so AB-00-06 and OPS-K-SOLVER-2 remain testable. |
| Test realism | Use invented mechanical examples sufficient for deterministic verification; do not copy protected benchmark tables or code examples. |

#### Examples

Example cases are intentionally not specified in this setup pass. Future examples should use invented geometry, invented loads, and invented support properties, with explicit units and no protected standards content.

#### Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| None | No source conflict detected in setup pass. | N/A | N/A | N/A | N/A | N/A |

## Component: execution/PKG-04_Solver Core and Numerical Methods/1_Working/DEL-04-04_Nonlinear support active-set solver/Procedure.md

### Procedure: DEL-04-04 Nonlinear support active-set solver

#### Purpose

Define the documentation setup procedure for DEL-04-04 without implementing nonlinear solver code.

#### Prerequisites

- Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Apply docs/CONTRACT.md invariants OPS-K-MECH-1, OPS-K-MECH-2, OPS-K-UNIT-1, OPS-K-SOLVER-1, OPS-K-SOLVER-2, OPS-K-DATA-2, OPS-K-REPORT-1, and OPS-K-AGENT-1 through OPS-K-AGENT-4.
- Apply architecture basis AB-00-01, AB-00-02, AB-00-03, AB-00-06, and AB-00-08.
- Keep all writes inside the DEL-04-04 folder.

#### Steps

1. Confirm the deliverable identity is DEL-04-04 under PKG-04.
2. Confirm the setup scope is documentation only: four documents, semantic files, dependency artifacts, and run records.
3. Capture nonlinear support behavior categories from SOW-012 and the deliverables register: one-way supports, gaps, lift-off, and friction.
4. Record future implementation needs as `TBD` when exact numerical library choices, convergence thresholds, friction defaults, or data contracts are not provided.
5. Preserve mechanics/reporting boundaries: mechanics solved by solver, acceptability handled by rule packs or humans, and no compliance/certification claims.
6. Generate dependency rows only from explicit scope, architecture, invariant, or local-document evidence.
7. Run local schema validation for `Dependencies.csv`.

#### Verification

- Four production documents exist and retain Datasheet, Specification, Guidance, and Procedure roles.
- `_SEMANTIC.md` exists and separates semantic lensing from engineering authority.
- `_SEMANTIC_LENSING.md` exists and records warranted enrichment items without rewriting production documents.
- `Dependencies.csv` validates against v3.1 schema.
- `_STATUS.md` is not advanced to `ISSUED`.

#### Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_SEMANTIC.md`
- `_SEMANTIC_LENSING.md`
- `Dependencies.csv`
- `_DEPENDENCIES.md`
- `_run_records/TASK_RUN_2026-04-30_1015_*.md`

## Component: execution/PKG-04_Solver Core and Numerical Methods/1_Working/DEL-04-04_Nonlinear support active-set solver/Specification.md

### Specification: DEL-04-04 Nonlinear support active-set solver

#### Scope

DEL-04-04 covers the future implementation surface for iterative activation of nonlinear support behavior: one-way supports, gaps, lift-off, friction, and convergence reporting. This setup kit is documentation-only and does not implement solver logic, set numerical tolerances, choose friction defaults, or make certification/compliance claims.

#### Requirements

| ID | Requirement | Source | Verification |
|---|---|---|---|
| DEL-04-04-REQ-01 | The deliverable shall preserve the 3D centerline/frame mechanics boundary for global piping analysis. | OPS-K-MECH-1; PKG-04 package scope | Architecture and solver-boundary tests confirm no local FEA substitution is introduced. |
| DEL-04-04-REQ-02 | The nonlinear support solver shall address one-way restraints, lift-off, gaps, and friction through a controlled iterative method. | SOW-012; Deliverables.csv DEL-04-04 | Convergence tests cover invented representative cases for each behavior category. |
| DEL-04-04-REQ-03 | The future implementation shall report convergence state, active-set state, and unresolved non-convergence. | OPS-K-SOLVER-2; AB-00-06 | Result-envelope and diagnostic tests assert reported state fields and warning class behavior. |
| DEL-04-04-REQ-04 | Solver changes shall have deterministic verification tests before release use. | OPS-K-SOLVER-1; AB-00-08 | Test inventory includes nonlinear support loop and convergence/non-convergence regression cases. |
| DEL-04-04-REQ-05 | Missing solve-required nonlinear support inputs shall be explicit findings, never silent defaults. | OPS-K-DATA-2; AB-00-06 | Negative tests assert missing data produces diagnostics rather than assumed values. |
| DEL-04-04-REQ-06 | Unit-bearing support, displacement, force, and friction-related quantities shall be unit-aware and dimensionally checked where applicable. | OPS-K-UNIT-1 | Unit tests cover accepted, rejected, and missing unit metadata. |
| DEL-04-04-REQ-07 | The solver shall compute mechanics only; rule-pack acceptability and professional compliance remain outside this deliverable. | OPS-K-MECH-2; package exclusions | Reports and result labels avoid compliance/certification language. |
| DEL-04-04-REQ-08 | Result and diagnostic outputs shall support report disclosure of solver version, warnings, assumptions, limitations, and provenance notes. | OPS-K-REPORT-1; AB-00-06 | Report-facing fixture tests confirm required metadata is present or explicitly TBD. |
| DEL-04-04-REQ-09 | Implementation choices for solver numerical library, convergence tolerances, friction defaults, and exact data contracts remain TBD until later authorized work. | _CONTEXT.md Still TBD; OPS-K-AGENT-1; human hard stops | Review confirms no invented values or defaults appear in setup artifacts. |

#### Standards

No protected standards text, formulas, tables, examples, or code-specific values are included in this setup kit. Public/protected data boundaries follow docs/CONTRACT.md. Any later code-specific or project-specific engineering values must be user-supplied or lawfully imported private data where applicable.

#### Verification

Future verification shall include deterministic invented-example tests for active-set activation/deactivation, gap closure/opening, lift-off, one-way support behavior, friction state reporting, convergence, and non-convergence diagnostics. Exact pass/fail thresholds, test matrices, and numerical tolerances are TBD and must not be invented by this setup pass.

#### Documentation

Required documentation artifacts for this setup are `Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`, `_SEMANTIC.md`, `_SEMANTIC_LENSING.md`, `_DEPENDENCIES.md`, `Dependencies.csv`, and `_run_records/`. Future implementation artifacts remain outside this setup task.
