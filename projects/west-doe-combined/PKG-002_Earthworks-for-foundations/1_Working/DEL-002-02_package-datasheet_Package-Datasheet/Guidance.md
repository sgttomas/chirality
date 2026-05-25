# Guidance: Package Datasheet

## Purpose

Use this package datasheet as the EPC Integrator's technical handoff record for `PKG-002 - Earthworks for foundations`. The accepted Gate 7 basis makes `Package Datasheet` one of the mandatory EPC Integrator anchor deliverables for every approved package, and states that package datasheets carry the technical handoff basis required for third-party vendor or discipline package engineering and design. Source: Gate 7 `PROJECT_DECOMP.md` deliverable-basis section.

## Principles

- Treat Gate 7 as the accepted decomposition truth for package identity, deliverable identity, artifacts, interfaces, objectives, and scope membership.
- Treat `_Sources/26020-Packages_Interfaces_4_export.xlsx`, `Packages` sheet row 3, as the authoritative source for the package row and interface flags.
- Treat the 3-25 DBM SEC-11 civil/foundation/drainage language as the accessible technical basis for civil design considerations applicable to the WBS 02 facility context.
- Preserve workbook interface `X` facts as datasheet evidence, not as separate deliverables.
- Use `TBD` for package-specific values that are not present in accessible source slices.

## Considerations

The package is source-limited. Workbook row 3 confirms identity, discipline, WBS, CoA tracking number, and two interface categories, but it does not provide quantities, elevations, limits of disturbance, borrow/disposal requirements, material classification, compaction criteria, or drawing references.

The DBM SEC-11 source supports civil design themes such as grading, drainage, surface-water management, foundations, supports, roads, retention pond, fencing, and security. It does not provide package-specific earthworks quantities or design values for `PKG-002`.

The final geotechnical report is a closure dependency for foundation design. Until that report is available and cited, foundation criteria beyond the DBM-level drivers should remain `TBD`.

Surface-water and drainage content should distinguish between source-supported design intent and package-specific design values. The DBM supports the intent to prevent uncontrolled offsite discharge, protect process areas, and support construction and operations access; it does not provide a package-specific drainage calculation in the accessible slices.

## Trade-offs

| Trade-off | Guidance |
|---|---|
| Completeness vs. source fidelity | Prefer an incomplete datasheet with explicit `TBD` entries over a complete-looking datasheet containing unsupported civil quantities or criteria. |
| Interface matrix detail vs. workbook evidence | Include the two workbook-supported interface categories; do not infer additional interfaces from neighboring packages or general civil practice. |
| DBM general civil requirements vs. package-specific requirements | Use DBM SEC-11 as applicable civil basis, but mark package-specific details as `TBD` unless another accessible source states them. |
| EPC Integrator vs. subcontractor responsibility | Preserve the Gate 7 statement that responsibility is source-dependent; do not create a separate vendor ownership model for this civil package. |

## Examples

- Supported entry: `Interface type: Grading / Site Drainage / Spill Containment - Applicable`, cited to workbook row 3 and Gate 7 `INTERFACE_REGISTER.csv`.
- Supported entry: `Final geotechnical report required before foundation design closure`, cited to DBM SEC-11.
- Unsupported entry to avoid: a numeric cut/fill volume, compaction percentage, or foundation bearing value without a cited source.

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| None | No source-to-source conflict identified in accessible slices. Remaining gaps are missing information rather than conflicting information. | N/A | N/A | N/A | N/A | N/A |
