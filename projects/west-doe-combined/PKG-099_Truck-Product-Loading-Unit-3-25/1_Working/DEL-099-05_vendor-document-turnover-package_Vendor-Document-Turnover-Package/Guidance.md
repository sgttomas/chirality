# Guidance: DEL-099-05 — Vendor Document Turnover Package

## Purpose

The Vendor Document Turnover Package exists so that the operator receives a complete, traceable, and current set of vendor information for the `PKG-099 Truck Product Loading` mechanical package, sufficient to operate, maintain, troubleshoot, inspect, and re-procure the equipment over its life. It also gives the EPC Integrator the evidence base needed to confirm that vendor design, interface, and integration constraints have been honored before turnover.

Source: `_CONTEXT.md` Scope; DBM SEC-09 "Mechanical Package Structure" (line 617).

## Principles

- **The register is the contract surface.** The vendor document register is the single index that determines whether turnover is complete. Anything not on the register is invisible at handover.
- **Source-required documents are not optional.** Documents named explicitly in the project package requirements specification (heading 51) are required, independent of the vendor's standard documentation set.
- **EPC Integrator review is integration-focused, not redesign.** Review confirms interface, integration, and specification compliance; it does not substitute for vendor engineering accountability.
- **Turnover is staged.** Issued-For-Review, Issued-For-Construction, and As-Built revisions serve different downstream consumers; the register should make stage explicit.

## Considerations

- The truck loading service is product (sales-spec) condensate, not sour service (DBM SEC-06 line 22; FACT). Documentation should reflect product-side service conditions, not sour-side metallurgy/coating choices.
- LACT equipment is third-party NRM scope (DBM SEC-06 line 417; FACT). The vendor turnover package must not include or be relied upon for LACT documentation, but should clearly identify the facility-side tie-in interface that the vendor equipment terminates at.
- Site ambient is -40 deg C minimum (DBM SEC-09 line 145; FACT). Vendor-supplied winterization, heat tracing, building heating, and field device suitability must be evidenced in documentation.
- Three loading stations, three condensate loading pumps (DBM SEC-06 lines 414-415; FACT). Documentation completeness should be evaluated per-station and per-pump, not as a single instance.

## Trade-offs

- **Register granularity vs. maintenance burden.** A finer register (every revision tracked) supports traceability but increases maintenance load. A coarser register risks losing change history. Default to per-document-number rows with revision sub-history.
- **Early submittal vs. late accuracy.** Issuing register entries early supports project tracking, but content accuracy lags. Trade-off should be resolved by clear stage labels (IFR/IFC/AB) rather than withholding entries.
- **Scope of vendor warranty vs. operator self-sufficiency.** Heavier IOM/training content reduces operator dependence on vendor field service but increases vendor documentation cost. The project specification index should govern; the local trade-off is **TBD**.

## Examples

Examples from accessible sources are limited because `26020-Package_Requirements.docx` heading 51 (the explicit per-package vendor documentation requirements) is not locally parseable. No invented examples are provided. **TBD — examples deferred until source becomes accessible.**

## Conflict Table (for human ruling)

| Conflict ID | Conflict | Source A | Source B | Impacted Sections | Proposed Authority (PROPOSAL) | Human Ruling (TBD) |
|---|---|---|---|---|---|---|
| C-1 | Required vendor document classes for PKG-099 are stated generically in DBM SEC-09 (line 617) but the package-specific list lives in `26020-Package_Requirements.docx` heading 51, which is not locally parseable. The two may not align in either direction. | DBM SEC-09 line 617 (generic mechanical package list) | `26020-Package_Requirements.docx` heading 51 (package-specific list) — **location TBD** | Specification R2, R3, R4; Datasheet "Required package deliverable content" | When package-specific list becomes available, it governs; the DBM SEC-09 list is a generic floor (PROPOSAL). | TBD |
| C-2 | Turnover record contents are not explicitly enumerated in any locally accessible source for this deliverable. Specification R5 lists typical industry items as ASSUMPTION. | None accessible | `26020-Package_Requirements.docx` heading 51 / project specification index (DBM SEC-12 line 888) — **location TBD** | Specification R5; Procedure steps for turnover assembly | When source becomes accessible, replace ASSUMPTION items with sourced list (PROPOSAL). | TBD |
| C-3 | Workbook Packages row 98 and `26020-Package_Requirements.docx` heading 51 are both cited by `_CONTEXT.md` as the source basis. Whether they agree on the document list and whether either is authoritative over the other for this deliverable is unverified. | `26020-Packages_Interfaces_4_export.xlsx` row 98 — **location TBD** | `26020-Package_Requirements.docx` heading 51 — **location TBD** | Specification R3, R4; Datasheet | Treat `26020-Package_Requirements.docx` heading 51 as primary for document classes; treat workbook row 98 as identity/interface metadata (PROPOSAL). | TBD |
