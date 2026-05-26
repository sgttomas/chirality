# Datasheet — DEL-042-04 Vendor Engineered Equipment Package

Production unit datasheet for the Package Vendor's engineered Control Room Building equipment package supplied to PKG-042.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-042-04_vendor-engineered-equipment-package` |
| Name | Vendor Engineered Equipment Package |
| ParentPackageID | `PKG-042` |
| PackageName | Control Room Building |
| ParentWorkbookID | 42 |
| Workbook Source | Workbook Packages row 44; `26020-03-39-010` |
| Discipline | Electrical |
| WBS | 03 |
| Type | Vendor Package Production Unit |
| ResponsibleParty | Package Vendor (engineering/design/equipment) with EPC Integrator integration review |
| Covers Scope Items | `SOW-0043` |
| Supports Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` |

Source: Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-042-04_vendor-engineered-equipment-package`; Gate 7 `PACKAGE_REGISTER.csv` row `PKG-042`; Gate 7 `SCOPE_LEDGER.csv` row `SOW-0043`.

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package class | Vendor-engineered building / packaged facility (Electrical discipline, WBS 03) | Gate 7 `PACKAGE_REGISTER.csv` `PKG-042` |
| Vendor ownership scope | Package engineering, package design, vendor documentation, physical equipment package | Gate 7 `PACKAGE_REGISTER.csv` `PKG-042` (ResponsibilityModel) |
| EPC ownership scope | Facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination | Gate 7 `PACKAGE_REGISTER.csv` `PKG-042` (ResponsibilityModel) |
| Building function (per DBM) | Operator facility hosting the operations control room environment; houses operator workstations, engineering workstations, primary servers, and core network switches | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §658, §704; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §3119, §3141 |
| Primary server hosting | Primary control-system server host located in the control room (secondary host in low-voltage MCC room) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §796 |
| Plot-plan position (anchor) | Coordinated with electrical buildings and operator facilities on plot plan; spacing per DBM separation criteria | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §671; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §254, §298 |
| Separation criteria (per DBM) | ≥ 15.24 m (50 ft) from pressurized bullets per API 2510; ≥ 25 m (82 ft) from fired heaters per OGAOM §9.6.15 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §254, §298 |
| Foundations basis | Foundations designed for final geotechnical report, equipment loads, snow/wind/seismic, frost protection, vibration, settlement, maintenance access | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §700 |
| Building-services scope (per DBM) | Coordinated with area classification, ventilation, heating, emergency egress, fire and gas detection, ESD pushbutton placement, RIO panel locations, power distribution, maintenance access | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §704 |
| Wiring method (non-process building interior) | EMT permitted in non-process locations such as MCC buildings, control rooms, offices, warehouses; min conduit 21 mm (3/4 in); CEC compliant | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §3025 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service environment | Controlled-environment operator facility supporting continuous facility monitoring and control | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §3119 |
| Area classification (interior) | Non-process / non-hazardous (general-purpose) — ASSUMPTION based on DBM allowance for EMT in control rooms (§3025); detailed area-classification drawing not in accessible source slices | ASSUMPTION; location TBD |
| Ambient / outdoor design conditions | Snow/wind/seismic design criteria per project geotechnical and structural basis; specific values TBD at deliverable scope | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §700; values `location TBD` |
| Fire & gas detection | Fire and gas detection coordination required (building-level); detection types/coverage `TBD` at deliverable scope | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §704 |
| Building HVAC | Building HVAC / heating and ventilation coordination required; equipment selection `TBD` | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §704 (Building HVAC / Services interface) |
| Communications | Core network switches and BPCS/operator network infrastructure hosted within the control room; integration to plant network `TBD` at vendor-package boundary | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §3141 |
| Pre-assembly mode | Building permitted to be fabricated and erected in assembly shop before shipment to site (DBM §3025 references this case for non-process buildings) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §3025 |

## Construction

| Element | Value | Source |
|---|---|---|
| Physical scope | Vendor-engineered Control Room Building as a discrete production unit (structure, envelope, interior fit-out, HVAC, building electrical, fire & gas, communications/network infrastructure, operator-room furnishings as defined by vendor design) | Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-042-04`; Gate 7 `PACKAGE_REGISTER.csv` `PKG-042` ScopeDescription |
| Engineering scope | Package engineering and design developed by Package Vendor from the EPC Scope of Work (`DEL-042-01`) and Package Datasheet (`DEL-042-02`) | Gate 7 `DELIVERABLE_REGISTER.csv` row `DEL-042-04` |
| Fabrication / supply | Vendor-supplied physical equipment package; pre-assembly/erection in vendor shop permitted | Gate 7 deliverable narrative; DBM §3025 |
| Documentation set | Vendor package design basis and datasheet set (handed off to `DEL-042-05`) | Gate 7 deliverable narrative; anticipated artifacts |
| Interface types in scope (package level) | Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | Gate 7 `PACKAGE_REGISTER.csv` `PKG-042` (InterfaceTypes) |
| Interior wiring conventions | EMT permitted in non-process building interior; rigid conduit in shop-fabricated lighting/exhaust/receptacle/switch systems; conduit sealing at area-classification boundaries; CEC compliant | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §3025 |
| Foundations / siting | Equipment-specific foundation and anchorage checks required (DBM §700); plot-plan separation per DBM separation criteria | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §700; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §254, §298 |
| Pre-existing-building option | DBM 4-25 references "install on site or modify if already existing" for office/control-room building; applicability to PKG-042 is `TBD` (PKG-042 is 03-25 / WBS 03) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` §2759, §2662; ASSUMPTION cross-DBM, applicability TBD |

## References

- Gate 7 snapshot root: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- `DELIVERABLE_REGISTER.csv` row `DEL-042-04_vendor-engineered-equipment-package`
- `PACKAGE_REGISTER.csv` row `PKG-042`
- `SCOPE_LEDGER.csv` row `SOW-0043`
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (sections 75, 658, 671, 700, 704, 796)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (sections 254, 298, 2662, 2759, 3025, 3119, 3121, 3141)
- Sibling EPC anchor deliverables: `DEL-042-01_scope-of-work`, `DEL-042-02_package-datasheet`
- Sibling construction deliverable: `DEL-042-03_construction-work-package`
- Sibling vendor-side deliverable: `DEL-042-05_vendor-document-turnover-package`
- Sibling EPC acceptance deliverable: `DEL-042-06_epc-vendor-package-review-and-acceptance`
