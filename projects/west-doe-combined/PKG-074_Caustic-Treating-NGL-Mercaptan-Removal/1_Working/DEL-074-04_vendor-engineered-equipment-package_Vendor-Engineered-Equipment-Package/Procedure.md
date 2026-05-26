# Procedure: Vendor Engineered Equipment Package

## Purpose

Define the working procedure to produce and check the DEL-074-04 Vendor Engineered Equipment Package for PKG-074 Caustic Treating (NGL Mercaptan Removal) using accepted Gate 7 truth and the available 4-25 Deepcut DBM source slices, pending later access to the binary 26020-Package_Requirements.docx and acceptance of the EPC Scope of Work (DEL-074-01) and EPC Package Datasheet (DEL-074-02).

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Gate 7 PACKAGE_REGISTER.csv, DELIVERABLE_REGISTER.csv, ARTIFACT_REGISTER.csv, INTERFACE_REGISTER.csv, OBJECTIVE_DELIVERABLE_MAP.csv.
- Process source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`:
  - Current-Scope NGL Mercaptan Treating.
  - NGL Mercaptan Treating Design Parameters.
  - NGL Mercaptan Treating Equipment and Utilities.
  - Incinerator Interface.
  - Disulphide Oil, Spent Caustic, and Waste Amine.
  - Common Equipment discussion.
  - Governing Codes, Standards, Specifications, and Studies.
- Declared dependencies review: no declared upstream or downstream dependencies are currently listed in `_DEPENDENCIES.md`. ASSUMPTION: DEL-074-01 (SOW) and DEL-074-02 (Package Datasheet) will be the upstream EPC handoff once produced and accepted.
- Deferred references not locally readable in this run:
  - `_Sources/26020-Package_Requirements.docx` (binary; package heading 28 detail).
  - `_Sources/26020-Packages_Interfaces_4_export.xlsx` (binary; interface workbook export).
- Open external/vendor inputs to be tracked as TBD until accepted: third-party proprietary process provider selection, contactor stages, caustic concentration confirmation, low/high pressure cases, winter vapour pressure values, high-ethane case, shower quantity/location, building floor material, caustic tank material selections, fresh/DSO tank design SGs.

## Steps

1. Confirm deliverable identity against `_CONTEXT.md` and DELIVERABLE_REGISTER.csv (DEL-074-04, Vendor Engineered Equipment Package, PKG-074, Mechanical, Vendor Package Production Unit).
2. Confirm package identity against PACKAGE_REGISTER.csv for PKG-074 (WBS 01; CoA 26020-01-27-002; responsibility split: Package Vendor owns engineering/design/documentation/equipment; EPC Integrator owns facility integration).
3. Record the 13 accepted interface facts from INTERFACE_REGISTER.csv for PKG-074:
   - Process Piping; Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Structural / Foundations / Supports.
4. Establish the vendor design basis from the DBM source slices:
   - Process basis (non-regenerative caustic, cooled C3+ NGL downstream of de-ethanizer, third-party proprietary provider).
   - Design parameters (rate, inlet/outlet pressure, temperature range, caustic chemistry, storage tank counts, extraction performance, sulphur performance).
   - Equipment and utilities (indoor installation, segregation, safety showers, contactor + outlet filters, water wash + coalescing, recycle pumps, pressurized caustic drain drum V-6940-1, fresh/spent caustic and DSO tanks, materials and ban on aluminum, incinerator interface via 3-25 facility).
   - Common-equipment classification.
5. Build the vendor design basis and datasheet set artifact (ART-04D78DC493) using only source-supported requirements and explicitly labeled assumptions.
6. Build the physical equipment package artifact scope (ART-7D22DB55EB) using the major included equipment list (ART-EDAC8A3AB7) constrained to source-supported items.
7. Build the interface matrix and trace each listed interface back to the Gate 7 INTERFACE_REGISTER.csv row.
8. Create or update the source-limited requirements closure record, including at minimum:
   - Deferred binary-source items from 26020-Package_Requirements.docx package heading 28.
   - TBC parameter values listed in the DBM design parameter and equipment tables.
   - Detailed-engineering open items (process provider selection, contactor stages, etc.).
   - EPC handoff anchoring once DEL-074-01 SOW and DEL-074-02 Package Datasheet are accepted.
9. Check that vendor scope does not absorb EPC Integrator responsibilities (facility integration, tie-ins, constructability, procurement/construction coordination).
10. Check that final design values not available in the source set remain `TBD`; do not infer.
11. Prepare the package for EPC Integrator integration review per the EPC Vendor Package Review and Acceptance basis (DEL-074-06).

## Verification

| Check | Method |
|---|---|
| Identity verification | Compare deliverable and package tables to `_CONTEXT.md`, DELIVERABLE_REGISTER.csv, and PACKAGE_REGISTER.csv. |
| Interface verification | Confirm all 13 PKG-074 interface facts are included and cited to INTERFACE_REGISTER.csv. |
| Process basis verification | Confirm the vendor design implements non-regenerative caustic treating on cooled C3+ NGL downstream of the de-ethanizer per 4-25_Deepcut_DBM.md. |
| Design parameter verification | Vendor datasheets carry DBM rate, pressures, temperatures, and caustic concentrations; TBC items flagged. |
| Equipment list verification | Vendor equipment list includes contactor/mixer, outlet filters (2 x 100%), water wash + coalescer, recycle pumps (2 x 100%), pressurized caustic drain drum (V-6940-1), fresh/spent caustic/DSO tanks (each 1 x 400 bbl), heater(s), circulation/transfer pumps. |
| Materials verification | No aluminum; SS insulation cladding/straps in caustic exposure areas; caustic-compatible tank materials; building floor/tank materials open as TBD. |
| Indoor installation verification | All caustic equipment within or adjacent to Mercaptan Treating Unit building. |
| Safety shower verification | Water safety showers present with discrete control-room alert; quantity/location TBD logged. |
| Incinerator interface verification | DSO/spent-caustic vent routing to 3-25 incinerator through upstream knock-out drum; TBD items captured. |
| Source grounding | Each non-trivial requirement cites Gate 7 registers or DBM source slices. |
| Open input verification | Vendor proprietary process selection, contactor stages, caustic concentration confirmation, low/high pressure cases, winter vapour pressure, high-ethane case, materials TBDs are listed in the closure record. |
| Cross-document consistency | Datasheet, Specification, Guidance, Procedure use consistent equipment names, tag numbers, interface labels, units, and source basis. |
| Dependency check | Confirm blockers are not inferred from undeclared relationships; use declared dependency edges only. |

## Records

- Vendor package design basis and datasheet set (ART-04D78DC493).
- Vendor engineered physical equipment package documentation (ART-7D22DB55EB).
- Major included equipment evidence (ART-EDAC8A3AB7).
- Interface matrix for the 13 PKG-074 workbook interface types.
- Source-limited requirements closure record (binary-source deferrals, TBC values, detailed-engineering open items, EPC-handoff anchoring).
- Materials and indoor-installation compliance record.
- Safety shower and control-room alarm documentation.
- Cross-document consistency check record.
- Open input / Human Ruling Required log (mirrors Guidance Conflict Table).
