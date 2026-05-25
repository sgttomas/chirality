# Datasheet: DEL-018-04 — Vendor Engineered Equipment Package (PKG-018 MV VFD)

Descriptive datasheet for the Package Vendor production unit that engineers, designs, fabricates/supplies, and delivers the physical MV VFD equipment package for PKG-018.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-018-04_vendor-engineered-equipment-package` | `_CONTEXT.md`; GATE-07 `DELIVERABLE_REGISTER.csv` row 93 |
| Deliverable Name | Vendor Engineered Equipment Package | `_CONTEXT.md`; GATE-07 `DELIVERABLE_REGISTER.csv` row 93 |
| Parent Package | `PKG-018` — MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD | `_CONTEXT.md`; GATE-07 `PACKAGE_REGISTER.csv` row 20 |
| Workbook Row | Packages row 20 | GATE-07 `PACKAGE_REGISTER.csv` row 20 |
| WBS | 02 | GATE-07 `PACKAGE_REGISTER.csv` row 20 |
| Discipline | Electrical | `_CONTEXT.md`; GATE-07 `PACKAGE_REGISTER.csv` row 20 |
| Deliverable Type | Vendor Package Production Unit | GATE-07 `DELIVERABLE_REGISTER.csv` row 93 |
| Responsible Party | Package Vendor (engineering/design/equipment), with EPC Integrator integration review | `_CONTEXT.md`; GATE-07 `DELIVERABLE_REGISTER.csv` row 93 |
| Covers Scope Items | `SOW-0019` | `_CONTEXT.md`; GATE-07 `DELIVERABLE_REGISTER.csv` row 93 |
| Supports Objectives | `OBJ-002`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010` (PACKAGE_HEURISTIC association — **ASSUMPTION**) | `_CONTEXT.md`; GATE-07 `OBJECTIVE_DELIVERABLE_MAP.csv` rows 425, 893, 1427 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package nominal service | Medium-voltage variable-frequency drive (MV VFD) for a 5000 HP class, 4160 V, 3-phase, 60 Hz motor on a 4160 V VFD bus | GATE-07 `PACKAGE_REGISTER.csv` row 20 (package title) |
| Package owner (engineering/design/equipment) | Package Vendor | GATE-07 `PACKAGE_REGISTER.csv` row 20 (Ownership column) |
| Facility integration owner | EPC Integrator (interfaces, tie-ins, constructability, facility-level integration) | GATE-07 `PACKAGE_REGISTER.csv` row 20 (Ownership column) |
| Applicable interface types | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports | GATE-07 `PACKAGE_REGISTER.csv` row 20 (Interfaces column) |
| Upstream EPC anchors | EPC Scope of Work (`DEL-018-01`); EPC Package Datasheet (`DEL-018-02`) | GATE-07 `DELIVERABLE_REGISTER.csv` rows 90, 91, 93; `_CONTEXT.md` |
| Driven equipment basis (informational, not in this package) | Inlet/sales gas compressor motors (KM-2150 / KM-2250) per DBM are 3,878 kW / 5,200 hp at 4,000 V, 3-phase, 60 Hz, 8-pole approximately 891 rpm, continuous inverter duty, with starting VFD per SCA-001 VE #34 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 324, 533 |
| Detailed VFD topology, output voltage match, harmonic filters, drive isolation transformer | TBD — to be developed by vendor engineering during detailed design | DBM notes electrical detailed design item; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 326; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 3088 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service environment | Outdoor / electrical-building installation per facility electrical building basis; detailed environment TBD pending EPC Package Datasheet | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2973 (Electrical buildings basis) |
| Hazardous area | Zone 2 marking required for VFD-fed motors located in Zone 2 areas, with temperature code lower than the area-classification or fugitive-emissions study value (motor-side rule applied to VFD-driven motors); package zone allocation TBD | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2961 |
| Source bus | 4160 V class MV bus (package title); SCA-001 VE #37 removes capacitor banks from synchronous-transfer buses where VFDs are present | GATE-07 `PACKAGE_REGISTER.csv` row 20; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 756 |
| Harmonic / reactive-power mitigation | Determined by detailed electrical studies | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 756 |
| Coordination with MCC starting basis | DBM indicates VFD and soft-starter requirements for 4.16 kV motors are TBD in the Deepcut narrative; the 03-25 Comp_and_Liquids basis is starting VFD for inlet compressors | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` lines 2957, 3088; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 326, 756 |
| Functional duty cycle (starting only vs continuous) | TBD — see Guidance Conflict Table | DBM excerpts above |

## Construction

| Item | Description | Source |
|---|---|---|
| Package boundary | Vendor-engineered MV VFD lineup as a packaged assembly (drive cubicle(s), required transformers/reactors/filters per vendor design, control and HMI, package internal cabling); package boundary, lineup arrangement, and shipping splits TBD by vendor engineering | GATE-07 `DELIVERABLE_REGISTER.csv` row 93 (Anticipated Artifacts); `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2973 |
| Enclosure / location | Electrical building (prefabricated, modular) — assumption based on facility electrical building basis | **ASSUMPTION** from `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2973 |
| Communications | EtherNet to plant PLC central control panel — assumption derived from 4160V MCC convention; vendor protocol/topology TBD | **ASSUMPTION** from `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 754; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2957 |
| External cabling type (load side) | Copper TECK cable for low-voltage power cable fed from VFDs (does not constrain MV-side cabling) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 3013 |
| Vendor documentation set | Vendor package design basis and datasheet set; submittals; turnover records (assembled separately under `DEL-018-05`) | GATE-07 `DELIVERABLE_REGISTER.csv` rows 93, 94 |

## References

- `_CONTEXT.md` (this deliverable folder)
- `_REFERENCES.md` (this deliverable folder)
- `_DEPENDENCIES.md` (this deliverable folder)
- GATE-07 snapshot: `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/`
  - `DELIVERABLE_REGISTER.csv` rows 90-95 (PKG-018 deliverable set; this deliverable is row 93)
  - `PACKAGE_REGISTER.csv` row 20 (PKG-018)
  - `OBJECTIVE_DELIVERABLE_MAP.csv` rows 425, 893, 1427 (and other OBJ rows for PKG-018)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` — driven-motor and 4160V MCC basis (lines 324, 326, 533, 744, 752, 754, 756, 760)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — 4.16 kV MCC starting basis and electrical building basis (lines 893, 1004, 1027, 2955, 2957, 2959, 2961, 2963, 2973, 3013, 3088)
- Sibling EPC anchor deliverables (read-only context): `DEL-018-01` Scope of Work; `DEL-018-02` Package Datasheet
