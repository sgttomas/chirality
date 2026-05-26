# Datasheet — DEL-086-04 Vendor Engineered Equipment Package

Status labels: `FACT` cites a locally accessible source slice; `ASSUMPTION` is a labeled inference; `TBD` marks unknowns; `location TBD` means source named but slice not locally accessible.

## Identification

| Field | Value | Provenance |
|---|---|---|
| Deliverable ID | `DEL-086-04_vendor-engineered-equipment-package` | `_CONTEXT.md` Identity |
| Name | Vendor Engineered Equipment Package | `_CONTEXT.md` |
| Parent Package | `PKG-086` — Flare Stack (Low Pressure) | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 59 |
| Workbook Row | 59 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| WBS | 02 | `PACKAGE_REGISTER.csv` row 59 |
| Equipment Tag (package) | 26020-02-PT-25-002 — Flare Stack (Low Pressure) | `PACKAGE_REGISTER.csv` row 59 (PackageEquipmentTag) |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 59 |
| Type | Vendor Package Production Unit | `_CONTEXT.md` |
| Responsible Party | Package Vendor (engineering/design/equipment) with EPC Integrator integration review | `_CONTEXT.md` |
| Covers Scope Items | `SOW-0091`, `SOW-0092`, `SOW-0093`, `SOW-0094` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supports Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION: PACKAGE_HEURISTIC association) | `_CONTEXT.md`; PACKAGE_HEURISTIC per skill |

## Attributes

| Attribute | Value | Provenance |
|---|---|---|
| Service | Low-pressure relief, blowdown, and vent disposal for the 03-25 facility; receives TEG regeneration, VRU, and compressor seal-pot services | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §Flare and Blowdown, line 499 (FACT) |
| Configuration | LP element of an HP/Cryo and LP dual flare stack arrangement; shared-interface system between 03-25 and 04-25 with open service-split allocation | Same source, lines 56, 497 (FACT) |
| Associated LP flare stack blower | In package scope (reference/interface package per PACKAGE_REGISTER row 59 RationaleNotes) | `PACKAGE_REGISTER.csv` row 59 RationaleNotes (FACT) |
| LP relief header size | 508 mm / 20 in (carried in current source basis) | DBM line 499 (FACT) |
| LP stack OD | TBD | DBM line 499 explicitly states "LP stack OD remains TBD" (FACT — TBD in source) |
| LP stack height | TBD | Not stated in accessible sources |
| LP KO drum | V-3900-2 (upstream interface; not in this package's scope but a defined downstream tie-in) | DBM line 499 (FACT) |
| LP KO drum transfer pump | P-3900-2, 1 × 100% (upstream interface) | DBM lines 499, 584 (FACT) |

## Conditions

| Parameter | Value | Provenance |
|---|---|---|
| Design pressure (stack) | TBD | Not stated in accessible sources; final flare studies pending |
| Design temperature (stack) | TBD | Not stated in accessible sources |
| Relief load basis | Staggered blowdown is required to limit maximum relief | DBM line 501 (FACT) |
| Blowdown philosophy | Per W242510-PRC-REP-000003-001 Plant Shutdown and Blowdown Philosophy (location TBD; document named but not locally available) | DBM line 501 |
| Materials of construction | TBD; sour-service requirements apply where streams contain H2S | DBM lines 605–611 §Isolation/§Mechanical (FACT — sour service general); specific stack materials TBD |
| Sour-service classification | Applicable; LP services include sour streams via TEG regen and seal-pot routing | DBM lines 499, 607 (ASSUMPTION based on service list) |
| Site environmental loads (wind/snow/seismic/frost) | Per current geotechnical and civil design criteria | DBM line 700 (FACT — general requirement); specific values TBD |

## Construction

| Item | Description | Provenance |
|---|---|---|
| Stack type | Self-supported dual flare stack referenced as budgetary pricing/delivery go-by only | `PACKAGE_REGISTER.csv` row 59 ApplicableSourceMaterials (Bid Docs/Budgetary/24292-02-PT-ENR-25-201_Self Supported Dual Flare Stack_R1.pdf) — location TBD (FACT — referenced; not locally readable) |
| Burner tip | TBD | Not stated in accessible sources |
| Pilot/ignition system | TBD | Not stated in accessible sources |
| Knock-out drum (LP KO) | V-3900-2 — interface; downstream of stack header system | DBM line 499 (FACT) |
| Foundation | Equipment-specific foundation and anchorage check required for flare/stack elements per current geotechnical report | DBM line 700 (FACT — requirement) |
| Skid/structural | Vendor scope; details TBD | ASSUMPTION (typical vendor package practice) |
| Shipped-loose items | Vendor document register to include shipped-loose item list | DBM line 617 (FACT — requirement) |
| Coatings/insulation | TBD | Not stated in accessible sources |
| Heat tracing / HVAC / fire & gas | Coordinated with civil, electrical, controls, instrumentation sections | DBM line 619 (FACT) |

## Interface Summary (read-only context from PACKAGE_REGISTER)

Applicable interface types for PKG-086: Utility Piping; Relief/Flare/Vent; Drain/Containment; Electrical Power; Grounding/Bonding; I&C / Control Cabling; Fire & Gas / Safety Systems; Structural / Foundations / Supports. (`PACKAGE_REGISTER.csv` row 59 InterfaceTypes — FACT)

## References

- `_CONTEXT.md` (deliverable identity)
- `_REFERENCES.md` (reference index)
- `DELIVERABLE_REGISTER.csv` row for `DEL-086-04_vendor-engineered-equipment-package` (GATE-07 snapshot)
- `PACKAGE_REGISTER.csv` row 59 (GATE-07 snapshot)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (locally accessible)
- `26020-Package_Requirements.docx` package heading 39 — referenced; .docx text not locally extracted (location TBD)
- `Bid Docs/Budgetary/brief.md` — Word Source Basis per row 59 (location TBD)
- `Bid Docs/Budgetary/24292-02-PT-ENR-25-201_Self Supported Dual Flare Stack_R1.pdf` — budgetary go-by only (location TBD)
- `W242510-PRC-REP-000003-001` Plant Shutdown and Blowdown Philosophy (location TBD)
