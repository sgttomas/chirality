# Specification — DEL-103-02 Package Datasheet (PKG-103 Pipe Rack Modules)

> Normative document. Requirements are derived only from accessible source slices. Inferred requirements are labeled **ASSUMPTION**; missing values are **TBD**.

## Scope

This specification establishes the normative requirements that the Package Datasheet for PKG-103 (Pipe Rack Modules) shall capture and convey to vendors and discipline engineering. It covers the technical, structural, electrical, classification, interface, and construction-handover data needed for third-party vendor or discipline package engineering.

**Includes:**
- Identification of the pipe-rack module package and its boundaries.
- Structural, electrical, heat-tracing, cable-tray, grounding, and interface attributes whose values are explicitly supported by accessible DBM source slices.
- Hazardous-area classification, grading interactions, foundation basis, and skid-edge interface conventions.

**Excludes:**
- Detailed module-by-module structural design (that is the EPC / discipline production package — `DEL-103-04`).
- Construction-execution sequencing (that is the Construction Work Package — `DEL-103-03`).
- Whole-facility integration narrative (that is the Scope of Work — `DEL-103-01`).

## Requirements

| Req ID | Requirement | Source / Basis | Label |
|---|---|---|---|
| R-DS-01 | The datasheet shall identify the package by its DeliverableID, PackageID, package name, and ParentWorkbookID. | `_CONTEXT.md`; decomposition row 585 | FACT |
| R-DS-02 | The datasheet shall declare ResponsibleParty = EPC Integrator. | `_CONTEXT.md`; decomposition row 585 | FACT |
| R-DS-03 | The datasheet shall record outdoor-pipe-rack hazardous-area classification as general purpose / non-hazardous unless detailed area-classification drawings identify otherwise. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2911; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` L722 | FACT |
| R-DS-04 | The datasheet shall record default foundation basis = driven steel piles, with final pile design parameters TBD pending the geotechnical report. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2740, L2749 | FACT |
| R-DS-05 | The datasheet shall record main cable tray runs as pre-installed in the shop on dedicated structural modules at the uppermost section of the pipe rack, with at least 30% future growth capacity in cable trays. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2999, L3023 | FACT |
| R-DS-06 | The datasheet shall record electric heat tracing primary voltage class as 208 V 1Ø 60 Hz with 120 V 1Ø 60 Hz for short lines / instrument tubing, fed from local transformers and heat-tracing distribution panels located along the pipe rack, with transformer feeds from motorized/trip MCC breakers for staged energization. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L3047, L3059 | FACT |
| R-DS-07 | The datasheet shall record grounding/bonding convention: pipe racks welded to piles; main #2/0 green insulated grounding conductor in the highest-voltage-carrying tray; no additional bonding conductors from cable tray down to piles. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2987 | FACT |
| R-DS-08 | The datasheet shall record skid-edge interface convention: isolation located in interconnect piping between the pipe rack and the module / processing unit / building, with vent / drain / spectacle blind provisions per skid-edge connection type. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2454–L2457 | FACT |
| R-DS-09 | The datasheet shall record alarm provisions: visual beacons and audible horns at strategic outdoor piperack locations. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L3262, L3264, L3293, L3296 | FACT |
| R-DS-10 | The datasheet shall record grading-interaction values: facility pad slopes from pipe rack at 1.5% per side; NGL-area grading slopes away from pipe rack and process areas. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L2708–L2709, L2722 | FACT |
| R-DS-11 | The datasheet shall record cable-tray routing constraint: shall not interfere with exchanger bundle removal, cranes / hoists, pumps, or valves. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` L3023 | FACT |
| R-DS-12 | The datasheet shall enumerate locally accessible source materials read and, separately, the package-row source materials that are not locally accessible (with `location TBD`). | Skill `four-documents` source-grounding rule | FACT |
| R-DS-13 | The datasheet shall capture package quantitative attributes (module count, tonnage, dimensional envelope, weight) when these become available from the package-requirements workbook source. Until then, these attributes shall be marked TBD. | Decomposition row 585 (`Workbook Packages row 104`); workbook source not locally accessible as text | ASSUMPTION (necessity); TBD (value) |
| R-DS-14 | The datasheet shall identify the covered scope item `SOW-0259` and the supported objectives carried in `_CONTEXT.md` (under the PACKAGE_HEURISTIC association mode). | `_CONTEXT.md`; OBJECTIVE_ASSOCIATION_MODE override | ASSUMPTION (objective list) |
| R-DS-15 | The datasheet shall be re-issued when any of the cited DBM source slices change in the snapshot of record. | Skill `four-documents` invariant on source fidelity | ASSUMPTION |

## Standards

| Standard / Code | Applicability | Locally Accessible? |
|---|---|---|
| API RP 505 | Basis for area-classification treatment of process modules / buildings as Zone 2 (general project basis) | Referenced in DBM; standard text not in `_Sources` — location TBD |
| Project DBM (Comp & Liquids, March 2025) | Project-wide basis for civil, structural, hazardous-area, electrical, grounding, and heat-tracing provisions | Yes — `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` |
| Project DBM (Deep Cut, April 2025) | Project-wide basis (deep cut variant) for the same scope dimensions | Yes — `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Geotechnical report (project) | Foundation design closure precondition | Not present in `_Sources` — location TBD |
| `26020-Package_Requirements.docx` | Workbook source backing decomposition row 585 | Not text-accessible (binary) — location TBD |
| `26020-Packages_Interfaces_4_export.xlsx` | Package interface workbook backing decomposition row 585 | Not text-accessible (binary) — location TBD |

## Verification

| Req ID | Verification Approach |
|---|---|
| R-DS-01, R-DS-02, R-DS-14 | Direct inspection of the Datasheet `Identification` section against `_CONTEXT.md` and the GATE-07 deliverable register row. |
| R-DS-03 | Cross-check Datasheet `Conditions` entry against DBM Deepcut L2911 and Comp & Liquids L722. |
| R-DS-04 | Cross-check Datasheet `Construction` entry against DBM Deepcut L2740, L2749. |
| R-DS-05 | Cross-check Datasheet `Attributes` and `Conditions` entries against DBM Deepcut L2999, L3023. |
| R-DS-06 | Cross-check Datasheet `Attributes` and `Construction` entries against DBM Deepcut L3047, L3059. |
| R-DS-07 | Cross-check Datasheet `Construction` entry against DBM Deepcut L2987. |
| R-DS-08 | Cross-check Datasheet `Attributes` entry against DBM Deepcut L2454–L2457. |
| R-DS-09 | Cross-check Datasheet `Attributes` entry against DBM Deepcut L3262/L3264/L3293/L3296. |
| R-DS-10 | Cross-check Datasheet `Conditions` entry against DBM Deepcut L2708–L2709, L2722. |
| R-DS-11 | Cross-check Datasheet `Conditions` entry against DBM Deepcut L3023. |
| R-DS-12 | Inspection of `References` and `Notes` sections for explicit accessible / not-accessible enumeration. |
| R-DS-13 | Inspection that quantitative attribute rows exist and are marked TBD, with disposition tied to workbook accessibility. |
| R-DS-15 | Procedural verification via the rerun protocol in `Procedure.md`. |

## Documentation

Anticipated artifacts produced by or carried within this deliverable:

- Package technical datasheet (`Datasheet.md` — this run).
- Vendor engineering handoff basis (extracted from this datasheet's attribute and condition rows).
- Package interface requirements matrix (carried as the skid-edge / grounding / cable-tray / heat-tracing rows; full matrix population requires the workbook source — TBD).
- Source-supported equipment and design-criteria record (the references and verification map in this Specification).

All four `four-documents` artifacts (`Datasheet.md`, `Specification.md`, `Guidance.md`, `Procedure.md`) shall be present.
