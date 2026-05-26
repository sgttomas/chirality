# Datasheet: DEL-079-02 — Package Datasheet (Instrument Air Building, PKG-079)

> Epistemic note: All values cited below are drawn from the locally accessible source slices listed under **References**. Where the source explicitly defers a value to the vendor or does not state one, the field is marked `TBD`. Inferences are labeled `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-079-02_package-datasheet` | `_CONTEXT.md` |
| Deliverable Name | Package Datasheet | `_CONTEXT.md` |
| Parent Package ID | `PKG-079` | `_CONTEXT.md` |
| Parent Workbook ID | 79 | `_CONTEXT.md` |
| Package Name | Instrument Air Building | `_CONTEXT.md` |
| Package CoA Tracking Number | `26020-01-39-001` | `26020-Packages_Interfaces_4_export.xlsx` sheet `Packages` row 69 |
| Package Tag (Requirements doc) | `26020-01-PT-39-001` | `26020-Package_Requirements.docx` Heading 1 #32 |
| Discipline | Mechanical | `_CONTEXT.md`; xlsx row 69 col E |
| Type | EPC Package Datasheet | `_CONTEXT.md` |
| Responsible Party | EPC Integrator | `_CONTEXT.md` |
| Location / Status | Shared 4-25 and 3-25 facility service; vetted package scope basis | `26020-Package_Requirements.docx` section `26020-01-PT-39-001`, scope-basis table |
| Source Basis | Bid Docs/Budgetary/`26020-01-PT-RFQ-39-001_Instr_Air_Bldg_R1.docx` | `26020-Package_Requirements.docx` section `26020-01-PT-39-001`, scope-basis table |

## Attributes — Major Included Equipment

Source: `26020-Package_Requirements.docx` section `26020-01-PT-39-001`, sub-heading **Major Included Equipment**.

| Item | Qty | Rating / Size | Notes |
|---|---|---|---|
| Instrument air compressor (oil-injected, rotary screw, air-cooled) | 2 | 1113 SCFM at 861 kPag (125 psig) discharge | Driven by electric motors |
| Electric motor (compressor driver) | 2 | 250 HP, soft starter or VFD-ready | Includes anti-condensation space heaters |
| Wet air receiver | 1 | Sized by vendor (`TBD`) | — |
| Dryer pre-filter | 2 | Sized by vendor (`TBD`) | — |
| Regenerative desiccant air dryer (100% capacity) | 1 unit (2 tanks/towers) | Size and capacity `TBD` by vendor | One operating / one regenerating; dryer sized for 2 compressors and leave |
| Common after-filter | 1 | `TBD` | Located downstream of combined dryer outlets |
| Dry air receiver | 1 (or 2 x 50% capacity) | `TBD` | Per **Basic Scope** wording |

## Operating and Design Conditions

Source: `26020-Package_Requirements.docx` section `26020-01-PT-39-001`, scope-notes table.

| Parameter | Value |
|---|---|
| Capacity / design throughput | 1113 SCFM at 861 kPag (125 psig) |
| Driver | Electric motors, soft starter or VFD-ready, 200-250 HP, 600 V / 3 PH / 60 Hz, TEFC, non-classified; speed TBD by vendor |
| Compressor max discharge / shutdown pressure | 1000 kPag |
| Maximum system design pressure | 1034 kPag (150 psig) |
| Minimum system pressure | 551 kPag (80 psig) |
| Facility shutdown pressure | 482 kPag (70 psig) |
| Design temperature range | -40 °C to 38 °C |
| Maximum delivered air water dew point | -73.3 °C at 1000 kPag |
| PSV set pressure (all PSVs in package) | 948 kPag (137.5 psig) |

## Construction / Mechanical Notes

- Compressor packages are vendor-shipped; site installation, piling, tie-in piping, and electrical terminations are **by others**. Mounting platform and stairs are also by others. (Source: scope-notes table, "By others" entry.)
- Driver electrical class assumed `Non-classified` per source.
- Building/HVAC, structural foundations, grounding, lighting, and fire & gas systems are interface scopes — see **Physical Interface Summary** below and the Specification.

## Physical Interface Summary

Authoritative interface row: `26020-Packages_Interfaces_4_export.xlsx` sheet `Packages` row 69 (`Instrument Air Building`); cross-checked against the interface table in `26020-Package_Requirements.docx` section `26020-01-PT-39-001`.

| Interface Type | Applies? | Notes |
|---|---|---|
| Process Piping | No | xlsx row 69 col F = blank |
| Utility Piping | Yes | xlsx col G = `X` |
| Relief / Flare / Vent | No | xlsx col H = blank |
| Drain / Containment | Yes | xlsx col I = `X` |
| Electrical Power | Yes | xlsx col J = `X` |
| EHT | No | xlsx col K = blank |
| Grounding / Bonding | Yes | xlsx col L = `X` |
| Area / Exterior Lighting | Yes | xlsx col M = `X`; Requirements doc cites `26020-Packages_Interfaces.3.xlsx` column M (row 69) |
| Cathodic Protection | No | xlsx col N = blank |
| I&C / Control Cabling | Yes | xlsx col O = `X` |
| Communications / Network | No | xlsx col P = blank |
| Building HVAC / Services | Yes | xlsx col Q = `X` |
| Fire & Gas / Safety Systems | Yes | xlsx col R = `X` |
| Maintenance Access | Yes | xlsx col S = `X` |
| Grading / Site Drainage / Spill Containment | No | xlsx col T = blank |
| Structural / Foundations / Supports | Yes | Requirements-doc interface table |
| Product Loading | No | Requirements-doc interface table |
| Pipeline / Pigging | No | Requirements-doc interface table |

`NOTE (CONFLICT)`: The Requirements doc references `26020-Packages_Interfaces.3.xlsx`; the locally accessible spreadsheet is `26020-Packages_Interfaces_4_export.xlsx` (revision 4 export). Treated as the same interface register at a later revision. See `Guidance.md` Conflict Table CT-01.

## Vendor Engineering Deliverables (Handoff Manifest)

Verbatim from `26020-Package_Requirements.docx` section `26020-01-PT-39-001`, sub-heading **Vendor Engineering Deliverables**. Grouped as in source.

**Core vendor documents:** PRQ-009 Vendor Document Index; DOC-008 Vendor Document Control Procedure; QLT-006 Supplier Quality Plan; QLT-003 Inspection and Test Plan (ITP); QLT-013 Material Test Reports / Certificates; QLT-020 Inspection Release Certificate; QLT-021 Manufacturing Record Book / Vendor Data Book; PRQ-013 Logistics / Shipping Plan; PRQ-015 Spare Parts Interchangeability Record (SPIR); PRQ-016 Vendor Data Book / Final Supplier Documentation.

**Core package engineering:** MEC-001 Mechanical Design Basis; MEC-002 Mechanical Equipment List; MEC-003 Mechanical Equipment Data Sheets; MEC-006 Package Equipment Specifications; MEC-014 Mechanical Calculation Package; MEC-016 Equipment General Arrangement Drawing; MEC-017 Equipment Installation / Setting Drawings; MEC-018 Lifting / Handling Study for Major Equipment; MEC-021 Equipment FAT / Performance Test Procedure; MEC-022 Equipment FAT / Performance Test Report; MEC-023 Vendor Data Book / Mechanical Final Documentation; MEC-024 Mechanical Spares / Special Tools Requirements; MEC-025 Mechanical Equipment IOM Manual.

**Rotating equipment / compressors:** MEC-004 Rotating Equipment Specifications; MEC-008 Compressor Data Sheets; MEC-019 Mechanical Seal / Lube Oil Specification; ELE-011 Motor Starting Study; REG-022 Pressure Equipment Registration Package.

**Static pressure equipment:** MEC-005 Static Equipment Specifications; MEC-009 Pressure Vessel Data Sheets.

**Utility piping interfaces:** PRO-011 Utility Summary / Utility Consumption Report; PIP-003 Piping Line List; PIP-008 Piping Isometric Drawings; PIP-017 Piping MTO; PIP-024 Hydrotest / Pressure Test Packages.

**Drainage / containment interfaces:** PRO-023 Process Sewer / Closed Drain Design Basis; CIV-014 Bund / Dike / Secondary Containment Drawings.

**Electrical, lighting, EHT, grounding:** ELE-002 Electrical Load List; ELE-003 Single-Line Diagrams; ELE-014 Cable Schedule; ELE-015 Cable Tray / Routing Drawings; ELE-016 Electrical Layout Drawings; ELE-020 Electrical Equipment Data Sheets; ELE-027 Electrical Installation Details; ELE-028 Electrical Interconnection / Connection Diagrams; ELE-029 Electrical FAT / SAT Procedure; ELE-030 Electrical Test Records / Energization Package; ELE-017 Lighting Layout Drawings; ELE-012 Grounding / Earthing Study; ELE-019 Earthing / Bonding Layout Drawings.

**Instrumentation and controls interfaces:** INS-002 Instrument Index; INS-003 Instrument Data Sheets; INS-005 Instrument Location Plans; INS-006 Instrument Hook-Up Drawings; INS-008 Instrument Loop Diagrams; INS-009 Instrument Wiring / Termination Diagrams; INS-010 Junction Box / Marshalling Drawings; INS-011 Instrument Cable Schedule; INS-016 Control Valve Data Sheets; INS-017 On-Off / Shutdown Valve Data Sheets; INS-018 Instrument I/O List; INS-025 Instrument MTO; INS-029 Instrument As-Built Drawings; CTL-003 Control Narrative / Functional Specification; CTL-005 Cause and Effect Matrix; CTL-006 DCS I/O List; CTL-026 Package Vendor Interface Specification.

**Building / HVAC / code interfaces:** PRO-024 Ventilation / Process Safety Equipment Inputs; TSF-023 Building Siting / Occupied Building Risk Assessment; REG-021 Fire Code / Building Code Compliance Package; STR-002 Structural General Arrangement Drawings; STR-012 Module Structural Drawings.

**Fire and gas / technical safety interfaces:** TSF-002 Fire and Gas Philosophy; TSF-003 Fire and Gas Mapping Study; TSF-004 Fire and Gas Detector Layout Drawings; TSF-009 SIL Determination Report; TSF-011 Safety Requirements Specification (SRS); TSF-013 Supplier SIL Documentation / Safety Manual; TSF-028 Emergency Response Plan Inputs.

**Structural, foundations, supports, access:** STR-001 Structural Design Basis; STR-004 Structural Calculation Package; STR-005 Foundation Design Calculations; STR-006 Foundation Drawings; STR-011 Platform / Access Structure Drawings; STR-013 Anchor Bolt / Embedment Drawings; STR-014 Lifting Lug / Transport Analysis; STR-020 Structural MTO.

## Coverage and Objectives

- **Covers Scope Items:** `SOW-0131`, `SOW-0132`, `SOW-0133`, `SOW-0134` (source: `_CONTEXT.md`)
- **Supports Objectives (PACKAGE_HEURISTIC, ASSUMPTION):** `OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (from `_CONTEXT.md`; package-grouping heuristic per `RuntimeOverrides.OBJECTIVE_ASSOCIATION_MODE = PACKAGE_HEURISTIC`)

## References

- `26020-Package_Requirements.docx` — section `26020-01-PT-39-001 - Instrument Air Building` (Heading 1 #32), located at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Package_Requirements.docx`. Source slices read: Basic Scope; Major Included Equipment; scope-basis table; scope-notes table; Physical Interface Summary table; Vendor Engineering Deliverables table; Interface Coordination Notes.
- `26020-Packages_Interfaces_4_export.xlsx` — sheet `Packages`, row 69 (`Instrument Air Building`), located at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/26020-Packages_Interfaces_4_export.xlsx`.
- `_CONTEXT.md` (deliverable-local).
- Decomposition: PROJECT_DECOMP Gate 7 snapshot at `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` (`DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv` — location TBD for specific deliverable row).
- Original RFQ basis: `Bid Docs/Budgetary/26020-01-PT-RFQ-39-001_Instr_Air_Bldg_R1.docx` — referenced in source; **not locally accessible**, treated as `location TBD`.
