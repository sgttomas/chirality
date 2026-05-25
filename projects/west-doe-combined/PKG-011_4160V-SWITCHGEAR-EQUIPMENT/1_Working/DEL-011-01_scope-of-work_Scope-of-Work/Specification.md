# Specification: DEL-011-01 Scope of Work

## Scope

This deliverable specifies the required content for the EPC Integrator's Scope of Work for PKG-011, `4160V SWITCHGEAR EQUIPMENT`. It covers package identity, source basis, WBS, discipline, package function, tagged-equipment basis where source-supported, package boundaries, whole-facility integration narrative, interface categories, and responsibility assignment.

The Scope of Work must preserve the Gate 7 responsibility split: the Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; the EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. Source: Gate 7 `PACKAGE_REGISTER.csv` row PKG-011; Gate 7 `PROJECT_DECOMP.md` Decision DEC-006.

Excluded from this deliverable: vendor package design, final equipment ratings, final electrical studies, final protection settings, and package-specific exclusions not stated in source materials. These remain `TBD` or belong to downstream vendor/design deliverables. Source: Gate 7 `PROJECT_DECOMP.md` Section 7; Gate 7 `PACKAGE_REGISTER.csv` row PKG-011.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| SOW-REQ-001 | The Scope of Work shall identify DEL-011-01, PKG-011, workbook ID 11, Workbook Packages row 13, WBS 02, CoA tracking number 26020-02-30-002, discipline Electrical, and package name `4160V SWITCHGEAR EQUIPMENT`. | Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-011-01; Gate 7 `PACKAGE_REGISTER.csv` row PKG-011. |
| SOW-REQ-002 | The Scope of Work shall state that PKG-011 is a workbook-defined vendor-responsible Electrical package and a distinct flat project package. | Gate 7 `SCOPE_LEDGER.csv` row SOW-0012. |
| SOW-REQ-003 | The Scope of Work shall assign package engineering, package design, vendor documentation, and physical equipment package responsibility to the Package Vendor. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-011; Gate 7 `ARTIFACT_REGISTER.csv` row ART-8698ECE3AB. |
| SOW-REQ-004 | The Scope of Work shall assign facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration to the EPC Integrator. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-011; Gate 7 `ARTIFACT_REGISTER.csv` row ART-8698ECE3AB. |
| SOW-REQ-005 | The Scope of Work shall include or reference a tagged equipment and package identity list containing package name, workbook ID, CoA tracking number, WBS, and detailed major-equipment text where source-supported. | Gate 7 `ARTIFACT_REGISTER.csv` row ART-117272CC52. |
| SOW-REQ-006 | The Scope of Work shall include a package function and whole-facility integration narrative. | Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-011-01; Gate 7 `ARTIFACT_REGISTER.csv` row ART-CBD9485295. |
| SOW-REQ-007 | The Scope of Work shall preserve the declared PKG-011 interface categories: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. | Gate 7 `INTERFACE_REGISTER.csv` rows IFC-59155DCD8A through IFC-680C970D3C. |
| SOW-REQ-008 | The Scope of Work shall not invent package-specific exclusions; exclusions shall remain `TBD` where source materials state no package-specific exclusions. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-011. |
| SOW-REQ-009 | The Scope of Work shall treat the 4160V MCC/switchgear technical basis conservatively: 03-25 DBM SEC-12 identifies a 4160V MCC serving large 4000V motors, including KM-2150 and KM-2250, with motor protection relays and an EtherNet communication port to the plant PLC central control panel; final equipment ratings and studies remain downstream detailed-design/vendor scope unless otherwise sourced. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 `4160V MCC`; Gate 7 `PROJECT_DECOMP.md` Section 7. |
| SOW-REQ-010 | The Scope of Work shall carry unresolved electrical design-development items as `TBD` when they affect this package, including 4.16 kV motor starting and shared 04-25/03-25 power coordination where applicable. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 unresolved electrical basis table; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12. |

## Standards

| Standard or basis | Applicability | Source |
|---|---|---|
| CSA C22.1-21 Canadian Electrical Code | Electrical installation basis for the facility electrical system and electrical devices/instrumentation certification expectations. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 `Electrical Design Basis` and standards table. |
| Applicable BC provincial and local electrical codes and regulations | Electrical design and installation compliance basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 `Electrical Design Basis`. |
| CSA, API, IEEE, ISA, NEMA, WorkSafeBC, Technical Safety BC, BCER | Applicable standards/regulatory bodies listed for electrical materials, equipment, testing, and inspection; exact clause applicability is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 `Electrical Design Basis`. |
| Project electrical and instrumentation specifications | Governing project specification set for electrical distribution design and electrical equipment procurement basis; specific spec revision applicability is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, SEC-12 Table 12-1. |

## Verification

| Requirement | Verification approach |
|---|---|
| SOW-REQ-001 through SOW-REQ-002 | Check the Scope of Work identity block against Gate 7 `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, and `SCOPE_LEDGER.csv`. |
| SOW-REQ-003 through SOW-REQ-004 | Check responsibility text against Gate 7 `PACKAGE_REGISTER.csv` and `ARTIFACT_REGISTER.csv`; confirm vendor design work is not assigned to EPC Integrator. |
| SOW-REQ-005 through SOW-REQ-006 | Confirm anticipated artifacts are present or explicitly referenced in the Scope of Work. |
| SOW-REQ-007 | Confirm all six PKG-011 interface categories are listed and none are converted into standalone deliverables. |
| SOW-REQ-008 through SOW-REQ-010 | Confirm unknowns and unresolved design-development items are marked `TBD` rather than resolved by assumption. |

## Documentation

The completed Scope of Work should produce or reference:

- Package scope of work.
- Tagged equipment and package identity list.
- Package function and whole-facility integration narrative.
- Responsibility assignment record.

Source: `_CONTEXT.md`; Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-011-01; Gate 7 `ARTIFACT_REGISTER.csv` rows ART-4FE41463DD through ART-8698ECE3AB.
