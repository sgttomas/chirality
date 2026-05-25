# Datasheet — DEL-019-04 Vendor Engineered Equipment Package

Production unit datasheet for the Package Vendor's engineered MV VFD equipment package supplied to PKG-019.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-019-04_vendor-engineered-equipment-package` |
| Name | Vendor Engineered Equipment Package |
| ParentPackageID | `PKG-019` |
| PackageName | MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD |
| ParentWorkbookID | 19 |
| Workbook Source | Workbook Packages row 21; `26020-02-30-009` |
| Discipline | Electrical |
| Type | Vendor Package Production Unit |
| ResponsibleParty | Package Vendor (engineering/design/equipment) with EPC Integrator integration review |
| Covers Scope Items | `SOW-0020` |
| Supports Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` |

Source: Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-019-04_vendor-engineered-equipment-package`; Gate 7 `PACKAGE_REGISTER.csv` row `PKG-019`.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package class | Vendor-engineered packaged equipment (Electrical, MV VFD) | Gate 7 `PACKAGE_REGISTER.csv` `PKG-019` |
| Vendor ownership scope | Package engineering, package design, vendor documentation, physical equipment package | Gate 7 `PACKAGE_REGISTER.csv` `PKG-019` (ResponsibilityNarrative) |
| EPC ownership scope | Facility integration, interfaces, tie-ins, constructability, procurement/construction coordination | Gate 7 `PACKAGE_REGISTER.csv` `PKG-019` (ResponsibilityNarrative) |
| Equipment driven (application) | Starting VFDs for inlet compressor motors `KM-2150`, `KM-2250` | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §324, §326, §756 |
| Driven motor electrical basis (per DBM) | 4,000 V, 3-phase, 60 Hz, 5,200 hp (3,878 kW), continuous inverter-duty, ~891 rpm, NEMA MG1, Class F insulation/Class B rise | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §324, §523, §533 |
| Package title rating (per workbook) | 5000 HP, 4160 V, 3-phase, 60 Hz | Workbook Packages row 21 (title) |
| Authority governing starting basis | SCA-001 VE #34 (starting VFDs required; soft starts not in current basis) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §326, §756 |
| Upstream supply (line side) | 4160V MCC serving large 4000V motors | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §752, §754 |

Note: the workbook title and the DBM motor basis disagree on nominal motor voltage and horsepower (4160 V / 5000 HP vs 4000 V / 5,200 HP). See `Guidance.md` Conflict Table.

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Starting VFD for medium-voltage induction-motor-driven inlet compressors | DBM §326, §756 |
| Duty | Continuous inverter-duty motor application; starting-VFD usage per SCA-001 VE #34 | DBM §324, §326 |
| Ambient / installation environment | TBD (not stated in accessible sources at deliverable scope) | location TBD |
| Harmonics / reactive mitigation | To be determined by detailed electrical studies; capacitor banks removed from synchronous bus on `MCC-8200` where VFDs are present (SCA-001 VE #37) | DBM §756 |
| Communications | EtherNet to plant PLC central control panel via 4160V MCC | DBM §754 |

## Construction

| Element | Value | Source |
|---|---|---|
| Physical scope | Vendor-engineered MV VFD equipment package as a discrete production unit (cabinets, power electronics, control, and ancillaries as specified by vendor design) | Gate 7 deliverable narrative |
| Engineering scope | Package engineering and design developed by Package Vendor from the EPC Scope of Work (`DEL-019-01`) and Package Datasheet (`DEL-019-02`) | Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-019-04` |
| Fabrication / supply | Vendor-supplied physical equipment package | Gate 7 deliverable narrative |
| Documentation set | Vendor package design basis and datasheet set (handed off to `DEL-019-05`) | Gate 7 deliverable narrative; anticipated artifacts |
| Interface types in scope (package level) | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports | Gate 7 `PACKAGE_REGISTER.csv` `PKG-019` (InterfaceTypes) |
| Detailed electrical sizing | VFD sizing is an electrical detailed-design item; final vendor-stated ratings | DBM §326; ASSUMPTION carried forward |

## References

- Gate 7 snapshot root: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- `DELIVERABLE_REGISTER.csv` row `DEL-019-04_vendor-engineered-equipment-package`
- `PACKAGE_REGISTER.csv` row `PKG-019`
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (sections 324, 326, 523, 533, 744, 752, 754, 756)
- Sibling EPC anchor deliverables: `DEL-019-01_scope-of-work`, `DEL-019-02_package-datasheet`
- Sibling vendor-side deliverable: `DEL-019-05_vendor-document-turnover-package`
- Sibling EPC acceptance deliverable: `DEL-019-06_epc-vendor-package-review-and-acceptance`
