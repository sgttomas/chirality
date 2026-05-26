# Procedure — DEL-044-02 Package Datasheet (PKG-044 Instrumentation)

## Purpose

Operational steps for the EPC Integrator to produce, verify, and hand off the PKG-044 Package Datasheet at Gate 5, with verification hooks back to `Specification.md`.

## Prerequisites

- Access to:
  - `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_STATUS.md` for this deliverable.
  - PACKAGE_REGISTER.csv, INTERFACE_REGISTER.csv, DELIVERABLE_REGISTER.csv from the Gate 7 final published snapshot (`_REFERENCES.md`).
  - `_Sources/26020-Package_Requirements.docx` (Workbook row 46) and `_Sources/26020-Packages_Interfaces_4_export.xlsx`.
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (cited PKG-044 source basis).
  - Project specification index (for instrumentation specs ELC-QAS-000014-001, -000015-001, -000018-001).
- No declared upstream dependencies (per `_DEPENDENCIES.md`); confirm before draft.

## Steps

1. **Confirm identity.** Open PACKAGE_REGISTER.csv; locate the row where `PackageID = PKG-044`. Copy PackageID, WorkbookRow (46), WBS (02), CoATrackingNumber (26020-01-32-002), Discipline (Instrumentation), Name, ResponsibilityModel into Datasheet "Identification" and "Attributes" sections verbatim. Verifies R-044-02-01, R-044-02-03.
2. **Populate interface matrix.** Filter INTERFACE_REGISTER.csv for `PackageID = PKG-044`. Expect 5 rows. Insert each row's InterfaceID and InterfaceType into the Datasheet "Interfaces" table. Verifies R-044-02-02.
3. **Apply scope statements.** Copy the package register Inclusion Criteria and Exclusions verbatim into the Datasheet Attributes section. Insert the Gate 6 disposition sentence (from any of the PKG-044 INTERFACE_REGISTER rows) into the Interfaces section narrative. Verifies R-044-02-04, R-044-02-07.
4. **Populate Conditions.** From DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, transcribe the minimum design ambient (-40 deg C, line 145), analyzer-quality air spec (line 509), and cross-facility utility allocation note (line 716) into the Datasheet Conditions table with line-number citations. Verifies R-044-02-05, R-044-02-06.
5. **Equipment tag list.** Open `_Sources/26020-Package_Requirements.docx` and `_Sources/26020-Packages_Interfaces_4_export.xlsx` at the rows corresponding to Workbook row 46 for PKG-044. Enumerate tagged equipment, loop list, and I/O list. If source-supported, populate; otherwise leave `TBD` with the file pointer. Verifies R-044-02-08.
6. **Standards.** Add Standards section listing the three identified project instrumentation specifications (ELC-QAS-000014-001, ELC-QAS-000015-001, ELC-QAS-000018-001) citing DBM-Deepcut/4-25_Deepcut_DBM.md lines 2887-2891 and the project specification index. Verifies R-044-02-09.
7. **Cross-check.** Compare Datasheet content against `Specification.md` requirements R-044-02-01 through R-044-02-09 one by one. Resolve any inconsistency before handoff or capture it in `Guidance.md` Conflict Table.
8. **Handoff package.** Produce the vendor handoff bundle: `Datasheet.md` (this file's product) + `Specification.md` + `Guidance.md` + this `Procedure.md` + linked source citations. Transmit to vendor / discipline-package engineering. Record transmission in `MEMORY.md` (when created).

## Verification

| Check | Method | Pass criterion |
|---|---|---|
| Identity block matches PACKAGE_REGISTER.csv | Manual diff | Field-by-field match |
| Interface table count = 5 with correct types | Count / type set comparison | Exact set: {Process Piping, Utility Piping, Electrical Power, I&C / Control Cabling, Communications / Network} |
| Verbatim sentences present (responsibility model; Gate 6 disposition) | String search | Found exactly once |
| Design conditions cited to DBM line numbers | Citation audit | Each Conditions row has SourcePath + line reference |
| Tag list present or TBD with pointer | Section presence check | Section exists; values present OR TBD with file pointer |
| Standards section cites ELC-QAS-000014/015/018-001 | String search | All three IDs present |
| Conflict Table empty or populated with structured rows | Schema check | Conforms to columns defined in `Guidance.md` |

## Records

- `Datasheet.md` (this deliverable's primary artifact).
- `Specification.md`, `Guidance.md` (companion documents anchoring requirements and rationale).
- Verification log entries appended to `MEMORY.md` when created (and to `_STATUS.md` history when state transitions).
- Run record `_run_records/TASK_RUN_<timestamp>.md` capturing each authoring or revision run.
- Vendor / discipline transmittal record (out-of-scope filing system; recorded by reference).
