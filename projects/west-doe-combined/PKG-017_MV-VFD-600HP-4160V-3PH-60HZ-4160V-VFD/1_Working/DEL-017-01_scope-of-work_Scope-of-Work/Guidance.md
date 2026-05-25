# Guidance: DEL-017-01_scope-of-work

## Purpose

The Scope of Work exists to convert the accepted Gate 7 package basis for `PKG-017` into a source-supported EPC anchor document defining the full package scope, tagged equipment basis, package function, source basis, boundaries, and whole-facility integration narrative for the workbook-named MV VFD package. It should let the Package Vendor receive a clear EPC scope envelope while keeping EPC-owned facility interfaces distinct from vendor-owned package design.

## Principles

- Preserve source spelling and identity. The package name is carried verbatim as "MV VFD - 600HP, 4160V, 3PH, 60HZ - 4160V VFD" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as evidence under the Scope of Work, not as separate deliverables.
- Keep vendor-owned design work (VFD topology, sizing, converter/inverter selection, cooling, harmonic filter selection) with the Package Vendor and facility-level integration with the EPC Integrator.
- Use `TBD` for driven-equipment identity, VFD rating, tagged equipment, vendor BOM, building/room assignment, supports, and harmonic mitigation approach until a source-supported package-specific basis is available.
- Use DBM electrical basis only at the level it supports: MV service voltage, 4160V MCC interface basis, starting-VFD policy (SCA-001 VE #34), capacitor-bank policy (SCA-001 VE #37), raceway separation, maintenance-access constraints, and area classification.

## Considerations

The DBM electrical design basis (3-25 Comp_and_Liquids) establishes a 4,160 V, 3 phase, 3 wire, 60 Hz LRG medium-voltage service intended for process AC inverter-drive motors from 250 hp to 5,500 hp. It positions the 4160V MCC as the integration point for large 4000V motors, with field-fused contactors, motor protection relays, and an EtherNet port to the plant PLC central control panel for data acquisition.

The DBM identifies starting VFDs as the supersession basis for the inlet compressor motors KM-2150 and KM-2250 under SCA-001 VE #34, and removes capacitor banks from the synchronous bus on MCC-8200 where VFDs are present under SCA-001 VE #37. Harmonic and reactive-power mitigation are explicitly deferred to detailed electrical studies, and VFD sizing is explicitly an electrical detailed-design item. These items should be reflected in the Scope of Work as governing constraints, not pre-resolved as design choices.

The workbook row and Gate 7 registers establish the existence of PKG-017, its WBS 02 placement, CoA tracking, applicable interface facts, and supported objectives. They do not establish a specific tagged motor, a specific compressor train, or a specific VFD rating beyond the workbook title string.

Maintenance access is both an explicit workbook interface fact and a DBM routing constraint for cable tray and conduit. The Scope of Work should require electrical routing and physical placement to preserve maintenance access while leaving detailed clearances to detailed design or vendor data.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Title "600HP, 4160V" vs DBM 4000V/5,200 hp inlet compressor drives | Treat the workbook title as identity only; do not assert a 600 hp 4160V VFD load until human ruling. | DBM identifies the MV process drives as 4,000 V / 3,878 kW (5,200 hp), and explicitly assigns 600 V VFDs to the 600V MCC lineup. A "600HP, 4160V" MV VFD load is not corroborated by accessible source slices. |
| Driven-equipment identity | Mark `TBD` pending workbook/vendor confirmation. | The Scope of Work cannot assign a specific compressor or other prime mover without source support. |
| Harmonic / reactive-power mitigation | Carry as a downstream electrical study item; do not commit to filters, reactors, or capacitor strategies. | DBM defers this explicitly to detailed electrical studies. |
| VFD topology and sizing | Mark `TBD`; identify as vendor/detailed-design scope. | DBM states VFD sizing is an electrical detailed-design item. |
| Installation location | Identify possible electrical-building context only; do not assign a building/room. | DBM places MV MCCs in electrical buildings but does not locate PKG-017. |
| Standards | List CEC, area classification, project electrical specifications, NEMA MG1 (conditional), SCA-001 VE #34/#37 as governing bases with clause/document locations `TBD` where not directly accessible. | DBM references these bases but detailed clauses/specification documents are not available in the deliverable folder. |

## Examples

- Acceptable scope-of-work entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 19 and `INTERFACE_REGISTER.csv`."
- Acceptable governance citation: "Starting VFDs are the SCA-001 VE #34 basis for the inlet compressor motors; soft starts are not used under the current basis."
- Acceptable source-gap entry: "Driven-equipment tag and VFD rating: TBD. No package-specific source slice available; workbook title and DBM MV drive ratings disagree (see Conflict Table HRR-017-01-001)."
- Not acceptable without new source: "PKG-017 is a 600 hp 4160V VFD driving motor M-XXXX." The accessible source set does not establish this assignment.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-017-01-001 | Workbook package title is "MV VFD - 600HP, 4160V" but DBM identifies MV process inverter-drive motors at 4,000 V / 3,878 kW (5,200 hp) (KM-2150/KM-2250) and places 600 V VFDs in the 600V MCC lineup. A "600HP, 4160V" MV VFD load is not corroborated. | Workbook Packages row 19; `PACKAGE_REGISTER.csv` row `PKG-017` | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Inlet Compressor Drive section and 600V MCC and Standby Power section | Datasheet Attributes; Specification Requirements REQ-017-01-009; Procedure Steps | Treat the workbook title as identity only; keep driven-equipment identity, VFD rating, and tagged equipment as `TBD` until the human confirms the intended load and voltage class. | TBD |
| HRR-017-01-002 | No accessible source slice identifies the specific driven motor/equipment, motor tag, VFD tag, or vendor for PKG-017. | Workbook Packages row 19 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical equipment narrative; `_Sources/26020-Package_Requirements.docx` (not machine-readable in this run) | Datasheet Attributes/Construction; Specification REQ-017-01-010; Procedure Records | Carry tagged equipment, vendor identity, and load identity as `TBD` until a source-supported package-specific match is confirmed. | TBD |
