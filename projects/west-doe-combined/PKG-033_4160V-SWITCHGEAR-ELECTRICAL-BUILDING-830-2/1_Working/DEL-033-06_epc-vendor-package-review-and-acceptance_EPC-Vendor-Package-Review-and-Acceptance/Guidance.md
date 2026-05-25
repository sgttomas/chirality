# Guidance: DEL-033-06_epc-vendor-package-review-and-acceptance

## Purpose

This deliverable converts the accepted Gate 7 basis for `PKG-033` (4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)) into EPC-side review and acceptance evidence. It demonstrates that the vendor package has been reviewed against the EPC Scope of Work, Package Datasheet, and Construction Work Package, and is ready for handoff to facility integration.

The deliverable is positioned as Gate 5 EPC Integrator evidence, additional to the four core EPC anchor deliverables (`DEL-033-01` through `DEL-033-04`/`DEL-033-05`). It does not author vendor engineering content; it reviews and accepts it.

## Principles

- Preserve source spelling and identity. The package name is carried as "4160V SWITCHGEAR ELECTRICAL BUILDING (830-2)" from workbook row 35 and `PACKAGE_REGISTER.csv`.
- Acceptance is review evidence, not redesign. Vendor-owned engineering content is not produced or restated here.
- Trace every acceptance entry back to a basis-document item (EPC SoW, Package Datasheet, or Construction Work Package) and to a vendor input (Vendor Engineered Equipment Package, Vendor Document Turnover Package).
- Use `TBD` for package-specific 4160V switchgear acceptance criteria until a package-specific source slice is available; `PACKAGE_REGISTER.csv` confirms no `26020-Package_Requirements.docx` PKG-033 match.
- Address every applicable interface for `PKG-033`. Twelve interfaces are listed in `INTERFACE_REGISTER.csv`; none may be silently dropped from the review log.

## Considerations

The package is electrical/vendor-owned with a large interface surface (twelve interface types in `INTERFACE_REGISTER.csv`). The review log and acceptance checklist must therefore cover both the electrical interface (Electrical Power, Grounding/Bonding, I&C/Control Cabling, Communications/Network, Area/Exterior Lighting, Fire & Gas/Safety Systems) and the facility/civil interface (Utility Piping, Drain/Containment, Building HVAC/Services, Maintenance Access, Grading/Site Drainage/Spill Containment, Structural/Foundations/Supports). Allocating only the electrical surface would understate the EPC integration scope.

The CoA tracking number 26020-02-30-024 ties this package to project cost-of-account tracking. Acceptance evidence should be retrievable by this number for downstream commercial and turnover use.

No package-specific source slice (e.g., `26020-Package_Requirements.docx` PKG-033 match) is available in this deliverable folder. Acceptance criteria for 4160V switchgear-specific items (relay settings, breaker ratings, factory test acceptance values, arc-flash and protection coordination) therefore remain `TBD` and must be sourced from the accepted EPC Package Datasheet (`DEL-033-02`) or vendor data when issued. Inferring these values from generic switchgear convention would substitute convention for source and is not permitted.

The deliverable is review-and-acceptance, not authorship. When vendor content conflicts with the EPC basis, the resolution path is to record the conflict in the review log against the relevant EPC basis item and route it for ruling, not to silently rewrite either side.

## Trade-offs

| Topic | Conservative position | Reason |
|---|---|---|
| Package-specific acceptance criteria | Mark `TBD` pending Package Datasheet detail and vendor data. | No PKG-033 source match in `26020-Package_Requirements.docx`. |
| Interface coverage scope | Cover all twelve `INTERFACE_REGISTER.csv` interfaces for `PKG-033`. | Source explicitly lists all twelve as applicable. |
| Test/inspection evidence depth | Accept vendor-supplied factory/shop evidence as-is and record gaps; do not synthesize substitute evidence. | EPC reviewer role; vendor owns test execution. |
| Vendor design conflicts | Record in review log against EPC basis item and surface for ruling. | Preserves vendor/EPC responsibility split. |
| Objectives mapping | Treat OBJ-002, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 as `PACKAGE_HEURISTIC` ASSUMPTION (best-effort) unless confirmed. | `OBJECTIVE_DELIVERABLE_MAP.csv` lists the row, but objective rows are package-grouped. |

## Examples

- Acceptable acceptance entry: "Acceptance against `DEL-033-02_package-datasheet` REQ-033-02-007 (interface coverage Electrical Power): vendor electrical single-line aligns with Package Datasheet interface fact `IFC-87E42C897B`. Status: ACCEPTED. Source: vendor doc ID `TBD`."
- Acceptable source-gap entry: "Factory test acceptance value for 4160V breaker interrupting rating: `TBD`. No PKG-033-specific source slice; pending vendor factory test report."
- Not acceptable: "Vendor switchgear acceptance: 4160V, 1200A bus, 40 kA interrupting rating, ACCEPTED." Source set does not support these values.

## Conflict Table (for human ruling)

| Conflict ID | Conflict (short statement) | Source A (file + section) | Source B (file + section) | Impacted sections | Proposed authority (PROPOSAL) | Human ruling (TBD) |
|---|---|---|---|---|---|---|
| HRR-033-06-001 | No package-specific source slice (`26020-Package_Requirements.docx` PKG-033 match) is available; acceptance values for 4160V switchgear-specific items cannot be source-grounded in this deliverable folder. | `_REFERENCES.md` Missing/Deferred References | `PACKAGE_REGISTER.csv` row `PKG-033` `DocxPackageMatched=FALSE` | Datasheet Construction; Specification Requirements (REQ-033-06-004, REQ-033-06-009); Procedure Steps | Treat package-specific acceptance criteria as `TBD` until Package Datasheet (`DEL-033-02`) and vendor data resolve them. Do not invent acceptance values. | TBD |
| HRR-033-06-002 | Sibling deliverables `DEL-033-01_scope-of-work`, `DEL-033-02_package-datasheet`, `DEL-033-03_construction-work-package`, `DEL-033-04_vendor-engineered-equipment-package`, and `DEL-033-05_vendor-document-turnover-package` are listed as the acceptance basis but their content maturity at this Phase 2.2 pass is `INITIALIZED` at best; final acceptance cannot be issued from this run. | `_CONTEXT.md` Scope | Sibling deliverable `_STATUS.md` files (not read here; out of scope) | Specification REQ-033-06-005, REQ-033-06-006; Procedure Steps | Treat this deliverable's outputs as the acceptance-evidence skeleton at INITIALIZED; populate substantive acceptance entries only after sibling basis deliverables reach the appropriate maturity. | TBD |
