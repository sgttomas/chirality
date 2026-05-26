# Datasheet: DEL-094-05 — Vendor Document Turnover Package

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-094-05_vendor-document-turnover-package` |
| Name | Vendor Document Turnover Package |
| ParentPackageID | `PKG-094` |
| PackageName | Tanks, Caustic (API 650) 3-25 |
| Discipline | Mechanical |
| Type | Vendor Document Turnover |
| ResponsibleParty | Package Vendor (vendor documentation) with EPC Integrator interface/integration review |
| Covers Scope Items | `SOW-0193`, `SOW-0194`, `SOW-0195`, `SOW-0196` |
| Supports Objectives | `OBJ-002` through `OBJ-010` (ASSUMPTION: package-grouping heuristic per `_CONTEXT.md`) |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable subject | Vendor document register, submittals, source-required vendor documentation, and turnover records for the PKG-094 caustic tanks package | `_CONTEXT.md` Scope; DELIVERABLE_REGISTER row DEL-094-05 |
| Document register basis | Mechanical package deliverables shall include "datasheets, cause-and-effect inputs, utility load summaries, relief/load data, field tie-in lists, operating and design envelopes, sparing philosophy, materials and coating basis, maintenance access, shipped-loose item lists, and vendor document registers" | `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` line 617 |
| Source-required vendor document table | Package-specific vendor document table is enumerated in the 26020 Package Requirements document | `_Sources/26020-Package_Requirements.docx` package heading 46 (location TBD — binary source; clause-level rows not extractable in this run) |
| EPC Integrator review role | EPC Integrator performs interface/integration review of vendor documentation | `_CONTEXT.md`; DELIVERABLE_REGISTER row DEL-094-05 |
| Vendor documentation responsibility | Package Vendor owns package engineering, package design, vendor documentation, and physical equipment supply | PACKAGE_REGISTER row PKG-094; DBM 3-25 |
| Cross-deliverable relationship | DEL-094-06 (EPC Vendor Package Review and Acceptance) consumes the vendor document review log produced from this deliverable | DELIVERABLE_REGISTER row DEL-094-06 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Package equipment scope (defines documentation envelope) | One (1) Spent Caustic Tank (TK-6930-2, ~400 bbl) and one (1) Fresh Caustic Tank, API 650 atmospheric, 32 oz / 1.0 oz vacuum | SOW-0194; SOW-0195 |
| Process service | Caustic mercaptan treating tankage in the 03-25 Liquids Hub (fresh / spent caustic storage) | DBM 3-25 |
| Code family (drives certification/turnover content) | Modified API 650 atmospheric tanks | SOW-0195 |
| Owner-supplied / by-others scope (defines documentation exclusions) | Foundations, mounting tanks at site, electrical/instrumentation, platforms, staircases, etc. by others | SOW-0196 |
| Document submission interface | Package Vendor submits to EPC Integrator for interface/integration review and acceptance (DEL-094-06) | DELIVERABLE_REGISTER rows DEL-094-05, DEL-094-06 |

## Construction (Document Set Composition)

| Document Class (anticipated) | Value | Source |
|---|---|---|
| Vendor document register (master index) | Required deliverable artifact | `_CONTEXT.md` Anticipated Artifacts; DELIVERABLE_REGISTER row |
| Vendor document submittals | Required deliverable artifact | `_CONTEXT.md` Anticipated Artifacts |
| Source vendor document table rows as artifacts | Each row of the source vendor document table is preserved as evidence/artifact rather than as a separate deliverable | `_CONTEXT.md` Notes; DELIVERABLE_REGISTER row Notes column |
| Turnover records | Required deliverable artifact | `_CONTEXT.md` Anticipated Artifacts |
| Equipment datasheets (vendor) | ASSUMPTION: typical for vendor packages; specific list TBD | DBM 3-25 line 617 (general); source vendor document table location TBD |
| Drawings (GA, P&ID extracts, foundation loads, nameplate / shipping) | TBD (specific list governed by source vendor document table) | location TBD |
| Cause-and-effect / control inputs | ASSUMPTION: typical mechanical package deliverable | DBM 3-25 line 617 |
| Utility load summaries | ASSUMPTION: typical mechanical package deliverable | DBM 3-25 line 617 |
| Relief / load data | ASSUMPTION: typical mechanical package deliverable | DBM 3-25 line 617 |
| Field tie-in lists | ASSUMPTION: typical mechanical package deliverable | DBM 3-25 line 617 |
| Operating and design envelopes | ASSUMPTION: typical mechanical package deliverable | DBM 3-25 line 617 |
| Sparing philosophy | ASSUMPTION: typical mechanical package deliverable | DBM 3-25 line 617 |
| Materials and coating basis | ASSUMPTION: typical mechanical package deliverable | DBM 3-25 line 617 |
| Maintenance access info | ASSUMPTION: typical mechanical package deliverable | DBM 3-25 line 617 |
| Shipped-loose item list | ASSUMPTION: typical mechanical package deliverable | DBM 3-25 line 617 |
| Inspection / test records (IRN, hydrotest, NDE) | TBD (governed by API 650 family and source vendor document table) | SOW-0195; location TBD |
| Operating & maintenance manuals | TBD (typical turnover) | location TBD |
| Spare parts list (commissioning / two-year) | TBD | location TBD |
| Material certifications (MTRs) | TBD | location TBD |
| Code stamping / nameplate records | TBD (API 650 family) | SOW-0195 |
| Painting / coating records | TBD | DBM 3-25 (caustic coating TBC) |

## Anticipated Artifacts (per `_CONTEXT.md`)

- Vendor document register
- Vendor document submittals
- Source vendor document table rows as artifacts where available
- Turnover records

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv` (row DEL-094-05; sibling rows DEL-094-01..06)
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/PACKAGE_REGISTER.csv` (row PKG-094)
- `_Decomposition/.../GATE-07_Final_Published_2026-05-24/SCOPE_LEDGER.csv` (SOW-0193..0196)
- `_Sources/DBM-Comp_and_Liquids/3-25_Comp_and_Liquids_DBM.md` (caustic treating, drain, mechanical packages basis)
- `_Sources/26020-Package_Requirements.docx` package heading 46 — source vendor document table (binary; clause-level slices not extracted in this run; `location TBD`)
