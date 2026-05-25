# Procedure: DEL-023-06_epc-vendor-package-review-and-acceptance

## Purpose

Define the procedure for producing the four-document kit and the EPC Vendor Package Review and Acceptance evidence set for `DEL-023-06`, covering the `PKG-023` MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Deliverable-local truth set: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, `_SEMANTIC.md` (placeholder).
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Companion in-project deliverables: `DEL-023-01` (EPC SoW), `DEL-023-02` (Package Datasheet), `DEL-023-03` (Construction Work Package), `DEL-023-04` (Vendor Engineered Equipment Package), `DEL-023-05` (Vendor Document Turnover Package) in their current states.
- EPC Scope of Work for `PKG-023` (external slice when accessible) — `location TBD`.
- Construction Work Package for `PKG-023` (external slice when accessible) — `location TBD`.
- Vendor data package for `PKG-023` (when accessible) — `location TBD`.
- Declared upstream/downstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state (`OPEN` or `INITIALIZED`) before generating or revising the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify against the `DEL-023-06_epc-vendor-package-review-and-acceptance` row in `DELIVERABLE_REGISTER.csv`.
3. Read `PACKAGE_REGISTER.csv` row `PKG-023` and carry forward identity, responsibility split, applicable interfaces, and objective support into the Datasheet.
4. Read `INTERFACE_REGISTER.csv` rows for `PKG-023` and confirm the six package interfaces (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) appear in the acceptance checklist scope.
5. Read the companion Package Datasheet `DEL-023-02_package-datasheet/Datasheet.md` and `Specification.md` (when drafted) to align identity, responsibility split, interface list, and `TBD` set. If `DEL-023-02` is still `OPEN`, record this as a current blocker for substantive acceptance evidence.
6. Attempt to locate external EPC Scope of Work and Construction Work Package source slices for `PKG-023`. If absent, mark dependent acceptance criteria as `TBD` and surface in the Guidance conflict table.
7. Read DBM-Deepcut electrical sections (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) covering 4.16 kV MCC, MV VFDs, Zone 2 area marking, and VFD-fed cable selection, to establish background design basis.
8. Draft `Datasheet.md` with identity, attributes, conditions, construction, and references. Cite only values supported by accessible sources; preserve unsupported values as `TBD`.
9. Draft `Specification.md` requirements REQ-023-06-001 through REQ-023-06-008 with explicit verification hooks. Cite the EPC SoW location as `TBD` rather than inventing clause references.
10. Draft `Guidance.md` with principles, considerations, trade-offs, illustrative examples, and a Conflict Table that records every unresolved source gap as a Human Ruling Required item.
11. Draft this `Procedure.md` so the production and acceptance sequence is repeatable.
12. Vendor review execution (for the operational use of this deliverable, once vendor data exists):
    a. For each vendor document received, log document name, revision, reviewer, disposition, and EPC SoW / Package Datasheet clause it satisfies (or `TBD`).
    b. For each of the six package interfaces, record a checklist disposition with supporting vendor evidence pointer (one row per interface ID from `INTERFACE_REGISTER.csv`).
    c. For test/inspection (FAT, SAT, electrical, grounding/bonding, harmonic verification where vendor design includes it), record evidence pointers and acceptance against EPC SoW criteria (or `TBD`).
    d. For turnover (mechanical-complete, energization-readiness, handover-to-operations), record evidence pointers and acceptance against Construction Work Package criteria (or `TBD`).
13. Perform cross-document consistency checks for identity, interface list, responsibility split, and the `TBD` set across all four documents.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful Pass 1+2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe per the `four-documents` Step 7 rule. Append a History line.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Identity consistency | Identity fields match `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`. |
| Interface coverage | All six package interfaces from `INTERFACE_REGISTER.csv` rows for `PKG-023` appear in the acceptance scope and across documents. |
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
