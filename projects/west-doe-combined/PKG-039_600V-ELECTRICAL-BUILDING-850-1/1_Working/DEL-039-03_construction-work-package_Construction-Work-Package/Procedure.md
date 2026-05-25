# Procedure: DEL-039-03_construction-work-package

## Purpose

This procedure describes how to produce and verify the Construction Work Package for `DEL-039-03_construction-work-package`, covering installation, construction interfaces, inspection evidence, tie-in planning, and turnover for `PKG-039` 600V ELECTRICAL BUILDING (850-1).

## Prerequisites

- Accepted Gate 7 PROJECT_DECOMP snapshot for `PKG-039` and `DEL-039-03_construction-work-package`.
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `Datasheet.md`, and `Specification.md` for this deliverable.
- Gate 7 rows for `PKG-039` in `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, and `OBJECTIVE_DELIVERABLE_MAP.csv`.
- DBM source slices from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` covering Construction Responsibility, Electrical Buildings, electrical inspection/certification, grounding/bonding, cable/raceway basis, and plot-plan gap.
- Vendor IFC design inputs, lift plans, field sequencing, manpower loading, and plot plan CIV-235633-5002: `TBD` until available.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md` at initialization.

## Steps

1. Confirm deliverable identity.
   - Verify the work package is for `DEL-039-03_construction-work-package`, parent package `PKG-039`, package name "600V ELECTRICAL BUILDING (850-1)", WBS 01, CoA 26020-01-30-030, discipline Electrical, and responsible party EPC Integrator.
   - Source: `_CONTEXT.md`, `PACKAGE_REGISTER.csv`, `DELIVERABLE_REGISTER.csv`, Workbook Packages row 41.

2. Establish responsibility boundaries.
   - State that the Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package.
   - State that the EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.
   - State that field construction responsibilities follow the DBM Construction Responsibility table.
   - Source: `PACKAGE_REGISTER.csv` row `PKG-039`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Construction Responsibility".

3. Build the interface and turnover checklist.
   - Include rows for Utility Piping, Drain / Containment, Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Building HVAC / Services, Fire & Gas / Safety Systems, Maintenance Access, Grading / Site Drainage / Spill Containment, and Structural / Foundations / Supports.
   - For each row, identify the construction tie-in owner, prerequisite input, inspection or test evidence, turnover record, and unresolved `TBD` item where the source set does not provide detail.
   - Source: `INTERFACE_REGISTER.csv` rows for `PKG-039`; `ARTIFACT_REGISTER.csv` `ART-17C0FB26AE`.

4. Define the installation workface plan.
   - Include receiving, off-loading, setting modules on foundations, mechanical hookup, shipped-loose item installation, structural supports, home-run cable installation, and electrical terminations.
   - Include the electrical-building configuration basis: prefabricated modular building, general-purpose area, elevated on piles, bottom cable entry, n + 1 HVAC, TECK/ACIC cabling, EMT between adjacent equipment, exterior GFI receptacle, and equipment-door removal allowance.
   - Mark lift plan, sequencing, scaffolding, manpower loading, and coordinate-level layout as `TBD` until vendor/detail design and plot plan inputs are available.
   - Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, "Electrical Buildings" and "Construction Responsibility"; `ARTIFACT_REGISTER.csv` `ART-93DCDB7068`.

5. Define electrical inspection and certification records.
   - Require inspection authority sign-off designated by Tourmaline Oil Corp and applicable CSA C22.1 / BC electrical code compliance evidence.
   - Require third-party certification records for supplied electrical equipment by CSA, ULc, FM, ETL, or another acceptable NRTL.
   - Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical inspection/certification paragraphs.

6. Define grounding and bonding verification.
   - Require evidence that major electrical equipment is directly connected to the ground grid at two points.
   - Require ground wells at electrical buildings, with bolted ground connections at test points for maintenance and operational testing.
   - Include ground inspection/test records in turnover.
   - Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding/bonding paragraph.

7. Capture source gaps and handoff items.
   - Record coordinate-level layout and drawing-based conflict checks as `TBD` pending CIV-235633-5002.
   - Record vendor IFC drawings, lift plans, scaffolding plans, sequencing, manpower loading, and package-specific turnover line items as `TBD` until accessible vendor/detail design inputs are available.
   - Do not replace missing source inputs with assumed values.

8. Assemble the construction work package.
   - Include the construction work package narrative, installation and tie-in workface plan, construction interface and turnover checklist, inspection/certification record index, grounding verification index, and `TBD`/source-gap register.
   - Cite the Gate 7 snapshot, Workbook Packages row 41, applicable registers, and DBM source sections used.

## Verification

| Check | Method | Acceptance |
|---|---|---|
| Identity | Compare package/deliverable fields to `_CONTEXT.md` and Gate 7 registers | IDs, package name, WBS, CoA, discipline, and responsible party match |
| Artifact completeness | Compare package contents to `ART-298F584585`, `ART-93DCDB7068`, and `ART-17C0FB26AE` | Construction package, workface plan, and interface/turnover checklist are present |
| Interface completeness | Compare checklist rows to `INTERFACE_REGISTER.csv` for `PKG-039` | All twelve interface facts are represented |
| Electrical-building basis | Compare installation plan to DBM "Electrical Buildings" source slice | Modular, elevated pile, bottom-entry, HVAC, cable, conduit, GFI, and access/removal bases are included or `TBD` where detail is absent |
| Construction responsibility | Compare field tasks to DBM "Construction Responsibility" table | Field construction tasks are assigned without shifting vendor design scope to EPC |
| Inspection/certification | Review inspection authority sign-off and NRTL certification records | Required records identified; missing records marked `TBD` |
| Grounding/bonding | Review grounding inspection/test records | Two-point ground-grid connections and ground-well test points are addressed |
| Source gaps | Review `TBD` list | Missing plot/vendor/detail design inputs are not asserted as facts |
| Cross-document consistency | Compare Datasheet, Specification, Guidance, and Procedure | Same package identity, interfaces, responsibilities, and `TBD` items are used |

## Records

- Construction work package for `PKG-039`.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist covering all twelve `PKG-039` interface facts.
- Electrical inspection authority sign-off index.
- Electrical equipment certification record index.
- Grounding/bonding inspection and test record index.
- Source-gap / `TBD` register for missing plot plan and vendor/detail design inputs.
- Final package turnover evidence cross-reference to Gate 7 artifact IDs `ART-298F584585`, `ART-93DCDB7068`, and `ART-17C0FB26AE`.
