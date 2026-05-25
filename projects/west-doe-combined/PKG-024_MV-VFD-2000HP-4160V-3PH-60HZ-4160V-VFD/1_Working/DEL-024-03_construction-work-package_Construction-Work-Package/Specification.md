# Specification: DEL-024-03_construction-work-package

## Scope

This specification governs the EPC Integrator-authored Construction Work Package for `PKG-024`, the MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD package. The Construction Work Package is a mandatory Gate 5 EPC anchor deliverable describing how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems.

The package is a vendor-owned Electrical package under WBS 01. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Field construction is assigned to Tourmaline Oil Corporation per the DBM Construction Responsibility section.

Exclusions:

- Vendor detailed design calculations, certified drawings, factory acceptance testing, and final equipment selections are excluded except where required as input to construction planning.
- Package-specific installation location, foundation drawings, cable schedules, tie-in point coordinates, exact driven-motor identity, and detailed turnover checklist content are `TBD` because the accessible source set does not provide confirmed package-specific values.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-024-03-001 | The Construction Work Package shall identify `PKG-024`, workbook row 26, WBS 01, CoA tracking number 26020-01-30-015, discipline Electrical, and package name "MV VFD - 2000HP, 4160V, 3PH, 60HZ - 4160V VFD." Source: Workbook Packages row 26; `PACKAGE_REGISTER.csv`. | Identity review against workbook row and Gate 7 registers. |
| REQ-024-03-002 | The Construction Work Package shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces; Tourmaline performs field construction. Source: `PACKAGE_REGISTER.csv` row `PKG-024`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Construction Responsibility section. | Responsibility statement review against Gate 7 package register and DBM. |
| REQ-024-03-003 | The Construction Work Package shall include the six applicable interface facts: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; and Structural / Foundations / Supports. Source: Workbook Packages row 26; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-024`. |
| REQ-024-03-004 | The Construction Work Package shall specify Tourmaline field construction scope at minimum for: shipping/off-loading, setting modules/equipment on foundations, mechanical hookup of modules and interconnecting piping, installation of shipped-loose instruments/valves/components, installation of miscellaneous structural supports, field installation of home-run cables, and electrical terminations. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Construction Responsibility section. | Workface-plan review against the DBM construction-scope list. |
| REQ-024-03-005 | The Construction Work Package shall flag installation of interconnecting piping/cabling to ISBL/OSBL tie-in points as an external interface responsibility marker requiring per-tie-in confirmation, and shall require joint planning for tie-ins to existing or related facilities. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Construction Responsibility section. | Tie-in list review; each tie-in carries an assigned responsibility or `TBD`. |
| REQ-024-03-006 | The Construction Work Package shall require grounding/bonding construction to comply with the DBM facility grounding basis: two-point ground-grid connection for major electrical equipment and separate copper ground conductors per CEC sizing for applicable equipment. Detailed conductor sizing for this VFD package shall be confirmed by detailed design. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding and bonding paragraphs. | Grounding/bonding inspection check. |
| REQ-024-03-007 | The Construction Work Package shall require cable tray and conduit routing not to interfere with maintenance access. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, cable tray and conduit paragraphs. | Walkdown check against routing drawings; maintenance access preserved. |
| REQ-024-03-008 | If the driven motor is located in a Zone 2 area, the Construction Work Package shall require area-classification marking and temperature-code verification per the DBM. Applicability is `TBD` pending area classification of the driven motor location. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, motor/VFD paragraphs. | Area-classification verification at installation. |
| REQ-024-03-009 | The Construction Work Package shall include a construction interface and turnover checklist covering mechanical setting, electrical terminations, grounding, I&C terminations, network connection, and maintenance access. Detailed checklist content is `TBD` and shall be developed with vendor input at detailed engineering. Source: `_CONTEXT.md` (Anticipated Artifacts); source gap on package-level checklist content. | Turnover checklist review at pre-energization. |
| REQ-024-03-010 | The Construction Work Package shall identify source gaps for installation location, driven-motor identification, tie-in coordinates, foundation details, cable schedules, and detailed turnover checklist content as `TBD` instead of invented values. Source: `_REFERENCES.md`; `26020-Package_Requirements.docx` package search. | Gap review before construction handoff. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, cable installation, and electrical termination basis referenced by the DBM electrical section. | Applicable; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway/VFD basis referenced by the DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to VFD-fed motors located in Zone 2 areas (marking and temperature code). | Applicable; package-specific area classification TBD. |
| DBM Construction Responsibility basis | Tourmaline field construction scope and external-interface tie-in marker. | Applicable as source-supported construction scope. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare Construction Work Package identity fields to workbook row 26 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare construction interface matrix to `INTERFACE_REGISTER.csv` rows for `PKG-024`. | All six interfaces (Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) are addressed. |
| Construction scope fidelity | Compare workface plan to DBM Construction Responsibility list. | All applicable Tourmaline field-scope items are reflected. |
| Tie-in handling | Review tie-in list. | Each tie-in carries responsibility assignment or `TBD` marker per the DBM external-interface basis. |
| Source fidelity | Check every non-trivial value against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv` and DBM Construction Responsibility section. | Vendor, EPC, and Tourmaline field construction scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and `TBD` set. | No unresolved internal inconsistency. |

## Documentation

The deliverable shall produce or preserve these artifacts (from `_CONTEXT.md` Anticipated Artifacts):

- Construction work package (governing document).
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.

Supporting documentation shall include:

- Citations to Workbook Packages row 26, Gate 7 registers, and the DBM Construction Responsibility section.
- Source-gap / `TBD` list for vendor or human resolution.
- Cross-reference to interface registry IDs for PKG-024.
