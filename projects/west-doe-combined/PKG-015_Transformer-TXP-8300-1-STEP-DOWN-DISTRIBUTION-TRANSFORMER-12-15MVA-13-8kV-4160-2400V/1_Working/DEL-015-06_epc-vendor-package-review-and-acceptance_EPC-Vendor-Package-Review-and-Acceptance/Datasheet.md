# Datasheet — DEL-015-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-015-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-015` |
| ParentWorkbookID | 15 |
| PackageName | Transformer TXP-8300-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 12/15MVA 13.8kV/4160/2400V |
| Discipline | Electrical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Covers Scope Items | `SOW-0016` |
| Supports Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` |
| Source Row | Workbook Packages row 17 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Acceptance Owner | EPC Integrator | PACKAGE_REGISTER.csv row PKG-015 |
| Package Vendor Role | Package engineering, package design, vendor documentation, physical equipment package | PACKAGE_REGISTER.csv row PKG-015 |
| EPC Integrator Role | Integration into the functional process facility (interfaces, tie-ins, constructability, procurement/construction coordination, facility-level integration) | PACKAGE_REGISTER.csv row PKG-015 |
| Anticipated Artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv row DEL-015-06 |
| Acceptance Basis Deliverables | DEL-015-01 Scope of Work; DEL-015-02 Package Datasheet; DEL-015-03 Construction Work Package | DELIVERABLE_REGISTER.csv rows DEL-015-01/02/03 |
| Acceptance Target Deliverables | Vendor-supplied DEL-015-04 Vendor Engineered Equipment Package and DEL-015-05 Vendor Document Turnover Package | DELIVERABLE_REGISTER.csv rows DEL-015-04/05 |
| Declared Package Interfaces | Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports | INTERFACE_REGISTER.csv rows for PKG-015 (7 entries) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site ambient design envelope | -40 deg C minimum to +35 deg C maximum | DBM 3-25, lines 96, 100-101, 686 |
| Low-ambient governance for exposed equipment | -40 deg C minimum ambient governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe condition applies | DBM 3-25, line 145 |
| Site elevation | 673 m AMSL | DBM 3-25, line 686 |
| Incoming MV service basis (facility) | 13.8 kV, 3 phase, 3 wire, 60 Hz LRG cross-facility feed from 04-25 main switchgear | DBM 3-25, lines 732, 740 |
| Medium-voltage service (facility, 4160V class) | 4,160 V, 3 phase, 3 wire, 60 Hz LRG for process AC inverter-drive motors 250 hp to 5,500 hp | DBM 3-25, line 733 |
| Closest DBM transformer reference | "13.8 kV to 4.16 kV, 12 MVA transformer" feeding the 4160V MCC for 4000V motors | DBM 3-25, line 744 |
| Package-named voltage taps | Package name carries 13.8kV / 4160V / 2400V; the 2400V tap is not described in the accessible DBM slice | CONFLICT: see Guidance Conflict Table HRR-015-06-001 |
| Power vs control cable separation basis | Power circuits at 13.8 kV, 4,160 V, and 600 V shall be separated from control and instrument circuits by distance, shielding, or routing | DBM 3-25, line 768 |

## Construction

| Item | Detail | Source |
|---|---|---|
| Acceptance form | Review and acceptance evidence package (review log, acceptance checklist, test/inspection records, turnover documents) | `_CONTEXT.md` anticipated artifacts |
| Receiving party | EPC Integrator project controls / engineering management | PACKAGE_REGISTER.csv row PKG-015 (EPC Integrator owns facility integration) |
| Issuing party | Package Vendor for vendor-side evidence; EPC Integrator for integration verification | PACKAGE_REGISTER.csv row PKG-015 |
| Format | Document set with controlled revisions; tabular vendor document review log; checklist-style acceptance record with explicit dispositions | ASSUMPTION (no source-prescribed format) |
| Granularity | At least one row per declared package interface and one row per anticipated artifact type | ASSUMPTION grounded in INTERFACE_REGISTER.csv rows for PKG-015 and `_CONTEXT.md` anticipated artifacts |

## References

- PACKAGE_REGISTER.csv (Gate 7 snapshot), row PKG-015.
- DELIVERABLE_REGISTER.csv (Gate 7 snapshot), row `DEL-015-06_epc-vendor-package-review-and-acceptance`; sibling rows DEL-015-01 through DEL-015-05.
- INTERFACE_REGISTER.csv (Gate 7 snapshot), 7 rows for PKG-015.
- OBJECTIVE_SCOPE_MAP.csv (Gate 7 snapshot), rows mapping OBJ-002/004/005/006/008/009/010 to SOW-0016/PKG-015.
- SCOPE_LEDGER.csv (Gate 7 snapshot), row SOW-0016.
- DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md (site basis sections; electrical sections including primary feeders and MV/LV systems).
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, `_SEMANTIC.md` in this deliverable folder.
- Upstream basis deliverables (peer rows): DEL-015-01 (SOW), DEL-015-02 (Package Datasheet), DEL-015-03 (Construction Work Package).
- Acceptance target deliverables (peer rows): DEL-015-04 (Vendor Engineered Equipment Package), DEL-015-05 (Vendor Document Turnover Package).
- Workbook Packages row 17 (cited by registers; not locally sliced).
