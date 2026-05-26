# Datasheet: DEL-066-06 — EPC Vendor Package Review and Acceptance (PKG-066 Tanks, Condensate API 650, 4-25)

> Descriptive datasheet identifying the EPC Integrator review-and-acceptance deliverable for the PKG-066 Condensate Storage Tanks package (4-25 Deepcut tank farm). All non-trivial values cite the source slice in `_REFERENCES.md`. Items not found in the locally accessible sources are marked `TBD`.

## Identification

| Field | Value | Source |
|---|---|---|
| DeliverableID | `DEL-066-06_epc-vendor-package-review-and-acceptance` | `_CONTEXT.md` |
| Deliverable Name | EPC Vendor Package Review and Acceptance | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 503 |
| Parent Package | `PKG-066` — Tanks, Condendate (API 650) 4-25 | `_CONTEXT.md`; `PACKAGE_REGISTER.csv` |
| Workbook Packages row | 89 (sourced) / 90 (per Deepcut DBM register) — see Conflict (Guidance.md) | `_CONTEXT.md`; `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2625 |
| Discipline | Mechanical | `_CONTEXT.md` |
| Type | EPC Vendor Package Acceptance | `_CONTEXT.md` |
| Responsible Party | EPC Integrator (lead) with Package Vendor input | `_CONTEXT.md` |
| Decomposition snapshot | `GATE-07_Final_Published_2026-05-24` | `_REFERENCES.md` |

## Attributes (Subject Package Under Review)

| Attribute | Value | Source |
|---|---|---|
| Package title (workbook) | Tanks, Condendate (API 650) 2 — Condensate Storage Tanks | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2625 |
| Package source heading | `26020-01-PT-19-004 - Tanks, Condensate` (4-25 West Doe Deepcut tank farm) | `26020-Package_Requirements.docx` heading at line 5004 (extracted text) |
| Plant location | 4-25 West Doe Deepcut tank farm | `26020-Package_Requirements.docx` line 5006 |
| Major tagged equipment | TK-9110-1, TK-9120-1, TK-9130-1, TK-9140-1, TK-9150-1 (5 tanks) | `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` line 2625 |
| Service | C5+ on-spec condensate product storage | `26020-Package_Requirements.docx` line 5010; `4-25_Deepcut_DBM.md` line 1633 |
| Design basis (tank) | Modified API 650 atmospheric tank; 16 oz test pressure | `4-25_Deepcut_DBM.md` lines 518, 1646-1647 |
| Maximum fill | 90% of tank volume (shutdown limit); thermal expansion review required | `4-25_Deepcut_DBM.md` lines 519, 1648 |
| Blanket gas basis | API 2000 (winter vacuum prevention) | `4-25_Deepcut_DBM.md` lines 520, 1663 |
| Storage capacity (local 4-25) | 4 x 3,800 bbl (DBM); register lists 5 tanks (TK-9110-1…-9150-1) — see Conflict (Guidance.md) | `4-25_Deepcut_DBM.md` lines 1639, 2625 |
| Local storage duration | ~4.5 days for liquids-hub upset | `4-25_Deepcut_DBM.md` line 1640 |
| Tank insulation | Product tanks non-insulated (recycle may be needed for winter temperature); slop tank fully insulated | `4-25_Deepcut_DBM.md` lines 1644-1645 |
| Design SG (product) | 1.0 | `4-25_Deepcut_DBM.md` line 1642 |
| Design SG (slop) | 1.00 (TBC) | `4-25_Deepcut_DBM.md` line 1643 |

## Conditions (Review Scope)

| Condition | Value | Source |
|---|---|---|
| Scope of review | Vendor package documentation, integration acceptance, and handoff readiness against EPC SoW, Package Datasheet, and CWP | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 503 |
| Acceptance basis documents | DEL-066-01 SoW; DEL-066-02 Package Datasheet; DEL-066-03 Construction Work Package; DEL-066-04 Vendor Engineered Equipment Package; DEL-066-05 Vendor Document Turnover Package | `_CONTEXT.md`; sibling deliverable IDs in `DELIVERABLE_REGISTER.csv` |
| Covered SoW items | SOW-0205, SOW-0206, SOW-0207, SOW-0208 | `_CONTEXT.md` |
| Supported objectives | OBJ-001, OBJ-003, OBJ-004, OBJ-005, OBJ-006, OBJ-007, OBJ-008, OBJ-009, OBJ-010 — package-grouping heuristic (ASSUMPTION) | `_CONTEXT.md`; `OBJECTIVE_DELIVERABLE_MAP.csv` rows 246-1706 |
| Vendor-engineered scope | Condensate product storage tanks with blanket gas, PVRV/EPRV protection, VRU header connection, grounding/cathodic protection, instrumentation, standard tank appurtenances | `26020-Package_Requirements.docx` line 5012 |

## Construction / Artifact Composition

Anticipated artifacts that constitute the review-and-acceptance evidence set:

| Artifact | Purpose | Source |
|---|---|---|
| Vendor document review log | Tracks each vendor document submission, EPC review status, and acceptance disposition | `_CONTEXT.md` |
| Package acceptance checklist | Pass/fail acceptance criteria mapped to EPC SoW, Package Datasheet, and CWP | `_CONTEXT.md`; `DELIVERABLE_REGISTER.csv` row 503 |
| Test / inspection evidence | ITP execution records, MTRs, NDE reports, FAT records | `26020-Package_Requirements.docx` lines 5068-5070, 5099-5101 (referenced vendor deliverables) |
| Turnover evidence | Manufacturing Record Book / Vendor Data Book, Inspection Release Certificate, IOM Manual | `26020-Package_Requirements.docx` lines 5072-5074, 5102-5107 |

## Interface Applicability (from package interface summary)

Interfaces declared applicable for this package (used as review-scope coverage list):

| Interface Type | Applicability | Source |
|---|---|---|
| Process Piping | Yes | `26020-Package_Requirements.docx` lines 5019-5020 |
| Relief / Flare / Vent | Yes | line 5023-5024 |
| Drain / Containment | Yes | line 5025-5026 |
| Area / Exterior Lighting | Yes | line 5029-5030 |
| Grounding / Bonding | Yes | line 5034-5035 |
| Cathodic Protection | Yes | line 5036-5037 |
| I&C / Control Cabling | Yes | line 5038-5039 |
| Grading / Site Drainage / Spill Containment | Yes | line 5048-5049 |
| Structural / Foundations / Supports | Yes | line 5050-5051 |
| Utility Piping | No | line 5021-5022 |
| Electrical Power | No | line 5027-5028 |
| EHT | No | line 5032-5033 |
| Communications / Network | No | line 5040-5041 |
| Building HVAC / Services | No | line 5042-5043 |
| Fire & Gas / Safety Systems | No | line 5044-5045 |
| Maintenance Access | No | line 5046-5047 |
| Product Loading | No | line 5052-5053 |
| Pipeline / Pigging | No | line 5054-5055 |

## References

- `_CONTEXT.md`, `_REFERENCES.md`, `_DEPENDENCIES.md` (deliverable-local)
- `_Sources/DBM-Deepcut/4-25_Deepcut_DBM.md` (Design Basis Memorandum, Deepcut 4-25)
- `_Sources/26020-Package_Requirements.docx`, package heading at line 5004 (`26020-01-PT-19-004 - Tanks, Condensate`, 4-25)
- Gate 7 snapshot registers: `DELIVERABLE_REGISTER.csv` row 503; `OBJECTIVE_DELIVERABLE_MAP.csv` rows 246, 715, 1165, 1707 et seq.; `OBJECTIVE_SCOPE_MAP.csv` rows 127-130 (PKG-066 SoW items)
- Sibling deliverables in PKG-066: DEL-066-01 (SoW), DEL-066-02 (Datasheet), DEL-066-03 (CWP), DEL-066-04 (Vendor Eng. Pkg), DEL-066-05 (Vendor Document Turnover)
