# Datasheet: DEL-051-05 — Vendor Document Turnover Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-051-05_vendor-document-turnover-package` | `_CONTEXT.md` |
| Name | Vendor Document Turnover Package | `_CONTEXT.md` |
| ParentPackage | `PKG-051` — Process Heat Medium Unit | `_CONTEXT.md` |
| Tagged Equipment ID | `26020-01-PT-15-001` | `26020-Package_Requirements.docx` §6 (Process Heat Medium Unit) |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | Vendor Document Turnover | `_CONTEXT.md` |
| Responsible Party | Package Vendor (vendor documentation); EPC Integrator (interface/integration review) | `_CONTEXT.md` |
| Covers Scope Items | `SOW-0165`, `SOW-0166`, `SOW-0167`, `SOW-0168` | `_CONTEXT.md` |
| Supports Objectives | `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION: PACKAGE_HEURISTIC association) | `OBJECTIVE_DELIVERABLE_MAP.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Document Register Scope | Vendor-supplied engineering, quality, fabrication, FAT/SAT, IOM, spares, and final data-book records for the Process Heat Medium Unit package | `26020-Package_Requirements.docx` §6 Vendor Engineering Deliverables |
| Register Categories | Core vendor documents; Core package engineering; Rotating equipment / pumps; Heat transfer equipment; Process package design; Utility piping interfaces; Drainage / containment interfaces; Electrical, lighting, EHT, grounding; Instrumentation and controls; Fire and gas / technical safety; Structural, foundations, supports, access | `26020-Package_Requirements.docx` §6 |
| Submittal Cadence | TBD (not stated in accessible source slice) | TBD |
| Turnover Trigger | Mechanical completion / FAT-SAT acceptance and shipment per Logistics/Shipping Plan (PRQ-013) | `26020-Package_Requirements.docx` §6 (PRQ-013, MEC-023, PRQ-016) |
| Final Vendor Data Book Items | PRQ-016 Vendor Data Book / Final Supplier Documentation; MEC-023 Vendor Data Book / Mechanical Final Documentation | `26020-Package_Requirements.docx` §6 |
| EPC Review Role | Interface/integration review of vendor documents against EPC Scope of Work (DEL-051-01) and Package Datasheet (DEL-051-02) | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-051-05 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Applicable Package | `26020-01-PT-15-001` — Process Heat Medium Unit | `26020-Package_Requirements.docx` §6 |
| Location / Status Basis | "4-25 West Doe Deepcut; vetted package scope basis" | `26020-Package_Requirements.docx` §6 Location/Status |
| Vendor Document Index Required | Yes — PRQ-009 Vendor Document Index is a core vendor deliverable | `26020-Package_Requirements.docx` §6 |
| Document Control Procedure | Yes — DOC-008 Vendor Document Control Procedure | `26020-Package_Requirements.docx` §6 |
| Quality Plan / ITP | QLT-006 Supplier Quality Plan; QLT-003 Inspection and Test Plan | `26020-Package_Requirements.docx` §6 |
| MTR / Certificates | QLT-013 Material Test Reports / Certificates | `26020-Package_Requirements.docx` §6 |
| Inspection Release | QLT-020 Inspection Release Certificate | `26020-Package_Requirements.docx` §6 |
| Manufacturing Record Book | QLT-021 Manufacturing Record Book / Vendor Data Book | `26020-Package_Requirements.docx` §6 |
| Spare Parts Record | PRQ-015 Spare Parts Interchangeability Record (SPIR) | `26020-Package_Requirements.docx` §6 |
| Code Registration | REG-022 Pressure Equipment Registration Package (heat transfer equipment) | `26020-Package_Requirements.docx` §6 |

## Construction (Document Register Contents)

The turnover register comprises the vendor-engineering deliverable codes assembled below. All entries are sourced verbatim from `26020-Package_Requirements.docx` §6 (Process Heat Medium Unit — Vendor Engineering Deliverables).

### Core vendor documents
- PRQ-009 Vendor Document Index
- DOC-008 Vendor Document Control Procedure
- QLT-006 Supplier Quality Plan
- QLT-003 Inspection and Test Plan (ITP)
- QLT-013 Material Test Reports / Certificates
- QLT-020 Inspection Release Certificate
- QLT-021 Manufacturing Record Book / Vendor Data Book
- PRQ-013 Logistics / Shipping Plan
- PRQ-015 Spare Parts Interchangeability Record (SPIR)
- PRQ-016 Vendor Data Book / Final Supplier Documentation

### Core package engineering
- MEC-001 Mechanical Design Basis
- MEC-002 Mechanical Equipment List
- MEC-003 Mechanical Equipment Data Sheets
- MEC-006 Package Equipment Specifications
- MEC-014 Mechanical Calculation Package
- MEC-016 Equipment General Arrangement Drawing
- MEC-017 Equipment Installation / Setting Drawings
- MEC-018 Lifting / Handling Study for Major Equipment
- MEC-021 Equipment FAT / Performance Test Procedure
- MEC-022 Equipment FAT / Performance Test Report
- MEC-023 Vendor Data Book / Mechanical Final Documentation
- MEC-024 Mechanical Spares / Special Tools Requirements
- MEC-025 Mechanical Equipment IOM Manual

### Rotating equipment / pumps
- MEC-004 Rotating Equipment Specifications
- MEC-007 Pump Data Sheets
- MEC-019 Mechanical Seal / Lube Oil Specification
- PRO-013 Pump Hydraulic / NPSH Calculations
- ELE-011 Motor Starting Study

### Heat transfer equipment
- MEC-005 Static Equipment Specifications
- MEC-010 Heat Exchanger Data Sheets
- REG-022 Pressure Equipment Registration Package

### Process package design
- PRO-004 Process Flow Diagram (PFD)
- PRO-005 Heat and Material Balance
- PRO-007 Process Description / Operating Philosophy
- PRO-008 Piping and Instrumentation Diagrams (P&IDs)
- PRO-010 Major Equipment Process Data Sheets
- PRO-011 Utility Summary / Utility Consumption Report
- PRO-012 Line Sizing / Hydraulic Calculation Package
- PRO-020 Process Control Philosophy
- PRO-025 Operating Guidelines / Startup-Shutdown Narrative
- PRO-026 HAZOP / PHA Technical Input Package
- PRO-027 Process Safety Information (PSI) Package
- PRO-028 Process As-Built PFD/P&ID Package

### Utility piping interfaces
- PIP-003 Piping Line List
- PIP-008 Piping Isometric Drawings
- PIP-017 Piping MTO / Material Take-Off
- PIP-024 Hydrotest / Pressure Test Packages

### Drainage / containment interfaces
- PRO-023 Process Sewer / Closed Drain Design Basis
- CIV-014 Bund / Dike / Secondary Containment Drawings

### Electrical, lighting, EHT, grounding
- ELE-002 Electrical Load List / Consumer List
- ELE-003 Single-Line Diagrams (SLDs)
- ELE-014 Cable Schedule
- ELE-015 Cable Tray / Routing Drawings
- ELE-016 Electrical Layout Drawings
- ELE-020 Electrical Equipment Data Sheets
- ELE-027 Electrical Installation Details
- ELE-028 Electrical Interconnection / Connection Diagrams
- ELE-029 Electrical FAT / SAT Procedure
- ELE-030 Electrical Test Records / Energization Package
- ELE-017 Lighting Layout Drawings
- ELE-012 Grounding / Earthing Study
- ELE-019 Earthing / Bonding Layout Drawings

### Instrumentation and controls
- INS-002 Instrument Index
- INS-003 Instrument Data Sheets
- INS-005 Instrument Location Plans
- INS-006 Instrument Hook-Up Drawings
- INS-008 Instrument Loop Diagrams
- INS-009 Instrument Wiring / Termination Diagrams
- INS-010 Junction Box / Marshalling Drawings
- INS-011 Instrument Cable Schedule
- INS-016 Control Valve Data Sheets
- INS-017 On-Off / Shutdown Valve Data Sheets
- INS-018 Instrument I/O List
- INS-025 Instrument MTO / Quantity Take-Off
- INS-029 Instrument As-Built Drawings
- CTL-003 Control Narrative / Functional Specification
- CTL-005 Cause and Effect Matrix
- CTL-006 DCS I/O List
- CTL-026 Package Vendor Interface Specification

### Fire and gas / technical safety
- TSF-002 Fire and Gas Philosophy
- TSF-003 Fire and Gas Mapping Study
- TSF-004 Fire and Gas Detector Layout Drawings
- TSF-009 SIL Determination Report
- TSF-011 Safety Requirements Specification (SRS)
- TSF-013 Supplier SIL Documentation / Safety Manual
- TSF-028 Emergency Response Plan Inputs

### Structural, foundations, supports, access
- STR-001 Structural Design Basis
- STR-002 Structural General Arrangement Drawings
- STR-004 Structural Calculation Package
- STR-005 Foundation Design Calculations
- STR-006 Foundation Drawings
- STR-011 Platform / Access Structure Drawings
- STR-012 Module Structural Drawings
- STR-013 Anchor Bolt / Embedment Drawings
- STR-014 Lifting Lug / Transport Analysis
- STR-020 Structural MTO / Quantity Take-Off

## References

- `26020-Package_Requirements.docx` §6 — Process Heat Medium Unit (Vendor Engineering Deliverables; Location/Status; Basic Scope; Physical Interface Summary)
- `_CONTEXT.md` — deliverable identity, scope, anticipated artifacts
- `_REFERENCES.md` — authoritative basis pointers
- `DELIVERABLE_REGISTER.csv` (GATE-07 snapshot) — DEL-051-05 row
- `OBJECTIVE_DELIVERABLE_MAP.csv` (GATE-07 snapshot) — objective association (PACKAGE_HEURISTIC; ASSUMPTION)
- `26020-Packages_Interfaces_4_export.xlsx` — interface table (row 79 cited in source)
