# Datasheet — DEL-062-05 Vendor Document Turnover Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-062-05_vendor-document-turnover-package` | `_CONTEXT.md` Identity |
| Name | Vendor Document Turnover Package | `_CONTEXT.md` Identity |
| ParentPackageID | `PKG-062` | `_CONTEXT.md` Identity |
| PackageName | NGL Loading Pumps Building | `_CONTEXT.md` Identity |
| Discipline | Mechanical | `_CONTEXT.md` Identity |
| Type | Vendor Document Turnover | `_CONTEXT.md` Identity |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `_CONTEXT.md` Identity |
| Source package heading | `26020-01-PT-18-003 — LPG Loading Pumps` (Heading 1 #16) | `_Sources/26020-Package_Requirements.docx` Heading 1 #16 |
| Covers Scope Items | SOW-0153; SOW-0154; SOW-0155; SOW-0156 | `_CONTEXT.md` Covers Scope Items |
| Supports Objectives | OBJ-001, OBJ-003 through OBJ-010 (PACKAGE_HEURISTIC, ASSUMPTION) | `_CONTEXT.md` Supports Objectives |

> **Naming note (see Guidance Conflict Table C-01):** the deliverable's parent package is decomposed as `NGL Loading Pumps Building` (`_CONTEXT.md`), but source heading 16 names the equipment package `LPG Loading Pumps` (`26020-01-PT-18-003`). These are treated as the same package per decomposition mapping; the LPG/NGL service-fluid naming is flagged for human ruling.

## Attributes — Package Configuration Context (from source)

| Attribute | Value | Source |
|---|---|---|
| Configuration | 4 × identical pumps in parallel | `26020-Package_Requirements.docx` heading 16 → Basic Scope |
| Pump model | Blackmer Model LGL4B Rotary Vane Pumps | heading 16 → Basic Scope, Major Included Equipment |
| Tag identifiers | P9510/20/30/40-1 | heading 16 → Major Included Equipment |
| Per-pump capacity | 68 m³/hr @ 345 kPad (300 USGPM @ 50 psid) — TBC TDH | heading 16 → Major Included Equipment; Scope Notes / Open Items |
| Process function | Move LPG product from storage to LPG Truck Loading | heading 16 → Basic Scope |
| Driver | Electric 575 V / 3 PH / 60 Hz motors, fed from 600 V MCC; local control (H-O-A or On-Off switch) | heading 16 → Scope Notes / Open Items |
| Motor sizing basis | Sized for inlet stabilizer composition density at -40 °C start-up condition | heading 16 → Scope Notes / Open Items |
| Building | Self-framing building to be erected at site | heading 16 → Major Included Equipment |
| Operating / design conditions | TBC — see capacity / site conditions | heading 16 → Scope Notes / Open Items |
| Location / Status | 4-25 West Doe Deepcut; budgetary RFQ basis; vetted package scope basis | heading 16 → Location / Status table |
| Source basis | `Bid Docs/Budgetary/26020-01-PT-RFQ-18-003-LPG_Loading_Pumps.docx` | heading 16 → Source Basis table |
| Scope exclusions (by others) | DCS integration, foundations, electrical supply to MCC | heading 16 → Scope Notes / Open Items |

These attributes are package-level context; the deliverable defined here is the *vendor document turnover package* covering the documentation for the equipment above.

## Documents in Turnover Scope — Source Vendor Document Table (heading 16, Vendor Engineering Deliverables)

The following document IDs are the source-declared vendor deliverables for the PKG-062 LPG/NGL Loading Pumps package, grouped as in the source. The Vendor Document Turnover Package collects, registers, and turns over evidence for these documents.

### Core vendor documents
| ID | Name |
|---|---|
| PRQ-009 | Vendor Document Index |
| DOC-008 | Vendor Document Control Procedure |
| QLT-006 | Supplier Quality Plan |
| QLT-003 | Inspection and Test Plan (ITP) |
| QLT-013 | Material Test Reports / Certificates |
| QLT-020 | Inspection Release Certificate |
| QLT-021 | Manufacturing Record Book / Vendor Data Book |
| PRQ-013 | Logistics / Shipping Plan |
| PRQ-015 | Spare Parts Interchangeability Record (SPIR) |
| PRQ-016 | Vendor Data Book / Final Supplier Documentation |

### Core package engineering
| ID | Name |
|---|---|
| MEC-001 | Mechanical Design Basis |
| MEC-002 | Mechanical Equipment List |
| MEC-003 | Mechanical Equipment Data Sheets |
| MEC-006 | Package Equipment Specifications |
| MEC-014 | Mechanical Calculation Package |
| MEC-016 | Equipment General Arrangement Drawing |
| MEC-017 | Equipment Installation / Setting Drawings |
| MEC-018 | Lifting / Handling Study for Major Equipment |
| MEC-021 | Equipment FAT / Performance Test Procedure |
| MEC-022 | Equipment FAT / Performance Test Report |
| MEC-023 | Vendor Data Book / Mechanical Final Documentation |
| MEC-024 | Mechanical Spares / Special Tools Requirements |
| MEC-025 | Mechanical Equipment IOM Manual |

### Rotating equipment / pumps
| ID | Name |
|---|---|
| MEC-004 | Rotating Equipment Specifications |
| MEC-007 | Pump Data Sheets |
| MEC-019 | Mechanical Seal / Lube Oil Specification |
| PRO-013 | Pump Hydraulic / NPSH Calculations |
| ELE-011 | Motor Starting Study |

### Loading / metering package
| ID | Name |
|---|---|
| INS-015 | Metering Package Specification |
| PRO-025 | Operating Guidelines / Startup-Shutdown Narrative |
| PIP-004 | Tie-In List / Tie-In Scope Sheets |
| PIP-018 | Valve Data Sheets |

### Relief / flare / vent design
| ID | Name |
|---|---|
| PRO-014 | Relief and Flare Design Basis |
| PRO-015 | PSV / Pressure Relief Sizing Calculations |
| PRO-016 | Relief Valve Data Sheets |
| PRO-017 | Flare Load Summary / Flare System Study |
| PRO-018 | Blowdown / Depressurization Study |

### Process piping interfaces
| ID | Name |
|---|---|
| PRO-008 | Piping and Instrumentation Diagrams (P&IDs) |
| PIP-003 | Piping Line List |
| PIP-006 | Equipment Arrangement / Piping General Arrangement |
| PIP-007 | Piping Plans and Sections |
| PIP-008 | Piping Isometric Drawings |
| PIP-009 | Fabrication Isometrics with BOM |
| PIP-017 | Piping MTO / Material Take-Off |
| PIP-024 | Hydrotest / Pressure Test Packages |
| PIP-025 | Flushing / Cleaning / Drying Procedure |
| PIP-028 | Piping As-Built Drawings |

### Utility piping interfaces
| ID | Name |
|---|---|
| PRO-011 | Utility Summary / Utility Consumption Report |

### Drainage / containment interfaces
| ID | Name |
|---|---|
| PRO-023 | Process Sewer / Closed Drain Design Basis |
| CIV-014 | Bund / Dike / Secondary Containment Drawings |

### Electrical, lighting, EHT, grounding
| ID | Name |
|---|---|
| ELE-002 | Electrical Load List / Consumer List |
| ELE-003 | Single-Line Diagrams (SLDs) |
| ELE-014 | Cable Schedule |
| ELE-015 | Cable Tray / Routing Drawings |
| ELE-016 | Electrical Layout Drawings |
| ELE-020 | Electrical Equipment Data Sheets |
| ELE-027 | Electrical Installation Details |
| ELE-028 | Electrical Interconnection / Connection Diagrams |
| ELE-029 | Electrical FAT / SAT Procedure |
| ELE-030 | Electrical Test Records / Energization Package |
| ELE-017 | Lighting Layout Drawings |
| ELE-018 | Electrical Heat Tracing Design Package |
| PIP-020 | Piping Insulation / Heat Tracing Schedule |
| PIP-021 | Piping Heat Tracing Interface Package |
| ELE-012 | Grounding / Earthing Study |
| ELE-019 | Earthing / Bonding Layout Drawings |

### Instrumentation and controls interfaces
| ID | Name |
|---|---|
| INS-002 | Instrument Index |
| INS-003 | Instrument Data Sheets |
| INS-005 | Instrument Location Plans |
| INS-006 | Instrument Hook-Up Drawings |
| INS-008 | Instrument Loop Diagrams |
| INS-009 | Instrument Wiring / Termination Diagrams |
| INS-010 | Junction Box / Marshalling Drawings |
| INS-011 | Instrument Cable Schedule |
| INS-016 | Control Valve Data Sheets |
| INS-017 | On-Off / Shutdown Valve Data Sheets |
| INS-018 | Instrument I/O List |
| INS-025 | Instrument MTO / Quantity Take-Off |
| INS-029 | Instrument As-Built Drawings |
| CTL-003 | Control Narrative / Functional Specification |
| CTL-005 | Cause and Effect Matrix |
| CTL-006 | DCS I/O List |
| CTL-026 | Package Vendor Interface Specification |

### Building / HVAC / code interfaces
| ID | Name |
|---|---|
| PRO-024 | Ventilation / Process Safety Equipment Inputs |
| TSF-023 | Building Siting / Occupied Building Risk Assessment |
| REG-021 | Fire Code / Building Code Compliance Package |
| STR-002 | Structural General Arrangement Drawings |
| STR-012 | Module Structural Drawings |

### Fire and gas / technical safety interfaces
| ID | Name |
|---|---|
| TSF-002 | Fire and Gas Philosophy |
| TSF-003 | Fire and Gas Mapping Study |
| TSF-004 | Fire and Gas Detector Layout Drawings |
| TSF-009 | SIL Determination Report |
| TSF-011 | Safety Requirements Specification (SRS) |
| TSF-013 | Supplier SIL Documentation / Safety Manual |
| TSF-028 | Emergency Response Plan Inputs |

### Structural, foundations, supports, access
| ID | Name |
|---|---|
| STR-001 | Structural Design Basis |
| STR-004 | Structural Calculation Package |
| STR-005 | Foundation Design Calculations |
| STR-006 | Foundation Drawings |
| STR-011 | Platform / Access Structure Drawings |
| STR-013 | Anchor Bolt / Embedment Drawings |
| STR-014 | Lifting Lug / Transport Analysis |
| STR-020 | Structural MTO / Quantity Take-Off |

## Physical Interface Applicability (from source heading 16)

| Interface Type | Applicability | Notes |
|---|---|---|
| Process Piping | Yes | |
| Utility Piping | Yes | |
| Relief / Flare / Vent | Yes | |
| Drain / Containment | Yes | |
| Electrical Power | Yes | |
| Area / Exterior Lighting | Yes | `26020-Packages_Interfaces.3.xlsx` column M (row 76) |
| EHT | Yes | |
| Grounding / Bonding | Yes | |
| Cathodic Protection | No | |
| I&C / Control Cabling | Yes | |
| Communications / Network | No | |
| Building HVAC / Services | Yes | |
| Fire & Gas / Safety Systems | Yes | |
| Maintenance Access | Yes | |
| Grading / Site Drainage / Spill Containment | No | |
| Structural / Foundations / Supports | Yes | |
| Product Loading | No | |
| Pipeline / Pigging | No | |

Source: `26020-Package_Requirements.docx` heading 16 → Physical Interface Summary.

## Conditions

| Field | Value | Source |
|---|---|---|
| Submittal stages | Bid, IFR, IFA, IFC, As-Built / Final | ASSUMPTION (industry-typical; not stated in heading 16). TBD against DOC-008 when issued. |
| Review cycle | EPC Integrator review per DOC-008 | TBD (DOC-008 not yet issued) |
| Transmittal medium | TBD (vendor portal vs. controlled file transfer) | TBD |
| Document numbering | Vendor-native numbering aligned to vendor document index (PRQ-009) | source: PRQ-009 listed in heading 16 vendor deliverables |
| Turnover package medium | Vendor Data Book (PRQ-016 / MEC-023) plus electronic transmittal | source: PRQ-016, MEC-023 listed in heading 16 |
| Interface Coordination Notes (source) | TBD per source heading 16 → Interface Coordination Notes | heading 16 (source explicitly TBD) |

## Construction (turnover package composition)

| Element | Content | Source |
|---|---|---|
| Vendor Document Index | Master list of all vendor documents in scope, with revision status, transmittal dates, and review state | source: PRQ-009 in heading 16 |
| Vendor Document Control Procedure | Vendor-issued procedure governing identification, numbering, revision, transmittal, and acceptance | source: DOC-008 in heading 16 |
| Document submittals | Each vendor document at the contractually required revision (Bid/IFR/IFA/IFC/As-Built) | ASSUMPTION on stage labels; document set per heading 16 vendor deliverables |
| Turnover records | Inspection Release Certificate (QLT-020), Manufacturing Record Book / Vendor Data Book (QLT-021), Final Supplier Documentation (PRQ-016), Mechanical Final Documentation (MEC-023), Logistics / Shipping Plan (PRQ-013), SPIR (PRQ-015) | source: heading 16 vendor deliverables |
| Quality and inspection evidence | Supplier Quality Plan (QLT-006), ITP (QLT-003), Material Test Reports / Certificates (QLT-013) | source: heading 16 vendor deliverables |

## References

- `_Sources/26020-Package_Requirements.docx`, Heading 1 #16 `26020-01-PT-18-003 — LPG Loading Pumps` (Basic Scope, Major Included Equipment, Physical Interface Summary, Vendor Engineering Deliverables table, Location/Status, Source Basis, Scope Notes / Open Items, Interface Coordination Notes).
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` (referenced by source as `26020-Packages_Interfaces.3.xlsx`; locally accessible export version present at shared sources root — naming discrepancy noted, see Conflict Table in Guidance).
- `_REFERENCES.md` (deliverable-local).
- `_CONTEXT.md` (deliverable-local).
- GATE-07 snapshot: `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`.
