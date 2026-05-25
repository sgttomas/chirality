# Specification: DEL-019-02_package-datasheet

## Scope

### In scope
- Technical handoff datasheet for `PKG-019` "MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD" (Workbook Packages row 21, CoA `26020-02-30-009`).
- Package data required for third-party vendor or discipline package engineering and design (`DELIVERABLE_REGISTER.csv` row 97).
- Package interface requirements matrix for the six interface types declared for `PKG-019` in `INTERFACE_REGISTER.csv`.
- Source-supported equipment and design criteria, with `TBD` where source material is not present.

### Out of scope
- Detailed VFD engineering, sizing, harmonic studies, and topology selection (vendor / detailed electrical design; ref. `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 326, 756).
- Construction work planning (`DEL-019-03_construction-work-package`).
- Vendor-engineered equipment package contents (`DEL-019-04_vendor-engineered-equipment-package`).
- Vendor document register and turnover (`DEL-019-05_vendor-document-turnover-package`).
- EPC vendor review and acceptance (`DEL-019-06_epc-vendor-package-review-and-acceptance`).

## Requirements

| Req ID | Requirement | Source | Status |
|---|---|---|---|
| REQ-019-02-01 | The datasheet shall identify the package by name, workbook row, CoA tracking number (`26020-02-30-009`), WBS (`02`), and discipline (Electrical), consistent with `PACKAGE_REGISTER.csv` row `PKG-019`. | `PACKAGE_REGISTER.csv` row 21 | FACT |
| REQ-019-02-02 | The datasheet shall capture the package responsibility model: Package Vendor owns package engineering, design, vendor documentation, and physical equipment; EPC Integrator owns facility integration and interfaces. | `PACKAGE_REGISTER.csv` row `PKG-019` | FACT |
| REQ-019-02-03 | The datasheet shall represent the six declared interface types (Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, Structural / Foundations / Supports) as evidence rows in the package interface requirements matrix. | `INTERFACE_REGISTER.csv` rows for `PKG-019` | FACT |
| REQ-019-02-04 | The datasheet shall record the driven-motor electrical basis (4,000 V class, three-phase, 60 Hz, 3,878 kW / 5,200 hp, NEMA MG1 compliant, TEFC or WPII, Class F / Class B rise, ~891 rpm 8-pole, continuous inverter duty, starting VFD per SCA-001 VE #34) as the source-supported reference for the driven load envelope. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 324-326, 533 | FACT |
| REQ-019-02-05 | The datasheet shall identify the upstream MV source as the 4160V MCC fed from a 13.8 kV → 4.16 kV, 12 MVA transformer with EtherNet communication to the plant PLC central control panel. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 744, 752-754 | FACT |
| REQ-019-02-06 | The datasheet shall note the SCA-001 VE #37 constraint removing capacitor banks from the synchronous bus on MCC-8200 where VFDs are present, and shall mark detailed harmonic / reactive-power mitigation as a detailed-design item. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 756 | FACT |
| REQ-019-02-07 | The datasheet shall not assert clause-level vendor-engineering values (filter topology, enclosure rating, cooling basis, footprint, weights) absent supporting source slices; missing values shall be marked `TBD`. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 326; source gap | FACT |
| REQ-019-02-08 | The datasheet shall surface the workbook ambiguity between `PKG-018` (row 20) and `PKG-019` (row 21), which share the same name and CoA tracking number, until human ruling resolves the motor-tag allocation. | `PACKAGE_REGISTER.csv` rows 20-21; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 326 | ASSUMPTION |
| REQ-019-02-09 | The datasheet shall surface the nameplate discrepancy between the workbook package name (5000 HP / 4160 V) and the DBM motor basis (5,200 hp / 4,000 V) as a conflict for human ruling. | Workbook Packages row 21; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 324 | ASSUMPTION |
| REQ-019-02-10 | The datasheet shall provide a vendor engineering handoff basis sufficient for a third party to begin package engineering, with all interpretive gaps explicitly marked `TBD`. | `DELIVERABLE_REGISTER.csv` row 97; `ARTIFACT_REGISTER.csv` row `ART-80FE29D4E9` | FACT |

## Standards

| Standard / governing reference | Applicability | Location | Status |
|---|---|---|---|
| NEMA MG1 | Driven-motor design and inverter-duty rating (per DBM motor basis). | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 324 | FACT |
| SCA-001 Vendor Exception #34 | Establishes the starting-VFD basis (KM-2150 / KM-2250); soft starts excluded. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 326 | FACT |
| SCA-001 Vendor Exception #37 | Removes capacitor banks from synchronous bus on MCC-8200 where VFDs are present. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 756 | FACT |
| Canadian Electrical Code (CEC) | Grounding and bonding sizing — directional. Applicability to PKG-019 confirmed by detailed design. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (grounding paragraphs, location TBD) | ASSUMPTION |
| IEEE 519 (harmonic limits) | PROPOSAL: candidate standard for harmonic mitigation per SCA-001 VE #37 trigger. Not cited in accessible source. | location TBD | ASSUMPTION |
| `26020-Package_Requirements.docx` | Project-level package requirements file referenced in `_REFERENCES.md` shared source root. No PKG-019-specific match located. | `_Sources/26020-Package_Requirements.docx` (no PKG-019 slice found in this run) | TBD |

## Verification

| Req ID | Verification approach | Evidence target |
|---|---|---|
| REQ-019-02-01 | Cross-check Datasheet Identification table against `PACKAGE_REGISTER.csv` row 21. | Identification block of `Datasheet.md`. |
| REQ-019-02-02 | Confirm responsibility-model row mirrors `PACKAGE_REGISTER.csv` responsibility text. | Identification block of `Datasheet.md`. |
| REQ-019-02-03 | Confirm each `INTERFACE_REGISTER.csv` PKG-019 row appears under Conditions with its `IFC-*` ID. | Conditions table of `Datasheet.md`. |
| REQ-019-02-04 | Confirm driven-motor electrical basis row cites DBM lines 324-326, 533. | Attributes table of `Datasheet.md`. |
| REQ-019-02-05 | Confirm MV source bus row cites DBM lines 744, 752-754. | Attributes table of `Datasheet.md`. |
| REQ-019-02-06 | Confirm SCA-001 VE #37 capacitor-bank constraint is captured. | Attributes table of `Datasheet.md`. |
| REQ-019-02-07 | Inspect Datasheet Construction table for `TBD` markings on vendor-engineering values. | Construction table of `Datasheet.md`. |
| REQ-019-02-08 | Confirm the PKG-018 / PKG-019 duplication is surfaced in `Guidance.md` Conflict Table. | `Guidance.md` Conflict Table row CONF-019-02-A. |
| REQ-019-02-09 | Confirm the 5000HP/4160V vs. 5200hp/4000V conflict is surfaced. | `Guidance.md` Conflict Table row CONF-019-02-B. |
| REQ-019-02-10 | Confirm the four-document kit complete and traceable to sources via `Procedure.md` records. | `Procedure.md` Records section. |

## Documentation

Per `ARTIFACT_REGISTER.csv` rows for `DEL-019-02_package-datasheet`:
- `ART-5A37F6237F` — Package technical datasheet (this `Datasheet.md`).
- `ART-80FE29D4E9` — Vendor engineering handoff basis (covered by Attributes + Conditions of `Datasheet.md`, supplemented by `Guidance.md`).
- `ART-0FE791170D` — Package interface requirements matrix (Conditions table of `Datasheet.md`).
- `ART-4F61C50D94`, `ART-3900B1470F`, `ART-AEA9144682`, `ART-931344A6F9`, `ART-2D951F7FE7`, `ART-1EE9AAD1E3` — Interface fact evidence rows (Conditions table of `Datasheet.md`, each cited by `IFC-*` ID).
