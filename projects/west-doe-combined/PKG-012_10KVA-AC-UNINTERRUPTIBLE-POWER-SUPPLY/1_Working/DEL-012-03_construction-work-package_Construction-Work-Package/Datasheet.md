# Datasheet: DEL-012-03 Construction Work Package

## Identification

| Field | Value |
|---|---|
| Deliverable ID | DEL-012-03_construction-work-package |
| Deliverable name | Construction Work Package |
| Parent package | PKG-012 |
| Package name | 10KVA AC UNINTERRUPTIBLE POWER SUPPLY |
| Discipline | Electrical |
| Type | EPC Construction Work Package |
| Responsible party | EPC Integrator |
| Covers scope item | SOW-0013 |
| Source basis | Workbook Packages row 14; Gate 7 PROJECT_DECOMP snapshot |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package tracking number | 26020-02-30-003 | PACKAGE_REGISTER.csv row PKG-012; 26020-Packages_Interfaces_4_export.xlsx row 14 |
| WBS | 02 | PACKAGE_REGISTER.csv row PKG-012; 26020-Packages_Interfaces_4_export.xlsx row 14 |
| Package discipline | Electrical | PACKAGE_REGISTER.csv row PKG-012; _CONTEXT.md |
| Package role | Vendor-owned electrical package with EPC Integrator facility integration | PACKAGE_REGISTER.csv row PKG-012 |
| Construction deliverable role | Integrator-authored construction work package for physical installation, construction, and tie-in to larger systems | ARTIFACT_REGISTER.csv ART-E686B9A20E |
| Anticipated artifacts | Construction work package; installation and tie-in workface plan; construction interface and turnover checklist | _CONTEXT.md; DELIVERABLE_REGISTER.csv row DEL-012-03 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Applicable workbook interfaces | Electrical Power; Grounding / Bonding; Maintenance Access; Structural / Foundations / Supports | INTERFACE_REGISTER.csv rows IFC-AA089340E0, IFC-2F50872E45, IFC-52E7E27E87, IFC-1D40B1F072; 26020-Packages_Interfaces_4_export.xlsx row 14 |
| UPS electrical basis | UPS services are 120 VAC / 125 VDC for control system, selected emergency/critical lighting, MV breaker control, and MV protective relay | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-12 Electrical Basis |
| Low-voltage service relation | UPS 10 kVA or smaller is associated with 120/208 V, 3 phase, 4 wire, 60 Hz solid grounded lighting and utility service; UPS larger than 10 kVA is associated with 600 V low-voltage service | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md SEC-12 Electrical Basis |
| Declared upstream dependencies | None declared | _DEPENDENCIES.md |
| Declared downstream dependencies | None declared | _DEPENDENCIES.md |
| Package-specific exclusions | TBD; no package-specific exclusions stated in source materials | PACKAGE_REGISTER.csv row PKG-012 |

## Construction

| Construction element | Required treatment in the construction work package | Source |
|---|---|---|
| Physical installation | Define field installation scope, sequence, constraints, and workface readiness for the UPS package without taking over vendor-owned package engineering/design | _CONTEXT.md; PACKAGE_REGISTER.csv row PKG-012 |
| Electrical power tie-in | Include power-source, isolation, termination, testing, and energization coordination placeholders; final values are TBD unless confirmed by issued design documents | INTERFACE_REGISTER.csv IFC-AA089340E0; DBM SEC-12 |
| Grounding and bonding | Include grounding/bonding connection and inspection checklist items; exact conductor/routing details are TBD | INTERFACE_REGISTER.csv IFC-2F50872E45 |
| Maintenance access | Include access, clearance, and maintainability checks around installed UPS equipment; dimensions are TBD | INTERFACE_REGISTER.csv IFC-52E7E27E87 |
| Structural/foundations/supports | Include support, anchorage, housekeeping pad, or mounting confirmation as applicable; final support details are TBD | INTERFACE_REGISTER.csv IFC-1D40B1F072 |
| Turnover | Include inspection, test, interface, and turnover records for the approved package | ARTIFACT_REGISTER.csv ART-DF82A3314B |

## References

- _CONTEXT.md for deliverable identity, scope, anticipated artifacts, and objective list.
- _DEPENDENCIES.md for declared dependency state.
- Gate 7 DELIVERABLE_REGISTER.csv row DEL-012-03.
- Gate 7 PACKAGE_REGISTER.csv row PKG-012.
- Gate 7 ARTIFACT_REGISTER.csv rows ART-E686B9A20E, ART-4ED1456A5C, ART-DF82A3314B.
- Gate 7 INTERFACE_REGISTER.csv rows IFC-AA089340E0, IFC-2F50872E45, IFC-52E7E27E87, IFC-1D40B1F072.
- Gate 7 OBJECTIVE_DELIVERABLE_MAP.csv rows for DEL-012-03 and OBJ-002, OBJ-004, OBJ-005, OBJ-008, OBJ-009, OBJ-010.
- _Sources/26020-Packages_Interfaces_4_export.xlsx, Packages sheet row 14.
- _Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, SEC-12 Electrical Basis.
