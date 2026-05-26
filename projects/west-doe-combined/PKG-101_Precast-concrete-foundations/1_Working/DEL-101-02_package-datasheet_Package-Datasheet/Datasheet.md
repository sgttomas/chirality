# Datasheet — DEL-101-02 Package Datasheet (PKG-101 Precast concrete foundations)

> Descriptive, source-grounded technical handoff data for the PKG-101 precast concrete foundations package.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-101-02_package-datasheet` | `_CONTEXT.md` Identity |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` Identity |
| Parent Package | `PKG-101` Precast concrete foundations | `_CONTEXT.md` Identity; PACKAGE_REGISTER.csv row PKG-101 |
| Workbook Row | 102 | PACKAGE_REGISTER.csv (WorkbookRow=102); `_CONTEXT.md` Source Reference |
| CoA Tracking Number | 26020-01-36-001 | PACKAGE_REGISTER.csv row PKG-101 |
| WBS | 01 | PACKAGE_REGISTER.csv row PKG-101 |
| Discipline | Structural | PACKAGE_REGISTER.csv; `_CONTEXT.md` |
| Type | EPC Package Datasheet | `_CONTEXT.md`; DELIVERABLE_REGISTER.csv |
| Responsible Party | EPC Integrator | DELIVERABLE_REGISTER.csv; `_CONTEXT.md` |
| Responsibility Model | EPC Integrator or discipline subcontractor responsibility is source-dependent; no separate vendor-package ownership model is inferred from current sources | PACKAGE_REGISTER.csv ResponsibilityModel field, row PKG-101 |
| Package Role (delivery package?) | FALSE (PackageRole flag = FALSE in package register) | PACKAGE_REGISTER.csv row PKG-101 |
| Supports Objectives | OBJ-001; OBJ-008 | DELIVERABLE_REGISTER.csv; PACKAGE_REGISTER.csv |
| Covers Scope Items | SOW-0257 | DELIVERABLE_REGISTER.csv |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package scope summary | Workbook-defined Structural package for "Precast concrete foundations" under WBS 01 with recorded physical interfaces | PACKAGE_REGISTER.csv ScopeDescription, row PKG-101 |
| Inclusion criteria | Workbook row 102; discipline Structural; WBS 01; applicable interface types: Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports | PACKAGE_REGISTER.csv InclusionCriteria, row PKG-101 |
| Exclusions | TBD — no package-specific exclusions stated in source materials | PACKAGE_REGISTER.csv Exclusions, row PKG-101 |
| Foundation system basis | Driven steel piles are the default support basis for buildings, equipment, towers, tanks, modules, pipe racks, and similar structures unless a more specific foundation basis is listed or detailed engineering confirms otherwise | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` § "Piles and Foundations" (line 2740) |
| Precast use — transformers | Generally supported on precast concrete bearing foundations | DBM `4-25_Deepcut_DBM.md` § "Piles and Foundations" table (line 2745) |
| Precast use — compressors | Precast concrete block supported on driven steel piles, subject to dynamic analysis; dynamic analysis results are TBD | DBM `4-25_Deepcut_DBM.md` § "Piles and Foundations" table (line 2746) |
| Alternate compressor concept | Verification by Propak of whether steel skid can be welded directly to piles instead of using concrete; considered unlikely for this compressor size | DBM `4-25_Deepcut_DBM.md` § "Piles and Foundations" (line 2747) |
| Compressor skid/foundation oil-leak consideration | Foundation/skid design shall consider containment and management of oil leaks from on-skid equipment | DBM `4-25_Deepcut_DBM.md` § "Piles and Foundations" (line 2748) |
| Concrete material/construction/testing standard | CSA A23.1 / A23.2 | DBM `4-25_Deepcut_DBM.md` § "Governing Civil and Structural Basis" (line 2677) |
| Concrete design standard | CAN/CSA A23.3 Design of Concrete Structures | DBM `4-25_Deepcut_DBM.md` § "Governing Civil and Structural Basis" (line 2674) |
| Foundation engineering reference | Canadian Foundation Engineering Manual | DBM `4-25_Deepcut_DBM.md` § "Governing Civil and Structural Basis" (line 2675) |
| Building code | National Building Code of Canada | DBM `4-25_Deepcut_DBM.md` § "Governing Civil and Structural Basis" (line 2672) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Bearing capacity | TBD pending geotechnical assessment | DBM `4-25_Deepcut_DBM.md` § "Geotechnical and Topographical Assumptions" (line 2691) |
| LPILE load-deflection curves | TBD pending geotechnical report | DBM line 2692 |
| Dynamic design criteria (for compressor foundations) | TBD pending geotechnical report and compressor dynamic analysis | DBM lines 2693, 2838 |
| Top-of-pile-cap elevation interactions with pad grading | Pad slope may be reduced from 1.5% to 1.0% where required to maintain reasonable top-of-pile-cap elevations | DBM § "Site Grading" (line 2710) |
| Spill containment / surface control around equipment | Surface-control features shall be considered around selected equipment to prevent on-site releases discharging outside the facility boundary | DBM § "Site Grading and Surface Water Management" (line 2702) |
| Site/seismic/snow/wind loading basis | Per National Building Code of Canada | DBM lines 2672, 2753 |

## Construction

| Item | Value | Source |
|---|---|---|
| Concrete construction and testing | Per CSA A23.1 / A23.2 | DBM line 2677 |
| Pile basis (where used as the carrying element under precast block) | Driven steel piles; final pile design parameters TBD pending geotechnical report | DBM lines 2740, 2749 |
| Compressor block dynamic verification | Required (subject to dynamic analysis); results TBD | DBM lines 2746, 2838, 2852 |
| Steel material grades (for adjacent structural steel) | CSA G40.20/G40.21 350W for W-flange and HSS; 300W for channels, plates, and angles | DBM line 2676 |

## Interfaces (carried as evidence per `_CONTEXT.md` Notes)

| InterfaceID | Interface Type | Applicability | Source |
|---|---|---|---|
| IFC-26343B703C | Grading / Site Drainage / Spill Containment | YES | INTERFACE_REGISTER.csv row IFC-26343B703C |
| IFC-BED3DE4194 | Structural / Foundations / Supports | YES | INTERFACE_REGISTER.csv row IFC-BED3DE4194 |

## Anticipated Artifacts (carried as datasheet contents)

| ArtifactID | Name | Type | Source |
|---|---|---|---|
| ART-7208F665C3 | Package technical datasheet | EPC Package Datasheet | ARTIFACT_REGISTER.csv |
| ART-080F36F89C | Vendor engineering handoff basis | Vendor Handoff Evidence | ARTIFACT_REGISTER.csv |
| ART-6679E64F6F | Package interface requirements matrix | EPC Interface Requirements Evidence | ARTIFACT_REGISTER.csv |
| ART-B722B4EE97 | Interface fact — Grading / Site Drainage / Spill Containment | Interface Fact Evidence (→ IFC-26343B703C) | ARTIFACT_REGISTER.csv |
| ART-1D7D43BEDB | Interface fact — Structural / Foundations / Supports | Interface Fact Evidence (→ IFC-BED3DE4194) | ARTIFACT_REGISTER.csv |

## Open / TBD Items

- Geotechnical bearing capacity, LPILE curves, dynamic criteria — TBD pending geotechnical report (DBM § "Geotechnical and Topographical Assumptions").
- Compressor foundation dynamic analysis — TBD (DBM line 2852).
- Direct steel skid-to-pile welding alternative — TBD; considered unlikely for compressor size (DBM line 2853).
- Package-specific exclusions — TBD; no exclusions stated in source materials (PACKAGE_REGISTER.csv).
- Workbook Packages row 102 cell-level details (beyond fields carried into the register) — `location TBD`: not directly read from `_Sources/26020-Packages_Interfaces_4_export.xlsx` in this run.
- `26020-Package_Requirements.docx` for PKG-101 — no matched DocxPackageHeading recorded (PACKAGE_REGISTER.csv `DocxPackageMatched=FALSE`); package-specific docx slice not located.

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
- DELIVERABLE_REGISTER.csv (GATE-07 snapshot)
- PACKAGE_REGISTER.csv (GATE-07 snapshot), row `PKG-101`
- INTERFACE_REGISTER.csv (GATE-07 snapshot), rows IFC-26343B703C, IFC-BED3DE4194
- ARTIFACT_REGISTER.csv (GATE-07 snapshot)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` § Civil Scope, Governing Civil and Structural Basis, Geotechnical and Topographical Assumptions, Site Grading and Surface Water Management, Piles and Foundations, External Dependencies, Assumptions/TBDs
- Workbook Packages row 102 (`_Sources/26020-Packages_Interfaces_4_export.xlsx`) — referenced; cell-level slice not read this run (`location TBD`)
- `_Sources/26020-Package_Requirements.docx` — referenced; no PKG-101 heading match (PACKAGE_REGISTER.csv DocxPackageMatched=FALSE)
