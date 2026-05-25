# Specification: DEL-033-03_construction-work-package

## Scope

This specification governs the EPC Integrator-authored Construction Work Package for `PKG-033`, the 4160V SWITCHGEAR ELECTRICAL BUILDING (830-2). The Construction Work Package is a mandatory Gate 5 EPC anchor deliverable describing how the package will be physically installed, built, inspected, turned over, and tied into the larger facility systems.

The package is a vendor-owned Electrical package under WBS 02. The Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. The EPC Integrator owns facility integration, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.

Exclusions:

- Vendor detailed design, switchgear bus arrangement, breaker count, protection scheme, and final equipment selections are excluded from this EPC construction work package unless later provided as vendor data.
- Detailed pile and foundation design, package-specific tie-in cable schedules, and per-circuit terminations are `TBD` because the accessible source set does not provide confirmed package-specific values.
- The 830-2 building location, process service assignment, and any -2 variant differentiation from the listed `830-1` are `TBD` pending an explicit source.

## Requirements

| ID | Requirement | Verification |
|---|---|---|
| REQ-033-03-001 | The Construction Work Package shall identify `PKG-033`, workbook row 35, WBS 02, CoA tracking number 26020-02-30-024, discipline Electrical, and package name "4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)". Source: Workbook Packages row 35; `PACKAGE_REGISTER.csv`. | Identification review against workbook row and Gate 7 registers. |
| REQ-033-03-002 | The Construction Work Package shall state the accepted responsibility split: Package Vendor owns package engineering/design/vendor documentation/physical equipment; EPC Integrator owns facility integration and interfaces. Source: `PACKAGE_REGISTER.csv` row `PKG-033`. | Responsibility statement review against Gate 7 package register. |
| REQ-033-03-003 | The Construction Work Package shall enumerate the twelve applicable interface facts for `PKG-033`: Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. Source: Workbook Packages row 35; `INTERFACE_REGISTER.csv`. | Interface matrix check against `INTERFACE_REGISTER.csv` rows for `PKG-033`. |
| REQ-033-03-004 | The Construction Work Package shall require building installation as an elevated, pile-supported, prefabricated modular electrical building with bottom-entry incoming and outgoing power cables. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph. | Building installation plan review against DBM source slice. |
| REQ-033-03-005 | The Construction Work Package shall require cable tray and conduit installation that preserves maintenance access and equipment removal pathways, and shall require TECK/ACIC cable usage with EMT conduit between adjacent equipment. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings and cable tray paragraphs. | Routing/wiring review against the DBM electrical conventions. |
| REQ-033-03-006 | The Construction Work Package shall require grounding installation including two-point ground-grid connection for major electrical equipment, ground wells with bolted test connections at electrical buildings/transformers, compression-type ground connections, and PVC-conducted above-grade ground wires where mechanically protected. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs. | Grounding installation inspection against DBM grounding basis. |
| REQ-033-03-007 | The Construction Work Package shall require HVAC commissioning that demonstrates the n+1 cooling arrangement so loss of one HVAC unit does not affect building heating/cooling. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph. | HVAC commissioning record review. |
| REQ-033-03-008 | The Construction Work Package shall require an outdoor GFI receptacle for exterior maintenance and equipment doors sized (or with removable transoms) for largest-equipment removal. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, electrical buildings paragraph. | Field installation check. |
| REQ-033-03-009 | The Construction Work Package shall include the anticipated artifacts: construction work package; installation and tie-in workface plan; construction interface and turnover checklist. Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-033-03_construction-work-package`. | Artifact set check against `_CONTEXT.md` anticipated artifacts. |
| REQ-033-03-010 | The Construction Work Package shall record source gaps for switchgear bus/breaker/protection details, 830-2 building location/process service, foundation/pile design loads, schedule/tie-in windows, and per-circuit cable schedules as `TBD` instead of invented values. Source: `_REFERENCES.md`. | Gap review before construction execution. |
| REQ-033-03-011 | The Construction Work Package shall preserve the 4.160 kV, 3-phase, 3-wire, 60 Hz, low-resistance-grounded medium-voltage service basis and the 5 kV three-conductor copper TECK cable basis where 4.16 kV circuits are within scope. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage and cable tables. | Cable and termination plan review against DBM source. |

## Standards

| Standard / basis | Applicability | Status |
|---|---|---|
| Canadian Electrical Code (CEC) | Electrical grounding, conduit support, and electrical installation basis referenced by DBM electrical section. | Applicable as source-supported design basis; clause locations TBD. |
| Project electrical specifications | Voltage/MCC/grounding/cable/raceway basis referenced by DBM electrical section. | Applicable; document location TBD. |
| Area classification standards | Applicable to electrical equipment, conduit sealing, and installation classification where hazardous/non-hazardous areas are defined; electrical buildings shall be in general purpose areas per DBM. | Applicable; package location/classification TBD. |
| Gate 7 PROJECT_DECOMP snapshot | Accepted decomposition truth for package identity, deliverable basis, artifacts, and interface facts. | Authoritative upstream snapshot. |

## Verification

| Verification item | Method | Acceptance basis |
|---|---|---|
| Identity completeness | Compare construction work package identity to workbook row 35 and Gate 7 registers. | All fields match accepted source spelling and IDs. |
| Interface completeness | Compare construction work package interface coverage to `INTERFACE_REGISTER.csv` rows for `PKG-033`. | All twelve applicable interfaces are addressed. |
| Source fidelity | Check every non-trivial value or requirement against cited source slices. | Unsupported values are marked `TBD` or `ASSUMPTION`, not treated as requirements. |
| Responsibility split | Compare responsibility language to `PACKAGE_REGISTER.csv`. | Vendor and EPC scopes are not conflated. |
| Cross-document consistency | Confirm Datasheet, Specification, Guidance, and Procedure use the same package name, IDs, interfaces, and TBDs. | No unresolved internal inconsistency. |
| Construction artifact set | Confirm artifacts include construction work package, installation/tie-in workface plan, and turnover checklist. | Artifact set matches `_CONTEXT.md` anticipated artifacts. |

## Documentation

The deliverable shall produce or preserve these artifacts:

- Construction work package.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Source-gap / `TBD` list for vendor or human resolution.

The deliverable shall cite the Gate 7 snapshot, workbook row 35, applicable Gate 7 registers, and the DBM electrical source slices used for medium-voltage service, electrical-building, grounding, cable tray/conduit, and motor-starting context.
