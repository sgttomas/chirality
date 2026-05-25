# Guidance: DEL-014-05_vendor-document-turnover-package

## Purpose

The Vendor Document Turnover Package exists so that the EPC Integrator and the operating facility receive a complete, controlled record of the `PKG-014` vendor package: what was engineered, what was delivered, how it is configured, how it is to be operated and maintained, and what evidence supports acceptance. Without this deliverable, the package cannot be integrated, accepted, or operated against its source basis. The deliverable is owned by the Package Vendor with EPC Integrator interface/integration review.

## Principles

- **Single ownership, dual review.** Vendor produces; EPC reviews. Reviewer and producer roles are not blended.
- **Source-required first.** Where the source basis (e.g., `26020-Package_Requirements.docx`) calls for a specific vendor document, that document is required, not optional.
- **Artifacts, not deliverables.** Individual source document rows are evidence/artifacts within this deliverable; they are not promoted to sibling deliverables.
- **Interface-anchored evidence.** Every declared `PKG-014` interface in `INTERFACE_REGISTER.csv` should be traceable to at least one vendor submittal.
- **Register before content.** The register is the controlling artifact; submittals plug into the register, not the other way around.
- **Conservative TBD over invention.** When source basis is unavailable (turnover record types, document-control field set, code/standard clauses), mark TBD and surface the gap rather than fabricate convention.

## Considerations

- The accessible DBM source slice (mechanical-packages paragraph) generalizes vendor document registers as a package-deliverable expectation; PKG-014 is an Electrical package. Treat the generalization as ASSUMPTION (best-effort mapping) until either the project document control standard or the package-specific source slice confirms.
- The package-specific slice of `_Sources/26020-Package_Requirements.docx` was not extracted during PREPARATION; once extracted it likely refines R-2, R-4, and R-5 in the Specification.
- The boundary between `DEL-014-05` (vendor documentation + turnover) and `DEL-014-06` (EPC review/acceptance evidence) is intentional: vendor produces and submits here; EPC's review log and acceptance evidence live in `DEL-014-06`.
- The boundary between `DEL-014-05` and `DEL-014-04` (Vendor Engineered Equipment Package) is similarly intentional: equipment engineering/design lives in `DEL-014-04`; this deliverable is the documentation envelope.

## Trade-offs

- **Granular register vs. lightweight register.** A granular register (revision-by-revision rows, status codes, transmittal IDs) supports rigorous turnover and audit but is heavier to maintain. A lightweight register reduces overhead but increases risk of dropped submittals. The project document control standard, when confirmed, governs this trade-off.
- **Holding submittals until complete vs. progressive turnover.** Holding allows clean, batched acceptance but delays facility readiness; progressive turnover keeps the EPC unblocked but increases coordination cost. Choice is TBD pending schedule basis.
- **Vendor-native document numbering vs. EPC numbering overlay.** Vendor-native preserves vendor traceability and is faster; EPC overlay improves facility-side findability but adds renumbering work.

## Examples

No source-grounded examples are available for `PKG-014` at this draft. When the `26020-Package_Requirements.docx` package-specific slice is extracted, examples should be added (e.g., specific required vendor document IDs, required turnover record types).

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-014-05-001 | Vendor document register expectation is stated in the DBM mechanical-packages paragraph; PKG-014 is an Electrical package. Whether the same package-deliverable expectation applies verbatim, applies with electrical-package adjustments, or is overridden by a different electrical-section package-deliverable rule is not resolvable from accessible source slices. | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md`, line 617 (mechanical packages paragraph) | DBM electrical sections (no equivalent paragraph located in accessible slices) | Datasheet Attributes; Specification R-1, R-2 | PROPOSAL: treat the mechanical-packages expectation as applicable to PKG-014 as ASSUMPTION (best-effort mapping); confirm or adjust once the electrical-section package-deliverable rule is located. | TBD |
| HRR-014-05-002 | The specific list of source-required vendor documents and turnover record types for low-voltage contactor panels is not available in accessible references. `_Sources/26020-Package_Requirements.docx` is named as the likely authority but is not slice-extracted. | `_REFERENCES.md` (`Missing/Deferred References`) | `_Sources/26020-Package_Requirements.docx` (unextracted) | Datasheet Attributes; Specification R-4, R-5; Procedure Steps | PROPOSAL: keep R-4 and R-5 as TBD; do not invent a list; dispatch a source-slicing task for the `PKG-014` portion of `26020-Package_Requirements.docx`. | TBD |
| HRR-014-05-003 | Submittal mechanics (status codes, numbering, review-cycle days), document-control field set, and turnover acceptance criteria are not located in accessible references. No project document control or turnover standard appears in `_REFERENCES.md`. | `_REFERENCES.md` (no document control or turnover standard listed) | None available | Specification R-2, R-5, R-6; Procedure Steps; Verification | PROPOSAL: keep mechanics TBD until the project document control standard and turnover standard are added to `_REFERENCES.md`. | TBD |
