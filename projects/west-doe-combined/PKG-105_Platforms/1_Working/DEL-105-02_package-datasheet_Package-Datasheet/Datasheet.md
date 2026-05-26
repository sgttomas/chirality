# Datasheet — DEL-105-02 Package Datasheet (PKG-105 Platforms)

> Source-grounded technical datasheet for the EPC Integrator handoff of the workbook-defined Structural package "Platforms" (Workbook row 106, WBS 01). Values not explicitly supported by accessible source material are marked **TBD** or **ASSUMPTION**; nothing is invented.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-105-02_package-datasheet` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package ID | `PKG-105` | `PACKAGE_REGISTER.csv` |
| Parent Package Name | Platforms | `PACKAGE_REGISTER.csv` row 106 |
| Workbook ID | 105 (workbook row 106) | `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| Discipline | Structural | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Package Type | EPC Package Datasheet | `DELIVERABLE_REGISTER.csv` |
| Responsible Party | EPC Integrator | `DELIVERABLE_REGISTER.csv` |
| CoA / Source ID(s) | 26020-01-36-005 | `PACKAGE_REGISTER.csv` |
| Scope Item Covered | `SOW-0261` | `SCOPE_LEDGER.csv` |
| Supports Objectives | OBJ-001, OBJ-005, OBJ-008, OBJ-010 | `OBJECTIVE_DELIVERABLE_MAP.csv` (PACKAGE_HEURISTIC; **ASSUMPTION (best-effort mapping)**) |

## Attributes

| Attribute | Value | Source / Note |
|---|---|---|
| Package function | Structural platforms supporting plant equipment, access, and tie-ins for the WBS 01 facility | `PACKAGE_REGISTER.csv`; `SCOPE_LEDGER.csv` SOW-0261 |
| Package classification | Workbook-defined Structural package | `SCOPE_LEDGER.csv` SOW-0261 |
| Major equipment list | TBD — workbook row 106 does not enumerate tagged equipment in the accessible register slice | `PACKAGE_REGISTER.csv` (Notes column lists interface types only) |
| Quantity / count of platforms | TBD | not stated in accessible sources |
| Geometry / footprint | TBD | not stated in accessible sources |
| Materials of construction | Structural steel per CSA G40.20/G40.21 350W for W-flange and HSS; 300W for channels, plates, and angles | `DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-11 §Governing Civil and Structural Basis (**ASSUMPTION**: applied to Structural Platforms package by default; not platform-specific in source) |
| Foundation basis | Driven steel piles (default for buildings, equipment, towers, tanks, modules, pipe racks, and similar structures) | `DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-11 §Piles and Foundations |
| Erection basis | TBD per platform; module/erection table in DBM SEC-11 does not list a discrete "platforms" inventory line | `DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-11 §Buildings and Miscellaneous Facilities (table) |

## Conditions

| Condition | Value | Source / Note |
|---|---|---|
| Environmental loading basis | Project-site snow, rain, wind, and seismic per National Building Code of Canada | `DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-11 §Buildings and Miscellaneous Facilities (**ASSUMPTION**: same loading regime applies to platforms; stated in source for project buildings) |
| Geotechnical parameters | TBD pending geotechnical report (bearing capacity, LPILE curves, dynamic design criteria) | `DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-11 §Geotechnical and Topographical Assumptions |
| Site grading / drainage interface | Pad slopes 1.5% (1.0% allowed where required) from main pipe racks; surface-control features per SEC-11 | `DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-11 §Site Grading and Surface Water Management |
| Containment / spill | Surface-control features around selected equipment; NGL area-specific containment provisions in SEC-11 | `DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-11 §Site Grading and Surface Water Management (relevance to platforms: **ASSUMPTION**, applied via interface to Grading / Site Drainage / Spill Containment) |
| Operating temperature / pressure | Not applicable — structural platforms are passive support | **ASSUMPTION** |

## Construction

| Item | Basis | Source / Note |
|---|---|---|
| Governing building code | National Building Code of Canada | DBM SEC-11 §Governing Civil and Structural Basis |
| Steel design code | CAN/CSA-S16 Design of Steel Structures | DBM SEC-11 §Governing Civil and Structural Basis |
| Concrete design code | CAN/CSA A23.3 (for concrete elements only) | DBM SEC-11 §Governing Civil and Structural Basis |
| Foundation engineering reference | Canadian Foundation Engineering Manual | DBM SEC-11 §Governing Civil and Structural Basis |
| Concrete material/test code | CSA A23.1/A23.2 | DBM SEC-11 §Governing Civil and Structural Basis |
| Fabrication / erection sequencing | TBD — platform-specific shop/field split not enumerated in DBM module table | DBM SEC-11 §Buildings and Miscellaneous Facilities |
| Coatings / finishes | TBD — DBM specifies building colors; no platform coating spec stated | DBM SEC-11 §Buildings and Miscellaneous Facilities |

## Package Interface Facts (carried as datasheet evidence per `_CONTEXT.md` Notes)

| Interface ID | Interface Type | Applicability | Disposition |
|---|---|---|---|
| `IFC-26E3DCAD56` | Area / Exterior Lighting | YES | Platform-to-equipment tie-ins confirmed by layout/model. Gate 6 disposition: EPC Integrator responsibility through overall 3D model and integrated P&ID set. (`INTERFACE_REGISTER.csv`) |
| `IFC-07C472C58B` | Grading / Site Drainage / Spill Containment | YES | Same Gate 6 disposition as above. (`INTERFACE_REGISTER.csv`) |
| `IFC-B7C0A01E38` | Structural / Foundations / Supports | YES | Same Gate 6 disposition as above. (`INTERFACE_REGISTER.csv`) |

## Anticipated Artifacts (this deliverable carries)

- Package technical datasheet (ART-E5A717EC97) — `ARTIFACT_REGISTER.csv`
- Vendor engineering handoff basis (ART-EA98D39386) — `ARTIFACT_REGISTER.csv`
- Package interface requirements matrix (ART-A71A680036) — `ARTIFACT_REGISTER.csv`
- Interface fact evidence: Area/Exterior Lighting (ART-39021CDFB3); Grading/Site Drainage/Spill Containment (ART-217A830349); Structural/Foundations/Supports (ART-1FA7F21048) — `ARTIFACT_REGISTER.csv`
- Interface note disposition record (ART-749A9EEC06) — `ARTIFACT_REGISTER.csv`

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- GATE-07 snapshot registers: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `ARTIFACT_REGISTER.csv`, `INTERFACE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`, `OBJECTIVE_REGISTER.csv`, `SCOPE_LEDGER.csv`
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` SEC-11 (Civil, Buildings, and Miscellaneous Facilities Basis)
- Workbook Packages row 106 (cited via registers; raw workbook source slice not directly accessible as text)
