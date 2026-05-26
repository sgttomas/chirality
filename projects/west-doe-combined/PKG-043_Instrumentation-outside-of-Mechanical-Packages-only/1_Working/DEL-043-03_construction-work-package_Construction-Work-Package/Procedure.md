# Procedure — DEL-043-03 Construction Work Package

This procedure describes how to **produce** the Construction Work Package deliverable artifact set for `PKG-043 Instrumentation (outside of Mechanical Packages only)`. Operational installation steps for individual instruments are out of scope for this deliverable and belong inside the produced CWP itself.

## Purpose

Produce the three CWP artifact classes (`_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 242):

1. Construction work package (master document).
2. Installation and tie-in workface plan.
3. Construction interface and turnover checklist.

…in a form that satisfies the requirements in `Specification.md` and respects the boundaries in `Guidance.md`.

## Prerequisites

**Declared upstream dependencies.** None declared during PREPARATION (`_DEPENDENCIES.md`). The following are *recommended* prerequisites based on cross-deliverable coherence inside `PKG-043` (ASSUMPTION; not declared edges):

- `DEL-043-01_scope-of-work` reaching at least `INITIALIZED` state, providing tagged equipment, package function, and integration narrative (`DELIVERABLE_REGISTER.csv` row 240).
- `DEL-043-02_package-datasheet` reaching at least `INITIALIZED` state, providing the package interface requirements matrix and source-supported equipment / design criteria (`DELIVERABLE_REGISTER.csv` row 241).

**Required references.**

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` in this deliverable folder.
- GATE-07 PROJECT_DECOMP snapshot: `DELIVERABLE_REGISTER.csv` (row 242), `PACKAGE_REGISTER.csv` (row 45), `SCOPE_LEDGER.csv` (row 45), `OBJECTIVE_SCOPE_MAP.csv`.

**Required access (currently `TBD`).** To advance items now marked `TBD` to FACT:

- Project construction specifications for instrumentation (location TBD).
- Facility area-classification basis (location TBD).
- Facility commissioning / turnover system structure (location TBD).
- Workbook Packages row 45 raw cells (`_Sources/26020-Package_Requirements.docx`, `26020-Packages_Interfaces_4_export.xlsx`) when slice access is available.

## Steps

1. **Load truth set.** Read `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and the GATE-07 register rows for this deliverable and its parent package. Record any deltas from this deliverable's drafted documents.
2. **Confirm scope and exclusions.** Restate the in/out scope and exclusions exactly as drafted in `Specification.md § Scope`. Resolve any conflict via the Conflict Table in `Guidance.md` before proceeding.
3. **Build the interface coverage matrix.** For each PKG-043 physical interface type (Process Piping; Utility Piping; Electrical Power; I&C / Control Cabling; Communications / Network — `PACKAGE_REGISTER.csv` row 45), list: counterparty package or system, interface point identifiers, readiness condition, witness/hold points, and turnover entry.
4. **Draft the master CWP document.** Use `Specification.md` requirements R-01 through R-11 as the section spine. For each requirement, write the construction-execution narrative and link to the source ITP, workface, and turnover artifacts.
5. **Draft the installation and tie-in workface plan.** Sequence workfaces consistent with WBS 01 (`PACKAGE_REGISTER.csv` row 45) and with the readiness windows from the interface coverage matrix. Where sequencing assumptions are unverified, mark `ASSUMPTION`.
6. **Draft the construction interface and turnover checklist.** Mirror the interface coverage matrix one-for-one and add the facility-turnover entries when the commissioning system structure is available (otherwise `TBD`).
7. **Build the objective traceability matrix.** Map every CWP section to the seven objectives listed on `DELIVERABLE_REGISTER.csv` row 242 (OBJ-001, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-010). Flag CONF-01 from `Guidance.md` until the human ruling is recorded.
8. **Resolve TBDs against governing standards.** When governing project construction specifications and area-classification documents become locally accessible, re-open requirements R-09 and R-10 and convert their ITP and hazardous-area content from `TBD` to source-grounded statements with `SourcePath` and `SectionRef`.
9. **Internal consistency sweep.** Run the cross-document consistency checks defined in the four-documents skill Step 5: Datasheet ↔ Specification, Specification ↔ Guidance, Specification ↔ Procedure, terminology, and values. Update the Conflict Table if anything cannot be resolved from drafts.
10. **Issue for review.** Submit the three artifact classes plus the supporting matrices for EPC Integrator internal review, then for human ruling on any open Conflict Table rows.

## Verification

- Section spine of the master CWP covers R-01 through R-11.
- Three artifact classes (CWP, workface plan, turnover checklist) are present and internally cross-referenced.
- Interface coverage matrix names all five PKG-043 interface types and lists no others.
- Objective traceability matrix accounts for all seven objectives from `DELIVERABLE_REGISTER.csv` row 242.
- Scope exclusions match `PACKAGE_REGISTER.csv` row 45 and the package name boundary.
- Every TBD has a named source dependency it would be cleared against.
- No statement in the CWP relies on a source that is not cited or marked `location TBD`.

## Records

- Master Construction Work Package document.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Interface coverage matrix.
- Objective traceability matrix.
- Conflict Table closure record (from `Guidance.md`) once human rulings are made.
- ITP and inspection records (produced during construction; out of scope for the deliverable artifact but referenced by it).
- Turnover acceptance records (produced during turnover; referenced by the turnover checklist).
