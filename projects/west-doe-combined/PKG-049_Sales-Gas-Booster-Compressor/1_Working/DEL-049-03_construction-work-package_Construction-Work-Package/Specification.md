# Specification — DEL-049-03 Construction Work Package (Sales Gas Booster Compressor)

> Normative requirements for the Construction Work Package (CWP) deliverable for `PKG-049 Sales Gas Booster Compressor`. Source: `_Sources/26020-Package_Requirements.docx` heading 4 (`26020-01-PT-12-004`). Inferred requirements are labelled `ASSUMPTION`. Unresolved values are `TBD`.

## Scope

### In Scope

- Define how the Sales Gas Booster Compressor package will be physically installed, built, inspected, turned over, and tied into the larger facility (`_CONTEXT.md` Scope).
- Workface-level installation plan for: setting the package on piles; structural attachment; process and utility piping tie-ins; relief/flare/vent tie-ins; drain/containment connections; electrical power and lighting; EHT; grounding/bonding; I&C cabling; fire & gas devices; structural supports/platforms/stairs; maintenance access provisions.
- Construction interface management and turnover documentation across EPC Integrator and the Package Vendor.

### Out of Scope (By Vendor or Others, per Source)

- Supply and engineering of the compressor package itself (covered by `DEL-049-04`).
- The following items are explicitly listed as "By others" relative to the Package Vendor (Source: SGBC Scope Notes / Open Items): shipping the package to site; installation on piles; tie-in piping; electrical connections; mounting platform and stairs. The CWP MUST allocate, plan, and schedule these scope items on the EPC Integrator's side.
- Cathodic Protection, Communications/Network, Building HVAC, Grading/Site Drainage/Spill Containment, Product Loading, Pipeline/Pigging interfaces (Source: SGBC Physical Interface Summary — "No").

## Requirements

### R-CWP-1 — Package Identification

The CWP MUST identify the package by equipment tag `26020-01-PT-12-004 - Sales Gas Booster Compressor` and reference `PKG-049` and the GATE-07 decomposition snapshot. (Source: `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv`.)

### R-CWP-2 — Construction Scope Coverage

The CWP MUST cover scope items `SOW-0169`, `SOW-0170`, `SOW-0171`, `SOW-0172` and trace its work breakdown back to these IDs. (Source: `DELIVERABLE_REGISTER.csv` row `DEL-049-03`.)

### R-CWP-3 — Foundation and Setting

The CWP MUST include a foundation/setting plan for installing the package on piles, citing the vendor's `STR-005 Foundation Design Calculations`, `STR-006 Foundation Drawings`, `STR-013 Anchor Bolt / Embedment Drawings`, and `MEC-017 Equipment Installation / Setting Drawings`. (Source: SGBC Vendor Engineering Deliverables list.)

### R-CWP-4 — Lifting, Handling, and Transport

The CWP MUST incorporate `MEC-018 Lifting / Handling Study for Major Equipment` and `STR-014 Lifting Lug / Transport Analysis` and define rigging plans, crane picks, load paths, and laydown sequencing for the SGBC package. (Source: SGBC Vendor Engineering Deliverables list.)

### R-CWP-5 — Piping Tie-Ins

The CWP MUST plan and schedule process, utility, relief/flare/vent, and drain tie-ins for the SGBC, anchored on `PIP-004 Tie-In List / Tie-In Scope Sheets`, `PIP-006 Equipment/Piping General Arrangement`, `PIP-008 Piping Isometric Drawings`, `PIP-009 Fabrication Isometrics with BOM`, and `PIP-017 Piping MTO`. (Source: SGBC Vendor Engineering Deliverables list and Physical Interface Summary — Process / Utility / Relief / Drain = Yes.)

### R-CWP-6 — Pressure Testing and Cleaning

The CWP MUST include `PIP-024 Hydrotest / Pressure Test Packages` and `PIP-025 Flushing / Cleaning / Drying Procedure` for in-scope tie-in piping. Test pressures MUST envelope SGBC suction design 6,137 kPag (890 psig) and discharge design 12,866 kPag (1,866 psig); exact test pressures, mediums, and hold times = TBD (project pressure-test specification slice not accessible). (Source: SGBC Scope Notes for design pressures; vendor artifact IDs.)

### R-CWP-7 — Electrical Installation

The CWP MUST include electrical installation deliverables `ELE-027 Electrical Installation Details`, `ELE-016 Electrical Layout Drawings`, `ELE-014 Cable Schedule`, `ELE-015 Cable Tray / Routing`, `ELE-028 Electrical Interconnection / Connection Diagrams`, `ELE-029 Electrical FAT / SAT Procedure`, and `ELE-030 Electrical Test Records / Energization Package`. The motor served is 1,000 kW, 4000 V / 3PH / 60 Hz, 891 RPM, DOL with soft-start. (Source: SGBC Driver spec; Vendor Engineering Deliverables.)

### R-CWP-8 — Lighting, EHT, Grounding

The CWP MUST include `ELE-017 Lighting Layout`, `ELE-018 EHT Design Package`, `PIP-020 / PIP-021` heat tracing schedules and interface, and `ELE-012 / ELE-019` grounding study and earthing/bonding drawings. (Source: SGBC Physical Interface Summary — Area Lighting, EHT, Grounding = Yes.)

### R-CWP-9 — Instrumentation Installation and Loop Verification

The CWP MUST include `INS-005 Instrument Location Plans`, `INS-006 Instrument Hook-Up Drawings`, `INS-008 Instrument Loop Diagrams`, `INS-009 Wiring/Termination Diagrams`, `INS-010 Junction Box / Marshalling`, `INS-011 Instrument Cable Schedule`, `INS-018 Instrument I/O List`, and `INS-029 As-Built Drawings`, and shall verify loops against `CTL-003 Control Narrative`, `CTL-005 Cause and Effect Matrix`, and `CTL-026 Package Vendor Interface Specification`. (Source: SGBC Vendor Engineering Deliverables.)

### R-CWP-10 — Fire & Gas / Safety

The CWP MUST install and commission F&G devices per `TSF-003 F&G Mapping Study`, `TSF-004 F&G Detector Layout`, and the SRS (`TSF-011`). (Source: SGBC Physical Interface Summary — F&G = Yes.)

### R-CWP-11 — Structural and Access

The CWP MUST install structural supports, platforms, stairs, and maintenance access per `STR-002 Structural GA`, `STR-011 Platform / Access Structure Drawings`, and `STR-012 Module Structural Drawings`. (Source: SGBC Vendor Engineering Deliverables; "Mounting platform and stairs" listed as "By others" relative to the vendor.)

### R-CWP-12 — Inspection and Test

The CWP MUST incorporate `QLT-003 ITP`, `QLT-013 MTRs`, `QLT-020 Inspection Release Certificate`, and `QLT-021 Manufacturing Record Book` and overlay site inspections (receiving, setting, alignment, pre-energization, instrument loop checks, pressure tests, F&G functional tests). (Source: SGBC Vendor Engineering Deliverables.)

### R-CWP-13 — FAT to SAT Continuity

The CWP MUST consume `MEC-021 FAT / Performance Test Procedure`, `MEC-022 FAT / Performance Test Report`, `ELE-029 Electrical FAT/SAT Procedure`, and define SAT activities mirroring FAT scope where re-verification at site is required. (Source: SGBC Vendor Engineering Deliverables.)

### R-CWP-14 — Mechanical Completion and Turnover

The CWP MUST produce a construction interface and turnover checklist that drives mechanical completion certification of the SGBC package and hands the package over to commissioning. Specific MC criteria, punch-list workflow, and turnover boundaries = TBD (project MC procedure not accessible). (Source: `_CONTEXT.md` Anticipated Artifacts; ASSUMPTION on the use of an EPC MC procedure.)

### R-CWP-15 — Pressure Equipment Registration

The CWP MUST integrate `REG-022 Pressure Equipment Registration Package` activities into the site sequence prior to commissioning. (Source: SGBC Vendor Engineering Deliverables — Pressure Equipment Registration Package.)

### R-CWP-16 — Spares and IOM Handover

The CWP MUST ensure `MEC-024 Spares / Special Tools Requirements`, `PRQ-015 SPIR`, and `MEC-025 IOM Manual` are received and registered at turnover. (Source: SGBC Vendor Engineering Deliverables.)

### R-CWP-17 — As-Builts

The CWP MUST require `PIP-028 Piping As-Built Drawings` and `INS-029 Instrument As-Built Drawings` (and electrical/structural as-builts as applicable) at close-out. (Source: SGBC Vendor Engineering Deliverables; ASSUMPTION on electrical/structural as-built equivalents.)

## Standards

| Standard | Applies To | Location |
|---|---|---|
| API 661 | Air-cooled heat exchanger construction quality (intercoolers) | Cited in SGBC Major Included Equipment |
| NEMA MG 1 | Motor construction/test for the 1,000 kW driver | Cited in SGBC Scope Notes |
| Pressure equipment registration regime governing the project jurisdiction | Pressure vessels and piping in the SGBC | TBD (jurisdiction not stated in accessible source — `REG-022` implies a registration regime) |
| Site-specific construction, hot-work, and confined-space procedures | All site construction activities | TBD (project HSE procedures not in `_REFERENCES.md`) |
| Project welding and NDE specifications | Tie-in piping construction | TBD (project welding specs not in `_REFERENCES.md`) |

## Verification

| Requirement | Verification |
|---|---|
| R-CWP-1, R-CWP-2 | Trace matrix from CWP work breakdown to `SOW-0169`–`SOW-0172` and to equipment tag `26020-01-PT-12-004` |
| R-CWP-3 | Pile-driving record, anchor bolt survey, baseplate elevation/level survey, grout cure record |
| R-CWP-4 | Approved lift plan; rigging inspection; load test certs; pre- and post-lift surveys |
| R-CWP-5 | Tie-in punch-list closure against `PIP-004`; weld map closure |
| R-CWP-6 | Hydrotest packs signed off; flush/dry records; chart recorder traces (limits TBD) |
| R-CWP-7 | Megger / continuity tests, motor solo run, energization checklist (`ELE-030`) |
| R-CWP-8 | Lighting illumination survey; heat-tracing continuity and circuit test; grounding resistance test |
| R-CWP-9 | Loop check sheets reconciled to `INS-008` and `CTL-005` |
| R-CWP-10 | F&G device functional tests against `TSF-005`/Cause & Effect |
| R-CWP-11 | Structural inspection reports; bolt torque records; platform / stair compliance walk-down |
| R-CWP-12 | ITP sign-offs; inspection release certificate issued |
| R-CWP-13 | SAT records cross-referenced to FAT punch-list closure |
| R-CWP-14 | Mechanical completion certificate; turnover checklist signed by EPC Integrator and commissioning lead |
| R-CWP-15 | Jurisdictional pressure equipment registration acceptance |
| R-CWP-16 | Spares received-and-inventoried record; IOM filed in turnover dossier |
| R-CWP-17 | As-built drawings issued and accepted at close-out |

## Documentation

The CWP deliverable bundle consists of:

- This Specification (`Specification.md`).
- `Datasheet.md` — package identification, attributes, conditions, interface applicability.
- `Guidance.md` — principles, considerations, trade-offs.
- `Procedure.md` — workface execution sequence and turnover.
- The three anticipated artifacts in `_CONTEXT.md`: Construction work package, Installation and tie-in workface plan, Construction interface and turnover checklist.
