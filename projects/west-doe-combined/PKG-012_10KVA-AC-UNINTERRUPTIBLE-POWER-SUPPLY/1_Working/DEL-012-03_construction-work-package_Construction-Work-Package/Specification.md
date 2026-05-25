# Specification: DEL-012-03 Construction Work Package

## Scope

This specification defines the minimum content and acceptance basis for the EPC Integrator's construction work package for PKG-012, the 10KVA AC UNINTERRUPTIBLE POWER SUPPLY package.

The construction work package covers physical installation, field construction planning, inspection, turnover, and tie-in to larger facility systems. It does not replace the Package Vendor's package engineering, package design, vendor documentation, or physical equipment package responsibilities.

## Requirements

| ID | Requirement | Source |
|---|---|---|
| CWP-001 | The construction work package shall identify DEL-012-03, PKG-012, package name, responsible party, WBS 02, tracking number 26020-02-30-003, and covered scope item SOW-0013. | _CONTEXT.md; PACKAGE_REGISTER.csv row PKG-012; DELIVERABLE_REGISTER.csv row DEL-012-03 |
| CWP-002 | The construction work package shall distinguish EPC Integrator facility-level integration, tie-ins, constructability, procurement/construction coordination, and facility integration from Package Vendor-owned engineering, design, documentation, and physical equipment supply. | PACKAGE_REGISTER.csv row PKG-012 |
| CWP-003 | The work package shall include a construction work package artifact, an installation and tie-in workface plan, and a construction interface and turnover checklist. | _CONTEXT.md; ARTIFACT_REGISTER.csv rows ART-E686B9A20E, ART-4ED1456A5C, ART-DF82A3314B |
| CWP-004 | The work package shall address the declared package interfaces: Electrical Power, Grounding / Bonding, Maintenance Access, and Structural / Foundations / Supports. | INTERFACE_REGISTER.csv rows IFC-AA089340E0, IFC-2F50872E45, IFC-52E7E27E87, IFC-1D40B1F072 |
| CWP-005 | The electrical tie-in basis shall remain consistent with the DBM electrical basis for UPS services: 120 VAC / 125 VDC serving control system, selected emergency/critical lighting, MV breaker control, and MV protective relay. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-12 Electrical Basis |
| CWP-006 | The work package shall not assert final feeder, breaker, cable, battery, mounting, clearance, or test values unless those values are confirmed in issued design/vendor documents; otherwise the values shall remain TBD. | PACKAGE_REGISTER.csv row PKG-012; DBM SEC-12; source gap noted in _REFERENCES.md |
| CWP-007 | The turnover checklist shall capture inspection, interface, tie-in, test, and turnover evidence for the approved package. | ARTIFACT_REGISTER.csv ART-DF82A3314B |

## Standards

| Standard or basis | Applicability | Status |
|---|---|---|
| Gate 7 PROJECT_DECOMP final published snapshot | Accepted upstream decomposition truth for package, deliverable, artifact, objective, and interface basis | Accessible |
| Workbook Packages row 14 | Authoritative workbook row for package identity and interface X-column facts | Accessible through _Sources/26020-Packages_Interfaces_4_export.xlsx |
| DBM-Comp_and_Liquids SEC-12 Electrical Basis | Electrical basis for UPS service categories and facility electrical integration | Accessible |
| CEC, area classification standards, project electrical specifications, voltage/MCC/grounding basis | Electrical discipline standards named in the DBM standards summary | Location TBD; clause-level requirements not extracted for this deliverable |

## Verification

| Requirement | Verification approach |
|---|---|
| CWP-001 | Check title block, package metadata, and scope summary against _CONTEXT.md and Gate 7 registers. |
| CWP-002 | Review responsibility matrix or execution notes for clear EPC Integrator versus Package Vendor boundaries. |
| CWP-003 | Confirm the three anticipated artifacts are present or explicitly tracked as deliverable sections/attachments. |
| CWP-004 | Check that each declared interface has a construction action, inspection hold/check point, and turnover evidence field. |
| CWP-005 | Check electrical tie-in narrative and test plan against DBM SEC-12; any unsupported final values must be marked TBD. |
| CWP-006 | Review numeric/equipment values against issued design/vendor documents before release for construction. |
| CWP-007 | Confirm turnover checklist contains inspection, interface, tie-in, test, and turnover records. |

## Documentation

The deliverable shall produce or include the following records:

- Construction work package.
- Installation and tie-in workface plan.
- Construction interface and turnover checklist.
- Electrical power tie-in checklist.
- Grounding/bonding inspection record.
- Maintenance access and clearance check record.
- Structural/foundations/supports installation check record.
- Energization or pre-energization checklist with unsupported values marked TBD pending issued design/vendor documents.
