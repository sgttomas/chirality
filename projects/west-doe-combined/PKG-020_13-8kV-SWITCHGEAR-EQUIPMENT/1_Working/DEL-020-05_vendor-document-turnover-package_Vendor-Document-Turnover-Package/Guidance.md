# Guidance: DEL-020-05_vendor-document-turnover-package

## Purpose

This deliverable exists so that the `PKG-020` 13.8kV switchgear vendor documentation — register, submittals, source-required documents, and turnover records — is produced, controlled, and turned over as a single Package Vendor deliverable, with EPC Integrator interface and integration review. It supports the project objectives carried at the package level (`OBJ-001`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-008`, `OBJ-009`, `OBJ-010`) via the package-grouping heuristic (ASSUMPTION).

It is the documentary backbone of the package: it is what the EPC Integrator and the owner ultimately use to accept, install, energize, operate, and maintain the switchgear.

## Principles

- **Single ownership, dual review.** The Package Vendor owns authorship of all vendor documentation; the EPC Integrator reviews for interface and integration suitability. Authorship and review are not the same activity and should not be conflated in the register.
- **Register first, content second.** A complete, current vendor document register is the project-control instrument that lets all downstream activity (review, FAT, shipment, installation, turnover) proceed predictably. If the register is wrong, the documents do not matter.
- **Source carryover, not promotion.** Individual source vendor document rows from `_Sources/26020-Package_Requirements.docx` are carried as artifacts/evidence on this deliverable. They are not promoted into separate deliverables — that is a decomposition decision already taken in Gate 7 (`DELIVERABLE_REGISTER.csv` notes column).
- **Turnover is documentary, not narrative.** Turnover content (FAT, SAT, calibration, as-built) is record-based; this deliverable assembles and controls those records, not the underlying physical work, which is covered by `DEL-020-04`.

## Considerations

- The DBM (`_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md`) is the project-basis source but does not enumerate PKG-020 vendor-documentation content. Substantive content here cannot be derived from DBM prose alone.
- `26020-Package_Requirements.docx` is the most likely project source for a required vendor-document list, but it is not currently available as a parsed slice. Until its PKG-020 slice is resolved, the required submittal list remains an ASSUMPTION.
- The package interface set (Electrical Power, Grounding/Bonding, I&C/Control Cabling, Communications/Network, Maintenance Access, Structural/Foundations/Supports) is authoritative from `INTERFACE_REGISTER.csv`. The vendor documentation must demonstrably support each of these interfaces.
- This deliverable depends on the EPC-side anchor deliverables (`DEL-020-01` SoW and `DEL-020-02` Package Datasheet) to define what submittals are required. Drafting vendor-document requirements ahead of those anchors is speculative.
- `DEL-020-06_epc-vendor-package-review-and-acceptance` is the downstream consumer of this turnover set. Submittal content should be shaped by what `DEL-020-06` needs to clear its acceptance checklist.

## Trade-offs

- **Breadth vs. burden.** A maximalist submittal list creates a heavy vendor burden and large review effort; a minimalist list creates integration risk. The PKG-020 submittal list should be set by `26020-Package_Requirements.docx` plus EPC review, not by either extreme.
- **Document-control rigor vs. transmittal speed.** Strict numbering and transmittal control supports auditability but slows iteration during early design; a lighter control regime accelerates iteration but creates traceability risk at turnover. The trade-off should be made explicitly by the project document-control procedure (TBD).
- **Vendor-native formats vs. project-standard formats.** Vendor standard formats (drawings, BOMs, FAT report templates) carry vendor warranty significance; reformatting them risks losing that. Project-standard formats ease aggregation. Default to vendor-native unless the project document-control procedure requires otherwise.

## Examples

No PKG-020-specific examples are available from the accessible source slices. Examples (e.g., a sample vendor document register row, a sample turnover index) should be added once a vendor-issued register or a project document-control template is resolved.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| CONF-020-05-01 | The required vendor-document submittal list for PKG-020 is asserted only as ASSUMPTION in this deliverable; the authoritative source `26020-Package_Requirements.docx` exists but has not been parsed/accessible in this run. | `_Sources/26020-Package_Requirements.docx` (location TBD; not accessible) | `Specification.md` REQ-020-05-02, REQ-020-05-03 | Datasheet attributes "Vendor document register", "Vendor submittal set"; Specification REQ-020-05-02, REQ-020-05-03; Procedure steps 2, 3 | Treat `26020-Package_Requirements.docx` PKG-020 slice as authoritative once parsed; demote ASSUMPTION text to TBD pending that slice. | TBD |
| CONF-020-05-02 | Turnover record content is asserted only as ASSUMPTION here; no PKG-020-specific source slice currently defines required FAT/SAT/calibration/as-built content. | Source gap (no PKG-020 slice) | `Specification.md` REQ-020-05-04 | Datasheet "Turnover record set"; Specification REQ-020-05-04; Procedure steps 4, 5 | Defer to the project quality-assurance standards and the vendor's standard turnover package; capture acceptance content via `DEL-020-06`. | TBD |
| CONF-020-05-03 | Project document-control procedure is referenced as governing numbering, transmittal, and revision control but is not present in the accessible source slice. | Source gap (no project document-control procedure slice) | `Specification.md` REQ-020-05-06; `Datasheet.md` "Document control / numbering" | Datasheet Construction "Document numbering and revision control"; Specification REQ-020-05-06; Procedure step 6 | Treat the project document-control procedure as authoritative once located; mark current text as ASSUMPTION pending that source. | TBD |
| CONF-020-05-04 | Objective associations (`OBJ-001`, `OBJ-004`–`OBJ-006`, `OBJ-008`–`OBJ-010`) are carried via the package-grouping heuristic, not an explicit deliverable-level objective mapping. | `_CONTEXT.md` Supports Objectives | `OBJECTIVE_DELIVERABLE_MAP.csv` (package-grouping) | Guidance "Purpose" | Treat objective associations as ASSUMPTION (best-effort mapping) unless human confirms a deliverable-level mapping. | TBD |
