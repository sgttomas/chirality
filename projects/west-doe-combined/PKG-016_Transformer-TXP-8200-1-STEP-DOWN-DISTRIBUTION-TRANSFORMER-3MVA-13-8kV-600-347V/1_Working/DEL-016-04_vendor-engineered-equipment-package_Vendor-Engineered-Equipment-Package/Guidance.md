# Guidance: DEL-016-04_vendor-engineered-equipment-package

## Purpose

The Vendor Engineered Equipment Package exists to convert the EPC package Scope of Work and Package Datasheet basis for PKG-016 into a vendor-owned engineered, fabricated/supplied 3 MVA, 13.8 kV / 600 / 347 V step-down distribution transformer (TXP-8200-1) package. The EPC Integrator remains responsible for facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination, and integration review.

Sources: Gate 7 `PACKAGE_REGISTER.csv`, PKG-016; Gate 7 `DELIVERABLE_REGISTER.csv`, DEL-016-04.

## Principles

- Keep vendor scope and EPC integration scope distinct. The Package Vendor owns package engineering, package design, vendor documentation, and physical equipment package evidence; the EPC Integrator owns facility-level integration and interface acceptance.
- Treat the Gate 7 package/register basis and the DBM electrical basis (System Voltages; Incoming Power and Transformers; 600V MCC and Standby Power) as the current accepted source basis for Phase 2.2 drafting.
- Carry unsupported vendor-specific detail as `TBD` until vendor documents or accepted EPC design sources establish it.
- Preserve interface completeness for all seven Gate 7 PKG-016 interface facts: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports.
- Do not infer transformer construction ratings (cooling, impedance, BIL, vector group), insulating medium, or test criteria from generic transformer practice where the source slice does not state them.

## Considerations

- The DBM Incoming Power and Transformers section explicitly identifies a "13.8 kV to 600 V, 3 MVA transformer" serving the 600 V MCC for LV loads, which matches PKG-016 / TXP-8200-1 by capacity and primary/secondary voltage.
- The DBM System Voltages table establishes 600 V, 3 phase, 3 wire, 60 Hz HRG with a 5 A continuous resistor as the LV service basis. This is the secondary-side coordination basis for the vendor design.
- The DBM does not separately enumerate a 347 V service. The 600/347 V designation in the package name is consistent with the typical Canadian 600 V wye line-to-neutral derivation, but this is an inference and shall not be treated as source-established.
- The DBM does not state whether the transformer is liquid-filled or dry-type. This affects oil containment, fire separation, and electrical-building location requirements and must be resolved by vendor design and EPC review.
- Grounding/bonding requires the major-electrical-equipment two-point ground-grid connection, and distribution transformers specifically require separate copper ground conductors per CEC sizing.
- Power/control separation rules apply at the 13.8 kV and 600 V terminations even when raceway design is part of EPC scope; the vendor package shall provide interface data that supports the EPC separation strategy.
- Area classification at the transformer location is not stated; the facility general basis is Class I Zone 2 IIA/IIB unless drawings classify otherwise. Vendor selections affecting hazardous-area suitability shall remain `TBD` until the location and classification are confirmed.

Sources: `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, electrical basis sections.

## Trade-offs

| Topic | Trade-off / caution |
|---|---|
| Vendor detail vs. source fidelity | Richer vendor detail would improve usefulness, but unsourced details must remain `TBD` until vendor design is available. |
| Package ownership vs. facility integration | Vendor engineering can define package internals (windings, accessories, controls), but EPC review must preserve facility-level interface consistency and ground-grid integration. |
| 347 V service interpretation | Treating 347 V as a derived line-to-neutral of a 600 V wye is plausible practice, but the accessible source set does not state it. Premature assumption could mis-specify panelboards, neutral bonding, or HRG coordination. |
| Liquid-filled vs. dry-type | Each option carries different foundation, oil-containment, fire-separation, ventilation, and indoor/outdoor placement consequences. Keep open until vendor selection and EPC siting are coordinated. |
| Hazardous-area applicability | Generic Zone 2 assumption could over-specify enclosure ratings or accessories; under-specifying risks non-compliant placement. Defer to classification drawings and EPC siting. |

## Examples

- Example source-grounded requirement: "Vendor design shall accept 13.8 kV, 3 phase, 3 wire, 60 Hz LRG primary supply per facility basis." Source: DBM System Voltages and Incoming Power and Transformers.
- Example source-grounded interface item: "Communications / Network interface applies to PKG-016." Source: Gate 7 `INTERFACE_REGISTER.csv`, PKG-016.
- Example `TBD`: cooling class, BIL, vector group, and tap-changer configuration, because no accessible source slice states them for DEL-016-04.
- Not acceptable without new source: "Transformer is ONAN liquid-filled with Dyn11 vector group, 5.75% impedance, and ±2×2.5% off-load tap changer." The accessible source set does not establish these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-016-04-001 | Package name carries a 600/347 V secondary, but the DBM System Voltages table does not enumerate a 347 V service. The technical meaning (e.g., wye line-to-neutral of 600 V) is not source-established. | Workbook Packages row 18; `PACKAGE_REGISTER.csv` row `PKG-016` | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, System Voltages | Datasheet Attributes (347 V service basis); Specification REQ-016-04-005; Procedure Steps | Treat 600 V as the source-confirmed secondary and carry 347 V as an `ASSUMPTION` (line-to-neutral of a 600 V wye) until vendor data or accepted EPC source confirms the configuration, panelboard scope, and neutral/HRG coordination. | TBD |
| HRR-016-04-002 | Insulating medium (liquid-filled vs. dry-type) and cooling class are not stated by accessible sources, yet they materially drive foundations, oil containment, fire separation, and siting (indoor/outdoor / electrical building). | Gate 7 `PACKAGE_REGISTER.csv` row `PKG-016` (no statement) | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, Electrical Buildings (no transformer-specific text) | Datasheet Attributes/Construction; Specification REQ-016-04-010, REQ-016-04-011; Procedure Steps | Keep insulating medium and cooling class as `TBD`; require the vendor to declare them in the design basis and route the consequence (foundation/containment/siting) through EPC integration review before acceptance. | TBD |
| HRR-016-04-003 | Detailed vendor document, inspection, factory/type/special test, and turnover requirements are expected but not stated in the accessible source slice for DEL-016-04. | Gate 7 `ARTIFACT_REGISTER.csv` (DEL-016-05, DEL-016-06 vendor turnover/acceptance evidence) | DEL-016-04 accessible sources | Specification Documentation; Procedure Records | Keep DEL-016-04 vendor package documentation requirements limited to design basis/datasheet set/physical package and defer detailed test/turnover requirements to DEL-016-05 and DEL-016-06 unless human rules otherwise. | TBD |
