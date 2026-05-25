# Guidance: DEL-030-01 Scope of Work

## Purpose

This deliverable exists as the mandatory Gate 5 EPC anchor Scope of Work for PKG-030 (the 2.5 MVA 13.8 kV / 600 V step-down distribution transformer package `TXP-8200-1`). It establishes a source-grounded, integration-focused scope description that downstream production units consume: the Package Datasheet (`DEL-030-02`), the Construction Work Package (`DEL-030-03`), the Vendor Engineered Equipment Package (`DEL-030-04`), the Vendor Document Turnover Package (`DEL-030-05`), and the EPC Vendor Package Review and Acceptance (`DEL-030-06`).

## Principles

- **Identity is workbook-authoritative.** The package identity, WBS, tracking number, discipline, and interface flag set are taken from workbook Packages row 32 and Gate 7 `PACKAGE_REGISTER.csv` row PKG-030. The Scope of Work shall not rename, renumber, or reclassify the package.
- **Responsibility split is Gate-7 authoritative.** The Package Vendor owns engineering, design, vendor documentation, and physical equipment package supply. The EPC Integrator owns facility integration, interfaces, tie-ins, constructability, procurement / construction coordination, and facility-level integration. The Scope of Work does not absorb vendor scope.
- **Facility context is DBM-authoritative; package design values are vendor-authoritative.** The DBM Deepcut document establishes facility-level utility supply, 13.8 kV distribution, transformer installation basis, and 600 V grounding. Package-internal design values (impedance, BIL, vector group, taps, insulation type, cooling, enclosure, etc.) are not stated in accessible sources and remain `TBD` until vendor / detailed engineering selection.
- **No silent reconciliation.** Apparent discrepancies between workbook-stated package identity (e.g., "600/347V" secondary nomenclature) and DBM-stated facility services (600 V, 3 phase, 3 wire) are carried as human-ruling items, not normalized.

## Considerations

- The DBM lists radial step-down distribution from 13.8 kV switchgear to several electrical buildings, including three 600 V electrical buildings (Acid Gas Compressor EB, Sales / Overheads Compressor EB, General Area / Tank Farm / Process EB). The specific destination for `TXP-8200-1` is not stated in accessible sources. Treat the destination-EB as `TBD-which-EB`.
- The DBM 600 V system is high-resistance grounded with a 5 A continuous resistor at each 600 V transformer neutral. This is a facility-level constraint and must be preserved in the Scope of Work's secondary-side grounding basis even though the transformer's vector group itself is `TBD`.
- The DBM treats large oil-filled transformers as a CEC-spacing and secondary-containment item; insulation type (oil vs dry) for `TXP-8200-1` is not stated in accessible sources, so containment / spacing applicability is conditional.
- The package interface set in Gate 7 includes Area / Exterior Lighting; that flag is preserved as a workbook-derived interface category even though the source does not give transformer-specific lighting requirements.

## Trade-offs

- Source-grounded conservatism leaves many design attributes as `TBD`. This is intentional under the four-documents skill (source fidelity > completeness). Downstream Package Datasheet work (`DEL-030-02`) is the correct place to resolve these once vendor or detailed-engineering data is available.
- Preserving the workbook-stated "600/347 V" secondary nomenclature avoids loss of source provenance; reconciling it against DBM 600 V 3-wire wording is left to human ruling because either resolution (4-wire secondary on this transformer, or workbook nomenclature simplification) materially affects downstream design.

## Examples

Accessible sources support statements such as:

- "The 2.5 MVA 13.8 kV / 600 V step-down distribution transformer `TXP-8200-1` is part of the radial step-down distribution from the plant 13.8 kV switchgear to a 600 V electrical building on the Deepcut facility." (Source: DBM Deepcut Electrical System; System Voltages; Transformers sections.)
- "The transformer secondary serves the facility 600 V system, which is high-resistance grounded with a 5 A continuous resistor at each 600 V transformer neutral." (Source: DBM Deepcut System Voltages and Grounding and Bonding sections.)

Accessible sources do not support statements such as a specific impedance, BIL, vector group, primary / secondary tap range, enclosure type, dimensions, or area classification for `TXP-8200-1`; such values shall remain `TBD`.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HR-030-01-01 | Specific 600 V electrical building destination for the secondary feed of `TXP-8200-1` is not stated in accessible sources; DBM lists three candidate 600 V EBs. | DBM Deepcut Electrical System section (13.8 kV switchgear distribution list) | Workbook Packages row 32 (package identity only) | Datasheet Conditions (Application); Specification SOW-030-08; Guidance Considerations | Carry as `TBD-which-EB` until package or facility one-line confirms destination | TBD |
| HR-030-01-02 | Package name secondary nomenclature is "600/347 V" implying 4-wire / 347 V phase-to-neutral, while DBM 600 V facility services are stated as 600 V, 3 phase, 3 wire (high-resistance grounded). | Workbook Packages row 32 / package name | DBM Deepcut System Voltages table (600 V row) | Datasheet Attributes (Secondary voltage; Secondary grounding); Specification SOW-030-12 | Preserve workbook package name verbatim; do not derive a secondary winding configuration; defer winding configuration / secondary system definition to vendor / facility engineering | TBD |
| HR-030-01-03 | Workbook PKG-030 (WBS 01, 2.5 MVA) and workbook PKG-016 (WBS 02, 3 MVA) share the equipment tag `TXP-8200-1`. It is not stated in accessible sources whether these are two physical transformers, two ratings for one physical transformer, or a workbook tag-reuse artifact. | Workbook Packages row 32 (PKG-030) | Workbook Packages row 18 (PKG-016) | Datasheet Identification / Attributes; Specification SOW-030-01 | Treat PKG-030 and PKG-016 as distinct workbook packages per Gate 7 register; surface the shared tag as a tagging anomaly for project-level ruling | TBD |
