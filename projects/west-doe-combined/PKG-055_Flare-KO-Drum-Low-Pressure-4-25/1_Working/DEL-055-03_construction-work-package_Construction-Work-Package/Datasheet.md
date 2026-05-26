# Datasheet: DEL-055-03 — Construction Work Package (LP Flare KO Drum, 4-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-055-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable Name | Construction Work Package | `_CONTEXT.md` |
| Parent Package | `PKG-055` — Flare KO Drum (Low Pressure) 4-25 | `_CONTEXT.md`; PACKAGE_REGISTER.csv row PKG-055 |
| Package Tag (vendor) | 26020-01-PT-17-003 — Flare KO Drum (LP) | PACKAGE_REGISTER.csv row PKG-055 |
| Facility | West Doe Deepcut Expansion (4-25) | DBM-Deepcut/4-25_Deepcut_DBM.md Sec. 1 (lines 5-16) |
| Site | LSD 04-25-80-15W6, ~22.2 km N of Dawson Creek, BC | DBM-Deepcut/4-25_Deepcut_DBM.md Sec. 1 (line 7) |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | EPC Construction Work Package | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Status (start of run) | OPEN | `_STATUS.md` |

## Attributes (Package Equipment Covered by this Work Package)

| Tag | Equipment | Service | Source |
|---|---|---|---|
| V-3900-1 | L.P. Flare K.O. Drum | LP flare knock-out drum | DBM-Deepcut/4-25_Deepcut_DBM.md line 2581 (Equipment List) |
| P-3900-1 | L.P. Flare K.O. Drum Transfer Pump | LP KO drum liquid transfer / truck-out | DBM-Deepcut/4-25_Deepcut_DBM.md line 2580 (Equipment List); Sec. on Flare Systems line 2029 |
| Package quantity | One (1) LP flare KO drum and one (1) LP flare KO drum transfer pump | PACKAGE_REGISTER.csv row PKG-055 |

## Conditions (Integration & Tie-in Context)

| Attribute | Value | Source |
|---|---|---|
| LP flare relief header size | 508 mm (20 in) | DBM-Deepcut/4-25_Deepcut_DBM.md line 2029 |
| LP element configuration | Piggy-back on common HP/cryo flare stack | DBM-Deepcut/4-25_Deepcut_DBM.md line 2029 |
| Services tied to LP flare | Amine regeneration, TEG regeneration, VRU, reciprocating compressor seal pot, primary seal vent, contaminated mole-sieve regen-gas blowdown, VRU suction header bypass | DBM-Deepcut/4-25_Deepcut_DBM.md lines 1702, 1781, 1787, 1801, 2029 |
| LP KO drum pump destination | Truck-out provided; LP-header pump return is also routed to condensate slop tank low-pressure header | DBM-Deepcut/4-25_Deepcut_DBM.md lines 1665, 2029 |
| LP header freeze protection | LP/HP flare headers outside heated buildings to be electrically heat traced and insulated (except PSV outlets that free-drain to header) | DBM-Deepcut/4-25_Deepcut_DBM.md line 2033 |
| Flare/KO drum minimum spacing from vegetation or other fire hazards | 10 m (32 ft) | DBM-Deepcut/4-25_Deepcut_DBM.md line 287 (OGAOM Sec. 9.6.15) |
| Pilot/purge fuel gas to LP stack | TBC; published source-level emissions estimate exists | DBM-Deepcut/4-25_Deepcut_DBM.md lines 1892, 2250-2251 |
| Relief volumes / backpressure | TBD pending detailed design Aspen Flare System Analyzer modelling | DBM-Deepcut/4-25_Deepcut_DBM.md lines 1834, 2021 |
| LP stack element OD | TBD | DBM-Deepcut/4-25_Deepcut_DBM.md lines 1834, 2031 |
| Shared 03-25 / 04-25 allocation | TBD | DBM-Deepcut/4-25_Deepcut_DBM.md line 1834 |

## Construction (Scope Items Covered)

| SOW ID | Source |
|---|---|
| SOW-0083 | DELIVERABLE_REGISTER.csv row DEL-055-03 |
| SOW-0084 | DELIVERABLE_REGISTER.csv row DEL-055-03 |
| SOW-0085 | DELIVERABLE_REGISTER.csv row DEL-055-03 |
| SOW-0086 | DELIVERABLE_REGISTER.csv row DEL-055-03 |

ASSUMPTION (package-grouping heuristic): The four SOW IDs above are listed against DEL-055-03 in the deliverable register but the underlying SOW line items themselves were not opened in this run (no SOW register file was read). Detailed SOW text is `TBD` pending review of the project Scope of Work register.

Anticipated artifacts (from `_CONTEXT.md`):

- Construction work package
- Installation and tie-in workface plan
- Construction interface and turnover checklist

## Applicable Interface Types (from package register)

Process Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports. — Source: PACKAGE_REGISTER.csv row PKG-055.

## References (sources used)

- `_CONTEXT.md` — deliverable identity, scope, anticipated artifacts.
- `_REFERENCES.md` — reference index.
- `_DEPENDENCIES.md` — no declared upstream/downstream at PREPARATION; treated as advisory.
- GATE-07 Final Published snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` — row DEL-055-03
  - `PACKAGE_REGISTER.csv` — row PKG-055
  - `OBJECTIVE_DELIVERABLE_MAP.csv` — DEL-055-03 supports OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — primary locally accessible source (Sections on Flare Systems, Flare/Incinerator Spacing, Equipment List).
- Inaccessible: `26020-Package_Requirements.docx` package heading 10 (not converted to local markdown); content depending solely on it remains `TBD`.

## Open Items / TBD

- Detailed equipment specifications for V-3900-1 and P-3900-1 (dimensions, design pressure/temperature, materials) — `TBD`; expected in DEL-055-02 (Package Datasheet) and DEL-055-04 (Vendor Engineered Equipment Package).
- LP stack element OD; relief volumes; LP pilot/purge gas rates; air-assist basis; shared 03-25/04-25 LP flare allocation — `TBD` (DBM lines 1834, 2031).
- Word source (`26020-Package_Requirements.docx`) heading 10 content — `location TBD`; not locally accessible in this run.
