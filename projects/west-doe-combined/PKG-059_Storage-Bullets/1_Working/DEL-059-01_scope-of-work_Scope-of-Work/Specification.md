# Specification — DEL-059-01_scope-of-work — Scope of Work (PKG-059 Storage Bullets)

## Scope

### Includes

This EPC Scope of Work establishes the package basis for **PKG-059 Storage Bullets**, namely the supply of two unstable condensate storage bullets and sixteen LPG product storage bullets for C5 condensate and LPG product storage at the 04-25 Deep Cut Gas Plant, including identification, tagged equipment, package function, source basis, boundaries, and whole-facility integration narrative.

Source: `_CONTEXT.md` Scope; SCOPE_LEDGER.csv SOW-0182.

### Excludes

- Foundations (by others). Source: SCOPE_LEDGER SOW-0184.
- DCS integration (by others). Source: SCOPE_LEDGER SOW-0184.
- Electrical supply to the MCC (by others). Source: SCOPE_LEDGER SOW-0184.
- Detailed Package Vendor engineering/design/documentation deliverables — these are not authored here but are required as separate deliverables (`DEL-059-04`, `DEL-059-05`).
- Package-specific exclusions other than the above: none stated in source materials. (`TBD` — PACKAGE_REGISTER Exclusions column reads "TBD; no package-specific exclusions stated in source materials.")

## Requirements

| ID | Requirement | Source |
|---|---|---|
| REQ-059-01-01 | The Storage Bullets package shall be carried as a distinct flat project package under WBS 01, Mechanical discipline, with CoA tracking number 26020-01-17-007. | SCOPE_LEDGER SOW-0181; PACKAGE_REGISTER row 83 |
| REQ-059-01-02 | The Package Vendor shall own package engineering, package design, vendor documentation, and the physical equipment package. | PACKAGE_REGISTER row 83 Responsibility; SCOPE_LEDGER SOW-0181; OBJ-004 |
| REQ-059-01-03 | The EPC Integrator shall own facility-level integration, interfaces, tie-ins, constructability, procurement/construction coordination. | PACKAGE_REGISTER row 83 Responsibility; SCOPE_LEDGER SOW-0181 |
| REQ-059-01-04 | The package shall include two unstable condensate storage bullets and sixteen LPG product storage bullets for C5 condensate and LPG product storage. | SCOPE_LEDGER SOW-0182 |
| REQ-059-01-05 | Each bullet shall be 3658 mm ID x 42494 mm seam-to-seam, with a nominal volume of 454 m3 / 120,000 US gal at 84% maximum volume. | SCOPE_LEDGER SOW-0183 |
| REQ-059-01-06 | Each bullet shall be designed for 1724 kPag at 66 C and full vacuum. | SCOPE_LEDGER SOW-0183 |
| REQ-059-01-07 | Bullets shall be mounted outdoors on saddles, with stairs and platforms provided. | SCOPE_LEDGER SOW-0183 |
| REQ-059-01-08 | Unstable condensate bullets shall store condensate from the C5 product line ahead of the condensate transfer pumps. | SCOPE_LEDGER SOW-0184 |
| REQ-059-01-09 | LPG bullets shall store C3, C4, or C3/C4 LPG mix from the depropanizer ahead of transfer to the off-site liquids hub via booster pumps. | SCOPE_LEDGER SOW-0184 |
| REQ-059-01-10 | LPG vapour equalization shall avoid pockets. | SCOPE_LEDGER SOW-0184 |
| REQ-059-01-11 | Butane storage shall be provided with blanket gas. | SCOPE_LEDGER SOW-0184 |
| REQ-059-01-12 | The package shall preserve interface types: Process Piping; Relief / Flare / Vent; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports. | INTERFACE_REGISTER (10 rows PKG-059); PACKAGE_REGISTER row 83 |
| REQ-059-01-13 | Sour-service safety, relief, flare, blowdown, drain/containment, fire/gas, shutdown, environmental, emissions, and regulatory codes/standards shall be carried into the package scope and interfaces. | OBJ-009 OBJECTIVE_REGISTER |
| REQ-059-01-14 | Pressurized-bullet spacing rules shall comply with API 2510 (e.g., maximum 6 bullets per cluster; 15.24 m (50 ft) cluster-to-cluster; 38.1 m (125 ft) to property line). ASSUMPTION: derived from `DBM-Deepcut/4-25_Deepcut_DBM.md` Pressurized Bullet Spacing tables; full API 2510 clause text not locally available. | DBM-Deepcut/4-25_Deepcut_DBM.md (lines ~245-266, 284, 299) |
| REQ-059-01-15 | Operability, maintainability, sparing, isolation, winterization, vendor-documentation, commissioning, turnover, and open-item closure evidence shall be preserved through downstream deliverables. | OBJ-010 OBJECTIVE_REGISTER |

## Standards

| Standard | Application | Location |
|---|---|---|
| API 2510 | Pressurized-bullet spacing, including bullet-to-property-line and inter-cluster distances | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` Pressurized Bullet Spacing; verbatim API 2510 clauses `location TBD` |
| 26020-Package_Requirements.docx | Package heading 14 — Storage Bullets package basis | `_Sources/26020-Package_Requirements.docx`; section heading 14; `location TBD` for verbatim slices (binary not parsed in-run) |
| Sour-service safety, environmental, regulatory codes and standards | Per OBJ-009 — carried into package interfaces | `location TBD` (specific code list pending design development) |

## Verification

| Requirement | Verification approach |
|---|---|
| REQ-059-01-01..03 | Document review of this SoW, the Package Datasheet (`DEL-059-02`), and the Responsibility Assignment Record artifact (ART-F8F9048873). |
| REQ-059-01-04..07 | Vendor Engineered Equipment Package (`DEL-059-04`) shall provide vessel datasheets, design calculations, and fabrication drawings demonstrating geometry, MAWP, MAWT, vacuum design, and saddle/stair/platform provisions. |
| REQ-059-01-08..11 | P&ID and process design review at the package boundary; LPG vapour-equalization arrangement, butane blanket-gas tie-in, and pump-suction service confirmed at integration design review. |
| REQ-059-01-12 | EPC integration review against INTERFACE_REGISTER PKG-059 entries; tie-in list reconciliation. |
| REQ-059-01-13 | Safety/HAZID/HAZOP review and code/standard register cross-walk during EPC integration. |
| REQ-059-01-14 | Plot-plan review against API 2510 spacing tables; deviations recorded as open issues. |
| REQ-059-01-15 | EPC Vendor Package Review and Acceptance (`DEL-059-06`); vendor document turnover (`DEL-059-05`) completeness check. |

## Documentation

Anticipated artifacts (from `_CONTEXT.md` and ARTIFACT_REGISTER):

- Package scope of work (this document context) — ART-E74992DA9A.
- Tagged equipment and package identity list — ART-D07C763AAE.
- Package function and whole-facility integration narrative — ART-07935F28C9.
- Package responsibility assignment record — ART-F8F9048873.
- Detailed mechanical package scope extraction evidence — ART-3213233765.

Downstream package deliverables: `DEL-059-02 Package Datasheet`, `DEL-059-03 Construction Work Package`, `DEL-059-04 Vendor Engineered Equipment Package`, `DEL-059-05 Vendor Document Turnover Package`, `DEL-059-06 EPC Vendor Package Review and Acceptance` (source: OBJECTIVE_DELIVERABLE_MAP.csv).
