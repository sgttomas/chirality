# Guidance: DEL-028-01 Scope of Work

## Purpose

This Scope of Work exists to give the EPC Integrator a bounded, source-traceable package integration basis for PKG-028 (`Transformer TXP-8801-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 7.5MVA 13.8kV/4160/2400V`) before the downstream package datasheet, construction work package, vendor package production, vendor document turnover, and EPC acceptance work proceed.

The source basis is intentionally narrow. Workbook row 30 establishes the package identity and interface flags; Gate 7 establishes the mandatory EPC anchor deliverable role and the Package Vendor / EPC Integrator responsibility split; the DBM Deepcut electrical section provides facility-level 13.8 kV distribution and grounding context. Package-specific transformer design details remain `TBD` unless later source material provides them.

## Principles

- Preserve the source-derived package name and equipment tag (`TXP-8801-1`, `7.5MVA 13.8kV/4160/2400V`) for identity traceability.
- Treat the Scope of Work as an EPC integration document, not a vendor design document.
- Keep Package Vendor responsibilities separate from EPC Integrator responsibilities.
- Include only source-supported package interfaces (the seven listed in the Gate 7 interface register for PKG-028).
- Use the DBM Deepcut electrical content as facility context only; do not infer transformer nameplate, impedance, vector group, taps, cooling, insulation, BIL, fluid, accessories, or secondary configuration from it.
- Prefer `TBD` over inferred technical values where accessible sources do not provide package-specific detail.

## Considerations

The package title carries a clear equipment tag and a rating string (`7.5 MVA`, primary `13.8 kV`, secondaries `4160 V` and `2400 V`), and the DBM establishes that the facility 13.8 kV switchgear feeds step-down transformers radially to electrical buildings and loads across the facility. This supports describing PKG-028 as one of the facility's 13.8 kV-fed step-down distribution transformers. It does not support declaring which downstream loads the transformer serves, whether `4160 V` and `2400 V` are two separate secondary windings or a sectionalized arrangement, or any vendor-specific parameter.

The workbook and Gate 7 interface basis flags seven interfaces for this package: Electrical Power, Grounding / Bonding, Area / Exterior Lighting, I&C / Control Cabling, Communications / Network, Maintenance Access, and Structural / Foundations / Supports. These should drive the SOW boundary narrative and later construction coordination. They should not be expanded to additional interface categories unless later accepted sources add them.

## Trade-offs

| Topic | Conservative treatment | Risk if overstated |
|---|---|---|
| Package function | Describe as a 13.8 kV-fed step-down distribution transformer with `4160 V` and `2400 V` secondary voltages serving facility distribution; mark load assignment and secondary configuration `TBD`. | The SOW could incorrectly allocate loads or define vendor scope before vendor data is available. |
| EPC responsibility | State facility integration, interfaces, tie-ins, constructability, procurement/construction coordination, and acceptance review. | EPC scope could accidentally absorb vendor package engineering/design obligations. |
| Technical values | Use only source-supported values and `TBD` elsewhere. | Unsupported values could propagate into datasheets, procurement, or construction packages. |
| Identity strings | Preserve `TXP-8801-1` and the full source-derived rating string. | Editing the identity string could break register traceability or appear to alter accepted upstream truth. |
| Standards citation | Cite CSA C22.1/CEC only where DBM supports it (spacing, grounding sizing); leave clause-level requirements TBD. | Naming clauses without source access could create unverifiable requirements downstream. |

## Examples

- Acceptable SOW language: "PKG-028 is the workbook-defined Electrical package `Transformer TXP-8801-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 7.5MVA 13.8kV/4160/2400V`, WBS 01, tracking number `26020-01-30-019`; the Package Vendor owns package engineering/design/equipment and the EPC Integrator owns facility integration and interface coordination."
- Acceptable SOW language: "The transformer is fed from the facility 13.8 kV switchgear consistent with the DBM Deepcut electrical distribution basis; downstream load assignment and the precise 4160 V / 2400 V secondary configuration are TBD pending detailed electrical design and vendor data."
- Avoid: "The EPC Integrator shall design transformer TXP-8801-1." Gate 7 assigns package engineering and design to the Package Vendor.
- Avoid: "Transformer impedance shall be [x] %." No accessible source slice supports that value.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling |
|---|---|---|---|---|---|---|
| HR-028-01 | Package name carries the rating string `7.5MVA 13.8kV/4160/2400V` as identity, but accessible sources do not confirm whether `4160 V` and `2400 V` are dual secondary windings, a tertiary winding, or a sectionalized configuration. | Workbook Packages row 30; Gate 7 `PACKAGE_REGISTER.csv` row PKG-028 (identity only). | DBM Deepcut Electrical (4-25_Deepcut_DBM.md) describes facility 13.8 kV distribution but does not name TXP-8801-1 or its secondary configuration. | Datasheet Conditions/Construction; Specification Requirements; Procedure Steps. | Carry the rating string as identity only; mark secondary configuration `TBD` pending vendor or detailed electrical source. | TBD |
| HR-028-02 | Package-specific transformer design values (impedance, vector group, taps, cooling class, insulation/BIL, fluid, accessories, weights, support loads) are not exposed in accessible sources. | Workbook row 30 gives identity and interface flags only. | DBM Deepcut electrical gives facility distribution and generic transformer foundation/grounding basis. | Datasheet Conditions/Construction; Specification Requirements; Procedure Steps. | Treat DBM as facility context; keep package-specific technical values `TBD` pending vendor/source data. | TBD |
| HR-028-03 | Facility load assignment for TXP-8801-1 (which electrical building/MCC/lineup it feeds) is not stated in accessible sources. | DBM Deepcut Electrical (lines 2917-2937) describes radial step-down distribution generically. | No vendor or detailed electrical document is currently in scope. | Datasheet Conditions; Specification Scope; Procedure Steps. | Do not assign loads; carry assignment as `TBD` pending detailed electrical design. | TBD |
