# Datasheet: DEL-030-01 Scope of Work

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-030-01_scope-of-work` |
| DeliverableName | Scope of Work |
| ParentPackageID | `PKG-030` |
| ParentWorkbookID | 30 |
| PackageName | Transformer TXP-8200-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 2.5MVA 13.8kV/600/347V |
| WorkbookRow | 32 |
| WBS | 01 |
| TrackingNumber | `26020-01-30-021` |
| Discipline | Electrical |
| Type | EPC Scope of Work |
| ResponsibleParty | EPC Integrator |
| CoversScopeItems | `SOW-0031` |
| SupportsObjectives | `OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-008; OBJ-009; OBJ-010` (ASSUMPTION: PACKAGE_HEURISTIC association) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Equipment tag | `TXP-8200-1` | Package name (workbook row 32) |
| Equipment description | Step-Down Distribution Transformer | Package name (workbook row 32) |
| Nominal rating | 2.5 MVA | Package name (workbook row 32); independent rating clauses TBD |
| Primary voltage | 13.8 kV | Package name; DBM Deepcut System Voltages table (medium-voltage 13.8 kV backbone) |
| Secondary voltage | 600 V / 347 V | Package name; DBM Deepcut System Voltages table (600 V, 3 phase, 3 wire, 60 Hz, high-resistance grounded) |
| Phases / wires / frequency | 3 phase, 60 Hz | DBM Deepcut System Voltages table |
| Secondary grounding | High-resistance grounded with 5 A continuous resistor (facility 600 V basis); 600 V transformer neutral grounded by 5 A continuous high-resistance grounding resistor | DBM Deepcut System Voltages and Grounding and Bonding sections |
| Vector group / winding configuration | TBD | Not stated in accessible sources |
| Insulation type (oil / dry) | TBD; if oil-filled, CEC spacing applies and secondary containment requirements shall be reviewed | DBM Deepcut Transformers section |
| Impedance, taps, BIL, temperature rise | TBD | Not stated in accessible sources |
| Cooling class | TBD | Not stated in accessible sources |
| Enclosure / area classification | TBD | Not stated in accessible sources |
| Dimensions / weight / footprint | TBD | Not stated in accessible sources |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Site / facility | West Doe Deepcut facility (04-25 / 03-25 power distribution shared) | DBM Deepcut Electrical System section |
| Utility supply context | BC Hydro 25 kV utility feed via 25 kV / 13.8 kV / 50 MVA utility transformer; 13.8 kV switchgear is the plant main power distribution center | DBM Deepcut Electrical System section |
| Application | Radial step-down from 13.8 kV bus to a 600 V electrical building / MCC bus (one of: 600 V Acid Gas Compressor EB, 600 V Sales/Overheads Compressor EB, 4.16 kV/600 V General Area/Tank Farm/Process EB); specific destination TBD | DBM Deepcut Electrical System (13.8 kV switchgear distribution list); 600 V MCC sections |
| Ambient / environmental design | TBD | Not stated in accessible sources |
| Seismic / wind / snow loads | TBD | Not stated in accessible sources |

## Construction

| Construction Item | Value | Source |
|---|---|---|
| Package responsibility split | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package supply. EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-030 |
| Installation basis | Large oil-filled transformers shall be spaced per CEC requirements and installed on structural steel transformer bases; secondary containment requirements shall be reviewed; selection shall avoid or limit containment where practical | DBM Deepcut Transformers section |
| Applicable package interfaces | Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports | Gate 7 `PACKAGE_REGISTER.csv` row PKG-030 (Applicable interface types) |
| Grounding | Each 600 V transformer shall be grounded by a 5 A continuous high-resistance grounding resistor; major electrical equipment connected to ground grid at two points; ground wells provided at power transformers for maintenance / operational testing | DBM Deepcut Grounding and Bonding section |

## References

- Workbook Packages row 32 (`26020-Packages_Interfaces_4_export.xlsx`)
- Gate 7 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `PACKAGE_REGISTER.csv` row PKG-030
  - `DELIVERABLE_REGISTER.csv` row DEL-030-01_scope-of-work
- DBM Deepcut: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Electrical System; System Voltages; Transformers; Motor Control and Motor Specifications; Electrical Buildings; Grounding and Bonding sections)
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` for this deliverable
