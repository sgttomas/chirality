# Specification: DEL-094-04 — Vendor Engineered Equipment Package

## Scope

This specification governs the Package Vendor's engineering, design, fabrication/supply, and delivery of the physical equipment package for PKG-094 "Tanks, Caustic (API 650) 3-25." The vendor production unit is anchored by the EPC package Scope of Work (DEL-094-01) and Package Datasheet (DEL-094-02), and produces the engineered equipment package together with its design basis and datasheet set for downstream construction (DEL-094-03), turnover (DEL-094-05), and EPC review/acceptance (DEL-094-06).

Inclusions:
- Mechanical engineering and design of the caustic tank package and ancillary equipment in PKG-094's scope.
- Fabrication/supply of the physical equipment package.
- Vendor design basis and vendor datasheet set issued as part of the package.

Exclusions:
- Construction installation work (covered by DEL-094-03).
- Vendor document turnover/turnover records (covered by DEL-094-05).
- EPC integration review and acceptance (covered by DEL-094-06).

## Requirements

### R1 — Compliance with EPC Scope of Work and Package Datasheet
The vendor package shall conform to the EPC-issued package Scope of Work (DEL-094-01) and Package Datasheet (DEL-094-02). Source: `_CONTEXT.md` Scope; decomposition register row.

### R2 — API 650 family code application (caustic tanks)
Caustic storage tanks within the package shall be designed in accordance with the API 650 code family appropriate to atmospheric tank service in caustic and ancillary process duty consistent with the package title. Specific edition, appendices (e.g., Appendix S, Appendix M), and any project-specific code modifications are TBD pending EPC-issued package datasheet. ASSUMPTION: API 650 governance is taken from the package title; clause-level requirements are not derived because the package datasheet and 26020-Package_Requirements.docx heading 46 are not locally accessible.

### R3 — Site/ambient design basis
The package shall be designed for the 03-25 site basis, with minimum ambient -40 deg C governing exposed equipment, package buildings, control panels, instrumentation, and field devices unless a more severe process or vendor condition applies. Winterization, electrical heat tracing, building heating, tank heating, foundations, structural steel, and equipment metallurgy shall reflect this basis. Source: DBM 3-25 site basis.

### R4 — Caustic service basis
Where caustic storage and handling equipment is in scope, the design basis shall be 50 wt% NaOH/H2O with SG 1.75 TBC for caustic solution. Source: DBM 3-25 (caustic basis; SG marked TBC in source).

### R5 — Tank construction class (caustic family)
Fresh-caustic, spent-caustic, caustic process-water, and H2O2 tanks are atmospheric 32 oz tanks, LP fuel-gas blanketed, heated, and insulated. Tank sizes are 400 bbl for the caustic family per current DBM basis. Final tank register supersedes the DBM if and when issued. Source: DBM 3-25 (liquids hub equipment basis; caustic tanks).

### R6 — Material selection and prohibitions
- Aluminum shall not be used in the caustic building. Source: DBM 3-25.
- Caustic-wetted material selection (vessel shell, internals, nozzles, gaskets) and internal coatings shall be selected for 50 wt% NaOH service across the design temperature range; specific materials and coatings are TBD pending vendor design (DBM marks caustic tank material/coating as TBC).

### R7 — Vent, drain, and interface requirements
- Spent caustic tank vent shall route through a flame arrestor to the incinerator header and support truck-out. Source: DBM 3-25.
- Fresh caustic tank shall not be connected to the VRU. Source: DBM 3-25.
- Caustic drain headers terminating at caustic tank flanges shall be designed minimum 300# ANSI; maximum design temperature 121 deg C / 250 deg F TBC; minimum drain-tank temperature 80 deg F. Source: DBM 3-25 (drain systems).

### R8 — Vendor design basis and datasheet set
The vendor shall produce a vendor package design basis and vendor datasheet set as anticipated artifacts of the production unit. Source: `_CONTEXT.md` Anticipated Artifacts.

### R9 — Interfaces
The package shall expose mechanical, process, instrumentation, electrical, and structural interfaces consistent with the Package Datasheet (DEL-094-02) and the 03-25 Liquids Hub design basis. Specific interface schedules are TBD pending Package Datasheet issuance.

### R10 — Scope-of-Work traceability
The vendor package shall trace back to scope items SOW-0193, SOW-0194, SOW-0195, SOW-0196. ASSUMPTION: mapping to individual SOW IDs requires the EPC SOW (DEL-094-01) for verification.

## Standards

| Standard | Application | Location |
|---|---|---|
| API 650 (atmospheric storage tanks) | Caustic tank shell/roof/bottom design and fabrication | Edition/appendices TBD (location TBD — not locally accessible) |
| 26020-Package_Requirements.docx heading 46 | Package-specific vendor requirements | location TBD (docx not converted) |
| Workbook Packages row 86 | Package row source basis | location TBD (xlsx not converted) |
| 03-25 Liquids Hub DBM | Site, process, and tank-family basis | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |

## Verification

| Requirement | Verification Approach |
|---|---|
| R1 | Document review against DEL-094-01 SOW and DEL-094-02 Package Datasheet by EPC Integrator (DEL-094-06). |
| R2 | Vendor code compliance certification; API 650 nameplate; design report review. |
| R3 | Vendor design basis cites -40 deg C ambient; package buildings/heat tracing documented; review by EPC. |
| R4 | Vendor datasheet states 50 wt% NaOH service basis and SG; reviewed against DBM. |
| R5 | Vendor tank datasheets list 400 bbl atmospheric, 32 oz construction, blanketed, heated, insulated; reviewed against DBM. |
| R6 | Material certifications (MTRs); coating system documentation; building material check (no aluminum). |
| R7 | P&ID/vent/drain interface drawings reviewed against DBM; flame arrestor specification documented. |
| R8 | Vendor design basis and datasheet set delivered with the package. |
| R9 | Interface documents reviewed against Package Datasheet. |
| R10 | Cross-walk of vendor scope to SOW items signed off by EPC Integrator. |

## Documentation

Anticipated documentation artifacts (per `_CONTEXT.md` and DBM):
- Vendor engineered physical equipment package (the equipment itself, with attached identification).
- Vendor package design basis.
- Vendor datasheet set (per equipment item).
- Code compliance documentation (API 650 design report, nameplate records).
- Material test reports (MTRs) and coating documentation.
- Interface drawings (process, mechanical, electrical, instrumentation, structural).
- Inputs to the vendor document turnover package (DEL-094-05).
