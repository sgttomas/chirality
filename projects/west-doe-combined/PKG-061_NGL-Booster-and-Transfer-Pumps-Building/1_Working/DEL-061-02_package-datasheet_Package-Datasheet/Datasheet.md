# Datasheet — DEL-061-02 Package Datasheet (PKG-061 NGL Booster and Transfer Pumps Building)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-061-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| ParentPackageID | `PKG-061` | `_CONTEXT.md` |
| Package Name | NGL Booster and Transfer Pumps Building | `_CONTEXT.md`; PACKAGE_REGISTER.csv row PKG-061 |
| Workbook Row | 75 | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Discipline | Mechanical | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator (integration); Package Vendor (package engineering/design/documentation/physical equipment) | PACKAGE_REGISTER.csv "ResponsibilityDescription" |
| Authoritative Word Source | `26020-Package_Requirements.docx`, package heading `26020-01-PT-18-004 - LPG Booster` (heading 17 in TOC) | `_REFERENCES.md`; `_Sources/26020-Package_Requirements.docx` |
| Authoritative DBM Source | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` row 58 | DBM table row 58 |
| Decomposition Snapshot | GATE-07_Final_Published_2026-05-24 | `_CONTEXT.md`, `_REFERENCES.md` |

## Attributes (Equipment)

| Tag | Service | Type | Quantity | Key Attributes | Source |
|---|---|---|---|---|---|
| P-9570-1 | LPG booster pump (LPG storage → LACT) | Vertical multistage can-type centrifugal, API 610 seal plan 13/52 | 1 (one of two parallel) | 575 V / 3 phase / 60 Hz motor | docx §26020-01-PT-18-004 (heading 17, "Major Included Equipment"); DBM row 58 ("API 610, multi-stage can") |
| P-9580-1 | LPG booster pump (LPG storage → LACT) | Vertical multistage can-type centrifugal, API 610 seal plan 13/52 | 1 (one of two parallel) | 575 V / 3 phase / 60 Hz motor | docx §26020-01-PT-18-004; DBM row 58 |

## Conditions (Process / Design)

| Parameter | Value | Source |
|---|---|---|
| Service fluid | LPG (transfer from LPG storage to LACT unit) | docx §26020-01-PT-18-004 "Basic Scope" |
| Arrangement | Two pumps in parallel; booster pressure where required | docx §26020-01-PT-18-004 "Basic Scope" |
| Flow per pump | 145 m³/h at 150% capacity sizing | docx §26020-01-PT-18-004 "Scope Notes / Open Items" |
| Design differential | 25 psid / 172 kPad | docx §26020-01-PT-18-004 "Scope Notes / Open Items" |
| TDH | TBD (`location TBD` — Scope Notes state "TBD TDH") | docx §26020-01-PT-18-004 |
| Operating conditions (T/P ranges) | TBD | not specified in accessible source |
| Design conditions (T/P) | TBD | not specified in accessible source |
| Site/area classification | TBD | not specified in accessible source |

## Construction

| Item | Value | Source |
|---|---|---|
| Pump type | Vertical multistage can-type centrifugal | docx §26020-01-PT-18-004 "Major Included Equipment"; DBM row 58 |
| Pump standard | API 610 | docx §26020-01-PT-18-004; DBM row 58 |
| Seal | API 610 seal plan 13/52 | docx §26020-01-PT-18-004 |
| Motor | 575 V / 3 phase / 60 Hz | docx §26020-01-PT-18-004 |
| Skid | Structural skid | docx §26020-01-PT-18-004 |
| Package piping, instrumentation, electrical | Included | docx §26020-01-PT-18-004 |
| Enclosure / HVAC | HVAC/enclosure provided as part of package; self-framing building (PROPOSAL: per package name "Building") | docx §26020-01-PT-18-004 (HVAC/enclosure listed); package name `_CONTEXT.md` |
| Code compliance | CRN / TSBC as applicable | docx §26020-01-PT-18-004 |
| Materials of construction | TBD | not specified in accessible source |

## Interfaces (Physical, package-level)

All physical interfaces below are listed in the package source as **TBC** (to-be-confirmed) at package-heading 17. Applicability types are taken from PACKAGE_REGISTER.csv "ApplicableInterfaceTypes" for PKG-061.

| Interface Type | Applicability per docx | Applicable per Register | Source |
|---|---|---|---|
| Process Piping | TBC | Yes | docx §26020-01-PT-18-004; PACKAGE_REGISTER.csv |
| Utility Piping | TBC | Yes | docx; register |
| Relief / Flare / Vent | TBC | Yes | docx; register |
| Drain / Containment | TBC | Yes | docx; register |
| Electrical Power | TBC | Yes | docx; register |
| Area / Exterior Lighting | TBC ("No direct row found in 26020-Packages_Interfaces.3.xlsx; confirm applicability") | Yes | docx; register |
| EHT | TBC | Yes | docx; register |
| Grounding / Bonding | TBC | Yes | docx; register |
| Cathodic Protection | TBC | Not listed in register applicable types | docx |
| I&C / Control Cabling | TBC | Yes | docx; register |
| Communications / Network | TBC | Not listed in register | docx |
| Building HVAC / Services | TBC | Yes | docx; register |
| Fire & Gas / Safety Systems | TBC | Yes | docx; register |
| Maintenance Access | TBC | Yes | docx; register |
| Grading / Site Drainage / Spill Containment | TBC | Not listed in register | docx |
| Structural / Foundations / Supports | TBC | Yes | docx; register |
| Product Loading | TBC | Not listed in register | docx |
| Pipeline / Pigging | TBC | Not listed in register | docx |

ASSUMPTION: Detailed interface row-level data resides in `26020-Packages_Interfaces.3.xlsx` / `26020-Packages_Interfaces_4_export.xlsx`; the slice copied into the Word source carries all rows as TBC. Detailed interface reconciliation deferred to package-interface deliverable.

## Vendor Engineering Deliverables (anticipated, from package source)

Core vendor documents: PRQ-009 (Vendor Document Index); DOC-008 (Vendor Document Control Procedure); QLT-006 (Supplier Quality Plan); QLT-003 (Inspection and Test Plan); QLT-013 (MTR/Certificates); QLT-020 (Inspection Release Certificate); QLT-021 (Manufacturing Record Book / Vendor Data Book); PRQ-013 (Logistics / Shipping Plan); PRQ-015 (SPIR); PRQ-016 (Vendor Data Book / Final Supplier Documentation).

Core package engineering: MEC-001 (Mechanical Design Basis); MEC-002 (Mechanical Equipment List); MEC-003 (Mechanical Equipment Data Sheets); MEC-006 (Package Equipment Specifications); MEC-014 (Mechanical Calculation Package); MEC-016 (Equipment General Arrangement Drawing); MEC-017 (Equipment Installation / Setting Drawings); MEC-018 (Lifting / Handling Study for Major Equipment); MEC-021 (Equipment FAT / Performance Test Procedure); MEC-022 (Equipment FAT / Performance Test Report); MEC-023 (Vendor Data Book / Mechanical Final Documentation); MEC-024 (Mechanical Spares / Special Tools Requirements); MEC-025 (Mechanical Equipment IOM Manual).

Rotating equipment / pumps: MEC-004 (Rotating Equipment Specifications); MEC-007 (Pump Data Sheets); MEC-019 (Mechanical Seal / Lube Oil Specification); PRO-013 (Pump Hydraulic / NPSH Calculations); ELE-011 (Motor Starting Study).

Source: `26020-Package_Requirements.docx`, package heading `26020-01-PT-18-004 - LPG Booster`, "Vendor Engineering Deliverables" table.

## Exclusions / By Others

- DCS integration — by others. Source: docx §26020-01-PT-18-004 "Scope Notes / Open Items".
- Foundations — by others. Source: docx §26020-01-PT-18-004.
- Electrical supply to MCC — by others. Source: docx §26020-01-PT-18-004.

## Naming Note (CONFLICT entry)

CONFLICT-01: Package folder/decomposition name is "NGL Booster and Transfer Pumps Building" (PKG-061; DBM row 58 row title); the authoritative Word source for this package is titled `26020-01-PT-18-004 - LPG Booster` and its Basic Scope describes LPG (not NGL) booster service to the LACT unit. Both the PACKAGE_REGISTER.csv and the DBM row 58 attach the LPG-booster pumps (P-9570-1/P-9580-1) to this package. Service fluid is LPG per all accessible sources; the building/package name carries "NGL" likely as a legacy or building-grouping label. See Conflict Table in `Guidance.md`.

## References

- `_Sources/26020-Package_Requirements.docx`, heading `26020-01-PT-18-004 - LPG Booster` (TOC heading 17). Extracted text lines 6000-6162.
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` row 58.
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` row PKG-061.
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row DEL-061-02.
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`.
