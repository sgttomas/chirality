# Datasheet: DEL-081-04 — Vendor Engineered Equipment Package (Flare KO Drum, High Pressure, 3-25)

> Descriptive datasheet for the Package Vendor production unit covering engineering, design, fabrication/supply, and the physical equipment for the high-pressure flare knockout drum package serving the 03-25 (Comp_and_Liquids) facility.

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-081-04_vendor-engineered-equipment-package` |
| Deliverable Name | Vendor Engineered Equipment Package |
| Parent Package | `PKG-081` — Flare KO Drum (High Pressure) 3-25 |
| Parent Workbook | 81 |
| Discipline | Mechanical |
| Deliverable Type | Vendor Package Production Unit |
| Responsible Party | Package Vendor (engineering / design / equipment) with EPC Integrator integration review |
| Covers Scope Items | SOW-0071, SOW-0072, SOW-0073, SOW-0074 |
| Supports Objectives | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION: PACKAGE_HEURISTIC mapping from OBJECTIVE_DELIVERABLE_MAP rows for PKG-081) |

## Attributes (Package Identity)

| Attribute | Value | Source |
|---|---|---|
| Service | High-pressure flare relief knockout (gas/liquid separation upstream of HP/Cryo flare stack) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` SEC titled "Flare and Blowdown" (lines ~495-501) |
| Candidate equipment tag(s) | `V-4100-2` (compressor area) and/or `V-4150-2` (tank farm) — both HP KO drums manifold to the HP flare | Same DBM section; NEEDS_HUMAN_RULING which tag this PKG-081 vendor package supplies |
| Associated transfer pump tag(s) | `P-4100-2` and/or `P-4150-2` (truck-out or transfer to slop), one per KO drum, 1 x 100 percent | DBM SEC-09 sparing table row "HP flare KO drum transfer pumps" (line ~583); DBM "Flare and Blowdown" (line ~497) |
| Upstream collection | HP relief header (508 mm / 20 inch in current source basis) | DBM "Flare and Blowdown" (line ~499) |
| Downstream | HP/Cryo flare stack (sonic, 660 mm OD x 60,957 mm tall) | DBM "Flare and Blowdown" (line ~499) |
| Liquid disposition | Truck-out or transfer to slop via KO drum pump | DBM "Flare and Blowdown" (line ~497) |

## Design Conditions

| Parameter | Value | Source |
|---|---|---|
| Design pressure | TBD — to be set by EPC Package Datasheet (DEL-081-02) consistent with HP flare header design basis | location TBD; upstream DEL-081-02 not yet issued |
| Design temperature (min/max) | TBD | location TBD; upstream DEL-081-02 not yet issued |
| Relief load (rated) | TBD — to be confirmed by final flare studies; staggered blowdown required to limit maximum relief | DBM "Flare and Blowdown" (line ~501); detailed source W242510-PRC-REP-000003-001 not available locally |
| Inlet nozzle size | TBD (consistent with 508 mm / 20 inch HP relief header) | DBM "Flare and Blowdown" (line ~499) |
| Liquid removal performance | TBD — droplet size and separation efficiency to be set by EPC Package Datasheet | location TBD |
| Material of construction | TBD — sour-service classification to be confirmed for the served headers | location TBD |
| Sour service | ASSUMPTION: likely applicable for headers receiving sour streams; confirm against DBM SEC on Materials/Sour Service | DBM SEC-09 / SEC on isolation philosophy (line ~607) |

## Construction

| Item | Value | Source |
|---|---|---|
| Package boundary | Vendor scope ends at battery-limit nozzles defined in EPC Package Datasheet; integration tie-ins by EPC Integrator | ASSUMPTION based on `_CONTEXT.md` ResponsibleParty split |
| Mounting | TBD (skid vs site-erected) — set by Package Datasheet | location TBD |
| Insulation / heat tracing | TBD; line freezing protection per project basis | location TBD |
| Spare philosophy | One transfer pump per KO drum, 1 x 100 percent | DBM SEC-09 sparing table (line ~583) |
| Painting / coating | TBD per project paint specification | location TBD |

## Anticipated Artifacts (deliverables produced under this production unit)

- Vendor engineered physical equipment package (the as-fabricated/as-supplied unit)
- Vendor package design basis and datasheet set
  (Source: `_CONTEXT.md` Anticipated Artifacts)

## References

- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — sections "Flare and Blowdown" and "Sparing Philosophy"
- `_Sources/26020-Package_Requirements.docx` package heading 34 (decomposition row source pointer; .docx text not read in this run — location TBD at clause level)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` — row `DEL-081-04_vendor-engineered-equipment-package`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_DELIVERABLE_MAP.csv` — PKG-081 rows
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- Upstream package documents (not yet issued): DEL-081-01 Scope of Work; DEL-081-02 Package Datasheet
