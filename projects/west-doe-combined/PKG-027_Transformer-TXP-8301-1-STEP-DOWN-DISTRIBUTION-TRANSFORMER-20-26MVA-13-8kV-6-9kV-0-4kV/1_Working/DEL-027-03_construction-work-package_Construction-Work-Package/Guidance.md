# Guidance: DEL-027-03_construction-work-package

## Purpose

The Construction Work Package exists to convert the accepted Gate 7 package basis for `PKG-027` into a source-supported construction execution document. It should let the EPC Integrator and field construction team plan, install, inspect, tie in, and turn over the TXP-8301-1 step-down distribution transformer while keeping Package Vendor design responsibility distinct from EPC-owned facility integration.

## Principles

- Preserve source spelling and identity. The package name is carried as "Transformer TXP-8301-1 - STEP DOWN DISTRIBUTION TRANSFORMER - 20/26MVA 13.8kV/6.9kV/0.4kV" because that is the workbook and Gate 7 register spelling.
- Treat workbook interface `X` facts as construction execution constraints, not as separate deliverables.
- Keep vendor-owned design/fabrication/vendor commissioning with the Package Vendor and field installation, tie-in, and facility-level integration with the EPC Integrator.
- Use `TBD` for rigging, oil-handling, FAT/SAT/commissioning protocol, foundation footing, termination drawings, and physical location until vendor data and detailed engineering are accepted.
- Use DBM electrical/foundations basis only at the level it supports: transformer foundation type, spacing, grounding architecture, NGR scheme, electrical-building housing possibilities, cable tray and conduit routing, and maintenance-access constraints.

## Considerations

The DBM electrical design basis describes a facility power-system architecture in which 13.8 kV switchgear distributes power radially through step-down transformers to lower-voltage buses. TXP-8301-1 (13.8 kV primary; 6.9 kV and 0.4 kV secondaries) is consistent with this architecture by voltage class, so construction work package planning should assume coordination with the 13.8 kV switchgear and downstream 6.9 kV and 0.4 kV distribution. However, the source does not name TXP-8301-1 specifically, so this association is recorded as ASSUMPTION.

DBM foundation guidance is generic: large oil-filled transformers are generally installed on structural steel transformer bases or precast concrete bearing foundations; secondary containment shall be reviewed and selection shall avoid or limit containment where practical. Whether TXP-8301-1 is oil-filled or dry-type is `TBD` from accessible sources, so construction work package content should remain neutral on construction-of-the-unit details.

Grounding considerations are well supported by DBM: two-point connection to the ground grid, ground wells at power transformers, and the 6.9 kV NGR scheme (100 A, 10 s, tripping). The 6.9 kV winding of TXP-8301-1 likely requires this NGR scheme, but applicability shall be confirmed in detailed engineering.

Maintenance access is both a workbook interface fact and a DBM routing constraint. Construction planning should preserve transformer pull/replacement clearance, fencing and gate access for crane lifts, and cable tray and conduit routing that does not interfere with maintenance.

The package-specific Word requirements source did not produce a PKG-027 match during this run; therefore, construction work package content should remain conservative until missing detailed requirements are resolved by vendor data, detailed engineering, or human ruling.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Oil-filled vs. dry-type construction | Mark construction-of-the-unit as `TBD`; plan civil/electrical for either case using DBM generic guidance. | Accessible sources do not confirm transformer construction type for TXP-8301-1. |
| Foundation type | Plan for structural steel transformer base or precast concrete bearing foundation per detailed design; do not specify footing geometry. | DBM gives generic foundation concepts; specific footing design is civil/structural detailed engineering scope. |
| 6.9 kV NGR scheme | Carry the 100 A, 10 s tripping NGR as a planning assumption; confirm against detailed protection design. | DBM applies this scheme to "each 6.9 kV transformer" but TXP-8301-1 specifics need confirmation. |
| Physical location | Identify as possible electrical-building / outdoor pad context, not a confirmed location. | DBM allows multiple configurations but does not locate TXP-8301-1. |
| FAT/SAT/commissioning | Plan to follow project electrical commissioning standard and vendor protocol; do not invent acceptance criteria. | No package-specific protocol available in accessible sources. |

## Examples

- Acceptable construction work package entry: "Construction shall install two-point grounding from TXP-8301-1 to the facility ground grid and provide a ground well at the transformer. Source: `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraphs."
- Acceptable source-gap entry: "Rigging plan and lift weight: TBD. Vendor weight data and approved rigging procedure required before lift."
- Not acceptable without new source: "TXP-8301-1 is an ONAN/ONAF oil-filled transformer mounted on a 6.5 m × 4.5 m concrete pad with 110% bunded containment." The accessible source set does not establish these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-027-03-001 | TXP-8301-1 construction-of-the-unit (oil-filled vs. dry-type) is not declared in accessible sources, while DBM describes both oil-filled and dry-type practices for the facility. | Workbook Packages row 29; `PACKAGE_REGISTER.csv` row `PKG-027` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, transformers paragraph (oil-filled), LACT dry-type paragraph | Datasheet Attributes/Construction; Specification REQ-027-03-004; Procedure Steps | Carry construction type as `TBD`; design construction scope to accommodate either case using DBM generic guidance until vendor data accepted. | TBD |
| HRR-027-03-002 | DBM applies the 100 A, 10 s tripping NGR scheme to "each 6.9 kV transformer." Whether TXP-8301-1's 6.9 kV winding falls under this scheme as installed is not confirmed in accessible sources. | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, grounding paragraph (6.9 kV transformer NGR) | Workbook Packages row 29; `INTERFACE_REGISTER.csv` `IFC-868150D715` | Datasheet Conditions (Grounding); Specification REQ-027-03-005; Procedure verification steps | Plan grounding installation assuming the 100 A, 10 s NGR tripping scheme; confirm against detailed electrical protection design and vendor coordination before energization. | TBD |
| HRR-027-03-003 | Package-specific construction details for TXP-8301-1 (rigging, lift, oil handling, FAT/SAT, termination drawings, foundation footing, physical location) are absent from accessible sources, including `26020-Package_Requirements.docx` which yielded no PKG-027 match during this run. | `_REFERENCES.md`; `26020-Package_Requirements.docx` search result | Workbook Packages row 29; Gate 7 `PACKAGE_REGISTER.csv` row `PKG-027` | Datasheet Construction; Specification REQ-027-03-009; Procedure Steps | Carry all package-specific construction details as `TBD` in the construction work package; require vendor data and detailed engineering inputs before construction release. | TBD |
