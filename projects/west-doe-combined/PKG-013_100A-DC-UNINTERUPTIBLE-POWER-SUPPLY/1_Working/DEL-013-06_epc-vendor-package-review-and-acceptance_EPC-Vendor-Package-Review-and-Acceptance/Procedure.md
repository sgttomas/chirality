# Procedure: DEL-013-06_epc-vendor-package-review-and-acceptance

## Purpose

Define the procedure for producing the four-document kit and the EPC Vendor Package Review and Acceptance evidence set for `DEL-013-06`, covering the `PKG-013` 100A DC UNINTERUPTIBLE POWER SUPPLY package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Deliverable-local truth set: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, `_SEMANTIC.md` (placeholder).
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Companion deliverable: `DEL-013-02_package-datasheet` (Package Datasheet) in its current state.
- EPC Scope of Work for `PKG-013` (when accessible) — `location TBD`.
- Construction Work Package for `PKG-013` (when accessible) — `location TBD`.
- Vendor data package for `PKG-013` (when accessible) — `location TBD`.
- Declared upstream/downstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state (`OPEN` or `INITIALIZED`) before generating or revising the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify against the `DEL-013-06_epc-vendor-package-review-and-acceptance` row in `DELIVERABLE_REGISTER.csv`.
3. Read `PACKAGE_REGISTER.csv` row `PKG-013` and carry forward identity, responsibility split, applicable interfaces, and objective support into the Datasheet.
4. Read `INTERFACE_REGISTER.csv` rows for `PKG-013` and confirm the four package interfaces (Electrical Power; Grounding / Bonding; Maintenance Access; Structural / Foundations / Supports) appear in the acceptance checklist scope.
5. Read the companion Package Datasheet `DEL-013-02_package-datasheet/Datasheet.md` and `Specification.md` to align identity, responsibility split, interface list, and `TBD` set.
6. Attempt to locate the EPC Scope of Work for `PKG-013` and the Construction Work Package for `PKG-013` in the accessible source set. If absent, mark dependent acceptance criteria as `TBD` and surface in the Guidance conflict table.
7. Draft `Datasheet.md` with identity, attributes, conditions, construction, and references. Cite only values supported by accessible sources; preserve unsupported values as `TBD`.
8. Draft `Specification.md` requirements REQ-013-06-001 through REQ-013-06-008 with explicit verification hooks. Cite the EPC SoW location as `TBD` rather than inventing clause references.
9. Draft `Guidance.md` with principles, considerations, trade-offs, illustrative examples, and a Conflict Table that records every unresolved source gap as a Human Ruling Required item.
10. Draft this `Procedure.md` so the production and acceptance sequence is repeatable.
11. Vendor review execution (for the operational use of this deliverable, once vendor data exists):
    a. For each vendor document received, log document name, revision, reviewer, disposition, and EPC SoW / Package Datasheet clause it satisfies (or `TBD`).
    b. For each of the four package interfaces, record a checklist disposition with supporting vendor evidence pointer.
    c. For test/inspection (FAT, SAT, electrical, grounding/bonding), record evidence pointers and acceptance against EPC SoW criteria (or `TBD`).
    d. For turnover (mechanical-complete, energization-readiness, handover-to-operations), record evidence pointers and acceptance against Construction Work Package criteria (or `TBD`).
12. Perform cross-document consistency checks for identity, interface list, responsibility split, and the `TBD` set across all four documents.
13. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
14. After successful Pass 1+2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe per the `four-documents` Step 7 rule. Append a History line.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Identity consistency | Identity fields match `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`. |
| Interface coverage | All four package interfaces from `INTERFACE_REGISTER.csv` rows for `PKG-013` appear in the acceptance scope and across documents. |
| Responsibility integrity | Vendor-owned and EPC-owned scopes are not conflated in any of the four documents. |
| Source-gap handling | EPC SoW and Construction Work Package gaps appear as `TBD` and as Conflict Table entries; no invented clause references. |
| Status-rule compliance | `_STATUS.md` modified only per the safe-update rule; no state regression. |
| Scope compliance | No files modified outside the deliverable folder. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history (this run's transition only)
- `_run_records/TASK_RUN_2026-05-24_*.md`
- (Operational, when vendor data exists) Vendor document review log, acceptance checklist, test/inspection evidence inventory, turnover evidence inventory.
