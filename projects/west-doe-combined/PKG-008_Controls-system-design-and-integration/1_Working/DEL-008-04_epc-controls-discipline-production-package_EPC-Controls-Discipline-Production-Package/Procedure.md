# Procedure: EPC / Controls Discipline Production Package

## Purpose

This procedure defines how to produce and verify the DEL-008-04 controls discipline production package using the accepted Gate 7 snapshot and accessible controls source slices.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md` are available.
- Source materials are locally accessible:
  - `26020-Packages_Interfaces_4_export.xlsx`, Packages sheet row 9;
  - Gate 7 registers for PKG-008 and DEL-008-04;
  - `4-25_Deepcut_DBM.md`, SEC-13 Controls System Basis, SEC-14 instrumented protection basis, and relevant SEC-12 electrical/control interface sections;
  - `3-25_Comp_and_Liquids_DBM.md`, SEC-13 Control System Basis as supporting shared-interface context.
- Declared upstream dependencies: none.

## Steps

1. Confirm deliverable identity.
   - Verify DEL-008-04, PKG-008, SOW-0008, discipline Controls, and type EPC/Discipline Production Unit against `_CONTEXT.md` and Gate 7 `DELIVERABLE_REGISTER.csv`.

2. Confirm package source row and interface facts.
   - Verify workbook Packages row 9 and Gate 7 `PACKAGE_REGISTER.csv` identify Controls system design and integration under WBS 01, CoA tracking number 26020-01-32-001.
   - Record interface types from Gate 7 `INTERFACE_REGISTER.csv`.
   - Carry the controls power-panel interface note and Gate 6 disposition.

3. Establish controls source basis.
   - Use DBM-Deepcut SEC-13 as the primary controls architecture source for PKG-008.
   - Use 3-25 SEC-13 only for supporting shared-interface context unless a later accepted source assigns it direct authority.
   - Record source sections used in the production package basis.

4. Build the requirements closure record.
   - Extract requirements only where supported by Gate 7 registers or DBM controls sections.
   - Mark missing values as `TBD`.
   - Label any inference as `ASSUMPTION`.
   - Keep detailed-design items open, including Remote I/O cabinet locations, DLR versus PRP selection, controller sizing/quantity, final package data maps, permissive logic, trip interfaces, and alarm priorities.

5. Build the discipline deliverable register.
   - Enter `TBD` for unenumerated internal controls deliverables.
   - Do not invent drawing, configuration, FAT/SAT, or turnover document lists unless a source or human ruling provides them.

6. Check cross-document consistency.
   - Confirm Datasheet attributes appear in Specification requirements where appropriate.
   - Confirm Specification requirements have Procedure verification hooks.
   - Confirm Guidance does not overstate unresolved detailed-design decisions.
   - Confirm all conflicting or unresolved source issues appear in the Guidance conflict table.

7. Prepare for handoff or review.
   - Package the production basis, TBD register, requirements closure record, interface list, conflict table, and source references for controls authority review.

## Verification

| Check | Acceptance basis |
|---|---|
| Identity check | DEL-008-04, PKG-008, SOW-0008, and Controls discipline match `_CONTEXT.md` and Gate 7 registers. |
| Source check | Every non-trivial requirement cites Gate 7 registers or DBM source sections. |
| Interface check | PKG-008 interface types and controls power-panel note are present. |
| TBD check | Unresolved detailed-design and discipline-register items remain marked `TBD` or appear in the conflict table. |
| Consistency check | Datasheet, Specification, Guidance, and Procedure use the same terminology and do not conflict on controller, network, Modbus, or safety-interface basis. |

## Records

- Discipline production package basis.
- TBD discipline deliverable register.
- Source-limited requirements closure record.
- PKG-008 interface list and controls power-panel note disposition.
- Human ruling items HRR-001 and HRR-002 from `Guidance.md`.
- Source reference list and verification notes.
