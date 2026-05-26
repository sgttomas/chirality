# Datasheet — DEL-079-03 Construction Work Package (Instrument Air Building)

> Descriptive identification of the Construction Work Package (CWP) deliverable for the PKG-079 Instrument Air Building package.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-079-03_construction-work-package | _CONTEXT.md |
| Deliverable Name | Construction Work Package | _CONTEXT.md |
| Parent Package | PKG-079 — Instrument Air Building | _CONTEXT.md |
| Workbook Row | 69 | _CONTEXT.md; Workbook Packages row 69 |
| Discipline | Mechanical | _CONTEXT.md |
| Deliverable Type | EPC Construction Work Package | _CONTEXT.md |
| Responsible Party | EPC Integrator | _CONTEXT.md |
| Gate | Gate 5 (EPC anchor) — ASSUMPTION based on `Mandatory Gate 5 EPC anchor deliverable` note in DELIVERABLE_REGISTER | DELIVERABLE_REGISTER.csv row DEL-079-03 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Function | Plant/utility instrument air supply package | SCOPE_LEDGER SOW-0132 (26020-Package_Requirements.docx pkg heading 32 — Basic scope; location TBD) |
| Major Equipment Count | 2 compressors, 1 wet air receiver, 2 dryer pre-filters, 1 regenerative desiccant dryer (2-tower), 1 after-filter, 1 dry air receiver (or two 50%) | SCOPE_LEDGER SOW-0132/0133 |
| Compressor Type | Oil-injected rotary screw, air-cooled | SCOPE_LEDGER SOW-0133 |
| Compressor Rated Capacity (each) | 1113 SCFM at 861 kPag (125 psig) discharge | SCOPE_LEDGER SOW-0133 |
| Driver | 250 HP electric motors, soft starter or VFD ready, anti-condensation space heaters | SCOPE_LEDGER SOW-0133 |
| Motor Electrical | 200-250 HP, 600 V / 3 PH / 60 Hz, TEFC, Non-classified | SCOPE_LEDGER SOW-0134 |
| Dryer Configuration | 100% capacity, 2 tanks/towers (one operating, one regenerating), sized for 2 compressors and leave | SCOPE_LEDGER SOW-0133 |
| Delivered Air Dew Point | -73.3 °C at 1000 kPag (maximum) | SCOPE_LEDGER SOW-0133 |
| PSV Set Pressure | 948 kPag (137.5 psig) | SCOPE_LEDGER SOW-0133 |
| Compressor Max Discharge / Shutdown | 1000 kPag | SCOPE_LEDGER SOW-0134 |
| Maximum System Design Pressure | 1034 kPag (150 psig) | SCOPE_LEDGER SOW-0134 |
| Minimum System Pressure | 551 kPag (80 psig) | SCOPE_LEDGER SOW-0134 |
| Facility Shutdown Pressure | 482 kPag (70 psig) | SCOPE_LEDGER SOW-0134 |
| Design Temperature Range | -40 °C to 38 °C | SCOPE_LEDGER SOW-0134 |
| Package Boundary Owner | Package Vendor (engineering/design/equipment); EPC Integrator (facility integration) | SCOPE_LEDGER SOW-0131 |
| Construction Site Civil Interface | Piles (installation on piles by others noted in SOW) | SCOPE_LEDGER SOW-0134 (By others) |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Ambient design temperature | -40 °C to 38 °C | SCOPE_LEDGER SOW-0134 |
| Compressor cooling medium | Air-cooled | SCOPE_LEDGER SOW-0133 |
| Hazardous area classification | Non-classified (motors) | SCOPE_LEDGER SOW-0134 |
| Site location | TBD (not enumerated in accessible decomposition slice) | TBD |
| Construction season window | TBD | TBD |
| Lift plan environmental constraints | TBD | TBD |

## Construction

| Item | Description | Source |
|---|---|---|
| Mode of delivery to site | Shipped compressor packages (by others per SOW); receipt and installation by EPC Integrator scope | SCOPE_LEDGER SOW-0134 |
| Foundation interface | Installation on piles (by others) — CWP must coordinate pile schedule, hold-down templates, grout | SCOPE_LEDGER SOW-0134 (By others); ASSUMPTION on grouting requirement |
| Mechanical tie-ins | Tie-in piping (by others per SOW) — CWP must define isolation, hot/cold cut-ins, test boundaries | SCOPE_LEDGER SOW-0134; ASSUMPTION on cut-in approach |
| Electrical tie-ins | Electrical connections (by others per SOW) — CWP must define lockout/tagout, cable pulls, termination, motor rotation check | SCOPE_LEDGER SOW-0134; ASSUMPTION on LOTO discipline |
| Structural | Mounting platform and stairs (by others per SOW) — CWP must define interface schedule and access for inspection | SCOPE_LEDGER SOW-0134 |
| Inspection scope | Receiving, fit-up, pressure test, electrical loop, dryer regen cycle witnessing — TBD by procedure | TBD; ASSUMPTION |
| Turnover | Construction Work Package -> EPC Vendor Package Review and Acceptance (DEL-079-06) | DELIVERABLE_REGISTER DEL-079-06; ASSUMPTION on handoff path |

## Anticipated Artifacts (per _CONTEXT.md)

- Construction work package (this deliverable's primary artifact)
- Installation and tie-in workface plan
- Construction interface and turnover checklist

## Covers Scope Items

- SOW-0131, SOW-0132, SOW-0133, SOW-0134 (per _CONTEXT.md and DELIVERABLE_REGISTER row 380)

## Supports Objectives

- OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 (per _CONTEXT.md; ASSUMPTION — best-effort PACKAGE_HEURISTIC mapping)

## References

- _CONTEXT.md (deliverable identity)
- _REFERENCES.md (decomposition snapshot pointers)
- DELIVERABLE_REGISTER.csv row DEL-079-03 (GATE-07 snapshot)
- SCOPE_LEDGER.csv rows SOW-0131..SOW-0134 (GATE-07 snapshot)
- 26020-Package_Requirements.docx package heading 32 — Basic scope; Major included equipment; Scope notes and open items (location TBD; not opened in this run)
- Workbook Packages row 69 (26020-Packages_Interfaces_4_export.xlsx; location TBD; not opened in this run)
