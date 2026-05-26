# Specification: DEL-064-04 — Vendor Engineered Equipment Package (Tanks, Water (API 650) 4-25)

> Normative document for the Package Vendor's engineering, design, fabrication/supply, and physical equipment package for PKG-064 (process water storage tanks, x2, at 4-25 Deepcut). Source-grounded to the West Doe Deepcut DBM where accessible; remaining items marked `TBD` or `ASSUMPTION`.

## Scope

### In scope
- Engineering and design of the PKG-064 process water storage tanks (equipment tags `TK-5317-1`, `TK-5318-1`) and the integrated vendor package required for fabrication, supply, delivery, and turnover, in accordance with the EPC Package Datasheet (`DEL-064-02`) and EPC Scope of Work (`DEL-064-01`). (`_CONTEXT.md` Scope; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` package line-item row 2628.)
- Vendor package design basis and datasheet set as anticipated artifacts. (`_CONTEXT.md` Anticipated Artifacts.)
- Physical equipment package: tanks, supports/saddles, nozzles, manways, tank internals, insulation/heat trace as required for winter freeze protection, level/temperature/pressure instrumentation, and PVRV(s) per atmospheric tank practice. (ASSUMPTION based on analogue 4-25 atmospheric tanks; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 518–524, 2509.)
- Integration interface package supporting EPC Integrator review (`DEL-064-06`).

### Out of scope (handled by other deliverables / disciplines)
- Tank Farm Pump Building 2 and process water transfer pumps (separate package roster line; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Tank Farm Pump Building row).
- VRU package and any tank vapour recovery integration (process water tanks are not listed in the VRU gas-source table — `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line ~1714).
- Site civil/foundation work outside the vendor's tank skid/ring-wall responsibility (boundary `TBD` — to be defined in EPC Scope of Work).
- Installation, tie-in, and turnover (covered by `DEL-064-03` Construction Work Package and `DEL-064-05` Vendor Document Turnover Package).

## Requirements

| ID | Requirement | Basis / Source | Label |
|---|---|---|---|
| R-064-04-01 | The vendor shall design and supply two (2) process water storage tanks identified as `TK-5317-1` and `TK-5318-1`. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` row 2628 | FACT |
| R-064-04-02 | The tanks shall conform to API 650 (modified, atmospheric service); the "modified" deviations from API 650 base text shall be defined in the vendor package design basis and reconciled with the EPC Package Datasheet. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` rows 518, 1646 (analogue to other 4-25 atmospheric tanks) | ASSUMPTION — confirm against PKG-064 package row in 26020-Package_Requirements.docx heading 19 (not directly accessible this run) |
| R-064-04-03 | The tanks shall be designed for atmospheric service with a 16 oz/in² test pressure basis, consistent with other 4-25 atmospheric storage tanks, unless the Package Datasheet (`DEL-064-02`) specifies otherwise. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` rows 518, 1647 | ASSUMPTION |
| R-064-04-04 | Maximum operating fill shall be 90% of tank volume; vendor shall provide thermal-expansion review. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` rows 519, 1648 (analogue) | ASSUMPTION |
| R-064-04-05 | Tank shall be externally insulated and freeze-protected to prevent winter freezing. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2509 ("water tanks shall be insulated to prevent winter freezing"); line 524 (analogue) | FACT (insulation requirement); ASSUMPTION (specific tracing scheme) |
| R-064-04-06 | Each tank shall include at least one PVRV; EPRV requirement to be reviewed and sized in detailed engineering. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 524 (analogue to produced water tanks) | ASSUMPTION |
| R-064-04-07 | Blanket gas connections shall be provided for winter vacuum prevention; vent/blanket rates per API 2000 basis. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line ~520, line ~1664 (analogue) | ASSUMPTION |
| R-064-04-08 | Tank materials of construction, internal coating (if any), foundation/ring-wall interface, nozzle schedule, manway schedule, and internals shall be specified by the Package Datasheet and finalized by the vendor; values not yet captured here are `TBD`. | source TBD | TBD |
| R-064-04-09 | Tank design specific gravity shall be specified in the Package Datasheet for process water service (no value located in accessible source slices). | source TBD | TBD |
| R-064-04-10 | The vendor shall produce a package design basis document and a datasheet set covering the tank, instrumentation, accessories, and any vendor-supplied skid items. | `_CONTEXT.md` Anticipated Artifacts | FACT |
| R-064-04-11 | The vendor package shall be designed to satisfy SOW items `SOW-0233`, `SOW-0234`, `SOW-0235`, `SOW-0236` as expressed by the EPC Scope of Work (`DEL-064-01`). | `_CONTEXT.md` Covers Scope Items; PROJECT_DECOMP register | FACT (linkage); content of SOW items — see `DEL-064-01` |
| R-064-04-12 | The vendor shall produce all interface data required for EPC Integrator integration review (`DEL-064-06`), including nozzle lists, loads, instrument I/O list, electrical/utilities list, and operating/upset cases. | `_CONTEXT.md` Scope; PROJECT_DECOMP row 545 | ASSUMPTION (typical vendor-package interface set) |
| R-064-04-13 | The vendor shall comply with site spacing requirements for atmospheric tanks (including minimum 25 m / 82 ft from flare per OGAOM Sec. 9.6.15 as cited in 4-25 DBM). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` row 283 | FACT (cited standard); ASSUMPTION (applicability to process water tank vs. produced water tank — confirm) |

## Standards

| Standard | Applicability | Source / Location |
|---|---|---|
| API 650 (modified) | Tank fabrication standard | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` rows 518, 1646; package title "Tanks, Water (API 650) 4-25"; package-level standard reference in `26020-Package_Requirements.docx` heading 19 — `location TBD` (binary source) |
| API 2000 | Vent and blanket gas sizing | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line ~520 (analogue) |
| OGAOM | Plant spacing | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` row 283 |
| ASME B31.3 (process piping), CSA, AWS, and other governing codes | Tank-package piping, welding, materials | `location TBD` — to be enumerated by Package Datasheet (`DEL-064-02`) |

## Verification

| Requirement | Verification approach |
|---|---|
| R-064-04-01 | Vendor equipment list and tag register reconciled with PROJECT_DECOMP package line-item row 2628. |
| R-064-04-02, R-064-04-03, R-064-04-04 | Vendor design basis document review; tank datasheet review; manufacturer's data report (API 650 nameplate / Form MDR) at fabrication completion. |
| R-064-04-05 | Insulation/heat-trace design review; field inspection at install. |
| R-064-04-06, R-064-04-07 | Relief and vent calculation review (PVRV/EPRV/blanket) per API 2000; HAZOP review. |
| R-064-04-08, R-064-04-09 | Datasheet review; vendor mill certificates; coating inspection per spec; foundation-load review. |
| R-064-04-10 | Document register check (handled jointly by `DEL-064-05`). |
| R-064-04-11, R-064-04-12 | EPC Integrator review and acceptance per `DEL-064-06`. |
| R-064-04-13 | Plot-plan review; spacing-check against OGAOM. |

## Documentation

Vendor package deliverables expected (anticipated artifacts per `_CONTEXT.md` plus typical vendor turnover scope):

- Vendor package design basis document
- Vendor tank datasheet(s) (per tank)
- General arrangement / outline drawings
- Foundation loading drawing
- Nozzle orientation and schedule
- Materials of construction and welding spec sheets
- Insulation and heat-trace specification
- Instrumentation index and loop diagrams (for vendor-supplied instruments)
- Vent/relief/blanket-gas sizing calculations
- Manufacturer's data report (API 650 MDR)
- Inspection and test plan (ITP)
- Operations and maintenance manuals
- Spare parts list

Detailed register and turnover collection is `DEL-064-05` scope.
