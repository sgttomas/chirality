# Datasheet — Construction Work Package (DEL-058-03)

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-058-03_construction-work-package` |
| Name | Construction Work Package |
| ParentPackageID | `PKG-058` |
| PackageName | Medium Pressure Flash Feed Separator |
| Discipline | Mechanical (EPC construction integration) |
| Type | EPC Construction Work Package |
| ResponsibleParty | EPC Integrator |
| DecompositionRef | `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 392 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package modules | Module `710-1 Medium Pressure Flash Feed Module` (Shop) and Module `730-1 Medium Pressure Flash Feed Module` (Shop) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2804, 2806 (Module table) |
| Tagged vessels | `MEDIUM PRESSURE FLASH FEED SEPARATOR (x2)` — first vessel tag `V-7110-1`; second vessel tag in row 53 register `E-7120-1` is the HCL heater bundle, vessel for module 730-1 is `V-7310-1` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2544, 2603-2604, 672 |
| Heater bundle (optional) | `MEDIUM PRESSURE F.F. HCL HEATER BUNDLE (x2)` tag `E-7120-1`; retention pending thermal reassessment | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2544, 2604, 674 |
| Module-count basis | 2 packages, 100% per package, 200% installed (parallel maintenance-isolation basis) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2366 |
| Fabrication basis | Shop-fabricated module shipped to site (Tourmaline field construction off-loads, sets, and hooks up) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2804, 2806, 111-114 |
| Package enclosure | Self-framing building enclosing instrumentation and one end of the vessel (configured similarly to inlet separator) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 672 |
| Internals | Mistex; no internal coating specified | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 672 |
| Methanol injection provision | Upstream of MPFF inlet level/pressure control valve, retained as safeguard | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 674 |
| Maintenance-isolation basis | Unit-basis isolation so entire unit can be taken out of service while other unit continues operation | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2408 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Design operating temperature (MPFF) | 40 deg C (assumed from system-level data, pending detailed engineering) — ASSUMPTION | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 670 |
| MPFF inlet temperature | TBD/TBC pending upstream HEX installation and thermal reassessment | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 670 |
| Residence-time basis | ≥10 minutes liquid residence between weir height and NLL-interface | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 670 |
| Design ambient (site, used for construction sequencing) | -40 deg C minimum to +35 deg C maximum | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 198 |
| Snow load Ss / Sr | 2.5 kPa / 0.2 kPa | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 206-207 |
| Soil type (foundation interface) | Clay overlying clay till, to be confirmed | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 210 |
| Geotechnical assessment for bearing/pile design | TBD pending report completion | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2834 |

## Construction Scope Allocation

Construction scope is divided between Tourmaline field construction (the Owner construction organization) and the EPC Integrator. The split below is taken directly from the construction responsibility table.

| Activity | Responsibility | Source |
|---|---|---|
| Construction management | Tourmaline field construction | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 107 |
| Grading, piling, foundation work | Tourmaline field construction | line 108 |
| Shipping of modules to site | Tourmaline field construction | line 111 |
| Off-loading of modules and equipment | Tourmaline field construction | line 112 |
| Setting modules, pipe racks, equipment on foundations | Tourmaline field construction | line 113 |
| Mechanical hookup of modules and interconnecting piping | Tourmaline field construction | line 114 |
| Installation of shipped-loose instruments, valves, components | Tourmaline field construction | line 115 |
| Installation of structural supports | Tourmaline field construction | line 116 |
| Installation of interconnecting piping to ISBL/OSBL tie-in points | External interface; responsibility confirmed per tie-in | line 117 |
| Field installation of home-run cables | Tourmaline field construction | line 118 |
| Electrical terminations | Tourmaline field construction | line 119 |
| EPC Integrator package construction work package authorship and interface to Tourmaline | EPC Integrator (this deliverable's authoring scope) | ASSUMPTION inferred from PROJECT_DECOMP responsible-party assignment |

## References

- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Construction Responsibility, MPFF system, Module list, Site Data)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` row 392
- `26020-Package_Requirements.docx` package heading 13 — TBD (source not parsed locally; location TBD)

## Open Items

- Detailed equipment tag list and shipped-loose register — TBD pending vendor package datasheet (DEL-058-02) issuance.
- Foundation interface data — TBD pending geotechnical report.
- HCL heater bundle retention — TBD pending thermal reassessment (affects nozzle preservation, tie-ins).
- Tie-in responsibility per ISBL/OSBL boundary — TBD per tie-in.
