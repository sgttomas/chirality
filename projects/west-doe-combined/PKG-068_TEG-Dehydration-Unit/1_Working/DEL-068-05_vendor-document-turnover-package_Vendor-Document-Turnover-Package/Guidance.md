# Guidance — DEL-068-05 Vendor Document Turnover Package (PKG-068 TEG Dehydration Unit)

## Purpose

This deliverable establishes a single, controlled, EPC-accepted body of vendor documentation for the PKG-068 TEG Dehydration Unit so that operations, maintenance, regulatory (pressure-equipment registration), and integrity-management functions can rely on it after package turnover. Per `DELIVERABLE_REGISTER.csv` row 550, the Package Vendor owns the documentation, and the EPC Integrator performs interface/integration review.

## Principles

- **Document ownership is unambiguous.** The Package Vendor authors and owns the documentation; the EPC Integrator reviews for interface/integration fit, not for vendor internal design correctness (which the vendor warrants).
- **Source vendor document table rows are artifacts, not separate deliverables.** Individual vendor documents listed in Workbook Packages row 97 (location TBD) are evidence supporting this deliverable; they do not create their own decomposition entries. Source: `_CONTEXT.md` Notes.
- **The register is the truth set.** Status and acceptance derive from the controlled PRQ-009 Vendor Document Index (governed by DOC-008), not from ad-hoc transmittals or email.
- **Turnover is the close-out event.** The deliverable is not complete until a final transmittal/manifest is issued and EPC-accepted (PRQ-016 + QLT-021 as the final record set); absence of explicit acceptance leaves the package documentation open.
- **Source fidelity over convention.** Document categories, codes, and timing required by `26020-Package_Requirements.docx` package heading 23 govern; do not substitute generic vendor-document conventions for the project's stated requirements.

## Considerations

- The TEG Dehydration package is a multi-equipment skid spanning static pressure equipment (TEG Contactor, Glycol Flash Tank, Fuel Gas Scrubber, TEG Make-up Tank), rotating equipment (Glycol Circulation Pumps), heat-transfer equipment (Inlet Air Cooler, Gas/Glycol Exchanger, Air/Glycol Exchanger, Glycol Reboiler), filtration (Filter Coalescer, Glycol Particulate/Charcoal Filters), and a Burner Control Panel. The documentation requirements differ in kind across these equipment classes; the register must reflect that breadth.
- The Glycol Reboiler/Still Column is fired equipment with a Burner Control Panel; vendor documentation should include the burner management system (BMS) and fire-and-gas / safety-instrumented function records (TSF-009, TSF-011, TSF-013) in addition to the mechanical/process set.
- Static pressure vessels require jurisdictional registration via REG-022 (Pressure Equipment Registration Package). Provincial pressure-vessel acceptance is typically a precondition for site commissioning; turnover should align with registration timing.
- The authoritative source for vendor-documentation requirements (`26020-Package_Requirements.docx` package heading 23) was text-extracted and read for this draft. The companion Workbook Packages row 97 vendor-doc columns (`26020-Packages_Interfaces_4_export.xlsx`) remain a binary `.xlsx` not converted; specific submittal codes/timings beyond what heading 23 enumerates remain `TBD` until that slice is extracted.
- DOC-008 (Vendor Document Control Procedure) is itself a vendor deliverable on the index; the controlling EPC project document control procedure (which sets review codes, file naming, and transmittal mechanics for the vendor to comply with) is referenced only implicitly in heading 23. Location of that EPC procedure is TBD.
- Vendor-document turnover interacts with DEL-068-06 (EPC Vendor Package Review and Acceptance); completeness here is a precondition for acceptance there.
- Supported objectives include OBJ-007/008/009/010 (typically integrity, safety, operability, and lifecycle objectives in this project — ASSUMPTION; precise objective text not re-quoted here). Documentation completeness is a key input to those objectives because operations and inspection programs cite vendor documentation.

## Trade-offs

- **Submittal granularity vs. review burden.** Listing every minor vendor document on PRQ-009 increases EPC review effort but improves traceability. DOC-008 (and the governing EPC project doc-control procedure — location TBD) governs the threshold.
- **Early vs. late submittal of as-builts.** Final as-built drawings (e.g., PRO-028, PIP-028, INS-029) can only be issued after fabrication and FAT, but holding back the rest of the package until then delays turnover. Standard practice (ASSUMPTION) is staged submittal with a final as-built revision at turnover.
- **Single combined vendor data book vs. discipline-split.** Heading 23 lists PRQ-016 (Vendor Data Book / Final Supplier Documentation), QLT-021 (Manufacturing Record Book / Vendor Data Book), and MEC-023 (Vendor Data Book / Mechanical Final Documentation) as separate deliverables. Whether these consolidate into one electronic data book or remain split per discipline at turnover is a project doc-control choice — TBD per DOC-008 and the project's overarching doc-control procedure.
- **Paper turnover vs. electronic-only.** Electronic data books are typical for current EPC practice (ASSUMPTION); paper turnover may still be required for jurisdictional pressure-equipment registration originals (REG-022 supporting documents) — TBD per provincial pressure-equipment authority requirements.
- **Burner Control Panel software/firmware records.** Burner management system firmware/configuration records are operationally critical for the reboiler; whether these are covered by CTL-003/CTL-026 or by a vendor-specific BMS deliverable not enumerated in heading 23 is TBD.

## Examples

Examples of register line items expected for this package (drawn from heading 23 enumerations; specific quantities/document numbers TBD until vendor issues PRQ-009):

- MEC-009 Pressure Vessel Data Sheet — TEG Contactor (as-built)
- MEC-009 Pressure Vessel Data Sheet — Glycol Flash Tank (as-built)
- REG-022 Pressure Equipment Registration Package — TEG Contactor; Glycol Flash Tank; Fuel Gas Scrubber
- MEC-007 Pump Data Sheets — Glycol Circulation Pumps
- MEC-019 Mechanical Seal / Lube Oil Specification — Glycol Circulation Pumps
- MEC-010 Heat Exchanger Data Sheets — Inlet Air Cooler; Gas/Glycol Exchanger; Air/Glycol Exchanger; Glycol Reboiler/Still Column
- PRO-008 P&IDs (package) — final as-built revision (under PRO-028 As-Built P&ID Package)
- PRO-007 Process Description / Operating Philosophy — TEG dehydration
- PRO-025 Operating Guidelines / Startup-Shutdown Narrative — including regeneration cycle
- TSF-011 Safety Requirements Specification (SRS) for the BMS / fired-equipment safety functions
- CTL-005 Cause and Effect Matrix — package interlocks
- QLT-013 Material Test Reports — pressure-retaining components
- MEC-022 Equipment FAT / Performance Test Report — package
- MEC-025 Mechanical Equipment IOM Manual — package
- PRQ-015 Spare Parts Interchangeability Record (SPIR)
- PRQ-016 Vendor Data Book / Final Supplier Documentation (final turnover)

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| (none open) | No source-grounded conflicts identified at Pass 1/Pass 2. The authoritative source slice (`26020-Package_Requirements.docx` package heading 23) was accessible and read; the companion Workbook row 97 columns and the EPC project document control procedure remain inaccessible and produce only `TBD` markers, not conflicts. | — | — | — | — | TBD |
