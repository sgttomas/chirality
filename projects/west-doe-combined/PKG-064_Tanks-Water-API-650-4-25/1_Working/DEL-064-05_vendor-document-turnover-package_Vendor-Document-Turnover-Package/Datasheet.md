# Datasheet — DEL-064-05 Vendor Document Turnover Package (PKG-064 Tanks, Water (API 650) 4-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-064-05_vendor-document-turnover-package` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable Name | Vendor Document Turnover Package | `DELIVERABLE_REGISTER.csv` |
| Parent Package | `PKG-064` — Tanks, Water (API 650) 4-25 | `PACKAGE_REGISTER.csv` row 96 |
| Workbook Row | 96 | `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-01-19-002 (also reported as 26020-01-PT-19-002 — Tanks, Water) | `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable Type | Vendor Document Turnover | `DELIVERABLE_REGISTER.csv` |
| Responsible Party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `DELIVERABLE_REGISTER.csv` |
| Vendor-Owned Package | TRUE | `PACKAGE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Equipment Documented | Two (2) Process Water Storage Tanks: `TK-5317-1`, `TK-5318-1` (each 2,000 bbl, modified API-650 atmospheric, externally insulated, heated, internally coated) | `PACKAGE_REGISTER.csv` row 96 (Basic scope); `4-25_Deepcut_DBM.md` lines 493, 518, 524, 2628 |
| Process Function | Sweet Produced Water & Process Water storage | `PACKAGE_REGISTER.csv` row 96 (Basic scope) |
| Covered Scope Items | SOW-0233; SOW-0234; SOW-0235; SOW-0236 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported Objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` (ASSUMPTION — best-effort package-grouping mapping per skill default) |
| Document Owner | Package Vendor | `DELIVERABLE_REGISTER.csv` ResponsibleParty |
| Document Reviewer | EPC Integrator (interface/integration review) | `DELIVERABLE_REGISTER.csv` ResponsibleParty |
| Anticipated Artifacts | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` AnticipatedArtifacts |
| Source Document Inventory | TBD — list of required vendor documents resides in `26020-Package_Requirements.docx` package heading 19 (location TBD; binary source not converted to text) and the vendor-documentation columns of Workbook Packages row 96 (location TBD) | `_REFERENCES.md`; `PACKAGE_REGISTER.csv` SourceRefRaw |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Lifecycle of submittals | Submittals span engineering/design phase through fabrication, FAT (where applicable for shop-fabricated subcomponents), shipment, field erection (API-650 tanks are field-erected), and post-installation turnover (ASSUMPTION — standard EPC/vendor practice for field-erected atmospheric tanks) | location TBD — `26020-Package_Requirements.docx` package heading 19 |
| Required document categories | TBD — categories (e.g., design calculations, fabrication drawings, weld procedures and qualifications (WPS/PQR/WPQ), materials test reports, NDE records, hydrotest/leak-test records, coating system records, insulation records, heat-trace records, OEM operating and maintenance manuals, spare parts lists) are project-defined and reside in `26020-Package_Requirements.docx` package heading 19 (location TBD) | `_REFERENCES.md` |
| Format / submission medium | TBD — electronic transmittal format, file naming, and document index conventions to be set per EPC project document control standard (location TBD) | location TBD |
| Review cycles | TBD — vendor submittal review codes and resubmittal expectations to be defined per project document control procedure (location TBD) | location TBD |
| Turnover trigger | Completion of tank field erection, hydrotest, coating, insulation, heat tracing commissioning, and acceptance with final as-built record set (ASSUMPTION) | location TBD |
| Construction context for documentation | API-650 atmospheric tanks; per DBM, water tanks shall be insulated to prevent winter freezing | `4-25_Deepcut_DBM.md` lines 518, 524, 2509 |

## Construction

| Item | Value | Source |
|---|---|---|
| Document Register Structure | TBD — register columns (Doc No., Title, Vendor Code, Discipline, Equipment Tag (`TK-5317-1`/`TK-5318-1`), Required-By date, Submittal status, Review code, Resubmittal count, Final-for-turnover flag) to be defined per project document control standard (location TBD) | `_REFERENCES.md` |
| Source vendor document rows | Individual source document table rows in Workbook Packages row 96 are evidence/artifacts of this deliverable, not separate deliverables | `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` Notes |
| Turnover record format | TBD — final transmittal manifest with hand-over signature/acceptance fields; location TBD | location TBD |
| Equipment tags covered | `TK-5317-1`, `TK-5318-1` (PROCESS WATER STORAGE TANK x2, 4-25) | `4-25_Deepcut_DBM.md` line 2628 |
| API-650 code-package items | Modified API-650 atmospheric tanks designed for 16 oz test pressure; jurisdictional code documentation per applicable provincial registration (ASSUMPTION on jurisdictional registration scope) | `4-25_Deepcut_DBM.md` line 518 |

## References

- `_CONTEXT.md` — deliverable identity, scope, objectives
- `_REFERENCES.md` — accepted upstream snapshot + source materials list
- `DELIVERABLE_REGISTER.csv` (Gate 7 snapshot) — deliverable row for `DEL-064-05`
- `PACKAGE_REGISTER.csv` (Gate 7 snapshot) — package row 96 (PKG-064)
- `OBJECTIVE_DELIVERABLE_MAP.csv` (Gate 7 snapshot) — objective-to-deliverable rows for `DEL-064-05`
- `26020-Package_Requirements.docx` package heading 19 — vendor documentation requirements (location TBD; binary source not converted to text)
- `26020-Packages_Interfaces_4_export.xlsx` Workbook Packages row 96 — vendor-documentation columns (location TBD; binary source not converted to text)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Deepcut DBM, process water tank tags/configuration context (lines 493, 508, 518, 524, 2509, 2628)
