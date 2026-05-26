# Datasheet — DEL-061-06 EPC Vendor Package Review and Acceptance

## Identification

| Field | Value |
|---|---|
| DeliverableID | `DEL-061-06_epc-vendor-package-review-and-acceptance` |
| Name | EPC Vendor Package Review and Acceptance |
| ParentPackageID | `PKG-061` |
| PackageName | NGL Booster and Transfer Pumps Building |
| Subject Package | NGL Booster and Transfer Pumps Building (`SourcePath: _Sources/26020-Package_Requirements.docx`, `SectionRef: Heading 17 — NGL Booster and Transfer Pumps Building`; location TBD at clause level — Heading 17 source slice not locally accessible in markdown form) |
| Discipline | Mechanical |
| Type | EPC Vendor Package Acceptance |
| ResponsibleParty | EPC Integrator (lead) with Package Vendor input |
| Decomposition Snapshot | GATE-07_Final_Published_2026-05-24 |

## Attributes

| Attribute | Value | Source |
|---|---|---|
| Deliverable role | Review and acceptance evidence pack for the Package Vendor production unit (`DEL-061-04`) and the Vendor Document Turnover (`DEL-061-05`) against EPC anchor deliverables (`DEL-061-01` SOW, `DEL-061-02` Package Datasheet, `DEL-061-03` Construction Work Package). | `DELIVERABLE_REGISTER.csv` row `DEL-061-06`; `_CONTEXT.md` |
| Acceptance subject | NGL booster and transfer pumps and the housing building scope (rotating equipment plus building/enclosure work). Specific tagged equipment and pump counts: TBD — to be enumerated from `26020-Package_Requirements.docx` Heading 17 "Basic Scope" / "Major Included Equipment" when source slice becomes locally accessible. | `26020-Package_Requirements.docx` Heading 17 (location TBD); decomposition Package name |
| Covered SOW IDs | `SOW-0149`, `SOW-0150`, `SOW-0151`, `SOW-0152` | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Supported Objectives | `OBJ-001`, `OBJ-003`, `OBJ-004`, `OBJ-005`, `OBJ-006`, `OBJ-007`, `OBJ-008`, `OBJ-009`, `OBJ-010` (ASSUMPTION — package-grouping heuristic via the GATE-07 objective-to-deliverable map applied at the `PKG-061` package level). | `OBJECTIVE_DELIVERABLE_MAP.csv`; `_CONTEXT.md` |

## Conditions

| Condition | Value | Source |
|---|---|---|
| Service / location | NGL liquids transfer service housed in a dedicated pumps building. Plot / location detail TBD (location TBD — Heading 17 "Location / Status"). | `26020-Package_Requirements.docx` Heading 17 (location TBD) |
| Building / enclosure condition | Pumps building enclosure provided as part of the package (ASSUMPTION — implied by package name "NGL Booster and Transfer Pumps Building"; building scope details TBD until Heading 17 is locally accessible). | Package name; ASSUMPTION |
| Acceptance trigger states (upstream maturity) | `DEL-061-04` and `DEL-061-05` reach a maturity state acceptable for integration review. (ASSUMPTION — exact gating values TBD; `_DEPENDENCIES.md` declares no upstream edges as of PREPARATION.) | `_DEPENDENCIES.md`; ASSUMPTION |
| Design / operating values (head, flow, NPSH, power, area classification) | TBD — not extracted from `26020-Package_Requirements.docx` Heading 17 in this run (source not locally accessible in markdown form). Numeric values will come from the Package Vendor's submitted pump data sheet (`MEC-007`), NPSH calcs (`PRO-013`), and electrical / area classification submittals. | `26020-Package_Requirements.docx` Heading 17 (location TBD) |

## Construction

| Acceptance Artifact (per `_CONTEXT.md` / decomposition) | Description | Source |
|---|---|---|
| Vendor document review log | Reviewer-by-document register tracking the Vendor Document Index (`PRQ-009`) and each enumerated vendor engineering deliverable for the NGL Booster and Transfer Pumps Building scope. Specific document list TBD until Heading 17 source slice is locally accessible. | `_CONTEXT.md` Anticipated Artifacts; `26020-Package_Requirements.docx` Heading 17 (location TBD) |
| Package acceptance checklist | Pass/fail acceptance matrix mapped to SOW items `SOW-0149..0152`, the Package Datasheet (`DEL-061-02`), and Construction Work Package (`DEL-061-03`). | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` |
| Test / inspection evidence | Aggregated Material Test Reports / Certificates (`QLT-013`), ITP execution records against `QLT-003`, Inspection Release Certificate (`QLT-020`), FAT records (`MEC-022`, `ELE-030`). (ASSUMPTION — typical artifact codes for rotating equipment plus building scope; precise artifact set TBD until Heading 17 is locally accessible.) | ASSUMPTION; convention from PKG-054 Heading 9 sibling evidence pattern |
| Turnover evidence | Manufacturing Record Book / Vendor Data Book (`QLT-021`, `MEC-023`, `PRQ-016`), Hydrotest / Pressure Test Packages (`PIP-024`) for any piping in package, and SPIR (`PRQ-015`). (ASSUMPTION — exact set TBD until Heading 17 vendor deliverables list is accessible.) | ASSUMPTION |
| Physical-interface acceptance coverage | Interface set marked `Yes` for the NGL Booster and Transfer Pumps Building row in the Heading 17 Physical Interface Summary. Specific interfaces TBD — see `_Sources/26020-Packages_Interfaces_4_export.xlsx` package row 75 (location TBD at column level). | `26020-Package_Requirements.docx` Heading 17 "Physical Interface Summary" (location TBD); `26020-Packages_Interfaces_4_export.xlsx` row 75 |

## References

- `_Sources/26020-Package_Requirements.docx` — Heading 17, "NGL Booster and Transfer Pumps Building" (location TBD at clause level; source slice not locally accessible in markdown during this run)
- `_Sources/26020-Packages_Interfaces_4_export.xlsx` — package row 75 (interface evidence, location TBD at column level)
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/DELIVERABLE_REGISTER.csv`
- `_Decomposition/PROJECT_DECOMP/_GateSnapshots/GATE-07_Final_Published_2026-05-24/OBJECTIVE_DELIVERABLE_MAP.csv`
- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md`
