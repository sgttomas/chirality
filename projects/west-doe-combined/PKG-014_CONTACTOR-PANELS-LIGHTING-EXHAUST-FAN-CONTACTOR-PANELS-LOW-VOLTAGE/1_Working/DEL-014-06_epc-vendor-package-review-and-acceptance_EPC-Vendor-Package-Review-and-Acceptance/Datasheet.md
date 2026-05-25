# Datasheet — DEL-014-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-014-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-014` |
| ParentWorkbookID | 14 |
| PackageName | CONTACTOR PANELS - LIGHTING / EXHAUST FAN CONTACTOR PANELS - LOW VOLTAGE |
| Discipline | Electrical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Covers Scope Items | `SOW-0015` |
| Supports Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` |
| Source Row | Workbook Packages row 16 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Acceptance Owner | EPC Integrator | PACKAGE_REGISTER.csv row PKG-014 |
| Package Vendor Role | Engineering, design, vendor documentation, physical equipment package | PACKAGE_REGISTER.csv row PKG-014 |
| EPC Integrator Role | Integration into the functional process facility (interfaces, tie-ins, constructability, facility-level integration) | PACKAGE_REGISTER.csv row PKG-014 |
| Anticipated Artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row DEL-014-06 |
| Acceptance Basis Documents | DEL-014-01 Scope of Work; DEL-014-02 Package Datasheet; DEL-014-03 Construction Work Package | DELIVERABLE_REGISTER.csv rows |
| Acceptance Target | Vendor-supplied DEL-014-04 Vendor Engineered Equipment Package and DEL-014-05 Vendor Document Turnover Package | DELIVERABLE_REGISTER.csv rows |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site ambient design floor | -40 deg C minimum ambient governs exposed package buildings, control panels, instrumentation, and field devices | DBM 3-25, line 145 |
| Low-voltage system voltage | 600 V, 3 phase, 3 wire, 60 Hz HRG with 5A continuous resistor (for LV motors, lighting transformers, building heaters, UPS > 10 kVA) | DBM 3-25, line 734 |
| Lighting/utility voltage | 120/208 V, 3 phase, 4 wire, 60 Hz solid grounded | DBM 3-25, line 735 |
| Standby power source | LV standby generators on the LV MCC with transfer switch | DBM 3-25, line 505 |
| Remote I/O interface to exhaust fans/heaters | Allen-Bradley Flex5000 RIO nodes may support building exhaust fan and heater controls | DBM 3-25, line 804 |

## Construction

| Item | Detail | Source |
|---|---|---|
| Acceptance Form | Review and acceptance evidence package (logs, checklists, test/inspection records, turnover documents) | `_CONTEXT.md` |
| Receiving party | EPC Integrator project controls / engineering management | PACKAGE_REGISTER.csv row PKG-014 |
| Issuing party | Package Vendor for vendor evidence; EPC Integrator for integration verification | PACKAGE_REGISTER.csv row PKG-014 |
| Format | Document set with controlled revisions; tabular review log; binary or graded acceptance checklist | ASSUMPTION (no source format prescribed) |

## References

- PACKAGE_REGISTER.csv (Gate 7 snapshot), row PKG-014.
- DELIVERABLE_REGISTER.csv (Gate 7 snapshot), row `DEL-014-06_epc-vendor-package-review-and-acceptance`.
- DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (Sections covering site basis, LV/lighting/UPS systems, MCC, RIO, electrical buildings).
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` in this deliverable folder.
- Upstream basis deliverables (peer rows): DEL-014-01 (SOW), DEL-014-02 (Package Datasheet), DEL-014-03 (Construction Work Package).
- Acceptance targets (peer rows): DEL-014-04 (Vendor Engineered Equipment Package), DEL-014-05 (Vendor Document Turnover Package).
- Workbook Packages row 16 (cited by package register; not locally sliced).
