# Datasheet — DEL-102-01 Scope of Work (PKG-102 Monolithic concrete foundations)

> Descriptive datasheet for the EPC Integrator Scope of Work covering PKG-102 "Monolithic concrete foundations" (Structural, WBS 01).
> Source-grounded against the GATE-07 Final Published PROJECT_DECOMP snapshot and DBM-Deepcut SEC-11.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-102-01_scope-of-work | `_CONTEXT.md` Identity table |
| Deliverable Name | Scope of Work | `_CONTEXT.md` Identity table |
| Parent Package ID | PKG-102 | `_CONTEXT.md` Identity table |
| Parent Workbook ID | 102 (Workbook row 103) | `PACKAGE_REGISTER.csv` PKG-102 row |
| Package Name | Monolithic concrete foundations | `PACKAGE_REGISTER.csv` PKG-102 row |
| Discipline | Structural | `PACKAGE_REGISTER.csv` PKG-102 row |
| WBS | 01 | `PACKAGE_REGISTER.csv` PKG-102 row |
| Deliverable Type | EPC Scope of Work | `_CONTEXT.md` Identity table |
| Responsible Party | EPC Integrator | `_CONTEXT.md` Identity table; `DELIVERABLE_REGISTER.csv` PKG-102 row |
| Covers Scope Items | SOW-0258 | `_CONTEXT.md`; `SCOPE_LEDGER.csv` SOW-0258 |
| Supports Objectives | OBJ-001; OBJ-008 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` PKG-102 row (ASSUMPTION: package-grouping heuristic per OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Provide monolithic cast-in-place concrete foundations for equipment, structures, modules, and ancillary items in WBS 01 of the West Doe Deepcut expansion | DBM-Deepcut SEC-11 "Piles and Foundations"; `PACKAGE_REGISTER.csv` PKG-102 description |
| Governing concrete design code | CAN/CSA A23.3 Design of Concrete Structures (latest edition) | DBM-Deepcut SEC-11 "Governing Civil and Structural Basis" |
| Governing materials/construction/testing standard | CSA A23.1/A23.2 | DBM-Deepcut SEC-11 "Governing Civil and Structural Basis" |
| Governing foundation engineering reference | Canadian Foundation Engineering Manual | DBM-Deepcut SEC-11 "Governing Civil and Structural Basis" |
| Governing building code (for loading) | National Building Code of Canada (latest edition) | DBM-Deepcut SEC-11 "Governing Civil and Structural Basis"; "Buildings and Miscellaneous Facilities" |
| Default site foundation basis | Driven steel piles for buildings, equipment, towers, tanks, modules, and pipe racks unless a specific concrete-foundation basis is established | DBM-Deepcut SEC-11 "Piles and Foundations" (provides context; identifies where monolithic concrete is or is not the default) |
| Monolithic-concrete application instances explicitly identified in source | None explicitly enumerated as "monolithic" in DBM-Deepcut SEC-11; precast concrete is identified for transformers, and precast concrete blocks (on driven piles) for compressors | DBM-Deepcut SEC-11 "Piles and Foundations" table |
| Tagged equipment and package identity list | TBD — workbook row 103 (binary `.xlsx`) is not parsed in this run; deliverable narrative requires the Workbook Packages row 103 tagged equipment slice | `_CONTEXT.md` Anticipated Artifacts; ASSUMPTION pending workbook extraction |
| Applicable interface types | Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv` PKG-102 row; `INTERFACE_REGISTER.csv` IFC-1EDEDC0453, IFC-8283744B5B |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Geotechnical bearing capacity | TBD pending site geotechnical report | DBM-Deepcut SEC-11 "Geotechnical and Topographical Assumptions" |
| LPILE load-deflection curves | TBD pending site geotechnical report | DBM-Deepcut SEC-11 "Geotechnical and Topographical Assumptions" |
| Dynamic design criteria | TBD pending site geotechnical report | DBM-Deepcut SEC-11 "Geotechnical and Topographical Assumptions" |
| Compressor foundation dynamic analysis | TBD | DBM-Deepcut SEC-11 "Piles and Foundations"; "Assumptions, TBDs, and Design Development Requirements" |
| Site grading and drainage interface | Pad slopes from pipe racks at 1.5% to each side (reducible to 1.0% to maintain reasonable top-of-pile-cap elevations) | DBM-Deepcut SEC-11 "Site Grading and Surface Water Management" |
| Spill containment interface | NGL storage and compressor skid containment provisions required at the grading/foundation interface | DBM-Deepcut SEC-11 "Site Grading and Surface Water Management"; "Piles and Foundations" |
| Topographical survey input | Existing grade surface file required; format/content TBD | DBM-Deepcut SEC-11 "Geotechnical and Topographical Assumptions" |
| Plot plan dependency | External plot plan required for layout and retention pond coordination | DBM-Deepcut SEC-11 "External Dependencies" |

## Construction

| Item | Description | Source |
|---|---|---|
| Cast-in-place concrete materials | CSA A23.1/A23.2 governs materials, construction, and testing | DBM-Deepcut SEC-11 "Governing Civil and Structural Basis" |
| Reinforced concrete design | Per CAN/CSA A23.3 | DBM-Deepcut SEC-11 "Governing Civil and Structural Basis" |
| Concrete-on-pile arrangements | Where used (e.g., precast compressor block on driven piles), foundation/skid design shall consider containment and management of on-skid equipment oil leaks | DBM-Deepcut SEC-11 "Piles and Foundations" |
| Construction interface to grading | Top-of-pile-cap (or top-of-foundation) elevations to be coordinated with facility pad grading (1.0%–1.5% slope basis) | DBM-Deepcut SEC-11 "Site Grading and Surface Water Management"; "Piles and Foundations" |
| Tagged equipment and module assignments | TBD pending workbook row 103 extraction; module/equipment-to-foundation assignment list TBD | ASSUMPTION; source slice not extracted in this run |

## References

- `_REFERENCES.md` (deliverable-local reference index)
- `_CONTEXT.md` (deliverable-local identity and scope)
- GATE-07 Final Published PROJECT_DECOMP snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `PACKAGE_REGISTER.csv` (PKG-102 row)
  - `DELIVERABLE_REGISTER.csv` (DEL-102-01_scope-of-work row; sibling PKG-102 deliverable rows)
  - `SCOPE_LEDGER.csv` (SOW-0258)
  - `INTERFACE_REGISTER.csv` (IFC-1EDEDC0453; IFC-8283744B5B)
  - `OBJECTIVE_REGISTER.csv` (OBJ-001; OBJ-008)
- DBM-Deepcut: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-11 (Civil, Buildings, and Miscellaneous Facilities Basis)
- Workbook (not parsed in this run): `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx`; `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx` (row 103)
