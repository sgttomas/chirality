# Specification — DEL-100-02 Package Datasheet (PKG-100 Hydrogen Peroxide Sweetening Unit)

> Normative requirements for the Package Datasheet deliverable.
> Source key: see `Datasheet.md` References.

## Scope

### In Scope

This deliverable specifies the **content and structure** of the EPC Integrator Package Datasheet for `PKG-100 Hydrogen Peroxide Sweetening Unit`. The Package Datasheet must contain the technical data required for third-party Package Vendor engineering, design, and equipment-package development of the sour-water H2O2 treatment package, and must carry the package interface facts as evidence.

Covered scope items (from `DEL-REG`):
- `SOW-0107`
- `SOW-0108`
- `SOW-0109`
- `SOW-0110`

Supported objectives (from `DEL-REG`):
- `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` — ASSUMPTION (best-effort mapping per `OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC`; package-grouped objective mapping).

### Out of Scope

- Vendor-internal engineering choices not constrained by the datasheet.
- Downstream produced-water pipeline design and installation downstream of the facility tie-in (by others — `DBM` line 216).
- Detailed construction installation steps (those belong to `DEL-100-03_construction-work-package`).
- Vendor document register, submittals, turnover records (those belong to `DEL-100-05_vendor-document-turnover-package`).
- Vendor package acceptance and review (that belongs to `DEL-100-06_epc-vendor-package-review-and-acceptance`).

## Requirements

| ID | Requirement | Source |
|---|---|---|
| R-01 | The Package Datasheet shall identify the package by tag `26020-03-PT-27-001` and name "Hydrogen Peroxide Sweetening Unit". | FACT — `PKG-REG` |
| R-02 | The Package Datasheet shall describe the package process function (sour water → static mixer → H2O2 reactors → produced-water tanks; H2O2 injected from H2O2 tank by H2O2 pumps). | FACT — `PKG-REG`; `DBM` lines 214, 216 |
| R-03 | The Package Datasheet shall list the package equipment constituents: Hydrogen Peroxide Pumps, Hydrogen Peroxide Reactors, and Static Mixer. | FACT — `PKG-REG` package scope |
| R-04 | The Package Datasheet shall record per-equipment design data (capacity, design P/T, materials, MOC, drivers, electrical class). Values not yet established shall be marked `TBD`. | ASSUMPTION — convention for EPC package datasheets; explicit per-equipment design data not stated in accessible source. |
| R-05 | The Package Datasheet shall record package throughput. Current basis: 3,840 m3/d (`TBC` per `DBM`). | FACT — `DBM` line 427 |
| R-06 | The Package Datasheet shall record site/environmental design conditions: elevation 673 m AMSL; design ambient -40 °C to +35 °C. | FACT — `DBM` SEC-11 |
| R-07 | The Package Datasheet shall enumerate all applicable interfaces, using the 13 interface types recorded for `PKG-100` in `IFC-REG`. | FACT — `IFC-REG` |
| R-08 | The Package Datasheet shall declare for each interface the boundary (battery limit), the responsible party on each side, and the handoff conditions (flange / terminal / connection). Values not yet defined shall be marked `TBD`. | ASSUMPTION — required to satisfy the "package interface requirements matrix" anticipated artifact (`DEL-REG`). |
| R-09 | The Package Datasheet shall record the responsibility split: Package Vendor owns package engineering, design, vendor documentation, and physical equipment; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, and procurement/construction coordination. | FACT — `PKG-REG` |
| R-10 | The Package Datasheet shall cite the source basis for the package: Workbook Packages row 63; `26020-Package_Requirements.docx` package heading 52; RFQ `26020-03-PT-RFQ-27-001-H202_Sweet_Unit.docx`. | FACT — `PKG-REG`; `DEL-REG`; `_CONTEXT.md` |
| R-11 | The Package Datasheet shall flag any value carried `TBC`/`TBD` in upstream sources and shall not invent values. | FACT (governance) — Chirality K-PROV-1 invariant; SKILL source-grounding rule. |
| R-12 | The Package Datasheet shall include a clear allocation of the H2O2 storage tank (1 × 400 bbl) as inside or outside the package vendor boundary. Current accessible source treats it as a 03-25 facility chemical-system tank (`DBM` lines 216, 428); package scope per `PKG-REG` lists pumps, reactors, static mixer only. | FACT (conflict) — see Guidance Conflict Table CT-01. |
| R-13 | The Package Datasheet shall align hazardous-area, fire & gas, EHT, grounding/bonding, area lighting, and HVAC interface requirements to the EPC Integrator facility-level basis rather than the vendor's standalone practice. | ASSUMPTION — derived from the `PKG-REG` responsibility split. |
| R-14 | The Package Datasheet shall preserve units consistent with the DBM (m3/d for throughput; bbl for tankage; °C for temperatures; m for elevation). | FACT — `DBM` |
| R-15 | The Package Datasheet shall be a Gate 5 EPC anchor deliverable and shall be issued before vendor engineering proceeds (`DEL-100-04`). | ASSUMPTION (sequencing) — derived from "Mandatory Gate 5 EPC anchor deliverable" note in `DEL-REG`. |

## Standards

| Standard | Applicability | Location |
|---|---|---|
| Package Requirements (project-internal) | Governing for package data content | `26020-Package_Requirements.docx` heading 52 — location TBD (binary, not locally text-accessible) |
| Sour-water H2O2 RFQ basis | Governing for service definition and vendor scope | `26020-03-PT-RFQ-27-001-H202_Sweet_Unit.docx` — location TBD (not present under `_Sources`) |
| API-650 Modified | Atmospheric tank design basis (referenced for produced-water tanks; potentially relevant to H2O2 tank) | `DBM` produced-water tank passage |
| Hazardous area classification basis | Facility-level basis governs package | `DBM` SEC-11 (generic reference) |
| ASSUMPTION: standard process-package codes (ASME B31.3, ASME BPVC, applicable electrical area-classification standards) | Likely applicable | location TBD; not explicit in accessible sources |

## Verification

| Requirement | Verification Approach |
|---|---|
| R-01 to R-03, R-09, R-10 | Document review against `PKG-REG`, `DEL-REG`, and `_CONTEXT.md`. |
| R-04 | Document review: each equipment row has a complete-or-`TBD` field set. |
| R-05, R-06, R-14 | Document review against `DBM` source slices; unit check. |
| R-07 | Cross-check the 13 interfaces in the datasheet against `IFC-REG` rows for `PKG-100`. |
| R-08 | Document review: each interface row has boundary, party-each-side, and handoff fields. |
| R-11 | Lint pass for unsourced numeric values; every non-trivial value carries a source citation or `TBD`. |
| R-12 | Conflict Table entry CT-01 ruling captured. |
| R-13 | Interface requirements traced to facility-level basis (`DBM` SEC-11 and equivalent) or to `TBD`. |
| R-15 | `_STATUS.md` sequencing check vs. `DEL-100-04`. |

## Documentation

The following artifacts must result (anticipated artifacts from `_CONTEXT.md` and `DEL-REG`):

- Package technical datasheet (this deliverable's core artifact)
- Vendor engineering handoff basis
- Package interface requirements matrix (the 13 PKG-100 interfaces, with battery limits)
- Source-supported equipment and design criteria summary

Each artifact must cite its source slices and surface remaining `TBD`s for human ruling.
