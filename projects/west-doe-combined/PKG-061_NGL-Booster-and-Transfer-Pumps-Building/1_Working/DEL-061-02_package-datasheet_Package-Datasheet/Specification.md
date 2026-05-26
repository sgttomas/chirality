# Specification — DEL-061-02 Package Datasheet (PKG-061)

## Scope

This specification governs the package datasheet content for **PKG-061 NGL Booster and Transfer Pumps Building**, the EPC Integrator technical handoff deliverable that conveys package data required for third-party vendor or discipline package engineering and design. Coverage:

- In scope: package identification, equipment list, process/design conditions, construction attributes, physical interface applicability, vendor engineering deliverable expectations, scope exclusions/by-others.
- Out of scope: detailed interface row-level reconciliation (deferred to the package-interface deliverable); detailed vendor-internal design.

Covers scope items `SOW-0149`, `SOW-0150`, `SOW-0151`, `SOW-0152` and supports objectives `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (per `_CONTEXT.md` and DELIVERABLE_REGISTER.csv).

## Requirements

### R-1 Package identity

The package datasheet SHALL identify the package by PackageID (PKG-061), Package Name, Workbook row, discipline, type, and responsibility allocation. Source: PACKAGE_REGISTER.csv row PKG-061.

### R-2 Equipment list

The datasheet SHALL list the two LPG booster pumps `P-9570-1` and `P-9580-1` as the primary package equipment, arranged in parallel. Source: docx §26020-01-PT-18-004 "Major Included Equipment"; DBM row 58.

### R-3 Equipment type and code

Each pump SHALL be a vertical multistage can-type centrifugal pump compliant with API 610. Source: docx §26020-01-PT-18-004; DBM row 58.

### R-4 Sealing

Each pump SHALL be furnished with API 610 seal plan 13/52. Source: docx §26020-01-PT-18-004.

### R-5 Motor electrical service

Pump motors SHALL be rated 575 V / 3 phase / 60 Hz. Source: docx §26020-01-PT-18-004.

### R-6 Hydraulic sizing

Each pump SHALL be sized for **145 m³/h** flow capacity at **150% capacity**, against a **booster design differential of 25 psid (172 kPad)**. TDH is **TBD** in the source (`location TBD`). Source: docx §26020-01-PT-18-004 "Scope Notes / Open Items".

### R-7 Pressure code

CRN / TSBC registration SHALL be provided as applicable. Source: docx §26020-01-PT-18-004.

### R-8 Skid and ancillaries

The package SHALL include structural skid, package piping, instrumentation, electrical, HVAC/enclosure, and commissioning support. Source: docx §26020-01-PT-18-004.

### R-9 Interface applicability

Physical interfaces declared applicable for PKG-061 (per PACKAGE_REGISTER.csv "ApplicableInterfaceTypes") SHALL be documented in the package datasheet as listed in `Datasheet.md` §"Interfaces". Detailed row-level applicability remains **TBC** per docx until reconciled to the current interface matrix (`26020-Packages_Interfaces_4_export.xlsx`). Source: PACKAGE_REGISTER.csv; docx §26020-01-PT-18-004 "Physical Interface Summary".

### R-10 Exclusions / by-others

The datasheet SHALL state that DCS integration, foundations, and electrical supply to MCC are **by others**. Source: docx §26020-01-PT-18-004 "Scope Notes / Open Items".

### R-11 Vendor engineering deliverables

The datasheet SHALL enumerate the vendor engineering deliverables required by the package source (core vendor documents; core package engineering; rotating equipment / pumps), as listed in `Datasheet.md` §"Vendor Engineering Deliverables". Source: docx §26020-01-PT-18-004 "Vendor Engineering Deliverables".

### R-12 Provenance discipline

Each non-trivial datasheet value SHALL cite its source (`SourcePath` + `SectionRef`) or carry `location TBD` if the exact slice is not pinned. Inferred values SHALL be labeled `ASSUMPTION`. Source: skill `four-documents` non-negotiable constraints.

### R-13 Naming-conflict disclosure

The datasheet SHALL surface the conflict between the package/folder name ("NGL Booster…") and the authoritative Word section title ("LPG Booster"), without silently reconciling. Source: Conflict Table in `Guidance.md`.

## Standards

| Standard | Use | Location |
|---|---|---|
| API 610 | Centrifugal pump type and seal-plan family | location TBD (referenced by docx §26020-01-PT-18-004) |
| API 610 Seal Plan 13/52 | Pump sealing arrangement | location TBD |
| CRN (Canadian Registration Number) | Pressure-equipment registration | location TBD |
| TSBC (Technical Safety BC) | Provincial regulatory acceptance | location TBD |

`location TBD` reflects that no copy of these standards is available in `_Sources`; standards are named by the package source but not provided.

## Verification

| Req | Verification approach | Evidence | Source |
|---|---|---|---|
| R-2 | Vendor equipment list (MEC-002) lists P-9570-1 and P-9580-1 | MEC-002 | docx Vendor Eng Deliverables |
| R-3, R-4 | Pump Data Sheets (MEC-007) and Rotating Equipment Specifications (MEC-004) state API 610 and seal plan 13/52 | MEC-007, MEC-004 | docx |
| R-5 | Motor Starting Study (ELE-011) and pump data sheet confirm 575 V / 3 ph / 60 Hz | ELE-011, MEC-007 | docx |
| R-6 | Pump Hydraulic / NPSH Calculations (PRO-013) and pump data sheet confirm 145 m³/h, 150%, 25 psid; TDH resolved | PRO-013, MEC-007 | docx |
| R-7 | CRN/TSBC certificates and pressure-equipment registration package | QLT-013, MEC-014 | docx |
| R-8 | Mechanical Design Basis (MEC-001), Equipment General Arrangement (MEC-016), Equipment Installation drawings (MEC-017) | MEC-001/016/017 | docx |
| R-9 | Package-interface deliverable cross-checks against `26020-Packages_Interfaces_4_export.xlsx` row(s) for PKG-061 | Package-interface deliverable | docx; PACKAGE_REGISTER.csv |
| R-10 | Battery-limit table in MEC-001 / package GA confirms by-others items | MEC-001, MEC-016 | docx |
| R-11 | Vendor Document Index (PRQ-009) lists each deliverable; SDR review at FAT | PRQ-009, QLT-021 | docx |
| R-12 | Datasheet content review (this deliverable) against `_REFERENCES.md` | This deliverable | skill `four-documents` |
| R-13 | Conflict Table in `Guidance.md` ruled by human | Conflict Table | Method |

## Documentation

The package datasheet shall be delivered as the following artifacts (per `_CONTEXT.md` "Anticipated Artifacts"):

- Package technical datasheet (`Datasheet.md`)
- Vendor engineering handoff basis (`Specification.md`, `Guidance.md`)
- Package interface requirements matrix (referenced; row-level reconciliation in package-interface deliverable) — `location TBD` for the row-level matrix.
- Source-supported equipment and design criteria (this deliverable's combined four-document kit)
