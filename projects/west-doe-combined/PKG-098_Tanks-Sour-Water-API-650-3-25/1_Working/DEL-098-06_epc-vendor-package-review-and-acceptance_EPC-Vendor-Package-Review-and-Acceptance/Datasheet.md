# Datasheet — DEL-098-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-098-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-098` (Tanks, Sour Water, API 650 — 3-25) |
| Workbook Package row | 93 [SourcePath: `_Sources/26020-Packages_Interfaces_4_export.xlsx`; SectionRef: row 93 — referenced by `_CONTEXT.md`] |
| Package Requirements heading | "26020-03-PT-19-007 - Tanks, Sour Water" [SourcePath: `_Sources/26020-Package_Requirements.docx`; SectionRef: package heading 50] |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance (review-and-acceptance deliverable, not a vendor-engineered artifact) |
| ResponsibleParty | EPC Integrator (lead); Package Vendor (input) |
| Covers Scope Items | `SOW-0221`, `SOW-0222`, `SOW-0223`, `SOW-0224` [from `_CONTEXT.md`] |
| Supports Objectives | `OBJ-002`..`OBJ-010` [from `_CONTEXT.md`; ASSUMPTION — package-heuristic association] |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Subject package | Three (3) 3800 bbl Sour Produced Water Storage Tanks (TK-9030-2, TK-9040-2, TK-9050-2); Two (2) 3800 bbl Sour Inlet Produced Water Storage Tanks (TK-9010-2, TK-9020-2); Two (2) 3800 bbl Produced Water Storage Tanks (TK-9010-1, TK-9020-1) | `_Sources/26020-Package_Requirements.docx` heading 50, "Major Included Equipment" |
| Process function | Sour Water Tanks (atmospheric storage) | `_Sources/26020-Package_Requirements.docx` heading 50, "Basic Scope" |
| Design code basis | API 650 (modified atmospheric storage) | ASSUMPTION — implied by PackageName "Tanks, Sour Water (API 650) 3-25" and analog 4-25 entry naming API 650 modified atmospheric; package-50 entry itself does not restate clause-level. [SourcePath: `_Sources/26020-Package_Requirements.docx`; SectionRef: heading 50 / analog heading 51 paragraph 5240] |
| Operating conditions | Pressure: Atmospheric; Temperature: 10 °C; further conditions TBD | `_Sources/26020-Package_Requirements.docx` heading 50, "Scope Notes / Open Items" |
| By-others scope (excluded from vendor) | Foundations, mounting tanks at site, electrical/instrumentation, platforms, staircase | Same source, "Scope Notes / Open Items" |
| Capacity / design throughput | "See attached in Appendix A" — TBD (Appendix A not in package-requirements slice read) | Same source, "Scope Notes / Open Items" |
| Driver | TBD | Same source |
| Acceptance subject artifacts | Vendor document index, ITP, MTRs, Inspection Release Certificate, FAT report, Vendor Data Book, GA / installation drawings, equipment data sheets, calculation package | `_Sources/26020-Package_Requirements.docx` heading 50, "Vendor Engineering Deliverables" list (PRQ-009, DOC-008, QLT-006, QLT-003, QLT-013, QLT-020, QLT-021, PRQ-013, PRQ-015, PRQ-016, MEC-001..MEC-025, MEC-005, MEC-011, PRO-014..PRO-018, PIP-003..PIP-009) |
| Anticipated artifacts produced by this deliverable | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | `_CONTEXT.md` "Anticipated Artifacts" |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service | Sour produced water / produced water (atmospheric storage) | `_Sources/26020-Package_Requirements.docx` heading 50 |
| Site applicability | 3-25 liquids area and related compressor station scope | Same source, "Location / Status" |
| Operating pressure | Atmospheric | Same source |
| Operating temperature | 10 °C (further design temperatures TBD) | Same source |
| Ambient design temperature | TBD (heading 50 does not restate; analog 4-25 cites -40 / +35 °C but is not the package-50 source) | location TBD |

## Construction

| Item | Value | Source |
|---|---|---|
| Construction code | API 650 (modified atmospheric) | ASSUMPTION — see Attributes row "Design code basis" |
| Tank sizing basis | 3800 bbl nominal capacity per tank, multiple identical tanks per service group | `_Sources/26020-Package_Requirements.docx` heading 50, Item Nos. 1-3 |
| Corrosion allowance / material grade | TBD | location TBD (not in heading 50 slice) |
| Coating / heating / insulation | TBD for package 50 specifically (analog 4-25 entry notes internal coating, external insulation, electric heating, PVRV/EPRV protection, LP fuel gas blanket) | ASSUMPTION — analog only; confirm against package vendor RFQ `Bid Docs/Budgetary/26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx` |
| Interfaces (per Package Interfaces row 93) | Process Piping: Yes; Utility Piping: No; Relief/Flare/Vent: Yes; Drain/Containment: Yes; Electrical Power: No; Area/Exterior Lighting: Yes; EHT: No; Grounding/Bonding: Yes; Cathodic Protection: Yes; I&C/Control Cabling: Yes; Communications/Network: No; HVAC: No; Fire & Gas: No; Maintenance Access: No; Grading/Site Drainage/Spill Containment: Yes; Structural/Foundations/Supports: Yes; Product Loading: No; Pipeline/Pigging: No | `_Sources/26020-Package_Requirements.docx` heading 50, "Physical Interface Summary"; cross-ref `_Sources/26020-Packages_Interfaces_4_export.xlsx` row 93 |

## References

- `_Sources/26020-Package_Requirements.docx` — heading 50 ("26020-03-PT-19-007 - Tanks, Sour Water"), source slice covering Location/Status, Source Basis, Basic Scope, Major Included Equipment, Scope Notes / Open Items, Physical Interface Summary, Vendor Engineering Deliverables.
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — row 93 (interface column M reference).
- Decomposition entry: PKG-098 / DEL-098-06 in `_Decomposition/.../GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`.
- Sibling package deliverables in `PKG-098_Tanks-Sour-Water-API-650-3-25/1_Working/` (DEL-098-01..05) for cross-deliverable acceptance scope.
- ASSUMPTION sources (not yet locally read): `Bid Docs/Budgetary/26020-03-PT-RFQ-19-007 - Sour Water Tanks.docx` (referenced inside heading 50 as Source Basis).
