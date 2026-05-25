# Specification: DEL-030-03_construction-work-package

## Scope

This specification governs the EPC Integrator-authored Construction Work Package for `PKG-030`, the Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V package. The Construction Work Package is a mandatory Gate 5 EPC anchor deliverable describing how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Field construction is executed by Tourmaline Oil Corporation under the DBM Construction Responsibility basis.

Exclusions:

- Vendor package engineering, design calculations, certified drawings, and equipment selection are excluded from this construction work package unless later provided as vendor data and integrated by reference.
- Detailed transformer nameplate values, BIL, impedance, cooling class, tap configuration, oil volume, weights, lift plan, rigging plan, oil filling/processing procedure, and protective-relay settings are `TBD` because the accessible source set does not contain package-specific values; they shall be incorporated when vendor package outputs (`DEL-030-04`) become available.
- Final pre-commissioning acceptance values, energization sequence, and protection-coordination test results are excluded from this deliverable and produced by `DEL-030-06` (EPC Vendor Package Review and Acceptance) on receipt of vendor and commissioning data.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-030-03-001 | The Construction Work Package shall identify `PKG-030`, workbook row 32, WBS 01, CoA tracking number 26020-01-30-021, discipline Electrical, and package name "Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V." Source: Workbook Packages row 32; `PACKAGE_REGISTER.csv`. | Identity check against workbook row 32 and Gate 7 registers. |
| REQ-030-03-002 | The Construction Work Package shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces; field construction is executed under the DBM Construction Responsibility basis (Tourmaline field construction scope). Source: `PACKAGE_REGISTER.csv` row `PKG-030`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section. | Responsibility-statement review against Gate 7 package register and DBM. |
| REQ-030-03-003 | The Construction Work Package shall produce the three required artifacts: a construction work package narrative, an installation and tie-in workface plan, and a construction interface and turnover checklist. Source: `ARTIFACT_REGISTER.csv` rows `ART-8A966A4CD7`, `ART-370E7F8537`, `ART-E6DA4BF5C2`. | Artifact-presence check against the Gate 7 artifact register. |
| REQ-030-03-004 | The Construction Work Package shall address all seven applicable interface facts for PKG-030 (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) as construction-execution scope items. Source: Workbook Packages row 32; `INTERFACE_REGISTER.csv` rows for `PKG-030`. | Interface-matrix check against the Gate 7 interface register. |
| REQ-030-03-005 | Foundation and support installation shall conform to the DBM foundation basis: transformers generally on precast concrete bearing foundations; large oil-filled transformers installed on structural steel bases with CEC spacing; secondary containment reviewed and selected to limit containment where practical. Package-specific loads and dimensions are `TBD` pending vendor data. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundation and Transformers paragraphs. | Foundation/support review at IFC; verify CEC spacing and containment review record. |
| REQ-030-03-006 | Grounding execution shall implement two-point ground-grid connection for major electrical equipment, a separate CEC-sized copper ground conductor for distribution transformers, ground wells at the transformer/electrical building with bolted/compression connections, and above-grade green-insulated conductors in PVC conduit where mechanical protection is required. The 600 V secondary system shall be grounded by a 5 A continuous high-resistance grounding resistor per the DBM neutral grounding basis. Package-specific sizing remains `TBD` pending detailed design. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs and neutral grounding resistor paragraph. | Grounding inspection against the cited grounding basis; record conductor sizes and resistor installation. |
| REQ-030-03-007 | Cable tray, conduit, and physical placement shall preserve maintenance access to the transformer (oil sampling, tap-changer, bushings, cooling system). Detailed clearance values are `TBD` pending vendor footprint and access drawings. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs. | Layout/maintenance-access review at constructability check and final walkdown. |
| REQ-030-03-008 | Medium-voltage cable installation between the 13.8 kV switchgear bus and the transformer primary shall use three-conductor copper TECK cable rated 15 kV with 133 percent insulation, shielded, in accordance with the DBM cable schedule basis. 600 V secondary cable to the plant 600 V MCCs shall use ACWU cable; single-conductor cables shall be avoided. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable schedule (13.8 kV row and 600 V transformer-secondary row). | Cable-type verification at receiving inspection and termination QC. |
| REQ-030-03-009 | Tie-in coordination shall apply joint planning with existing or related facility scopes; tie-in timing shall be established as the project progresses and recorded in the construction interface and turnover checklist. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility / tie-in paragraph; `ARTIFACT_REGISTER.csv` row `ART-E6DA4BF5C2`. | Tie-in plan review; presence of tie-in coordination record in the turnover checklist. |
| REQ-030-03-010 | The workface plan shall cover off-loading, setting on foundation, mechanical hookup, installation of shipped-loose components, structural supports, home-run cable installation, electrical terminations, and area lighting work for the transformer package, consistent with Tourmaline field construction scope. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section; `ARTIFACT_REGISTER.csv` row `ART-370E7F8537`. | Workface-plan content review against Construction Responsibility activity list. |
| REQ-030-03-011 | Detailed transformer rating data (nameplate, BIL, impedance, cooling class, tap configuration, oil volume, weights), rigging/lift plan, oil-filling and processing procedure, energization sequence, and protective-relay settings shall be carried as `TBD` until vendor package outputs (`DEL-030-04`) are accepted; this deliverable shall not invent these values. Source: source gap; `DEL-030-04` deliverable record. | Gap-review check; confirm `TBD` markers carried, not invented. |
| REQ-030-03-012 | The Construction Work Package shall not modify or override vendor-owned engineering/design content and shall reference vendor documentation (`DEL-030-05`) once accepted rather than restating it. Source: `PACKAGE_REGISTER.csv` row `PKG-030`; `DELIVERABLE_REGISTER.csv` row `DEL-030-05_vendor-document-turnover-package`. | Cross-deliverable scope review at handoff to `DEL-030-06`. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Transformer spacing, grounding conductor sizing, conduit/cable installation, and electrical installation basis referenced by the DBM electrical section. | Applicable as source-supported design basis; clause locations `TBD`. |
| Project electrical specifications | Voltage classes, MCC, grounding, cable, and raceway bases referenced by the DBM electrical section. | Applicable; document locations `TBD`. |
| Area classification standards | Applicable to electrical equipment, conduit sealing, and installation classification where hazardous/non-hazardous areas are defined; transformer location classification `TBD`. | Applicable; package location classification `TBD`. |
| DBM Construction Responsibility basis | Field construction assigned to Tourmaline Oil Corporation; activity list governs scope of construction execution for this package. | Authoritative basis from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare construction-package identity fields to workbook row 32 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Artifact completeness | Confirm work package narrative, workface plan, and turnover checklist exist. | Three artifacts present per `ARTIFACT_REGISTER.csv` rows. |
| Interface completeness | Compare construction-package interface coverage to `INTERFACE_REGISTER.csv` rows for `PKG-030`. | All seven applicable interfaces are addressed as construction-execution scope. |
| Foundation/support compliance | Inspect foundation type, structural steel base (if applicable), CEC spacing, and secondary-containment review record. | Construction execution matches DBM foundation/Transformers basis; deviations recorded. |
| Grounding inspection | Verify two-point ground-grid connection, separate CEC-sized copper ground conductor, ground wells, bolted/compression connections, and the 5 A high-resistance grounding resistor on the 600 V secondary. | Inspection record matches DBM grounding/bonding and neutral grounding resistor basis. |
| Cable/cable-tray QC | Verify 13.8 kV TECK primary cable type and 600 V ACWU secondary cable type against the DBM cable schedule basis; verify tray/conduit does not impede maintenance access. | Cable types and routing match DBM cable schedule; maintenance-access walkdown passes. |
| Tie-in coordination | Verify a joint tie-in plan exists and tie-in timing is recorded. | Joint tie-in record present; coordinated with existing/related facility scopes. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and `TBD` markers. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Construction work package narrative (`ART-8A966A4CD7`).
- Installation and tie-in workface plan (`ART-370E7F8537`).
- Construction interface and turnover checklist (`ART-E6DA4BF5C2`).
- Source-gap / `TBD` list for vendor or human resolution (vendor nameplate data, lift plan, oil-filling procedure, energization sequence, protective-relay settings, package-specific clearances, installation-location assignment).

The deliverable shall cite the Gate 7 snapshot, workbook row 32, applicable Gate 7 registers, and the DBM Construction Responsibility and electrical source slices used as basis.
