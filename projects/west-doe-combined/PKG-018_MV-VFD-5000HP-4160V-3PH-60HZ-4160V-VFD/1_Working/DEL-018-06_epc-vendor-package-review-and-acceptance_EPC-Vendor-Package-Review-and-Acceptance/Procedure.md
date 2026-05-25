# Procedure: DEL-018-06_epc-vendor-package-review-and-acceptance

## Purpose

Define the procedure for producing the four-document kit and the EPC Vendor Package Review and Acceptance evidence set for `DEL-018-06`, covering the `PKG-018` MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`.
- Deliverable-local truth set: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md`, `_SEMANTIC.md` (placeholder).
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Companion deliverables in `PKG-018/1_Working/`: `DEL-018-01_scope-of-work`, `DEL-018-02_package-datasheet`, `DEL-018-03_construction-work-package`, `DEL-018-04_vendor-engineered-equipment-package`, `DEL-018-05_vendor-document-turnover-package`.
- DBM compression/electrical context: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`.
- EPC Scope of Work clause set external to the project workspace (when accessible) — `location TBD`.
- Construction Work Package clause set external to the project workspace (when accessible) — `location TBD`.
- Vendor data package for `PKG-018` (when accessible) — `location TBD`.
- Declared upstream/downstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm `_STATUS.md` is in an overwrite-allowed state (`OPEN` or `INITIALIZED`) before generating or revising the four documents.
2. Read deliverable identity from `_CONTEXT.md` and verify against the `DEL-018-06_epc-vendor-package-review-and-acceptance` row in `DELIVERABLE_REGISTER.csv`.
3. Read `PACKAGE_REGISTER.csv` row `PKG-018` and carry forward identity, responsibility split, applicable interfaces, and objective support into the Datasheet.
4. Read `INTERFACE_REGISTER.csv` rows for `PKG-018` and confirm the six package interfaces (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) appear in the acceptance checklist scope.
5. Read the companion deliverables `DEL-018-01`, `DEL-018-02`, `DEL-018-03` (and `DEL-018-04`, `DEL-018-05` for context) to align identity, responsibility split, interface list, and `TBD` set.
6. Read DBM compression/electrical context (`_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`) for the motor and 4160V MCC basis, including the SCA-001 VE #34 starting-VFD basis and SCA-001 VE #37 capacitor-bank removal on MCC-8200.
7. Attempt to locate the EPC Scope of Work clause set and the Construction Work Package clause set in the accessible source set. If absent, mark dependent acceptance criteria as `TBD` and surface in the Guidance conflict table.
8. Draft `Datasheet.md` with identity, attributes, conditions, construction, and references. Cite only values supported by accessible sources; preserve unsupported values as `TBD`.
9. Draft `Specification.md` requirements REQ-018-06-001 through REQ-018-06-009 with explicit verification hooks. Cite EPC SoW / CWP locations as `TBD` rather than inventing clause references.
10. Draft `Guidance.md` with principles, considerations, trade-offs, illustrative examples, and a Conflict Table that records every unresolved source gap as a Human Ruling Required item.
11. Draft this `Procedure.md` so the production and acceptance sequence is repeatable.
12. Vendor review execution (for the operational use of this deliverable, once vendor data exists):
    a. For each vendor document received, log document name, revision, reviewer, disposition, and EPC SoW / Package Datasheet clause it satisfies (or `TBD`).
    b. For each of the six package interfaces, record a checklist disposition with supporting vendor evidence pointer.
    c. For test/inspection (FAT, SAT, dielectric/protective-relay, harmonic/reactive-power, control/communication interface, grounding/bonding), record evidence pointers and acceptance against EPC SoW criteria (or `TBD`).
    d. For harmonic and reactive-power behavior on the 4160V bus (DBM SCA-001 VE #37), record vendor-addressed evidence, EPC-study-addressed evidence, or `TBD`.
    e. For turnover (mechanical-complete, energization-readiness, control-system-integration, handover-to-operations), record evidence pointers and acceptance against Construction Work Package criteria (or `TBD`).
13. Perform cross-document consistency checks for identity, interface list, responsibility split, and the `TBD` set across all four documents.
14. If source disagreement or unsupported source ambiguity remains, add or update the Guidance Conflict Table and carry the item into the run record as `NEEDS_HUMAN_RULING`.
15. After successful Pass 1+2 completion, update `_STATUS.md` from `OPEN` to `INITIALIZED` only when the state transition is safe per the `four-documents` Step 7 rule. Append a History line.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document files exist | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` are present in the deliverable folder. |
| Default sections present | Datasheet has Identification, Attributes, Conditions, Construction, References; Specification has Scope, Requirements, Standards, Verification, Documentation; Guidance has Purpose, Principles, Considerations, Trade-offs, Examples; Procedure has Purpose, Prerequisites, Steps, Verification, Records. |
| Identity consistency | Identity fields match `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv`, and `PACKAGE_REGISTER.csv`. |
| Interface coverage | All six package interfaces from `INTERFACE_REGISTER.csv` rows for `PKG-018` appear in the acceptance scope and across documents. |
| Responsibility integrity | Vendor-owned and EPC-owned scopes are not conflated in any of the four documents. |
| Source-gap handling | EPC SoW, CWP, and vendor-data gaps appear as `TBD` and as Conflict Table entries; no invented clause references. |
| Harmonic/reactive coverage | REQ-018-06-007 is referenced in Datasheet conditions, Specification requirements, Guidance principles, and Procedure step 12d. |
| Status-rule compliance | `_STATUS.md` modified only per the safe-update rule; no state regression. |
| Scope compliance | No files modified outside the deliverable folder. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md` state history (this run's transition only)
- `_run_records/TASK_RUN_2026-05-24_*.md`
- (Operational, when vendor data exists) Vendor document review log, acceptance checklist, test/inspection evidence inventory, harmonic/reactive-power study evidence, turnover evidence inventory.
