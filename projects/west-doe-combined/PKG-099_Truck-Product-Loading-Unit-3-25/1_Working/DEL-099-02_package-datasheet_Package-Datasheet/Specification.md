# Specification — DEL-099-02 Package Datasheet (Truck Product Loading Unit 3-25)

Pass set: P1_P2 (drafted 2026-05-25 by TASK+four-documents)

## Scope

This specification governs the **EPC Integrator Package Datasheet** for `PKG-099 — Truck Product Loading Unit 3-25`, the technical handoff artifact that conveys package data required for third-party vendor or discipline package engineering and design of the `26020-03-PT-23-001 — Condensate Truck Loading Stations` package.

In scope:
- Package identification, design conditions, scope boundaries, equipment list, and interface applicability matrix (per `_Sources/26020-Package_Requirements.docx`).
- Required vendor engineering deliverable index (per source §Vendor Engineering Deliverables).
- Interface declarations consumed downstream by discipline packages (process piping, electrical, I&C, F&G, civil, structural).

Out of scope:
- Detailed mechanical design of the loading stations themselves (vendor scope).
- By-Others scope explicitly delegated in source (shipping, installation on piles, tie-in piping, electrical connection installation, platforms and stairs) — `_Sources/26020-Package_Requirements.docx` §Scope Notes.
- Standalone interface deliverables — per `_CONTEXT.md` Notes, "interface facts are intentionally carried here as evidence rather than standalone deliverables".

## Requirements

Numbering: `REQ-099-02-NN`. Each item cites source.

### Identification & Traceability

- **REQ-099-02-01** The datasheet SHALL identify the package by its vendor package tag `26020-03-PT-23-001` and project title `Condensate Truck Loading Stations`. (Source: `26020-Package_Requirements.docx` Heading1.)
- **REQ-099-02-02** The datasheet SHALL cite the RFQ source basis `RFQ/Bid Docs/26020-03-PT-RFQ-23-001_Truck_Load_stn_R0.docx`. (Source: §Source Basis.)
- **REQ-099-02-03** The datasheet SHALL identify the managing project as `26020-03 3-25 Liquids Hub`. (Source: §Location/Status.)

### Process / Functional Requirements

- **REQ-099-02-10** The package SHALL provide two (2) truck loading/unloading stations, each capable of loading two (2) trucks simultaneously (2x2). (Source: §Basic Scope, §Major Included Equipment.)
- **REQ-099-02-11** The package SHALL handle sweet dehydrated condensate received from the Condensate Storage Tanks via the Truck Loading pumps, metered at the station, and discharged into atmospheric condensate trucks. (Source: §Basic Scope.)
- **REQ-099-02-12** Design rate per station (loading or unloading) SHALL be 103 m³/h. (Source: §Scope Notes.)
- **REQ-099-02-13** Total Condensate Truck Loading Header design flow (across 4 lines) SHALL be 415 m³/h. (Source: §Scope Notes.)
- **REQ-099-02-14** Each station SHALL include solids filtration via a basket strainer; baseline specification: Sureflow `0300BF300SS`, 316SS, with mesh screen. (Source: §Major Included Equipment.)
- **REQ-099-02-15** Each station SHALL include an Emergency Shut Down Valve (ESDV). (Source: §Major Included Equipment.) Quantity per station/header: **TBD**.
- **REQ-099-02-16** Each station SHALL include flow transmitters for metering. (Source: §Major Included Equipment.) Accuracy class / custody-transfer category: **TBD**.

### Scope Boundary (By Others)

- **REQ-099-02-20** The following are explicitly **By Others** and SHALL NOT be priced or supplied by the package vendor: shipping packages to site; installation on piles; tie-in piping; electrical connections; mounting platform, stairs and similar access steel. (Source: §Scope Notes.)

### Interface Requirements (Applicability)

- **REQ-099-02-30** The package SHALL declare physical interface applicability per the matrix below; baseline values per `_Sources/26020-Package_Requirements.docx` §Physical Interface Summary (Datasheet §Physical Interface Summary table is the authoritative carrier within this deliverable). Required interfaces include: Process Piping, Drain/Containment, Electrical Power, Area/Exterior Lighting, Grounding/Bonding, I&C/Control Cabling, Fire & Gas/Safety Systems, Grading/Site Drainage/Spill Containment, Structural/Foundations/Supports, Product Loading.
- **REQ-099-02-31** Excluded interfaces (declared "No"): Utility Piping, Relief/Flare/Vent, EHT, Cathodic Protection, Communications/Network, Building HVAC, Maintenance Access (declared as "No"), Pipeline/Pigging. (Source: §Physical Interface Summary.)
- **REQ-099-02-32** Interface fact for Area/Exterior Lighting SHALL reference `26020-Packages_Interfaces.3.xlsx` column M (row 98) as the data source. (Source: §Physical Interface Summary, heading 18225.) ASSUMPTION: The Gate-7-published interface workbook now lives at `_Sources/26020-Packages_Interfaces_4_export.xlsx`; mapping of `.3.xlsx` → `_4_export.xlsx` row 98/col M to be reconciled — **TBD**.

### Vendor Engineering Deliverable Set

- **REQ-099-02-40** The vendor SHALL produce, at minimum, the deliverables enumerated in `_Sources/26020-Package_Requirements.docx` §Vendor Engineering Deliverables for `26020-03-PT-23-001`, organized into:
  - **Core vendor documents:** `PRQ-009` Vendor Document Index, `DOC-008` Vendor Document Control Procedure, `QLT-006` Supplier Quality Plan, `QLT-003` Inspection and Test Plan (ITP), `QLT-013` Material Test Reports / Certificates, `QLT-020` Inspection Release Certificate, `QLT-021` Manufacturing Record Book / Vendor Data Book, `PRQ-013` Logistics / Shipping Plan, `PRQ-015` Spare Parts Interchangeability Record (SPIR), `PRQ-016` Vendor Data Book / Final Supplier Documentation.
  - **Core package engineering:** `MEC-001` Mechanical Design Basis, `MEC-002` Mechanical Equipment List, `MEC-003` Mechanical Equipment Data Sheets, `MEC-006` Package Equipment Specifications, `MEC-014` Mechanical Calculation Package, `MEC-016` Equipment GA Drawing, `MEC-017` Equipment Installation / Setting Drawings, `MEC-018` Lifting / Handling Study, `MEC-021` Equipment FAT / Performance Test Procedure, `MEC-022` Equipment FAT / Performance Test Report, `MEC-023` Vendor Data Book / Mechanical Final Documentation, `MEC-024` Mechanical Spares / Special Tools Requirements, `MEC-025` Mechanical Equipment IOM Manual.
  - **Loading / metering package:** `INS-015` Metering Package Specification, `PRO-025` Operating Guidelines / Startup-Shutdown Narrative, `PIP-004` Tie-In List / Tie-In Scope Sheets, `PIP-018` Valve Data Sheets.
  - **Process piping interfaces:** `PRO-008` P&IDs, `PIP-003` Line List, `PIP-006` Equipment Arrangement / Piping GA, `PIP-007` Piping Plans and Sections, `PIP-008` Piping Isometric Drawings, `PIP-009` Fabrication Isometrics with BOM, `PIP-017` Piping MTO, `PIP-024` Hydrotest / Pressure Test Packages, `PIP-025` Flushing / Cleaning / Drying Procedure, `PIP-028` Piping As-Built Drawings.
  - **Drainage / containment interfaces:** `PRO-023` Process Sewer / Closed Drain Design Basis, `CIV-014` Bund / Dike / Secondary Containment Drawings.
  - **Electrical, lighting, EHT, grounding:** `ELE-002` Electrical Load List, `ELE-003` Single-Line Diagrams, `ELE-014` Cable Schedule, `ELE-015` Cable Tray / Routing Drawings, `ELE-016` Electrical Layout Drawings, `ELE-020` Electrical Equipment Data Sheets, `ELE-027` Electrical Installation Details, `ELE-028` Electrical Interconnection / Connection Diagrams, `ELE-029` Electrical FAT / SAT Procedure, `ELE-030` Electrical Test Records / Energization Package, `ELE-017` Lighting Layout Drawings, `ELE-012` Grounding / Earthing Study, `ELE-019` Earthing / Bonding Layout Drawings.
  - **Instrumentation and controls interfaces:** `INS-002` Instrument Index, `INS-003` Instrument Data Sheets, `INS-005` Instrument Location Plans, `INS-006` Hook-Up Drawings, `INS-008` Instrument Loop Diagrams, `INS-009` Wiring / Termination Diagrams, `INS-010` JB / Marshalling Drawings, `INS-011` Instrument Cable Schedule, `INS-016` Control Valve Data Sheets, `INS-017` On-Off / Shutdown Valve Data Sheets, `INS-018` Instrument I/O List, `INS-025` Instrument MTO, `INS-029` Instrument As-Built Drawings, `CTL-003` Control Narrative / Functional Specification, `CTL-005` Cause and Effect Matrix, `CTL-006` DCS I/O List, `CTL-026` Package Vendor Interface Specification.
  - **Fire and gas / technical safety interfaces:** `TSF-002` F&G Philosophy, `TSF-003` F&G Mapping Study, `TSF-004` F&G Detector Layout Drawings, `TSF-009` SIL Determination Report, `TSF-011` Safety Requirements Specification (SRS), `TSF-013` Supplier SIL Documentation / Safety Manual, `TSF-028` Emergency Response Plan Inputs.
  - **Structural, foundations, supports, access:** `STR-001` Structural Design Basis, `STR-002` Structural GA Drawings, `STR-004` Structural Calculation Package, `STR-005` Foundation Design Calculations, `STR-006` Foundation Drawings, `STR-011` Platform / Access Structure Drawings, `STR-012` Module Structural Drawings, `STR-013` Anchor Bolt / Embedment Drawings, `STR-014` Lifting Lug / Transport Analysis, `STR-020` Structural MTO.
  - **Civil grading / spill containment interfaces:** `CIV-003` Grading Plan, `CIV-004` Drainage / Stormwater Management Report, `CIV-015` Retention Pond / Containment Basin Design, `CIV-019` Civil MTO.

## Standards

- **STD-01** Vendor RFQ document — `RFQ/Bid Docs/26020-03-PT-RFQ-23-001_Truck_Load_stn_R0.docx`. **location TBD** (path not locally resolved).
- **STD-02** Project Package Requirements — `_Sources/26020-Package_Requirements.docx`, Heading1 `26020-03-PT-23-001`.
- **STD-03** Project Interface Workbook — `_Sources/26020-Packages_Interfaces_4_export.xlsx` (Gate 7 export); historical filename `26020-Packages_Interfaces.3.xlsx` referenced inline within source. Reconciliation **TBD**.
- **STD-04** Industry codes (atmospheric loading, custody-transfer metering, ESDV per applicable Provincial/Federal jurisdiction): **ASSUMPTION** — likely applicable, not enumerated in source.

## Verification

| Requirement | Verification Method | Evidence |
|---|---|---|
| REQ-099-02-01..03 (Identification) | Document review of Datasheet §Identification against source Heading1 | Datasheet, source `26020-Package_Requirements.docx` |
| REQ-099-02-10..11 (Function & station count) | Document review against §Basic Scope and §Major Included Equipment | Datasheet §Attributes / §Major Included Equipment |
| REQ-099-02-12..13 (Design flows) | Cross-check Datasheet §Design Conditions against source §Scope Notes | Datasheet §Design Conditions |
| REQ-099-02-14..16 (Strainer / ESDV / Flow Tx) | Vendor Mechanical Equipment Data Sheets (`MEC-003`); ITP (`QLT-003`); FAT (`MEC-021/022`) | Vendor deliverables |
| REQ-099-02-20 (By Others) | Bid-stage scope confirmation, vendor pricing exclusion list | Vendor RFQ response |
| REQ-099-02-30..32 (Interfaces) | Cross-check Datasheet §Physical Interface Summary against source `26020-Packages_Interfaces_4_export.xlsx` row 98 | Interface workbook |
| REQ-099-02-40 (Vendor doc set) | Vendor Document Index (`PRQ-009`) review at kickoff | `PRQ-009` |

## Documentation

Anticipated artifacts (from `_CONTEXT.md`):

- Package technical datasheet (this Datasheet.md plus formally issued vendor datasheet — `MEC-003`).
- Vendor engineering handoff basis (this Specification.md plus RFQ package).
- Package interface requirements matrix (Datasheet §Physical Interface Summary).
- Source-supported equipment and design criteria (Datasheet §Major Included Equipment, §Design Conditions).
