# Specification — DEL-021-04 Vendor Engineered Equipment Package (6.9 kV Switchgear Equipment)

> Normative requirements for the Package Vendor production unit (engineering, design, fabrication/supply, physical equipment) for `PKG-021`. Requirements derive from the accessible Deepcut DBM electrical source slices and the Gate 7 decomposition row. Inferred requirements are labelled `ASSUMPTION`; unsupported values are `TBD`.

## Scope

### Included

- Vendor engineering and design of the 6.9 kV switchgear equipment package serving Building 820-1 (6.9 kV Inlet/Sales Compressor Electrical Building).
- Fabrication/supply of the physical equipment package (switchgear lineup(s) and integrated devices).
- Vendor package design basis and datasheet set supporting the equipment.
- Integration review interfaces presented to the EPC Integrator for facility integration acceptance (`DEL-021-06`).

### Excluded

- Facility-level integration, tie-ins, constructability, and procurement/construction coordination — owned by the EPC Integrator per `PACKAGE_REGISTER` ownership statement for PKG-021.
- Civil/structural foundations and building shell beyond vendor-supplied skid or lineup steel.
- Plant-wide grounding grid; the vendor scope terminates at the equipment ground bus / specified connection points.
- Vendor document submittal/turnover package — that is `DEL-021-05`.

## Requirements

### REQ-021-04-001 — System voltage and configuration

The 6.9 kV switchgear equipment package SHALL be engineered for nominal 6.9 kV, 3 phase, 3 wire, 60 Hz service. (Source: DBM System Voltages table.)

### REQ-021-04-002 — System grounding compatibility

The equipment SHALL be compatible with low-resistance grounded operation using a 100 A, 10 s neutral grounding resistor on each 6.9 kV transformer secondary, operated as a tripping system. (Source: DBM Grounding and Bonding section.)

### REQ-021-04-003 — Upstream feed and bus sizing basis

The lineup SHALL be designed for radial supply from the facility 13.8 kV switchgear via step-down transformer(s). Continuous bus current, short-circuit current, and withstand ratings: TBD pending load-flow and short-circuit studies identified in the DBM Electrical Studies list. (ASSUMPTION shape; numeric values TBD.)

### REQ-021-04-004 — Interface with 6.9 kV MCC and starting VFDs

The switchgear lineup SHALL provide feeder positions sized and protected to serve `MCC-8200` (mechanically latched fused contactors, motor protection relays, Ethernet to plant PLC) and the starting VFDs for `KM-2150` and `KM-2250` Inlet/Sales Gas Compressor motors. (Source: DBM Motor Control section.)

### REQ-021-04-005 — No PFCC on synchronous-transfer bus

Power-factor-correction capacitor banks SHALL NOT be installed on the `MCC-8200` synchronous-transfer bus. The switchgear design SHALL NOT presume PFCC on that bus. (Source: DBM Motor Control section, explicit prohibition.)

### REQ-021-04-006 — Protection, metering, and communications

Motor protection relays and metering SHALL be provided as required by the equipment scope. An Ethernet communication interface to the plant PLC central control panel SHALL be provided for data acquisition. Bus-level protection scheme (differential, arc-flash mitigation, lockout): TBD pending the relay coordination and arc-flash energy study identified in the DBM Electrical Studies list.

### REQ-021-04-007 — Installation environment

Equipment SHALL be designed for indoor installation in a prefabricated modular electrical building with n+1 HVAC and bottom cable entry. (Source: DBM Electrical Buildings section.)

### REQ-021-04-008 — Cable terminations

Equipment SHALL accommodate bottom cable entry, with terminations compatible with three-conductor copper TECK cable rated 8 kV with 100 percent insulation (shielded) for 6.9 kV medium-voltage cables. (Source: DBM Power Cables table, line ~3008.)

### REQ-021-04-009 — Governing codes and standards

The package SHALL be designed in accordance with the governing electrical codes and standards for the project. Canadian Electrical Code (CEC) spacing and installation requirements apply for transformer-related accessories at the package boundary where applicable. (Source: DBM Transformers and Area Classification sections.) Specific clause-level code editions: location TBD pending the project electrical specifications (`26020-Package_Requirements.docx`, not extracted in accessible markdown form).

### REQ-021-04-010 — Interface obligations

The package SHALL provide engineered interfaces consistent with the PKG-021 PACKAGE_REGISTER applicable interface types: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Detailed interface clauses are governed by `DEL-021-02 Package Datasheet`. (Source: Gate 7 PACKAGE_REGISTER row.)

### REQ-021-04-011 — Quantity allocation

Quantity of 6.9 kV switchgear lineups within PKG-021 SHALL be confirmed by the EPC Integrator via `DEL-021-02 Package Datasheet`. The DBM equipment list entry "Medium Voltage Switchgear (1)" is not allocated to PKG-021 in accessible sources. (HRR-021-04-001.) TBD.

## Standards (governing — location TBD where not extracted)

- Project package requirements: `_Sources/26020-Package_Requirements.docx` — location TBD.
- Canadian Electrical Code (CEC) — referenced in DBM; clause TBD.
- API RP-505 — referenced in DBM for area classification (general project context; not directly binding on switchgear electrical design clauses).
- IEEE / ANSI C37 series for MV switchgear — ASSUMPTION: likely applicable; not explicitly cited in accessible sources.

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-021-04-001 | Vendor design basis review confirming nameplate voltage class and phase/wire/frequency configuration. |
| REQ-021-04-002 | Review of neutral-grounding interface drawings and protection settings against the 100 A/10 s tripping basis. |
| REQ-021-04-003 | Confirmation that vendor sizing assumptions reflect accepted load-flow and short-circuit study outputs (when issued). |
| REQ-021-04-004 | Inspection of one-line diagrams confirming feeder positions to MCC-8200 and starting VFDs. |
| REQ-021-04-005 | Inspection of bus-arrangement drawings confirming no PFCC bank on the synchronous-transfer bus. |
| REQ-021-04-006 | Factory acceptance test (FAT) of protection relays, metering, and Ethernet interface to PLC. |
| REQ-021-04-007 | Confirmation that equipment dimensional, environmental, and HVAC heat-load data match the Building 820-1 design. |
| REQ-021-04-008 | Confirmation of termination compartment compatibility with 8 kV three-conductor copper TECK cable. |
| REQ-021-04-009 | Vendor declaration of code compliance and listing/certification evidence. |
| REQ-021-04-010 | Interface verification against `DEL-021-02 Package Datasheet` interface matrix. |
| REQ-021-04-011 | EPC Integrator confirmation of lineup quantity via `DEL-021-02`. |

Independent verification mechanisms (FAT witness, site acceptance test, integration acceptance) are governed by `DEL-021-06 EPC Vendor Package Review and Acceptance`.

## Documentation

The Package Vendor SHALL produce, at minimum:

- Vendor package design basis.
- Vendor equipment datasheet set (switchgear lineup, breakers, instrument transformers, protection/metering devices).
- One-line and three-line diagrams for the package.
- Termination, grounding, and interface drawings.
- Protection and control schematics, settings, and Ethernet/PLC interface description.
- Factory test plans, FAT procedures, and FAT records (records turned over via `DEL-021-05`).
- Installation, operation, and maintenance manuals.

Full vendor document register, submittal cadence, and turnover records are owned by `DEL-021-05 Vendor Document Turnover Package`.
