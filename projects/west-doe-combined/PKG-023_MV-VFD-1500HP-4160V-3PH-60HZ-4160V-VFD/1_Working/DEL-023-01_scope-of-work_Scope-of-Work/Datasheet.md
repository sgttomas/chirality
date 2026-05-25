# Datasheet — DEL-023-01 Scope of Work (PKG-023 MV VFD 1500HP 4160V)

Descriptive datasheet for the EPC Integrator Scope of Work deliverable for PKG-023.
This document records identity, package attributes, environmental/integration conditions,
and construction-relevant facts that frame the Scope of Work narrative. Technical
ratings beyond the workbook title are recorded as `TBD` and surfaced for human ruling
because the locally accessible Deepcut DBM source slice does not assign a 1500HP / 4160V
MV VFD to this package.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-023-01_scope-of-work` | Gate 7 `DELIVERABLE_REGISTER.csv` |
| Deliverable Name | Scope of Work | Gate 7 `DELIVERABLE_REGISTER.csv` |
| Parent Package ID | `PKG-023` | Gate 7 `PACKAGE_REGISTER.csv` |
| Workbook ID | 23 | `PACKAGE_REGISTER.csv` (Workbook row 25) |
| Package Title | MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD | `PACKAGE_REGISTER.csv` |
| Discipline | Electrical | `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| Project CoA | 26020-01-30-014 | `PACKAGE_REGISTER.csv` |
| Responsible Party | EPC Integrator | `_CONTEXT.md`, `DELIVERABLE_REGISTER.csv` |
| Artifact Type | EPC Scope of Work | `DELIVERABLE_REGISTER.csv` |
| Scope Item | `SOW-0024` | `DELIVERABLE_REGISTER.csv` |
| Supports Objectives | OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-008; OBJ-009; OBJ-010 | `DELIVERABLE_REGISTER.csv` (ASSUMPTION: package-grouping heuristic) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package function (title basis) | Medium-voltage variable-frequency drive for a 1,500 HP / 4,160 V / 3-phase / 60 Hz motor application, supplied from a 4,160 V VFD section | Workbook Packages row 25 (title) |
| Package family | Vendor-owned MV VFD package (Electrical) | `PACKAGE_REGISTER.csv` |
| Service / driven equipment | TBD — no Deepcut DBM source slice maps a 1,500 HP MV VFD to PKG-023 (HRR-023-01-001) | Source absence in `DBM-Deepcut/4-25_Deepcut_DBM.md` |
| Quantity in facility | TBD | Not stated in available source slice |
| Installed spare basis | TBD | Not stated in available source slice |
| Motor rating served | 1,500 HP nameplate (title-only); detailed motor data TBD | Workbook Packages row 25 (title) |
| Supply voltage to VFD | 4,160 V, 3-phase, 60 Hz (title-only) | Workbook Packages row 25 (title) |
| Output voltage to motor | 4,160 V class (title-only) | Workbook Packages row 25 (title) |
| Topology (e.g., multilevel / NPC / cascaded) | TBD | Not stated |
| Cooling method | TBD | Not stated |
| Enclosure / area classification | TBD | Not stated; Zone-2 marking obligations may apply per DBM §electrical (general) |
| Bypass / synchronous transfer | TBD; DBM describes "Starting VFD with synchronous transfer to a normal-service bus" for inlet/sales compressor service only, not assigned to PKG-023 | `4-25_Deepcut_DBM.md` line 893 |

## Conditions (Integration Environment)

| Condition | Value | Source |
|---|---|---|
| Site / facility | West Doe Deepcut expansion | `4-25_Deepcut_DBM.md` (project framing) |
| Plant electrical class for 4.16 kV MCC | 4.16 kV MCCs use mechanically latched fused contactors with motor protection relays and Ethernet to plant PLC; "VFD and soft-starter requirements for 4.16 kV motors are TBD" | `4-25_Deepcut_DBM.md` lines 2957, 3088 |
| Standalone 600 V VFD policy | Standalone 600 V VFDs not allowed unless dedicated to large motors; informs the precedent that MV/standalone VFDs are dedicated to large motors | `4-25_Deepcut_DBM.md` line 2959 |
| Hazardous area marking | VFD-fed motors located in Zone 2 areas shall be marked and supplied with a temperature code lower than the temperature code on the area-classification drawing or fugitive-emissions study | `4-25_Deepcut_DBM.md` line 2961 |
| Site environmental conditions (temperature, altitude, seismic, wind, snow) | TBD | Not in available source slice |
| Available utilities (control power, instrument air, cooling water/glycol) | TBD | Not in available source slice |

## Construction (Integration Facts)

| Item | Value | Source |
|---|---|---|
| Vendor scope | Package engineering, package design, vendor documentation, physical equipment package | `PACKAGE_REGISTER.csv` |
| EPC Integrator scope | Facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination | `PACKAGE_REGISTER.csv` |
| Applicable interface types | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports | `PACKAGE_REGISTER.csv`; `INTERFACE_REGISTER.csv` (IFC-2F6B2D3B80, IFC-CEF43B776E, IFC-488756F914, IFC-FF4188D90D, IFC-38BEE3F6CC, IFC-0AED039BBE) |
| Exclusions | "TBD; no package-specific exclusions stated in source materials." | `PACKAGE_REGISTER.csv` |
| Mandatory anchor flag | Mandatory Gate 5 EPC anchor deliverable | `DELIVERABLE_REGISTER.csv` (Notes) |

### Anticipated Artifacts (carried in this Scope of Work)

| Artifact ID | Artifact | Type |
|---|---|---|
| ART-D70FE712E8 | Package scope of work | EPC Scope of Work |
| ART-2C8B496DD1 | Tagged equipment and package identity list | Tagged Equipment Evidence |
| ART-26BB26779C | Package function and whole-facility integration narrative | EPC Integration Narrative |
| ART-A3F647F3C3 | Package responsibility assignment record | Responsibility Evidence |

Source: `ARTIFACT_REGISTER.csv` (Gate 7).

## References

- Gate 7 snapshot root: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
- `DELIVERABLE_REGISTER.csv` — row for `DEL-023-01_scope-of-work`
- `PACKAGE_REGISTER.csv` — row for `PKG-023`
- `ARTIFACT_REGISTER.csv` — artifacts for `DEL-023-01`
- `INTERFACE_REGISTER.csv` — interfaces for `PKG-023`
- Workbook Packages row 25 (cited; not opened as a separate readable source file in PREPARATION)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Deepcut Design Basis Memorandum (PKG-023 not explicitly named)
