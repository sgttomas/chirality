# Guidance: DEL-031-05 — Vendor Document Turnover Package

## Purpose

DEL-031-05 exists so the Package Vendor's documentation for the PKG-031 step-down distribution transformer (TXP-8500-1, 3 MVA, 13.8 kV / 600/347 V) is registered, submitted, controlled, and formally turned over as a single coherent deliverable, with EPC Integrator interface/integration review preserved as a separate responsibility (DEL-031-06).

The decomposition explicitly carries source vendor-document rows as artifacts/evidence under this deliverable rather than minting one deliverable per vendor document (PROJECT_DECOMP DEC-004 and DEC-012).

## Principles

- **Vendor ownership.** Vendor documents are authored and owned by the Package Vendor; the EPC Integrator reviews and integrates but does not author (DEC-006; OBJ-004).
- **Single turnover container.** All vendor documents and turnover evidence for PKG-031 are grouped here; source vendor-document rows are artifacts, not deliverables (DEC-004).
- **Source fidelity.** The required vendor document set is bounded by what the PKG-031 section of `26020-Package_Requirements.docx` specifies plus what the vendor's scope of supply contractually requires. Do not invent required documents from generic transformer conventions when the source is silent — mark `TBD` and surface via a Conflict Table or open item.
- **Closure evidence.** Turnover is not transmittal; it is the reconciled, signed-off record that the register is complete and disposition is recorded for every open item (OBJ-010).

## Considerations

- The PKG-031-specific vendor-documentation table in `26020-Package_Requirements.docx` has not been sliced into `0_References/`. Until that slice is captured, the register contents and required document list are `TBD` against source.
- Distribution transformer vendor packages typically include nameplate drawings, outline/general arrangement, factory test reports (routine and type), insulation/dielectric test reports, oil/insulating-fluid analysis (if liquid-filled), bushing and tap-changer data, IOM manuals, and shipping records — treat this as **ASSUMPTION** until confirmed by the PKG-031 source slice.
- Coordination with DEL-031-06 (EPC Vendor Package Review and Acceptance) is essential: this deliverable is the input register and submittal set that DEL-031-06 reviews and accepts.

## Trade-offs

- **Register granularity vs. effort.** A finer register (per drawing sheet, per test report) gives better traceability but increases administrative load. The decomposition treats source vendor-document table rows as the minimum granularity (one register row per source-required document type) — additional rows may be added where vendor scope produces sub-documents.
- **Early submittal vs. final-only.** Submitting interim revisions enables earlier EPC integration review (DEL-031-06) but adds transmittal churn. The default expectation (ASSUMPTION) is interim submittal for design-affecting documents and final-only for purely as-built/test documents.

## Examples

- A vendor-supplied factory acceptance test (FAT) report becomes a register row, a submittal artifact, and a turnover record (final accepted revision transmittal). It is referenced by DEL-031-06 acceptance evidence.
- A nameplate drawing is a register row; revisions are tracked through transmittal; the as-shipped final is the turnover artifact.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-031-05-001 | The required PKG-031 vendor document list is not locally sliced from `26020-Package_Requirements.docx`; register contents are `TBD`. | `_REFERENCES.md` ("No deliverable-specific source slices copied") | `_Sources/26020-Package_Requirements.docx` (PKG-031 section, location TBD) | Specification REQ-031-05-01, REQ-031-05-03; Datasheet Construction | Capture the PKG-031 section as a local source slice in `0_References/` before producing the register. | TBD |
| HRR-031-05-002 | Transformer fluid type (liquid-filled vs. dry) is not stated in extracted sources; vendor document set differs materially (e.g., dielectric fluid analysis applicability). | `_CONTEXT.md` (silent) | `_Sources/26020-Package_Requirements.docx` (PKG-031 section — TBD) | Datasheet Attributes; Specification REQ-031-05-03 | Defer fluid-dependent register rows until PKG-031 source slice or vendor scope confirms. | TBD |
| HRR-031-05-003 | Transmittal protocol and EPC review interface mechanism are not specified in extracted sources. | `_CONTEXT.md` (silent) | Project execution plan (not in extracted sources) | Specification REQ-031-05-02, REQ-031-05-05; Procedure Steps | Adopt the project-standard document control protocol once identified; meanwhile follow declared coordination mode (DECLARED). | TBD |
