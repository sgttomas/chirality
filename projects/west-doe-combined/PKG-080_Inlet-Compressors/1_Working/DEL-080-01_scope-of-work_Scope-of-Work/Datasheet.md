# Datasheet — DEL-080-01 Scope of Work (PKG-080 Inlet Compressors)

> Descriptive datasheet for the EPC Integrator Scope of Work deliverable for the
> Inlet Compressors package (PKG-080). Populated from `_CONTEXT.md`,
> `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `SCOPE_LEDGER.csv`, and
> the locally accessible DBM source slice
> `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (SEC-04, SEC-05).

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-080-01_scope-of-work` | `_CONTEXT.md` |
| Deliverable Name | Scope of Work | `_CONTEXT.md` |
| Parent Package ID | `PKG-080` | `_CONTEXT.md` |
| Parent Package Name | Inlet Compressors | `_CONTEXT.md` |
| Parent Workbook ID | 80 (Workbook Packages row 66) | `PACKAGE_REGISTER.csv` |
| Package Tracking No. | `26020-02-PT-12-001` (Inlet Compressors) | `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `_CONTEXT.md` |
| WBS | 02 | `PACKAGE_REGISTER.csv` |
| Type | EPC Scope of Work | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Covers Scope Items | SOW-0119, SOW-0120, SOW-0121, SOW-0122 | `_CONTEXT.md`, `SCOPE_LEDGER.csv` |
| Supports Objectives | OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 | `_CONTEXT.md` (PACKAGE_HEURISTIC; ASSUMPTION) |
| Authoritative decomposition snapshot | GATE-07_Final_Published_2026-05-24 | `_REFERENCES.md` |

## Attributes (Package Identity and Function)

| Attribute | Value | Source |
|---|---|---|
| Package function | Two identical parallel sour inlet gas reciprocating compressor packages compressing Doe field sour gas for export to 04-25 inlet gathering | `SCOPE_LEDGER.csv` SOW-0120; DBM SEC-05 Inlet Compression Overview |
| Configuration | 2 x 50 percent, no installed spare | DBM SEC-05 Inlet Compression Overview |
| Per-unit capacity | 40 MMSCFD | DBM SEC-05; SCOPE_LEDGER SOW-0122 |
| Total facility capacity | 80 MMSCFD (2,264 e3m3/d) | DBM Facility Overview; SEC-05 |
| Compressor type | Two-stage separable reciprocating | DBM SEC-05 |
| Preliminary model | Ariel KBC/6, TBC (decomposition row carries "KBZ/6" — see Guidance Conflict Table C-01) | DBM SEC-05; SCOPE_LEDGER SOW-0121 (CONFLICT) |
| Cylinder arrangement | Three first-stage cylinders, three second-stage cylinders | DBM SEC-05 |
| Driver | Electric motor, 5,200 hp / 3,878 kW, 4,000 V, 3-phase, 60 Hz, ~891 rpm 8-pole, NEMA MG1, TEFC or WPII, Class F insulation / Class B rise, continuous inverter-duty, starting VFD (SCA-001 VE #34) | DBM SEC-05 Electric Driver and Starting Basis |
| Modularization | Shop-assembled, disassembled into three pieces for transport, installed in self-framing buildings | DBM SEC-05; SCOPE_LEDGER SOW-0121 |
| Major included equipment (per package) | Suction scrubbers (cyclonic 1st stage; vertical mesh/vane 2nd stage), intercooler and aftercooler (aerial), recycle valve, packing drain/vent seal pot, package piping, instrumentation, electrical, HVAC, package auxiliaries | DBM SEC-05; SCOPE_LEDGER SOW-0121 |
| Tagged unit tags | KM-2150, KM-2250 (governed by SCA-001 VE #34 for starting basis) | DBM SEC-05 Electric Driver and Starting Basis |
| Materials | NACE-compliant materials and seals (sour service) | SCOPE_LEDGER SOW-0122 |

## Conditions (Process Design Basis)

| Parameter | Value | Source |
|---|---:|---|
| Service | Sour natural gas (~0.296 mol% H2S in compressor composition) | DBM SEC-05 Compression Design Conditions |
| 1st-stage suction pressure (low / normal / design / MAWP) | 125 / 165 / 165 / 653 psig | DBM SEC-05 |
| 1st-stage discharge pressure (normal / design / MAWP) | 380 / 380 / 653 psig | DBM SEC-05 |
| 2nd-stage suction pressure (normal / design / MAWP) | 375 / 375 / 653 psig | DBM SEC-05 |
| 2nd-stage discharge pressure (normal / design / MAWP) | 800 / 800 / 1,350 psig | DBM SEC-05 (SCA-002 supersession) |
| 1st-stage suction temperature (low / high / max) | 4 / 15 / 48 deg C | DBM SEC-05 |
| Cooler outlet temperatures (1st & 2nd stage) | 43.3 deg C | DBM SEC-05 Scrubbers, Coolers, Recycle, Purge |
| Discharge pressure governing basis | Fixed at 800 psig per SCA-002 (supersedes prior 650–800 psig) | DBM SEC-05 |
| Suction-source pressure / temperature (facility inlet) | 1,275 kPag suction, 6,550 kPag discharge (decomposition summary; consistent with DBM kPa values when converted from psig); inlet temperature 8.3 deg C facility feed | SCOPE_LEDGER SOW-0122; DBM SEC-04 |

> Unit-system note: SCOPE_LEDGER SOW-0122 uses kPag (1275 / 6550); DBM SEC-05
> uses psig (165 / 800). Values are directionally consistent (~165 psig ≈ 1138
> kPag at suction; ~800 psig ≈ 5516 kPag at discharge). The discrepancy between
> SCOPE_LEDGER kPa values and DBM psig values is recorded in the Guidance
> Conflict Table (C-02) for human ruling.

## Construction (Scope Boundaries and Responsibility Split)

| Item | EPC Integrator (this deliverable) | Package Vendor | Source |
|---|---|---|---|
| Package engineering, package design, vendor documentation, physical equipment package | — | Owned | `PACKAGE_REGISTER.csv` PKG-080 |
| Facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination | Owned | — | `PACKAGE_REGISTER.csv` PKG-080 |
| Applicable interface types (EPC owns at the package boundary) | Process Piping; Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; EHT; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Building HVAC/Services; Fire & Gas/Safety Systems; Maintenance Access; Structural/Foundations/Supports | Internal to package skid/building scope | `PACKAGE_REGISTER.csv` PKG-080 |
| Inlet pressure-control / recycle / purge interfaces | Tie-in coordination; sweet-gas purge from fuel-gas system; packing drain/vent routing to VRU suction and vacuum pump interface | Recycle valve hardware and package failure-action definition (TBC) | DBM SEC-04, SEC-05 |
| Sour-gas export | Tie-in to 04-25 inlet gathering downstream of TEG dehydration | — | DBM SEC-04 Sour-Gas Export; SEC-05 |
| Tagged equipment | KM-2150, KM-2250 (two compressor packages); package number 26020-02-PT-12-001 | Vendor-supplied skid contents | DBM SEC-05; `PACKAGE_REGISTER.csv` |

## Anticipated Artifacts (this Scope-of-Work deliverable)

- Package scope of work narrative (this document set)
- Tagged equipment and package identity list (Datasheet "Identification" + "Attributes")
- Package function and integration narrative (Specification Scope; Guidance Purpose)
- Responsibility assignment record (Construction table above; Specification Standards/Verification)

Source: `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` row `DEL-080-01_scope-of-work`.

## References

- `_CONTEXT.md` (deliverable identity, scope, anticipated artifacts)
- `_REFERENCES.md` (authoritative decomposition basis, shared source root)
- `_DEPENDENCIES.md` (no declared edges; advisory)
- GATE-07 snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` row `DEL-080-01_scope-of-work`
  - `PACKAGE_REGISTER.csv` row `PKG-080`
  - `SCOPE_LEDGER.csv` rows `SOW-0119`–`SOW-0122`
  - `OBJECTIVE_DELIVERABLE_MAP.csv` (objective association: PACKAGE_HEURISTIC; ASSUMPTION)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — SEC-04 (Inlet/Separation/Export) and SEC-05 (Inlet Compression and TEG Dehydration); locally accessible authoritative source slice
- `26020-Package_Requirements.docx` package heading 33 — referenced by decomposition; binary docx, **location TBD** (not locally accessible as text)
- `Bid Docs/Budgetary/brief.md`, `24292-02-PT-ENR-12-201_Compressors_R2.pdf` — referenced by PACKAGE_REGISTER; **location TBD** (not present in `_Sources/`)
