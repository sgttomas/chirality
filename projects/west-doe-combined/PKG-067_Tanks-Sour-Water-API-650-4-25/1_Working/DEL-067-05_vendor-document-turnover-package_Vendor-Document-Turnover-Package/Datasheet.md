# Datasheet — DEL-067-05 Vendor Document Turnover Package (PKG-067 Tanks, Sour Water (API 650) 4-25)

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-067-05_vendor-document-turnover-package` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Deliverable Name | Vendor Document Turnover Package | `DELIVERABLE_REGISTER.csv` |
| Parent Package | `PKG-067` — Tanks, Sour Water (API 650) 4-25 | `PACKAGE_REGISTER.csv` row 94 |
| Workbook Row | 94 | `PACKAGE_REGISTER.csv` |
| WBS | 01 | `PACKAGE_REGISTER.csv` |
| CoA Tracking Number | 26020-01-19-005 (normalized: 26020-01-19-005; also reported as `26020-01-PT-19-005 - Tanks, Sour Water`) | `PACKAGE_REGISTER.csv` |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Deliverable Type | Vendor Document Turnover | `DELIVERABLE_REGISTER.csv` |
| Responsible Party | Package Vendor (vendor documentation) with EPC Integrator interface/integration review | `DELIVERABLE_REGISTER.csv` |
| Vendor-Owned Package | TRUE | `PACKAGE_REGISTER.csv` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Package Equipment Documented | Two produced-water / sour-water API-650 storage tanks (4-25 service): `TK-9010-1`, `TK-9020-1` (PRODUCED WATER STORAGE TANK x2) — ASSUMPTION (tag mapping derived from 4-25 Deepcut DBM tank list; package register row 94 names "Tanks, Sour Water (API 650) 4-25" and confirms two-tank scope per analog 3-25 sour water tank pair) | `4-25_Deepcut_DBM.md` (tank-list rows 90/99 region — line/section TBD); `PACKAGE_REGISTER.csv` row 94 ScopeDescription |
| Tank Specification Basis | Modified API 650 (per 4-25 DBM tank specification line entry) | `4-25_Deepcut_DBM.md` — "Condensate tank specification | Modified API 650" (section TBD; applicable to API-650 atmospheric tanks; tank-pair specification confirmation TBD pending sour-water-specific source slice) |
| Covered Scope Items | SOW-0225; SOW-0226; SOW-0227; SOW-0228 | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported Objectives | OBJ-001; OBJ-003; OBJ-004; OBJ-005; OBJ-006; OBJ-007; OBJ-008; OBJ-009; OBJ-010 (ASSUMPTION — package-heuristic association per `OBJECTIVE_ASSOCIATION_MODE=PACKAGE_HEURISTIC`) | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` |
| Document Owner | Package Vendor | `DELIVERABLE_REGISTER.csv` ResponsibleParty |
| Document Reviewer | EPC Integrator (interface/integration review) | `DELIVERABLE_REGISTER.csv` ResponsibleParty |
| Anticipated Artifacts | Vendor document register; vendor document submittals; source vendor document table rows as artifacts where available; turnover records | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` AnticipatedArtifacts |
| Source Document Inventory | TBD — required vendor documents list resides in `26020-Package_Requirements.docx` package heading 22 (location TBD; binary source not converted to text) and Workbook Packages row 94 vendor-documentation columns (location TBD; binary source not converted to text) | `_REFERENCES.md`; `PACKAGE_REGISTER.csv` SourceRefs |
| Analog Reference | Bid Docs / Budgetary RFQ for 3-25 sour water tanks: `26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx` and its working brief (analog basis only; no direct 4-25 package-folder brief, DOCX, or PDF scope source) | `PACKAGE_REGISTER.csv` row 94 SourceRefs |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Sour water / produced water atmospheric storage (4-25 process area) | `PACKAGE_REGISTER.csv` row 94 ScopeDescription; `4-25_Deepcut_DBM.md` tank-list (section TBD) |
| Lifecycle of submittals | Submittals span engineering/design phase through fabrication, FAT/site testing, shipment, and post-installation turnover (ASSUMPTION based on standard EPC/vendor practice) | location TBD — `26020-Package_Requirements.docx` package heading 22 |
| Required document categories | TBD — categories (e.g., tank datasheets, foundation interface drawings, general arrangement drawings, weld procedures, materials certificates, NDE records including bottom and shell weld inspection, hydrostatic test records, coating/lining records, API-650 nameplate/data report, OEM operation and maintenance manuals, spare parts lists) are project-defined and reside in `26020-Package_Requirements.docx` package heading 22 (location TBD) | `_REFERENCES.md` |
| Format / submission medium | TBD — electronic transmittal format, file naming, and document index conventions to be set per EPC project document control standard (location TBD) | location TBD |
| Review cycles | TBD — vendor submittal review codes and resubmittal expectations to be defined per project document control procedure (location TBD) | location TBD |
| Turnover trigger | Completion of tank shop fabrication or field-erection acceptance, hydrostatic testing, and shipment/installation milestones with final as-built record set (ASSUMPTION) | location TBD |
| Sour service considerations | Material selection, coating/lining, and weld procedure documentation may be governed by sour-service requirements (NACE MR0175 / ISO 15156) — ASSUMPTION; applicability and required documentation TBD pending source confirmation | location TBD |

## Construction

| Item | Value | Source |
|---|---|---|
| Document Register Structure | TBD — register columns (Doc No., Title, Vendor Code, Discipline, Equipment Tag, Required-By date, Submittal status, Review code, Resubmittal count, Final-for-turnover flag) to be defined per project document control standard (location TBD) | `_REFERENCES.md` |
| Source vendor document rows | Individual source document table rows are evidence/artifacts of this deliverable, not separate deliverables | `_CONTEXT.md` Notes; `DELIVERABLE_REGISTER.csv` Notes |
| Turnover record format | TBD — final transmittal manifest with hand-over signature/acceptance fields; location TBD | location TBD |
| Equipment tags covered | `TK-9010-1` and `TK-9020-1` (PRODUCED WATER STORAGE TANKS, x2) — ASSUMPTION (tag derivation from 4-25 Deepcut DBM tank list region) | `4-25_Deepcut_DBM.md` (line/section TBD); `PACKAGE_REGISTER.csv` row 94 |

## References

- `_CONTEXT.md` — deliverable identity, scope, objectives
- `_REFERENCES.md` — accepted upstream snapshot + source materials list
- `DELIVERABLE_REGISTER.csv` (Gate 7 snapshot) — DEL-067-05 row
- `PACKAGE_REGISTER.csv` (Gate 7 snapshot) — package row 94 (PKG-067)
- `OBJECTIVE_DELIVERABLE_MAP.csv` (Gate 7 snapshot) — objective-to-deliverable rows for DEL-067-05
- `26020-Package_Requirements.docx` package heading 22 — vendor documentation requirements (location TBD; binary source not converted to text)
- `26020-Packages_Interfaces_4_export.xlsx` Workbook Packages row 94 — vendor-documentation columns (location TBD; binary source not converted to text)
- `/Users/ryan/ai-env/projects/chirality/projects/west-doe-combined/_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` — Deepcut DBM, sour water tank tag/configuration context
- Analog: `26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx` (3-25 sour water tanks RFQ) — analog basis only
