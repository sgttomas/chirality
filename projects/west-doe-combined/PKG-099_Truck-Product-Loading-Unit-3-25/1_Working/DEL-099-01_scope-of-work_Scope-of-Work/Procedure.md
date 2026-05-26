# Procedure — DEL-099-01 Scope of Work (PKG-099 Truck Product Loading Unit 3-25)

> Operational view of how to produce (and verify) the EPC Integrator Scope of Work artifact for PKG-099.
> Steps are drawn from `Specification.md` requirements and accessible sources. Items requiring human judgement are marked `TBD` and surfaced via the Conflict Table in `Guidance.md`.

## Purpose

Define the repeatable production procedure that yields a compliant Scope of Work document satisfying `R-1` through `R-12` in `Specification.md` and producing the artifacts enumerated in `_CONTEXT.md` (Anticipated Artifacts) and the `ARTIFACT_REGISTER.csv` rows for DEL-099-01.
Source: `_CONTEXT.md`; `Specification.md` (this folder); `ARTIFACT_REGISTER.csv`.

## Prerequisites

1. Read these files (this deliverable folder):
   - `_CONTEXT.md`
   - `_REFERENCES.md`
   - `_DEPENDENCIES.md` (Declared Upstream/Downstream — both currently "None declared")
   - `_STATUS.md`
2. Read the accepted decomposition snapshot rows for PKG-099 / DEL-099-01:
   - `DELIVERABLE_REGISTER.csv` (DEL-099-01 row)
   - `PACKAGE_REGISTER.csv` (PKG-099 row)
   - `ARTIFACT_REGISTER.csv` (PKG-099 rows)
   - `INTERFACE_REGISTER.csv` (PKG-099 rows)
3. Open accessible source material:
   - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — sections SEC-01, SEC-05, SEC-06, SEC-12, SEC-13, SEC-15, SEC-17.
4. Note inaccessible sources (carry as `location TBD`; do not fabricate values):
   - `_Sources/26020-Package_Requirements.docx` heading 51
   - `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 98
   - RFQ `26020-03-PT-RFQ-23-001_Truck_Load_stn_R0.docx`

## Steps

### S-1 — Establish package identity (R-2)

1. Populate the identity block (Workbook ID 99, row 98; CoA `26020-03-23-001`; WBS 03; Discipline Mechanical; Tag Name `26020-03-PT-23-001 - Condensate Truck Loading Stations`).
2. Cite `PACKAGE_REGISTER.csv` PKG-099 row.

### S-2 — Capture package function statement (R-1, R-6)

1. Use the workbook-derived function statement verbatim for the Function paragraph.
2. Add a one-paragraph whole-facility integration narrative covering: Liquids Hub upstream supply, parallel disposition vs NRM LACT custody transfer, shared utilities/F&G/drainage interfaces.
3. Cite `PACKAGE_REGISTER.csv` PKG-099 row and `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-01, SEC-06.

### S-3 — Enumerate tagged equipment (R-3)

1. List Truck Loading/Unloading Stations, basket strainer (Sureflow 0300BF300SS, 316SS, mesh screen), ESDV, flow transmitters from `ARTIFACT_REGISTER.csv` ART-517D0E9F90.
2. For the station-count attribute, reference Conflict Table entry **CT-01** in `Guidance.md` and carry both candidate values (2 stations 2x2 per workbook/RFQ; 3 stations per DBM) until human ruling.

### S-4 — Record design basis values (R-4, R-5)

1. Per-station loading capacity: 103 m3/h at 345 kPad differential — cite DBM SEC-06.
2. One condensate loading pump per truck-loading station — cite DBM SEC-06.
3. Mark both as **ASSUMPTION** until corroborated by RFQ/Package Requirements extraction (CT-02).

### S-5 — Record responsibility assignment (R-7)

1. State Package Vendor scope vs EPC Integrator scope per `PACKAGE_REGISTER.csv` PKG-099 Responsibility column.
2. Cite `ARTIFACT_REGISTER.csv` ART-B927725D35.

### S-6 — Enumerate applicable interfaces (R-9)

1. Produce a table of the eleven applicable interface types and `IFC-*` IDs (see `Datasheet.md` Applicable Interfaces).
2. Cite `INTERFACE_REGISTER.csv` rows.
3. Defer interface-level requirements to `DEL-099-02_package-datasheet` per principle 5 in `Guidance.md`.

### S-7 — Record scope coverage and exclusions (R-8, R-10)

1. List covered scope items (`SOW-0241`–`SOW-0244`) and supported objectives (`OBJ-002`, `OBJ-003`–`OBJ-010`).
2. Record exclusions: NRM LACT is third-party scope (boundary at tie-in flange); pipeline-export design downstream of facility tie-in is by others; record CT-03 status.

### S-8 — Record permit and environmental posture (R-12)

1. Carry forward BCER 100120203 status and the explicit need for further permit amendment for the truck-rack scope from DBM SEC-17.

### S-9 — Apply source-citation discipline (R-11)

1. For every substantive value, attach a source reference. Where the source exists but is not locally accessible (docx/xlsx/RFQ), use the form `<SourcePath> (location TBD)` and do not derive clause-level numerics from such sources.
2. Inferred statements are labelled **ASSUMPTION**; missing values are labelled `TBD`.

### S-10 — Produce / update derived artifacts in ARTIFACT_REGISTER

Ensure that each of the following PKG-099 / DEL-099-01 ART rows is reflected in the Scope of Work body content:

- `ART-F9FBC08466` Package scope of work
- `ART-6C537783A7` Tagged equipment and package identity list
- `ART-B3C48AB23D` Package function and whole-facility integration narrative
- `ART-B927725D35` Package responsibility assignment record
- `ART-E2749573BE` Detailed mechanical package scope extraction evidence

### S-11 — Cross-document consistency sweep

1. Confirm Datasheet attributes, Specification requirements, Guidance principles/considerations, and these Procedure steps use the same terminology, the same `IFC-*` IDs, and the same numeric values.
2. Where consistency cannot be enforced (notably station count), confirm a Conflict Table row exists in `Guidance.md` with status `TBD`.

## Verification

| Check | Method | Pass criterion |
|---|---|---|
| V-1 | Identity-block audit against `PACKAGE_REGISTER.csv` PKG-099 row | All identity fields match the row exactly |
| V-2 | Function paragraph audit | Verbatim alignment with `PACKAGE_REGISTER.csv` Package Scope column |
| V-3 | Equipment list audit | Matches `ART-517D0E9F90`; station-count attribute references CT-01 |
| V-4 | Design-basis numeric audit | 103 m3/h / 345 kPad / 1 pump per station all cite DBM SEC-06 and are marked `ASSUMPTION` per CT-02 |
| V-5 | Responsibility table audit | Vendor vs Integrator split matches `PACKAGE_REGISTER.csv` and `ART-B927725D35` |
| V-6 | Interface enumeration audit | Eleven interface types listed with their `IFC-*` IDs from `INTERFACE_REGISTER.csv` |
| V-7 | Coverage/exclusion audit | `SOW-0241`–`SOW-0244` and `OBJ-002`/`OBJ-003`–`OBJ-010` listed; LACT and downstream-pipeline exclusions recorded; CT-03 status present |
| V-8 | Permit-posture audit | BCER 100120203 and truck-rack amendment caveat present |
| V-9 | Citation audit | Every substantive value cites a source or carries `TBD`/`ASSUMPTION`/`location TBD`; no fabricated values |
| V-10 | Cross-document consistency sweep (Step 5 of skill) | Terminology, IDs, and values consistent across the four documents; remaining inconsistencies appear in the Conflict Table |

## Records

- `Datasheet.md` (this folder)
- `Specification.md` (this folder)
- `Guidance.md` (this folder, includes Conflict Table)
- `Procedure.md` (this folder)
- `_STATUS.md` (this folder, safe state update `OPEN → INITIALIZED` per Step 7 of `four-documents` skill)
- `_run_records/TASK_RUN_<date>_<HHMM>.md` (this folder, run report capturing pass coverage, sources read, conflicts opened, and `RUN_STATUS`)
