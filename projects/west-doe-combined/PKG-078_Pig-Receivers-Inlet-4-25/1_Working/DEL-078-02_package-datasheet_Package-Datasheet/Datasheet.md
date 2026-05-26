# Datasheet — DEL-078-02 Package Datasheet (Pig Receivers (Inlet) 4-25)

Source-grounded EPC Package Datasheet capturing the package data required for third-party vendor or discipline package engineering and design of the PKG-078 Pig Receivers (Inlet) 4-25 package at the West Doe Deepcut (04-25) facility.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-078-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 433 |
| Parent Package ID | `PKG-078` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 78 |
| Package Name | Pig Receivers (Inlet) 4-25 | `PACKAGE_REGISTER.csv` row 78 |
| Package Tag (vendor-level) | `26020-01-PT-35-001 - Pig Receivers (Inlet)` | `PACKAGE_REGISTER.csv` row 78 (AuthoritativeCompanionRegisterRow) |
| Workbook Row | 78 | `PACKAGE_REGISTER.csv` row 78 |
| WBS | 01 | `PACKAGE_REGISTER.csv` row 78 |
| Discipline | Mechanical | `PACKAGE_REGISTER.csv` row 78; `_CONTEXT.md` |
| Type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 433 |
| Responsible Party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 433 |
| Process Function | Plant inlet pipeline gas enters the facility through the pig receivers installed and moves on into the inlet separators. | `PACKAGE_REGISTER.csv` row 78; SCOPE_LEDGER `SOW-0162` |
| Facility | West Doe 04-25 Deepcut Expansion | DBM-Deepcut/4-25_Deepcut_DBM.md SEC-04 |

## Attributes (Package Equipment)

| Attribute | Value | Units | Source |
|---|---|---|---|
| Number of pig receivers | 3 (identical) | ea | SCOPE_LEDGER `SOW-0162`, `SOW-0163` |
| Receiver tag basis | `PR-1010 / PR-1020 / PR-1030-1` | — | SCOPE_LEDGER `SOW-0163` |
| Nominal receiver barrel OD | 610 | mm (24 in) | SCOPE_LEDGER `SOW-0162`, `SOW-0163` |
| Skid type | Dedicated structural-steel non-enclosed skids | — | SCOPE_LEDGER `SOW-0162`, `SOW-0163` |
| Skid-mounted isolation | All skid-mounted isolation or ESDV | — | SCOPE_LEDGER `SOW-0163` |
| Overpressure protection | HIPPS (High Integrity Pressure Protection System) package per skid | — | SCOPE_LEDGER `SOW-0163` |
| HIPPS ESDV location | Upstream of each pig receiver | — | SCOPE_LEDGER `SOW-0163` |
| HIPPS control element | Pressure control valve with outlet pressure transmitter, PID control to maintain inlet separator vessel operating pressure below applicable setpoint | — | SCOPE_LEDGER `SOW-0163` |
| HIPPS shutdown logic | Shutdown valve with pneumatic hi-low shutoff, plus an additional redundant shutdown valve and pneumatic hi-low, to close high-pressure inlet | — | SCOPE_LEDGER `SOW-0163` |
| Sour gas purge | Sweet gas purge downstream of manual isolation valve for sour gas purge of receiver barrel prior to opening for pig retrieval | — | SCOPE_LEDGER `SOW-0163` |
| Vent | Vent line to HP flare system | — | SCOPE_LEDGER `SOW-0163` |
| Service classification | Sour service; H2S design 1.0 mol% | mol% | SCOPE_LEDGER `SOW-0163`; DBM SEC-04 (1.0 mol% H2S plant inlet design) |
| Service type (overall) | High-pressure wet sour natural gas | — | DBM-Deepcut SEC-04; SCOPE_LEDGER `SOW-0163` |

## Conditions (Design and Operating Basis)

| Condition | Value | Source |
|---|---|---|
| Package design throughput (total) | 225 MMSCFD | SCOPE_LEDGER `SOW-0164` |
| Normal flowrate per receiver | TBC | SCOPE_LEDGER `SOW-0164` |
| Normal operating pressure | 653 to 725 psig | SCOPE_LEDGER `SOW-0164` |
| MAOP | 1300 psig | SCOPE_LEDGER `SOW-0164` |
| Design pressure (low / normal high) | 653 / 725 psig | SCOPE_LEDGER `SOW-0164` |
| MAWP | 1440 psig | SCOPE_LEDGER `SOW-0164` |
| Historical ambient temperature | -19 deg C min / 22.2 deg C max | SCOPE_LEDGER `SOW-0164` |
| Ambient design temperature | -40 deg C min / +35 deg C max | SCOPE_LEDGER `SOW-0164` |
| Plant inlet design H2S | 1.0 mol% (design); high and license values TBC | DBM-Deepcut SEC-04 |
| Plant inlet design CO2 | 0.7 mol% (design); high and license values TBC | DBM-Deepcut SEC-04 |
| Plant inlet water | 4 lbH2O/MMSCF design; low <4, high 7 | DBM-Deepcut SEC-04 |
| Inlet pipeline boundary basis | Stated basis 1100 psig and 40 deg F to 95 deg F (5 deg C to 35 deg C); to be confirmed during detailed engineering | DBM-Deepcut SEC-04 |
| Hydrate suppression | No continuous hydrate suppression in raw inlet gas piping; methanol injection points included for transient management | DBM-Deepcut SEC-04 |

> ASSUMPTION: The package operating pressure window (653-725 psig) is the package vendor's design point and is lower than the DBM lease-boundary basis (1100 psig). The pressure-reduction path between lease boundary and pig receiver upstream tie-in is governed by upstream facility piping/HIPPS arrangement; resolution belongs to the EPC Integrator at tie-in design. Recorded as ASSUMPTION pending EPC confirmation.

## Construction (Package Composition)

| Item | Description | Source |
|---|---|---|
| (3x) Pig receiver assemblies | `PR-1010 / 1020 / 1030-1`, 610 mm (24 in) OD barrel, dedicated structural steel non-enclosed skid | SCOPE_LEDGER `SOW-0163` |
| HIPPS package (per skid) | ESDV(s) upstream of receiver, pressure control valve, outlet pressure transmitter, redundant pneumatic hi-low shutdown logic | SCOPE_LEDGER `SOW-0163` |
| Sweet-gas purge tie-in | Downstream of manual isolation valve, sized for sour gas purge of receiver barrel | SCOPE_LEDGER `SOW-0163` |
| HP flare vent tie-in | Vent line from each receiver to HP flare system | SCOPE_LEDGER `SOW-0163` |
| Skid structural steel | Dedicated non-enclosed structural-steel skid per receiver | SCOPE_LEDGER `SOW-0162`, `SOW-0163` |
| Materials of construction | TBD by Package Vendor for stated sour service (1.0 mol% H2S, sour service design) | SCOPE_LEDGER `SOW-0163`; specific MOC class not stated in available sources |
| Pressure relief sizing basis | TBD — relief/vent routing defined (HP flare); sizing basis not stated in available sources | SCOPE_LEDGER `SOW-0163` |
| Insulation / EHT extent | TBD; EHT identified as a package interface but extent not stated in available sources | INTERFACE_REGISTER `IFC-9313950850` (EHT) |
| Coatings / external protection | TBD; not stated in available sources | location TBD |

## Interfaces (Package Interface Requirements Matrix)

Package interfaces extracted from `INTERFACE_REGISTER.csv` (rows for PKG-078):

| InterfaceID | Interface Type | Counterparty Boundary | Source |
|---|---|---|---|
| IFC-49A2026DAA | Process Piping | Facility process piping at receiver inlet and outlet flanges | INTERFACE_REGISTER row 647 |
| IFC-11316BD975 | Relief / Flare / Vent | HP flare header tie-in | INTERFACE_REGISTER row 648; SCOPE_LEDGER `SOW-0163` |
| IFC-17309B535C | Drain / Containment | Facility closed/open drain system; spill containment grading | INTERFACE_REGISTER row 649 |
| IFC-F2CC0221E0 | Electrical Power | Facility MCC (by others per `SOW-0164`) | INTERFACE_REGISTER row 650; SCOPE_LEDGER `SOW-0164` |
| IFC-9313950850 | EHT (Electric Heat Trace) | Facility EHT supply / control | INTERFACE_REGISTER row 651 |
| IFC-99C4B8C9E0 | I&C / Control Cabling | Facility DCS integration (DCS integration by others per `SOW-0164`) | INTERFACE_REGISTER row 652; SCOPE_LEDGER `SOW-0164` |
| IFC-A553991A6E | Maintenance Access | Pig handling / receiver opening access provisions | INTERFACE_REGISTER row 653 |
| IFC-3894C2DC14 | Grading / Site Drainage / Spill Containment | Facility civil grading and drainage | INTERFACE_REGISTER row 654 |
| IFC-6798D96AAF | Structural / Foundations / Supports | Foundations by others per `SOW-0164` | INTERFACE_REGISTER row 655; SCOPE_LEDGER `SOW-0164` |
| IFC-65EDB92369 | Pipeline / Pigging | Plant inlet pipeline launcher/receiver compatibility; pig launcher provisions at upstream facility | INTERFACE_REGISTER row 656; SCOPE_LEDGER `SOW-0162` |

**By Others (explicit per `SOW-0164`):** interconnecting piping, DCS integration, foundations, electrical supply to MCC.

## Scope Coverage

This datasheet supports the following Scope Ledger items (`SCOPE_LEDGER.csv`):

- `SOW-0161` — Carry vendor-responsible Mechanical package as distinct flat project package
- `SOW-0162` — Basic scope (3x 610 mm OD pig receivers with HIPPS, structural steel skids)
- `SOW-0163` — Major included equipment (receiver assemblies, HIPPS, purge, vent)
- `SOW-0164` — Scope notes, open items, capacity, operating/design conditions

## Supported Objectives

Per `_CONTEXT.md` (PACKAGE_HEURISTIC mode, ASSUMPTION: best-effort mapping):
`OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010`.

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- `PACKAGE_REGISTER.csv` (Gate 7 snapshot, row 78)
- `DELIVERABLE_REGISTER.csv` (Gate 7 snapshot, row 433)
- `SCOPE_LEDGER.csv` (Gate 7 snapshot, rows 162-165 covering `SOW-0161` through `SOW-0164`)
- `INTERFACE_REGISTER.csv` (Gate 7 snapshot, rows 647-656 covering PKG-078)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (SEC-04 Inlet, Separation, Stabilization basis)
- Underlying source: `26020-Package_Requirements.docx` package heading 31 (location TBD — not directly read; SCOPE_LEDGER rows are the locally accessible extraction)
- Underlying source: `Bid Docs/Budgetary/26020-01-PT-RFQ-35-001-Pig_Recv_2.docx` (location TBD — not locally accessible in `_Sources`)
