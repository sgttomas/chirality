# Procedure: DEL-010-02_package-datasheet — Package Datasheet

## Purpose

This procedure defines how to produce and verify the Controls system design and integration package datasheet for `DEL-010-02_package-datasheet`.

## Prerequisites

| Prerequisite | Status | Source |
|---|---|---|
| Accepted decomposition snapshot | Available: Gate 7 final published PROJECT_DECOMP snapshot dated 2026-05-24. | `_CONTEXT.md`; `_REFERENCES.md` |
| Deliverable-local context | Available. | `_CONTEXT.md` |
| Deliverable-local references | Available, with no deliverable-specific source slices copied during PREPARATION. | `_REFERENCES.md` |
| Declared upstream dependencies | None declared. | `_DEPENDENCIES.md` |
| Workbook interface source | Available: `26020-Packages_Interfaces_4_export.xlsx`, sheet1 row 11. | `_REFERENCES.md`; shared `_Sources` root |
| DBM controls/electrical/instrumentation source | Available: `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`. | `_REFERENCES.md`; shared `_Sources` root |

## Steps

1. Confirm deliverable identity from `_CONTEXT.md` and Gate 7 `DELIVERABLE_REGISTER.csv`.
2. Confirm artifact expectations from Gate 7 `ARTIFACT_REGISTER.csv` rows for `DEL-010-02_package-datasheet`.
3. Extract package interface categories from `26020-Packages_Interfaces_4_export.xlsx`, sheet1 row 11.
4. Cross-check the package interface categories against Gate 7 `INTERFACE_REGISTER.csv` rows for `PKG-010`.
5. Record the Gate 7 disposition that controls power-panel interface facts remain under the package datasheet and do not create a separate package/deliverable.
6. Extract controls architecture fields from DBM SEC-13:
   - BPCS centralized monitoring/control basis.
   - Standalone Unit Control System handling for compression unit controls.
   - PCN, I/O Network, IDMZ, Enterprise Network, PRP, and dual-uplink network basis.
   - Allen-Bradley ControlLogix 1756-L8x BPCS platform.
   - Allen-Bradley Flex5000 Remote I/O basis.
   - Package protocol/hardwired-signal distinction and Modbus monitoring-only constraint.
7. Extract supporting electrical/building interface fields from DBM SEC-12 and SEC-09:
   - Shared cross-facility electrical utility basis.
   - Electrical power, MCC, cable separation, lighting, heat tracing, building heater, HVAC/ventilation, and RIO interface coordination topics.
8. Extract fire/gas/safety interface fields from DBM SEC-14:
   - Fire/gas/H2S/LEL/methyl mercaptan/ESD/unit shutdown interface topics.
   - Remote I/O wiring basis where practical.
   - Detailed-design gaps for detector quantity, set points, voting, trip lists, shutdown levels, reset responsibilities, and cause/effect logic.
9. Populate the datasheet and supporting specification/guidance/procedure documents.
10. Mark unsupported detailed-design or vendor-integration fields as `TBD`.
11. Run a cross-document consistency check:
    - Interface categories match across all four documents.
    - Requirements have verification hooks.
    - Guidance does not overstate source support.
    - Procedure steps do not create unsourced design requirements.
12. Preserve any unresolved authority question in `Guidance.md` under `Conflict Table (for human ruling)`.

## Verification

| Check | Acceptance criterion |
|---|---|
| Four-document presence | `Datasheet.md`, `Specification.md`, `Guidance.md`, and `Procedure.md` exist. |
| Default section presence | Each document retains the four-documents default schema sections. |
| Source traceability | Non-trivial requirements and values cite Gate 7, workbook row 11, or DBM section references. |
| Interface consistency | The same eight package interface categories appear in the datasheet/specification/procedure basis. |
| TBD handling | Unsupported data maps, trips, alarms, detector details, network addressing, VLANs, policies, and model details remain `TBD`. |
| Dependency handling | No blockers are asserted because no declared upstream dependencies exist. |
| Status transition | If current state is `OPEN`, `_STATUS.md` may be updated to `INITIALIZED` after the four documents are produced. |

## Records

Retain these records with the deliverable:

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md`
- `_run_records/TASK_RUN_*.md`
- Source reference list in `_REFERENCES.md`
- Human ruling item `HRR-010-02-001` until confirmed or superseded by later accepted authority
