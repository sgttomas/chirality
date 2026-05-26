# Procedure — DEL-104-03 Construction Work Package

## Purpose

Define the operational steps to (a) author and assemble the Construction Work Package deliverable for PKG-104 "Structural steel - outside of modules", and (b) execute the package in the field through installation, inspection, interface closeout, and turnover. The procedure aligns with the project Construction Responsibility model (Tourmaline field execution, EPC Integrator package authorship) per `4-25_Deepcut_DBM.md` Construction Responsibility.

## Prerequisites

**Declared upstream dependencies:** None declared in `_DEPENDENCIES.md`. Procedure proceeds under the package's standalone basis with the following implicit predecessors needed for execution (ASSUMPTION — not declared edges):

- PKG-104 Scope of Work (`DEL-104-01`) and PKG-104 Package Datasheet (`DEL-104-02`) authored and at INITIALIZED or later (project package handoff basis).
- EPC/Structural Discipline Production Package (`DEL-104-04`) sufficient to define structural members, connections, and tie-in geometry.
- Geotechnical report issued and reviewed (foundation TBDs from `4-25_Deepcut_DBM.md` Geotechnical and Topographical Assumptions resolved for impacted scope).
- Topographical survey delivered; existing-grade surface file available to Propak.
- Plot plan stable for the outside-of-modules steel footprint.
- IFC drawings, bolt-up details, weld procedures, and ITP issued.

**Required references:**

- `4-25_Deepcut_DBM.md` (Construction Responsibility; Civil Scope; Governing Civil and Structural Basis; Geotechnical and Topographical Assumptions; Piles and Foundations; Site Grading and Surface Water Management; General Layout Basis; Minimum Spacing Criteria; Buildings and Miscellaneous Facilities).
- Decomposition snapshot registers (`PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_REGISTER.csv`, `SCOPE_LEDGER.csv`).
- `26020-Package_Requirements.docx` and `26020-Packages_Interfaces_4_export.xlsx` (location TBD — opened in a subsequent pass).

## Steps

### Part A — Author the Construction Work Package

1. Confirm package identity and scope from `_CONTEXT.md` and `PACKAGE_REGISTER.csv` (PKG-104, WBS 01, CoA 26020-01-36-004, Structural steel - outside of modules).
2. Confirm artifact set from `ARTIFACT_REGISTER.csv` for `DEL-104-03`: Construction Work Package; Installation and Tie-In Workface Plan; Construction Interface and Turnover Checklist.
3. Extract governing structural/civil basis (codes, materials, foundation default, grading basis) from `4-25_Deepcut_DBM.md` and carry into the work package's basis-of-construction section.
4. Identify and characterise the two PKG-104 interface facts (`IFC-CCDE4B56CA` Grading/Site Drainage/Spill Containment; `IFC-ECDD4D3A15` Structural/Foundations/Supports) from `INTERFACE_REGISTER.csv` and develop interface coordination text and checklist rows.
5. Draft the Installation and Tie-In Workface Plan (`ART-A0BC38D152`):
   - sequence outside-of-modules steel erection relative to module setting, pipe-rack steel, and grading milestones;
   - identify joint-planning meetings for ISBL/OSBL tie-ins;
   - call out access envelopes per DBM General Layout Basis and Minimum Spacing Criteria.
6. Draft the Construction Interface and Turnover Checklist (`ART-8131641C3B`):
   - one row per interface fact and per tie-in;
   - acceptance criterion and evidence reference for each;
   - explicit linkage to the open-item register and `OBJ-010` handoff evidence.
7. Mark all package-specific values that depend on the geotechnical report or detailed engineering as TBD with the dependency named.
8. Review for source-anchoring (every non-trivial value cites a source slice or is labelled ASSUMPTION/TBD) before issuing the work package.

### Part B — Execute the Construction Work Package in the field

9. Tourmaline field construction mobilises and validates the prerequisites (geotechnical report received; IFC drawings issued; ITP available). ASSUMPTION: ITP existence (REQ-104-03-12).
10. Install foundations per the work package's foundation basis (driven steel piles default per DBM, or alternate per detailed engineering); record pile driving logs and as-built pile coordinates.
11. Erect outside-of-module structural steel per IFC drawings, CAN/CSA-S16 erection requirements, and the project bolting/welding procedures (TBD — procedures not in accessible sources).
12. Coordinate with adjacent grading and drainage work to maintain the DBM pad-grading basis (1.5% from pipe racks; 1.0% allowance) and surface-water control features.
13. Execute each ISBL/OSBL tie-in under joint Tourmaline/EPC planning per the Construction Responsibility section; close the per-tie-in responsibility entry before tie-in.
14. Inspect per the ITP at the designated hold/witness points; record acceptance/rejection.
15. Complete the Construction Interface and Turnover Checklist row-by-row; reconcile open items into the package-level open-item register.
16. Hand over to commissioning with the completed turnover checklist, MTRs, inspection records, pile logs, and as-built grading/tie-in surveys.

## Verification

| Step | Verification | Evidence |
|---|---|---|
| 1-2 | Package and artifact identity match registers | Register cross-check sheet |
| 3 | Basis-of-construction text matches DBM source slices | Source-citation review |
| 4 | Interface coordination rows exist for both interface facts | Interface checklist |
| 5 | Workface plan covers sequencing, joint-planning, and access | Workface plan review record |
| 6 | Turnover checklist links each row to acceptance criterion and evidence | Checklist review record |
| 7-8 | TBDs are explicit; assumptions labelled | Pre-issue review log |
| 9 | Prerequisite gate closed | Mobilisation readiness record |
| 10 | Pile installation conforms to driving log targets / detailed-engineering basis | Pile log; as-built |
| 11 | Erection passes CAN/CSA-S16 inspection criteria | Erection inspection report |
| 12 | Finished grade matches grading plan and DBM basis | Grading as-built survey |
| 13 | Each tie-in responsibility confirmed before execution | Tie-in responsibility log |
| 14 | ITP hold/witness points closed | ITP records |
| 15 | Turnover checklist fully reconciled | Closed checklist; open-item register |
| 16 | Commissioning accepts handoff | Turnover acceptance record |

## Records

The following records constitute the evidence basis for the Construction Work Package per `OBJ-010` (operability/maintainability/sparing/isolation/winterization/vendor-documentation/commissioning/turnover/controlled open-item closure):

- Construction Work Package document (`ART-9478B627E2`)
- Installation and Tie-In Workface Plan (`ART-A0BC38D152`)
- Construction Interface and Turnover Checklist (`ART-8131641C3B`)
- Pile installation logs and as-built pile coordinates
- Mill test reports for structural steel heats
- Weld procedure qualification records and NDE records (TBD — sources not opened)
- Concrete mix submittals, batch tickets, cylinder test results (where concrete is poured under this package)
- Grading as-built survey
- Tie-in responsibility log
- ITP records (ASSUMPTION — ITP existence)
- Open-item register reconciliation at turnover
- Turnover acceptance record
