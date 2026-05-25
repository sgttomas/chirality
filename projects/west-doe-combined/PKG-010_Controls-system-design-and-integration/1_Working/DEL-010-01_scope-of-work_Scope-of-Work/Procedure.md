# Procedure: DEL-010-01_scope-of-work - Scope of Work

## Purpose

Define the bounded procedure for producing and checking the `DEL-010-01_scope-of-work` package SOW for `PKG-010` Controls system design and integration.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Workbook row 11 in `_Sources/26020-Packages_Interfaces_4_export.xlsx` is available.
- Gate 7 `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and objective maps are available.
- Relevant DBM source slices are available from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, especially SEC-13, SEC-14, and SEC-15.
- Declared upstream dependencies: none declared during PREPARATION.
- Declared downstream dependencies: none declared during PREPARATION.

## Steps

1. Confirm package identity from `_CONTEXT.md`, Gate 7 `DELIVERABLE_REGISTER.csv`, Gate 7 `PACKAGE_REGISTER.csv`, and workbook row 11.
2. Record package identity fields: `PKG-010`, workbook ID 10, workbook row 11, WBS 03, CoA tracking number `26020-01-32-001`, package name `Controls system design and integration`, discipline `Controls`, and deliverable type `EPC Scope of Work`.
3. Establish the SOW artifact set from Gate 7 `ARTIFACT_REGISTER.csv`: package scope of work, tagged equipment/package identity list, package function and whole-facility integration narrative, and responsibility assignment record.
4. Extract source-supported interface facts from workbook row 11 and Gate 7 `INTERFACE_REGISTER.csv` rows for `PKG-010`.
5. Carry the full applicable interface list into the SOW: Process Piping; Utility Piping; Relief / Flare / Vent; Electrical Power; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems.
6. Draft the package function narrative using DBM SEC-13: centralized monitoring and control for the 03-25 Compressor Station and Liquids Hub; BPCS primary process control except compression Unit Control Systems, which remain standalone and integrated for monitoring/alarming.
7. Draft the communications/network basis using DBM SEC-13: segregated I/O network, redundant Ethernet communications, and Parallel Redundancy Protocol.
8. Draft the instrument-air and shutdown-interface notes using DBM SEC-13 and SEC-14. Mark final package data maps, permissive logic, trip interfaces, alarm priorities, trip lists, shutdown levels, cause-and-effect actions, and reset responsibilities as detailed-design/vendor-integration deliverables.
9. Preserve the Gate 6 disposition for controls power-panel interfaces: keep them as interface facts/artifacts under the package datasheet; do not create a separate package or deliverable.
10. Mark unsupported values `TBD`, including detailed tagged equipment, package-specific exclusions, final logic values, and final responsibility split between EPC Integrator and any discipline subcontractor.
11. Cross-check the SOW against the Datasheet, Specification, and Guidance so package identity, interface lists, deferred values, and human ruling items are consistent.

## Verification

| Check | Acceptance basis |
|---|---|
| Package identity matches accepted truth | `_CONTEXT.md`, workbook row 11, Gate 7 `PACKAGE_REGISTER.csv`, and Gate 7 `DELIVERABLE_REGISTER.csv` agree. |
| Interface list is complete | All eight `PKG-010` interface types in Gate 7 `INTERFACE_REGISTER.csv` appear in the SOW documents. |
| Controls narrative is source-grounded | DBM SEC-13 supports BPCS role, standalone compression Unit Control Systems, I/O network segregation, redundant Ethernet, PRP, and final vendor-integration data map/trip/alarm resolution. |
| Shutdown and fire/gas handling is not overstated | DBM SEC-14 deferred trip lists, shutdown levels, cause-and-effect actions, and reset responsibilities remain marked as detailed-design deliverables. |
| Unavailable data is not invented | Detailed tagged equipment, package-specific exclusions, and final execution responsibility split are marked `TBD` or routed to the Conflict Table. |
| Declared dependencies are respected | No blockers are asserted because `_DEPENDENCIES.md` declares no upstream or downstream dependencies. |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md`
- `_run_records/TASK_RUN_2026-05-24_1657.md`
- Source evidence: Gate 7 snapshot records, workbook row 11, and DBM SEC-13/SEC-14/SEC-15 source slices.
