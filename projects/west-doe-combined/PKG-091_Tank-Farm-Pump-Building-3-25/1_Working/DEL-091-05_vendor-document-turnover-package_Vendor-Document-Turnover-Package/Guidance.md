# Guidance — DEL-091-05 Vendor Document Turnover Package

## Purpose

This deliverable consolidates vendor-produced documentation for the PKG-091 Tank Farm Pump Building 3-25 package into a single controlled turnover set so the EPC Integrator and downstream facility operations have one authoritative document basis per vendor package.

Why a single turnover deliverable rather than per-document deliverables: PROJECT_DECOMP DEC-004 and DEC-012 explicitly group source-table vendor document rows as artifacts under a package-level vendor document turnover deliverable, both to preserve workbook-row authority and to keep deliverable granularity at the responsibility-unit level (vendor package vs. EPC integration unit). (Source: GATE-07 PROJECT_DECOMP.md.)

## Principles

- **Vendor authorship, EPC review.** The Package Vendor authors and controls the documents; the EPC Integrator reviews interfaces and integrates the package into the facility. Vendor design responsibility is not transferred to the EPC. (Source: SOW-0185; PROJECT_DECOMP DEC-006.)
- **Workbook + source table as authority.** The workbook package row and the `26020-Package_Requirements.docx` package heading 44 Vendor Engineering Deliverables table are the authoritative basis for *what* documents are required. The snapshot ARTIFACT_REGISTER is the current derivative enumeration. (Source: PROJECT_DECOMP authority statement.)
- **No row-splitting.** Individual vendor document rows are never escalated to standalone deliverables; they remain artifacts under this one turnover deliverable. (Source: PROJECT_DECOMP DEC-004.)
- **Category coherence.** Documents are organized by source vendor-document category (Core vendor documents, Core package engineering, Rotating equipment/pumps, and the additional categories present in the source table) so reviewers can audit completeness category-by-category.
- **Turnover supports operability/maintainability.** OBJ-010 binds vendor documentation, commissioning, turnover, and open-item closure together; the turnover binder is the principal evidence vehicle for that closure. (Source: GATE-07 OBJECTIVE_REGISTER.csv, OBJ-010 text in PROJECT_DECOMP.md.)

## Considerations

- **Source-table accessibility.** The DOCX source for package heading 44 was not locally readable as text in the run that initialized these documents. The GATE-07 ARTIFACT_REGISTER (114 DEL-091-05 rows) is the strongest derivative; required/optional flags and exact source row text are `location TBD` until the source slice is reread.
- **Category completeness.** The accessible artifact rows clearly populate Core vendor documents, Core package engineering, and Rotating equipment/pumps categories. Additional categories appear as `Vendor Documentation Category Evidence` rows; the full per-category enumeration should be confirmed against the source table before acceptance.
- **Interface boundary.** Documents covering scope `by others` (DCS integration, foundations, electrical supply to MCC per SOW-0188) are outside the vendor's documentation set; do not require the vendor to author documents for those areas.
- **Cold-climate provisions.** SOW-0187/0188 imply -40 C start-up conditions and winterization concerns; vendor documents for motors, lube/seal systems, and IOM should reflect those conditions, but explicit document-level winterization requirements are `TBD` (location TBD).

## Trade-offs

- **Single binder vs. per-discipline binders.** Bundling all vendor categories into a single turnover deliverable simplifies handover and aligns with the decomposition decision; the trade-off is binder size and the need for clear category indexing.
- **Document timing.** Some documents (e.g., FAT Report, Inspection Release Certificate, Final Vendor Data Book) are necessarily produced late in the vendor workflow; the register and control procedure must support staged submittals while still gating release on the late-stage records.
- **Required vs. optional documents.** Until the source slice is reread, treating every snapshot artifact row as required is the safe default; later refinement may downgrade specific rows to optional based on the source table. (Recorded as a near-term reread target.)

## Examples

- The Vendor Document Index (PRQ-009) lists every controlled document for the package; the Vendor Document Control Procedure (DOC-008) defines revision control and transmittal flow for those documents.
- The Manufacturing Record Book / Vendor Data Book (QLT-021) bundles MTRs, ITP records, NDE records, and inspection releases for shop quality evidence; the Final Vendor Data Book (PRQ-016) and Mechanical Final Data Book (MEC-023) consolidate the as-supplied document set at turnover.
- Pump Data Sheets (MEC-007) and Rotating Equipment Specifications (MEC-004) reflect the SOW-0187 pump list — vertical inline centrifugal with API-682 Plan 14/52 seal plans for the condensate services and pneumatic diaphragm services per Graco/Hydracell selections.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| — | None identified at initialization. The DOCX heading 44 source slice was not locally readable as text in this run, so latent conflicts between the source vendor-document table and the snapshot ARTIFACT_REGISTER cannot yet be surfaced. | — | — | Spec R-091-05-03/04/05/07 and Datasheet Construction table | Reread `_Sources/26020-Package_Requirements.docx` heading 44 in a follow-up pass and surface any discrepancies here. | TBD |
