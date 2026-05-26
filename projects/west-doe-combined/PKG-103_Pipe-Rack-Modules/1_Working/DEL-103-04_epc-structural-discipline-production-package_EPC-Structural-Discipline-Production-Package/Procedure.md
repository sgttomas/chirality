# Procedure: EPC / Structural Discipline Production Package — PKG-103 Pipe Rack Modules

## Purpose

Define the working procedure to produce and check the DEL-103-04 Structural discipline production package for PKG-103 Pipe Rack Modules using accepted Gate 7 truth and available structural/civil DBM source slices.

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Gate 7 registers: `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- Structural/civil source slices from:
  - `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Civil Scope; Governing Civil and Structural Basis; Geotechnical and Topographical Assumptions; Site Grading and Surface Water Management; Piles and Foundations; Buildings and Miscellaneous Facilities; External Dependencies).
  - `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (Site and Civil Conditions; Foundations and Structural Supports; Area Classification).
- Declared dependencies review: no declared upstream or downstream dependencies are currently listed in `_DEPENDENCIES.md`.
- Open external inputs to be tracked as `TBD` until accepted: geotechnical assessment report; topographical survey and grade surface file; plot plan; piping anchor/guide load schedule; electrical power, EHT, I&C, and communications cable schedules and tray basis; detailed P&ID/3D model deliverables that define rack-supported commodities.

## Steps

1. Confirm deliverable identity against `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv` row DEL-103-04.
2. Confirm package identity against `PACKAGE_REGISTER.csv` row PKG-103 (Structural; Pipe Rack Modules; WBS 03; CoA 26020-03-36-003).
3. Record the nine accepted interface facts from `INTERFACE_REGISTER.csv` for PKG-103:
   - Process Piping (IFC-1B5D83EC66).
   - Utility Piping (IFC-AECC45897E).
   - Relief / Flare / Vent (IFC-933A9B9DC3).
   - Electrical Power (IFC-3268483707).
   - EHT (IFC-489CEA5AA8).
   - I&C / Control Cabling (IFC-FC76A7E07D).
   - Communications / Network (IFC-38D5605A15).
   - Grading / Site Drainage / Spill Containment (IFC-E2FEA8FA23).
   - Structural / Foundations / Supports (IFC-BC9813EE49).
4. Record the Gate 6 disposition for each interface fact: pipe racks and pipe rack modules are designed exclusively by the EPC Integrator.
5. Establish the structural source basis from the DBM:
   - Governing codes (NBCC; CAN/CSA-S16; CAN/CSA A23.3; CSA A23.1/A23.2; Canadian Foundation Engineering Manual).
   - Structural steel grades (CSA G40.20/G40.21 350W for W-flange and HSS; 300W for channels, plates, and angles).
   - Default foundation basis: driven steel piles for pipe racks.
   - Site/environmental basis: -40 deg C to +35 deg C ambient; 673 m AMSL elevation; NBCC snow/wind/seismic.
   - Pipe-rack grading interface: high equal-elevation ridge along the main pipe rack with 1.5% facility-pad slope to each side (allowable reduction to 1.0%).
   - Area classification baseline: outdoor pipe racks are general-purpose non-hazardous unless detailed classification drawings identify otherwise.
6. Build the discipline production package basis using only source-supported requirements and assumptions explicitly labeled as assumptions.
7. Create or update the source-limited requirements closure record, including at minimum:
   - Missing detailed discipline deliverable register.
   - Missing geotechnical assessment report (bearing capacity, LPILE curves, dynamic design criteria).
   - Missing topographical survey and grade surface file.
   - Missing plot plan and 3D-model rack-supported commodity definitions.
   - Missing piping anchor/guide load schedule.
   - Missing electrical/EHT/I&C/communications cable schedules and cable-tray basis.
   - Shop-vs-field erection split for pipe rack modules (not enumerated in DBM module/erection table).
   - Final pile design parameters and foundation member sizes.
8. Build the interface matrix and trace each listed interface back to the Gate 7 interface register IFC ID.
9. Confirm that pipe rack steel design, member sizes, connection design, anchor loads, and rack geometry are not asserted from package name alone — keep them `TBD` until source-supported inputs are accepted.
10. Confirm the area-classification baseline (outdoor pipe rack non-hazardous) is carried as a baseline, not a final classification.
11. Prepare the package for review by the EPC Integrator or assigned structural discipline subcontractor.

## Verification

| Check | Method |
|---|---|
| Identity verification | Compare deliverable and package tables to `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv` row DEL-103-04, and `PACKAGE_REGISTER.csv` row PKG-103. |
| Interface verification | Confirm all nine accepted interface facts are included and cited to `INTERFACE_REGISTER.csv` IFC IDs, with the EPC-Integrator design disposition noted. |
| Source grounding | Confirm each non-trivial requirement cites a Gate 7 register row or a named DBM source slice. |
| Standards verification | Confirm NBCC, CAN/CSA-S16, CAN/CSA A23.3, CSA A23.1/A23.2, Canadian Foundation Engineering Manual, and CSA G40.20/G40.21 appear in the design criteria sheet. |
| Foundation verification | Confirm the foundation concept register cites driven steel piles as the default basis for pipe racks and lists open geotechnical parameters. |
| Open input verification | Confirm the closure record lists geotechnical report, topographical survey/grade surface file, plot plan, piping loads, cable schedules, shop/field split, and final pile parameters as `TBD` or HRR items. |
| Site basis verification | Confirm the ambient temperature range, elevation, and snow/wind/seismic basis appear in the design basis register. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use consistent names, interface labels, IFC IDs, and source basis. |
| Dependency check | Confirm blockers are not inferred from undeclared relationships; use declared dependency edges only. |

## Records

- Discipline production package basis (structural).
- TBD discipline deliverable register.
- Source-limited requirements closure record.
- Interface matrix for the nine PKG-103 interfaces with IFC IDs and EPC-Integrator disposition.
- Structural design criteria sheet (codes, steel grades, site basis, foundation default).
- Foundation concept register (driven steel piles default; open geotechnical parameters).
- Area-classification carry-over note (outdoor pipe rack non-hazardous baseline).
- Open input / Human Ruling Required log.
- Cross-document consistency check record.
