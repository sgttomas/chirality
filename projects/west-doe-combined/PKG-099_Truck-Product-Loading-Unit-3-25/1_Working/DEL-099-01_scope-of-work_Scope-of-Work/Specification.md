# Specification — DEL-099-01 Scope of Work (PKG-099 Truck Product Loading Unit 3-25)

> Normative view of what this EPC Scope of Work must contain and the requirements it imposes on the package.
> Each requirement is source-grounded or marked **ASSUMPTION**. `TBD` is used where evidence is missing or inaccessible.

## Scope

### In scope (EPC Integrator — Scope of Work content)

This deliverable produces the EPC Integrator authored package Scope of Work for PKG-099 (Truck Product Loading Unit 3-25), comprising:

- Package scope of work statement (function, fluids, boundaries) — covers `SOW-0241`–`SOW-0244` and supports `OBJ-002`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010`. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` DEL-099-01 row.)
- Tagged equipment and package identity list. (Source: `ARTIFACT_REGISTER.csv` ART-6C537783A7.)
- Package function and whole-facility integration narrative. (Source: `ARTIFACT_REGISTER.csv` ART-B3C48AB23D.)
- Package responsibility assignment record. (Source: `ARTIFACT_REGISTER.csv` ART-B927725D35.)
- Source scope evidence linking the package basis to `26020-Package_Requirements.docx` heading 51 and Workbook Packages row 98. (Source: `ARTIFACT_REGISTER.csv` ART-E2749573BE; `ART-F9FBC08466`.)

### Out of scope

- Package Datasheet content (carried in `DEL-099-02_package-datasheet`). (Source: `DELIVERABLE_REGISTER.csv` DEL-099-02 row.)
- Construction Work Package content (carried in `DEL-099-03_construction-work-package`). (Source: `DELIVERABLE_REGISTER.csv` DEL-099-03 row.)
- Vendor engineered equipment package (vendor production unit; carried in `DEL-099-04`). (Source: `DELIVERABLE_REGISTER.csv` DEL-099-04 row.)
- Vendor document turnover (`DEL-099-05`) and EPC vendor package review and acceptance (`DEL-099-06`). (Source: `DELIVERABLE_REGISTER.csv` DEL-099-05/-06 rows.)
- Third-party NRM LACT equipment for sales condensate custody transfer; the 03-25 scope ends at the tie-in flange. (Source: `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-01 line 22, SEC-05 line 207.)
- Pipeline export design downstream of the 03-25 facility tie-in (by others). (Source: `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06 line 216, SEC-08 line 432.)

## Requirements

### R-1 — Package function statement

The Scope of Work shall state the package function as: Sweet Dehydrated Condensate from the Condensate Storage Tanks is pumped by Truck Loading pumps to the Truck Loading stations, metered, and fills atmospheric condensate trucks.
Source: `PACKAGE_REGISTER.csv` PKG-099 row (Package Scope).

### R-2 — Tagged equipment and identity

The Scope of Work shall identify the package by Workbook ID 99 (row 98), CoA/Tag number `26020-03-23-001`, WBS 03, Discipline Mechanical, and Tag Name `26020-03-PT-23-001 - Condensate Truck Loading Stations`.
Source: `PACKAGE_REGISTER.csv` PKG-099 row.

### R-3 — Major included equipment (per RFQ row evidence)

The Scope of Work shall reference the major included equipment list:
- Truck Loading/Unloading Stations (quantity per HRR — see CT-01)
- Basket strainer: Sureflow 0300BF300SS, 316SS, with Mesh Screen
- Emergency Shut Down Valve (ESDV)
- Flow transmitters
Source: `ARTIFACT_REGISTER.csv` ART-517D0E9F90.

### R-4 — Per-station capacity (DBM basis)

The Scope of Work shall record the per-station loading capacity basis as 103 m3/h at 345 kPad differential per station.
Source: `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06 (line 415).

### R-5 — Upstream supply basis

The Scope of Work shall record that condensate is supplied from the Condensate Storage Tanks via dedicated condensate loading pumps (one per truck-loading station per DBM basis).
Source: `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-06 (lines 414, 526, 578).

### R-6 — Whole-facility integration narrative

The Scope of Work shall include a narrative explaining how the package integrates with the Liquids Hub, with the NRM LACT custody-transfer interface (parallel disposition for sales condensate), with shared utilities (electrical, F&G, drainage, lighting, control), and with the construction/operation interfaces listed in R-9.
Source: `ARTIFACT_REGISTER.csv` ART-B3C48AB23D; `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-01, SEC-06.

### R-7 — Responsibility assignment

The Scope of Work shall record: Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns integration into the functional process facility — interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration.
Source: `PACKAGE_REGISTER.csv` PKG-099 row (Owner/Responsibility); `ARTIFACT_REGISTER.csv` ART-B927725D35.

### R-8 — Scope items coverage

The Scope of Work shall traceably cover `SOW-0241`, `SOW-0242`, `SOW-0243`, `SOW-0244` and identify which objectives it supports (`OBJ-002` and `OBJ-003`–`OBJ-010`).
Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` DEL-099-01 row.

### R-9 — Applicable interfaces enumerated

The Scope of Work shall enumerate the eleven workbook-flagged applicable interface types for PKG-099 (Process Piping; Drain/Containment; Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Grading/Site Drainage/Spill Containment; Structural/Foundations/Supports; Product Loading) and reference the corresponding `INTERFACE_REGISTER.csv` IDs (`IFC-*` listed in Datasheet).
Source: `PACKAGE_REGISTER.csv` PKG-099 row (Applicable Interface Types); `INTERFACE_REGISTER.csv` PKG-099 rows.

### R-10 — Exclusions

The Scope of Work shall record the LACT third-party scope boundary (R-1 service is parallel, not the LACT route) and shall note that pipeline-export design downstream of the facility tie-in is by others. Where the workbook explicitly states no package-specific exclusions, that fact shall be recorded.
Source: `PACKAGE_REGISTER.csv` PKG-099 row (Exclusions: "TBD; no package-specific exclusions stated in source materials."); `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-01 line 22, SEC-06 line 216.

### R-11 — Source basis traceability

Every substantive value in the Scope of Work shall cite a source. Inaccessible sources (e.g., `26020-Package_Requirements.docx` heading 51, RFQ docx) shall be cited with `location TBD` and not relied on for clause-level numeric values.
Source: skill `four-documents` SKILL.md Authority hierarchy and source-grounding rule.

### R-12 — Permit and environmental basis (carry-forward)

The Scope of Work shall note that the truck-rack scope is subject to further BCER permit amendment beyond BCER 100120203 and that the facility electrification basis underlies the current environmental exclusion.
Source: `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC-17 (line 872).

## Standards

| Standard / Source | Applicability | Local Access |
|---|---|---|
| `26020-Package_Requirements.docx` heading 51 | Authoritative package basis for PKG-099 | Not locally accessible (docx); `location TBD` |
| Workbook `26020-Packages_Interfaces_4_export.xlsx` row 98 | Authoritative workbook row for PKG-099 | Not locally accessible (xlsx); facts carried via `PACKAGE_REGISTER.csv`/`INTERFACE_REGISTER.csv` derived rows |
| RFQ `26020-03-PT-RFQ-23-001_Truck_Load_stn_R0.docx` | Vendor RFQ source for major equipment list | Not locally accessible; equipment facts carried via `ART-517D0E9F90` |
| `DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` | Design Basis Memorandum for 03-25 Compressor Station and Liquids Hub | Locally accessible |
| Codes/standards for truck loading (grounding, overfill, vapour recovery, classification, fire protection) | Likely applicable | **ASSUMPTION: likely applicable**; not enumerated in accessible sources at this grain — `TBD` |

## Verification

| Req | Verification approach | Evidence target |
|---|---|---|
| R-1 | Section review against `PACKAGE_REGISTER.csv` PKG-099 row | Scope statement matches workbook function text |
| R-2 | Identity table review | Workbook ID 99 / row 98 / Tag 26020-03-23-001 / WBS 03 present |
| R-3 | Equipment list cross-check | Matches `ART-517D0E9F90` |
| R-4 | DBM cross-check | Per-station 103 m3/h / 345 kPad recorded |
| R-5 | DBM cross-check | One loading pump per station basis recorded |
| R-6 | Narrative review | Integration narrative present and source-cited |
| R-7 | Responsibility table review | Vendor vs Integrator split per workbook |
| R-8 | Traceability check | `SOW-0241`–`SOW-0244` and OBJ list explicitly referenced |
| R-9 | Interface enumeration check | Eleven interfaces listed with `IFC-*` IDs |
| R-10 | Exclusion review | LACT and pipeline-export boundary recorded |
| R-11 | Citation audit | Every substantive claim cites a source or is marked `TBD`/`ASSUMPTION` |
| R-12 | Permit note review | BCER 100120203 + truck-rack amendment caveat recorded |

## Documentation

Deliverable artifacts produced (per `ARTIFACT_REGISTER.csv` PKG-099 rows for DEL-099-01):

- `ART-F9FBC08466` Package scope of work
- `ART-6C537783A7` Tagged equipment and package identity list
- `ART-B3C48AB23D` Package function and whole-facility integration narrative
- `ART-B927725D35` Package responsibility assignment record
- `ART-E2749573BE` Detailed mechanical package scope extraction evidence
