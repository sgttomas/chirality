# Datasheet — DEL-086-02 Package Datasheet (Flare Stack (Low Pressure))

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-086-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package | `PKG-086` — Flare Stack (Low Pressure) | PACKAGE_REGISTER.csv row 59 |
| Vendor Package Tag (parent) | `26020-02-PT-25-002` — Flare Stack (Low Pressure) | PACKAGE_REGISTER.csv row 59 |
| Workbook Row | 59 | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| WBS Area | 02 (3-25 facility) | PACKAGE_REGISTER.csv row 59 |
| Discipline | Mechanical | `_CONTEXT.md` |
| Deliverable Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Scope Items Covered | SOW-0091, SOW-0092, SOW-0093, SOW-0094 | `_CONTEXT.md` |
| Objectives Supported (PACKAGE_HEURISTIC) | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (ASSUMPTION: package-grouped mapping) | `_CONTEXT.md` |

## Attributes (package equipment list and key facts)

| Item | Tag / Value | Source |
|---|---|---|
| LP flare stack | TBD — stack tag not stated in accessible source slices | TBD (location TBD: `26020-Package_Requirements.docx` package heading 39; not locally parsed) |
| LP flare stack blower | TBD — blower tag not stated in accessible source slices | TBD (location TBD: same as above) |
| Package quantity (stacks) | 1 LP flare stack (ASSUMPTION: single stack per facility based on PACKAGE_REGISTER scope statement) | PACKAGE_REGISTER.csv row 59 (scope statement) |
| Package quantity (blowers) | 1 LP flare stack blower (ASSUMPTION) | PACKAGE_REGISTER.csv row 59 |
| Stack configuration | Part of the HP/Cryo and LP dual flare stack arrangement at/associated with 03-25, shared with 04-25 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` §"Flare and Blowdown" (line 497) |
| LP relief header size (basis) | 508 mm / 20 in | DBM §"Flare and Blowdown" (line 499) |
| Companion HP/Cryo stack reference dimensions | 660 mm OD x 60,957 mm tall (HP/Cryo sonic stack only; LP stack OD remains TBD per source) | DBM §"Flare and Blowdown" (line 499) |
| LP stack OD | TBD | DBM §"Flare and Blowdown" (line 499) explicitly states "LP stack OD remains TBD" |
| LP stack height | TBD | TBD (not stated in accessible sources) |
| LP flare services received | TEG regeneration, VRU, and compressor seal-pot services | DBM §"Flare and Blowdown" (line 499) |
| Upstream LP KO drum | `V-3900-2` (out of scope for this package; covered by `PKG-082`) | DBM §"Flare and Blowdown" (line 499) |
| Upstream LP KO drum transfer pump | `P-3900-2` to slop (out of scope) | DBM §"Flare and Blowdown" (line 499); §pump count table (line 584) |
| Equipment design margin (vessels) | 10 percent on flow (discipline-level starting basis; validate vs vendor) | DBM §"Equipment Design Margins" (ASSUMPTION: stack/blower sizing margins follow same discipline basis) |

## Conditions (process/design conditions)

| Parameter | Value | Source |
|---|---|---|
| Service | LP flare burn / vent (low-pressure relief disposal); blower-assisted | DBM §"Flare and Blowdown" (line 499) |
| Stack mechanical design pressure | TBD | TBD (not in accessible DBM section) |
| Stack mechanical design temperature | TBD | TBD |
| Operating pressure (header inlet to stack) | TBD | TBD |
| Operating temperature | TBD | TBD |
| Relief load / blowdown load to LP flare | TBD — requires final flare studies and Plant Shutdown and Blowdown Philosophy `W242510-PRC-REP-000003-001` (not locally accessible) | DBM §"Flare and Blowdown" (line 501); §"Emissions Basis" |
| Staggered blowdown requirement | Required to limit maximum relief | DBM §"Flare and Blowdown" (line 501) |
| Wind / snow / seismic / frost design criteria | TBD — to be set by geotechnical and site civil criteria | DBM §"Foundations" (line 700) |
| Sour service / NACE applicability | ASSUMPTION: applicable on inlet relief side based on facility isolation philosophy; confirm via process/HAZOP | DBM §isolation philosophy (line 607) |
| Blower capacity / motor rating | TBD | TBD |
| Pilot fuel gas demand and reliability basis | TBD | TBD |
| Emissions / permit values | TBD — see DBM emissions note | DBM §"Emissions Basis" (line 555) |

## Construction (mechanical and interface construction facts)

| Item | Basis | Source |
|---|---|---|
| Applicable interface types | Utility Piping; Relief / Flare / Vent; Drain / Containment; Electrical Power; Grounding / Bonding; I&C / Control Cabling; Fire & Gas / Safety Systems; Structural / Foundations / Supports | PACKAGE_REGISTER.csv row 59 |
| Foundations / anchorage | Equipment-specific foundation and anchorage checks required for tall vessels and flare/stack-class elements | DBM §"Foundations" (line 700) |
| Material selection | TBD pending design conditions, service classification, and sour-service confirmation | TBD |
| Stack support type | TBD — source budgetary go-by (`Bid Docs/Budgetary/24292-02-PT-ENR-25-201_Self Supported Dual Flare Stack_R1.pdf`) named in PACKAGE_REGISTER but is a "budgetary pricing/delivery go-by only" and is not locally accessible | PACKAGE_REGISTER.csv row 59 (Source Basis) |
| Heat tracing / EHT | TBD — likely limited to liquid drain lines if any | TBD |
| Vendor documentation register | Per `DEL-086-05` (Vendor Document Turnover Package) | DELIVERABLE_REGISTER.csv (DEL-086-05 row) |
| Package responsibility split | Package Vendor owns package engineering/design/documentation/equipment; EPC Integrator owns facility integration, interfaces, tie-ins, constructability | PACKAGE_REGISTER.csv row 59 |
| Shared-facility split between 03-25 and 04-25 | LP flare stack is part of the HP/Cryo + LP dual flare system shared with 04-25; exact service split and owner interface carried as open interface item | DBM §3.1 cross-facility shared utilities (line 56) |

## References

- `_CONTEXT.md` (deliverable identity, scope)
- `_REFERENCES.md` (authoritative basis pointers)
- PACKAGE_REGISTER.csv row 59 — `PKG-086` (GATE-07 snapshot)
- DELIVERABLE_REGISTER.csv — `DEL-086-02` row (GATE-07 snapshot)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — primary accessible source slice (§"Flare and Blowdown" lines 495-501; §"Equipment Design Margins"; §"Pump Counts" line 584; §isolation philosophy line 607; §"Foundations" line 700; §"Emissions Basis" line 555)
- Inaccessible (recorded as missing):
  - `26020-Package_Requirements.docx` package heading 39 — referenced but binary not parsed in this run.
  - `26020-Packages_Interfaces_4_export.xlsx` — referenced but binary not parsed in this run.
  - `Bid Docs/Budgetary/brief.md` and `Bid Docs/Budgetary/24292-02-PT-ENR-25-201_Self Supported Dual Flare Stack_R1.pdf` — not in workspace `_Sources/` tree (budgetary go-by only per PACKAGE_REGISTER).
  - `W242510-PRC-REP-000003-001` (Plant Shutdown and Blowdown Philosophy) — not in workspace.
