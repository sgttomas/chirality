# Specification: DEL-023-03_construction-work-package

## Scope

This specification governs the EPC Integrator-authored Construction Work Package for `PKG-023`, the MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD package. The Construction Work Package is a mandatory Gate 5 EPC anchor deliverable that defines how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems.

The package is a vendor-owned Electrical package under WBS 01 (CoA `26020-01-30-014`). The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design calculations, certified drawings, factory-acceptance test records, and final equipment selections are excluded from this construction work package unless later provided as accepted vendor data.
- Package-specific VFD topology, motor identity/load, harmonic mitigation, isolation transformer requirements, lift weights, foundation loads, energization sequence, and detailed commissioning steps are `TBD` because the accessible source set does not provide confirmed package-specific values.
- Detailed civil/foundation, electrical area-classification placement, and protective relaying coordination work that belongs to the respective discipline deliverables is referenced, not duplicated here.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-023-03-001 | The Construction Work Package shall identify `PKG-023`, workbook row 25, WBS 01, CoA tracking `26020-01-30-014`, discipline Electrical, and package name "MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD." Source: Workbook Packages row 25; `PACKAGE_REGISTER.csv`. | Identity review against workbook row and Gate 7 registers. |
| REQ-023-03-002 | The Construction Work Package shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, and procurement/construction coordination. Source: `PACKAGE_REGISTER.csv` row `PKG-023`. | Responsibility statement review against Gate 7 package register. |
| REQ-023-03-003 | The Construction Work Package shall include all six applicable interface facts: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. Source: Workbook Packages row 25; `INTERFACE_REGISTER.csv` rows for `PKG-023`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-023`. |
| REQ-023-03-004 | The Construction Work Package shall assign field construction activities (grading, foundations, setting equipment on foundations, mechanical hookup, structural support installation, electrical terminations, home-run cable installation) to Tourmaline Oil Corporation. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section. | Construction responsibility matrix review against the DBM Construction Responsibility section. |
| REQ-023-03-005 | The Construction Work Package shall require tie-ins to existing or related facilities to be jointly planned and that tie-in timing be established as the project progresses. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Construction Responsibility section. | Tie-in plan review. |
| REQ-023-03-006 | The Construction Work Package shall require power feeders to the VFD to be 4.160 kV, 3-phase, 3-wire, 60 Hz, low-resistance grounded, consistent with the facility medium-voltage service basis for inverter-drive motors rated 250 hp up to 5,500 hp. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, medium-voltage services table. | Construction electrical scope review. |
| REQ-023-03-007 | The Construction Work Package shall require 4.160 kV medium-voltage cable to be three-conductor copper TECK rated 5 kV with 100 percent insulation, and low-voltage power cable fed from the VFD to be copper TECK cable, unless detailed design specifies otherwise with source basis. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable schedule. | Cable schedule review. |
| REQ-023-03-008 | The Construction Work Package shall require major electrical equipment to be directly connected to the ground grid at two points, and shall require separate copper ground conductors per CEC sizing for distribution transformers, panelboards, and applicable motor circuits, where applicable to this VFD lineup. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Grounding inspection check. |
| REQ-023-03-009 | The Construction Work Package shall require cable tray and conduit routing to preserve maintenance access for the VFD lineup and the driven motor. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray / conduit and maintenance access paragraphs. | Routing and access walkdown. |
| REQ-023-03-010 | Where the VFD drives a motor located in a Zone 2 area, the Construction Work Package shall require the motor to be marked accordingly and supplied with a temperature code lower than that on the area-classification drawing or fugitive-emissions study. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motors / area classification paragraph. | Area-classification verification. |
| REQ-023-03-011 | The Construction Work Package shall preserve as `TBD` (not invent) the VFD topology, isolation transformer, harmonic/output filtering, driven motor identity and load, lift weights and rigging plan, foundation loads, energization sequence, and commissioning steps until vendor data and integration design are accepted. Source: source gap; `_REFERENCES.md`. | Source-gap review before construction execution. |
| REQ-023-03-012 | The Construction Work Package shall produce or preserve the construction interface and turnover checklist artifact identified in `_CONTEXT.md` and `ARTIFACT_REGISTER.csv`. Source: `_CONTEXT.md` Anticipated Artifacts. | Artifact review against `ARTIFACT_REGISTER.csv`. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, cable installation, and installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage, MCC/VFD, grounding, cable, and raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to motor temperature code marking and equipment placement where Zone 2 applies. | Applicable; package-specific area assignment TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, scope, and interface facts. | Authoritative upstream snapshot. |
| `26020-Package_Requirements.docx` | Likely applicable. Document was not opened for a PKG-023-specific match in this run. | ASSUMPTION: likely applicable; clause locations TBD. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare construction work package identity fields to workbook row 25 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare construction interface matrix to `INTERFACE_REGISTER.csv` rows for `PKG-023`. | All six interfaces (Electrical Power, Grounding/Bonding, I&C/Control Cabling, Communications/Network, Maintenance Access, Structural/Foundations/Supports) are represented. |
| Construction responsibility split | Compare assigned activities to DBM Construction Responsibility section and `PACKAGE_REGISTER.csv`. | Tourmaline field-construction scope and EPC integration scope are not conflated with vendor package design. |
| Tie-in coordination | Review tie-in plan against DBM Construction Responsibility section. | Joint planning and progressive tie-in timing are explicit. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not asserted as fact. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and `TBD` items. | No unresolved internal inconsistency. |
| Turnover checklist | Confirm construction interface and turnover checklist artifact is present and references accepted vendor and discipline inputs. | Artifact exists or its `TBD` status is explicit. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Construction work package (master document).
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Source-supported construction scope and responsibility matrix.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 25, applicable Gate 7 registers, and the DBM electrical/construction source slices used for medium-voltage service, cable, grounding, area classification, electrical building, and construction responsibility basis.
