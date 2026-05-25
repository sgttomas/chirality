# Guidance: DEL-029-05_vendor-document-turnover-package

## Purpose

The Vendor Document Turnover Package exists so that the documentation produced by the Package Vendor for `PKG-029` (Transformer TXP-8600-1) is collected, controlled, reviewed by the EPC Integrator, and turned over in a form sufficient for facility integration, construction, commissioning, operation, and maintenance. It is the bridge between vendor-owned package design/equipment (`DEL-029-04`) and EPC-owned vendor package review and acceptance (`DEL-029-06`).

## Principles

- **Vendor owns; EPC reviews.** The Package Vendor authors and controls vendor documentation. The EPC Integrator reviews for interface, integration, and project-document-control compliance. The boundary is preserved in `PACKAGE_REGISTER.csv` and `_CONTEXT.md`.
- **Source-grounded.** Vendor documentation requirements that are confirmed by accessible source material (DBM electrical, transformer foundation, grounding slices) are stated as requirements. Where source material is silent (document classes, submittal stages, turnover record types), entries remain `TBD` or `ASSUMPTION` rather than invented.
- **Interface-complete.** All seven interface facts for `PKG-029` must be represented in vendor documentation; an interface fact without supporting vendor documentation is a turnover gap.
- **Decomposition does not substitute for source.** The decomposition routes the work to the Package Vendor; it does not enumerate vendor documents. Enumeration must come from the project document control procedure or vendor submittal practice, not from decomposition prose.

## Considerations

- The accessible DBM source slice (line 617) lists vendor document registers as one of several mechanical/equipment package deliverables. This anchors the register expectation but does not enumerate package-specific document classes for a step-down distribution transformer.
- The DBM transformer slices (lines 2745, 2949) anchor foundation and oil-filled handling expectations. Vendor documentation for foundation loads, anchorage, and (if applicable) oil containment should be present.
- The DBM grounding slices (lines 2985, 2989, 2991) anchor grounding interface expectations. Vendor documentation must show ground-grid connection points and any required separate copper ground conductor sizing basis.
- The DBM voltage table (line 2937) anchors the 600 V high-resistance grounding context for the secondary side of the transformer.
- `26020-Package_Requirements.docx` is not accessible for `PKG-029`; if it later becomes accessible, it may add or override document-class expectations.
- Objective association is `PACKAGE_HEURISTIC` (best-effort mapping); do not treat the listed objectives as hard requirements without human confirmation.

## Trade-offs

- **Register breadth vs. submittal load.** A broad vendor document register reduces gap risk but increases vendor and EPC review load. The minimum set (certified drawings, nameplate data, FAT reports, O&M, spares) is anchored conservatively; project document control procedure governs expansion.
- **Early submittal vs. certified content.** Early preliminary submittals support EPC integration design but may be superseded; certified-for-fabrication and certified-for-record submittals must be tracked separately in the register.
- **Oil-filled vs. dry-type selection.** Source guidance favors avoiding or limiting containment where practical. The selection trade-off affects vendor documentation scope (containment, oil sampling, fire separation) and is owned by the package design deliverable (`DEL-029-04`); turnover documentation must follow the selected configuration.

## Examples

- TBD. Source material does not provide a worked example of a vendor document register or turnover record set for a 2.5 MVA, 13.8 kV / 600 / 347 V step-down distribution transformer in this project's source set.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CFT-029-05-001 | Decomposition lists "Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records" as anticipated artifacts, but the accessible source set does not enumerate document classes, submittal stages, or turnover record types for `PKG-029`. | `DELIVERABLE_REGISTER.csv` row `DEL-029-05_vendor-document-turnover-package`; `_CONTEXT.md` | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (line 617); `26020-Package_Requirements.docx` (no `PKG-029` match accessible) | Datasheet Attributes/Construction; Specification REQ-029-05-003/-004/-005 | PROPOSAL: treat decomposition entries as scope routing; require Package Vendor to populate the register and submittal/turnover content per project document control procedure; mark specific enumerations `TBD` until that procedure is accessible. | TBD |
| CFT-029-05-002 | The 600 V secondary tap (347 V phase-to-ground) is implied by the package name (600 / 347 V), but the DBM voltage table describes the 600 V system as 3-phase, 3-wire, high-resistance grounded — a system with no continuous neutral. | Package name (Workbook Packages row 31) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`, voltage table (line 2937) | Datasheet Identification; Specification REQ-029-05-007 | PROPOSAL: do not assert 347 V neutral availability for this package in vendor documentation requirements; require the Package Vendor to confirm secondary configuration and grounding in submittals before EPC review. | TBD |

## Notes

- Pass 3 (semantic lensing enrichment) has not been run; `_SEMANTIC_LENSING.md` is not present. Items above are drafted from Pass 1 and reviewed in Pass 2 for cross-document consistency.
