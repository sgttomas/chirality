# Guidance: DEL-011-04_vendor-engineered-equipment-package

## Purpose

The Vendor Engineered Equipment Package exists to convert the EPC package Scope of Work and Package Datasheet basis for PKG-011 into a vendor-owned engineered, fabricated/supplied 4160V switchgear equipment package. The EPC Integrator remains responsible for facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and integration review.

Sources: Gate 7 `PACKAGE_REGISTER.csv`, PKG-011; Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-011-04.

## Principles

- Keep vendor scope and EPC integration scope distinct. The Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package evidence; the EPC Integrator owns facility-level integration and interface acceptance.
- Treat the Gate 7 package/register basis and DBM SEC-12 electrical basis as the current accepted source basis for Phase 2.2 drafting.
- Carry unsupported vendor-specific detail as `TBD` until vendor documents or accepted EPC design sources establish it.
- Preserve interface completeness for Electrical Power, Grounding / Bonding, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports.
- Do not infer switchgear construction ratings, lineup arrangements, protection settings, or test criteria from generic practice where the source slice does not state them.

## Considerations

- The DBM identifies 4,160 V, 3 phase, 3 wire, 60 Hz LRG as the medium-voltage service basis for process AC inverter-drive motors from 250 hp to 5,500 hp. This is the primary electrical basis for the vendor package until superseded by accepted design truth.
- The incoming transformer basis is 13.8 kV to 4.16 kV, 12 MVA for the 4160V MCC serving 4000V motors.
- The 4160V MCC source basis includes field-fused contactors, motor protection relays, and an EtherNet communication port to the plant PLC central control panel for data acquisition.
- KM-2150 and KM-2250 are specifically identified as large 4000V motor loads served by the MCC, and the source basis requires starting VFDs for those inlet compressor motors.
- Harmonic and reactive-power mitigation remains study-dependent. Vendor design should avoid closing this issue without the detailed electrical studies or an accepted human/design ruling.
- Area classification, electrical building HVAC/ventilation, hazardous area classification, and controls architecture affect package interfaces even when the vendor package is not the building deliverable itself.

Sources: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 Electrical Basis.

## Trade-offs

| Topic | Trade-off / caution |
|---|---|
| Vendor detail vs. source fidelity | Richer vendor detail would improve usefulness, but unsourced details must remain `TBD` until vendor design is available. |
| Package ownership vs. facility integration | Vendor engineering can define package internals, but EPC review must preserve facility-level interface consistency. |
| VFD/starter basis | The DBM basis is explicit for KM-2150/KM-2250 VFDs and no soft starts; any vendor deviation needs formal review. |
| Harmonic/reactive-power mitigation | Premature mitigation selection could conflict with future electrical studies; keep it open until studies determine the basis. |

## Examples

- Example source-grounded requirement: "Vendor design shall support 4,160 V, 3 phase, 3 wire, 60 Hz LRG medium-voltage service." Source: DBM SEC-12 System Voltages.
- Example source-grounded interface item: "Communications / Network interface applies to PKG-011." Source: Gate 7 `INTERFACE_REGISTER.csv`, PKG-011.
- Example `TBD`: switchgear lineup dimensions and enclosure ratings, because no accessible source slice states them for DEL-011-04.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-011-04-001 | Package name is "4160V SWITCHGEAR EQUIPMENT", while the DBM source slice specifically describes a "4160V MCC" serving 4000V motors. It is unclear whether the vendor package should be titled/handled as switchgear, MCC, or a combined lineup. | Gate 7 `PACKAGE_REGISTER.csv`, PKG-011 | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, SEC-12 4160V MCC | Datasheet Attributes; Specification Requirements; Procedure Steps | Use Gate 7 package name for deliverable identity and DBM 4160V MCC text only as the available electrical basis until EPC/vendor source clarifies equipment nomenclature. | TBD |
| HRR-011-04-002 | Detailed vendor document, inspection, factory test, and turnover requirements are expected but not stated in the accessible source slice for this deliverable. | Gate 7 `ARTIFACT_REGISTER.csv`, DEL-011-06 vendor test evidence | DEL-011-04 accessible sources | Specification Documentation; Procedure Records | Keep DEL-011-04 vendor package documentation requirements limited to design basis/datasheet/physical package and defer detailed test/turnover requirements to vendor review/acceptance deliverables unless human rules otherwise. | TBD |
