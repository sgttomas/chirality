# Guidance: DEL-023-02_package-datasheet

## Purpose

The Package Datasheet exists to convert the accepted Gate 7 package basis for `PKG-023` into a source-supported technical handoff document. It should let the Package Vendor understand the EPC integration basis for the "MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD" package while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried as "MV VFD - 1500HP, 4160V, 3PH, 60HZ - 4160V VFD" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence carried under the Package Datasheet, not as separate deliverables.
- Keep vendor-owned design work with the Package Vendor and facility-level integration with the EPC Integrator.
- Use `TBD` for VFD topology, harmonic mitigation, isolation transformer, bypass, cooling, driven equipment identification, building/room assignment, and support details until a source-supported package-specific basis is available.
- Use the DBM electrical basis only at the level it supports: voltage class assignment, MV MCC arrangement, Starting VFD precedent, electrical-building housing possibilities, grounding/bonding, cable tray, conduit, motor space heaters, and VFD-fed motor area-classification marking.

## Considerations

The DBM electrical basis assigns motors larger than 250 hp to 4,000 V or 13.2 kV, and explicitly defers VFD and soft-starter requirements for 4.16 kV motors. The DBM Starting VFD precedent applies to the KM-2150/2250 Inlet/Sales Gas Compressor motors with synchronous transfer to a normal-service bus; whether PKG-023 follows that starting-and-transfer pattern, a continuous-duty drive pattern, or another topology is not stated in the accessible source set.

The DBM driver inventory (Electric Compressor Drivers and other motor-driven service tables) does not list a 1500 hp / 4160 V service entry that can be tied to PKG-023 by name. The package name therefore carries nameplate-style identity, but the driven equipment service is not identified from accessible source.

The DBM identifies that electrical buildings may house medium-voltage VFDs as required by detailed design, and that VFD-fed motors located in Zone 2 areas must be marked and temperature-coded accordingly. Neither the installation location nor the area classification of the driven motor served by this package is stated in the accessible source set.

Grounding/bonding and maintenance access are applicable interface topics. The DBM source contains facility grounding basis (two-point ground grid connection for major electrical equipment, separate copper ground conductors per CEC for transformers, panelboards, and 100+ hp three-phase motors) and a cable tray/conduit constraint (must not interfere with maintenance access).

The package-specific Word requirements source did not produce a PKG-023 match during this run. Vendor-facing datasheet content should remain conservative until the missing detailed requirements are resolved.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| 4.16 kV VFD topology | Mark `TBD` pending detailed engineering. | DBM explicitly says "VFD and soft-starter requirements for 4.16 kV motors are TBD." |
| Driven service / load identification | Treat package name as nameplate identity; do not assign a driven service from the DBM driver inventory. | No 1500 hp / 4160 V entry in the DBM Electric Compressor Drivers table or other accessible service tables. |
| Starting vs. continuous-duty VFD | Mark `TBD` rather than inherit the KM-2150/2250 Starting-VFD pattern. | The Starting-VFD pattern in DBM is specific to inlet/sales gas compressors; transfer or duty cycle for PKG-023 is not stated. |
| Installation location | Identify as possible context (electrical building), not a confirmed location. | DBM says electrical buildings may house MV VFDs but does not locate PKG-023. |
| MV cable type | Mark `TBD` for MV VFD output cable. | DBM cable schedule explicitly cites TECK for "Low-voltage power cable fed from VFDs"; MV VFD output cable type is not in the accessible slice. |
| Standards | List CEC, area classification, NEMA MG 1, and project electrical specifications as governing bases with locations TBD. | DBM references these bases but detailed clauses/specification documents are not available in the deliverable folder. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 25 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Driven service: TBD. No accessible source slice identifies the load served by this MV VFD package."
- Not acceptable without new source: "VFD output is continuous-duty with line-side harmonic filter and integral isolation transformer at 4160 V to a specific compressor frame." The accessible source set does not establish this configuration.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-023-02-001 | The workbook/package title asserts a 1500 hp / 4160 V VFD package, but the DBM 4.16 kV MCC paragraph and 4.16 kV motor starting table both state that VFD and soft-starter requirements for 4.16 kV motors are TBD. | Workbook Packages row 25; `PACKAGE_REGISTER.csv` row `PKG-023` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, 4.16 kV MCC paragraph; 4.16 kV motor starting table row | Datasheet Attributes/Construction; Specification Requirements; Procedure Steps | Treat package title as nameplate identity; keep VFD topology, isolation transformer, harmonic mitigation, bypass, and cooling as `TBD` until a detailed 4.16 kV VFD basis or vendor package data is accepted. | TBD |
| HRR-023-02-002 | The driven equipment (load served by this MV VFD package) is not identified in the accessible source slices; the DBM Electric Compressor Drivers inventory does not list a 1500 hp / 4160 V service. | Workbook Packages row 25 (package name only) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, Prime Mover and Major Driver Inventory; Electric Compressor Drivers table | Datasheet Attributes; Specification Requirements; Procedure Steps | Do not assign a driven service to PKG-023 from the DBM driver inventory; carry the driven equipment identification as `TBD` pending human or project-design ruling. | TBD |
| HRR-023-02-003 | The DBM identifies "Starting VFDs" for KM-2150/2250 Inlet/Sales Gas Compressor motors with synchronous transfer, but does not state whether PKG-023 is a starting VFD with transfer, a continuous-duty drive, or another topology. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, MCC-8200 / Starting VFD paragraphs | Workbook Packages row 25; `PACKAGE_REGISTER.csv` row `PKG-023` | Datasheet Attributes; Specification Requirements | Mark starting/duty topology as `TBD` and do not inherit the KM-2150/2250 Starting-VFD pattern by default. | TBD |
