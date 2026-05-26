# Datasheet: DEL-098-02 Package Datasheet

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | DEL-098-02_package-datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-098-02_package-datasheet` |
| Deliverable name | Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-098-02_package-datasheet` |
| Parent package | PKG-098 — Tanks, Sour Water (API 650) 3-25 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row `PKG-098` |
| Workbook ID / row | 98 / row 93 | `PACKAGE_REGISTER.csv` row `PKG-098` |
| WBS | 03 | `PACKAGE_REGISTER.csv` row `PKG-098` |
| CoA tracking number | 26020-03-19-007 | `PACKAGE_REGISTER.csv` row `PKG-098` |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row `PKG-098` |
| Responsible party | EPC Integrator | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-098-02_package-datasheet` |
| Deliverable type | EPC Package Datasheet | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row `DEL-098-02_package-datasheet` |
| Covered scope items | SOW-0221; SOW-0222; SOW-0223; SOW-0224 | `_CONTEXT.md`; `SCOPE_LEDGER.csv` rows `SOW-0221`–`SOW-0224` |
| Word source basis | 26020-Package_Requirements.docx package heading 50 — "26020-03-PT-19-007 - Tanks, Sour Water" | `PACKAGE_REGISTER.csv` row `PKG-098`; `_REFERENCES.md` |
| Underlying vendor source | Bid Docs/Budgetary/26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx (referenced as Source Basis in Word section) | 26020-Package_Requirements.docx package heading 50, Source Basis line |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package scope statement | Vendor-responsible Mechanical package "Tanks, Sour Water (API 650) 3-25" carried as a distinct flat project package for WBS 03. | `SCOPE_LEDGER.csv` row `SOW-0221` |
| Basic scope | Item No. 1: Three (3) 3800 bbl Sour Produced Water Storage Tanks (TK-9030-2, TK-9040-2, TK-9050-2). Process function: Sour Water Tanks. | 26020-Package_Requirements.docx package heading 50, Basic Scope; `SCOPE_LEDGER.csv` row `SOW-0222` |
| Major included equipment | Item No. 1: Three (3) 3800 bbl Sour Produced Water Storage Tanks (TK-9030-2, TK-9040-2, TK-9050-2); Item No. 2: Two (2) 3800 bbl Sour Inlet Produced Water Storage Tanks (TK-9010-2, TK-9020-2); Item No. 3: Two (2) 3800 bbl Produced Water Storage Tanks (TK-9010-1, TK-9020-1). | 26020-Package_Requirements.docx package heading 50, Major Included Equipment; `ARTIFACT_REGISTER.csv` artifact `ART-914A0B9939`; `SCOPE_LEDGER.csv` row `SOW-0223` |
| Common construction features (Items 1–3) | Design and fabrication to modified API 650; internal coating Devchem 253 applied to floor, walls, and roof; external insulation with electric heating; Kennilworth type HCL float skim system, one per tank. | 26020-Package_Requirements.docx package heading 50, Major Included Equipment; `SCOPE_LEDGER.csv` row `SOW-0223` |
| Datasheet purpose | Integrator-authored technical handoff data required for third-party package engineering and design. | `ARTIFACT_REGISTER.csv` artifact `ART-1458F2586B` |
| Vendor engineering handoff basis | Technical basis, battery limits, design expectations, and source-supported requirements to be handed to the package delivery entity. | `ARTIFACT_REGISTER.csv` artifact `ART-F958B0973F` |
| Interface requirements matrix | Workbook interface facts carried as datasheet evidence for third-party engineering/design handoff. | `ARTIFACT_REGISTER.csv` artifact `ART-119F7B5D2B` |
| Interface fact — Process Piping | Applicable: YES | `INTERFACE_REGISTER.csv` row `IFC-A66F4C4FA5`; `ARTIFACT_REGISTER.csv` artifact `ART-6F284ED097`; 26020-Package_Requirements.docx package heading 50, Physical Interface Summary |
| Interface fact — Relief / Flare / Vent | Applicable: YES | `INTERFACE_REGISTER.csv` row `IFC-DAF44D294E`; `ARTIFACT_REGISTER.csv` artifact `ART-2B9D5C42C7`; 26020-Package_Requirements.docx package heading 50, Physical Interface Summary |
| Interface fact — Drain / Containment | Applicable: YES | `INTERFACE_REGISTER.csv` row `IFC-179837C546`; `ARTIFACT_REGISTER.csv` artifact `ART-274EC84FD3`; 26020-Package_Requirements.docx package heading 50, Physical Interface Summary |
| Interface fact — Grounding / Bonding | Applicable: YES | `INTERFACE_REGISTER.csv` row `IFC-F56BBD79A8`; `ARTIFACT_REGISTER.csv` artifact `ART-5714AEE300`; 26020-Package_Requirements.docx package heading 50, Physical Interface Summary |
| Interface fact — Area / Exterior Lighting | Applicable: YES | `INTERFACE_REGISTER.csv` row `IFC-BF1F96F8F1`; `ARTIFACT_REGISTER.csv` artifact `ART-62DD9E5732`; 26020-Package_Requirements.docx package heading 50, Physical Interface Summary |
| Interface fact — Cathodic Protection | Applicable: YES | `INTERFACE_REGISTER.csv` row `IFC-9E5DB860CB`; `ARTIFACT_REGISTER.csv` artifact `ART-FD3CEF57E1`; 26020-Package_Requirements.docx package heading 50, Physical Interface Summary |
| Interface fact — I&C / Control Cabling | Applicable: YES | `INTERFACE_REGISTER.csv` row `IFC-A3605A8A7A`; `ARTIFACT_REGISTER.csv` artifact `ART-164D49B018`; 26020-Package_Requirements.docx package heading 50, Physical Interface Summary |
| Interface fact — Grading / Site Drainage / Spill Containment | Applicable: YES | `INTERFACE_REGISTER.csv` row `IFC-7E4BCEA8B5`; `ARTIFACT_REGISTER.csv` artifact `ART-27066C3306`; 26020-Package_Requirements.docx package heading 50, Physical Interface Summary |
| Interface fact — Structural / Foundations / Supports | Applicable: YES | `INTERFACE_REGISTER.csv` row `IFC-EB5309AFE1`; `ARTIFACT_REGISTER.csv` artifact `ART-FE9E7CD9A0`; 26020-Package_Requirements.docx package heading 50, Physical Interface Summary |
| Responsibility model | Package Vendor owns package engineering, package design, vendor documentation, and the physical equipment package. EPC Integrator owns integration into the functional process facility, including interfaces, tie-ins, constructability, procurement/construction coordination, and facility-level integration. | `PACKAGE_REGISTER.csv` row `PKG-098`; `SCOPE_LEDGER.csv` row `SOW-0221` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Operating pressure | Atmospheric | 26020-Package_Requirements.docx package heading 50, Scope Notes / Open Items; `SCOPE_LEDGER.csv` row `SOW-0224` |
| Operating temperature (Items 1 and 3) | 10 °C | 26020-Package_Requirements.docx package heading 50, Scope Notes / Open Items; `SCOPE_LEDGER.csv` row `SOW-0224` |
| Operating temperature (Item No. 2) | TBD | 26020-Package_Requirements.docx package heading 50, Scope Notes / Open Items; `SCOPE_LEDGER.csv` row `SOW-0224` |
| Design pressure | 32 oz test pressure | 26020-Package_Requirements.docx package heading 50, Scope Notes / Open Items; `SCOPE_LEDGER.csv` row `SOW-0224` |
| Design temperature range | -40 °C (min) and 60 °C (max) | 26020-Package_Requirements.docx package heading 50, Scope Notes / Open Items; `SCOPE_LEDGER.csv` row `SOW-0224` |
| Capacity / design throughput | "See attached in Appendix A" — Appendix A not locally accessible (TBD) | 26020-Package_Requirements.docx package heading 50, Scope Notes / Open Items; `SCOPE_LEDGER.csv` row `SOW-0224` |
| Driver | TBD | 26020-Package_Requirements.docx package heading 50, Scope Notes / Open Items; `SCOPE_LEDGER.csv` row `SOW-0224` |
| Service category | Sour service (sour produced water; H2S-bearing) | 26020-Package_Requirements.docx package heading 50, Basic Scope and Major Included Equipment (ASSUMPTION: H2S characterization not stated at this heading; sour service is named explicitly) |
| Location / status | 3-25 liquids area and related compressor station scope; vetted package scope basis. | 26020-Package_Requirements.docx package heading 50, Location / Status |
| Objective context | OBJ-002, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 are mapped to this deliverable. | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-098-02_package-datasheet` |
| Declared upstream dependencies | None declared. | `_DEPENDENCIES.md` |
| Declared downstream dependencies | None declared. | `_DEPENDENCIES.md` |

## Construction

| Item | Value | Source |
|---|---|---|
| Design and fabrication standard | Modified API 650 | 26020-Package_Requirements.docx package heading 50, Major Included Equipment; `SCOPE_LEDGER.csv` row `SOW-0223` |
| Internal coating | Devchem 253 applied to floor, walls, and roof | 26020-Package_Requirements.docx package heading 50, Major Included Equipment; `SCOPE_LEDGER.csv` row `SOW-0223` |
| External insulation | External insulation with electric heating | 26020-Package_Requirements.docx package heading 50, Major Included Equipment; `SCOPE_LEDGER.csv` row `SOW-0223` |
| Skim system | Kennilworth type HCL float skim system, one per tank | 26020-Package_Requirements.docx package heading 50, Major Included Equipment; `SCOPE_LEDGER.csv` row `SOW-0223` |
| Items by others (excluded from vendor package) | Foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase, etc. | 26020-Package_Requirements.docx package heading 50, Scope Notes / Open Items; `SCOPE_LEDGER.csv` row `SOW-0224` |
| Construction-facing companion deliverable | DEL-098-03_construction-work-package | `DELIVERABLE_REGISTER.csv` row `DEL-098-03_construction-work-package` |
| Vendor equipment companion deliverable | DEL-098-04_vendor-engineered-equipment-package | `DELIVERABLE_REGISTER.csv` row `DEL-098-04_vendor-engineered-equipment-package` |
| Vendor document turnover companion deliverable | DEL-098-05_vendor-document-turnover-package | `DELIVERABLE_REGISTER.csv` row `DEL-098-05_vendor-document-turnover-package` |
| Detailed vendor engineering deliverable set | Listed in 26020-Package_Requirements.docx package heading 50, Vendor Engineering Deliverables table; carried forward through DEL-098-04 and DEL-098-05 — not enumerated in this datasheet. | 26020-Package_Requirements.docx package heading 50, Vendor Engineering Deliverables |
| Material/metallurgy selections, plate thicknesses, nozzle schedule, anchor design | TBD — not stated at package heading 50; expected in vendor package engineering. | Source gap from 26020-Package_Requirements.docx package heading 50 |
| H2S concentration and NACE compliance details | TBD — not stated at package heading 50 (heading 50 names sour service but does not record NACE compliance text as the analog Sour Condensate section does). | Source gap from 26020-Package_Requirements.docx package heading 50; `_REFERENCES.md` |
| Codes and standards beyond modified API 650 | TBD — additional codes (API 2000, NACE, electric heat trace, internal coating qualification) not enumerated at package heading 50. | Source gap from 26020-Package_Requirements.docx package heading 50 |

## References

- `_CONTEXT.md`
- `_DEPENDENCIES.md`
- `_REFERENCES.md`
- Gate 7 final published `PROJECT_DECOMP.md`
- Gate 7 final published `PACKAGE_REGISTER.csv` row `PKG-098`
- Gate 7 final published `DELIVERABLE_REGISTER.csv` row `DEL-098-02_package-datasheet`
- Gate 7 final published `ARTIFACT_REGISTER.csv` artifacts for `DEL-098-02_package-datasheet`
- Gate 7 final published `INTERFACE_REGISTER.csv` rows for `PKG-098`
- Gate 7 final published `OBJECTIVE_REGISTER.csv` rows `OBJ-002` through `OBJ-010`
- Gate 7 final published `OBJECTIVE_DELIVERABLE_MAP.csv` rows for `DEL-098-02_package-datasheet`
- Gate 7 final published `SCOPE_LEDGER.csv` rows `SOW-0221` through `SOW-0224`
- `_Sources/26020-Package_Requirements.docx`, package heading 50 ("26020-03-PT-19-007 - Tanks, Sour Water")
