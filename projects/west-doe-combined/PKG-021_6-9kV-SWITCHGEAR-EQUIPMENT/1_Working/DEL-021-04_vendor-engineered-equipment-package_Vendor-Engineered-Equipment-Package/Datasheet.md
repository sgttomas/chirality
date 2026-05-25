# Datasheet — DEL-021-04 Vendor Engineered Equipment Package (6.9 kV Switchgear Equipment)

> Descriptive datasheet for the Package Vendor production unit (engineering, design, fabrication/supply, and the physical equipment package) for `PKG-021 6.9kV SWITCHGEAR EQUIPMENT`. Values not directly supported by accessible source slices are marked `TBD` or labelled `ASSUMPTION`.

## Identification

| Field | Value |
|---|---|
| Deliverable ID | `DEL-021-04_vendor-engineered-equipment-package` |
| Deliverable Name | Vendor Engineered Equipment Package |
| Parent Package | `PKG-021 6.9kV SWITCHGEAR EQUIPMENT` |
| Workbook Row | 23 |
| Workbook Package Code | `26020-01-30-012` (PACKAGE_REGISTER row for PKG-021) |
| Discipline | Electrical |
| Type | Vendor Package Production Unit |
| Responsible Party | Package Vendor (engineering / design / equipment) with EPC Integrator integration review |
| Covers Scope Items | `SOW-0022` |
| Supports Objectives | `OBJ-001, OBJ-004, OBJ-005, OBJ-006, OBJ-008, OBJ-009, OBJ-010` (PACKAGE_HEURISTIC — ASSUMPTION) |

## Attributes (Equipment Subject of the Vendor Package)

| Attribute | Value | Source |
|---|---|---|
| Nominal system voltage served | 6.9 kV | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` System Voltages table |
| Phases / wires / frequency | 3 phase, 3 wire, 60 Hz | Same source, System Voltages table |
| System grounding | Low-resistance grounded; 100 A, 10 s neutral grounding resistor per 6.9 kV transformer; operates as a tripping system | Same source, Grounding and Bonding section |
| Functional role | Medium-voltage distribution for facility process AC inverter-drive motors rated 5,500 hp and above (Inlet/Sales Compressor Electrical Building) | Same source, System Voltages and Power System sections |
| Associated electrical building | 820-1 6.9 kV Inlet / Sales Compressor Electrical Building (shop-fab modular) | Same source, Buildings list and Electrical Buildings section |
| Associated MCC | `MCC-8200` 6.9 kV motor control center (mechanically latched fused contactors, motor protection relays, Ethernet to plant PLC) | Same source, Motor Control section |
| Associated starting equipment | Starting VFDs for `KM-2150` / `KM-2250` Inlet/Sales Gas Compressor motors | Same source, Motor Control section |
| Power-factor correction | PFCC banks shall NOT be installed on the `MCC-8200` synchronous-transfer bus | Same source, Motor Control section |
| Upstream feed | Radial step-down from facility 13.8 kV switchgear | Same source, Power System section |
| Quantity of 6.9 kV switchgear lineups in PKG-021 | TBD — equipment list row "Medium Voltage Switchgear (1)" in DBM-Deepcut section 27 is not explicitly allocated to PKG-021 vs. other MV packages | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line ~2880; HRR-021-04-001 |
| Continuous bus current rating | TBD | Pending load-flow study (DBM lists load-flow study as TBD-defined) |
| Short-circuit / withstand rating | TBD | Pending short-circuit and arc-flash studies |
| BIL | TBD | Not stated in accessible sources |
| Enclosure / construction (metal-clad / metal-enclosed) | TBD | Not stated in accessible sources |
| Compartmentation, breaker type | TBD | Not stated in accessible sources |
| Protection and metering scheme | Motor protection relays integrated with MCC; bus-level protection TBD; relay coordination and arc-flash study identified as required electrical study | DBM electrical studies list and Motor Control section |

## Operating and Environmental Conditions

| Item | Value | Source |
|---|---|---|
| Installation | Indoor, within prefabricated modular electrical building (Building 820-1) | DBM Electrical Buildings section |
| Area classification at install location | General purpose (electrical building located in general-purpose area) | DBM Area Classification section |
| Climate control | n+1 HVAC in electrical building | DBM Electrical Buildings section |
| Cable entry | Bottom entry; building elevated on piles | DBM Electrical Buildings section |
| Site ambient design conditions | TBD (not stated in accessible electrical source slice) | — |

## Construction (Package Composition — ASSUMPTION shape pending vendor scope)

The vendor-engineered package is expected to comprise, at minimum:

- 6.9 kV switchgear lineup(s) including main, tie (if any), and feeder breakers serving the 6.9 kV MCC `MCC-8200` and any direct medium-voltage loads. (ASSUMPTION — composition pending detailed engineering and `DEL-021-02 Package Datasheet`.)
- Protection, metering, and control devices integrated with plant PLC over Ethernet. (Grounded in DBM motor-control statement; bus-level scope ASSUMPTION.)
- Vendor-supplied design basis, datasheets, drawings, and qualification documentation supporting the physical equipment package. (Per `_CONTEXT.md` anticipated artifacts.)

Detailed construction (lineup arrangement, breaker count, ratings, accessory equipment, instrument transformers, surge protection, station service) is `TBD` until the EPC Package Datasheet (`DEL-021-02`) and Scope of Work (`DEL-021-01`) are issued to the Package Vendor.

## Interfaces (per PACKAGE_REGISTER row for PKG-021)

Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports.

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (this deliverable)
- Gate 7 snapshot: `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/` — `DELIVERABLE_REGISTER.csv`, `PACKAGE_REGISTER.csv`, `OBJECTIVE_DELIVERABLE_MAP.csv`
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Power System, System Voltages, Motor Control, Grounding, Electrical Buildings, equipment lists (lines ~2811-2985)
- `_Sources/26020-Package_Requirements.docx` — location TBD (text not extracted into accessible markdown slice)

## Open Items / TBD

- TBD: bus current rating, short-circuit/withstand rating, BIL, enclosure construction, breaker type — all pending load-flow and short-circuit/arc-flash studies.
- TBD: quantity allocation of "Medium Voltage Switchgear" in the DBM equipment list to PKG-021 specifically (HRR-021-04-001).
- TBD: scope-split between Package Vendor and EPC Integrator at the bottom-cable-entry, grounding tie-in, and PLC network demarcation points (pending `DEL-021-01` Scope of Work).
