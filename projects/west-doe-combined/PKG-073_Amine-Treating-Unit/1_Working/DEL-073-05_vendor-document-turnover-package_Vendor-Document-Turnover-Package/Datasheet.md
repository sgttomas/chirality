# Datasheet — DEL-073-05 Vendor Document Turnover Package (PKG-073)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-073-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-073` |
| Package Name | Amine Treating Unit |
| Workbook Tag | `26020-01-27-001` (PACKAGE_REGISTER row 49) |
| Discipline | Mechanical |
| WBS | 01 |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| Covers Scope Items | `SOW-0051`, `SOW-0052`, `SOW-0053`, `SOW-0054` |
| Supports Objectives | `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION: PACKAGE_HEURISTIC mapping by package; not individually confirmed at deliverable-ID level) |

## Attributes

The deliverable is a document set rather than a physical artifact. Attribute values describe the document register that the Package Vendor must deliver and the EPC Integrator must accept.

| Attribute | Value | Source |
|---|---|---|
| Document register basis | Per-package `Vendor Engineering Deliverables` list defined in source `26020-Package_Requirements.docx` for the Amine Treating Unit (heading 27) | `_Sources/26020-Package_Requirements.docx`, "26020-01-PT-27-001 - Amine Treating Unit" / "Vendor Engineering Deliverables" |
| Document control procedure | Vendor Document Control Procedure (`DOC-008`) required as core vendor document | same as above, "Core vendor documents" |
| Index | Vendor Document Index (`PRQ-009`) required as core vendor document | same as above |
| Final book | Vendor Data Book / Final Supplier Documentation (`PRQ-016`); mechanical final book `MEC-023` | same as above |
| Quality records | Supplier Quality Plan `QLT-006`; ITP `QLT-003`; MTRs/Certificates `QLT-013`; Inspection Release Certificate `QLT-020`; Manufacturing Record Book / VDB `QLT-021` | same as above |
| Logistics records | Logistics / Shipping Plan `PRQ-013`; SPIR `PRQ-015` | same as above |
| Discipline applicability | Mechanical-led process package (MDEA absorption/regeneration); process, pressure-equipment, piping, electrical, I&C, relief/flare, drainage, structural document classes all enumerated in source heading 27 | `_Sources/26020-Package_Requirements.docx` heading 27 |
| Coverage | Four SOW items: `SOW-0051`, `SOW-0052`, `SOW-0053`, `SOW-0054` | `DELIVERABLE_REGISTER.csv` row 262 |
| Source basis pointer | `Bid Docs/Budgetary/26020-01-PT-RFQ-27-001_Amine_Treat_Unit_R0.docx` (referenced by package heading 27; not present as a separate slice in `_Sources/`) | `_Sources/26020-Package_Requirements.docx` heading 27 Source Basis |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Lifecycle stage at acceptance | Post-FAT through turnover, including as-built records | `_Sources/26020-Package_Requirements.docx` heading 27 (PIP-028 As-Built; MEC-022 FAT Report; ELE-030 Energization Package) |
| Site basis affecting documentation | Cold-climate West Doe Deepcut site; design ambient -40 °C min / +35 °C max; extreme ambient -49.2 °C / +38.9 °C; vendor data must reflect ambient and electrical-area conditions per facility design basis | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 196–198; `_Sources/26020-Package_Requirements.docx` heading 27 |
| Acceptance gate | EPC Integrator interface/integration review and acceptance via `DEL-073-06` | `DELIVERABLE_REGISTER.csv` rows 262, 263 |
| Submittal cadence | TBD — not stated in accessible source slices |
| Native file format requirements | TBD — not stated in accessible source slices |
| Vendor scope (process) | Complete Amine Treating Unit (ATU) removing H₂S and CO₂ from sour natural gas using continuous MDEA absorption-regeneration across two modules: Amine Gas Sweetening and Amine Regeneration | `_Sources/26020-Package_Requirements.docx` heading 27 "Basic Scope" |

## Construction

The "construction" of this deliverable is the assembly and turnover of a vendor document set. The composing document classes are taken directly from `_Sources/26020-Package_Requirements.docx` heading 27 "Vendor Engineering Deliverables" template for the Amine Treating Unit.

**Core vendor documents (always required):**

- `PRQ-009` Vendor Document Index
- `DOC-008` Vendor Document Control Procedure
- `QLT-006` Supplier Quality Plan
- `QLT-003` Inspection and Test Plan (ITP)
- `QLT-013` Material Test Reports / Certificates
- `QLT-020` Inspection Release Certificate
- `QLT-021` Manufacturing Record Book / Vendor Data Book
- `PRQ-013` Logistics / Shipping Plan
- `PRQ-015` Spare Parts Interchangeability Record (SPIR)
- `PRQ-016` Vendor Data Book / Final Supplier Documentation

**Core package engineering (mechanical):**

- `MEC-001` Mechanical Design Basis
- `MEC-002` Mechanical Equipment List
- `MEC-003` Mechanical Equipment Data Sheets
- `MEC-006` Package Equipment Specifications
- `MEC-014` Mechanical Calculation Package
- `MEC-016` Equipment General Arrangement Drawing
- `MEC-017` Equipment Installation / Setting Drawings
- `MEC-018` Lifting / Handling Study for Major Equipment
- `MEC-021` Equipment FAT / Performance Test Procedure
- `MEC-022` Equipment FAT / Performance Test Report
- `MEC-023` Vendor Data Book / Mechanical Final Documentation
- `MEC-024` Mechanical Spares / Special Tools Requirements
- `MEC-025` Mechanical Equipment IOM Manual

**Static pressure equipment:**

- `MEC-005` Static Equipment Specifications
- `MEC-009` Pressure Vessel Data Sheets
- `REG-022` Pressure Equipment Registration Package

**Process package design:**

- `PRO-004` Process Flow Diagram (PFD)
- `PRO-005` Heat and Material Balance
- `PRO-007` Process Description / Operating Philosophy
- `PRO-008` Piping and Instrumentation Diagrams (P&IDs)
- `PRO-010` Major Equipment Process Data Sheets
- `PRO-011` Utility Summary / Utility Consumption Report
- `PRO-012` Line Sizing / Hydraulic Calculation Package
- `PRO-020` Process Control Philosophy
- `PRO-025` Operating Guidelines / Startup-Shutdown Narrative
- `PRO-026` HAZOP / PHA Technical Input Package
- `PRO-027` Process Safety Information (PSI) Package
- `PRO-028` Process As-Built PFD/P&ID Package

**Relief / flare / vent design:**

- `PRO-014` Relief and Flare Design Basis
- `PRO-015` PSV / Pressure Relief Sizing Calculations
- `PRO-016` Relief Valve Data Sheets
- `PRO-017` Flare Load Summary / Flare System Study
- `PRO-018` Blowdown / Depressurization Study

**Process piping interfaces:**

- `PIP-003` Piping Line List
- `PIP-004` Tie-In List / Tie-In Scope Sheets
- `PIP-006` Equipment Arrangement / Piping General Arrangement
- `PIP-007` Piping Plans and Sections
- `PIP-008` Piping Isometric Drawings
- `PIP-009` Fabrication Isometrics with BOM
- `PIP-017` Piping MTO / Material Take-Off
- `PIP-018` Valve Data Sheets
- `PIP-024` Hydrotest / Pressure Test Packages
- `PIP-025` Flushing / Cleaning / Drying Procedure
- `PIP-028` Piping As-Built Drawings

**Drainage / containment interfaces:**

- `PRO-023` Process Sewer / Closed Drain Design Basis
- `CIV-014` Bund / Dike / Secondary Containment Drawings

**Electrical, lighting, EHT, grounding:**

- `ELE-002` Electrical Load List / Consumer List
- `ELE-003` Single-Line Diagrams (SLDs)
- `ELE-014` Cable Schedule
- `ELE-015` Cable Tray / Routing Drawings
- `ELE-016` Electrical Layout Drawings
- `ELE-020` Electrical Equipment Data Sheets
- `ELE-027` Electrical Installation Details
- `ELE-028` Electrical Interconnection / Connection Diagrams
- `ELE-029` Electrical FAT / SAT Procedure
- `ELE-030` Electrical Test Records / Energization Package
- `ELE-017` Lighting Layout Drawings
- `ELE-018` Electrical Heat Tracing Design Package
- `PIP-020` Piping Insulation / Heat Tracing Schedule
- `PIP-021` Piping Heat Tracing Interface Package
- `ELE-012` Grounding / Earthing Study
- `ELE-019` Earthing / Bonding Layout Drawings

**Instrumentation and controls interfaces:**

- `INS-002` Instrument Index
- `INS-003` Instrument Data Sheets
- `INS-005` Instrument Location Plans
- `INS-006` Instrument Hook-Up Drawings
- `INS-008` Instrument Loop Diagrams
- `INS-009` Instrument Wiring / Termination Diagrams
- `INS-010` Junction Box / Marshalling Drawings
- `INS-011` Instrument Cable Schedule
- `INS-016` Control Valve Data Sheets
- `INS-017` On-Off / Shutdown Valve Data Sheets
- `INS-018` Instrument I/O List
- `INS-025` Instrument MTO / Quantity Take-Off
- `INS-029` Instrument As-Built Drawings
- `CTL-003` Control Narrative / Functional Specification
- `CTL-005` Cause and Effect Matrix
- `CTL-006` DCS I/O List
- `CTL-026` Package Vendor Interface Specification

**Fire and gas / technical safety interfaces:**

- `TSF-002` Fire and Gas Philosophy
- `TSF-003` Fire and Gas Mapping Study
- `TSF-004` Fire and Gas Detector Layout Drawings
- `TSF-009` SIL Determination Report
- `TSF-011` Safety Requirements Specification (SRS)
- `TSF-013` Supplier SIL Documentation / Safety Manual
- `TSF-028` Emergency Response Plan Inputs

**Structural, foundations, supports, access:**

- `STR-001` Structural Design Basis
- `STR-002` Structural General Arrangement Drawings
- `STR-004` Structural Calculation Package
- `STR-005` Foundation Design Calculations
- `STR-006` Foundation Drawings
- `STR-011` Platform / Access Structure Drawings
- `STR-012` Module Structural Drawings
- `STR-013` Anchor Bolt / Embedment Drawings
- `STR-014` Lifting Lug / Transport Analysis
- `STR-020` Structural MTO / Quantity Take-Off

Refer to `Specification.md` for the binding discipline applicability rules and verification mapping. Note: the source heading 27 list omits "Rotating equipment / compressors" and "Rotating equipment / pumps" subsections that appear in other package templates; per source the ATU set is the enumeration above, not a superset.

## References

- Gate 7 PROJECT_DECOMP snapshot deliverable row: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`, row 262 (`DEL-073-05_vendor-document-turnover-package`)
- Gate 7 PROJECT_DECOMP snapshot package row: `.../PACKAGE_REGISTER.csv`, row 49 (`PKG-073`, tag `26020-01-27-001`, "Amine Treating Unit")
- `_Sources/26020-Package_Requirements.docx` — heading 27 "26020-01-PT-27-001 - Amine Treating Unit" (Basic Scope, Major Included Equipment, Physical Interface Summary, Vendor Engineering Deliverables)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — facility design basis (MDEA amine treating cited at line 41; site ambient at lines 196–198)
- Deliverable-local: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
