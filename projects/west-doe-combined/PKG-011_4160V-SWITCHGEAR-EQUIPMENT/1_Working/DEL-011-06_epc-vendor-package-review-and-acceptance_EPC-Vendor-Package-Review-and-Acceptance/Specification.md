# Specification: EPC Vendor Package Review and Acceptance

## Scope

This specification defines the EPC Integrator acceptance basis for DEL-011-06, covering vendor package review, integration acceptance, and handoff readiness for PKG-011, 4160V SWITCHGEAR EQUIPMENT. It covers review evidence, acceptance checklist evidence, factory/shop test and inspection evidence, and turnover evidence identified in Gate 7.

Excluded from this deliverable: Package Vendor engineering, package design, vendor documentation production, and physical equipment supply. Those responsibilities remain with the Package Vendor under the Gate 7 PKG-011 responsibility model. Package-specific exclusions beyond that model are TBD because no additional exclusions were stated in the available source materials.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-011-06-001 | The acceptance package shall preserve the Package Vendor / EPC Integrator split: Package Vendor owns package engineering, package design, vendor documentation, and physical equipment; EPC Integrator owns integration into the functional process facility. | Gate 7 `PACKAGE_REGISTER.csv`, PKG-011. |
| REQ-011-06-002 | The EPC acceptance file shall include a vendor document review and comment log. | Gate 7 `ARTIFACT_REGISTER.csv`, ART-A43AC29984. |
| REQ-011-06-003 | The EPC acceptance file shall include a vendor package acceptance and turnover checklist. | Gate 7 `ARTIFACT_REGISTER.csv`, ART-B4B14E04DE. |
| REQ-011-06-004 | The EPC acceptance file shall include factory/shop test and inspection evidence. | Gate 7 `ARTIFACT_REGISTER.csv`, ART-D93D35BDC7. |
| REQ-011-06-005 | Acceptance review shall address each declared PKG-011 interface type: Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. | Workbook `26020-Packages_Interfaces_4_export.xlsx`, Packages row 13; Gate 7 `INTERFACE_REGISTER.csv`, PKG-011. |
| REQ-011-06-006 | Acceptance review shall verify that vendor information needed for medium-voltage service aligns with the 4,160 V, 3 phase, 3 wire, 60 Hz LRG basis where applicable to the package. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 System Voltages. |
| REQ-011-06-007 | Acceptance review shall verify that vendor information for the 4160V MCC supports field-fused contactors, motor protection relays, and EtherNet communication to the plant PLC central control panel, or shall record deviations/open items. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC. |
| REQ-011-06-008 | Acceptance review shall verify that vendor interface information supports required separation between power circuits and control/instrument circuits, or shall record unresolved routing/shielding/open-item requirements. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Buildings, Raceways, Lighting, and Heat Tracing. |
| REQ-011-06-009 | ASSUMPTION: The acceptance checklist should include an open-item register or equivalent disposition field for vendor-document, interface, test, and turnover gaps. | Supported directionally by OBJ-010 in Gate 7 `OBJECTIVE_REGISTER.csv`; exact project form is TBD. |

## Standards

| Standard / control | Applicability |
|---|---|
| Gate 7 PROJECT_DECOMP snapshot | Authoritative decomposition and register basis for package identity, responsibility, deliverable scope, artifacts, interfaces, and objective mapping. |
| 03-25 Compressor Station and Liquids Hub DBM, SEC-12 Electrical Basis | Source basis for electrical service, 4160V MCC, separation, raceway, grounding, bonding, and detailed-design coordination expectations. |
| Project electrical specifications | Mentioned by the DBM as governing cable tray, conduit, grounding, and bonding; specific document numbers and clauses are TBD because no specification slice was available in this deliverable context. |
| Vendor package requirements document | Available as `26020-Package_Requirements.docx`, but no package-specific heading was matched for PKG-011 in Gate 7 (`DocxPackageMatched=FALSE`); package-specific requirements remain TBD unless later source slices are identified. |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-011-06-001 | Confirm acceptance package assigns vendor and EPC responsibilities without transferring vendor engineering/design duties to EPC. |
| REQ-011-06-002 | Check that the vendor document review log exists and records review status and comment disposition for vendor documents. |
| REQ-011-06-003 | Check that the acceptance and turnover checklist exists and references EPC Scope of Work, Package Datasheet, Construction Work Package, vendor documents, interface items, tests, and turnover records. |
| REQ-011-06-004 | Check that factory/shop test and inspection evidence is present or explicitly listed as TBD/open. |
| REQ-011-06-005 | Check that all six declared interface types are represented in the acceptance checklist or open-item register. |
| REQ-011-06-006 | Check vendor electrical data against the 4,160 V service basis where the vendor package supplies or interfaces with MV equipment. |
| REQ-011-06-007 | Check 4160V MCC vendor data for contactor, relay, and communications evidence or recorded deviation. |
| REQ-011-06-008 | Check interface documentation for power/control separation requirements or recorded detailed-design open item. |
| REQ-011-06-009 | Check that unresolved gaps are carried as controlled open items with owner and disposition status. |

## Documentation

Required documentation artifacts for this deliverable:

- Vendor document review and comment log.
- Vendor package acceptance and turnover checklist.
- Factory/shop test and inspection evidence.
- Turnover evidence.
- ASSUMPTION: Open-item / exception log tied to acceptance status; exact form TBD.
