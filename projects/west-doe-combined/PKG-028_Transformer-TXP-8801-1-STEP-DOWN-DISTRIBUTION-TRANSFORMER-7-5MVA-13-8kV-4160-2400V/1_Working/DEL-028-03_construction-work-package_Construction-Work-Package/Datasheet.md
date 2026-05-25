# Datasheet: DEL-028-03_construction-work-package — Construction Work Package

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-028-03_construction-work-package` | `_CONTEXT.md` |
| Deliverable Name | Construction Work Package | `_CONTEXT.md` |
| ParentPackageID | `PKG-028` | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Package Name | Transformer TXP-8801-1 — STEP DOWN DISTRIBUTION TRANSFORMER — 7.5MVA 13.8kV/4160/2400V | PACKAGE_REGISTER.csv (Workbook Packages row 30) |
| Equipment Tag | TXP-8801-1 | Package name (Workbook Packages row 30) |
| Discipline | Electrical | `_CONTEXT.md`; PACKAGE_REGISTER.csv |
| Deliverable Type | EPC Construction Work Package | DELIVERABLE_REGISTER.csv |
| Responsible Party | EPC Integrator | DELIVERABLE_REGISTER.csv |
| WBS | 01 | PACKAGE_REGISTER.csv |
| CoA / Tracking | 26020-01-30-019 | PACKAGE_REGISTER.csv |
| Supports Objectives | OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-008; OBJ-009; OBJ-010 (PACKAGE_HEURISTIC, ASSUMPTION at deliverable-ID level) | OBJECTIVE_DELIVERABLE_MAP.csv |
| Covers Scope Items | SOW-0029 | DELIVERABLE_REGISTER.csv |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function | Step-down distribution transformer feeding medium- / low-voltage downstream loads from the 13.8 kV plant main power distribution system | DBM-Deepcut §2919 (general 13.8 kV switchgear distribution via step-down transformers); package name |
| Primary voltage (nameplate, from package title) | 13.8 kV | Package name (Workbook Packages row 30) |
| Secondary voltages (nameplate, from package title) | 4160 V and 2400 V | Package name (Workbook Packages row 30) |
| Rated capacity (nameplate, from package title) | 7.5 MVA | Package name (Workbook Packages row 30) |
| Winding configuration | TBD | not in accessible source slices |
| Cooling class (e.g., ONAN/ONAF) | TBD | not in accessible source slices |
| Insulating fluid / dry-type | TBD | not in accessible source slices |
| Tap changer (de-energized / OLTC) | TBD | not in accessible source slices |
| Impedance | TBD | not in accessible source slices |
| BIL (HV / LV) | TBD | not in accessible source slices |
| Neutral grounding (secondary) | Conventional grounding configuration for medium-voltage step-down transformer — TBD specific resistor rating until vendor data accepted | DBM-Deepcut §2985 (6.9 kV transformers grounded via 100 A, 10 s NGR; 600 V transformers via 5 A continuous HRG) — ASSUMPTION: not directly applicable to 4160/2400 V secondaries |
| Outdoor / indoor location | TBD | not in accessible source slices |
| Area classification | TBD | not in accessible source slices |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Foundation type | Precast concrete bearing foundation (typical for transformers) | DBM-Deepcut §2745 (`Transformers — Generally supported on precast concrete bearing foundations`) |
| Site interfaces (declared) | Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports | PACKAGE_REGISTER.csv; INTERFACE_REGISTER.csv rows for PKG-028 |
| Climatic / seismic basis | TBD | not in accessible source slices |
| Acoustic limits | TBD | not in accessible source slices |
| Construction sequencing prerequisites | Foundation accepted; ground grid extended to transformer pad; 13.8 kV feeder cable raceway installed and ready for pull; downstream 4160 V and 2400 V feeders/raceways available for tie-in | ASSUMPTION based on declared interfaces and general DBM electrical practice |

## Construction

| Element | Description | Source |
|---|---|---|
| Construction work package scope | Physical installation, building, inspection, turnover, and tie-in of the TXP-8801-1 transformer package into the larger facility systems | `_CONTEXT.md` (Scope); DELIVERABLE_REGISTER.csv |
| Installation and tie-in workface plan | Workface planning evidence for setting the transformer on its foundation and connecting it to adjacent electrical, grounding, lighting, controls, communications, and structural systems | ARTIFACT_REGISTER.csv (ART-D64770700D) |
| Construction interface and turnover checklist | Construction-facing interface, tie-in, inspection, and turnover evidence for the approved package | ARTIFACT_REGISTER.csv (ART-790F01D335) |
| Major construction activities | Receipt and inspection; rigging and setting on foundation; bonding to ground grid; primary 13.8 kV terminations; secondary 4160 V and 2400 V terminations; control / monitoring wiring; pre-energization testing; energization and turnover | ASSUMPTION based on declared interfaces and DBM-Deepcut general electrical practice; vendor IOM TBD |
| Inspection / hold points | TBD until vendor IOM and EPC ITP are issued | not in accessible source slices |

## References

- `_CONTEXT.md` — deliverable identity, scope, anticipated artifacts
- `_REFERENCES.md` — authoritative decomposition basis
- Gate 7 PROJECT_DECOMP snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - DELIVERABLE_REGISTER.csv (DEL-028-03 row)
  - PACKAGE_REGISTER.csv (PKG-028 row, Workbook Packages row 30)
  - ARTIFACT_REGISTER.csv (ART-C0CF6D35AA, ART-D64770700D, ART-790F01D335)
  - INTERFACE_REGISTER.csv (PKG-028 interface rows)
  - OBJECTIVE_DELIVERABLE_MAP.csv (DEL-028-03 rows)
- DBM-Deepcut/4-25_Deepcut_DBM.md — §2745 (transformer foundations); §2919 (13.8 kV step-down distribution); §2985 (transformer grounding)
- Vendor IOM, factory test report, and EPC construction ITP — TBD (not in PREPARATION source set)
