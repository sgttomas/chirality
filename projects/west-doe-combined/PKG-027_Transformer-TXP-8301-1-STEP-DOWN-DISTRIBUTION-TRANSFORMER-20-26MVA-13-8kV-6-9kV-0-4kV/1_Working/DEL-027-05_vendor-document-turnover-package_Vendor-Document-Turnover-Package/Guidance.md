# Guidance: DEL-027-05_vendor-document-turnover-package

## Purpose

This guidance explains how to draft, review, and close out the Vendor Document Turnover Package for `PKG-027` (Transformer TXP-8301-1, 20/26 MVA, 13.8 kV / 6.9 kV / 0.4 kV) without overstating what the current source set actually supports. The deliverable exists so that the Package Vendor can hand over a coherent, auditable documentation set that the EPC Integrator can review for facility integration and that the project can retain as turnover evidence.

## Principles

- **Vendor authorship, EPC review.** The Package Vendor owns the documentation. The EPC Integrator's role here is interface/integration review, not authorship.
- **Source fidelity over completeness theater.** Where the source set is silent on vendor-document content (`ARTIFACT_REGISTER.csv` row `ART-AACDC8D0FF` records this gap), keep items `TBD` rather than inventing requirements.
- **Interface facts are first-class.** The seven `PKG-027` interface facts in `INTERFACE_REGISTER.csv` are the spine of the documentation register; each interface should be traceable to at least one vendor document.
- **Electrical design basis anchors content where available.** The DBM electrical section provides grounding, neutral grounding, foundation, and distribution conventions that vendor documentation must remain consistent with even when package-specific source detail is absent.
- **Turnover is evidence, not paperwork.** Turnover records should support post-installation operations, maintenance, testing, and warranty enforcement, not just contractual closeout.

## Considerations

- The package title gives the transformer rating (20/26 MVA) and three voltages (13.8 kV / 6.9 kV / 0.4 kV). The DBM indicates 6.9 kV windings are grounded via 100 A neutral grounding resistors operating as tripping systems; vendor documentation should reflect this. The 0.4 kV (400 V) winding does not match the DBM 600 V / 208/120 V LV bases; the role of the 0.4 kV winding (e.g., dedicated load, auxiliary) is not resolved by available source slices.
- The artifact register row `ART-AACDC8D0FF` is an explicit source-gap marker. Treat it as the central guidance signal: detailed vendor-document requirements are not in current source material and must be defined by vendor scope and EPC review.
- Vendor-document conventions (numbering, status codes, return codes, revision control) are typically project-EPC conventions. The accessible source set does not specify them for this project, so they are `TBD` unless the project document control standard is provided.
- Foundation / installation documentation should be consistent with the DBM statement that transformers are generally supported on precast concrete bearing foundations and installed on structural steel transformer bases.

## Trade-offs

- **Breadth vs. source-grounding.** A complete-looking submittal index could be drafted from generic transformer-project convention, but that would overstate source authority. Choose source-grounding plus explicit `TBD`s.
- **Vendor-driven vs. EPC-driven register.** If the vendor proposes the register first, the project gets vendor-native completeness but may miss EPC interface requirements; if EPC drives it first, integration coverage is strong but vendor-specific items may be missed. The default is vendor-led, EPC-reviewed.
- **Early register vs. mature submittals.** Issuing a register before vendor selection is unavoidable for planning but the register must be marked provisional until vendor scope is fixed.

## Examples

Examples of source-grounded vendor documentation entries that can be anchored today:

- A grounding-and-bonding evidence document referencing the DBM two-point ground-grid connection and ground-well-at-power-transformer requirements.
- A neutral grounding configuration document for the 6.9 kV winding reflecting the 100 A, 10 s resistor / tripping configuration (ASSUMPTION: applies to the 6.9 kV winding; confirm by detailed design).
- A foundation/installation document referencing the DBM precast concrete bearing foundation convention and CEC spacing review for oil-filled transformers.

Examples of items that are `TBD` and should not be invented:

- Specific factory test list and acceptance values for TXP-8301-1.
- Oil quality, dielectric, and DGA acceptance values for this unit.
- Vendor document numbering and return-code workflow.
- Spare parts list and warranty terms.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-027-05-001 | Package title states three voltages 13.8 kV / 6.9 kV / 0.4 kV (suggesting a three-winding step-down distribution transformer), but accessible source slices do not confirm the winding configuration, vector group, tap arrangement, MVA assignment per winding (20 vs. 26), or cooling class basis for TXP-8301-1. | Package title in Workbook Packages row 29 / `PACKAGE_REGISTER.csv` row `PKG-027` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` electrical section (no PKG-027-specific slice) | Datasheet Identification/Attributes; Specification REQ-027-05-001; Procedure prerequisites | Treat package title as identity only; carry winding configuration, MVA-per-winding, cooling, vector group, and tap arrangement as `TBD` until vendor data or a detailed electrical source is accepted. | TBD |
| HRR-027-05-002 | The 0.4 kV (400 V) winding voltage does not match the DBM low-voltage bases (600 V; 208/120 V; 125 VDC); the role of the 0.4 kV winding and which loads it serves are not resolved by accessible source slices. | Package title in Workbook Packages row 29 | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage table and electrical buildings | Datasheet Attributes/Conditions; Specification REQ-027-05-003, REQ-027-05-005 | Carry 0.4 kV-winding load assignment, downstream switchgear/MCC, grounding configuration, and feeder destination as `TBD`; do not infer LV system architecture from the package title alone. | TBD |
| HRR-027-05-003 | Artifact register row `ART-AACDC8D0FF` records that detailed vendor-document requirements are not present in current source material for `PKG-027`; no accessible source slice defines required vendor documents, register schema, submittal workflow, or turnover-record content for this package. | `ARTIFACT_REGISTER.csv` row `ART-AACDC8D0FF` | `_REFERENCES.md` (no deliverable-specific source slices copied) | Datasheet Attributes (vendor document register, submittal list, source-required documentation, turnover records); Specification REQ-027-05-007, REQ-027-05-008 | Treat vendor-document register, submittal list, and turnover content as `TBD` pending vendor scope and EPC document-control standard; do not invent a register schema from generic convention. | TBD |
