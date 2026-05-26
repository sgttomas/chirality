# Guidance — DEL-064-05 Vendor Document Turnover Package (PKG-064 Tanks, Water (API 650) 4-25)

## Purpose

This deliverable establishes a single, controlled, EPC-accepted body of vendor documentation for the PKG-064 Process Water Storage Tank package (`TK-5317-1`, `TK-5318-1`) so that operations, maintenance, regulatory, and integrity-management functions can rely on it after package turnover. Per `DELIVERABLE_REGISTER.csv`, the Package Vendor owns the documentation, and the EPC Integrator performs interface/integration review.

## Principles

- **Document ownership is unambiguous.** The Package Vendor is the document author and owner; the EPC Integrator reviews for interface/integration fit, not for vendor internal design correctness (which the vendor warrants).
- **Source vendor document table rows are artifacts, not separate deliverables.** Individual vendor documents listed in Workbook Packages row 96 (location TBD) are evidence supporting this deliverable; they do not create their own decomposition entries. Source: `_CONTEXT.md` Notes.
- **The register is the truth set.** Status and acceptance derive from the controlled Vendor Document Register, not from ad-hoc transmittals or email.
- **Turnover is the close-out event.** The deliverable is not complete until a final transmittal/manifest is issued and EPC-accepted; absence of explicit acceptance leaves the package documentation open.
- **Source fidelity over convention.** Document categories, codes, and timing required by `26020-Package_Requirements.docx` package heading 19 (location TBD) govern; do not substitute generic vendor-document conventions for the project's stated requirements.
- **Field-erected scope drives documentation flow.** API-650 atmospheric tanks are field-erected, so documentation milestones differ from shop-fabricated equipment (e.g., no single FAT; field hydrotest is the principal acceptance test). Source: `4-25_Deepcut_DBM.md` line 518.

## Considerations

- The authoritative source for vendor-documentation requirements (`26020-Package_Requirements.docx` package heading 19) and the vendor-doc columns of Workbook Packages row 96 are binary source files (`.docx` / `.xlsx`) listed in `_REFERENCES.md` but not converted to locally readable text in `_Sources`. Substantive category/timing requirements remain `TBD` until source slices are extracted.
- The package covers two like-for-like tanks (`TK-5317-1`, `TK-5318-1`). Documentation should be issued per tank where uniqueness exists (e.g., MTRs, NDE records, hydrotest records, coating inspection records) and once where common (e.g., design calculation set, OEM manuals).
- Material/coating/freeze-protection details drawn from the DBM (Devchem 253 internal coating; external insulation; heat tracing for freeze protection; PVRV; potential sour-vapour isolation review) all generate evidence-bearing documents that should be tracked in the register. Source: `4-25_Deepcut_DBM.md` lines 524, 2509.
- Vendor-document turnover interacts with DEL-064-06 (EPC Vendor Package Review and Acceptance); completeness here is a precondition for acceptance there.
- Supported objectives include OBJ-001/003/004/005/006/007/008/009/010. Documentation completeness is a key input to those objectives because operations, integrity, and inspection programs cite vendor documentation (ASSUMPTION on exact objective wording; not re-quoted here).

## Trade-offs

- **Submittal granularity vs. review burden.** Listing every minor vendor document on the register increases EPC review effort but improves traceability. Project document control procedure (location TBD) governs the threshold.
- **Early vs. late submittal of as-builts.** Final as-built drawings can only be issued after field erection, hydrotest, coating, and insulation completion. Standard practice (ASSUMPTION) is staged submittal with a final as-built revision at turnover.
- **Per-tank vs. common documentation.** Issuing every document set per tank inflates register size; issuing only common documents loses traceability of tank-unique manufacturing/inspection records. Standard practice (ASSUMPTION) is to common design/manuals and per-tank fabrication/inspection records.
- **Paper turnover vs. electronic-only.** Electronic data books are typical for current EPC practice (ASSUMPTION); paper originals may still be required for jurisdictional registration records (location TBD per project doc-control procedure).

## Examples

Examples of register line items that would be expected for this package (illustrative only — not extracted from authoritative source; all subject to confirmation against `26020-Package_Requirements.docx` package heading 19, location TBD):

- API-650 design calculation package (shell, bottom, roof, anchorage, settlement, seismic, wind)
- General arrangement / fabrication / erection drawings as-built (per tank)
- Welding procedure specifications and qualifications (WPS/PQR/WPQ)
- Materials test reports (MTRs) for shell, bottom, roof, and nozzle materials (per tank)
- NDE records (RT/UT/PT/MT/VT as applicable, per tank)
- Hydrotest / leak-test records (per tank)
- Internal coating system specification (Devchem 253) and application/inspection records (per tank)
- External insulation specification and installation records (per tank)
- Heat-tracing system documentation and commissioning records (per tank)
- PVRV / EPRV sizing and certification (per tank)
- Kennilworth-type hydrocarbon skim float system documentation (per tank)
- OEM operating and maintenance manuals
- Recommended spare-parts list
- Jurisdictional registration package (where applicable)

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none open) | No source-grounded conflicts identified at Pass 1/Pass 2. Authoritative `26020-Package_Requirements.docx` package heading 19 not yet accessible as text; conflicts cannot be enumerated against decomposition prose. | — | — | — | — | TBD |
