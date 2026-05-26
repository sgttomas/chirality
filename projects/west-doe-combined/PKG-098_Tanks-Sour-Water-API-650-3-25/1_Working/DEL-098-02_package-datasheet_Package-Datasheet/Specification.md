# Specification: DEL-098-02 Package Datasheet

## Scope

This specification governs the EPC Integrator package datasheet for `PKG-098` Tanks, Sour Water (API 650) 3-25. The datasheet is the mandatory technical handoff deliverable for `DEL-098-02_package-datasheet` and must carry source-supported package data for third-party vendor package engineering and design.

Included scope:

- Package identity and handoff basis for `PKG-098`, workbook ID 98, workbook row 93, WBS 03, CoA tracking number `26020-03-19-007`.
- The scope items `SOW-0221`, `SOW-0222`, `SOW-0223`, and `SOW-0224` covering vendor-package responsibility split, basic scope, major included equipment, and scope notes/open items.
- Process and integration interface facts for Process Piping; Relief / Flare / Vent; Drain / Containment; Grounding / Bonding; Area / Exterior Lighting; Cathodic Protection; I&C / Control Cabling; Grading / Site Drainage / Spill Containment; Structural / Foundations / Supports.
- Major included equipment list and common construction features (Items 1–3) as stated at 26020-Package_Requirements.docx package heading 50.
- Operating and design conditions as stated in the Scope Notes / Open Items block of package heading 50.
- Objective context for `OBJ-002` through `OBJ-010`.

Excluded scope:

- Vendor package engineering, package design, vendor documentation, and physical equipment supply (owned by the Package Vendor and tracked in `DEL-098-04_vendor-engineered-equipment-package` and `DEL-098-05_vendor-document-turnover-package`).
- Detailed construction, installation, tie-in, inspection, and turnover content that belongs in `DEL-098-03_construction-work-package`.
- Items explicitly "by others" at the package heading (foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase, etc.).
- Design values, codes, and detailed engineering not supported by package heading 50 or the Gate 7 accepted registers.

Sources: `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row `PKG-098`; `DELIVERABLE_REGISTER.csv` row `DEL-098-02_package-datasheet`; `SCOPE_LEDGER.csv` rows `SOW-0221`–`SOW-0224`; `INTERFACE_REGISTER.csv` rows for `PKG-098`; `ARTIFACT_REGISTER.csv` artifacts for `DEL-098-02_package-datasheet`; 26020-Package_Requirements.docx package heading 50.

## Requirements

| Requirement ID | Requirement | Source | Verification |
|---|---|---|---|
| REQ-098-02-001 | The datasheet must identify `PKG-098` as Tanks, Sour Water (API 650) 3-25, workbook ID 98, workbook row 93, WBS 03, discipline Mechanical, and CoA tracking number `26020-03-19-007`. | `PACKAGE_REGISTER.csv` row `PKG-098` | Datasheet identity table check |
| REQ-098-02-002 | The datasheet must identify the responsible party as EPC Integrator and the deliverable type as EPC Package Datasheet. | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-098-02_package-datasheet` | Datasheet identity table check |
| REQ-098-02-003 | The datasheet must carry `SOW-0221`, `SOW-0222`, `SOW-0223`, and `SOW-0224` as the covered scope items. | `_CONTEXT.md`; `SCOPE_LEDGER.csv` rows `SOW-0221`–`SOW-0224` | Scope traceability check |
| REQ-098-02-004 | The datasheet must state the Package Vendor / EPC Integrator responsibility split exactly as recorded in `PACKAGE_REGISTER.csv` row `PKG-098`. | `PACKAGE_REGISTER.csv` row `PKG-098`; `SCOPE_LEDGER.csv` row `SOW-0221` | Responsibility wording check |
| REQ-098-02-005 | The datasheet must record the Basic Scope: three (3) 3800 bbl Sour Produced Water Storage Tanks (TK-9030-2, TK-9040-2, TK-9050-2) with process function Sour Water Tanks. | 26020-Package_Requirements.docx package heading 50, Basic Scope; `SCOPE_LEDGER.csv` row `SOW-0222` | Datasheet attributes check |
| REQ-098-02-006 | The datasheet must record the Major Included Equipment exactly as stated, including Items 1–3 (tag counts and tag numbers) and the common construction features (modified API 650 design and fabrication; Devchem 253 internal coating on floor, walls, roof; external insulation with electric heating; Kennilworth type HCL float skim system, one per tank). | 26020-Package_Requirements.docx package heading 50, Major Included Equipment; `SCOPE_LEDGER.csv` row `SOW-0223`; `ARTIFACT_REGISTER.csv` artifact `ART-914A0B9939` | Datasheet attributes/construction check |
| REQ-098-02-007 | The datasheet must record the operating and design conditions exactly as stated: operating pressure Atmospheric; operating temperature 10 °C with Item No. 2 TBD; design pressure 32 oz test pressure; design temperature -40 °C (min) and 60 °C (max). | 26020-Package_Requirements.docx package heading 50, Scope Notes / Open Items; `SCOPE_LEDGER.csv` row `SOW-0224` | Datasheet conditions check |
| REQ-098-02-008 | The datasheet must record the "by others" exclusions exactly as stated (foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase, etc.). | 26020-Package_Requirements.docx package heading 50, Scope Notes / Open Items; `SCOPE_LEDGER.csv` row `SOW-0224` | Datasheet construction check |
| REQ-098-02-009 | The datasheet must include all nine package interface facts named in `INTERFACE_REGISTER.csv` for `PKG-098`, with names spelled exactly as in the register. | `INTERFACE_REGISTER.csv` rows for `PKG-098`; 26020-Package_Requirements.docx package heading 50, Physical Interface Summary | Interface matrix check |
| REQ-098-02-010 | The datasheet must include the three EPC handoff artifacts (package technical datasheet, vendor engineering handoff basis, package interface requirements matrix) and the tagged equipment evidence artifact. | `ARTIFACT_REGISTER.csv` artifacts `ART-1458F2586B`, `ART-F958B0973F`, `ART-119F7B5D2B`, `ART-914A0B9939` | Artifact coverage check |
| REQ-098-02-011 | The datasheet must expose the mapped objective context for `OBJ-002` through `OBJ-010` without treating objective statements as clause-level mechanical or process design criteria. | `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-098-02_package-datasheet`; `OBJECTIVE_REGISTER.csv` | Objective traceability check |
| REQ-098-02-012 | Any unsupported design values, material/metallurgy selections, plate thicknesses, nozzle schedules, code clauses beyond modified API 650, NACE/H2S details, capacity/throughput (Appendix A), and driver selection must remain `TBD`, not inferred. | 26020-Package_Requirements.docx package heading 50, Scope Notes / Open Items; `_REFERENCES.md` Missing / Deferred References | Source gap review |

## Standards

| Standard / basis | Status | Source |
|---|---|---|
| Modified API 650 | Named at package heading 50 as the design and fabrication basis for Items 1–3. Modifications not enumerated at this heading (TBD). | 26020-Package_Requirements.docx package heading 50, Major Included Equipment |
| Gate 7 final published PROJECT_DECOMP snapshot | Governing accepted decomposition truth for this run. | `_REFERENCES.md`; Gate 7 `PROJECT_DECOMP.md` |
| Workbook Packages row 93 | Accepted source reference for package identity, workbook row, responsibility model, interface facts, and source references. | `PACKAGE_REGISTER.csv` row `PKG-098`; `INTERFACE_REGISTER.csv` rows for `PKG-098` |
| 26020-Package_Requirements.docx package heading 50 | Accepted package-requirements source for basic scope, major included equipment, scope notes/open items, physical interface summary, and vendor engineering deliverables. | `_REFERENCES.md`; `ARTIFACT_REGISTER.csv` artifacts citing heading 50 |
| 26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx (Bid Docs/Budgetary) | Underlying vendor RFQ named as Source Basis at heading 50. Not locally accessible (location TBD). | 26020-Package_Requirements.docx package heading 50, Source Basis line |
| API 2000 (tank venting), NACE MR0175/MR0103 (sour service), coating qualification, electric heat-trace standards | Applicability is likely (ASSUMPTION) given sour service, atmospheric storage, internal coating, and electric heating, but not named at package heading 50 (location TBD). | 26020-Package_Requirements.docx package heading 50, Major Included Equipment; source gap |
| Appendix A — Capacity / design throughput | Referenced at package heading 50 but not locally accessible (location TBD). | 26020-Package_Requirements.docx package heading 50, Scope Notes / Open Items |

## Verification

| Check | Method | Acceptance |
|---|---|---|
| Identity completeness | Compare Datasheet Identification against `PACKAGE_REGISTER.csv` and `DELIVERABLE_REGISTER.csv`. | All listed identity fields match accepted Gate 7 rows. |
| Scope traceability | Compare covered scope item list against `_CONTEXT.md` and `SCOPE_LEDGER.csv`. | `SOW-0221` through `SOW-0224` are all present. |
| Responsibility check | Compare responsibility model wording against `PACKAGE_REGISTER.csv` row `PKG-098`. | Vendor-versus-EPC split is reproduced without paraphrase changes that alter ownership. |
| Equipment list check | Compare Major Included Equipment against package heading 50. | All three Items (tag counts and tag numbers) and the four common construction features appear verbatim. |
| Conditions check | Compare operating and design conditions against package heading 50. | Pressure, temperature, design pressure, design temperature, and Item No. 2 TBD all present. |
| Interface matrix check | Compare Datasheet interface list against `INTERFACE_REGISTER.csv` rows for `PKG-098`. | All nine YES interfaces present with exact register names; no additional interfaces invented. |
| Artifact coverage | Compare Datasheet attributes/construction against `ARTIFACT_REGISTER.csv`. | Datasheet includes EPC handoff artifacts and the tagged equipment evidence artifact. |
| Objective traceability | Compare mapped objectives against `_CONTEXT.md` and `OBJECTIVE_DELIVERABLE_MAP.csv`. | `OBJ-002` through `OBJ-010` are present as context only. |
| Source gap control | Review all technical values and codes. | Unsupported values (Appendix A capacity, driver, Item No. 2 temperature, additional codes, H2S/NACE specifics, materials, plate thicknesses) remain `TBD` or are explicitly labeled ASSUMPTION. |

## Documentation

Required deliverable artifacts:

- Package technical datasheet (`ART-1458F2586B`).
- Vendor engineering handoff basis (`ART-F958B0973F`).
- Package interface requirements matrix (`ART-119F7B5D2B`).
- Source-supported equipment and design criteria, including tagged equipment evidence (`ART-914A0B9939`).
- Interface fact evidence artifacts for all nine applicable interfaces (`ART-6F284ED097`, `ART-2B9D5C42C7`, `ART-274EC84FD3`, `ART-5714AEE300`, `ART-62DD9E5732`, `ART-FD3CEF57E1`, `ART-164D49B018`, `ART-27066C3306`, `ART-FE9E7CD9A0`).

Supporting records:

- Gate 7 final published snapshot references used for traceability.
- 26020-Package_Requirements.docx package heading 50 source slices.
- List of unresolved `TBD` technical values and standards (Appendix A capacity, Item No. 2 operating temperature, driver, modifications to API 650, additional codes, NACE/H2S specifics, materials/metallurgy).
- Any future human rulings recorded in `Guidance.md` Conflict Table.
