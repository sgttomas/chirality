# Specification — DEL-102-02 Package Datasheet (PKG-102 Monolithic concrete foundations)

## Scope

**Covers.** This Package Datasheet captures the EPC Integrator technical handoff data required for third-party vendor or discipline-package engineering and design of PKG-102 "Monolithic concrete foundations." Content includes: package identification (datasheet evidence), governing codes and standards, geotechnical and loading inputs, concrete and reinforcement basis (where source-supported), foundation type basis, anchor/embedment basis, interface requirements matrix carried from workbook evidence, and source-supported equipment and design criteria.
Source: `_CONTEXT.md` §Scope; `DELIVERABLE_REGISTER.csv` row `DEL-102-02_package-datasheet`.

**Excludes.** Production of detailed foundation drawings, reinforcement schedules, concrete mix designs, formwork shop drawings, geotechnical interpretation, pile design, equipment skid design, electrical/grounding details, and discipline production-package authorship. These are addressed by DEL-102-04 (EPC/Structural Discipline Production Package), the geotechnical report, and discipline detailed-engineering deliverables.
Source: derived from `_CONTEXT.md` Anticipated Artifacts list and `DELIVERABLE_REGISTER.csv` rows for siblings DEL-102-01, DEL-102-03, DEL-102-04.

## Requirements

### R1 — Identification

| ID | Requirement | Source |
|---|---|---|
| R1.1 | The datasheet shall identify the package by ID (`PKG-102`), workbook ID (102), workbook row (103), discipline (Structural), and WBS (01). | `PACKAGE_REGISTER.csv` row PKG-102 |
| R1.2 | The datasheet shall record the deliverable ID `DEL-102-02_package-datasheet`, parent package, and responsible party (EPC Integrator, with the noted source-dependent caveat). | `_CONTEXT.md` Identity table; `PACKAGE_REGISTER.csv` row PKG-102 (`ResponsibleParty` note) |
| R1.3 | The datasheet shall list scope-item coverage (`SOW-0258`) and supported objectives (`OBJ-001`, `OBJ-008`; ASSUMPTION: package-grouping heuristic). | `_CONTEXT.md` "Covers Scope Items", "Supports Objectives"; `DELIVERABLE_REGISTER.csv` row |

### R2 — Governing Codes and Standards

| ID | Requirement | Source |
|---|---|---|
| R2.1 | Concrete foundation design shall comply with CAN/CSA A23.3 (Design of Concrete Structures), latest edition. | DBM-Deepcut §"Governing Civil and Structural Basis" |
| R2.2 | Concrete materials, construction, and testing shall comply with CSA A23.1/A23.2, latest edition. | DBM-Deepcut §"Governing Civil and Structural Basis" |
| R2.3 | Building loading (snow, rain, wind, seismic) shall comply with the National Building Code of Canada, project-site values, latest edition. | DBM-Deepcut §"Governing Civil and Structural Basis"; §"Buildings and Miscellaneous Facilities" |
| R2.4 | Foundation engineering shall reference the Canadian Foundation Engineering Manual, latest edition. | DBM-Deepcut §"Governing Civil and Structural Basis" |
| R2.5 | Where embedded or attached steel components are required, they shall comply with CAN/CSA S16 and material standards CSA G40.20/G40.21 (350W W-flange/HSS; 300W channels, plates, angles). | DBM-Deepcut §"Governing Civil and Structural Basis" |

### R3 — Geotechnical and Site Inputs

| ID | Requirement | Source |
|---|---|---|
| R3.1 | Bearing capacity used for foundation sizing shall be taken from the project geotechnical assessment report. | DBM-Deepcut §"Geotechnical and Topographical Assumptions"; §"External Dependencies" — currently TBD |
| R3.2 | Lateral resistance and pile load-deflection parameters (LPILE) where applicable to combined pile/concrete-cap systems shall be taken from the geotechnical report. | DBM-Deepcut §"Geotechnical and Topographical Assumptions" — currently TBD |
| R3.3 | Dynamic design criteria for vibrating-equipment foundations shall be taken from the geotechnical report and discipline dynamic analysis. | DBM-Deepcut §"Piles and Foundations"; §"External Dependencies" — currently TBD |
| R3.4 | Foundation top-of-cap elevations shall be coordinated with facility pad grading (1.5% nominal; 1.0% allowance where required). | DBM-Deepcut §"Site Grading and Surface Water Management" |

### R4 — Foundation Type Basis

| ID | Requirement | Source |
|---|---|---|
| R4.1 | The project default support basis for buildings, equipment, towers, tanks, modules, pipe racks, and similar structures is driven steel piles unless a more specific basis applies; the PKG-102 "Monolithic concrete foundations" label is reconciled with the source-stated foundation bases below (see Guidance Conflict C-01). | DBM-Deepcut §"Piles and Foundations" |
| R4.2 | Transformer foundations shall be precast concrete bearing foundations. | DBM-Deepcut §"Piles and Foundations" table |
| R4.3 | Compressor foundations shall be precast concrete block supported on driven steel piles, subject to dynamic analysis (results TBD). | DBM-Deepcut §"Piles and Foundations" table |
| R4.4 | Compressor skid/foundation design shall consider containment and management of on-skid equipment oil leaks. | DBM-Deepcut §"Piles and Foundations" table |
| R4.5 | Concrete mix design (`f'c`, exposure class, durability), reinforcement grade and detailing, and anchor/embedment schedules are TBD; values shall be supplied by detailed engineering and incorporated by reference. | location TBD (not stated in available sources) |

### R5 — Interfaces

| ID | Requirement | Source |
|---|---|---|
| R5.1 | The datasheet shall carry the package's active workbook interface facts as evidence: `IFC-1EDEDC0453` (Grading / Site Drainage / Spill Containment) and `IFC-8283744B5B` (Structural / Foundations / Supports). | `INTERFACE_REGISTER.csv`; Workbook Packages row 103; `ARTIFACT_REGISTER.csv` rows ART-05281DC8CE, ART-F35AC96771 |
| R5.2 | The datasheet shall present a package interface requirements matrix that maps each active interface type to its receiving discipline and the data required for the handoff (ASSUMPTION where the workbook only carries an X-mark with no further attributes). | `ARTIFACT_REGISTER.csv` row ART-BA3D34EA23; `INTERFACE_REGISTER.csv` |

### R6 — External Dependencies

| ID | Requirement | Source |
|---|---|---|
| R6.1 | The datasheet shall list external inputs required to close TBD parameters: geotechnical assessment report, topographical survey/grade surface file, plot plan (incl. CIV-235633-5002-001), and compressor dynamic analysis. | DBM-Deepcut §"External Dependencies" |

## Standards

| Standard | Edition basis | Local accessibility |
|---|---|---|
| National Building Code of Canada | Latest | location TBD (not in local source set) |
| CAN/CSA A23.3 — Design of Concrete Structures | Latest | location TBD (not in local source set) |
| CSA A23.1/A23.2 — Concrete materials, construction, testing | Latest | location TBD (not in local source set) |
| Canadian Foundation Engineering Manual | Latest | location TBD (not in local source set) |
| CAN/CSA S16 — Design of Steel Structures | Latest | location TBD (not in local source set) |
| CSA G40.20/G40.21 — Structural steel materials | Latest | location TBD (not in local source set) |

Source for the list: DBM-Deepcut §"Governing Civil and Structural Basis." Editions and clause-level requirements were not derived because the standards themselves are not locally accessible (ASSUMPTION: "latest edition" per DBM directive).

## Verification

| Requirement | Verification Approach |
|---|---|
| R1.1–R1.3 (Identification) | Field-by-field check against `_CONTEXT.md` and `PACKAGE_REGISTER.csv` row PKG-102. |
| R2.1–R2.5 (Codes and standards) | Document inspection: datasheet cites each governing code/standard with edition basis. |
| R3.1–R3.3 (Geotechnical inputs) | Cross-reference to geotechnical report (when issued); TBD entries closed by report acceptance. |
| R3.4 (Top-of-cap coordination) | Cross-check against civil grading drawing/plot plan revisions. |
| R4.1–R4.4 (Foundation type basis) | Source citation check against DBM-Deepcut §"Piles and Foundations" and any superseding detailed-engineering record. |
| R4.5 (Concrete/reinforcement/anchorage TBDs) | Closure when detailed engineering issues mix designs, rebar schedules, and anchor schedules; datasheet revision references those documents. |
| R5.1 (Interface facts carried) | Inspection: both interface IDs present with workbook-row provenance. |
| R5.2 (Interface matrix) | Inspection: matrix rows align with `INTERFACE_REGISTER.csv` entries; ASSUMPTIONS labeled. |
| R6.1 (External dependencies) | Inspection: every TBD attribute has a matching external-input row. |

## Documentation

The following artifacts are expected to exist within or be referenced from this deliverable (from `_CONTEXT.md` Anticipated Artifacts and `ARTIFACT_REGISTER.csv`):

- Package technical datasheet (`ART-413738A117`)
- Vendor engineering handoff basis (`ART-2B819DEF12`)
- Package interface requirements matrix (`ART-BA3D34EA23`)
- Interface fact — Grading / Site Drainage / Spill Containment (`ART-05281DC8CE`, evidencing `IFC-1EDEDC0453`)
- Interface fact — Structural / Foundations / Supports (`ART-F35AC96771`, evidencing `IFC-8283744B5B`)
- Source-supported equipment and design criteria record (carried inline in `Datasheet.md` Attributes/Conditions/Construction)

The four production documents in this folder (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`) are not themselves the package artifact; they capture, organize, and source-ground the data that the formal datasheet artifact will contain.
