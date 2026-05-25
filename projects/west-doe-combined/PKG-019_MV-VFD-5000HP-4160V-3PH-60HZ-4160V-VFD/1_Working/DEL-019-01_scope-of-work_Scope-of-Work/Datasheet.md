# Datasheet: DEL-019-01 Scope of Work

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-019-01_scope-of-work | `_CONTEXT.md` Identity |
| Deliverable name | Scope of Work | `_CONTEXT.md` Identity |
| Parent package | PKG-019 | `_CONTEXT.md` Identity; Gate 7 `PACKAGE_REGISTER.csv` row PKG-019 |
| Package name | MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD | Gate 7 `PACKAGE_REGISTER.csv` row PKG-019; `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 21 |
| Workbook ID / row | ID 19 / row 21 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 21 |
| WBS | 02 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 21 |
| Tracking number | 26020-02-30-009 | `_Sources/26020-Packages_Interfaces_4_export.xlsx` Packages row 21 |
| Discipline | Electrical | `_CONTEXT.md` Identity; workbook Packages row 21 |
| Deliverable type | EPC Scope of Work | `_CONTEXT.md` Identity |
| Responsible party | EPC Integrator | `_CONTEXT.md` Identity |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package execution model | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package; EPC Integrator owns facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-019 |
| Mandatory EPC anchor deliverable | Scope of Work is one of the mandatory EPC Integrator deliverables for every approved package. | Gate 7 `PROJECT_DECOMP.md` mandatory EPC anchor deliverable basis; `_CONTEXT.md` Notes |
| Scope item | SOW-0020 | `_CONTEXT.md` Covers Scope Items; Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-019-01 |
| Supported objectives | OBJ-002; OBJ-004; OBJ-005; OBJ-006; OBJ-008; OBJ-009; OBJ-010 | `_CONTEXT.md` Supports Objectives; Gate 7 `DELIVERABLE_REGISTER.csv` row DEL-019-01 |
| Anticipated artifacts | Package scope of work; tagged equipment and package identity list; package function and integration narrative; responsibility assignment record. | `_CONTEXT.md` Anticipated Artifacts |
| Tagged equipment | TBD; no equipment tag is exposed in the accessible workbook row or Gate 7 package row for PKG-019. The DBM identifies inlet compressors `KM-2150` and `KM-2250` as VFD-started 4,000 V motors, but assignment of those VFDs to PKG-019 is not confirmed in the accessible sources. See Conflict Table HR-019-01-02. | Workbook Packages row 21; Gate 7 `PACKAGE_REGISTER.csv` row PKG-019; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 324-326, 533, 752-756 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Facility MV electrical context | DBM identifies a 13.8 kV to 4.16 kV, 12 MVA transformer feeding the 4160V MCC, which serves large 4000V motors including inlet compressors `KM-2150` and `KM-2250`; SCA-001 VE #34 requires starting VFDs for those inlet compressor motors. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 744, 752-756, 324-326 |
| Motor basis referenced in DBM | 4,000 V, three-phase, 60 Hz, ~3,878 kW / 5,200 hp inlet compressor motor; NEMA MG1 compliant; TEFC or WPII; Class F insulation, Class B rise; ~891 rpm 8-pole; continuous inverter duty; starting VFD per SCA-001 VE #34. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 324, 533 |
| Package interfaces | Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. | Workbook Packages row 21; Gate 7 `PACKAGE_REGISTER.csv` row PKG-019 |
| Package-specific exclusions | TBD; no package-specific exclusions stated in source materials (Gate 7 record). | Gate 7 `PACKAGE_REGISTER.csv` row PKG-019 |
| Package title vs. DBM motor voltage | Package name reads "MV VFD - 5000HP, 4160V, 3PH, 60HZ - 4160V VFD" while DBM describes the inlet compressor motors served by the 4160V MCC as 4,000 V / ~5,200 hp; voltage class designation (4.16 kV system vs. 4,000 V motor nameplate) and 5000HP vs. 5200HP figures are not reconciled in accessible sources. | Gate 7 `PACKAGE_REGISTER.csv` row PKG-019; `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 324, 744, 752 |
| Design values for VFD topology, harmonic filtering, transformer/reactor configuration, enclosure, cooling, footprint, weights, environmental rating | TBD; not present in accessible source slices for this deliverable. | Workbook Packages row 21; Gate 7 PKG-019 rows; DBM electrical sections |
| Harmonic / reactive-power mitigation basis | DBM notes SCA-001 VE #37 removes capacitor banks from the synchronous bus on MCC-8200 where VFDs are present; harmonic and reactive-power mitigation is to be determined by detailed electrical studies. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` lines 756 |

## Construction

| Construction / integration topic | Scope-of-work treatment |
|---|---|
| EPC integration boundary | Include facility-level integration, tie-ins, constructability, procurement/construction coordination, and interface management; do not assign vendor package engineering, package design, vendor documentation, or physical equipment package supply to the EPC Integrator. |
| Electrical Power | Identify the package as a medium-voltage power interface to the 4160V system; coordinate with the 13.8 kV to 4.16 kV / 12 MVA transformer and 4160V MCC basis described in the DBM; detailed VFD-side electrical studies are TBD. |
| Grounding / Bonding | Carry grounding/bonding as an interface requiring EPC review and construction coordination at the VFD lineup and downstream motor circuits. |
| I&C / Control Cabling | Carry control and monitoring cabling between the VFD, plant control system, and driven motor as an interface; specific I/O list and control philosophy are TBD pending vendor data. |
| Communications / Network | Carry communications/network as an interface (e.g., to plant PLC / data acquisition consistent with the DBM EtherNet basis for the 4160V MCC); specific protocols, ports, and addressing are TBD. |
| Maintenance Access | Carry maintenance access as an interface requiring layout, clearance, and handoff coordination. |
| Structural / Foundations / Supports | Carry structural/support requirements as interface scope; package-specific loads, footprint, and support details are TBD pending vendor data. |

## References

- `_CONTEXT.md`, DEL-019-01 identity, scope, artifacts, objective context.
- `_DEPENDENCIES.md`, declared dependency state.
- Gate 7 `PROJECT_DECOMP.md`, package anchor deliverable basis.
- Gate 7 `PACKAGE_REGISTER.csv`, row PKG-019.
- Gate 7 `DELIVERABLE_REGISTER.csv`, row DEL-019-01_scope-of-work.
- Gate 7 `INTERFACE_REGISTER.csv`, PKG-019 rows.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx`, Packages row 21.
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical and 4160V MCC sections (lines 324-326, 533, 744-756).
