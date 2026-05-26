# Specification — Vendor Engineered Equipment Package (DEL-089-04)

## Scope

### Included

- Vendor-owned engineering and design of two (2) identical 610 mm (24 in) OD inlet pig receiver assemblies (PR-1010-2, PR-1020-2), each on a dedicated structural steel non-enclosed skid (SOW-0158; SOW-0159).
- Skid-mounted isolation, ESDV upstream of receiver, sweet-gas purge tie-in arrangement, and vent connection to HP flare (SOW-0159).
- Vendor fabrication/supply of the physical equipment package and vendor design basis/datasheet set (DELIVERABLE_REGISTER.csv DEL-089-04 anticipated artifacts; ARTIFACT_REGISTER.csv ART-AFDDE0BE60, ART-6017932F95).
- Vendor support of EPC Integrator integration review (DELIVERABLE_REGISTER.csv DEL-089-04 ResponsibleParty; OBJ-004).

### Excluded (By Others)

- Interconnecting piping outside the skid battery limits (SOW-0160).
- DCS integration / facility controls integration (SOW-0160; OBJ-006 places I&C with the EPC integration scope).
- Foundations (SOW-0160).
- Electrical supply to the MCC (SOW-0160).

## Requirements

### R1 — Quantity and Configuration
The vendor shall supply two (2) identical pig receiver assemblies tagged PR-1010-2 and PR-1020-2, each mounted on a dedicated structural steel non-enclosed skid (SOW-0158; SOW-0159).

### R2 — Receiver Size
Each pig receiver shall be 610 mm (24 in) OD (SOW-0158; SOW-0159).

### R3 — Process Service
The package shall be designed for plant inlet pipeline gas service feeding downstream inlet separators (SOW-0158).

### R4 — Pressure Envelope
The receiver and skid-mounted components shall be designed to the following pressure envelope (SOW-0160):
- Normal Operating Pressure: 125–200 psig
- MAOP: 572 psig
- Design Pressure (low): 125 psig; Design Pressure (normal high): 200 psig
- MAWP: 635 psig

### R5 — Temperature Envelope
Equipment shall be rated for ambient design temperatures of -40 °C minimum to +35 °C maximum (SOW-0160). Historical ambient extremes are -19 °C to +22.2 °C (SOW-0160).

### R6 — Throughput
The package shall be sized consistent with a package design throughput of 80 MMSCFD (SOW-0160). Normal flowrate per receiver is TBC (TBD — source explicitly defers).

### R7 — Sour Service
Equipment shall be designed for sour service at a stated design level of 0.1 mol% (per source statement) (SOW-0159). Materials and components in wetted/process boundary service shall be sour-service-compatible (ASSUMPTION: compliance with NACE MR0175 / ISO 15156 expected per sour-service objective OBJ-009; specific clause-level requirements TBD — standard text not locally accessible).

### R8 — Isolation and ESDV
All skid-mounted isolation shall be provided, and an ESDV shall be installed upstream of each receiver (SOW-0159).

### R9 — Purge
A sweet-gas purge tie-in shall be provided downstream of a manual isolation valve to enable sour-gas purge of the receiver barrel prior to opening for pig retrieval (SOW-0159).

### R10 — Vent
A vent line shall be provided to the HP flare system (SOW-0159).

### R11 — Battery Limits and Integration Interfaces
The vendor scope ends at defined battery limits. Interconnecting piping, DCS integration, foundations, and electrical supply to the MCC are by others (SOW-0160). The vendor design basis and datasheet set shall expose the interface requirements needed by the EPC Integrator (ART-6017932F95; OBJ-004).

### R12 — Vendor Documentation Interface
The vendor shall produce a design basis and datasheet set sufficient to support EPC integration review (ART-6017932F95; DEL-089-04 anticipated artifacts). The vendor-document turnover set itself is tracked under DEL-089-05 (DELIVERABLE_REGISTER.csv).

### R13 — Responsibility Model
The Package Vendor owns engineering, design, fabrication/supply, and the physical package; the EPC Integrator owns facility integration and integration review (OBJ-004; DEL-089-04 ResponsibleParty in DELIVERABLE_REGISTER.csv).

## Standards

| Standard | Applicability | Local Source Slice |
|---|---|---|
| NACE MR0175 / ISO 15156 — Sour Service Materials | ASSUMPTION: applies via sour service requirement R7 and OBJ-009 | location TBD (not locally accessible) |
| ASME B31.3 — Process Piping | ASSUMPTION: applies to skid-mounted piping | location TBD (not locally accessible) |
| ASME BPVC Section VIII Div. 1 — Pressure Vessels | ASSUMPTION: applies to pig receiver barrel | location TBD (not locally accessible) |
| CSA Z662 — Oil and Gas Pipeline Systems | ASSUMPTION: applies if receiver is considered a pipeline appurtenance | location TBD (not locally accessible) |
| Project-specific specifications and codes | Per OBJ-009 (regulatory/codes/standards carried into packages) | location TBD |

Governing project code list shall be confirmed by the upstream EPC Scope of Work (DEL-089-01) and Package Datasheet (DEL-089-02) — both not yet drafted at the time of this run.

## Verification

| Req | Verification Approach |
|---|---|
| R1, R2 | Vendor general arrangement (GA) drawings and equipment list — vendor design basis and datasheet set (ART-6017932F95). |
| R3 | Process datasheet and P&ID extract showing inlet service routing to inlet separators. |
| R4, R5 | Vendor pressure-vessel and skid-piping datasheets and code calculations (ASSUMPTION: ASME Sec VIII / B31.3). |
| R6 | Vendor capacity/sizing calculation against 80 MMSCFD; receiver-level normal flow open until upstream confirms (TBD). |
| R7 | Vendor MoC report and NACE MR0175 / ISO 15156 compliance statement (ASSUMPTION). |
| R8, R9, R10 | Vendor P&ID and ESDV / purge / vent schematics; valve datasheets. |
| R11, R12, R13 | EPC integration review of vendor design basis and datasheet set; interface log clearance against the EPC Package Datasheet (DEL-089-02). |

## Documentation

Anticipated artifacts from this deliverable (DELIVERABLE_REGISTER.csv DEL-089-04 + ARTIFACT_REGISTER.csv):

- Vendor engineered physical equipment package (ART-AFDDE0BE60) — the physical package itself as evidence of execution.
- Vendor package design basis and datasheet set (ART-6017932F95).
- Major included equipment evidence (ART-8976B99094) — captures the source-defined equipment list against which vendor design is validated.

Vendor document turnover (document register, submittals, turnover records) is the responsibility of DEL-089-05 and is not duplicated here.
