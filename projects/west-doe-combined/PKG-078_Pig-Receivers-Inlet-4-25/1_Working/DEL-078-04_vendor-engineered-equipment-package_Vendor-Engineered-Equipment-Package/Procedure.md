# Procedure — DEL-078-04 Vendor Engineered Equipment Package

> Operational steps for producing the vendor-engineered equipment package. Steps requiring judgment beyond accessible source authority are marked `TBD`.

## Purpose

Define how the Package Vendor produces the engineered equipment package for the three (3) Pig Receivers (Inlet) of the 4-25 Deepcut facility, and how the EPC Integrator confirms integration readiness before handing the package to construction.
Source: `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 78.

## Prerequisites

- Upstream EPC Scope of Work for PKG-078 (`DEL-078-01_scope-of-work`) accepted. Source: `DELIVERABLE_REGISTER.csv` line 432.
- Upstream EPC Package Datasheet for PKG-078 (`DEL-078-02_package-datasheet`) accepted. Source: `DELIVERABLE_REGISTER.csv` line 433.
- Construction Work Package outline for PKG-078 (`DEL-078-03_construction-work-package`) available for integration awareness. Source: `DELIVERABLE_REGISTER.csv` line 434.
- Project DBM (`DBM-Deepcut/4-25_Deepcut_DBM.md`) accessible to the Package Vendor.
- RFQ source basis `26020-01-PT-RFQ-35-001-Pig_Recv_2.docx` and `26020-Package_Requirements.docx` package heading 31 issued to vendor. Source: `PACKAGE_REGISTER.csv` row 78 (note: not locally accessible at this draft).
- Declared upstream dependencies satisfied per `_DEPENDENCIES.md` (none declared as of PREPARATION).

## Steps

1. **Receive and review EPC anchor documents.** The Package Vendor obtains the EPC Scope of Work, Package Datasheet, RFQ, and applicable DBM slices, and reconciles them against the PKG-078 register row.
2. **Confirm scope split.** Confirm the Package Vendor scope (engineering, design, fabrication/supply, physical equipment) and EPC Integrator scope (integration, interfaces, tie-ins, constructability, facility-level integration). Source: `PACKAGE_REGISTER.csv` row 78.
3. **Establish design basis.** Develop the vendor package design basis citing:
   - three (3) identical 610 mm OD (24") pig receivers on dedicated structural-steel non-enclosed skids;
   - HIPPS package per skid;
   - full-port upstream isolation / ESDVs;
   - barred tees against pig migration;
   - LP fuel-gas sweet-gas purge connection;
   - HP flare vent routing.
   Source: `PACKAGE_REGISTER.csv` row 78; `DBM-Deepcut/4-25_Deepcut_DBM.md` lines 585 and ~809.
4. **Resolve vessel parameters.** Specify receiver vessel design pressure, design temperature, materials of construction, and trim selection consistent with sour-service requirements and the inlet pipeline MAWP of 1440 psig (TBC). **TBD** specific values pending RFQ/Package Datasheet slice access.
5. **Engineer the HIPPS package.** Develop the HIPPS architecture (independent pressure control/shutdown), shutdown setpoints, and SIL verification. Coordinate setpoints with the EPC Integrator to account for high-pressure gas volume between plant inlet ESDVs and inlet separator inlet PCVs. Source: `DBM-Deepcut/4-25_Deepcut_DBM.md` line ~809.
6. **Produce vendor documentation set.** Produce the vendor package design basis, equipment datasheets, P&IDs, mechanical drawings, pressure-vessel documentation, HIPPS SIL report, electrical and I&C documentation, structural skid drawings, and operating/maintenance manuals. Forward turnover-class documents to `DEL-078-05_vendor-document-turnover-package`.
7. **Coordinate interfaces with EPC Integrator.** For each declared PKG-078 interface type (Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; I&C / Control Cabling; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports; Pipeline / Pigging), exchange data and confirm tie-in expectations. Source: `PACKAGE_REGISTER.csv` row 78.
8. **Fabricate, inspect, and FAT.** Fabricate the three skids, perform shop inspection, hydrotest the receiver vessels, and complete HIPPS FAT before shipment. **ASSUMPTION** on detailed inspection plan pending RFQ access.
9. **Ship to site and support integration.** Deliver the engineered equipment package to site; support EPC Integrator during installation, tie-in, commissioning, and turnover. Final acceptance is recorded under `DEL-078-06_epc-vendor-package-review-and-acceptance`.

## Verification

| Check | Pass Criterion |
|---|---|
| All three receivers fabricated to identical design | Vendor BOM and nameplates match PKG-078 register row. |
| Skid configuration | Non-enclosed structural-steel skids per DBM line 585. |
| Full-port isolation upstream | Valve datasheets confirm full port; FAT pass. |
| Barred tees | P&ID and isometrics show barred tees; visual inspection. |
| Purge and vent routing | LP fuel-gas connection and HP flare tie-in present and labelled correctly. |
| HIPPS SIL verification | SIL report accepted; FAT pass; setpoints aligned with EPC inlet-system basis. |
| Material certifications | Mill test certificates and pressure-vessel documentation complete (per regulatory jurisdiction). |
| Interface sign-off | EPC interface matrix closed for all ten declared interface types. |
| Document turnover | Vendor document set forwarded to `DEL-078-05` and accepted under `DEL-078-06`. |

## Records

- Vendor package design basis (issued).
- Equipment datasheets, P&IDs, mechanical drawings, structural skid drawings.
- Pressure-vessel documentation (U-stamp or jurisdictional equivalent), mill test certificates.
- HIPPS SIL verification report, HIPPS FAT records.
- Inspection and FAT reports for each receiver/skid.
- Interface coordination records with EPC Integrator (linked to `DEL-078-06`).
- Turnover document set (linked to `DEL-078-05`).
