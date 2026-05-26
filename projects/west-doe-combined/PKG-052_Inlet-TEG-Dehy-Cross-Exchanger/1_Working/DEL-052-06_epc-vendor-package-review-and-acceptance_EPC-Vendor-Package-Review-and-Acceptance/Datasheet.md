# Datasheet — DEL-052-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value | Source |
|---|---|---|
| Deliverable ID | `DEL-052-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` Identity |
| Deliverable Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row DEL-052-06 |
| Type | EPC Vendor Package Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Discipline | Mechanical | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` row PKG-052 |
| Parent Package | `PKG-052` — Inlet / TEG Dehy Cross Exchanger | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Workbook Row | 62 | `PACKAGE_REGISTER.csv` row PKG-052 |
| CoA / Equipment Tag | `26020-01-16-001` (E-5718-1) | `PACKAGE_REGISTER.csv` row PKG-052 |
| Responsible Party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Decomposition Snapshot | GATE-07 Final Published 2026-05-24 (PROJECT_DECOMP) | `_REFERENCES.md` |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Covered SOW IDs | `SOW-0103`, `SOW-0104`, `SOW-0105`, `SOW-0106` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported Objectives | `OBJ-001`, `OBJ-003`–`OBJ-010` (excl. `OBJ-002`) | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` (PACKAGE_HEURISTIC — ASSUMPTION at deliverable-ID level) |
| Acceptance Subject (package under review) | Inlet / TEG DEHY Cross Exchanger E-5718-1; TEMA 'R' BEM; Duty 5514.3 kW (18.82 MMBTU/hr); accompanying piping/instrumentation and skid | `PACKAGE_REGISTER.csv` row PKG-052 (Detailed Mechanical Package Scope) |
| Process Function Context | Cold sour gas from the inlet separator exchanges heat with sweet gas leaving the amine sweetening unit; sour gas then flows to the inlet compressors | `PACKAGE_REGISTER.csv` row PKG-052 |
| Anticipated Artifacts | Vendor document review log; package acceptance checklist; test/inspection evidence; turnover evidence | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Registered Artifact IDs | `ART-F0F5332A58` (Vendor document review and comment log); `ART-21EEB708EC` (Vendor package acceptance and turnover checklist); `ART-7F212499D9` (Factory/shop test and inspection evidence) | `ARTIFACT_REGISTER.csv` rows for DEL-052-06 |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Authority Basis for Review | EPC Scope of Work (DEL-052-01), Package Datasheet (DEL-052-02), Construction Work Package (DEL-052-03) | `_CONTEXT.md` Scope; `DELIVERABLE_REGISTER.csv` |
| Vendor Inputs Reviewed | Vendor Engineered Equipment Package (DEL-052-04); Vendor Document Turnover Package (DEL-052-05) | `DELIVERABLE_REGISTER.csv` rows DEL-052-04 / DEL-052-05 (ASSUMPTION: these are the input streams to review/acceptance) |
| Interface Scope (per workbook) | Process Piping; Utility Piping; Drain / Containment; EHT; Grounding / Bonding; Area / Exterior Lighting; I&C / Control Cabling; Maintenance Access; Structural / Foundations / Supports | `INTERFACE_REGISTER.csv` rows for PKG-052; `PACKAGE_REGISTER.csv` PKG-052 |
| Package-Specific Exclusions | TBD; no package-specific exclusions stated in source materials | `PACKAGE_REGISTER.csv` row PKG-052 |
| Mandatory-Deliverable Flag | Additional Gate 5 EPC review/acceptance deliverable | `DELIVERABLE_REGISTER.csv` notes column |

## Construction (of the Acceptance Record)

The deliverable is documentary: it is constructed by assembling the four artifact streams identified above into a single review/acceptance record set.

| Artifact Stream | Composition (intended contents) | Source for composition |
|---|---|---|
| Vendor document review log | Per-document review record covering vendor submittals against EPC SOW, Package Datasheet, CWP, and source vendor-document requirements | `ARTIFACT_REGISTER.csv` ART-F0F5332A58 |
| Package acceptance & turnover checklist | Integration acceptance checklist confirming readiness for installation, tie-in, and facility turnover | `ARTIFACT_REGISTER.csv` ART-21EEB708EC |
| Factory/shop test & inspection evidence | Vendor-supplied factory/shop test reports and inspection evidence; detailed acceptance criteria are source-specific | `ARTIFACT_REGISTER.csv` ART-7F212499D9 |
| Turnover evidence | Records substantiating handoff readiness from vendor to EPC Integrator and into the facility | `_CONTEXT.md` Anticipated Artifacts; `DELIVERABLE_REGISTER.csv` |

Specific test types, inspection plans, acceptance criteria, and submittal lists are TBD pending access to `26020-Package_Requirements.docx` package heading 7 and to vendor RFQ basis `26020-01-PT-RFQ-16-001-Heat_Ex_ST.docx`.

## References

- `_CONTEXT.md`
- `_REFERENCES.md`
- `_DEPENDENCIES.md`
- `DELIVERABLE_REGISTER.csv` (GATE-07 snapshot) row DEL-052-06
- `PACKAGE_REGISTER.csv` (GATE-07 snapshot) row PKG-052
- `ARTIFACT_REGISTER.csv` (GATE-07 snapshot) rows ART-F0F5332A58, ART-21EEB708EC, ART-7F212499D9
- `INTERFACE_REGISTER.csv` (GATE-07 snapshot) PKG-052 interface rows
- `OBJECTIVE_DELIVERABLE_MAP.csv` (GATE-07 snapshot)
- 26020-Package_Requirements.docx (location TBD for clause text; binary at `_Sources/26020-Package_Requirements.docx`)
- Bid Docs/Budgetary/26020-01-PT-RFQ-16-001-Heat_Ex_ST.docx (location TBD; not present under `_Sources/`)
