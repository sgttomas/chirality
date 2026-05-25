# Specification: DEL-021-03_construction-work-package

## Scope

This specification governs the EPC Integrator-authored Construction Work Package for `PKG-021`, the 6.9kV SWITCHGEAR EQUIPMENT package. It is a mandatory Gate 5 EPC anchor deliverable describing how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems.

The package is a vendor-owned Electrical package under WBS 01 (CoA tracking number 26020-01-30-012). The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Field construction is assigned to Tourmaline Oil Corporation per the DBM Construction Responsibility section.

The construction work package shall cover: receipt and off-loading, foundation/skid placement, mechanical hookup, electrical and control cabling tie-ins, grounding/bonding, inspection, testing, and construction turnover for the PKG-021 equipment.

Exclusions:

- Vendor detailed design calculations, certified drawings, factory acceptance tests, and final equipment selections are excluded (carried under DEL-021-04 vendor engineered package and DEL-021-05 vendor document turnover).
- Detailed lift plans, rigging studies, installation sequencing, schedule, and PKG-021-specific construction quantities are `TBD` because the accessible source set does not provide a confirmed PKG-021-specific construction basis.
- Operations and maintenance activities post-turnover are outside this deliverable.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-021-03-001 | The Construction Work Package shall identify `PKG-021`, workbook row 23, WBS 01, CoA tracking number 26020-01-30-012, discipline Electrical, and package name "6.9kV SWITCHGEAR EQUIPMENT." Source: Workbook Packages row 23; `PACKAGE_REGISTER.csv`. | Identification review against workbook row 23 and Gate 7 registers. |
| REQ-021-03-002 | The Construction Work Package shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces; Tourmaline Oil Corporation executes field construction per the DBM Construction Responsibility section. Sources: `PACKAGE_REGISTER.csv` row `PKG-021`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Construction Responsibility. | Responsibility statement review against Gate 7 register and DBM source. |
| REQ-021-03-003 | The Construction Work Package shall plan for tie-ins against the six applicable interface facts for `PKG-021`: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 23; `INTERFACE_REGISTER.csv`. | Interface coverage check against the six `PKG-021` rows in `INTERFACE_REGISTER.csv`. |
| REQ-021-03-004 | The Construction Work Package shall comply with project electrical construction specification `ELC-QAS-000001-001` (Revision 1) and medium-voltage switchgear specification `ELC-QAS-000007-001` (Revision 1). Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Table 12-1. | Cross-check of installation, inspection, and testing steps against the named specifications. Location of clause-level requirements is TBD pending access to the specification documents. |
| REQ-021-03-005 | The Construction Work Package shall require ground-grid connection at two points for major electrical equipment and shall comply with the 100 A, 10 s neutral-grounding-resistor basis for 6.9 kV transformers. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Grounding and Bonding section. | Grounding inspection record; resistor configuration verification at energization. |
| REQ-021-03-006 | The Construction Work Package shall require bottom-entry cable installation for switchgear housed in prefabricated electrical buildings (where applicable to PKG-021) and shall preserve equipment door clearances and removable transom sections during installation. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Electrical Buildings section. | Walk-down and clearance verification before energization. |
| REQ-021-03-007 | The Construction Work Package shall specify 6.9 kV MV cable installation using three-conductor copper TECK cable rated 8 kV with 100 percent insulation (shielded), and shall require cable tray and conduit routing that does not interfere with maintenance access. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Cable Specifications and Cable Tray/Conduit paragraphs. | Cable schedule review; field cable installation inspection. |
| REQ-021-03-008 | The Construction Work Package shall require completion of the prescribed electrical studies (short-circuit, relay coordination and arc-flash energy, load-flow) prior to energization, with study outcomes confirming equipment ratings and relay settings. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical studies table. | Verification of completed study reports and applied relay settings before energization. |
| REQ-021-03-009 | The Construction Work Package shall produce the three artifacts defined in `ARTIFACT_REGISTER.csv` for this deliverable: a construction work package (`ART-C2EC8C7D5D`), an installation and tie-in workface plan (`ART-7EEEDBBC28`), and a construction interface and turnover checklist (`ART-AD43276A93`). | Document review against Gate 7 artifact register. |
| REQ-021-03-010 | The Construction Work Package shall mark detailed lift plans, rigging studies, sequencing, schedule, PKG-021 equipment quantities/ratings, and installation building/location as `TBD` rather than inventing values, until vendor data and detailed engineering provide the source basis. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Source-gap review before construction execution. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CSA C22.1-21) | Governs electrical installation, grounding, conductor sizing, and conduit support for the package. | Applicable as source-supported design basis (DBM SEC-12 governing codes paragraph). Clause-level locations TBD. |
| Project specification `ELC-QAS-000001-001` Electrical Construction | Governs electrical construction execution. | Applicable; document location TBD (referenced by DBM Table 12-1). |
| Project specification `ELC-QAS-000007-001` Medium Voltage Switchgear | Governs MV switchgear equipment basis and installation. | Applicable; document location TBD. |
| Project specification `ELC-QAS-000003-001` Electrical Requirements for Packaged Equipment | Governs electrical requirements for packaged equipment such as PKG-021. | Applicable; document location TBD. |
| Area classification standards (API RP-505 basis per DBM) | Electrical buildings located in general purpose areas; package equipment installation must respect the project area classification basis. | Applicable; PKG-021 location classification confirmation TBD. |
| NEMA VE2 | Cable tray support where project drawings do not specify a detail. | Applicable per DBM Cable Tray and Conduit paragraph. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare CWP identity fields to workbook row 23 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Responsibility split | Compare CWP responsibility language to `PACKAGE_REGISTER.csv` and DBM Construction Responsibility section. | Vendor, EPC Integrator, and Tourmaline field construction scopes are not conflated. |
| Interface tie-in coverage | Compare CWP tie-in plan to the six `PKG-021` rows in `INTERFACE_REGISTER.csv`. | All six interface types are addressed in tie-in scope and the turnover checklist. |
| Specification compliance | Cross-check construction, inspection, and testing steps to `ELC-QAS-000001-001`, `ELC-QAS-000007-001`, and `ELC-QAS-000003-001`. | Steps reference the governing specifications; clause-level mapping `TBD` where specifications are not accessible. |
| Grounding verification | Inspect ground-grid connections (two-point) and confirm neutral grounding resistor configuration. | Matches DBM grounding basis. |
| Electrical-study completion | Verify short-circuit, relay coordination/arc-flash, and load-flow studies are complete and applied prior to energization. | Study records exist and equipment ratings/settings are consistent. |
| Source fidelity | Check non-trivial values or requirements against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |
| Artifact completeness | Confirm the three deliverable artifacts (`ART-C2EC8C7D5D`, `ART-7EEEDBBC28`, `ART-AD43276A93`) are produced. | All three artifacts present and aligned with Gate 7 artifact register. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Construction work package (per `ART-C2EC8C7D5D`).
- Installation and tie-in workface plan (per `ART-7EEEDBBC28`).
- Construction interface and turnover checklist (per `ART-AD43276A93`).
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 23, applicable Gate 7 registers, and the DBM electrical and construction-responsibility source slices.
