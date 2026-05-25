# Specification: DEL-015-03_construction-work-package

## Scope

This specification governs the EPC Integrator-authored Construction Work Package for `PKG-015`, the Transformer TXP-8300-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 12/15MVA 13.8kV/4160/2400V package. The Construction Work Package is a mandatory Gate 5 EPC anchor deliverable describing how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems.

The package is a vendor-owned Electrical package under WBS 02. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Field construction is executed by Tourmaline Oil Corporation under the DBM Construction Responsibility basis.

Exclusions:

- Vendor package engineering, design calculations, certified drawings, and equipment selection are excluded from this construction work package unless later provided as vendor data and integrated by reference.
- Detailed transformer nameplate values, BIL, impedance, cooling class, tap configuration, oil volume, weights, lift plan, rigging plan, oil filling/processing procedure, and protective-relay settings are `TBD` because the accessible source set does not contain package-specific values; they shall be incorporated when vendor package outputs (`DEL-015-04`) become available.
- Final pre-commissioning acceptance values, energization sequence, and protection-coordination test results are excluded from this deliverable and produced by `DEL-015-06` (EPC Vendor Package Review and Acceptance) on receipt of vendor and commissioning data.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-015-03-001 | The Construction Work Package shall identify `PKG-015`, workbook row 17, WBS 02, CoA tracking number 26020-02-30-006, discipline Electrical, and package name "Transformer TXP-8300-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 12/15MVA 13.8kV/4160/2400V." Source: Workbook Packages row 17; `PACKAGE_REGISTER.csv`. | Identity check against workbook row 17 and Gate 7 registers. |
| REQ-015-03-002 | The Construction Work Package shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces; field construction is executed under the DBM Construction Responsibility basis (Tourmaline field construction scope). Source: `PACKAGE_REGISTER.csv` row `PKG-015`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section. | Responsibility-statement review against Gate 7 package register and DBM. |
| REQ-015-03-003 | The Construction Work Package shall produce the three required artifacts: a construction work package narrative, an installation and tie-in workface plan, and a construction interface and turnover checklist. Source: `ARTIFACT_REGISTER.csv` rows `ART-59A22A2C20`, `ART-1F850BBCB2`, `ART-43ADD84004`. | Artifact-presence check against the Gate 7 artifact register. |
| REQ-015-03-004 | The Construction Work Package shall address all seven applicable interface facts for PKG-015 (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) as construction-execution scope items. Source: Workbook Packages row 17; `INTERFACE_REGISTER.csv` rows for `PKG-015`. | Interface-matrix check against the Gate 7 interface register. |
| REQ-015-03-005 | Foundation and support installation shall conform to the DBM foundation basis: transformers generally on precast concrete bearing foundations; large oil-filled transformers installed on structural steel bases with CEC spacing; secondary containment reviewed and selected to limit containment where practical. Package-specific loads and dimensions are `TBD` pending vendor data. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, foundation and Transformers paragraphs. | Foundation/support review at IFC; verify CEC spacing and containment review record. |
| REQ-015-03-006 | Grounding execution shall implement two-point ground-grid connection for major electrical equipment, a separate CEC-sized copper ground conductor for distribution transformers, ground wells at the transformer/electrical building with bolted/compression connections, and above-grade green-insulated conductors in PVC conduit where mechanical protection is required. Package-specific sizing remains `TBD` pending detailed design. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Grounding inspection against the cited grounding basis; record conductor sizes used. |
| REQ-015-03-007 | Cable tray, conduit, and physical placement shall preserve maintenance access to the transformer (oil sampling, tap-changer, bushings, cooling system). Detailed clearance values are `TBD` pending vendor footprint and access drawings. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs. | Layout/maintenance-access review at constructability check and final walkdown. |
| REQ-015-03-008 | Medium-voltage cable installation between the 13.8 kV switchgear bus and the transformer primary shall use three-conductor copper TECK cable rated 15 kV with 133 percent insulation, shielded, in accordance with the DBM cable schedule basis. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable schedule, 13.8 kV row. | Cable-type verification at receiving inspection and termination QC. |
| REQ-015-03-009 | Tie-in coordination shall apply joint planning with existing or related facility scopes; tie-in timing shall be established as the project progresses and recorded in the construction interface and turnover checklist. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility / tie-in paragraph; `ARTIFACT_REGISTER.csv` row `ART-43ADD84004`. | Tie-in plan review; presence of tie-in coordination record in the turnover checklist. |
| REQ-015-03-010 | The workface plan shall cover off-loading, setting on foundation, mechanical hookup, installation of shipped-loose components, structural supports, home-run cable installation, electrical terminations, and area lighting work for the transformer package, consistent with Tourmaline field construction scope. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section; `ARTIFACT_REGISTER.csv` row `ART-1F850BBCB2`. | Workface-plan content review against Construction Responsibility activity list. |
| REQ-015-03-011 | Detailed transformer rating data (nameplate, BIL, impedance, cooling class, tap configuration, oil volume, weights), rigging/lift plan, oil-filling and processing procedure, energization sequence, and protective-relay settings shall be carried as `TBD` until vendor package outputs (`DEL-015-04`) are accepted; this deliverable shall not invent these values. Source: source gap; `DEL-015-04` deliverable record. | Gap-review check; confirm `TBD` markers carried, not invented. |
| REQ-015-03-012 | The Construction Work Package shall not modify or override vendor-owned engineering/design content and shall reference vendor documentation (`DEL-015-05`) once accepted rather than restating it. Source: `PACKAGE_REGISTER.csv` row `PKG-015`; `DELIVERABLE_REGISTER.csv` row `DEL-015-05_vendor-document-turnover-package`. | Cross-deliverable scope review at handoff to `DEL-015-06`. |

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
| Identity completeness | Compare construction-package identity fields to workbook row 17 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Artifact completeness | Confirm work package narrative, workface plan, and turnover checklist exist. | Three artifacts present per `ARTIFACT_REGISTER.csv` rows. |
| Interface completeness | Compare construction-package interface coverage to `INTERFACE_REGISTER.csv` rows for `PKG-015`. | All seven applicable interfaces are addressed as construction-execution scope. |
| Foundation/support compliance | Inspect foundation type, structural steel base (if applicable), CEC spacing, and secondary-containment review record. | Construction execution matches DBM foundation/Transformers basis; deviations recorded. |
| Grounding inspection | Verify two-point ground-grid connection, separate CEC-sized copper ground conductor, ground wells, and bolted/compression connections. | Inspection record matches DBM grounding/bonding basis. |
| Cable/cable-tray QC | Verify 13.8 kV TECK cable type and routing against the DBM cable schedule basis; verify tray/conduit does not impede maintenance access. | Cable-type and routing match DBM cable schedule; maintenance-access walkdown passes. |
| Tie-in coordination | Verify a joint tie-in plan exists and tie-in timing is recorded. | Joint tie-in record present; coordinated with existing/related facility scopes. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and `TBD` markers. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Construction work package narrative (`ART-59A22A2C20`).
- Installation and tie-in workface plan (`ART-1F850BBCB2`).
- Construction interface and turnover checklist (`ART-43ADD84004`).
- Source-gap / `TBD` list for vendor or human resolution (vendor nameplate data, lift plan, oil-filling procedure, energization sequence, protective-relay settings, package-specific clearances).

The deliverable shall cite the Gate 7 snapshot, workbook row 17, applicable Gate 7 registers, and the DBM Construction Responsibility and electrical source slices used as basis.
