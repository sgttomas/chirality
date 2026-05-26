# Procedure: DEL-098-02 Package Datasheet

## Purpose

This procedure describes how to produce and check the `PKG-098` Tanks, Sour Water (API 650) 3-25 package datasheet from the accepted Gate 7 PROJECT_DECOMP snapshot, the deliverable-local context, and the package heading 50 source slice of 26020-Package_Requirements.docx.

## Prerequisites

- Accepted upstream decomposition truth: Gate 7 final published PROJECT_DECOMP snapshot dated 2026-05-24.
- Deliverable-local context files: `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`, and `_STATUS.md`.
- Local access to 26020-Package_Requirements.docx package heading 50 ("26020-03-PT-19-007 - Tanks, Sour Water").
- Current deliverable state permits overwrite under `ALLOW_OVERWRITE_STATES=OPEN,INITIALIZED`.
- Declared upstream dependencies: none declared in `_DEPENDENCIES.md`.
- Declared downstream dependencies: none declared in `_DEPENDENCIES.md`.
- Underlying vendor RFQ (Bid Docs/Budgetary/26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx) and Appendix A are NOT locally accessible — values that depend on them remain `TBD`.

## Steps

1. Confirm deliverable identity from `_CONTEXT.md` and `DELIVERABLE_REGISTER.csv`.
   - Expected result: `DEL-098-02_package-datasheet`, Package Datasheet, `PKG-098`, Tanks, Sour Water (API 650) 3-25, Mechanical, EPC Integrator, EPC Package Datasheet.
2. Confirm package identity and responsibility model from `PACKAGE_REGISTER.csv` row `PKG-098`.
   - Expected result: workbook ID 98, workbook row 93, WBS 03, CoA tracking number `26020-03-19-007`; vendor-owned engineering/design/equipment with EPC-owned facility integration.
3. Confirm covered scope items from `SCOPE_LEDGER.csv`.
   - Expected result: `SOW-0221` (vendor/EPC split), `SOW-0222` (basic scope), `SOW-0223` (major included equipment + common construction), `SOW-0224` (scope notes / open items).
4. Reproduce Basic Scope from 26020-Package_Requirements.docx package heading 50.
   - Expected result: Item No. 1 — three (3) 3800 bbl Sour Produced Water Storage Tanks (TK-9030-2, TK-9040-2, TK-9050-2); process function Sour Water Tanks.
5. Reproduce Major Included Equipment from package heading 50.
   - Expected result: Items 1–3 with tag counts and tag numbers; common construction features (modified API 650; Devchem 253 internal coating on floor/walls/roof; external insulation with electric heating; Kennilworth type HCL float skim system, one per tank).
6. Reproduce operating and design conditions from package heading 50, Scope Notes / Open Items.
   - Expected result: operating pressure Atmospheric; operating temperature 10 °C (Items 1 and 3), Item No. 2 TBD; design pressure 32 oz test pressure; design temperature -40 °C (min) and 60 °C (max).
7. Reproduce "by others" exclusions from package heading 50.
   - Expected result: foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase, etc.
8. Populate the interface matrix from `INTERFACE_REGISTER.csv` rows for `PKG-098`.
   - Expected result: nine YES interfaces present using exact register names (Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports).
9. Confirm artifact coverage from `ARTIFACT_REGISTER.csv`.
   - Expected result: EPC handoff artifacts (`ART-1458F2586B`, `ART-F958B0973F`, `ART-119F7B5D2B`), tagged equipment evidence (`ART-914A0B9939`), and all nine interface fact evidence artifacts present.
10. Confirm mapped objectives from `_CONTEXT.md` and `OBJECTIVE_DELIVERABLE_MAP.csv`.
    - Expected result: `OBJ-002` through `OBJ-010` included as context.
11. Mark unsupported design values as `TBD`.
    - Includes Appendix A capacity/throughput, driver, Item No. 2 operating temperature, modifications to API 650, H2S concentration and NACE clauses, additional codes (API 2000, NACE MR0175/MR0103, coating qualification, electric heat-trace), material/metallurgy, plate thicknesses, and nozzle/anchor design.
12. Cross-check the Datasheet, Specification, Guidance, and Procedure for terminology and value consistency (tank tags, temperatures, pressures, interface names).
13. Record unresolved human-ruling items in the Guidance Conflict Table (`HRR-098-02-001` through `HRR-098-02-004`).
14. Update `_STATUS.md` from OPEN to INITIALIZED using `tools/scaffolding/write_status.sh` with actor `TASK+four-documents`.

## Verification

| Verification item | Acceptance criterion | Source |
|---|---|---|
| Identity check | Datasheet and Specification identify `PKG-098`, Tanks, Sour Water (API 650) 3-25, Mechanical, WBS 03, workbook row 93, and CoA tracking number `26020-03-19-007`. | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Scope check | `SOW-0221`, `SOW-0222`, `SOW-0223`, and `SOW-0224` appear as covered scope items. | `_CONTEXT.md`; `SCOPE_LEDGER.csv` |
| Responsibility check | Vendor / EPC integrator split is reproduced from `PACKAGE_REGISTER.csv` without paraphrase changes that alter ownership. | `PACKAGE_REGISTER.csv` row `PKG-098` |
| Equipment check | Basic Scope and Major Included Equipment match package heading 50, including tag numbers, item counts, and common construction features. | 26020-Package_Requirements.docx package heading 50; `SCOPE_LEDGER.csv` rows `SOW-0222`, `SOW-0223` |
| Conditions check | Operating pressure, operating temperature (with Item No. 2 TBD), design pressure, and design temperature appear exactly as stated. | 26020-Package_Requirements.docx package heading 50, Scope Notes / Open Items |
| Exclusions check | "By others" list (foundations, mounting, electrical/instrumentation, platforms, staircase, etc.) is preserved verbatim. | 26020-Package_Requirements.docx package heading 50, Scope Notes / Open Items |
| Interface check | All nine YES interfaces from `INTERFACE_REGISTER.csv` for `PKG-098` appear with exact register names. | `INTERFACE_REGISTER.csv` |
| Artifact check | All anticipated datasheet, vendor handoff, interface matrix, tagged equipment evidence, and interface fact evidence artifacts are represented. | `ARTIFACT_REGISTER.csv` |
| Objective check | `OBJ-002` through `OBJ-010` are included as context only. | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` |
| Source gap check | Unsupported design values, codes, materials, and capacity/driver remain `TBD` or are routed to the Guidance Conflict Table. | 26020-Package_Requirements.docx package heading 50; `_REFERENCES.md` |

## Records

- `Datasheet.md`
- `Specification.md`
- `Guidance.md`
- `Procedure.md`
- `_STATUS.md`
- `_run_records/TASK_RUN_2026-05-25_<HHMM>.md`
- Future human ruling records for `HRR-098-02-001` through `HRR-098-02-004`, if resolved.
