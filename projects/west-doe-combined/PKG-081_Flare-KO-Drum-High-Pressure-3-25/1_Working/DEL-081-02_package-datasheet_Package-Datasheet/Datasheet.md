# Datasheet — DEL-081-02 Package Datasheet (Flare KO Drum (High Pressure) 3-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-081-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package | `PKG-081` — Flare KO Drum (High Pressure) 3-25 | PACKAGE_REGISTER.csv row 54 |
| Vendor Package Tag (parent) | `26020-02-PT-17-001` — Flare KO Drum (High Pressure) | PACKAGE_REGISTER.csv row 54 |
| Workbook Row | 54 | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| WBS Area | 02 (3-25 facility) | PACKAGE_REGISTER.csv row 54 |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Scope Items Covered | SOW-0071, SOW-0072, SOW-0073, SOW-0074 | `_CONTEXT.md` |
| Objectives Supported (PACKAGE_HEURISTIC) | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION: package-grouped mapping) | `_CONTEXT.md` |

## Attributes (package equipment list and key facts)

| Item | Tag / Value | Source |
|---|---|---|
| HP flare KO drum (compressor area) | V-4100-2 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §"Flare and Blowdown" (line 497) |
| HP flare KO drum (tank farm) | V-4150-2 | DBM §"Flare and Blowdown" (line 497) |
| HP flare KO drum transfer pump (per drum, 1 x 100%) | P-4100-2 | DBM §"Flare and Blowdown" (line 497); §pump count table (line 583) |
| HP flare KO drum transfer pump (per drum, 1 x 100%) | P-4150-2 | DBM §"Flare and Blowdown" (line 497); §pump count table (line 583) |
| Package quantity (drums) | 2 HP flare KO drums | PACKAGE_REGISTER.csv row 54 (scope statement) |
| Package quantity (pumps) | 2 dedicated transfer pumps | PACKAGE_REGISTER.csv row 54 |
| HP relief header size (basis) | 508 mm / 20 in | DBM §"Flare and Blowdown" (line 499) |
| Liquid disposition from pumps | Truck-out or transfer to slop | DBM §"Flare and Blowdown" (line 497) |
| Manifolded to | HP/Cryo and LP dual flare stack (HP flare side); shared with 04-25 | DBM §"Flare and Blowdown" (line 497) |
| Equipment design margin (vessels) | 10 percent on flow (discipline-level starting basis; validate vs vendor) | DBM §"Equipment Design Margins" |

## Conditions (process/design conditions)

| Parameter | Value | Source |
|---|---|---|
| Service | HP flare relief liquid knockout, sour hydrocarbon service possible | DBM §"Flare and Blowdown"; §isolation philosophy (line 607) |
| Design pressure | TBD (location TBD — not in accessible DBM section; expected in budgetary go-by `Bid Docs/Budgetary/24292-02-PT-ENR-17-201_HP FKOD_R2.pdf`, not locally accessible) | TBD |
| Design temperature | TBD (location TBD; same source as above) | TBD |
| Operating pressure | TBD | TBD |
| Operating temperature | TBD | TBD |
| Relief load / blowdown load | TBD — requires final flare studies and Plant Shutdown and Blowdown Philosophy `W242510-PRC-REP-000003-001` (not locally accessible) | DBM §"Flare and Blowdown" (line 501); §"Emissions Basis" |
| Staggered blowdown requirement | Required to limit maximum relief | DBM §"Flare and Blowdown" (line 501) |
| Sour service / NACE applicability | ASSUMPTION: applicable based on isolation philosophy language; confirm via process simulation/HAZOP | DBM §isolation philosophy (line 607) |
| Vessel sizing | TBD — set by flare relief studies | TBD |
| Drum elevation / NPSH for transfer pumps | TBD | TBD |

## Construction (mechanical and interface construction facts)

| Item | Basis | Source |
|---|---|---|
| Applicable interface types | Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT (heat tracing); Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports | PACKAGE_REGISTER.csv row 54 |
| Foundations / anchorage | Equipment-specific foundation and anchorage checks required (tall vessels and flare/stack-class elements) | DBM §"Foundations" (line 700) |
| Material selection | TBD pending design pressure/temperature and sour-service confirmation | TBD |
| Heat tracing / EHT | Likely required for liquid lines and instrument lines; specific scope TBD | DBM general; TBD |
| Vendor documentation register | Per `DEL-081-05` (Vendor Document Turnover Package) | DELIVERABLE_REGISTER.csv row 292 |
| Package responsibility split | Package Vendor owns package engineering/design/documentation/equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability | PACKAGE_REGISTER.csv row 54 |

## References

- `_CONTEXT.md` (deliverable identity, scope)
- `_REFERENCES.md` (authoritative basis pointers)
- PACKAGE_REGISTER.csv row 54 — `PKG-081` (GATE-07 snapshot)
- DELIVERABLE_REGISTER.csv row 289 — `DEL-081-02` (GATE-07 snapshot)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — primary accessible source slice (SEC "Flare and Blowdown"; SEC "Equipment Design Margins"; SEC "Pump Counts"; SEC isolation philosophy)
- Inaccessible (recorded as missing):
  - `26020-Package_Requirements.docx` heading 34 — referenced but binary not parsed in this run.
  - `26020-Packages_Interfaces_4_export.xlsx` — referenced but binary not parsed in this run.
  - `Bid Docs/Budgetary/brief.md` and `Bid Docs/Budgetary/24292-02-PT-ENR-17-201_HP FKOD_R2.pdf` — not in workspace `_Sources/` tree.
  - `W242510-PRC-REP-000003-001` (Plant Shutdown and Blowdown Philosophy) — not in workspace.
