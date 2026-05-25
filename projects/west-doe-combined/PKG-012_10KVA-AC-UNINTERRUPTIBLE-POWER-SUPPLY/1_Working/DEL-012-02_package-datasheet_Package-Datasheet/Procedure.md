# Procedure: Produce the Package Datasheet

## Purpose

Define the bounded procedure for producing and checking the EPC Integrator Package Datasheet for `DEL-012-02_package-datasheet`, the `PKG-012` 10KVA AC UNINTERRUPTIBLE POWER SUPPLY package.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local files `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Declared upstream dependencies: none declared during PREPARATION.
- Declared downstream dependencies: none declared during PREPARATION.
- Source-control rule: do not reinterpret raw source corpus in this Phase 2.2 run; consume Gate 7 and existing deliverable context as accepted upstream truth.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md` and DELIVERABLE_REGISTER.csv:
   - Deliverable ID: `DEL-012-02_package-datasheet`.
   - Parent package: `PKG-012`.
   - Package name: `10KVA AC UNINTERRUPTIBLE POWER SUPPLY`.
   - Responsible party: `EPC Integrator`.
2. Confirm package basis from PACKAGE_REGISTER.csv:
   - Workbook ID `12`, workbook row `14`, WBS `02`, tracking number `26020-02-30-003`.
   - Discipline `Electrical`.
   - Package Vendor / EPC Integrator responsibility boundary.
3. Populate datasheet identification and scope fields from accepted Gate 7 and deliverable-local context.
4. Populate the interface requirements matrix with only the Gate 7 interface facts for PKG-012:
   - Electrical Power.
   - Grounding / Bonding.
   - Maintenance Access.
   - Structural / Foundations / Supports.
5. Populate the vendor handoff basis with accepted responsibility and boundary language.
6. Mark all unsupported package-specific values as `TBD`, including voltage, phase, frequency, battery autonomy, battery type, bypass, environmental ratings, installation location, footprint, weights, heat rejection, anchorage, testing criteria, and detailed vendor document requirements.
7. Cross-check Datasheet.md, Specification.md, Guidance.md, and Procedure.md for consistent package name, IDs, responsibility language, interface list, source references, and TBD treatment.
8. Record human ruling items for missing source-supported technical values or standards.

## Verification

| Check | Acceptance criterion |
|---|---|
| Identity | Datasheet identity matches _CONTEXT.md, PACKAGE_REGISTER.csv, and DELIVERABLE_REGISTER.csv. |
| Interface coverage | All four Gate 7 interface facts are present and no unsupported interface facts are added. |
| Responsibility boundary | Package Vendor and EPC Integrator responsibilities match PACKAGE_REGISTER.csv and PROJECT_DECOMP.md. |
| Source fidelity | Unsupported technical details are marked `TBD` or captured in Guidance.md Conflict Table. |
| Dependency handling | No advisory blocker is asserted because no declared dependency edges exist. |
| Cross-document consistency | Datasheet, Specification, Guidance, and Procedure use consistent terminology and values. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md`
- `_run_records/TASK_RUN_2026-05-24_1702.md`
