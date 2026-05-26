# Procedure: DEL-094-03_construction-work-package — Construction Work Package

## Purpose

Define a conservative procedure for producing and using the PKG-094 Construction Work Package for the Tanks, Caustic (API 650) 3-25 package (one fresh caustic tank, one spent caustic tank) from the accepted Gate 7 basis and locally accessible source material.

## Prerequisites

- Accepted Gate 7 decomposition snapshot is available.
- Deliverable-local `_CONTEXT.md`, `_REFERENCES.md`, and `_DEPENDENCIES.md` have been read.
- Workbook source row is available: `26020-Packages_Interfaces_4_export.xlsx`, `Packages` row 86.
- DBM caustic-service and site source slices are available: `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Facility Overview; Site Basis; Liquids Hub Equipment Basis; Caustic Mercaptan Treating Basis; Drain Systems.
- Declared upstream dependencies: none declared during PREPARATION.
- Required but unresolved construction inputs: API 650 clause-level provisions; tank material/coating selection (TBC); caustic drain maximum temperature (TBC); heat-tracing decision; foundation drawings and equipment coordinates; plot plan tie-in coordinates; approved inspection/turnover forms; PKG-094 field construction execution responsibility assignment; extracted slice of `26020-Package_Requirements.docx` heading 46.

## Steps

1. Confirm package identity.
   - Verify deliverable ID, package ID (PKG-094), WBS (03), CoA tracking number (26020-03-19-002), discipline (Mechanical), scope items (SOW-0193..SOW-0196), responsible party (EPC Integrator), and objective mapping against `_CONTEXT.md`, workbook row 86, and Gate 7 registers.

2. Establish construction scope boundary.
   - Include physical installation, construction, inspection, turnover, and tie-in planning for one (1) fresh caustic tank and one (1) spent caustic tank.
   - Record exclusions as `TBD` per PACKAGE_REGISTER.csv row PKG-094.

3. Build the interface checklist.
   - Add all nine PKG-094 interface categories from workbook row 86 and `INTERFACE_REGISTER.csv`: Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports.
   - Add detailed checklist line items only where supported by approved drawings, DBM basis, or project forms; otherwise mark as `TBD`.

4. Build the workface plan.
   - Include caustic-service construction constraints from the DBM: atmospheric 32 oz tanks; LP fuel-gas blanket; heating and insulation; spent-caustic flame arrestor to incinerator header; truck-out support at the spent caustic tank; fresh caustic not connected to VRU.
   - Carry the material restriction: no aluminum in the caustic building.
   - Carry caustic drain construction provisions: 300# ANSI minimum drain-header rating; 300# flange termination at the spent-caustic tank; maximum drain temperature 121 deg C / 250 deg F (TBC); minimum drain-tank temperature 80 deg F; heat tracing 37.8 deg C / 100 deg F with redundant circuits (under consideration).
   - Distinguish EPC Integrator deliverable ownership from the package vendor's engineering/equipment scope per PACKAGE_REGISTER row PKG-094; flag field construction execution responsibility as `TBD`.

5. Carry standards and site basis into the package.
   - Name API 650 as the governing tank standard; mark clause-level construction/inspection provisions `location TBD` until source slices are available.
   - Carry DBM site basis affecting construction: LSD 03-25-80-15 W6M; 673 m AMSL; -40 deg C minimum ambient; winterization, heat tracing, building/tank heating, foundations, structural steel, low-temperature metallurgy, and module layout impacts.

6. Prepare inspection and turnover records.
   - Name required record categories: tank fabrication and installation records (per API 650 once accessible); caustic-service hydrotest and leak-test records; coating/insulation inspection records (material selection TBC); drain-system tie-in inspection records; interface sign-off for the nine interface categories; open item log; turnover checklist.
   - Leave final form numbers and acceptance criteria as `TBD` unless approved project forms are available.

7. Run cross-document consistency check.
   - Confirm that Datasheet attributes/conditions appear in Specification requirements where applicable (tank service basis CWP-004; material restriction CWP-005; venting CWP-006; drain CWP-007; site CWP-008).
   - Confirm that every Specification requirement has a corresponding Procedure step or Verification check.
   - Confirm that unsupported values remain `TBD`, `TBC`, `ASSUMPTION`, or Conflict-Table entries.

8. Route unresolved conflicts for human ruling.
   - Use the Guidance Conflict Table for: PKG-094 field construction responsibility (CWP-094-CON-001); API 650 source access (CWP-094-CON-002); caustic material/drain/SG TBC items (CWP-094-CON-003); vendor/EPC construction handoff boundary (CWP-094-CON-004); missing slice of `26020-Package_Requirements.docx` heading 46 (CWP-094-CON-005).
   - Do not resolve responsibility or material-selection conflicts without an accepted project RACI, vendor data, or human ruling.

## Verification

- Package identity matches workbook row 86 and Gate 7 PACKAGE_REGISTER/DELIVERABLE_REGISTER rows.
- Interface checklist includes all nine PKG-094 workbook/INTERFACE_REGISTER interface facts.
- DBM caustic-service and caustic-drain values are not overstated as final construction criteria where DBM marks them `TBC` or `under consideration`.
- API 650 is named as governing standard; clause-level provisions are marked `TBD` until source slices are available.
- Construction execution responsibility is not collapsed into deliverable ownership.
- All missing quantities, drawings, form IDs, coordinates, and material/coating selections are marked `TBD` or `TBC`.

## Records

- Construction Work Package.
- Installation and tie-in workface plan (fresh caustic tank; spent caustic tank).
- Construction interface and turnover checklist (nine PKG-094 interfaces).
- Open input / TBD register (API 650 clauses; material/coating; drain temperature; heat tracing; foundation/plot data; Word source slice).
- Responsibility matrix or RACI reference: TBD.
- Inspection records: TBD final forms (tank fabrication/installation per API 650; caustic-service hydrotest/leak test; coating/insulation inspection; drain-system tie-in).
- Turnover package index: TBD final form/index structure.
