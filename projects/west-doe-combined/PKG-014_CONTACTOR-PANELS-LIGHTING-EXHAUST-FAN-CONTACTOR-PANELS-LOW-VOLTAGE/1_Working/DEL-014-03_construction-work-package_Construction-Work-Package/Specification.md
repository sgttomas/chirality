# Specification: DEL-014-03_construction-work-package

## Scope

This specification governs the EPC Integrator-authored Construction Work Package for `PKG-014`, the "CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE" package. The Construction Work Package is a mandatory Gate 5 EPC anchor deliverable that describes how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems.

The package is a vendor-owned Electrical package under WBS 02. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Per the DBM, field construction is assigned to Tourmaline Oil Corporation.

Exclusions:

- Vendor detailed design, panel internal arrangement drawings, certified panel drawings, and final contactor/component selections are excluded from this construction work package unless later provided as vendor data and integrated by reference.
- Package-specific contactor ratings, panel counts, panel construction (free-standing vs. wall-mount), enclosure ratings, lighting circuit schedule, exhaust-fan schedule, and assigned installation locations are `TBD` because the accessible source set does not provide confirmed package-specific values.
- Detailed test plans, inspection hold points, and turnover certificate templates are `TBD` pending construction execution planning.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-014-03-001 | The Construction Work Package shall identify `PKG-014`, workbook row 16, WBS 02, CoA tracking number 26020-02-30-005, discipline Electrical, and package name "CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE." Source: Workbook Packages row 16; `PACKAGE_REGISTER.csv`. | Identification review against workbook row and Gate 7 registers. |
| REQ-014-03-002 | The Construction Work Package shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces; field construction is assigned to Tourmaline. Source: `PACKAGE_REGISTER.csv` row `PKG-014`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility. | Responsibility statement review against Gate 7 package register and DBM. |
| REQ-014-03-003 | The Construction Work Package shall include the seven applicable interface facts as tie-in scope: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 16; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-014`. |
| REQ-014-03-004 | The Construction Work Package shall require that grounding/bonding follow the DBM basis: major electrical equipment connected to the ground grid at two points and CEC-sized separate copper ground conductors where applicable. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding/bonding paragraphs. | Grounding/bonding scope review at construction tie-in points. |
| REQ-014-03-005 | The Construction Work Package shall require cable tray and conduit routing to preserve maintenance access and operator clearances at all contactor panels and adjacent equipment. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, cable tray/conduit paragraphs. | Routing review against approved cable/conduit layouts. |
| REQ-014-03-006 | The Construction Work Package shall identify the field construction activities in scope: off-loading and setting modules/equipment, mechanical hookups, installation of shipped-loose components, miscellaneous structural supports, home-run cable installation, electrical terminations, and area lighting installation, scoped to PKG-014 as applicable. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility (lines ~107-125). | Construction scope checklist review. |
| REQ-014-03-007 | The Construction Work Package shall coordinate exhaust fan and heater controls with Remote I/O panel placement, recognizing that building exhaust fan and heater controls may be supported by RIO nodes per the DBM. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Remote I/O paragraph (line ~804). | I&C/RIO interface coordination review. |
| REQ-014-03-008 | The Construction Work Package shall require lighting circuits installed by the package or by field construction to use the project lighting service basis (120/208 V, 3 phase, 4 wire, 60 Hz solid grounded) and low-voltage service basis (600 V, 3 phase, 3 wire HRG 5 A) consistent with the DBM voltage table for any feeders sized within the package boundary. Source: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, voltage/service table (lines ~734-735). | Voltage/feeder review against DBM voltage table. |
| REQ-014-03-009 | The Construction Work Package shall require contactor panels, enclosures, and exposed field components to be suitable for the project site basis (including -40 deg C minimum ambient) unless vendor data establishes a more severe applicable condition. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, site basis (line ~145). | Environmental rating review against vendor data and site basis. |
| REQ-014-03-010 | The Construction Work Package shall produce the three required artifacts: construction work package, installation and tie-in workface plan, and construction interface and turnover checklist. Source: `ARTIFACT_REGISTER.csv` rows `ART-6B7A89231D`, `ART-46CD09710D`, `ART-497FADDF9B`. | Artifact completeness review against the Gate 7 artifact register. |
| REQ-014-03-011 | The Construction Work Package shall identify source gaps (panel count, contactor rating, enclosure rating, installation location, lighting/exhaust-fan circuit schedules) as `TBD` rather than carrying invented values, pending vendor data or detailed design. Source: source gap recorded in `_REFERENCES.md` and this run record. | Gap review at construction handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical installation, grounding, conduit support, and electrical termination basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage, grounding, cable, raceway, and termination basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to electrical equipment, conduit sealing, and installation classification where hazardous/non-hazardous areas are defined. | Applicable; PKG-014 area assignment TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare construction work package identity fields to workbook row 16 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare tie-in scope to `INTERFACE_REGISTER.csv` rows for `PKG-014`. | All seven applicable interface facts are present and addressed. |
| Source fidelity | Check every non-trivial requirement, voltage value, or scope statement against cited DBM/source slices. | Unsupported items are marked `TBD`/`ASSUMPTION`, not treated as design values. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv` and DBM Construction Responsibility. | Vendor package design, EPC integration, and field construction scopes are not conflated. |
| Artifact completeness | Confirm production of the three artifacts. | Construction work package, installation and tie-in workface plan, and construction interface and turnover checklist are produced or planned. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and `TBD` items. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Construction work package (`ART-6B7A89231D`).
- Installation and tie-in workface plan (`ART-46CD09710D`).
- Construction interface and turnover checklist (`ART-497FADDF9B`).
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 16, applicable Gate 7 registers, and the DBM source slices used for construction responsibility, electrical service basis, and interface bases.
