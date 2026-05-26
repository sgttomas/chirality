# Datasheet — DEL-040-04 Vendor Engineered Equipment Package (600V Electrical Building 860-1)

> Descriptive datasheet for the Package Vendor production unit (engineering, design, fabrication/supply, and the physical equipment package) for `PKG-040 600V ELECTRICAL BUILDING (860-1)`. Values not directly supported by accessible source slices are marked `TBD` or labelled `ASSUMPTION`.

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-040-04_vendor-engineered-equipment-package` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 225 |
| Deliverable Name | Vendor Engineered Equipment Package | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Parent Package | `PKG-040 600V ELECTRICAL BUILDING (860-1)` | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row 42 |
| Workbook Row | 42 | `PACKAGE_REGISTER.csv` row 42 |
| Workbook Package Code | `26020-01-30-031` | `PACKAGE_REGISTER.csv` row 42 |
| WBS | 01 | `PACKAGE_REGISTER.csv` row 42 |
| Discipline | Electrical | `PACKAGE_REGISTER.csv`; `_CONTEXT.md` |
| Deliverable Type | Vendor Package Production Unit | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Responsible Party | Package Vendor (engineering / design / equipment) with EPC Integrator integration review | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Covers Scope Items | `SOW-0041` | `DELIVERABLE_REGISTER.csv` |
| Supports Objectives | `OBJ-001; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010` (PACKAGE_HEURISTIC — ASSUMPTION) | `OBJECTIVE_DELIVERABLE_MAP.csv` rows 110-115 (OBJ-001) and matching rows for OBJ-004/005/006/007/008/009/010 grouped by PKG-040 |

## Attributes (Equipment Subject of the Vendor Package)

| Attribute | Value | Source |
|---|---|---|
| Building identity | "860-1 600V General Area / Tank Farm Electrical Building" — prefabricated modular electrical building serving the facility General Area and Tank Farm at 600 V. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Buildings table (line 2816); Power System (line 2925) |
| Building function | Prefabricated modular electrical building housing 600 V low-voltage distribution and ancillary electrical equipment for the General Area / Tank Farm served area. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings (lines 2971-2979) |
| Low-voltage service basis | 600 V, 3 phase, 3 wire, 60 Hz, high-resistance grounded with 5 A continuous resistor | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` System Voltages (line 2937) |
| Anticipated equipment housed (per DBM building basis) | 600 V MCC(s); 600 V VFDs as part of the MCC lineup; 120 V AC UPS systems with battery banks and distribution panels; 125 V DC UPS systems with battery banks and distribution panels; 600 V to 208/120 V distribution transformer(s) and panelboard(s); 208/120 V contactor panel(s); plant PLC control panel(s); network rack(s). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings (line 2973) |
| Upstream feed (ASSUMPTION) | Radial step-down from the facility 13.8 kV switchgear via a 13.8 kV-to-600 V transformer; the specific transformer designation feeding 860-1 is TBD. DBM Power System line 2925 enumerates a "4.16 kV/600 V General Area/Tank Farm/Process Electrical Building" radial destination — whether this is a single mixed-voltage building or distinct buildings sharing this served area is not explicit. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Power System (lines 2919-2925); Buildings table (line 2816); HRR-040-04-001 |
| Standby power interface | Standby power served at the 600 V MCC level via TOU-typical low-voltage standby generator(s) and transfer switch(es); applicability to 860-1 specifically is ASSUMPTION pending detailed design. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Standby Power and Motor Control sections (lines 2943, 2959) |
| 600 V MCC composition | Traditional MCCs with electronic motor overload relays; H-O-A or On-Off local control stations adjacent to each motor; field-wired back to MCC starter circuits; 600 V VFDs built into the MCC lineup unless dedicated to large motors. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Motor Control section (line 2959) |
| 600 V MCC metering / protection | Include power metering and ground/resistor fault detection; ground-fault protection alarm-only to maintain continuity of operations. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Grounding section (line 2985) |
| 208/120 V derivation | 600 V to 208/120 V distribution transformer(s) with neutral solidly grounded, each feeding its own 208/120 V distribution panelboard. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` 208/120 V section (line 2967) |
| 600 V SCR heater-control panels | Provided in the electrical building where required for process-temperature heater control (e.g., tank-area heaters, freeze-protection circuits served via the building); supplied by feeder breakers in the 600 V MCC. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (line 2969) |
| Quantity allocation to PKG-040 | TBD. DBM equipment list rows for low-voltage switchgear, MCCs, and induction motors (lines 2877-2882) are not explicitly allocated to PKG-040 vs other 600 V electrical buildings (PKG-033 840-1, PKG-034 820-2, PKG-035 850-1). | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Equipment List (lines 2877-2882); HRR-040-04-002 |
| Bus current rating | TBD | Pending facility load-flow study referenced by DBM (line 2901) |
| Short-circuit / withstand rating | TBD | Pending short-circuit and arc-flash studies referenced by DBM (lines 2899-2900) |
| Cable termination basis | Bottom-entry cables; 600 V incoming and outgoing power cables; ACWU for #1/0 AWG and larger and for 600 V transformer secondary to MCC; copper TECK for low-voltage power smaller than #1/0 AWG. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Cables/Raceways (lines 2977, 3010-3012) |

## Operating and Environmental Conditions

| Item | Value | Source |
|---|---|---|
| Installation | Indoor, within a prefabricated modular electrical building, located in a general purpose area. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Area Classification and Electrical Buildings (lines 2911, 2971-2977) |
| Climate control | n+1 HVAC sized so the cooling system tolerates failure or maintenance shutdown of one HVAC unit without affecting heating/cooling. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings (line 2975) |
| Cable entry | Bottom entry for incoming and outgoing power cables; building elevated on piles to provide cable-tray space beneath. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings (line 2977) |
| Internal wiring | TECK and ACIC cables; EMT conduit between adjacent equipment (e.g., control panels to contactor panels); outdoor GFI receptacle for exterior maintenance; equipment doors sized (or transomed) for largest-equipment removal. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Electrical Buildings (line 2979) |
| Site ambient design conditions | TBD (not stated in accessible electrical source slice) | — |
| Spacing to fired heaters / control room | 25 m (82 ft) minimum where applicable. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (line 298) |

## Construction (Package Composition — ASSUMPTION shape pending vendor scope)

The vendor-engineered package is expected to comprise, at minimum:

- The prefabricated modular electrical building shell with n+1 HVAC, bottom-entry cable provisions, GFI receptacle, and equipment access doors. (ASSUMPTION; grounded in DBM Electrical Buildings description.)
- 600 V MCC lineup(s) with electronic overload relays, integrated 600 V VFDs (except where dedicated standalone is justified), power metering, and ground/resistor fault detection.
- 600 V SCR heater-control panel(s) where required by the served area's process heating, freeze protection, and tank-area heating loads.
- 600 V to 208/120 V distribution transformer(s) with solidly grounded neutral and 208/120 V distribution panelboard(s).
- 208/120 V contactor panel(s) for lighting/utility distribution.
- 120 V AC and 125 V DC UPS systems with battery banks and distribution panels as required by the served control and protection loads.
- Plant PLC control panel(s) and network rack(s) integrating to the plant control architecture.
- Vendor-supplied design basis, datasheets, drawings, and qualification documentation supporting the physical equipment package. (Per `_CONTEXT.md` anticipated artifacts and `ARTIFACT_REGISTER.csv` rows for DEL-040-04.)

Detailed composition (MCC sectional layout, VFD count and rating, UPS sizing and autonomy, transformer kVA, panel schedules, accessory equipment) is `TBD` until the EPC Package Datasheet (`DEL-040-02`) and Scope of Work (`DEL-040-01`) are issued to the Package Vendor.

## Interfaces (per PACKAGE_REGISTER row for PKG-040)

Utility Piping; Drain / Containment; Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Building HVAC / Services; Fire & Gas / Safety Systems; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports.

Source: `INTERFACE_REGISTER.csv` 12 rows for `PKG-040` (IFC-C7A10165E0, IFC-84254E4D74, IFC-01418C7B46, IFC-1AFD94C7C5, IFC-31FBC53269, IFC-4924815E92, IFC-07F9E1739B, IFC-E5C808A2AF, IFC-AB1228ED22, IFC-DD57C5C1B0, IFC-CB9A638F41, IFC-327D21980E).

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (this deliverable).
- Gate 7 snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — `DELIVERABLE_REGISTER.csv` (row 225), `PACKAGE_REGISTER.csv` (row 42), `ARTIFACT_REGISTER.csv` (rows 887-888 for DEL-040-04), `INTERFACE_REGISTER.csv` (12 rows for PKG-040), `OBJECTIVE_DELIVERABLE_MAP.csv` (rows grouped under PKG-040 across OBJ-001/004/005/006/007/008/009/010).
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Power System, System Voltages, Motor Control, Electrical Buildings, Grounding and Bonding, 208/120 V, Cables/Raceways, Standby Power, Area Classification, Buildings table, Equipment List (lines ~2811-2820, 2856-3025).
- `_Sources/26020-Package_Requirements.docx` — location TBD (not extracted to accessible markdown).

## Open Items / TBD

- TBD: Specific 13.8 kV-to-600 V transformer feed designation for 860-1, and whether 860-1 shares a building footprint with the 4.16 kV General Area distribution (HRR-040-04-001).
- TBD: Bus current rating, short-circuit/withstand rating, MCC/UPS/transformer kVA and quantity — pending facility load-flow, short-circuit, and arc-flash studies.
- TBD: Quantity allocation of DBM Equipment List low-voltage switchgear, MCC, and induction-motor rows to PKG-040 vs other 600 V electrical buildings (HRR-040-04-002).
- TBD: Binding code editions (CEC edition; IEEE/ANSI references for LV switchgear/MCC) pending extraction of `26020-Package_Requirements.docx` (HRR-040-04-003).
- TBD: Sibling `DEL-040-01` Scope of Work and `DEL-040-02` Package Datasheet are normally upstream consumers of vendor commitments; their drafts are not yet established (HRR-040-04-004).
- TBD: Site ambient design conditions for the General Area / Tank Farm location.
