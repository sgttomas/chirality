# Datasheet — DEL-044-02 Package Datasheet (PKG-044 Instrumentation)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-044-02_package-datasheet | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| ParentPackageID | PKG-044 | `_CONTEXT.md` |
| Package Name | Instrumentation (outside of Mechanical Packages only) | PACKAGE_REGISTER.csv (PKG-044) |
| Discipline | Instrumentation | PACKAGE_REGISTER.csv (PKG-044) |
| WBS | 02 | PACKAGE_REGISTER.csv (PKG-044) |
| CoA Tracking Number | 26020-01-32-002 | PACKAGE_REGISTER.csv (PKG-044) |
| Workbook Source | Workbook Packages row 46 | PACKAGE_REGISTER.csv; `_REFERENCES.md` |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Covers Scope Item | SOW-0045 | DELIVERABLE_REGISTER.csv (DEL-044-02) |
| Supports Objectives | OBJ-002, OBJ-003, OBJ-005, OBJ-006, OBJ-007, OBJ-010 | DELIVERABLE_REGISTER.csv (DEL-044-02) — ASSUMPTION via PACKAGE_HEURISTIC |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Role | Authoritative companion register row | PACKAGE_REGISTER.csv |
| Responsibility Model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from current sources. | PACKAGE_REGISTER.csv |
| Inclusion Criteria | Workbook row 46; discipline Instrumentation; WBS 02. Applicable interface types: Process Piping; Utility Piping; Electrical Power; I&C / Control Cabling; Communications / Network. | PACKAGE_REGISTER.csv |
| Exclusions | TBD; no package-specific exclusions stated in source materials. | PACKAGE_REGISTER.csv |
| Interface Review Note | Field supports, power, and comms not marked unless confirmed by package scope. Gate 6 disposition: instrumentation field supports, power, and communications are included in each package scope as appropriate under the plug-n-play package philosophy. | PACKAGE_REGISTER.csv; INTERFACE_REGISTER.csv |
| Equipment Tag List | TBD — not enumerated in locally accessible sources | (location TBD; workbook row 46 binary) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site ambient minimum design temperature | -40 deg C minimum ambient governs exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe process or vendor condition applies. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, line 145 |
| Area classification, ventilation, heating, F&G detection | Buildings/shelters shall be coordinated with area classification, ventilation, heating, emergency egress, fire and gas detection, ESD pushbutton placement, RIO panel locations, power distribution, and maintenance access. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, line 704 |
| Analyzer-quality air | Sulphur GC/detectors require analyzer-quality air with hydrocarbon content < 1 ppm and dew point < -40 deg C (cylinder supply where required). Final analyzer technology, placement, and tag list remain TBD. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, line 509 |
| Process / utility integration | Power and utilities are shared between 03-25 and 04-25; associated electrical, instrumentation, controls, and interface scope included where required for 03-25 operation. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, line 716 |

## Construction

| Item | Value | Source |
|---|---|---|
| Package construction model | Plug-n-play package philosophy: instrumentation field supports, power, and communications included in each package scope as appropriate. | INTERFACE_REGISTER.csv Gate 6 disposition note (PKG-044 interfaces) |
| Self-framing / shelter enclosures | Where required for instrumentation, package buildings or self-framing shelters with heating, HVAC, F&G detection, and drain/vent tie-ins shall be coordinated. | DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md, lines 260, 619, 704 |
| Field supports / cable tray / junction boxes | TBD — not enumerated for PKG-044 in accessible sources |
| Tag list / loop list / I/O list | TBD — workbook row 46 not directly readable in this run |

## Interfaces

Interface inventory derived from INTERFACE_REGISTER.csv (rows where `PackageID = PKG-044`):

| InterfaceID | Interface Type | Marked in Source | Source |
|---|---|---|---|
| IFC-A0182B4C75 | Process Piping | YES | INTERFACE_REGISTER.csv |
| IFC-9E42D79051 | Utility Piping | YES | INTERFACE_REGISTER.csv |
| IFC-0DD8B45540 | Electrical Power | YES | INTERFACE_REGISTER.csv |
| IFC-20C7248CDB | I&C / Control Cabling | YES | INTERFACE_REGISTER.csv |
| IFC-0664000480 | Communications / Network | YES | INTERFACE_REGISTER.csv |

Gate 6 disposition (all five rows): "instrumentation field supports, power, and communications are included in each package scope as appropriate under the plug-n-play package philosophy."

## References

- `_CONTEXT.md` — deliverable identity and scope.
- `_REFERENCES.md` — reference index.
- PACKAGE_REGISTER.csv — Gate 7 snapshot row for PKG-044.
- INTERFACE_REGISTER.csv — Gate 7 snapshot interface rows for PKG-044.
- DELIVERABLE_REGISTER.csv — Gate 7 snapshot row for DEL-044-02.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — companion DBM cited as PKG-044 source basis.
- `_Sources/26020-Package_Requirements.docx` — workbook row 46 (binary; location TBD for in-run read).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — package/interface workbook export (binary; location TBD for in-run read).
