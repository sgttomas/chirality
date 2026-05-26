# Datasheet — DEL-062-02 Package Datasheet (NGL Loading Pumps Building, PKG-062)

> Pass 1 + Pass 2 draft. Source-grounded; non-trivial values cite `SourcePath` / `SectionRef`. Inferences labeled `ASSUMPTION`; missing values marked `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-062-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| ParentPackageID | `PKG-062` | `_CONTEXT.md` |
| Package Name (decomposition) | NGL Loading Pumps Building | `PACKAGE_REGISTER.csv` (Gate-07) row `PKG-062` |
| Package Equipment Tag | `26020-01-PT-18-003` | `PACKAGE_REGISTER.csv` (Gate-07); `26020-Package_Requirements.docx`, package section `26020-01-PT-18-003 - LPG Loading Pumps` |
| Package Label in Source Document | "LPG Loading Pumps" | `26020-Package_Requirements.docx`, heading `26020-01-PT-18-003 - LPG Loading Pumps` |
| Workbook Row | 76 | `SCOPE_LEDGER.csv` SOW-0153; `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Location / Status (source) | 4-25 West Doe Deepcut; budgetary RFQ basis; vetted package scope basis | `26020-Package_Requirements.docx` (`26020-01-PT-18-003 - LPG Loading Pumps`, "Location / Status") |
| Source Basis (vendor bid doc) | `Bid Docs/Budgetary/26020-01-PT-RFQ-18-003-LPG_Loading_Pumps.docx` | `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Source Basis") — location TBD (file not present in `_Sources`) |

## Attributes — Major Included Equipment

| Tag(s) | Description | Quantity | Make / Model | Type | Source |
|---|---|---|---|---|---|
| `P9510-1`, `P9520-1`, `P9530-1`, `P9540-1` | Loading Pumps (move LPG product from storage to LPG Truck Loading) | 4 | Blackmer Model `LGL4B` | Rotary Vane Pump (parallel arrangement) | `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Major Included Equipment") |
| Building | Self-framing building to be erected at site | 1 | TBD | Self-framing | `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Major Included Equipment") |

CONFLICT-1 (see `Guidance.md` Conflict Table): Decomposition names the package "NGL Loading Pumps Building" while the source row labels the pumps "LPG Loading Pumps" and the basic-scope text states the process function as moving "LPG product from storage to LPG Truck Loading."

## Conditions — Capacity, Driver, Operating, Design

| Parameter | Value | Notes / Status | Source |
|---|---|---|---|
| Capacity per pump | 68 m³/hr @ 345 kPad (300 USGPM @ 50 psid) | TBC TDH (To Be Confirmed Total Dynamic Head) | `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Major Included Equipment" and "Scope Notes / Open Items") |
| Number of pumps | 4 (parallel) | — | Same source, "Basic Scope" / "Major Included Equipment" |
| Driver | Electric motor, 575 V / 3 PH / 60 Hz | — | Same source, "Scope Notes / Open Items" |
| Motor power source | 600 V MCC (fed from facility MCC) | — | Same source, "Scope Notes / Open Items" |
| Local control | H-O-A or On-Off switch | — | Same source, "Scope Notes / Open Items" |
| Motor sizing basis | Sized for inlet stabilizer composition density at -40 °C start-up condition | — | Same source, "Scope Notes / Open Items" |
| Operating conditions | TBC — per capacity/site conditions | TBC in source | Same source, "Scope Notes / Open Items" |
| Design conditions | TBC — per capacity/site conditions | TBC in source | Same source, "Scope Notes / Open Items" |
| Start-up ambient (motor sizing) | -40 °C | — | Same source, "Scope Notes / Open Items" |

## Construction — Building, Skid, Mounting

| Item | Value | Source |
|---|---|---|
| Building | Self-framing building, erected at site | `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Major Included Equipment") |
| Pump arrangement | 4 identical pumps in parallel | Same source, "Basic Scope" |
| Foundations | By others (EPC) | Same source, "Scope Notes / Open Items" ("By others: ... foundations ...") |
| Electrical supply to MCC | By others (EPC) | Same source, "Scope Notes / Open Items" ("By others: ... electrical supply to MCC") |
| DCS integration | By others (EPC) | Same source, "Scope Notes / Open Items" ("By others: DCS integration ...") |

## Physical Interface Applicability (from source row)

Interface source declared in document: `26020-Packages_Interfaces.3.xlsx` (note: the file shipped in `_Sources` is `26020-Packages_Interfaces_4_export.xlsx` — see CONFLICT-2 in `Guidance.md`).

| Interface Type | Applicability | Source |
|---|---|---|
| Process Piping | Yes | `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Physical Interface Summary") |
| Utility Piping | Yes | Same source |
| Relief / Flare / Vent | Yes | Same source |
| Drain / Containment | Yes | Same source |
| Electrical Power | Yes | Same source |
| Area / Exterior Lighting | Yes (interface row in source, column M, row 76) | Same source |
| EHT (Electrical Heat Tracing) | Yes | Same source |
| Grounding / Bonding | Yes | Same source |
| Cathodic Protection | No | Same source |
| I&C / Control Cabling | Yes | Same source |
| Communications / Network | No | Same source |
| Building HVAC / Services | Yes | Same source |
| Fire & Gas / Safety Systems | Yes | Same source |
| Maintenance Access | Yes | Same source |
| Grading / Site Drainage / Spill Containment | No | Same source |
| Structural / Foundations / Supports | Yes | Same source |
| Product Loading | No | Same source |
| Pipeline / Pigging | No | Same source |

## Vendor Engineering Deliverables (interface evidence carried in this Package Datasheet)

Authority: `26020-Package_Requirements.docx` (`26020-01-PT-18-003 - LPG Loading Pumps`, "Vendor Engineering Deliverables"). Per `_CONTEXT.md` Notes: "interface facts are intentionally carried here as evidence rather than standalone deliverables."

### Core vendor documents
- `PRQ-009` — Vendor Document Index
- `DOC-008` — Vendor Document Control Procedure
- `QLT-006` — Supplier Quality Plan
- `QLT-003` — Inspection and Test Plan (ITP)
- `QLT-013` — Material Test Reports / Certificates
- `QLT-020` — Inspection Release Certificate
- `QLT-021` — Manufacturing Record Book / Vendor Data Book
- `PRQ-013` — Logistics / Shipping Plan
- `PRQ-015` — Spare Parts Interchangeability Record (SPIR)
- `PRQ-016` — Vendor Data Book / Final Supplier Documentation

### Core package engineering
- `MEC-001` — Mechanical Design Basis
- `MEC-002` — Mechanical Equipment List
- `MEC-003` — Mechanical Equipment Data Sheets
- `MEC-006` — Package Equipment Specifications
- `MEC-014` — Mechanical Calculation Package
- `MEC-016` — Equipment General Arrangement Drawing
- `MEC-017` — Equipment Installation / Setting Drawings
- `MEC-018` — Lifting / Handling Study for Major Equipment
- `MEC-021` — Equipment FAT / Performance Test Procedure
- `MEC-022` — Equipment FAT / Performance Test Report
- `MEC-023` — Vendor Data Book / Mechanical Final Documentation
- `MEC-024` — Mechanical Spares / Special Tools Requirements
- `MEC-025` — Mechanical Equipment IOM Manual

### Rotating equipment / pumps
- `MEC-004` — Rotating Equipment Specifications
- `MEC-007` — Pump Data Sheets
- `MEC-019` — Mechanical Seal / Lube Oil Specification
- `PRO-013` — Pump Hydraulic / NPSH Calculations
- `ELE-011` — Motor Starting Study

### Loading / metering package
- `INS-015` — Metering Package Specification
- `PRO-025` — Operating Guidelines / Startup-Shutdown Narrative
- `PIP-004` — Tie-In List / Tie-In Scope Sheets
- `PIP-018` — Valve Data Sheets

### Relief / flare / vent design
- `PRO-014` — Relief and Flare Design Basis
- `PRO-015` — PSV / Pressure Relief Sizing Calculations
- `PRO-016` — Relief Valve Data Sheets
- `PRO-017` — Flare Load Summary / Flare System Study
- `PRO-018` — Blowdown / Depressurization Study

### Process piping interfaces
- `PRO-008` — Piping and Instrumentation Diagrams (P&IDs)
- `PIP-003` — Piping Line List
- `PIP-006` — Equipment Arrangement / Piping General Arrangement
- `PIP-007` — Piping Plans and Sections
- `PIP-008` — Piping Isometric Drawings
- `PIP-009` — Fabrication Isometrics with BOM
- `PIP-017` — Piping MTO / Material Take-Off
- `PIP-024` — Hydrotest / Pressure Test Packages
- `PIP-025` — Flushing / Cleaning / Drying Procedure
- `PIP-028` — Piping As-Built Drawings

### Utility piping interfaces
- `PRO-011` — Utility Summary / Utility Consumption Report

### Drainage / containment interfaces
- `PRO-023` — Process Sewer / Closed Drain Design Basis
- `CIV-014` — Bund / Dike / Secondary Containment Drawings

### Electrical, lighting, EHT, grounding
- `ELE-002` — Electrical Load List / Consumer List
- `ELE-003` — Single-Line Diagrams (SLDs)
- `ELE-014` — Cable Schedule
- `ELE-015` — Cable Tray / Routing Drawings
- `ELE-016` — Electrical Layout Drawings
- `ELE-020` — Electrical Equipment Data Sheets
- `ELE-027` — Electrical Installation Details
- `ELE-028` — Electrical Interconnection / Connection Diagrams
- `ELE-029` — Electrical FAT / SAT Procedure
- `ELE-030` — Electrical Test Records / Energization Package
- `ELE-017` — Lighting Layout Drawings
- `ELE-018` — Electrical Heat Tracing Design Package
- `PIP-020` — Piping Insulation / Heat Tracing Schedule
- `PIP-021` — Piping Heat Tracing Interface Package
- `ELE-012` — Grounding / Earthing Study
- `ELE-019` — Earthing / Bonding Layout Drawings

### Instrumentation and controls interfaces
- `INS-002` — Instrument Index
- `INS-003` — Instrument Data Sheets
- `INS-005` — Instrument Location Plans
- `INS-006` — Instrument Hook-Up Drawings
- `INS-008` — Instrument Loop Diagrams
- `INS-009` — Instrument Wiring / Termination Diagrams
- `INS-010` — Junction Box / Marshalling Drawings
- `INS-011` — Instrument Cable Schedule
- `INS-016` — Control Valve Data Sheets
- `INS-017` — On-Off / Shutdown Valve Data Sheets
- `INS-018` — Instrument I/O List
- `INS-025` — Instrument MTO / Quantity Take-Off
- `INS-029` — Instrument As-Built Drawings
- `CTL-003` — Control Narrative / Functional Specification
- `CTL-005` — Cause and Effect Matrix
- `CTL-006` — DCS I/O List
- `CTL-026` — Package Vendor Interface Specification

### Building / HVAC / code interfaces
- `PRO-024` — Ventilation / Process Safety Equipment Inputs
- `TSF-023` — Building Siting / Occupied Building Risk Assessment
- `REG-021` — Fire Code / Building Code Compliance Package
- `STR-002` — Structural General Arrangement Drawings
- `STR-012` — Module Structural Drawings

### Fire and gas / technical safety interfaces
- `TSF-002` — Fire and Gas Philosophy
- `TSF-003` — Fire and Gas Mapping Study
- `TSF-004` — Fire and Gas Detector Layout Drawings
- `TSF-009` — SIL Determination Report
- `TSF-011` — Safety Requirements Specification (SRS)
- `TSF-013` — Supplier SIL Documentation / Safety Manual
- `TSF-028` — Emergency Response Plan Inputs

### Structural / foundations / supports
- Source row continues beyond extracted slice. Full list `TBD` — re-extract from `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Vendor Engineering Deliverables", post "Structural, fou…") for closeout.

## Scope Items Covered

- `SOW-0153` — Workbook-defined package "NGL Loading Pumps Building" carried as a flat project package for WBS 01 (`SCOPE_LEDGER.csv`).
- `SOW-0154` — Basic scope (Blackmer LGL4B × 4) (`SCOPE_LEDGER.csv`).
- `SOW-0155` — Major included equipment + self-framing building (`SCOPE_LEDGER.csv`).
- `SOW-0156` — Scope notes / open items: by-others list, capacity, driver, operating/design TBC (`SCOPE_LEDGER.csv`).

## Objectives Supported (ASSUMPTION: package-grouping heuristic)

`OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010` — propagated from `_CONTEXT.md` and `SCOPE_LEDGER.csv` SOW rows for `PKG-062`. Per `OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC`, treat as directionally relevant context unless `OBJECTIVE_DELIVERABLE_MAP.csv` confirms at the deliverable-ID level.

## Exclusions / By Others

- DCS integration — by others (EPC scope). Source: `26020-Package_Requirements.docx` (`26020-01-PT-18-003`, "Scope Notes / Open Items").
- Foundations — by others (EPC scope). Same source.
- Electrical supply to the MCC — by others (EPC scope). Same source.

## References (used in this Datasheet)

- `26020-Package_Requirements.docx`, section `26020-01-PT-18-003 - LPG Loading Pumps` (subsections: Location / Status; Source Basis; Basic Scope; Major Included Equipment; Scope Notes / Open Items; Physical Interface Summary; Vendor Engineering Deliverables) — local source at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx`.
- `PACKAGE_REGISTER.csv` row `PKG-062` — `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv`.
- `SCOPE_LEDGER.csv` rows `SOW-0153..0156` — same Gate-07 snapshot.
- `DELIVERABLE_REGISTER.csv` row `DEL-062-02_package-datasheet` — same Gate-07 snapshot.
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (this deliverable folder).
- Bid Docs/Budgetary RFQ `26020-01-PT-RFQ-18-003-LPG_Loading_Pumps.docx` — referenced by source row but **not locally accessible**; location TBD.
- `26020-Packages_Interfaces.3.xlsx` — referenced by source row; local file is `26020-Packages_Interfaces_4_export.xlsx` (filename/version mismatch — CONFLICT-2).
