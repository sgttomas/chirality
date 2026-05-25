# Datasheet — DEL-034-04 Vendor Engineered Equipment Package (600V Electrical Building 820-2)

> Descriptive datasheet for the Package Vendor production unit (engineering, design, fabrication/supply, and the physical equipment package) for `PKG-034 600V ELECTRICAL BUILDING (820-2)`. Values not directly supported by accessible source slices are marked `TBD` or labelled `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-034-04_vendor-engineered-equipment-package` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 189 |
| Deliverable Name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent Package | `PKG-034 600V ELECTRICAL BUILDING (820-2)` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 36 |
| Workbook Row | 36 | `PACKAGE_REGISTER.csv` row 36 |
| Workbook Package Code | `26020-02-30-025` | `PACKAGE_REGISTER.csv` row 36 |
| WBS | 02 | `PACKAGE_REGISTER.csv` row 36 |
| Discipline | Electrical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Deliverable Type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible Party | Package Vendor (engineering / design / equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers Scope Items | `SOW-0035` | `DELIVERABLE_REGISTER.csv` |
| Supports Objectives | `OBJ-002; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010` (PACKAGE_HEURISTIC — ASSUMPTION) | `OBJECTIVE_DELIVERABLE_MAP.csv` rows 455, 989, 1523, 2065, 2497, 3055, 3627, 4172 |

## Attributes (Equipment Subject of the Vendor Package)

| Attribute | Value | Source |
|---|---|---|
| Building function | Prefabricated modular electrical building housing 600 V low-voltage distribution and ancillary electrical equipment for its served area. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings section (lines 2971-2979) |
| Low-voltage service basis | 600 V, 3 phase, 3 wire, 60 Hz, high-resistance grounded with 5 A continuous resistor | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` System Voltages (line 2937) |
| Anticipated equipment housed (per DBM building basis) | 600 V MCC(s); 600 V VFDs as part of the MCC lineup; 120 V AC UPS systems with battery banks and distribution panels; 125 V DC UPS systems with battery banks and distribution panels; 600 V to 208/120 V distribution transformer(s) and panelboard(s); 208/120 V contactor panel(s); plant PLC control panel(s); network rack(s). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings (line 2973) |
| Upstream feed (ASSUMPTION) | Radial step-down from the facility 13.8 kV switchgear via a 13.8 kV-to-600 V transformer; specific transformer designation for 820-2 is TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System (lines 2919-2925); building 820-2 not enumerated in the DBM buildings list |
| Building identifier "820-2" | Building 820-2 is not enumerated in the DBM Deepcut buildings list, which names 820-1 (6.9 kV Inlet/Sales Compressor Electrical Building) but not 820-2. Allocation, service area, and elevation of 820-2 are TBD. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Buildings table (lines 2811-2816); HRR-034-04-001 |
| Standby power interface | Standby power served at the 600 V MCC level via TOU-typical low-voltage standby generator(s) and transfer switch(es); applicability to 820-2 specifically is ASSUMPTION pending detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Standby Power and Motor Control sections (lines 2076, 2943, 2959) |
| 600 V MCC composition | Traditional MCCs with electronic motor overload relays; H-O-A or On-Off local control stations adjacent to each motor; field-wired back to MCC starter circuits; 600 V VFDs built into the MCC lineup unless dedicated to large motors. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Motor Control section (line 2959) |
| 600 V MCC metering / protection | Include power metering and ground/resistor fault detection; ground-fault protection alarm-only to maintain continuity of operations. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Grounding section (line 2985) |
| 208/120 V derivation | 600 V to 208/120 V distribution transformer(s) with neutral solidly grounded, each feeding its own 208/120 V distribution panelboard. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` 208/120 V section (line 2967) |
| 600 V SCR heater-control panels | Provided in the electrical building where required for process-temperature heater control; supplied by feeder breakers in the 600 V MCC. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (line 2969) |
| Quantity allocation to PKG-034 | TBD. DBM equipment list rows (Low Voltage Switchgear (2), Low Voltage MCCs (1), Low Voltage Induction Motors (2)) are not explicitly allocated to PKG-034 vs other 600 V electrical buildings (PKG-033 840-1, PKG-035 850-1, PKG-040 860-1). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Equipment list (lines 2877-2882); HRR-034-04-002 |
| Bus current rating | TBD | Pending facility load-flow study referenced by DBM |
| Short-circuit / withstand rating | TBD | Pending short-circuit and arc-flash studies referenced by DBM |
| Cable termination basis | Bottom-entry cables; 600 V incoming and outgoing power cables; ACWU for #1/0 AWG and larger and for 600 V transformer secondary to MCC; copper TECK for low-voltage power smaller than #1/0 AWG. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Cables/Raceways (lines 2977, 3010-3012) |

## Operating and Environmental Conditions

| Item | Value | Source |
|---|---|---|
| Installation | Indoor, within a prefabricated modular electrical building, located in a general purpose area. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Area Classification and Electrical Buildings (lines 2911, 2971-2977) |
| Climate control | n+1 HVAC sized so the cooling system tolerates failure or maintenance shutdown of one HVAC unit without affecting heating/cooling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings (line 2975) |
| Cable entry | Bottom entry for incoming and outgoing power cables; building elevated on piles to provide cable-tray space beneath. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings (line 2977) |
| Internal wiring | TECK and ACIC cables; EMT conduit between adjacent equipment (e.g., control panels to contactor panels); outdoor GFI receptacle for exterior maintenance; equipment doors sized (or transomed) for largest-equipment removal. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings (line 2979) |
| Site ambient design conditions | TBD (not stated in accessible electrical source slice) | — |
| Spacing to fired heaters / control room | 25 m (82 ft) minimum where applicable (OGAOM 9.6.15). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (line 298) |

## Construction (Package Composition — ASSUMPTION shape pending vendor scope)

The vendor-engineered package is expected to comprise, at minimum:

- The prefabricated modular electrical building shell with n+1 HVAC, bottom-entry cable provisions, GFI receptacle, and equipment access doors. (ASSUMPTION; grounded in DBM Electrical Buildings description.)
- 600 V MCC lineup(s) with electronic overload relays, integrated 600 V VFDs (except where dedicated standalone is justified), power metering, and ground/resistor fault detection.
- 600 V SCR heater-control panel(s) where required by the served area's process heating.
- 600 V to 208/120 V distribution transformer(s) with solidly grounded neutral and 208/120 V distribution panelboard(s).
- 208/120 V contactor panel(s) for lighting/utility distribution.
- 120 V AC and 125 V DC UPS systems with battery banks and distribution panels as required by the served control and protection loads.
- Plant PLC control panel(s) and network rack(s) integrating to the plant control architecture.
- Vendor-supplied design basis, datasheets, drawings, and qualification documentation supporting the physical equipment package. (Per `_CONTEXT.md` anticipated artifacts.)

Detailed composition (MCC sectional layout, VFD count and rating, UPS sizing and autonomy, transformer kVA, panel schedules, accessory equipment) is `TBD` until the EPC Package Datasheet (`DEL-034-02`) and Scope of Work (`DEL-034-01`) are issued to the Package Vendor.

## Interfaces (per PACKAGE_REGISTER row for PKG-034)

Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports.

Source: `INTERFACE_REGISTER.csv` rows 190-201 for `PKG-034`.

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (this deliverable).
- Gate 7 snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — `DELIVERABLE_REGISTER.csv` (row 189), `PACKAGE_REGISTER.csv` (row 36), `ARTIFACT_REGISTER.csv` (rows 719-720), `INTERFACE_REGISTER.csv` (rows 190-201), `OBJECTIVE_DELIVERABLE_MAP.csv` (rows 455, 989, 1523, 2065, 2497, 3055, 3627, 4172).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Power System, System Voltages, Motor Control, Electrical Buildings, Grounding and Bonding, 208/120 V, Cables/Raceways, Standby Power, Area Classification, Equipment List (lines ~2076, 2811-2816, 2860-3012).
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — facility-level 600 V MCC and standby power context (lines 734, 745, 758-768).
- `_Sources/26020-Package_Requirements.docx` — location TBD (not extracted to accessible markdown).

## Open Items / TBD

- TBD: Building 820-2 not enumerated in the accessible DBM buildings list (HRR-034-04-001).
- TBD: Specific 13.8 kV-to-600 V transformer feed designation for 820-2.
- TBD: Bus current rating, short-circuit/withstand rating, MCC/UPS/transformer kVA and quantity — pending facility load-flow, short-circuit, and arc-flash studies.
- TBD: Quantity allocation of DBM Equipment List "Low Voltage Switchgear (2)", "Low Voltage MCCs (1)", "Low Voltage Induction Motors (2)" to PKG-034 vs other 600 V electrical buildings (HRR-034-04-002).
- TBD: Binding code editions (CEC edition; IEEE/ANSI references for LV switchgear/MCC) pending extraction of `26020-Package_Requirements.docx` (HRR-034-04-003).
- TBD: Sibling `DEL-034-01` Scope of Work and `DEL-034-02` Package Datasheet are normally upstream consumers of vendor commitments; their drafts are not yet established (HRR-034-04-004).
