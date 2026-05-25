# Datasheet — DEL-026-03 Construction Work Package

Deliverable type: EPC Construction Work Package (descriptive)
Parent package: PKG-026 — Transformer TXP-8300-2, STEP DOWN DISTRIBUTION TRANSFORMER, 20/26MVA, 13.8kV / 6.9kV / 0.4kV
Discipline: Electrical
Responsible party: EPC Integrator
Variant: PROJECT_DECOMP (Gate 7 snapshot 2026-05-24)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | DEL-026-03_construction-work-package | `_CONTEXT.md` |
| DeliverableName | Construction Work Package | `_CONTEXT.md` |
| ParentPackageID | PKG-026 | `_CONTEXT.md`; PACKAGE_REGISTER row PKG-026 |
| Package tag | TXP-8300-2 | Package name (Workbook Packages row 28) |
| Package code | 26020-02-30-017 | PACKAGE_REGISTER row PKG-026 |
| WBS | 02 (Electrical) | PACKAGE_REGISTER row PKG-026 |
| Workbook source | Workbook Packages row 28 | `_CONTEXT.md`; DELIVERABLE_REGISTER row DEL-026-03 |
| Decomposition snapshot | GATE-07_Final_Published_2026-05-24 | `_REFERENCES.md` |
| Covers scope items | SOW-0027 | DELIVERABLE_REGISTER row DEL-026-03 |
| Supports objectives | OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010 | DELIVERABLE_REGISTER row DEL-026-03 (PACKAGE_HEURISTIC mapping; ASSUMPTION at deliverable granularity) |

## Subject Equipment (as titled in the package)

| Attribute | Value | Source |
|---|---|---|
| Equipment tag | TXP-8300-2 | Package name (Workbook Packages row 28) |
| Service description | Step-down distribution transformer | Package name (Workbook Packages row 28) |
| Rating | 20 / 26 MVA (dual rating per package title; ONAN/ONAF basis ASSUMPTION) | Package name; rating basis TBD (not in accessible DBM slices) |
| Primary voltage | 13.8 kV | Package name; DBM-Deepcut §Power System (13.8 kV plant backbone distribution) |
| Secondary voltage(s) | 6.9 kV and 0.4 kV | Package name; DBM-Deepcut §Power System and §System Voltages |
| Number of windings | TBD (three voltages may imply two-winding or three-winding configuration) | Not stated in accessible source slices |
| Cooling class | TBD | Not stated in accessible source slices |
| Neutral grounding (6.9 kV side) | 100 A, 10 s neutral grounding resistor; tripping system | DBM-Deepcut §System Voltages / Grounding (line 2985 region) |
| Neutral grounding (0.4 kV / 600 V class) | DBM 600 V system uses 5 A continuous high-resistance grounding; applicability to a 0.4 kV winding is TBD | DBM-Deepcut §Power System grounding paragraph |
| Insulating medium | Oil-filled (ASSUMPTION based on DBM statement that large transformers are oil-filled) | DBM-Deepcut §Transformers |
| Installation base | Structural-steel transformer base (ASSUMPTION based on DBM general practice) | DBM-Deepcut §Transformers |

## Construction Work Package — Identification Attributes

| Attribute | Value | Source |
|---|---|---|
| CWP scope | How package PKG-026 will be physically installed, built, inspected, turned over, and tied into facility systems | DELIVERABLE_REGISTER DEL-026-03 |
| Workface plan basis | Installation and tie-in workface plan for TXP-8300-2 and ancillaries | `_CONTEXT.md` anticipated artifacts |
| Construction responsibility (facility level) | Tourmaline Oil Corporation field construction (mechanical hookup, setting on foundations, electrical terminations, home-run cable installation, structural supports) | DBM-Deepcut §Construction Responsibility (lines 101–125) |
| Tie-in interface types declared at PKG-026 | Electrical Power; Grounding/Bonding; Area/Exterior Lighting; I&C/Control Cabling; Communications/Network; Maintenance Access; Structural/Foundations/Supports | PACKAGE_REGISTER row PKG-026 |
| Vendor/EPC split | Package Vendor owns engineering, design, vendor documentation, and physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, and procurement/construction coordination | PACKAGE_REGISTER row PKG-026 |
| Gate context | Mandatory Gate 5 EPC anchor deliverable | DELIVERABLE_REGISTER row DEL-026-03 |

## Anticipated Artifacts Produced (per `_CONTEXT.md`)

- Construction work package
- Installation and tie-in workface plan
- Construction interface and turnover checklist

## Conditions / Site Context

| Condition | Value | Source |
|---|---|---|
| Facility | Tourmaline West Doe Deepcut Gas Plant Expansion (04-25) | DBM-Deepcut §Facility identity |
| Construction phasing | One phase, single train, nominal 300 MMSCFD | DBM-Deepcut summary table |
| Field construction manager | Tourmaline Oil Corporation | DBM-Deepcut §Construction Responsibility |
| Module-shipping policy | EPC scope includes shipping of modules to site; offloading; setting on foundations | DBM-Deepcut §Construction Responsibility |
| Tie-in handling | Installation of interconnecting piping to ISBL/OSBL tie-in points carries an external interface responsibility marker — to be confirmed per tie-in | DBM-Deepcut §Construction Responsibility (line 117 region) |
| Spacing | CEC spacing applies to large oil-filled transformers; spacing on structural steel bases is general practice | DBM-Deepcut §Transformers |

## References (sources used)

- `_CONTEXT.md` (this deliverable folder)
- `_REFERENCES.md` (this deliverable folder)
- `_DEPENDENCIES.md` (this deliverable folder)
- DELIVERABLE_REGISTER row DEL-026-03 (Gate 7 snapshot)
- PACKAGE_REGISTER row PKG-026 (Gate 7 snapshot)
- DBM-Deepcut/4-25_Deepcut_DBM.md — §Power System; §System Voltages; §Transformers; §Construction Responsibility
- Workbook Packages row 28 (cited by registers; row text not separately re-extracted here)

## TBD / Open items

- Cooling class, impedance, tap range, winding configuration, BIL, sound level for TXP-8300-2: not in accessible DBM slices — TBD until vendor datasheet or detailed electrical source is accepted.
- Exact basis of "20/26 MVA" dual rating (ONAN/ONAF vs. ONAN/ONAF/ONAF, or other): ASSUMPTION ONAN/ONAF; confirm with vendor data.
- 0.4 kV secondary/tertiary derivation (true tertiary vs. separate companion transformer): TBD; package title lists three voltages while DBM describes radial step-down chain.
- Specific tie-in points (foundation IDs, cable tray routes, grounding mat connections): TBD until detailed engineering drawings are accepted into `_Sources`.
