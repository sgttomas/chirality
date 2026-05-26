# Specification — DEL-050-01_scope-of-work (PKG-050 Stabilizer Overheads Compressors)

## Scope

### In scope (this deliverable)

This deliverable defines the EPC Integrator's authored package Scope of Work for PKG-050 Stabilizer Overheads Compressors. The Scope of Work shall record, for the package as a whole:

- Tagged equipment and package identity (workbook ID, CoA tracking number, WBS, discipline).
- Package basic scope (count, configuration, capacity philosophy).
- Package process function and whole-facility integration narrative.
- Major included equipment basis.
- Source basis (workbook row, Word package heading).
- Boundaries between Package Vendor and EPC Integrator responsibility.
- Applicable interface types declared in the workbook.

Source: `_CONTEXT.md` Scope; ARTIFACT_REGISTER.csv DEL-050-01 rows (ART-AF6ADA74A4, ART-8BA2B0B695, ART-CA258CB1DF, ART-769C18AA16, ART-A06F144C77).

### Out of scope (this deliverable)

- Technical handoff datasheet content (carried in DEL-050-02_package-datasheet — ARTIFACT_REGISTER.csv).
- Construction Work Package (DEL-050-03).
- Vendor Engineered Equipment Package (DEL-050-04).
- Vendor Document Turnover Package (DEL-050-05).
- EPC Vendor Package Review and Acceptance (DEL-050-06).
- Package-specific exclusions: per PACKAGE_REGISTER.csv PKG-050, "TBD; no package-specific exclusions stated in source materials."

## Requirements

REQ identifiers are deliverable-local. Each requirement is source-grounded; ASSUMPTION-labelled items are inferences from the decomposition narrative.

| REQ | Requirement | Source |
|---|---|---|
| REQ-01 | The Scope of Work shall record the package identity as PKG-050 "Stabilizer Overheads Compressors", workbook row 81, CoA tracking 26020-01-12-005, WBS 01, discipline Mechanical. | PACKAGE_REGISTER.csv PKG-050 |
| REQ-02 | The Scope of Work shall record the basic scope: supply of two (2) identical induction-motor-driven separable reciprocating compressor packages, each designed for 100% capacity. | SCOPE_LEDGER.csv SOW-0174 |
| REQ-03 | The Scope of Work shall record the process function: compress and recycle multiple streams from 50 psig to 1100 psig; final discharge routed to amine inlet filter coalescer or recycled to first stage. | SCOPE_LEDGER.csv SOW-0174 |
| REQ-04 | The Scope of Work shall enumerate the major included equipment: Ariel KBC/6 four-stage separable reciprocating compressor; 2700 HP motor (4000 V / 3PH / 60 Hz) with speed control and automated recycle valve, "No Toshiba motors"; forced-air intercooler after each stage on common frame (AP-661 modified) with warm-air recirculation plenum heater and non-sparking bidirectional cooling; 1st-stage two-phase cyclonic scrubber; 2nd/3rd/4th-stage two-phase demister scrubbers; packing vent/drain separation pot (DP 101 kPag); vacuum pump; seal-pot waste-oil transfer pump. | SCOPE_LEDGER.csv SOW-0175 |
| REQ-05 | The Scope of Work shall record the by-others installation scope: shipping packages to site, installation on piles, tie-in piping, electrical connections, mounting platform and stairs. | SCOPE_LEDGER.csv SOW-0176 |
| REQ-06 | The Scope of Work shall record the design capacity per stage (Stage 1 = 2.5 MMSCFD; Stage 2 = 5 MMSCFD; Stage 3 = 17 MMSCFD; Stage 4 = 17 MMSCFD) and 3:1 turndown. | SCOPE_LEDGER.csv SOW-0176 |
| REQ-07 | The Scope of Work shall record the operating pressure/temperature envelope per stage as published in the source extract; values where the source slice is truncated shall be marked TBD. | SCOPE_LEDGER.csv SOW-0176 |
| REQ-08 | The Scope of Work shall record the design temperature envelope (149 °C each-stage suction; 177 °C each-stage discharge), MAWP at 1st-stage suction (1723 kPag), minimum MAWP at final-stage discharge (9101 kPag at 177 °C), and shall mark other MAWP values "TBC" per source. | SCOPE_LEDGER.csv SOW-0176 |
| REQ-09 | The Scope of Work shall enumerate the workbook-declared applicable interface types for PKG-050 (13 interface types: Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports). | INTERFACE_REGISTER.csv PKG-050 |
| REQ-10 | The Scope of Work shall record the responsibility split: Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package; EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | PACKAGE_REGISTER.csv PKG-050 responsibility narrative |
| REQ-11 | The Scope of Work shall cite the source basis: Workbook Packages row 81 and `26020-Package_Requirements.docx` package heading 5; and shall reference the Word Source Basis bid document `26020-01-PT-RFQ-12-005_Stabilizer_OH_Comp.docx`. | PACKAGE_REGISTER.csv PKG-050 |
| REQ-12 | The Scope of Work shall state that no package-specific exclusions are recorded in source (per PACKAGE_REGISTER.csv PKG-050: "TBD; no package-specific exclusions stated in source materials"). | PACKAGE_REGISTER.csv PKG-050 |
| REQ-13 | The Scope of Work shall record the supported objectives at package level (OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010). ASSUMPTION (best-effort mapping): per `OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC`. | OBJECTIVE_DELIVERABLE_MAP.csv / `_CONTEXT.md` Supports Objectives; PACKAGE_REGISTER.csv PKG-050 |
| REQ-14 | The Scope of Work shall not introduce requirements, design values, or work items not anchored in an accessible source slice; unverifiable items shall be marked TBD or escalated via the Conflict Table. | Skill four-documents Authority hierarchy |

## Standards

| Standard / Reference | Applicability | Source / location |
|---|---|---|
| NEMA MG 1 | Motor testing/labelling standard cited for the 2700 HP induction driver | SCOPE_LEDGER.csv SOW-0176 (location in standard: TBD) |
| Ariel KBC/6 vendor design basis | Compressor frame is named in source; vendor design basis governs detailed selection | SCOPE_LEDGER.csv SOW-0175 (vendor document not locally accessible: location TBD) |
| `26020-Package_Requirements.docx` package heading 5 | Authoritative package scope statement | Source file not locally extracted: location TBD |
| Workbook `26020-Packages_Interfaces_4_export.xlsx` row 81 | Authoritative interface and identity row | `_Sources/26020-Packages_Interfaces_4_export.xlsx` — present; specific row read via SCOPE_LEDGER / PACKAGE_REGISTER extracts |
| Project DBM (Comp & Liquids / Deepcut) | Word Source Basis context for compression / liquids | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — present; specific sections TBD |

## Verification

| REQ | Verification approach |
|---|---|
| REQ-01 | Inspection: Scope of Work contains identity table matching PACKAGE_REGISTER.csv PKG-050. |
| REQ-02 | Inspection: basic-scope statement reproduced from SCOPE_LEDGER.csv SOW-0174. |
| REQ-03 | Inspection: process-function narrative reproduced from SOW-0174. |
| REQ-04 | Inspection: equipment list cross-checked line-by-line against SOW-0175. |
| REQ-05 | Inspection: by-others statement reproduced from SOW-0176. |
| REQ-06 | Inspection: capacity / turndown table values match SOW-0176. |
| REQ-07 | Inspection: per-stage P/T table mirrors SOW-0176; truncated source fields explicitly marked TBD. |
| REQ-08 | Inspection: design-envelope and MAWP values reproduced from SOW-0176 with "TBC" preserved. |
| REQ-09 | Inspection: interface enumeration matches INTERFACE_REGISTER.csv PKG-050 (13 IFC- rows). |
| REQ-10 | Inspection: responsibility split reproduced from PACKAGE_REGISTER.csv PKG-050 responsibility narrative. |
| REQ-11 | Inspection: source-basis citations present in Scope of Work. |
| REQ-12 | Inspection: exclusions section states "no package-specific exclusions in source". |
| REQ-13 | Inspection: objective list matches `_CONTEXT.md` Supports Objectives; ASSUMPTION label preserved. |
| REQ-14 | Audit: each non-trivial claim cites a source (`SourcePath` + `SectionRef`) or `location TBD`; no fabricated values. |

## Documentation (Anticipated Artifacts)

From `_CONTEXT.md` Anticipated Artifacts and ARTIFACT_REGISTER.csv (DEL-050-01):

- Package scope of work (ART-AF6ADA74A4)
- Tagged equipment and package identity list (ART-8BA2B0B695)
- Package function and whole-facility integration narrative (ART-CA258CB1DF)
- Package responsibility assignment record (ART-769C18AA16)
- Detailed mechanical package scope extraction evidence (ART-A06F144C77)
