# Guidance: DEL-029-04_vendor-engineered-equipment-package

## Purpose

The Vendor Engineered Equipment Package converts the accepted Gate 7 package basis for `PKG-029` into a vendor-owned production unit comprising engineering, design, fabrication/supply, vendor documentation, and the physical equipment package for Transformer TXP-8600-1 (2.5 MVA, 13.8 kV / 600 / 347 V step-down distribution transformer). It is the vendor counterpart to the EPC-authored Package Datasheet and Scope of Work; the EPC Integrator retains facility integration and interfaces.

## Principles

- Preserve source spelling and identity. The package name, tag, and ratings carry the workbook and Gate 7 register spelling.
- Treat the seven workbook interface `X` facts (Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports) as evidence under this vendor production unit, not as separate deliverables.
- Keep vendor-owned design work with the Package Vendor and facility-level integration with the EPC Integrator.
- Use the DBM electrical basis only at the level it supports: distribution transformer service to 600 V MCCs, secondary high-resistance neutral grounding (5 A continuous), foundations and spacing, cable type (ACWU; no single-conductor) for the secondary feeder, and grounding-grid coordination.
- Mark TBD: facility allocation (04-25 vs 03-25), insulation type, cooling class, impedance, tap-changer arrangement, accessory selection, EHT/auxiliary loads, and control voltage source.

## Considerations

The DBMs describe 13.8 kV→600 V step-down distribution transformers generally and an explicit "13.8 kV to 600V, 3 MVA" transformer for 03-25, but neither DBM names tag TXP-8600-1 or a 2.5 MVA unit; TXP-8600-1's identity and rating come from the workbook row, not from a DBM source slice. Treat workbook-defined identity as authoritative for nameplate and ratings, and DBM electrical basis as authoritative for the connected facility electrical system (600 V LV service, HRG, MCC topology, standby power, cable type, foundations, grounding grid).

347 V is consistent with a 600 V, 3-phase wye system line-to-neutral derivative typically used for lighting; whether TXP-8600-1's secondary is connected to facility lighting circuits, or whether 347 V is carried only as a derived nameplate descriptor, is not stated in accessible source slices and shall be confirmed by vendor data and EPC integration.

Standby power at the 600 V MCC level (LV standby generators with transfer switches) implies that the 600 V bus served by TXP-8600-1 may be paralleled or transferred during outages; transfer scheme, generator count, and load shedding remain `TBD` in both DBMs.

Foundations, secondary containment (if oil-filled), and CEC spacing are EPC integration topics that the vendor package shall be designed to be compatible with, but specific facility values (pad location, containment volumes, ground-well placement) come from EPC integration.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Insulation type (oil-filled vs dry-type) | Mark `TBD` pending vendor selection and EPC area classification ruling. | DBM allows both classes in different contexts; PKG-029 is not assigned. |
| Facility allocation (04-25 vs 03-25) | Mark `TBD`. | The 03-25 DBM lists a 13.8 kV→600 V, 3 MVA unit; 2.5 MVA TXP-8600-1 is not identified in either DBM. |
| 347 V interpretation | Treat as derived line-to-neutral of a 600 V wye secondary; do not infer dedicated 347 V lighting distribution from PKG-029 alone. | Source slices do not allocate a 347 V lighting feeder to TXP-8600-1. |
| Standards | List CEC, project electrical specifications, and likely industry transformer standards as governing bases with locations TBD. | DBM references CEC and project electrical specifications; specific transformer-standard selection is vendor scope. |

## Examples

- Acceptable datasheet entry: "Applicable interfaces: Electrical Power; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Communications / Network; Maintenance Access; Structural / Foundations / Supports. Source: Workbook Packages row 31 and `INTERFACE_REGISTER.csv`."
- Acceptable source-gap entry: "Insulation type: TBD. No package-specific source slice classifies TXP-8600-1 as oil-filled or dry-type."
- Not acceptable without new source: "TXP-8600-1 is the main step-down for the 04-25 Acid Gas Compressor Electrical Building." The accessible source set does not allocate TXP-8600-1 to a specific electrical building.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-029-04-001 | Workbook identifies TXP-8600-1 as a 2.5 MVA 13.8 kV/600/347 V step-down distribution transformer, but neither DBM names this tag nor a 2.5 MVA distribution transformer; the 03-25 DBM lists a 3 MVA 13.8 kV→600 V unit. | Workbook Packages row 31; `PACKAGE_REGISTER.csv` row `PKG-029` | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, "Incoming Power and Transformers"; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers/electrical buildings paragraphs | Datasheet Attributes/Construction; Specification Requirements | Treat workbook identity (tag, rating, voltages) as authoritative for the vendor package; keep DBM rating differences as facility-level coordination items resolved by EPC Integrator. | TBD |
| HRR-029-04-002 | Allocation of TXP-8600-1 to a specific facility (04-25 Deepcut or 03-25 Comp and Liquids) and to a specific electrical building / transformer pad is not stated in accessible source slices. | Workbook Packages row 31 | DBM electrical-building paragraphs in both DBMs | Datasheet Construction (Installation location); Procedure Steps | Do not assert a facility or building allocation in vendor documentation until the EPC Integrator issues an integration ruling. | TBD |
| HRR-029-04-003 | Insulation type (oil-filled vs dry-type), cooling class, impedance, and tap-changer arrangement are not stated in accessible source slices. | DBM transformer paragraphs (oil-filled and LACT dry-type examples) | Workbook Packages row 31 (title only) | Datasheet Attributes/Construction; Specification Requirements; Standards | Carry as vendor-design TBDs; do not infer insulation/cooling from DBM examples for other transformers. | TBD |
